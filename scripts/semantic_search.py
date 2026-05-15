#!/usr/bin/env python3
"""Cosine-similarity retrieval over data/embeddings.parquet.

Auto-detects vector dim and picks an encoder model accordingly:
  - 384-dim -> sentence-transformers/all-MiniLM-L6-v2
  - 768-dim -> nomic-ai/nomic-embed-text-v1.5

If your parquet was rebuilt with a different model, pass --model.

Examples:
  python scripts/semantic_search.py "predictions about open source"
  python scripts/semantic_search.py --model nomic-ai/nomic-embed-text-v1.5 "ERP and CRM convergence"
  python scripts/semantic_search.py --tier 1 --type study "category creation playbook"
"""
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+")
    ap.add_argument("--model", default=None, help="Override encoder model")
    ap.add_argument("--type", default=None, help="Filter by page_type (study/entity/technology/chapter)")
    ap.add_argument("--tier", type=int, default=None, help="Filter by tier (1 or 2)")
    ap.add_argument("--k", type=int, default=15)
    args = ap.parse_args()

    try:
        import duckdb
        from sentence_transformers import SentenceTransformer
    except ImportError as e:
        print(f"Missing dependency: {e}", file=sys.stderr)
        sys.exit(1)

    # Detect dim from parquet
    con = duckdb.connect()
    con.execute(f"CREATE TABLE emb AS SELECT * FROM read_parquet('{ROOT/'data/embeddings.parquet'}');")
    dim = con.execute("SELECT len(vector) FROM emb LIMIT 1").fetchone()[0]

    model_id = args.model or (
        "sentence-transformers/all-MiniLM-L6-v2" if dim == 384
        else "nomic-ai/nomic-embed-text-v1.5"
    )
    print(f"# Embedding dim={dim}, encoder={model_id}", file=sys.stderr)

    model = SentenceTransformer(model_id, trust_remote_code=True)
    query = " ".join(args.query)
    prefix = "search_query: " if "nomic" in model_id else ""
    qvec = model.encode(f"{prefix}{query}", normalize_embeddings=True).tolist()

    where = []
    params = [qvec]
    if args.type:
        where.append("page_type = ?")
        params.append(args.type)
    if args.tier is not None:
        where.append("tier = ?")
        params.append(args.tier)
    wclause = (" WHERE " + " AND ".join(where)) if where else ""

    sql = f"""
        SELECT page_path, page_type, title, tier,
               list_cosine_similarity(vector, ?) AS score
        FROM emb{wclause}
        ORDER BY score DESC
        LIMIT {int(args.k)}
    """
    rows = con.execute(sql, params).fetchall()
    print(f"\nTop {len(rows)} matches for: {query}\n")
    for path, ptype, title, tier, score in rows:
        print(f"  {score:.3f}  [t{tier} {ptype:<10}] {path:<55} {title}")


if __name__ == "__main__":
    main()
