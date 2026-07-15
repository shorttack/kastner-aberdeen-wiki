#!/usr/bin/env python3
"""kw ask — RAG over the Kastner Aberdeen Wiki.

v7 changes (2026-05-28, post-think-budget bug):
  * Pass "think": false to Ollama by default. Newer qwen3.5-mlx Ollama
    builds split output into `thinking` (chain-of-thought) and `response`
    (final answer). v6 only read `response` and never saw any text
    because the model was burning its num_predict budget inside the
    thinking phase before reaching the answer.
  * Read both `response` and `thinking` from each stream event. With
    --show-think we surface thinking too. Without, we drop it.
  * If after the full stream `response` is still empty and only `thinking`
    arrived, emit a clear stderr diagnostic.
  * --think flag re-enables thinking (debug only).

v6 changes carried forward:
  * Parquet schema matches reembed.py output (page_path, page_type, slug,
    title, tier, vector). No frontmatter reparse at retrieval time.
  * --no-notes / --only-notes / --type filters.
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

# --cloud path: call the Perplexity API directly (mirrors run_prescience_pass_c_v7.py).
# The legacy implementation shelled out to a `pplx` CLI binary that does not exist
# on this Mac; this replaces it with a direct HTTPS call using the same API key file.
CLOUD_API_URL = "https://api.perplexity.ai/chat/completions"
CLOUD_MODEL = "sonar-reasoning-pro"
CLOUD_KEY_PATHS = [
    Path.home() / ".config" / "adoptex" / "perplexity.env",
    Path("/tmp/perplexity.env"),
]


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


def stream_ollama(prompt: str, model: str, temperature: float, max_tokens: int,
                  enable_think: bool = False, show_think: bool = False):
    """Stream from Ollama. v7 reads both `response` and `thinking` fields.

    enable_think=False asks Ollama to skip thinking entirely (recommended
    for production — saves budget, avoids empty-response trap).
    enable_think=True + show_think=True is for debugging.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "think": enable_think,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        },
    }
    r = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json=payload,
        stream=True,
        timeout=600,
    )
    r.raise_for_status()

    saw_response = False
    saw_thinking = False
    done_reason = ""
    for line in r.iter_lines():
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        resp_tok = obj.get("response", "")
        think_tok = obj.get("thinking", "")
        if resp_tok:
            saw_response = True
            sys.stdout.write(resp_tok)
            sys.stdout.flush()
        if think_tok:
            saw_thinking = True
            if show_think:
                sys.stderr.write(think_tok)
                sys.stderr.flush()
        if obj.get("done"):
            done_reason = obj.get("done_reason", "")
            break

    sys.stdout.write("\n")

    if not saw_response:
        if saw_thinking:
            sys.stderr.write(
                "\n[kw ask] WARNING: model returned only `thinking`, no `response`.\n"
                "[kw ask] The thinking phase exhausted the token budget before the\n"
                "[kw ask] answer started. v7 already passes think=false; if you see\n"
                "[kw ask] this, your Ollama build may be ignoring the flag.\n"
                "[kw ask] Try: --max-tokens 4000, or update Ollama, or use --cloud.\n"
            )
        else:
            sys.stderr.write(
                f"\n[kw ask] WARNING: empty response (done_reason={done_reason!r}).\n"
            )


def _load_cloud_key() -> str:
    for pth in CLOUD_KEY_PATHS:
        if pth.exists():
            for line in pth.read_text().splitlines():
                if line.startswith("PERPLEXITY_API_KEY="):
                    return line.split("=", 1)[1].strip()
    sys.stderr.write(
        "[kw ask --cloud] PERPLEXITY_API_KEY not found in "
        + " or ".join(str(p) for p in CLOUD_KEY_PATHS)
        + "\n"
    )
    sys.exit(2)


def call_cloud(prompt: str) -> None:
    """Synthesize via the Perplexity cloud API (sonar-reasoning-pro).

    Direct HTTPS call — no external CLI. Strips any <think>...</think> reasoning
    block so the user sees clean synthesis, matching the local-model behavior.
    """
    api_key = _load_cloud_key()
    try:
        r = requests.post(
            CLOUD_API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": CLOUD_MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=600,
        )
    except requests.RequestException as e:
        sys.stderr.write(f"[kw ask --cloud] request failed: {e}\n")
        sys.exit(2)
    if r.status_code != 200:
        sys.stderr.write(
            f"[kw ask --cloud] API {r.status_code}: {r.text[:400]}\n"
        )
        sys.exit(2)
    try:
        content = r.json()["choices"][0]["message"]["content"]
    except (KeyError, IndexError, ValueError) as e:
        sys.stderr.write(f"[kw ask --cloud] unexpected response shape: {e}\n")
        sys.exit(2)
    # sonar-reasoning-pro emits a <think>...</think> preamble; drop it.
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
    sys.stdout.write(content)
    if not content.endswith("\n"):
        sys.stdout.write("\n")
    sys.stderr.write(f"[kw ask --cloud] model={CLOUD_MODEL}\n")


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
    p.add_argument("--think", action="store_true",
                   help="Enable model's thinking phase (debug). Default OFF in v7.")
    p.add_argument("--show-think", action="store_true",
                   help="Print thinking phase to stderr (implies --think)")

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
        # --show-think implies --think
        enable_think = args.think or args.show_think
        stream_ollama(
            prompt,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            enable_think=enable_think,
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
    think_mode = "off" if not (args.think or args.show_think) else "on"
    sys.stderr.write(
        f"[kw ask] filter: {mode}, k={args.k}, model={args.model}, think={think_mode}\n"
    )


if __name__ == "__main__":
    main()
