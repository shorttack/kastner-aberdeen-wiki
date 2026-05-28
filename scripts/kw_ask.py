#!/usr/bin/env python3
"""kw ask — RAG over the Kastner Aberdeen Wiki.

v5 changes (2026-05-28):
  * --no-notes : exclude page_type == "note" from retrieval (pure archive mode)
  * --only-notes : restrict to notes only (interpretive layer mode)
  * --type still works exactly as before (single page_type match)
  * --no-notes and --only-notes are mutually exclusive with each other and
    with --type; argparse enforces.

Default behaviour is unchanged: all page types are searched, including notes
once kw_note has started creating them. This means the corpus grows smarter
every time Pete saves a note.

Filter precedence at retrieval time:
  --type X       →  page_type == X
  --only-notes   →  page_type == "note"
  --no-notes     →  page_type != "note"
  (none)         →  no filter

Schema note: the embeddings parquet already carries page_type (written by
reembed.py from each page's YAML frontmatter), so no re-embed is required to
enable these flags.
"""
from __future__ import annotations
import argparse
import json
import os
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

# Top-level dir under wiki/ maps to page_type for pages that lack
# explicit frontmatter page_type (mostly root index files).
_DIR_TO_PTYPE = {
    "studies": "study",
    "entities": "entity",
    "technologies": "technology",
    "themes": "theme",
    "collections": "collection",
    "decades": "decade",
    "volume-1": "chapter",
    "notes": "note",          # v5: kw_note writes here
}

_meta_cache: dict[str, tuple[str, str]] = {}

_FM_TITLE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.MULTILINE)
_FM_PTYPE_RE = re.compile(r'^page_type:\s*"?(.*?)"?\s*$', re.MULTILINE)


def _derive_page_type_from_path(page_path: str) -> str:
    parts = Path(page_path).parts
    # page_path is relative to ROOT, like "wiki/notes/foo.md"
    if len(parts) >= 2 and parts[0] == "wiki":
        return _DIR_TO_PTYPE.get(parts[1], "unknown")
    return "unknown"


def _page_meta(page_path: str) -> tuple[str, str]:
    if page_path in _meta_cache:
        return _meta_cache[page_path]
    full = ROOT / page_path
    title = Path(page_path).stem
    ptype = _derive_page_type_from_path(page_path)
    if full.exists():
        try:
            head = full.read_text(encoding="utf-8", errors="replace")[:2000]
            if head.startswith("---"):
                end = head.find("\n---\n", 4)
                if end > 0:
                    front = head[3:end]
                    m = _FM_TITLE_RE.search(front)
                    if m:
                        title = m.group(1).strip()
                    m = _FM_PTYPE_RE.search(front)
                    if m:
                        ptype = m.group(1).strip()
        except Exception:
            pass
    _meta_cache[page_path] = (title, ptype)
    return title, ptype


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

    Precedence (argparse enforces mutual exclusion at CLI layer):
      include_types takes priority over exclude_types takes priority over
      page_type. Inside this function we just apply whatever is non-None.
    """
    qv = embed_query(query)
    df = duckdb.sql(
        f"SELECT path AS page_path, slug, embedding AS vector "
        f"FROM '{EMB_PARQUET}' "
        f"WHERE embedding IS NOT NULL"
    ).df()
    if len(df) == 0:
        return df

    meta = df["page_path"].apply(_page_meta)
    df["title"] = meta.apply(lambda t: t[0])
    df["page_type"] = meta.apply(lambda t: t[1])

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
    """Stream filter that removes <think>...</think> blocks token-by-token."""
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
                if not show_think:
                    # drop everything until </think>
                    pass
                else:
                    yield ""  # placeholder
                # try to find close in remaining buf
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
    """Defer to `pplx ask` for cloud synthesis."""
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

    # Mutually exclusive page_type filters (v5)
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

    # Sources block (to stderr so it doesn't pollute pipes into kw_note)
    sys.stderr.write("\n--- Sources ---\n")
    for _, h in hits.iterrows():
        sys.stderr.write(
            f"{h['score']:.3f}  {h['slug']:48s}  {h['page_type']}\n"
        )

    # v5: filter banner so the user always sees provenance mode
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
