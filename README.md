# Kastner Aberdeen Wiki — v1.6

Local-first research environment derived from the [aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive)
master CSVs. Built by `kastner-wiki-builder` skill v2.

**v1.6 — "full 1,400+ study content"** (2026-05-31)

The current corpus: **1,434 studies · 23,605 observations · 3,207 entity rows · 4,312 technology rows · 124 high-prescience studies** (Pass C, `prescience_max ≥ 4`), spanning **1979–2026**.

These are the live counts. Per-subdirectory and per-section numbers elsewhere may lag the masters — when in doubt, `_master_*.csv` is truth.

## What's new in v1.6

- **Full 1,434-study corpus** ingested (up from 944 in v1.5)
- **Phase 5 embeddings regenerated** with v3 schema (`page_path / page_type / slug / title / vector / dim`)
- **Prescience scores** from local `qwen3.5:27b-mlx` Pass C run (2026-05-26)
- New 8th master ingested: `_master_prescience_scores.csv`
- New DuckDB views: `v_studies_with_prescience`, `v_top_prescient_studies`,
  `v_prescience_by_decade`, `v_low_confidence_prescience`
- New page subdir: `wiki/_prescient.md` (top 50 most prescient studies)
- Frontmatter on every page: `prescience_max`, `prescience_mean`,
  `prescience_obs_count`

## Quick start

1. Open `wiki/` as an Obsidian vault.
2. Open `wiki/_index.md` and follow links.
3. From terminal: `python3 scripts/semantic_search.py "query"`.
4. From SQL: `duckdb db/kastner.duckdb` then `SELECT * FROM v_top_prescient_studies LIMIT 20`.

## File map

| Path | What |
|---|---|
| `wiki/` | Obsidian vault root — open this in Obsidian |
| `data/*.parquet` | Columnar copies of master CSVs |
| `db/kastner.duckdb` | Pre-built DuckDB with ~18 named views |
| `db/queries/*.sql` | Reusable query examples |
| `scripts/rebuild.py` | Full rebuild (rarely needed) |
| `scripts/verify.py` | Self-test |
| `scripts/semantic_search.py` | Local cosine-sim search |
| `build_manifest.json` | What was built, when, with what counts |
| `AGENTS.md` | LLM primer |
| `chat-starter.md` | Pre-warmed prompts |

## Rebuild

```bash
make rebuild
```

Or step-by-step:

```bash
python3 scripts/build/01_load_csvs_v1.py --archive ~/Desktop/Archive/aberdeen-group-archive --wiki .
python3 scripts/build/02_build_data_layer_v1.py --wiki .
python3 scripts/build/03_generate_vault_v1.py --wiki . [--skip-llm]
python3 scripts/build/04_generate_indices_v1.py --wiki .
python3 scripts/build/05_compute_embeddings_v1.py --wiki .
python3 scripts/build/06_emit_scaffolding_v1.py --wiki .
python3 scripts/verify.py --wiki .
```
