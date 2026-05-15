#!/usr/bin/env python3
"""Self-test for kastner-aberdeen-wiki."""
import sys, os, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
errors = []
def check(cond, msg):
    if cond: print(f"  PASS: {msg}")
    else: print(f"  FAIL: {msg}"); errors.append(msg)
print("Verifying kastner-aberdeen-wiki...")
for f in ["data/studies.parquet","data/entities.parquet","data/technologies.parquet",
          "data/observations.parquet","db/kastner.duckdb","AGENTS.md",
          "chat-starter.md","README.md"]:
    check((ROOT/f).exists(), f"{f} exists")
try:
    import duckdb
    con = duckdb.connect(str(ROOT/"db/kastner.duckdb"))
    for v in ["studies_with_high_prescience","entities_with_observation_count",
              "technologies_with_observation_count","volume_1_chapters"]:
        n = con.execute(f"SELECT COUNT(*) FROM {v}").fetchone()[0]
        check(n > 0, f"view {v} returns rows ({n})")
    con.close()
except Exception as e:
    errors.append(f"duckdb error: {e}")
wiki_pages = list((ROOT/"wiki").rglob("*.md"))
check(len(wiki_pages) > 100, f"wiki has {len(wiki_pages)} pages")
sys.exit(1 if errors else 0)
