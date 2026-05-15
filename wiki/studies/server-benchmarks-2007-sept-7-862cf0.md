---
title: "Intel and AMD Server Benchmarks (September 2007)"
slug: server-benchmarks-2007-sept-7-862cf0
page_type: study
author: "Peter S. Kastner"
date: "2007-09-01"
study_type: benchmark
subject_domain: "server-cpu-benchmarks/intel-vs-amd"
methodology: "benchmarking, competitive-profiling"
importance: medium
importance_rationale: "Compact primary benchmark table capturing Intel's Xeon 7350 quad-core performance lead over AMD's 2007 offerings at the moment of the Intel Core era taking off. Useful reference snapshot."
relevance: low
relevance_rationale: "Specific benchmark scores are dated; methodology comparison (SPECjbb, SPECint_rate_2006, SAP-SD) remains valid benchmark reference."
prescience: medium
prescience_rationale: "Implicitly signaled Intel's tick-tock-era competitive advantage that persisted through the late 2000s until AMD's Zen revival in 2017."
license: CC-BY-4.0
tier: 2
entity_count: 6
tech_count: 11
obs_count: 19
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Intel and AMD Server Benchmarks (September 2007)

> Kastner-authored Excel spreadsheet comparing Intel Xeon 7140M dual-core, Xeon 7350 quad-core, and AMD Opteron 8220se dual-core and Barcelona 8222 across SQL Server database, ERP SAP-SD, Java SPECjbb, Integer SPECint_rate_2006, and SPEC webserver 2005 benchmarks. Includes DP chipset RAS feature comparison for Intel 5000X, 5000P, and 5000V. Primary document of Intel's quad-core lead over AMD's first-generation Barcelona in 2007.

**Author:** Peter S. Kastner · **Date:** 2007-09-01 · **Type:** benchmark
**Importance:** medium — *Compact primary benchmark table capturing Intel's Xeon 7350 quad-core performance lead over AMD's 2007 offerings at the moment of the Intel Core era taking off. Useful reference snapshot.*
**Prescience:** medium — *Implicitly signaled Intel's tick-tock-era competitive advantage that persisted through the late 2000s until AMD's Zen revival in 2017.*

## Entities (6)

- [[amd|Advanced Micro Devices (AMD)]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sap|SAP SE]]
- [[spec|Standard Performance Evaluation Corporation (SPEC)]]

## Technologies (11)

- [[amd-barcelona-8222|AMD Opteron Barcelona 8222 (quad-core)]]
- [[amd-opteron-8220se|AMD Opteron 8220se (dual-core)]]
- [[intel-5000p|Intel 5000P Chipset]]
- [[intel-5000v|Intel 5000V Chipset]]
- [[intel-5000x|Intel 5000X Chipset]]
- [[intel-xeon-7140m|Intel Xeon 7140M (dual-core)]]
- [[intel-xeon-7350|Intel Xeon 7350 (quad-core)]]
- [[sap-sd|SAP Sales and Distribution (SD) Benchmark]]
- [[spec-int-rate|SPECint_rate_2006]]
- [[spec-jbb|SPECjbb]]
- [[spec-webserver-2005|SPEC webserver 2005]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'server-benchmarks-2007-sept-7-862cf0' ORDER BY year_observed;
```

