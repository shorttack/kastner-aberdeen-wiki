#!/usr/bin/env python3
"""kw_ask.py — chatbox over the Kastner Aberdeen Wiki via bge-m3 RAG.

Workflow:
  1. Embed your question with bge-m3 via local Ollama
  2. Cosine-similarity match against data/embeddings.parquet (10,299 pages)
  3. Load the top-k page contents, build a context bundle
  4. Send to local LLM (qwen3.5:27b-mlx by default) for synthesis
  5. Stream the response, show sources at the end

Usage:
  kw ask "what did Aberdeen get right about cloud computing?"
  kw ask "agentic AI in enterprise" --k 10
  kw ask "Intel manufacturing strategy" --model qwen3.5:35b-mlx
  kw ask "ATM vs Ethernet 1995-1998" --cloud         # route to Claude via pplx
  kw ask "rural broadband BEAD economics" --no-stream

Flags:
  --k N            Number of source pages to retrieve (default: 6)
  --model NAME     Ollama model for synthesis (default: qwen3.5:27b-mlx)
  --cloud          Use Claude Sonnet via `pplx ask` instead of local LLM
  --no-stream      Wait for full response, don't stream tokens
  --type TYPE      Restrict retrieval to one page_type (study, entity, technology, theme, ...)
  --no-llm         Just show the retrieval hits, skip synthesis (semantic search only)
  --temperature F  LLM temperature (default: 0.3)
  --max-tokens N   Max tokens in response (default: 1200)
"""
import argparse
import os
import sys
import json
import subprocess
import time
from pathlib import Path

import requests
import duckdb
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EMB_PARQUET = ROOT / "data" / "embeddings.parquet"
WIKI_ROOT = ROOT / "wiki"

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"
DEFAULT_LLM = "qwen3.5:27b-mlx"
PAGE_CHARS = 2000  # per-page context budget


def embed_query(text: str) -> np.ndarray:
    r = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=60,
    )
    r.raise_for_status()
    v = np.array(r.json()["embedding"], dtype=np.float32)
    v /= np.linalg.norm(v) + 1e-9
    return v


def _derive_type(path: str) -> str:
    parts = path.split("/")
    folder = parts[-2] if len(parts) >= 2 else ""
    return {
        "entities": "entity",
        "studies": "study",
        "technologies": "technology",
        "codes": "code",
        "collections": "collection",
        "decades": "decade",
        "themes": "theme",
        "volume-1": "volume-1",
        "bases": "base",
    }.get(folder, folder or "unknown")


def retrieve(query: str, k: int = 6, page_type: str | None = None):
    qv = embed_query(query)
    df = duckdb.sql(
        f"SELECT page_path, slug, title, page_type, vector "
        f"FROM '{EMB_PARQUET}' "
        f"WHERE vector IS NOT NULL"
    ).df()
    # Some old embedding files used 'path'/'embedding'; this build uses 'page_path'/'vector'
    if page_type:
        df = df[df["page_type"] == page_type].reset_index(drop=True)
    if len(df) == 0:
        return df
    vecs = np.stack(df["vector"].apply(np.array).values).astype(np.float32)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9
    vecs = vecs / norms
    sims = vecs @ qv
    top = np.argsort(-sims)[:k]
    out = df.iloc[top][["slug", "title", "page_type", "page_path"]].copy()
    out["score"] = sims[top]
    return out


def load_page_content(page_path: str, char_budget: int = PAGE_CHARS) -> str:
    full = ROOT / page_path
    if not full.exists():
        return ""
    txt = full.read_text(encoding="utf-8", errors="replace")
    # Strip frontmatter for the LLM (it's noise for synthesis)
    if txt.startswith("---\n"):
        end = txt.find("\n---\n", 4)
        if end > 0:
            txt = txt[end + 5 :]
    return txt[:char_budget].strip()


