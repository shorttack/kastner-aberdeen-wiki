# Kastner Aberdeen Wiki — v1.6

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

## What's new in v1.6

- **Short-horizon (3-year / 5-year) prescience** — full-corpus rescore of every
  gradeable observation against what was actually true 3 and 5 years after each
  claim's anchor year (sonar-pro, 2026-06-29). Replaces the one-shot ~30-year
  verdict with researchable near-term verdicts.
- New master: `_master_prescience_short_horizon.csv` (17,030 obs; per-obs
  `prescience_3y` / `prescience_5y` + rationales, -1=prefiltered, -2=window not
  yet elapsed).
- Study-level SH verdicts in `_master_studies.csv`: `prescience_3y_enum` /
  `prescience_5y_enum` (+ rationales) for 792 gradeable studies.
- New DuckDB views: `v_prescience_sh`, `v_observations_with_sh`,
  `v_studies_with_sh_verdicts`, `v_sh_3y_distribution`, `v_sh_5y_distribution`.
- Study pages now carry a **Short-horizon prescience** section (3y/5y verdicts).

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
