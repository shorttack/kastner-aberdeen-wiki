---
title: "Competitors Find Fault With Tolerant's Performance Claim — Tandem, Stratus argue Eternity performance figures"
slug: informationweek-tolerant-debitcredit-198-4f3b26
page_type: study
author: "Paul E. Schindler Jr. (InformationWEEK staff)"
date: "1986-01-20"
study_type: trade-press-article
subject_domain: "transaction-processing-benchmarks"
methodology: "news-reporting, expert-interview, vendor-data-analysis"
importance: medium
importance_rationale: "Captures the early TP1/ET1 (debit-credit) benchmark wars of 1985-86 — a precursor to the more rigorous TPC-A and TPC-C benchmarks (1989+). Shows Stratus's market position during Kastner's last year there (he transitioned to DEC in 1985-86) and validates the competitive set."
relevance: medium
relevance_rationale: "TPS benchmarking remains foundational to OLTP/database evaluation; modern TPC-C, YCSB, and Sysbench descend directly from the ET1/TP1 debit-credit tradition. Tolerant the company is gone but the methodological controversy (vendor-curated benchmarks vs. independent measurement) persists."
prescience: medium
prescience_rationale: "Serlin's recommendation that 'users run their own benchmarks' anticipated the rise of TPC and other independent benchmark consortia (TPC founded 1988). The article also correctly identifies the unsustainability of vendor-driven benchmark wars."
license: CC-BY-4.0
tier: 2
entity_count: 10
tech_count: 8
obs_count: 11
tags: [type/study, importance/medium, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Competitors Find Fault With Tolerant's Performance Claim — Tandem, Stratus argue Eternity performance figures

> InformationWEEK page 22 (January 20, 1986) reports on a controversy over Tolerant Systems' Eternity transaction-processing performance claims. Tolerant claims its Eternity system at $23,800 per TPS beats Tandem ($42,200) and Stratus ($68,700) using TP1/ET1 (debit-credit) benchmark figures from Datapro and Omri Serlin's ITOM International newsletter. Tandem responds with internal numbers showing $20,800/TPS using configurations more comparable to Tolerant's. Serlin himself published Stratus internal figures showing $23,100/TPS. Serlin says 'these measurements are at best ambiguous and always the subject of intense controversy' and recommends users run their own benchmarks. Background: Tolerant Transaction Systems Inc. founder Eli Alon promised Unix-based fault-tolerant processing in 1985; firm dropped Alon and the word 'transaction' from its name. With release 5.0 of its Unix-like OS, Tolerant introduced multi-System-Building-Block (SBB) fault tolerance using National Semiconductor 32016 chips. Marketing director Shirley Henry says major vendors will resell Eternity. Confirms Tandem as market leader and Stratus as 'distant second-place competitor' in OLTP fault-tolerant computing.

**Author:** Paul E. Schindler Jr. (InformationWEEK staff) · **Date:** 1986-01-20 · **Type:** trade-press-article
**Importance:** medium — *Captures the early TP1/ET1 (debit-credit) benchmark wars of 1985-86 — a precursor to the more rigorous TPC-A and TPC-C benchmarks (1989+). Shows Stratus's market position during Kastner's last year there (he transitioned to DEC in 1985-86) and validates the competitive set.*
**Prescience:** medium — *Serlin's recommendation that 'users run their own benchmarks' anticipated the rise of TPC and other independent benchmark consortia (TPC founded 1988). The article also correctly identifies the unsustainability of vendor-driven benchmark wars.*

## Entities (10)

- [[datapro-research|Datapro Research Corporation]]
- [[eli-alon|Eli Alon]]
- [[informationweek-magazine|InformationWEEK magazine]]
- [[itom-international|ITOM International Co.]]
- [[national-semiconductor|National Semiconductor Corp.]]
- [[omri-serlin|Omri Serlin]]
- [[shirley-henry|Shirley Henry]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[tolerant-systems|Tolerant Systems Inc. (formerly Tolerant Transaction Systems)]]

## Technologies (8)

- [[ns-32016|National Semiconductor 32016]]
- [[stratus-continuous-processing|Stratus Continuous Processing]]
- [[system-building-block-sbb|Tolerant System Building Block (SBB)]]
- [[tandem-nonstop|Tandem NonStop architecture]]
- [[tolerant-eternity|Tolerant Eternity series]]
- [[tolerant-eternity-os-50|Tolerant Eternity OS Release 5.0]]
- [[tp1-et1-debit-credit|TP1/ET1 (Debit-Credit) Benchmark]]
- [[transactions-per-second-tps|Transactions Per Second (TPS) per processor]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'informationweek-tolerant-debitcredit-198-4f3b26' ORDER BY year_observed;
```

