#!/usr/bin/env python3
"""scripts/verify.py — Self-test for v1.6 wiki build."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

try:
    import duckdb
    import pandas as pd
except ImportError:
    sys.exit("ERROR: install duckdb + pandas")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", required=True)
    args = ap.parse_args()
    wiki = Path(args.wiki).resolve()
    fails = []
    warns = []

    # 1. Required dirs
    for d in ("wiki", "data", "db"):
        if not (wiki / d).exists():
            fails.append(f"missing dir: {d}")

    # 2. Parquet files load
    parquets = ["studies", "entities", "technologies", "observations",
                "prescience_scores", "known_entities", "known_technologies",
                "collection_stats"]
    for name in parquets:
        p = wiki / "data" / f"{name}.parquet"
        if not p.exists():
            fails.append(f"missing parquet: {name}.parquet")
            continue
        try:
            df = pd.read_parquet(p)
            if len(df) == 0:
                warns.append(f"{name}.parquet has 0 rows")
        except Exception as e:
            fails.append(f"parquet read failed for {name}: {e}")

    # 3. DuckDB opens, views work
    db = wiki / "db" / "kastner.duckdb"
    if db.exists():
        try:
            con = duckdb.connect(str(db))
            for v in ["v_studies_with_prescience", "v_top_prescient_studies",
                      "v_prescience_by_decade", "v_observations_with_prescience",
                      "v_prescience_sh", "v_studies_with_sh_verdicts",
                      "v_sh_3y_distribution", "v_sh_5y_distribution"]:
                n = con.execute(f"SELECT COUNT(*) FROM {v}").fetchone()[0]
                if n == 0:
                    warns.append(f"view {v} returned 0 rows")
            con.close()
        except Exception as e:
            fails.append(f"DuckDB failure: {e}")

    # 4. Manifest exists
    mp = wiki / "build_manifest.json"
    if not mp.exists():
        fails.append("missing build_manifest.json")
    else:
        m = json.loads(mp.read_text())
        for ph in ("phase_1", "phase_2", "phase_3", "phase_4"):
            if ph not in m:
                fails.append(f"manifest missing {ph}")

    # 5. _prescient.md page exists
    if not (wiki / "wiki" / "_prescient.md").exists():
        fails.append("missing wiki/_prescient.md")

    print("=" * 60)
    print(f"VERIFY: {len(fails)} fails, {len(warns)} warns")
    print("=" * 60)
    for f in fails:
        print(f"  FAIL  {f}")
    for w in warns:
        print(f"  WARN  {w}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
