---
title: "Performance Breakthroughs: The Benchmarking Fanatics Are Still at It"
slug: 2002-performance-breakthroughs-the-benchmarking-fanatic-6d41fa
page_type: study
author: "Robert Dorin"
date: "2002-10-01"
study_type: market-study
subject_domain: "server-benchmarking"
methodology: "benchmarking"
importance: medium
importance_rationale: "Timely snapshot of high-end server benchmark competition at a pivotal moment when Itanium 2 was newly released and vendors were establishing performance credibility for an anticipated recovery in enterprise hardware spending."
relevance: low
relevance_rationale: "Itanium 2 is now dead (Intel ended shipments 2021); HP Superdome transitioned to x86; TPC benchmarks still exist but the specific performance figures are entirely obsolete. Value is primarily historical."
prescience: medium
prescience_rationale: "The prediction of a market share battle among server vendors when IT spending recovered proved correct — but the actual battleground shifted to x86-64 (Xeon/Opteron) rather than Itanium, which ultimately failed in the market."
license: CC-BY-4.0
tier: 2
entity_count: 6
tech_count: 6
obs_count: 13
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Performance Breakthroughs: The Benchmarking Fanatics Are Still at It

> Several key SAP and TPC benchmarks released in summer 2002 represent high-end server performance breakthroughs for HP, IBM, and Intel (via NEC). Despite a current hardware sales slump, major server suppliers are preparing for a market share battle expected to resume when IT buyers re-engage. The study covers Itanium 2, HP Superdome, IBM, NEC, DB2, SAP, TPC-C and TPC-H results.

**Author:** Robert Dorin · **Date:** 2002-10-01 · **Type:** market-study
**Importance:** medium — *Timely snapshot of high-end server benchmark competition at a pivotal moment when Itanium 2 was newly released and vendors were establishing performance credibility for an anticipated recovery in enterprise hardware spending.*
**Prescience:** medium — *The prediction of a market share battle among server vendors when IT spending recovered proved correct — but the actual battleground shifted to x86-64 (Xeon/Opteron) rather than Itanium, which ultimately failed in the market.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[intel|Intel Corporation]]
- [[nec|NEC Corporation]]
- [[sap|SAP SE]]

## Technologies (6)

- [[db2|IBM DB2]]
- [[hp-superdome|HP Superdome]]
- [[itanium-2|Intel Itanium 2]]
- [[sap-r3|SAP R/3]]
- [[tpc-c|TPC-C Benchmark]]
- [[tpc-h|TPC-H Benchmark]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2002-performance-breakthroughs-the-benchmarking-fanatic-6d41fa' ORDER BY year_observed;
```

