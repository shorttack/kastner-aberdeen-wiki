---
title: "Microsoft Scalability Day: The Emperor Has No Clothes"
slug: ntscaling-07177f
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1997"
study_type: market-study
subject_domain: "Windows NT Enterprise Scalability"
methodology: "expert-opinion, competitive-analysis"
importance: low
importance_rationale: "Brief companion piece providing a pointed analyst critique of NT enterprise scalability claims; low standalone importance but historically illustrative of 1990s analyst skepticism toward Windows NT."
relevance: medium
relevance_rationale: "Directly relevant to understanding analyst positioning on Windows NT versus Unix/mainframe during the late 1990s platform wars."
prescience: high
prescience_rationale: "Kastner's skepticism about NT enterprise scalability proved prescient; Windows Server did not dominate Fortune 500 mission-critical workloads for many years and Unix remained entrenched."
license: CC-BY-4.0
tier: 1
entity_count: 3
tech_count: 5
obs_count: 7
tags: [type/study, importance/low, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Microsoft Scalability Day: The Emperor Has No Clothes

> A short Aberdeen Group commentary assessing Microsoft's claims at its Scalability Day event circa 1997. Kastner argues NT remains unsuitable for Fortune 500 enterprise environments and that partner solutions are required to achieve high transaction rates, availability, and fault tolerance. He concludes that Unix, AS/400, and mainframes remain the legitimate province of the enterprise high-end.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1997 · **Type:** market-study
**Importance:** low — *Brief companion piece providing a pointed analyst critique of NT enterprise scalability claims; low standalone importance but historically illustrative of 1990s analyst skepticism toward Windows NT.*
**Prescience:** high — *Kastner's skepticism about NT enterprise scalability proved prescient; Windows Server did not dominate Fortune 500 mission-critical workloads for many years and Unix remained entrenched.*

## Entities (3)

- [[aberdeen-group|Aberdeen Group]]
- [[microsoft|Microsoft]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (5)

- [[as400|IBM AS/400]]
- [[ibm-mainframe-zarch|IBM zSeries Mainframe (z900/z990)]]
- [[microsoft-backoffice|Microsoft BackOffice]]
- [[microsoft-windows-nt|Microsoft Windows NT]]
- [[unix|UNIX (various)]]

## Key observations (top 25)

- **1997** — NT enterprise readiness: Not a panacea from desktop to enterprise, particularly for Fortune 500 complex environments
- **1997** — NT maximum concurrent-user deployments observed: Considerable difficulty finding sites with more than a few hundred users
- **1997** — Recommended NT enterprise strategy: Use Microsoft partners for enterprise-class software and services; beware all-Microsoft solutions
- **1997** — NT suitability: Best suited to departmental applications only
- **1997** — Enterprise high-end platform assessment: Unix, AS/400, and mainframe legitimately remain the province of the enterprise high-end
- **1997** — NT improvement trajectory: NT will be better in 1998 than it is now
- **1998** — NT improvement trajectory - outcome: unknown

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ntscaling-07177f' ORDER BY year_observed;
```

