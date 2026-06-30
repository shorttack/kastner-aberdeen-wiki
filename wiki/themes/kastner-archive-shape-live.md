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
tags:
  - meta
  - shape
  - canonical-counts
synthetic: true
last_rebuild: 2026-06-28
---

# Kastner Archive — Live Shape (Current Corpus)

> [!important] This page is the single source of truth for the CURRENT size and shape of the Kastner IT Research Archive. It is regenerated from the live DuckDB (`db/kastner.duckdb`) on every full rebuild. When any question asks "how big / how many / what is the shape of the archive" in the present tense, answer from THIS page. Other pages (study abstracts, theme rollups, the memoir, the prescience methodology demo) quote **historical corpus snapshots** that were accurate at their authoring time — do not treat those as the current count.

## Current shape (as of 2026-06-28 rebuild)

| Dimension | Count |
|---|---|
| **Studies** | **1,504** |
| **Observations** | **24,715** |
| **Entities** | **3,293** |
| **Technologies** | **4,376** |
| **High-prescience studies** | **876** |
| Studies with pub_year resolved | 1,504 / 1,504 (100%) |
| Decades covered | 6 |
| Scored observations (Pass C) | 16,998 |
| Studies with ≥1 scored observation | 1,321 |

These figures come directly from the canonical shape-audit query against the live DuckDB:

```sql
SELECT
  (SELECT COUNT(*) FROM v_studies) AS studies,                                  -- 1504
  (SELECT COUNT(*) FROM v_observations) AS observations,                        -- 24715
  (SELECT COUNT(*) FROM v_entities) AS entities,                                -- 3293
  (SELECT COUNT(*) FROM v_technologies) AS technologies,                        -- 4376
  (SELECT COUNT(*) FROM v_studies WHERE pub_year IS NOT NULL) AS with_pub_year, -- 1504
  (SELECT COUNT(DISTINCT (CAST(pub_year AS INTEGER)//10)*10)
     FROM v_studies WHERE pub_year IS NOT NULL) AS decades_covered,             -- 6
  (SELECT COUNT(*) FROM v_studies_with_high_prescience) AS high_prescience;     -- 876
```

## Why other pages cite different numbers

Several narrative pages quote **earlier corpus snapshots** and those numbers are correct *for those documents*:

- The **technology-breadth memoir** describes "592 of the archive's 915 studies" — the archive held 915 studies when the memoir was authored. That is a historical fact about the memoir, not a current count.
- The **prescience methodology demo** and the **prescience market rollup** cite a "933-study archive, 19,175 observations, 466 high-prescience studies." The demo's $10.9 trillion attributed-value result was computed against that 933-study snapshot. Restating it against the current 1,504-study corpus would falsely attribute the result to a dataset it was never run on.

In short: snapshot figures in those pages are intentionally preserved for historical/replication fidelity. **This page carries the live number.**

## Pointers

- Live database: `db/kastner.duckdb` (views prefixed `v_`)
- Masters (source of truth): repo root of `aberdeen-group-archive` (`_master_studies.csv`, `_master_observations.csv`, etc.)
- Shape audit lives in the `kastner-archive-pipeline` skill and is pasted into `_decisions_log.md` on every rebuild.
