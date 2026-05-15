---
title: "A Measure of Transaction Processing Power (Tandem Technical Report 85.2)"
slug: tandem-tr-85-2-debitcredit-1985-ca207a
page_type: study
author: "Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers)"
date: "1985-02-01"
study_type: benchmark
subject_domain: "transaction-processing-benchmarks"
methodology: "benchmark-specification, industry-consensus"
importance: high
importance_rationale: "Single most influential benchmark paper in OLTP history — it created the methodology that became TPC, shaping 40+ years of database and transaction-processing system marketing, purchasing, and engineering."
relevance: high
relevance_rationale: "TPC-C (direct descendant of DebitCredit) is still the reference OLTP benchmark in 2026; cost-of-ownership metrics derived from this paper remain industry standard."
prescience: high
prescience_rationale: "Predicted that a standard TPS/price-per-tps metric would become essential to system pricing, sales, and purchase — proven correct via TPC council formation (1988) and subsequent universal adoption across DBMS vendors."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 7
obs_count: 11
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# A Measure of Transaction Processing Power (Tandem Technical Report 85.2)

> Tandem Technical Report 85.2 (February 1985) by 'Anon et al' — the foundational transaction-processing benchmark paper that defined Sort, Scan, and DebitCredit (ET-1/TP-1) and introduced the Transactions Per Second (TPS) and 5-year capital-cost price/performance metrics. A condensed version appeared in Datamation April 1, 1985. The 'Anon et al' byline concealed a collaboration led by Jim Gray (then at Tandem) with ~24 academics, vendors, and users. This paper is the direct ancestor of the Transaction Processing Performance Council (TPC) benchmarks (TPC-A, TPC-B, TPC-C) and is foundational to Kastner's subsequent career as an OLTP/benchmarks analyst at Stratus and Aberdeen Group.

**Author:** Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers) · **Date:** 1985-02-01 · **Type:** benchmark
**Importance:** high — *Single most influential benchmark paper in OLTP history — it created the methodology that became TPC, shaping 40+ years of database and transaction-processing system marketing, purchasing, and engineering.*
**Prescience:** high — *Predicted that a standard TPS/price-per-tps metric would become essential to system pricing, sales, and purchase — proven correct via TPC council formation (1988) and subsequent universal adoption across DBMS vendors.*

## Entities (6)

- [[datamation|Datamation magazine]]
- [[jim-gray|Jim Gray]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[tpc|Transaction Processing Performance Council (TPC)]]

## Technologies (7)

- [[5-year-tco|5-Year Capital Cost (TCO) metric]]
- [[debitcredit-et1-tp1|DebitCredit / ET-1 / TP-1 benchmark]]
- [[scan-benchmark|Scan benchmark]]
- [[sort-benchmark|Sort benchmark]]
- [[tpc-a|TPC-A benchmark]]
- [[tpc-c|TPC-C benchmark]]
- [[tps|Transactions Per Second (TPS) metric]]

## Key observations (top 25)

- **1985** — DebitCredit benchmark definition: Simple interactive transaction processing application used to define TPS throughput measure
- **1985** — Sort benchmark purpose: Measures system input/output performance via elapsed batch time
- **1985** — Scan benchmark purpose: Bulk-data-movement utility benchmark measuring I/O
- **1985** — Price metric definition: Five-year capital cost of system equipment exclusive of communications lines, terminals, development and operations
- **1985** — TPS throughput measure: Transactions Per Second — standard throughput metric defined to enable cross-vendor comparison
- **1985** — Traditional metrics inadequate: Whetstones, MIPS, MegaFLOPS, GigaLIPS all focus on CPU — they do not capture TP-system features
- **1985** — TPS will become valuable sales/pricing aid: Paper predicts standard TPS metric will aid system pricing, sales, and purchase
- **1985** — Paper authorship: 'Anon et al' — two dozen people active in transaction processing including academics, vendors, and users
- **1985** — Condensed publication: Condensed version published in Datamation April 1, 1985
- **1988** — TPC formation and TPC-A adoption: Transaction Processing Performance Council formed 1988; TPC-A standardized DebitCredit-style benchmark published 1989
- **1985** — Kastner's use of the benchmark: Kastner (then at Stratus) used ET-1/TP-1 as the standard Stratus-vs-Tandem price/performance comparison framework — see 1986 ET1-vs-TP1 dossier

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'tandem-tr-85-2-debitcredit-1985-ca207a' ORDER BY year_observed;
```

