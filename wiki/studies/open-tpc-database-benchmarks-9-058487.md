---
title: "Open: TPC Database Benchmarks — Truth and Benchmarks"
slug: open-tpc-database-benchmarks-9-058487
page_type: study
author: "Nancy Cohen (Open Magazine)"
date: "2005-03-14"
study_type: news-article
subject_domain: "commercial-benchmarks"
methodology: "industry-analysis, expert-opinion"
importance: high
importance_rationale: "Strong primary-source summary of the case for TPC from Kastner — a long-time TPC-watcher — and captures the TPC-E / web-service / decision-support roadmap circa 2005."
relevance: high
relevance_rationale: "TPC benchmarks remain industry standard (TPC-C, TPC-E, TPC-H, TPC-DS); arguments here still referenced."
prescience: high
prescience_rationale: "Kastner framing held: TPC-E launched 2007, TPC-DS expanded decision-support benchmarks, and TPC remained the gold-standard commercial benchmark organization."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 5
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Open: TPC Database Benchmarks — Truth and Benchmarks

> Open Magazine feature (2005-03-14) on the Transaction Processing Performance Council (TPC) and why commercial buyers trust its database benchmarks. Peter Kastner is identified unusually as 'analyst for Vericours' rather than Aberdeen. Kastner credits TPC as an independence lever that has kept vendors on their toes, describes the 'lies, damned lies, and benchmarks' legacy before TPC's 1988 founding, and attributes 100-fold application-performance improvements to TPC-induced competition. He calls TPC benchmarks 'the gold standard of commercial benchmarks.'

**Author:** Nancy Cohen (Open Magazine) · **Date:** 2005-03-14 · **Type:** news-article
**Importance:** high — *Strong primary-source summary of the case for TPC from Kastner — a long-time TPC-watcher — and captures the TPC-E / web-service / decision-support roadmap circa 2005.*
**Prescience:** high — *Kastner framing held: TPC-E launched 2007, TPC-DS expanded decision-support benchmarks, and TPC remained the gold-standard commercial benchmark organization.*

## Entities (11)

- [[dell-computer|Dell Computer / Dell Inc.]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[ibm|International Business Machines Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[nancy-cohen|Nancy Cohen]]
- [[open-magazine|Open Magazine (open-mag.com)]]
- [[oracle-corp|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]
- [[tpc|Transaction Processing Performance Council]]
- [[vericours|Vericours]]

## Technologies (5)

- [[commercial-rdbms|Commercial Relational Database Management Systems]]
- [[tpc-c|TPC-C OLTP benchmark]]
- [[tpc-e|TPC-E brokerage OLTP benchmark]]
- [[tpc-h|TPC-H decision-support benchmark]]
- [[tpc-web-service-benchmark|TPC Web-Service Benchmark (proposed)]]

## Key observations (top 25)

- **2005** — TPC as confidence floor: The TPC is a place where business IT seekers can go with greater confidence for numbers without fear of stacked configuration decks and misleading numbers.
- **2005** — Pre-TPC benchmark era: Every vendor had specific tests, but buyers were confused and sometimes misled. There was lots of truth in the maxim 'Lies, damned lies, and benchmarks.'
- **2005** — 100-fold performance improvement: As a result of TPC-induced competition, the industry has seen application-level performance improvements of 100-fold.
- **2005** — TPC engineering rigor: The secret to the success of TPC benchmarks is that the specifications are set by a committee of benchmark-jaded engineers from Dell, HP, IBM, Sun, Oracle, and Microsoft. These men and women fight competitively every day — and lots of nights.
- **2005** — Gold standard framing: The combination of detailed benchmark standards, an independent audit, and in-the-sunlight peer review makes the TPC benchmarks the gold standard of commercial benchmarks.
- **2005** — TPC-E roadmap: TPC announced an OLTP benchmark — TPC-E — with expanded workload modeled on brokerage houses, reflecting more contemporary workloads than TPC-C.
- **2005** — Proposed Web-service benchmark: TPC announced a proposed Web-service benchmark with database interactions and durable message-queue operations displaying ACID properties against a commercial application server.
- **2005** — Proposed decision-support benchmark: TPC announced a proposed decision-support benchmark measuring a randomized set of transactions.
- **2005** — Kastner affiliation [REVIEW]: Kastner cited as 'analyst for Vericours' — not Aberdeen Group. Likely a post-Aberdeen consulting affiliation circa 2005-2007; may also reflect editorial error.
- **2007** — TPC-E formally launched: TPC-E was formally released in February 2007 — fulfilling the 2005 roadmap Kastner previewed.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'open-tpc-database-benchmarks-9-058487' ORDER BY year_observed;
```

