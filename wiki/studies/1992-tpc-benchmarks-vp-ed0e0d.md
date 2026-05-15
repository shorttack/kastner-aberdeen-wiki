---
title: "Better Performance and Lower Prices Through TPC Benchmarks"
slug: 1992-tpc-benchmarks-vp-ed0e0d
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1992-03"
study_type: white-paper
subject_domain: "transaction processing benchmarks"
methodology: "market analysis; benchmark review; vendor comparison"
importance: high
importance_rationale: "Full manuscript of Aberdeen's seminal TPC benchmark viewpoint. The complete published text; excerpted slide versions are already in the archive as dectp92, hptpc92, ibmtpc92, tpc2-92."
relevance: medium
relevance_rationale: "Benchmark methodology still instructive for evaluating competitive performance claims."
prescience: high
prescience_rationale: "Kastner's analysis of vendor trajectory proved largely correct: Unix/RDBMS suppliers emerged as price-performance leaders, VAX faded, and TPC benchmarks became lasting industry standards."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 9
obs_count: 32
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Better Performance and Lower Prices Through TPC Benchmarks

> Aberdeen Technology Viewpoint examining TPC benchmarks (TPC-A, TPC-B, TPC-C) as the de facto standard for measuring commercial performance and price-performance. Covers the history of Debit/Credit benchmarking, TPC formation in 1988, and detailed vendor comparisons across DEC VAX, HP, IBM AS/400, Sequent, Bull, Sun, and others. Concludes that TPC-A competition has driven a five-fold improvement in price-performance over two years and advocates that buyers mandate TPC-A results in RFPs.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1992-03 · **Type:** white-paper
**Importance:** high — *Full manuscript of Aberdeen's seminal TPC benchmark viewpoint. The complete published text; excerpted slide versions are already in the archive as dectp92, hptpc92, ibmtpc92, tpc2-92.*
**Prescience:** high — *Kastner's analysis of vendor trajectory proved largely correct: Unix/RDBMS suppliers emerged as price-performance leaders, VAX faded, and TPC benchmarks became lasting industry standards.*

## Entities (8)

- [[aberdeen-group|Aberdeen Group]]
- [[bull|Groupe Bull]]
- [[digital-equipment|Digital Equipment Corporation]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sequent-computer-systems|Sequent Computer Systems]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (9)

- [[as400|IBM AS/400]]
- [[digital-vax|Digital VAX/OpenVMS]]
- [[hp-3000|HP 3000]]
- [[hp-9000|HP 9000]]
- [[oltp|Online Transaction Processing (OLTP)]]
- [[oracle-rdb|Oracle Rdb]]
- [[rdbms|Relational Database (RDBMS)]]
- [[tpc-benchmark|TPC (Transaction Processing Performance Council) Benchmarks]]
- [[unix-server|Unix Enterprise Servers]]

## Key observations (top 25)

- **1992** — TPC description: De facto industry standard for measuring commercial performance and price-performance
- **1990** — First TPC-A result (HP 960) K$/TPS-A: 36.5
- **1992** — Best TPC-A price-performance Q1 1992 K$/TPS-A: 7.7
- **1992** — Price-performance improvement since 1990: 79% industry drop in K$/TPS-A
- **1992** — TPC-A price-performance leadership changes in Q1 1992: 6 changes in 2.5 months involving 6 different suppliers
- **1992** — Best TPC-A price-performance leader performance (Q1 1992): 28 TPS-A for $214K total system cost
- **1992** — MicroVAX 3100-80 TPC-A price-performance K$/TPS-A: 7.69
- **1992** — MicroVAX 4000-300 TPC-A price-performance K$/TPS-A: 10.71
- **1992** — VAX 6000-640 SMP TPC-A throughput TPS-A: 200+
- **1988** — VAX 8830 Debit/Credit throughput TPS: 27
- **1992** — VAX TPC-A price-performance improvement since Aug 1990: 50% throughput increase; 3x price-performance improvement
- **1992** — VAX 4000-300 price-performance improvement over 20 months K$/TPS-A: From 31.90 to 10.71 (threefold improvement)
- **1992** — VAX 4000-300 cost reduction components: Disk -24%; memory -25%; 32MB less memory required; 25% service discount
- **1992** — IBM AS/400 E70 vs E10 price-performance premium: 77% more expensive at high-end E70 vs entry-level E10
- **1992** — HP 3000 midrange TPC price-performance improvement since Jan 1990: 61% price-performance improvement; 171% performance improvement
- **1992** — Bull DPX/2 TPC-A leadership: Led TPC-A price-performance below $10K/TPS-A in Q1 1992
- **1992** — Sun Sparcserver TPC-A leadership: Led TPC-A price-performance in Q1 1992
- **1992** — TPC membership count: Over 40 members
- **1992** — TPC-C benchmark status: Under public review; expected approval summer 1992
- **1992** — TPC-A terminal scaling rule floor estimate K$/TPS-A: ~2.5K terminals-only at $250/terminal minimum cost
- **1985** — Debit/Credit benchmark origin: Published 1985 in Datamation anonymously by ~20 academics and industry developers
- **1988** — TPC formation year: Late 1988
- **1992** — Digital TPC-A price-performance range across full VAX line: Within 20% from MicroVAX 3100 entry-level to VAX 6000-640
- **1992** — Aberdeen TPC benchmark auditor role: Aberdeen Group has audited several TPC benchmarks
- **1992** — HP ALLBASE RDBMS TPC-A/B status: Advanced from also-ran to serious-contender

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1992-tpc-benchmarks-vp-ed0e0d' ORDER BY year_observed;
```

