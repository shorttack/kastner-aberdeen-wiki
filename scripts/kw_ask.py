#!/usr/bin/env python3
"""kw_ask.py v3 — chatbox over the Kastner Aberdeen Wiki via bge-m3 RAG.

v3 changes:
  - `--cloud` flag is now a stub: prints a clear error directing the user to
    `--model qwen3.5:35b-mlx` instead. No more `FileNotFoundError: pplx` traceback.
  - Cloud synthesis is reserved for a future release when an API-key-backed
    provider is wired in (Anthropic, Perplexity Sonar API, OpenAI, or Gemini).

v2 changes:
  - Disable model "thinking" via Ollama's `think: false` (qwen3.5 emits
    long <think>...</think> blocks otherwise, eating the entire token budget)
  - Belt-and-suspenders: strip any <think>...</think> blocks from output
  - Bump num_predict to 2000 by default (synthesis answers can be long)
  - Show explicit error message if Ollama returns empty response

Workflow:
  1. Embed your question with bge-m3 via local Ollama
  2. Cosine-similarity match against data/embeddings.parquet
  3. Load the top-k page contents, build a context bundle
  4. Send to local LLM (qwen3.5:27b-mlx by default) for synthesis
  5. Stream the response, show sources at the end
"""
import argparse
import os
import sys
import re
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
PAGE_CHARS = 2000

THINK_RE = re.compile(r"<think>.*?</think>\s*", flags=re.DOTALL | re.IGNORECASE)


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


def retrieve(query: str, k: int = 6, page_type: str | None = None):
    qv = embed_query(query)
    df = duckdb.sql(
        f"SELECT page_path, slug, title, page_type, vector "
        f"FROM '{EMB_PARQUET}' "
        f"WHERE vector IS NOT NULL"
    ).df()
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
    if txt.startswith("---\n"):
        end = txt.find("\n---\n", 4)
        if end > 0:
            txt = txt[end + 5 :]
    return txt[:char_budget].strip()


def build_prompt(question: str, hits) -> str:
    chunks = []
    for i, (_, h) in enumerate(hits.iterrows(), 1):
        body = load_page_content(h["page_path"])
        if not body:
            continue
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

Be direct. Do not deliberate. Start your answer with the conclusion.

QUESTION: {question}

SOURCE PAGES:
{context}

