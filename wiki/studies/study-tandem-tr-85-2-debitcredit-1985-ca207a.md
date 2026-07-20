---
title: "A Measure of Transaction Processing Power (Tandem Technical Report 85.2)"
slug: "study-tandem-tr-85-2-debitcredit-1985-ca207a"
page_type: "study"
tags: ["type/study", "collection/benchmark"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "tandem-tr-85-2-debitcredit-1985-ca207a"
author: "Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers)"
date: "1985-02-01"
pub_year: 1985
type: "benchmark"
subject_domain: "transaction-processing-benchmarks"
methodology: "benchmark-specification, industry-consensus"
source_file: "A-Measure-of-Transaction-Processing-Power-Tandem-85.2-4.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 2.82
prescience_obs_count: 11
---

# A Measure of Transaction Processing Power (Tandem Technical Report 85.2)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=4.00 over 11 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.27 over 11 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Tandem Technical Report 85.2 (February 1985) by 'Anon et al' — the foundational transaction-processing benchmark paper that defined Sort, Scan, and DebitCredit (ET-1/TP-1) and introduced the Transactions Per Second (TPS) and 5-year capital-cost price/performance metrics. A condensed version appeared in Datamation April 1, 1985. The 'Anon et al' byline concealed a collaboration led by Jim Gray (then at Tandem) with ~24 academics, vendors, and users. This paper is the direct ancestor of the Transaction Processing Performance Council (TPC) benchmarks (TPC-A, TPC-B, TPC-C) and is foundational to Kastner's subsequent career as an OLTP/benchmarks analyst at Stratus and Aberdeen Group.


_Published 1985, author **Anon et al (Jim Gray and ~24 TP-industry co-authors; Tandem Computers)**, type **benchmark**._


## Top observations

- Simple interactive transaction processing application used to define TPS throughput measure `[ps=5]`
- Transactions Per Second — standard throughput metric defined to enable cross-vendor comparison `[ps=5]`
- Whetstones, MIPS, MegaFLOPS, GigaLIPS all focus on CPU — they do not capture TP-system features `[ps=5]`
- Paper predicts standard TPS metric will aid system pricing, sales, and purchase `[ps=5]`
- Transaction Processing Performance Council formed 1988; TPC-A standardized DebitCredit-style benchmark published 1989 `[ps=5]`
- Measures system input/output performance via elapsed batch time `[ps=3]`
- Bulk-data-movement utility benchmark measuring I/O `[ps=3]`
- Five-year capital cost of system equipment exclusive of communications lines, terminals, development and operations `[ps=0]`
- 'Anon et al' — two dozen people active in transaction processing including academics, vendors, and users `[ps=0]`
- Condensed version published in Datamation April 1, 1985 `[ps=0]`
- Kastner (then at Stratus) used ET-1/TP-1 as the standard Stratus-vs-Tandem price/performance comparison framework — see 1986 ET1-vs-TP1 dossier `[ps=0]`
