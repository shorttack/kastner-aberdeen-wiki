---
title: "AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science"
slug: amd-profile01-64e43b
page_type: study
author: "Peter S. Kastner"
date: "2002-02"
study_type: white-paper
subject_domain: "Semiconductor / PC Processor Marketing"
methodology: "Benchmark analysis, competitive evaluation, literature review of public benchmark results"
importance: medium
importance_rationale: "Captures a significant early-2000s processor marketing controversy that foreshadowed ongoing CPU benchmark debates between AMD and Intel."
relevance: high
relevance_rationale: "Directly authored/associated with Aberdeen Group; rich in competitive analysis and technical critique relevant to the Kastner collection's focus on IT market analysis."
prescience: high
prescience_rationale: "Accurately predicted AMD would abandon GHz-E and introduce a new performance framework; AMD did retire model-number equivalency and moved to the Athlon 64 brand with different positioning by 2003."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 8
obs_count: 17
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# AMD's Gigahertz Equivalency: Confused Customers Accept Bad Science

> Aberdeen Group critiques AMD's Athlon XP Gigahertz Equivalency (GHz-E) marketing strategy, arguing the model-numbering methodology is fundamentally flawed. GHz-E ratings are a snapshot-in-time metric that becomes misleading as benchmarks, operating systems, and Intel processors evolve. The paper documents benchmark disclosure failures (SYSmark 2001 not filed with Bapco), a Media Player bug fix incorporated post-audit, and I/O-inclusive benchmarks misapplied to processor-only comparison. Aberdeen concludes AMD will be forced to abandon GHz-E in 2002 and recommends investigation of SPECcpu 2000 as an alternative framework via the True Performance Initiative.

**Author:** Peter S. Kastner · **Date:** 2002-02 · **Type:** white-paper
**Importance:** medium — *Captures a significant early-2000s processor marketing controversy that foreshadowed ongoing CPU benchmark debates between AMD and Intel.*
**Prescience:** high — *Accurately predicted AMD would abandon GHz-E and introduce a new performance framework; AMD did retire model-number equivalency and moved to the Athlon 64 brand with different positioning by 2003.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[advanced-micro-devices|Advanced Micro Devices (AMD)]]
- [[arthur-andersen|Arthur Andersen]]
- [[bapco|Business Applications Performance Corporation (BAPCo)]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[spec-org|Standard Performance Evaluation Corporation (SPEC)]]

## Technologies (8)

- [[amd-true-performance-initiative|AMD True Performance Initiative (TPI)]]
- [[athlon-xp|AMD Athlon XP Processor]]
- [[intel-pentium4-northwood|Intel Pentium 4 (Northwood)]]
- [[intel-pentium4-willamette|Intel Pentium 4 (Willamette)]]
- [[speccpu-2000|SPECcpu 2000]]
- [[sysmark-2001|BAPCo SYSmark 2001]]
- [[winbench-2000|Winbench 2000]]
- [[windows-xp|Microsoft Windows XP]]

## Key observations (top 25)

- **2001** — GHz Equivalency Model Number Strategy: Athlon XP 2000+ (1.667GHz) rated equivalent to Intel P4 2.0GHz Willamette
- **2002** — SYSmark 2001 Disclosure Failure: No Athlon XP 2000+ results filed with BAPCo as of Feb 15, 2002
- **2001** — SYSmark 2001 Weight in GHz-E Score: ~33.3% (one-half Office Productivity plus two-thirds Content Creation)
- **2002** — Media Player Bug Fix Post-Audit: Benchmark results updated after Arthur Andersen audit to include bug fix favoring AMD
- **2002** — Intel SYSmark Scores vs AMD-Reported Intel Scores: Intel's own Bapco results exceed AMD-reported Intel scores on same processor
- **2002** — Obsolete Benchmark Usage: Winbench 2000 uses DirectX 7.0; AMD/Intel systems tested under DirectX 8.1
- **2002** — GHz-E Abandonment Prediction: AMD will be forced to abandon GHz-E and introduce new rating methodology within 2002
- **2003** — GHz-E Abandonment Actual Outcome: [UNVERIFIED]
- **2001** — True Performance Initiative Announcement: Announced October 2001 as strategic alternative to GHz-E
- **2002** — Northwood Architecture Advantage: P4 2.0A GHz Northwood (130nm, larger cache) outperforms 2.0GHz Willamette at same clock speed
- **2002** — Usage Model Bias: AMD's 1/3-1/3-1/3 office/content/gaming workload mix not representative of many users
- **2002** — I/O Inclusion in Processor Benchmark: Business Winstone 2001 (I/O-intensive system benchmark) included to measure processor performance
- **2002** — Legal Risk from Misleading Marketing: European ads reported GHz-E model numbers as actual GHz; could constitute deceptive trade practices
- **2002** — SPECcpu 2000 as Alternative Benchmark: Aberdeen recommends AMD examine SPECcpu 2000 before advancing TPI
- **2002** — Benchmark Obsolescence Rate: GHz-E methodology projected to break down completely within 90 days of any measurement
- **2002** — Arthur Andersen Audit Limitations: AA attestation covers only the 2000+ model; discrepancies between AA results and Bapco site unexplained
- **2002** — AMD Processor Efficiency Recognition: AMD processors are efficient for many applications and do not need GHz-E to deserve market respect

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'amd-profile01-64e43b' ORDER BY year_observed;
```

