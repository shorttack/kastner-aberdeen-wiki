# AGENTS.md — Kastner Aberdeen Wiki

LLM primer. Read this before answering questions against the wiki.

## What this repo is

A read-optimized snapshot of the Aberdeen Group archive (1979–2013) maintained
by Pete Kastner. Three persistent layers:

1. **Obsidian vault** at `wiki/` — human-friendly Markdown with wikilinks,
   Dataview queries, and YAML frontmatter.
2. **DuckDB** at `db/kastner.duckdb` — analytical queries against ~18 named views.
3. **Parquet** at `data/*.parquet` — direct columnar access.

## Prescience scoring (v1.5)

Every observation in `_master_observations.csv` may have a prescience score
0-5 assigned by `qwen3.5:27b-mlx` (Pass C, 2026-05-26). Calibration kappa
vs Claude Sonnet: **0.853**. Confidence is 1 (low) to 3 (high).

| Score | Meaning |
|---:|---|
| 0 | Stated trivia / non-claim |
| 1 | Routine observation; uninteresting in hindsight |
| 2 | Reasonable take at the time |
| 3 | Notably right call |
| 4 | Prescient; ahead of consensus |
| 5 | Remarkably prescient; called something major early |

## Query recipes

### Top 20 most prescient studies
```sql
SELECT title, pub_year, prescience_max, prescience_mean
FROM v_top_prescient_studies LIMIT 20;
```

### Prescient observations from a single study
```sql
SELECT obs_id, prescience_score, prescience_rationale, metric_value
FROM v_observations
WHERE study_id = '<id>' AND prescience_score >= 4
ORDER BY prescience_score DESC;
```

### High-prescience studies by decade
```sql
SELECT decade, high_prescience_studies, studies_scored
FROM v_prescience_by_decade;
```

## Short-horizon prescience (3-year / 5-year) — v1.6

A full-corpus rescore (sonar-pro, 2026-06-29) grades each gradeable observation
against what was actually true 3 and 5 years after the claim's anchor year.
This replaces the one-shot ~30-year verdict (largely a gimmick) with
researchable near-term verdicts. Per-obs scores live in
`_master_prescience_short_horizon.csv`; study-level enums live in
`_master_studies.csv` as `prescience_3y_enum` / `prescience_5y_enum`.

Score sentinels: **-1** = prefiltered (too thin to grade), **-2** = window has
not yet elapsed (claim too recent to verify at that horizon).

### Studies prescient at 3 / 5 years
```sql
SELECT study_id, title, prescience_3y_enum, prescience_5y_enum
FROM v_studies_with_sh_verdicts
WHERE prescience_3y_enum = 'high' OR prescience_5y_enum = 'high'
ORDER BY study_id;
```

### 3-year score distribution (per observation)
```sql
SELECT prescience_3y, n FROM v_sh_3y_distribution ORDER BY prescience_3y;
```

### Observation-level 3y/5y scores joined to the obs
```sql
SELECT obs_id, study_id, prescience_3y, prescience_5y
FROM v_observations_with_sh
WHERE prescience_3y >= 4 OR prescience_5y >= 4
ORDER BY prescience_3y DESC, prescience_5y DESC;
```

## Naming conventions

- Slugs are lowercase-hyphenated and match CSV `*_id` columns.
- Study slugs are prefixed `study-`. Entities and technologies are not.
- Collection pages live at `wiki/collections/<type>.md`.