ANSWER (be specific, cite slugs, ~250-400 words):"""


class ThinkStripper:
    """Stream filter that removes <think>...</think> blocks token-by-token."""
    def __init__(self):
        self.buf = ""
        self.in_think = False

    def feed(self, chunk: str) -> str:
        out = []
        self.buf += chunk
        while self.buf:
            if self.in_think:
                end = self.buf.find("</think>")
                if end < 0:
                    self.buf = ""  # consume but don't emit
                    return ""
                self.buf = self.buf[end + len("</think>"):]
                self.in_think = False
                # Skip leading whitespace after </think>
                self.buf = self.buf.lstrip()
                continue
            start = self.buf.find("<think>")
            if start < 0:
                # No <think> tag in buffer — emit everything we can
                # but hold back last 8 chars in case "<think>" is being assembled
                if len(self.buf) <= 8:
                    return "".join(out)
                emit = self.buf[:-8]
                self.buf = self.buf[-8:]
                out.append(emit)
                return "".join(out)
            # Emit text before <think>, then enter think mode
            if start > 0:
                out.append(self.buf[:start])
            self.buf = self.buf[start + len("<think>"):]
            self.in_think = True
        return "".join(out)

    def flush(self) -> str:
        if self.in_think:
            return ""
        return self.buf


def synthesize_local(prompt: str, model: str, stream: bool, temperature: float, max_tokens: int) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
        "think": False,  # disable qwen3.5 reasoning blocks
        "options": {
            "temperature": temperature,
            "num_ctx": 16384,
            "num_predict": max_tokens,
        },
        "keep_alive": "30m",
    }
    if stream:
        full = []
        stripper = ThinkStripper()
        with requests.post(
            f"{OLLAMA_URL}/api/generate", json=payload, stream=True, timeout=600
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if not line:
                    continue
                obj = json.loads(line)
                if "error" in obj:
                    print(f"\n[ollama error] {obj['error']}", file=sys.stderr)
                    sys.exit(1)
                tok = obj.get("response", "")
                if tok:
                    visible = stripper.feed(tok)
                    if visible:
                        print(visible, end="", flush=True)
                        full.append(visible)
                if obj.get("done"):
                    tail = stripper.flush()
                    if tail:
                        print(tail, end="", flush=True)
                        full.append(tail)
                    break
        print()
        out = "".join(full).strip()
        if not out:
            print("[kw] WARNING: model returned no visible content. "
                  "Try --model qwen3.5:35b-mlx or --cloud.", file=sys.stderr)
        return out
    else:
        r = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=600)
        r.raise_for_status()
        ans = r.json().get("response", "")
        ans = THINK_RE.sub("", ans).strip()
        if not ans:
            print("[kw] WARNING: model returned no visible content.", file=sys.stderr)
        else:
            print(ans)
        return ans


def synthesize_cloud(prompt: str, stream: bool) -> str:
    """Stub. Cloud synthesis is not currently wired to any provider.

    Previous v1/v2 shelled out to an internal `pplx` CLI that isn't
    distributable. To re-enable cloud synthesis in a future release, wire
    one of: Anthropic (ANTHROPIC_API_KEY), Perplexity Sonar API (PPLX_API_KEY),
    OpenAI (OPENAI_API_KEY), or Gemini (GEMINI_API_KEY). All require a
    paid/metered key the user must obtain themselves.
    """
    print(
        "[kw] --cloud is not currently available. Cloud synthesis requires a\n"
        "     paid API key (Anthropic, Perplexity Sonar API, OpenAI, or Gemini)\n"
        "     that this build doesn't have wired in. For now, use the local\n"
        "     models which are production-grade for this archive:\n\n"
        "       kw ask \"...\"                              # qwen3.5:27b-mlx (default)\n"
        "       kw ask \"...\" --model qwen3.5:35b-mlx     # bigger, slower, smarter\n",
        file=sys.stderr,
    )
    sys.exit(2)


def main():
    p = argparse.ArgumentParser(prog="kw ask", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("question", nargs="+")
    p.add_argument("--k", type=int, default=6)
    p.add_argument("--model", default=DEFAULT_LLM)
    p.add_argument("--cloud", action="store_true")
    p.add_argument("--no-stream", action="store_true")
    p.add_argument("--type", help="Restrict retrieval to one page type")
    p.add_argument("--no-llm", action="store_true")
    p.add_argument("--temperature", type=float, default=0.3)
    p.add_argument("--max-tokens", type=int, default=2000)
    p.add_argument("--show-think", action="store_true",
                   help="Don't strip <think> blocks (debugging)")
    args = p.parse_args()

    question = " ".join(args.question).strip()
    if not question:
        p.error("question is empty")

    if not EMB_PARQUET.exists():
        print(f"ERROR: {EMB_PARQUET} not found.", file=sys.stderr)
        sys.exit(1)

    t0 = time.time()
    print(f"[kw] retrieving k={args.k} pages for: {question!r}", file=sys.stderr)
    hits = retrieve(question, k=args.k, page_type=args.type)
    t_ret = time.time() - t0
    print(f"[kw] retrieved {len(hits)} hits in {t_ret:.2f}s", file=sys.stderr)

    if len(hits) == 0:
        print("No matches found.", file=sys.stderr)
        sys.exit(1)

    if args.no_llm:
        print()
        for _, h in hits.iterrows():
            print(f"  {h['score']:.3f}  {h['page_type']:12s}  {h['slug']}")
            print(f"          {h['title']}")
            print(f"          {h['page_path']}")
        return

    prompt = build_prompt(question, hits)
    print(f"[kw] synthesizing with {'Claude (cloud)' if args.cloud else args.model}...",
          file=sys.stderr)
    print()

    # Optionally bypass strip for debugging
    if args.show_think:
        global THINK_RE
        THINK_RE = re.compile(r"(?!a)a")  # never matches

    if args.cloud:
        synthesize_cloud(prompt, stream=not args.no_stream)
    else:
        synthesize_local(
            prompt, args.model, stream=not args.no_stream,
            temperature=args.temperature, max_tokens=args.max_tokens,
        )

    print("\n--- Sources ---", file=sys.stderr)
    for _, h in hits.iterrows():
        print(f"  [{h['score']:.3f}] {h['slug']:50s}  ({h['page_type']})", file=sys.stderr)


if __name__ == "__main__":
    main()
