---
title: "Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus"
slug: stratus-et1-functional-spec-and-benchmar-0c3172
page_type: study
author: "Stratus Computer (engineering and benchmark documents)"
date: "1986"
study_type: internal-engineering-corpus
subject_domain: "transaction-processing/benchmark-methodology"
methodology: "vendor-engineering-spec-plus-benchmark-results"
importance: high
importance_rationale: "Authoritative Stratus engineering primary-source clarifying the TP1-vs-ET1 distinction (a frequent industry confusion) and documenting Stratus's 1986 ET1 methodology in response to Tandem's 1985 TXP ET1 publicity (FTSN-33)."
relevance: high
relevance_rationale: "Resolves the TP1/ET1 confusion across the entire Stratus corpus and gives Stratus's official 1986 ET1 methodology — the engineering basis for any 1986+ Stratus competitive benchmark claim Kastner or others would later make."
prescience: medium
prescience_rationale: "Stratus's 1986 critique of MIPS/Whetstone for OLTP and emphasis on standardized transaction benchmarks anticipated the founding of the TPC in 1988 and the dominance of TPC-A/B/C through the 1990s, then the modern TPC-E / YCSB / cloud-DB benchmark era."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 5
obs_count: 7
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Stratus ET1 Functional Specification (May 1, 1986) and Stratus Transaction Processing Benchmarks (June 26, 1986) — Consolidated Stratus 1986 ET1 Corpus

> Two-document Stratus 1986 ET1 corpus consolidating: (1) the Stratus ET1 Functional Specification (May 1, 1986) — Stratus's internal definition of the Anon-et-al ET1 'debit-credit' transaction (Read X.25, Read+Rewrite Account/Teller/Branch, Write History sequential, Write X.25 acknowledgement; 1,000 branches, 10K tellers, 10M accounts, 100 tps peak); explicitly clarifies that 'TP1 (Stratus internal) and ET1 are NOT the same benchmark or even a variation' — TP1 was Stratus's earlier internal benchmark, not based on ET1 or debit-credit, with different I/O profile and different database; vendor comparisons based on TP1-vs-ET1 results are 'invalid'. (2) Stratus Transaction Processing Benchmarks (June 26, 1986) — Stratus's official ET1 benchmark results, framed within a broader critique of MIPS and Whetstone benchmarks for OLTP, a quantitative TP1-vs-ET1 comparison (TP1 does ~4x as many physical I/Os as ET1; logical I/O ratio 7:8 but physical I/O ratio dominates due to small relative file caching), and detailed ET1 benchmark methodology (PL1 requester/server with Stratus TPF; 85%/15% local-vs-remote branch traffic model; multimodule dispatch). This corpus is Stratus's direct response to the 1985 Tandem TXP ET1 marketing barrage (Batch 25 study #6 / Serlin FTSN-33).

**Author:** Stratus Computer (engineering and benchmark documents) · **Date:** 1986 · **Type:** internal-engineering-corpus
**Importance:** high — *Authoritative Stratus engineering primary-source clarifying the TP1-vs-ET1 distinction (a frequent industry confusion) and documenting Stratus's 1986 ET1 methodology in response to Tandem's 1985 TXP ET1 publicity (FTSN-33).*
**Prescience:** medium — *Stratus's 1986 critique of MIPS/Whetstone for OLTP and emphasis on standardized transaction benchmarks anticipated the founding of the TPC in 1988 and the dominance of TPC-A/B/C through the 1990s, then the modern TPC-E / YCSB / cloud-DB benchmark era.*

## Entities (5)

- [[datamation-magazine|Datamation magazine]]
- [[ibm|IBM Corporation]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[tpc-org|Transaction Processing Performance Council (TPC)]]

## Technologies (5)

- [[benchmark-physical-vs-logical-io|Physical-vs-Logical I/O Distinction in TP Benchmarks]]
- [[et1-debit-credit|ET1 Debit-Credit Benchmark]]
- [[stratus-et1-implementation|Stratus ET1 Implementation (May 1, 1986)]]
- [[stratus-tp1-benchmark|Stratus TP-1 Internal Transaction Benchmark]]
- [[stratus-tpf|Stratus TPF (Transaction Processing Facility)]]

## Key observations (top 25)

- **1986** — ET1 transaction profile: Read X.25 + Read/Rewrite Account/Teller/Branch + Write History sequential + Write X.25 ack
- **1986** — Database scale: 2M accounts (200 MB), 2K tellers, 200 branches (per module); access patterns: Account indexed, Teller relative random, Branch relative random
- **1986** — Multi-module branch model: 85% transactions hit current process branch; remaining 15% dispatched to other modules
- **1986** — TP1-vs-ET1 distinction: TP1 and ET1 are NOT the same benchmark or even a variation; vendor comparisons based on TP1-vs-ET1 results are invalid
- **1986** — Physical I/O ratio: TP1 does 12 physical I/Os per tx; ET1 does 3 — TP1 does ~4x as many physical I/Os as ET1
- **1986** — TP1 profile: 150ms CPU loop + 5 indexed reads + 2 rewrites + 1 sequential log write; PL1 requester, COBOL server; Stratus TPF
- **1986** — Critique of MIPS/Whetstone: MIPS and Whetstone are inadequate for OLTP; with multiprocessor, MIPS changes as I/O processors are added; transaction benchmarks needed

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-et1-functional-spec-and-benchmar-0c3172' ORDER BY year_observed;
```

