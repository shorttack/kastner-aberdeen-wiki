#!/usr/bin/env python3
"""Re-embed the wiki using a different model.

Examples:
  # Use nomic-embed-text-v1.5 (768-dim, your preferred quality)
  python scripts/reembed.py --model nomic-ai/nomic-embed-text-v1.5

  # Use any other sentence-transformers model
  python scripts/reembed.py --model BAAI/bge-large-en-v1.5

  # Use Ollama (HTTP API at localhost:11434)
  python scripts/reembed.py --ollama nomic-embed-text-v2-moe

Memory note:
- nomic-embed-text-v1.5 needs ~3GB RAM at fp32, ~1.5GB at fp16 on GPU.
- The 48GB Mac Mini M4 will run any of these comfortably with MPS (Metal).
"""
import argparse, gc, os, sys, time
from pathlib import Path
import yaml
import pyarrow as pa
import pyarrow.parquet as papq

ROOT = Path(__file__).resolve().parents[1]
OUT_PARQUET = ROOT / "data" / "embeddings.parquet"


def embed_with_sentence_transformers(model_id: str, batch: int):
    from sentence_transformers import SentenceTransformer
    import torch
    device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[reembed] Loading {model_id} on {device}")
    model = SentenceTransformer(model_id, trust_remote_code=True, device=device)
    pages = sorted((ROOT / "wiki").rglob("*.md"))
    print(f"[reembed] {len(pages)} pages, batch={batch}")
    # Probe dim
    dim = model.encode(["probe"], normalize_embeddings=True, show_progress_bar=False).shape[1]
    print(f"[reembed] embedding dim: {dim}")
    schema = pa.schema([
        ("page_path", pa.string()),
        ("page_type", pa.string()),
        ("slug", pa.string()),
        ("title", pa.string()),
        ("tier", pa.int32()),
        ("vector", pa.list_(pa.float32())),
    ])
    if OUT_PARQUET.exists():
        OUT_PARQUET.unlink()
    writer = papq.ParquetWriter(str(OUT_PARQUET), schema, compression="zstd")
    total = 0; t0 = time.time()
    buf_texts, buf_meta = [], []
    def flush():
        nonlocal total
        if not buf_texts: return
        vecs = model.encode(buf_texts, normalize_embeddings=True,
                            show_progress_bar=False, batch_size=batch)
        tbl = pa.table({
            "page_path":[m["path"] for m in buf_meta],
            "page_type":[m["type"] for m in buf_meta],
            "slug":[m["slug"] for m in buf_meta],
            "title":[m["title"] for m in buf_meta],
            "tier":[m["tier"] for m in buf_meta],
            "vector":[v.astype("float32").tolist() for v in vecs],
        }, schema=schema)
        writer.write_table(tbl)
        total += len(buf_texts)
        if total % 500 == 0 or total == len(pages):
            r = total / (time.time() - t0)
            print(f"[reembed] {total}/{len(pages)} @ {r:.1f}/s")
        buf_texts.clear(); buf_meta.clear(); gc.collect()
    for p in pages:
        text = p.read_text(encoding="utf-8")
        front, body = {}, text
        if text.startswith("---"):
            try:
                end = text.index("---", 3); front = yaml.safe_load(text[3:end]) or {}; body = text[end+3:].strip()
            except Exception: pass
        # nomic models prefer "search_document:" prefix
        prefix = "search_document: " if "nomic" in model_id else ""
        buf_texts.append(f"{prefix}{front.get('title','')}\n\n{body[:1500]}")
        buf_meta.append({
            "path": str(p.relative_to(ROOT)),
            "type": front.get("page_type","unknown"),
            "slug": front.get("slug",""),
            "title": str(front.get("title","")),
            "tier": int(front.get("tier",2) or 2),
        })
        if len(buf_texts) >= batch: flush()
    flush(); writer.close()
    print(f"[reembed] DONE — {total} rows in {OUT_PARQUET}")


def embed_with_ollama(model_name: str, batch: int):
    import urllib.request, json
    pages = sorted((ROOT / "wiki").rglob("*.md"))
    print(f"[reembed-ollama] {len(pages)} pages via Ollama model={model_name}")
    # Probe dim
    req = urllib.request.Request("http://localhost:11434/api/embeddings",
        data=json.dumps({"model": model_name, "prompt": "probe"}).encode(),
        headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req) as r:
        dim = len(json.loads(r.read())["embedding"])
    print(f"[reembed-ollama] embedding dim: {dim}")
    schema = pa.schema([
        ("page_path", pa.string()), ("page_type", pa.string()),
        ("slug", pa.string()), ("title", pa.string()),
        ("tier", pa.int32()), ("vector", pa.list_(pa.float32())),
    ])
    if OUT_PARQUET.exists(): OUT_PARQUET.unlink()
    writer = papq.ParquetWriter(str(OUT_PARQUET), schema, compression="zstd")
    rows = {"page_path":[],"page_type":[],"slug":[],"title":[],"tier":[],"vector":[]}
    total = 0; t0 = time.time()
    for p in pages:
        text = p.read_text(encoding="utf-8"); front, body = {}, text
        if text.startswith("---"):
            try:
                end = text.index("---", 3); front = yaml.safe_load(text[3:end]) or {}; body = text[end+3:].strip()
            except Exception: pass
        prompt = f"{front.get('title','')}\n\n{body[:1500]}"
        req = urllib.request.Request("http://localhost:11434/api/embeddings",
            data=json.dumps({"model": model_name, "prompt": prompt}).encode(),
            headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(req) as r:
            vec = json.loads(r.read())["embedding"]
        rows["page_path"].append(str(p.relative_to(ROOT)))
        rows["page_type"].append(front.get("page_type","unknown"))
        rows["slug"].append(front.get("slug",""))
        rows["title"].append(str(front.get("title","")))
        rows["tier"].append(int(front.get("tier",2) or 2))
        rows["vector"].append(vec)
        total += 1
        if total % batch == 0:
            writer.write_table(pa.table(rows, schema=schema))
            for k in rows: rows[k] = []
            if total % 500 == 0:
                r = total / (time.time() - t0); print(f"[reembed-ollama] {total}/{len(pages)} @ {r:.1f}/s")
    if rows["slug"]:
        writer.write_table(pa.table(rows, schema=schema))
    writer.close()
    print(f"[reembed-ollama] DONE — {total} rows")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", help="sentence-transformers model id")
    ap.add_argument("--ollama", help="Ollama model name (uses HTTP localhost:11434)")
    ap.add_argument("--batch", type=int, default=32)
    args = ap.parse_args()
    if args.ollama:
        embed_with_ollama(args.ollama, args.batch)
    elif args.model:
        embed_with_sentence_transformers(args.model, args.batch)
    else:
        ap.error("Pass --model or --ollama")
