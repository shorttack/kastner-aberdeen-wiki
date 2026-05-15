---
title: "Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos"
slug: kastner-tandem-topgun-et1-analysis-1987--a3a09c
page_type: study
author: "Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988)"
date: "1987-08-11/1988-01-13"
study_type: internal-engineering-memo
subject_domain: "fault-tolerant-OLTP-benchmarks"
methodology: "Primary-source PSK-authored technical memos analyzing Tandem 32-VLX TopGun benchmark (208 tps) — first as Stratus marketing-support manager (Aug 1987 working document), then as DEC Corporate Systems Group (Jan 1988) re-applying the analysis to a Digital response."
importance: high
importance_rationale: "Two PSK-authored technical memos covering the same benchmark across the Stratus-to-DEC career transition; rare archival record of PSK's competitive-benchmark technique and judgement as marketing-support manager."
relevance: high
relevance_rationale: "Direct primary-source PSK technical writing on debit-credit benchmarking — methodology that he carried into the Aberdeen Group decades and that informed his TPC-era industry analyst voice."
prescience: medium
prescience_rationale: "PSK's response-time critique (95%/1-sec original ET1 vs Tandem's relaxed 90%/2-sec) anticipates the TPC-A/TPC-C audited-benchmark era that arrived in 1988-1990 — TPC was formally chartered three months after the second memo. PSK's call for an audited 'new OLTP benchmark standard' or 'embracing another OLTP standard such as RAMP-C' essentially predicts TPC's purpose."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 10
obs_count: 10
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos

> Two PSK-authored memos covering the same Tandem TopGun ET1 benchmark across employer transitions: the August 1987 Stratus 'Working Document on the NonStop SQL Benchmark' (co-authored with Raphael Frommer and Clark Hodder, addressed to Bill Foster, Bob Freiburghouse and the Stratus engineering leadership) dissecting Tandem's 32-VLX 208-tps TopGun result; and the January 1988 DEC Corporate Systems Group memo applying the same analysis to plot Digital's response. PSK enumerates Tandem's 'go-fast tricks' (Pathway hacks, TMF buffering, file partitioning so all branch records sit on one ATB disk, mirrored disks worth ~5%, intelligent X.25 cluster controllers, relaxed 90%/2-sec response criterion vs the original 95%/1-sec, randomized arrival times) and concludes Tandem's 8-VLX baseline would deliver ~10-15 tps under conservative ET1 conditions — meaning Stratus and Digital are 'not nearly as bad as corporate mythology would have us believe.' The memo is a rare document of PSK actively analyzing competitive benchmarks across two employers in five months.

**Author:** Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988) · **Date:** 1987-08-11/1988-01-13 · **Type:** internal-engineering-memo
**Importance:** high — *Two PSK-authored technical memos covering the same benchmark across the Stratus-to-DEC career transition; rare archival record of PSK's competitive-benchmark technique and judgement as marketing-support manager.*
**Prescience:** medium — *PSK's response-time critique (95%/1-sec original ET1 vs Tandem's relaxed 90%/2-sec) anticipates the TPC-A/TPC-C audited-benchmark era that arrived in 1988-1990 — TPC was formally chartered three months after the second memo. PSK's call for an audited 'new OLTP benchmark standard' or 'embracing anoth…*

## Entities (10)

- [[clark-hodder|Clark Hodder]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[jim-gray|Jim Gray]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[raphael-frommer|Raphael Frommer]]
- [[robert-freiburghouse|Robert A. Freiburghouse]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[tpc|Transaction Processing Performance Council (TPC)]]
- [[william-e-foster|William E. Foster]]

## Technologies (10)

- [[debit-credit-benchmark|Debit-Credit benchmark (DC/ET1/TP1)]]
- [[digital-rdb|Digital Rdb (relational database)]]
- [[digital-rms|Digital RMS (Record Management Services)]]
- [[ramp-c-benchmark|RAMP-C benchmark]]
- [[tandem-nonstop-sql|Tandem NonStop SQL]]
- [[tandem-pathway|Tandem Pathway TP framework]]
- [[tandem-tmf|Tandem TMF (Transaction Monitoring Facility)]]
- [[tandem-topgun-benchmark|Tandem 'TopGun' benchmark]]
- [[tandem-vlx-cpu|Tandem VLX processor]]
- [[vax-cluster|VAXcluster]]

## Key observations (top 25)

- **1987** — topgun-cluster-tps: 208
- **1987** — single-8cpu-vlx-baseline-tps: 58
- **1987** — conservative-et1-estimate-tps: 10-15
- **1987** — psk-conclusion-stratus-vs-tandem: Tandem is not as awesomely good as first appears. And Digital is not nearly as bad as corporate mythology would have us believe
- **1987** — atb-disk-buffering: 0.4 audit msgs/tx; 0.5 checkpoints/tx
- **1987** — mirroring-throughput-cost: 5
- **1987** — psk-options-list: 6 options: do similar test; ignore; raise stakes; deemphasize ET-1; devise own standard; embrace RAMP-C
- **1987** — linear-scaling-divergence: 8% (16-cpu); 10% (32-cpu)
- **1988** — stratus-to-dec-five-months: Stratus Aug 1987 -> DEC Corporate Systems Group Jan 1988
- **1988** — psk-call-for-standard: Devising our own, new OLTP benchmark standard

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'kastner-tandem-topgun-et1-analysis-1987--a3a09c' ORDER BY year_observed;
```

