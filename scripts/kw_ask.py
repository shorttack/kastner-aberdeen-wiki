#!/usr/bin/env python3
"""kw ask — RAG over the Kastner Aberdeen Wiki.

v6 changes (2026-05-28, post-reembed):
  * Schema fix: read the parquet columns reembed.py actually writes —
    page_path, page_type, slug, title, tier, vector. v4/v5 read stale
    column names (path, embedding) and crashed after rebuild-embeddings.
  * Drop the frontmatter-reparse path: page_type is now a real column
    in the parquet, so we don't need to read 10k .md files to derive it.
    Retrieval is ~10x faster as a side effect.
  * --no-notes / --only-notes / --type filters work on the parquet
    column directly (set-membership in SQL would also work, but pandas
    filter is fine for 10k rows).

Behaviour identical to v5 from the user's perspective.
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import duckdb
import numpy as np
import requests

ROOT = Path(__file__).resolve().parents[1]
EMB_PARQUET = ROOT / "data" / "embeddings.parquet"
WIKI_ROOT = ROOT / "wiki"

DEFAULT_EMBED_MODEL = "bge-m3"
DEFAULT_LLM = "qwen3.5:27b-mlx"
OLLAMA_HOST = "http://localhost:11434"
PAGE_CHARS = 4000


def embed_query(q: str) -> np.ndarray:
    r = requests.post(
        f"{OLLAMA_HOST}/api/embeddings",
        json={"model": DEFAULT_EMBED_MODEL, "prompt": q},
        timeout=60,
    )
    r.raise_for_status()
    v = np.array(r.json()["embedding"], dtype=np.float32)
    n = np.linalg.norm(v) + 1e-9
    return v / n


def retrieve(
    query: str,
    k: int = 6,
    page_type: str | None = None,
    exclude_types: set[str] | None = None,
    include_types: set[str] | None = None,
):
    """Top-k retrieval with optional page_type filters.

    Parquet schema (written by scripts/reembed.py):
      page_path: str, page_type: str, slug: str, title: str,
      tier: int32, vector: list<float32>
    """
    qv = embed_query(query)
    df = duckdb.sql(
        f"SELECT page_path, page_type, slug, title, vector "
        f"FROM '{EMB_PARQUET}' "
        f"WHERE vector IS NOT NULL"
    ).df()
    if len(df) == 0:
        return df

    if include_types:
        df = df[df["page_type"].isin(include_types)].reset_index(drop=True)
    elif exclude_types:
        df = df[~df["page_type"].isin(exclude_types)].reset_index(drop=True)
    elif page_type:
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
            txt = txt[end + 5:]
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
using ONLY the sources below. Cite each source by its slug in square
brackets, e.g. [as400]. If the sources don't answer the question, say so.

QUESTION: {question}

SOURCES:
{context}

ANSWER:"""


_THINK_OPEN_RE = re.compile(r"<think>", re.IGNORECASE)
_THINK_CLOSE_RE = re.compile(r"</think>", re.IGNORECASE)


def _strip_think_stream(tokens, show_think: bool = False):
    """Stream filter that removes <think>...</think> blocks."""
    buf = ""
    in_think = False
    for tok in tokens:
        buf += tok
        while True:
            if in_think:
                m = _THINK_CLOSE_RE.search(buf)
                if not m:
                    if show_think:
                        yield buf
                    buf = ""
                    break
                if show_think:
                    yield buf[: m.end()]
                buf = buf[m.end():]
                in_think = False
            else:
                m = _THINK_OPEN_RE.search(buf)
                if not m:
                    yield buf
                    buf = ""
                    break
                yield buf[: m.start()]
                buf = buf[m.start():]
                in_think = True
                close = _THINK_CLOSE_RE.search(buf)
                if close:
                    if show_think:
                        yield buf[: close.end()]
                    buf = buf[close.end():]
                    in_think = False
                else:
                    break
    if buf and not in_think:
        yield buf


def stream_ollama(prompt: str, model: str, temperature: float, max_tokens: int,
                  show_think: bool = False):
    r = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        },
        stream=True,
        timeout=600,
    )
    r.raise_for_status()

    def raw_tokens():
        for line in r.iter_lines():
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            tok = obj.get("response", "")
            if tok:
                yield tok
            if obj.get("done"):
                break

    for piece in _strip_think_stream(raw_tokens(), show_think=show_think):
        if piece:
            sys.stdout.write(piece)
            sys.stdout.flush()
    sys.stdout.write("\n")


def call_cloud(prompt: str) -> None:
    proc = subprocess.run(
        ["pplx", "ask", prompt],
        capture_output=True,
        text=True,
        timeout=600,
    )
    if proc.returncode != 0:
        sys.stderr.write(f"[kw ask --cloud] pplx ask failed: {proc.stderr}\n")
        sys.exit(2)
    sys.stdout.write(proc.stdout)
    if not proc.stdout.endswith("\n"):
        sys.stdout.write("\n")


def main():
    p = argparse.ArgumentParser(
        prog="kw ask",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("question", nargs="+")
    p.add_argument("--k", type=int, default=6)
    p.add_argument("--model", default=DEFAULT_LLM)
    p.add_argument("--cloud", action="store_true")
    p.add_argument("--no-stream", action="store_true")
    p.add_argument("--no-llm", action="store_true")
    p.add_argument("--temperature", type=float, default=0.3)
    p.add_argument("--max-tokens", type=int, default=2000)
    p.add_argument("--show-think", action="store_true",
                   help="Show <think> chain-of-thought (qwen3 only)")

    filt = p.add_mutually_exclusive_group()
    filt.add_argument("--type",
                      help="Restrict retrieval to one page type "
                           "(study|entity|technology|theme|chapter|note|...)")
    filt.add_argument("--no-notes", action="store_true",
                      help="Exclude notes — pure archive research mode")
    filt.add_argument("--only-notes", action="store_true",
                      help="Restrict to notes — interpretive layer only")

    args = p.parse_args()
    question = " ".join(args.question)

    t0 = time.time()
    page_type = args.type
    exclude_types = {"note"} if args.no_notes else None
    include_types = {"note"} if args.only_notes else None

    hits = retrieve(
        question,
        k=args.k,
        page_type=page_type,
        exclude_types=exclude_types,
        include_types=include_types,
    )
    t_ret = time.time() - t0

    if len(hits) == 0:
        sys.stderr.write("[kw ask] no hits (check filters)\n")
        sys.exit(1)

    if args.no_llm:
        for _, h in hits.iterrows():
            print(f"  {h['score']:.3f}  {h['page_type']:12s}  {h['slug']}")
        sys.stderr.write(f"[kw ask] retrieve: {t_ret*1000:.0f} ms\n")
        return

    prompt = build_prompt(question, hits)
    sys.stderr.write(f"[kw ask] retrieve: {t_ret*1000:.0f} ms — synthesizing…\n")

    if args.cloud:
        call_cloud(prompt)
    else:
        stream_ollama(
            prompt,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            show_think=args.show_think,
        )

    sys.stderr.write("\n--- Sources ---\n")
    for _, h in hits.iterrows():
        sys.stderr.write(
            f"{h['score']:.3f}  {h['slug']:48s}  {h['page_type']}\n"
        )

    mode = "all"
    if args.no_notes:
        mode = "no-notes (pure archive)"
    elif args.only_notes:
        mode = "only-notes (interpretive)"
    elif args.type:
        mode = f"type={args.type}"
    sys.stderr.write(f"[kw ask] filter: {mode}, k={args.k}, model={args.model}\n")


if __name__ == "__main__":
    main()
