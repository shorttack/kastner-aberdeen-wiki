---
title: "A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 — Multi-Horizon)"
slug: "study-2026-kastner-prescience-methodology-demo-v2-0cdf49"
page_type: "study"
tags: ["type/study", "collection/topic-analysis", "methodology/v2", "horizon/multi"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "2026-kastner-prescience-methodology-demo-v2-0cdf49"
author: "Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect)"
date: "2026-06-18"
pub_year: 2026
type: "topic-analysis"
subject_domain: "research-methodology"
methodology: "industry-analysis,attribution-modeling,multi-horizon-scoring,sensitivity-analysis,primary-source-triangulation,reproducibility-framework"
source_file: "kastner-author/2026-kastner-prescience-methodology-demo-v2-0cdf49/source/original_text.md"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "not-applicable"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
synthetic: true
supersedes: "2026-kastner-prescience-methodology-demo-0cdf48"
---

# A Worked Example: Quantifying Analyst Prescience Using the Kastner IT Research Archive (v2.0 — Multi-Horizon)

> Methodology v2.0 regeneration of the 2026-05-16 worked example, rebuilt against the v1.6.2 Kastner archive corpus (1,452 studies / 23,926 observations / 865 studies with prescience_max ≥ 4). Adds per-observation multi-horizon prescience scoring (`score_overall`, `score_3yr`, `score_5yr`) shipped in v1.6.2 of `_master_prescience_scores.csv`. New §3.6 (multi-horizon methodology) and §5.4 (horizon-decomposed attribution: overall / 3yr / 5yr / beyond-5yr). v1.0 dollar figures retained for reference; v2.0 dollar figures marked TBD pending Pete-authored recompute. Lead-time scoring (previously subjective §4) is now data-derivable from horizon columns.

_Published 2026-06-18, author **Peter S. Kastner (subject/reviewer) and Perplexity Computer (methodology architect)**, type **topic-analysis**._

## What changed v1.0 → v2.0

| Dimension | v1.0 (2026-05-16) | v2.0 (2026-06-18) |
|---|---|---|
| Corpus | 933 studies / 19,175 obs / 466 high-prescience | 1,452 studies / 23,926 obs / 865 prescience_max ≥ 4 |
| Scoring schema | single `prescience_score` per obs | `score_overall` + `score_3yr` + `score_5yr` per obs |
| Headline themes | 15 themes; AI/ML Infrastructure below threshold | 15 themes (same set); AI/ML Infrastructure expected to promote |
| Attribution dimensions | lead-time (subjective), contrarian, specificity, share | lead-time now horizon-derivable; contrarian, specificity, share unchanged |
| Net mid-attributed value | $10.9T (2026 USD), band $8.8T–$13.4T | $TBD (v2.0 recompute pending Pete-authored pass) |
| Gross | $41.3T | $TBD |
| Attribution rate | 26.4% | $TBD |
| Methodology version | 1.0 | 2.0 |
| Build sources | v1.4 corpus snapshot | v1.6.2 release (archive a472cc4f, wiki bc71a2a7) |

## Replication

The full source text — methodology sections §1–§11, sensitivity tables, replication code, recompute checklist — lives in the archive at:

```
kastner-author/2026-kastner-prescience-methodology-demo-v2-0cdf49/source/original_text.md
```

The v1.6.2 DuckDB query for the high-prescience pool used by this study:

```sql
SELECT study_id, title, study_prescience_enum, prescience_max, prescience_mean
FROM v_studies_with_high_prescience
ORDER BY prescience_max DESC, prescience_mean DESC;
```

Expected result count: 865 studies (against the v1.6.2 corpus).

## Predecessor

This v2.0 study supersedes — but does not delete — the v1.0 study at [[study-2026-kastner-prescience-methodology-demo-0cdf48]] (study_id `2026-kastner-prescience-methodology-demo-0cdf48`, published 2026-05-16). v1.0 remains in the archive as historical record; its dollar figures are the canonical v1.0 reference values cited in the v2.0 comparison table above.

## Pending work (v2.0 recompute — Pete-authored)

1. Re-derive 15-theme membership against the 865-study pool (vs. v1.0's 466-study pool)
2. Recompute gross market values per theme using v1.6.2 corpus
3. Recompute net-attributed values using horizon-decomposed lead-time scoring
4. Recompute four sub-tables in §5.4: overall, 3yr, 5yr, beyond-5yr attribution
5. Compute sensitivity band against v1.6.2 corpus
6. Verify AI/ML Infrastructure theme membership (expected promotion to headline)
7. Update §11 recompute checklist with completion timestamps
8. Re-run replication code blocks against v_studies_with_high_prescience
9. Sign-off + publish v2.0 dollar figures

Until items 1–9 are complete, all v2.0 dollar figures in the source text remain marked `$TBD (v2.0 recompute pending)`.
