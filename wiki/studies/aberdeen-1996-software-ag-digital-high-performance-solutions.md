---
title: "Software AG and Digital: Spreading High-Performance Solutions Throughout The Enterprise"
slug: aberdeen-1996-software-ag-digital-high-performance-solutions
page_type: study
author: "Aberdeen Group"
date: "1996-12-01"
study_type: market-study
subject_domain: "RDBMS-hardware-performance"
methodology: "industry-analysis, benchmarking, competitive-profiling"
importance: medium
importance_rationale: "Published at a pivotal moment in database hardware architecture when 64-bit/VLM technology was emerging; provides early documentation of in-memory database performance benefits that presaged today's in-memory computing era (SAP HANA, Redis, etc.)."
relevance: medium
relevance_rationale: "The in-memory database performance principles documented here remain foundational to modern data architectures; however, ADABAS D and Digital Alpha are both effectively obsolete, limiting direct applicability."
prescience: medium
prescience_rationale: "Aberdeen correctly predicted in-memory computing would deliver orders-of-magnitude performance gains; however, the specific Software AG/Digital combination did not dominate the market as suggested—Digital was acquired by Compaq in 1998, and the VLM approach was eventually eclipsed by commodity x86 with large RAM."
license: CC-BY-4.0
tier: 2
entity_count: 6
tech_count: 7
obs_count: 20
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Software AG and Digital: Spreading High-Performance Solutions Throughout The Enterprise

> Aberdeen Group evaluates the Software AG ADABAS D RDBMS combined with Digital Equipment Corporation's 64-bit Alpha servers with Very Large Memory (VLM) technology. The study finds that VLM technology delivers 10-100x performance improvement for in-memory database operations, positioning the Software AG/Digital combination as an enterprise solution for OLTP, data marts, and application servers. Aberdeen concludes the combination meets a broad range of user needs for high-performance data management.

**Author:** Aberdeen Group · **Date:** 1996-12-01 · **Type:** market-study
**Importance:** medium — *Published at a pivotal moment in database hardware architecture when 64-bit/VLM technology was emerging; provides early documentation of in-memory database performance benefits that presaged today's in-memory computing era (SAP HANA, Redis, etc.).*
**Prescience:** medium — *Aberdeen correctly predicted in-memory computing would deliver orders-of-magnitude performance gains; however, the specific Software AG/Digital combination did not dominate the market as suggested—Digital was acquired by Compaq in 1998, and the VLM approach was eventually eclipsed by commodity x86 w…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[digital-equipment-corporation|Digital Equipment Corporation (DEC)]]
- [[ibm|IBM Corporation]]
- [[oracle-corporation|Oracle Corporation]]
- [[sap|SAP AG]]
- [[software-ag|Software AG]]

## Technologies (7)

- [[adabas-d|ADABAS D]]
- [[digital-alpha|Digital Alpha Architecture (64-bit)]]
- [[entire-networking|ENTIRE Networking]]
- [[esperant|ESPERANT]]
- [[natural-language|NATURAL (4GL Development Language)]]
- [[sap-r3|SAP R/3]]
- [[vlm-technology|Very Large Memory (VLM) Technology]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-software-ag-digital-high-performance-solutions' ORDER BY year_observed;
```

