---
title: "Pass A v2 — Archive Verification Pipeline"
slug: pass-a-v2-verification-pipeline
page_type: theme
theme_type: methodology
tier: 1
tags: [type/theme, methodology, pass-a-v2, verification, theme/pipeline]
source_csv: derived
pass_a_v2_added: true
---

# Pass A v2 — Archive Verification Pipeline

> Pass A v2 propagates structural verification through the entire archive — adding a
> `verification_method` column to every observation, lifting viability predictions whose
> outcome is evidenced by predecessor→successor linkage, and clearing legacy `[REVIEW]`
> markers in a rule-based triage. No LLM calls, no external evidence — pure structural
> verification.

## What Pass A v2 produced

| Metric | Pass A v1 (commit 7e052957) | Pass A v2 (commit 7f0dad1c) |
|---|---:|---:|
| Master observations | 19,408 | **19,694** (+286 from 3 new studies) |
| REVIEW markers cleared | 56 | 0 (none remained) |
| Viability-prediction lifts | 690 | 38 net-new |
| verification_method populated | 100% | 100% |
| Viability-prediction verified+partial rate | 45.5% | **46.1%** (788 / 1,711) |
| Prediction → outcome links | 3,245 | **3,347** (1,388 linked) |

## verification_method distribution (after v2)

| Method | Count |
|---|---:|
| ingest-extraction | 17,553 |
| web-source | 1,187 |
| outcome-linkage | 855 |
| unverified | 79 |
| placeholder | 16 |
| cross-reference | 4 |

## What changed in this wiki

- `observations.parquet` and `kastner.duckdb` rebuilt from current archive masters.
- New columns surfaced: `verification_method`, `collection`, `thread_tag`.
- New DuckDB views: `verification_method_distribution`, `viability_predictions_status`.
- New tier-1 study pages added:
  - [[2026-kastner-ibm-longitudinal]]
  - [[2026-kastner-oracle-longitudinal]]
  - [[2026-kastner-enterprise-ai-arc]]
- 32 new entity stubs and 133 new technology stubs auto-generated from the
  updated `_known_entities.csv` / `_known_technologies.csv`.

## Methodology in three lines

1. **REVIEW triage** — pre-existing `[REVIEW]` confidence markers are graded with
   rule-based heuristics (year proximity, source page hits, methodology code) and
   lifted into `low | medium | partially-verified`.
2. **Prediction → outcome linkage** — viability predictions are joined to later
   observations of the same `entity_id` / `tech_id`. A predecessor whose successor
   shows continued activity (or a documented dissolution) is lifted to `verified`,
   `partially-verified`, or `refuted` based on the outcome match.
3. **verification_method assignment** — every observation receives one of six
   verification_method values to make the provenance of each verification visible
   to downstream queries.

## How to query Pass A v2 results

```sql
-- Distribution of verification methods
SELECT * FROM verification_method_distribution;

-- All verified viability predictions across the archive
SELECT study_id, entity_id, tech_id, year_observed, metric_name,
       metric_value, verification_method
FROM observations
WHERE observation_type = 'viability-prediction'
  AND confidence IN ('verified','partially-verified')
ORDER BY year_observed;

-- The 38 net-new lifts unlocked by the 3 new studies
SELECT * FROM observations
WHERE verification_method = 'outcome-linkage'
  AND confidence IN ('verified','partially-verified','refuted')
  AND study_id IN ('2026-kastner-ibm-longitudinal',
                   '2026-kastner-oracle-longitudinal',
                   '2026-kastner-enterprise-ai-arc');
```

## Cross-references

- [[kastner-core-arguments-framework]] — the analytical superstructure Pass A serves
- [[kastner-prescience-market-rollup]] — the methodology demonstration
- [[kastner-top-100-economic-calls]] — the ranked-list output Pass A verifies
- [[intel-corporation-longitudinal]] — companion longitudinal study

## Provenance

- Archive commit: `7f0dad1c` on `shorttack/aberdeen-group-archive` `main`
- DOI: `10.5281/zenodo.20245076`
- Method: no LLM, no external evidence; pure structural verification
- All writes used `csv.QUOTE_ALL`; v18 validation gate passed on all new studies
