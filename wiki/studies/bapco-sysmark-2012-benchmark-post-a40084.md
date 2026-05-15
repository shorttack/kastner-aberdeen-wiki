---
title: "BAPco SYSmark 2012: Why AMD Dropped Out and What the Benchmark Actually Measures"
slug: bapco-sysmark-2012-benchmark-post-a40084
page_type: study
author: "Peter S. Kastner"
date: "2011-08-01"
study_type: white-paper
subject_domain: "commercial-benchmarks"
methodology: "benchmarking, competitive-profiling, expert-opinion"
importance: medium
importance_rationale: "Captures the AMD-BAPco schism mid-2011 — a pivotal commercial-benchmarks governance event. Kastner applied BAPco's own test harness to the disputed hardware."
relevance: medium
relevance_rationale: "Benchmark-bias framework and SYSmark methodology remain reusable templates; specific 2011 CPUs and scores are historical."
prescience: low
prescience_rationale: "Kastner implicitly defends SYSmark relevance; AMD continued to reject BAPco-style benchmarks for a decade; overall frame was contested, not validated."
license: CC-BY-4.0
tier: 2
entity_count: 5
tech_count: 14
obs_count: 14
tags: [type/study, importance/medium, prescience/low, decade/2010s]
source_csv: master_studies.csv
---

# BAPco SYSmark 2012: Why AMD Dropped Out and What the Benchmark Actually Measures

> Kastner blog post defending BAPco's SYSmark 2012 benchmark against AMD's June 2011 withdrawal from the consortium. Reports Kastner's own test results on the AMD Fusion A8-3850 APU ('Llano', scored 91) versus Intel Sandy Bridge Pentium 840 (98), Core i3-2120 (127), and Core i5-2500 (166). Argues the benchmark reflects 20 years of real-workload modeling across six scenarios (Office, Media, Web, Data/Financial, 3D, System Management) and rejects AMD's framing. The post is a commercial-benchmarks topic deep-dive from Kastner's post-Aberdeen independent-analyst era.

**Author:** Peter S. Kastner · **Date:** 2011-08-01 · **Type:** white-paper
**Importance:** medium — *Captures the AMD-BAPco schism mid-2011 — a pivotal commercial-benchmarks governance event. Kastner applied BAPco's own test harness to the disputed hardware.*
**Prescience:** low — *Kastner implicitly defends SYSmark relevance; AMD continued to reject BAPco-style benchmarks for a decade; overall frame was contested, not validated.*

## Entities (5)

- [[amd|Advanced Micro Devices]]
- [[bapco|Business Applications Performance Corporation (BAPco)]]
- [[intel-corp|Intel Corporation]]
- [[microsoft|Microsoft]]
- [[peter-kastner|Peter S. Kastner]]

## Technologies (14)

- [[amd-llano|AMD A8-3850 (Llano)]]
- [[amd-phenom-ii|AMD Phenom II 1100T]]
- [[ati-radeon-4290|ATI Radeon HD 4290]]
- [[autocad|Autodesk AutoCAD]]
- [[intel-clarkdale|Intel Core i3-540 (Clarkdale)]]
- [[intel-core-i3-2120|Intel Core i3-2120]]
- [[intel-core-i5-2500|Intel Core i5-2500]]
- [[intel-pentium-840|Intel Pentium 840]]
- [[intel-pentium-g620t|Intel Pentium G620T]]
- [[intel-sandy-bridge|Intel Sandy Bridge]]
- [[ms-office|Microsoft Office]]
- [[sysmark-2007|BAPco SYSmark 2007]]
- [[sysmark-2012|BAPco SYSmark 2012]]
- [[windows-7|Windows 7]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'bapco-sysmark-2012-benchmark-post-a40084' ORDER BY year_observed;
```

