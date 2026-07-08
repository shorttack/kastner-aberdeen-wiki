---
title: "Kastner Archive — Live Shape (Current Corpus)"
slug: kastner-archive-shape-live
page_type: theme
type: theme
aliases:
  - "shape of the Kastner archive"
  - "archive shape"
  - "current archive size"
  - "how many studies in the Kastner archive"
  - "how big is the Kastner archive"
  - "how many entities in the Kastner archive"
  - "how many technologies in the Kastner archive"
tags:
  - meta
  - shape
  - canonical-counts
synthetic: true
last_rebuild: 2026-07-08
---

# Kastner Archive — Live Shape (Current Corpus)

> [!important] This page is the single source of truth for the CURRENT size and shape of the Kastner IT Research Archive. It is regenerated from the live DuckDB (`db/kastner.duckdb`) on every full rebuild. When any question asks "how big / how many / what is the shape of the archive" in the present tense, answer from THIS page. Other pages (study abstracts, theme rollups, the memoir, the prescience methodology demo) quote **historical corpus snapshots** that were accurate at their authoring time — do not treat those as the current count.

## Current shape (as of 2026-07-08 rebuild — post-SAP-unblock cleanse)

| Dimension | Count |
|---|---|
| **Studies** | **1,504** |
| **Observations** | **24,842** |
| **Entities** | **3,288** |
| **Technologies** | **4,368** |
| **High-prescience studies** | **876** |
| Studies with pub_year resolved | 1,504 / 1,504 (100%) |
| Decades covered | 6 (1970s–2020s) |
| Long-horizon Pass C scored observations | 8,589 |
| **Short-horizon (SH) prescience scores** | **17,030** |
| **Studies with SH verdicts (3y + 5y)** | **792** |

**Delta vs 2026-07-04 baseline** (SAP-unblock master cleanse, committed 2026-07-08):
- Entities: 3,293 → **3,288** (−5; SAP alias collapse + confirmed duplicates)
- Technologies: 4,376 → **4,368** (−8; 8 confirmed mislabels reassigned to canonical slugs)
- Studies + observations: unchanged (row identity preserved end-to-end)

These figures come directly from the canonical shape-audit query against the live DuckDB:

```sql
SELECT
  (SELECT COUNT(*) FROM v_studies) AS studies,                                  -- 1504
  (SELECT COUNT(*) FROM v_observations) AS observations,                        -- 24842
  (SELECT COUNT(*) FROM v_entities) AS entities,                                -- 3288
  (SELECT COUNT(*) FROM v_technologies) AS technologies,                        -- 4368
  (SELECT COUNT(*) FROM v_studies WHERE pub_year IS NOT NULL) AS with_pub_year, -- 1504
  (SELECT COUNT(DISTINCT (CAST(pub_year AS INTEGER)//10)*10)
     FROM v_studies WHERE pub_year IS NOT NULL) AS decades_covered,             -- 6
  (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience,     -- 876
  (SELECT COUNT(*) FROM v_prescience_sh) AS sh_scores,                          -- 17030
  (SELECT COUNT(*) FROM v_studies_with_sh_verdicts) AS sh_verdicts;             -- 792
```

## Why other pages cite different numbers

Several narrative pages quote **earlier corpus snapshots** and those numbers are correct *for those documents*:

- The **technology-breadth memoir** describes "592 of the archive's 915 studies" — the archive held 915 studies when the memoir was authored. That is a historical fact about the memoir, not a current count.
- The **prescience methodology demo** and the **prescience market rollup** cite a "933-study archive, 19,175 observations, 466 high-prescience studies." The demo's $10.9 trillion attributed-value result was computed against that 933-study snapshot. Restating it against the current 1,504-study corpus would falsely attribute the result to a dataset it was never run on.
- The **v1.6 and v1.7 release notes** quote intermediate counts (e.g., 1,452 studies / 3,276 entities / 4,361 techs) from those release points. Same principle: correct at authoring time, superseded by later rebuilds.

In short: snapshot figures in those pages are intentionally preserved for historical/replication fidelity. **This page carries the live number.**

## Pointers

- Live database: `db/kastner.duckdb` (views prefixed `v_`)
- Masters (source of truth): repo root of `aberdeen-group-archive` (`_master_studies.csv`, `_master_observations.csv`, `_master_entities.csv`, `_master_technologies.csv`, `_master_prescience_scores.csv`, `_master_prescience_sh.csv`, etc.)
- Shape audit lives in the `kastner-archive-pipeline` skill and is pasted into `_decisions_log.md` on every rebuild.
- **Refresh cadence**: this page is currently refreshed manually via `refresh_shape_live_v1.py` (or the sandbox agent) after every rebuild. Planned Phase 6 automation (WORKLIST item #9) will emit this page from live DuckDB on every full pipeline run.
