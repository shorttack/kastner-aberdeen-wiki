---
title: "Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus"
slug: "study-stratus-et1-functional-spec-and-benchmar-0c3172"
page_type: "study"
tags: ["type/study", "collection/internal-engineering-corpus"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "stratus-et1-functional-spec-and-benchmar-0c3172"
author: "Stratus Computer (engineering and benchmark documents)"
date: "1986"
pub_year: 1986
type: "internal-engineering-corpus"
subject_domain: "transaction-processing/benchmark-methodology"
methodology: "vendor-engineering-spec-plus-benchmark-results"
source_file: "Stratus-debit-credit-ET1-1986-Tandem-6.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus

> Two-document Stratus 1986 ET1 corpus consolidating: (1) the Stratus ET1 Functional Specification (May 1, 1986) — Stratus's internal definition of the Anon-et-al ET1 'debit-credit' transaction (Read X.25, Read+Rewrite Account/Teller/Branch, Write History sequential, Write X.25 acknowledgement; 1,000 branches, 10K tellers, 10M accounts, 100 tps peak); explicitly clarifies that 'TP1 (Stratus internal) and ET1 are NOT the same benchmark or even a variation' — TP1 was Stratus's earlier internal benchmark, not based on ET1 or debit-credit, with different I/O profile and different database; vendor comparisons based on TP1-vs-ET1 results are 'invalid'. (2) Stratus Transaction Processing Benchmarks (June 26, 1986) — Stratus's official ET1 benchmark results, framed within a broader critique of MIPS and Whetstone benchmarks for OLTP, a quantitative TP1-vs-ET1 comparison (TP1 does ~4x as many physical I/Os as ET1; logical I/O ratio 7:8 but physical I/O ratio dominates due to small relative file caching), and detailed ET1 benchmark methodology (PL1 requester/server with Stratus TPF; 85%/15% local-vs-remote branch traffic model; multimodule dispatch). This corpus is Stratus's direct response to the 1985 Tandem TXP ET1 marketing barrage (Batch 25 study #6 / Serlin FTSN-33).


_Published 1986, author **Stratus Computer (engineering and benchmark documents)**, type **internal-engineering-corpus**._


## Top observations

- Read X.25 + Read/Rewrite Account/Teller/Branch + Write History sequential + Write X.25 ack
- 2M accounts (200 MB), 2K tellers, 200 branches (per module); access patterns: Account indexed, Teller relative random, Branch relative random
- 85% transactions hit current process branch; remaining 15% dispatched to other modules
- TP1 and ET1 are NOT the same benchmark or even a variation; vendor comparisons based on TP1-vs-ET1 results are invalid
- TP1 does 12 physical I/Os per tx; ET1 does 3 — TP1 does ~4x as many physical I/Os as ET1
- 150ms CPU loop + 5 indexed reads + 2 rewrites + 1 sequential log write; PL1 requester, COBOL server; Stratus TPF
- MIPS and Whetstone are inadequate for OLTP; with multiprocessor, MIPS changes as I/O processors are added; transaction benchmarks needed