def build_prompt(question: str, hits) -> str:
    chunks = []
    for i, (_, h) in enumerate(hits.iterrows(), 1):
        body = load_page_content(h["page_path"])
        chunks.append(
            f"[{i}] {h['title']} ({h['page_type']}, slug={h['slug']}, "
            f"sim={h['score']:.3f})\n{body}"
        )
    context = "\n\n---\n\n".join(chunks)
    return f"""You are a research assistant for the Kastner Aberdeen Wiki — a 1990–2026
archive of Aberdeen Group technology research. Answer the user's question
using ONLY the source pages below. Cite sources by slug in square brackets,
e.g. [intel-corporation-longitudinal]. If the sources don't contain a
reliable answer, say so plainly — do not speculate.

QUESTION: {question}

SOURCE PAGES:
{context}

ANSWER (be specific, cite slugs, ~250-400 words):"""


def synthesize_local(prompt: str, model: str, stream: bool, temperature: float, max_tokens: int) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
        "options": {
            "temperature": temperature,
            "num_ctx": 16384,
            "num_predict": max_tokens,
        },
        "keep_alive": "30m",
    }
    if stream:
        full = []
        with requests.post(
            f"{OLLAMA_URL}/api/generate", json=payload, stream=True, timeout=600
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if not line:
                    continue
                obj = json.loads(line)
                tok = obj.get("response", "")
                if tok:
                    print(tok, end="", flush=True)
                    full.append(tok)
                if obj.get("done"):
                    break
        print()
        return "".join(full)
    else:
        r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=600)
        r.raise_for_status()
        ans = r.json().get("response", "")
        print(ans)
        return ans


def synthesize_cloud(prompt: str, stream: bool) -> str:
    """Route to Claude Sonnet via `pplx ask`. Requires pplx CLI on PATH."""
    cmd = ["pplx", "ask", "--model", "claude_sonnet_4_6"]
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        print(f"[pplx] error: {proc.stderr}", file=sys.stderr)
        sys.exit(1)
    print(proc.stdout)
    return proc.stdout


def main():
    p = argparse.ArgumentParser(prog="kw ask", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("question", nargs="+", help="Your question (will be joined)")
    p.add_argument("--k", type=int, default=6, help="Number of source pages (default 6)")
    p.add_argument("--model", default=DEFAULT_LLM, help="Ollama model for synthesis")
    p.add_argument("--cloud", action="store_true", help="Use Claude via pplx ask")
    p.add_argument("--no-stream", action="store_true", help="Don't stream tokens")
    p.add_argument("--type", help="Restrict retrieval to one page type")
    p.add_argument("--no-llm", action="store_true", help="Just show retrieval hits")
    p.add_argument("--temperature", type=float, default=0.3)
    p.add_argument("--max-tokens", type=int, default=1200)
    args = p.parse_args()

    question = " ".join(args.question).strip()
    if not question:
        p.error("question is empty")

    # Sanity checks
    if not EMB_PARQUET.exists():
        print(f"ERROR: {EMB_PARQUET} not found. Run scripts/reembed.py first.", file=sys.stderr)
        sys.exit(1)

    t0 = time.time()
    print(f"[kw] retrieving k={args.k} pages for: {question!r}", file=sys.stderr)
    hits = retrieve(question, k=args.k, page_type=args.type)
    t_ret = time.time() - t0
    print(f"[kw] retrieved {len(hits)} hits in {t_ret:.2f}s", file=sys.stderr)

    if len(hits) == 0:
        print("No matches found. Check page_type filter or vault state.", file=sys.stderr)
        sys.exit(1)

    if args.no_llm:
        print()
        for _, h in hits.iterrows():
            print(f"  {h['score']:.3f}  {h['page_type']:12s}  {h['slug']}")
            print(f"          {h['title']}")
            print(f"          {h['page_path']}")
        return

    prompt = build_prompt(question, hits)
    print(f"[kw] synthesizing with {'Claude (cloud)' if args.cloud else args.model}...", file=sys.stderr)
    print()

    if args.cloud:
        synthesize_cloud(prompt, stream=not args.no_stream)
    else:
        synthesize_local(
            prompt, args.model, stream=not args.no_stream,
            temperature=args.temperature, max_tokens=args.max_tokens,
        )

    # Sources footer
    print("\n--- Sources ---", file=sys.stderr)
    for _, h in hits.iterrows():
        print(f"  [{h['score']:.3f}] {h['slug']:50s}  ({h['page_type']})", file=sys.stderr)


if __name__ == "__main__":
    main()
