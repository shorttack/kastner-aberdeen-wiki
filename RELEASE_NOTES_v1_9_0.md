# v1.9.0 — Sibling wiki release (no wiki regen)

**Released:** 2026-06-22
**Sibling archive release:** `shorttack/aberdeen-group-archive` v1.9.0 (commit `a02c23f1`)
**Wiki HEAD at release:** `97355369` (unchanged since v1.7.0)

## What this release contains

This wiki release is a **paired sibling tag only** — no Parquet, DuckDB, or page regeneration was performed.

### Why no regen

The v1.9.0 archive work happened in two layers, neither of which requires wiki propagation:

1. **v1.8.0 substrate work** (`kastner_quotes_clean.csv` 1087 → 1208 rows): apply ran on Pete's Mac via `apply_unindexed_quotes_v3.py --commit`. The committed file in `origin/main` of the archive will sync at Pete's next EOD batch. The wiki's `master_observations.csv` is not affected (the quotations corpus is a separate substrate layer).
2. **CompChem exemplar ingest**: landed in the new `project_examples/` top-level directory in the archive. This is intentionally outside the masters — `project_examples/` is a showcase directory, not a corpus directory. No master CSV change, no Parquet rebuild, no Obsidian page regen.

## When to regen

Wiki regen will be required when:
- The `kastner_quotes_clean.csv` 1208-row state syncs to archive `origin/main` AND we elect to surface quotations as Obsidian pages (currently out of scope).
- The next master CSV update lands (Pass A v3, prescience refresh, or a new corpus addition).
- The Mac MCP Bridge build kicks off and needs the wiki data layer indexed (Phase 0 still deferred).

## Sibling release notes

Full v1.9.0 release notes (covering v1.8.0 substrate work and CompChem ingest) live in the archive repo:
[`RELEASE_NOTES_v1_9_0.md`](https://github.com/shorttack/aberdeen-group-archive/blob/main/RELEASE_NOTES_v1_9_0.md)

---

_Owner: Pete Kastner._
