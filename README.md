# Kastner Aberdeen Wiki — v1.5

Local-first research environment derived from the [aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive)
master CSVs. Built by `kastner-wiki-builder` skill v2.

## What's new in v1.5

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
