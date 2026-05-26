#!/usr/bin/env python3
"""scripts/semantic_search.py — Local cosine-sim search over the wiki."""
from __future__ import annotations
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit("ERROR: install pandas + numpy")


OLLAMA_BASE = os.environ.get("OLLAMA_BASE", "http://localhost:11434")


def embed_query(text: str, model: str = "nomic-embed-text") -> list[float]:
    payload = json.dumps({"model": model, "prompt": text}).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/api/embeddings", data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))["embedding"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--wiki", default=".")
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()

    df = pd.read_parquet(wiki / "data" / "embeddings.parquet")
    df = df[df["dim"] > 0]
    M = np.vstack(df["embedding"].to_list())
    q = np.array(embed_query(args.query))
    sims = M @ q / (np.linalg.norm(M, axis=1) * np.linalg.norm(q) + 1e-9)
    df = df.assign(sim=sims).sort_values("sim", ascending=False).head(args.top)
    for _, r in df.iterrows():
        print(f"{r['sim']:.4f}  {r['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
