---
title: "Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck)"
slug: aberdeen-dops-tpc-1992-deck-bbe78e
page_type: study
author: "Peter S. Kastner (Aberdeen Group)"
date: "1992-02-01"
study_type: market-study
subject_domain: "transaction-processing-benchmarks-distributed-computing"
methodology: "benchmark-analysis, market-tracking, competitive-profiling"
importance: high
importance_rationale: "Documents Aberdeen's DOPS framework — Kastner's signature analytical contribution extending TPC-A beyond single-system benchmarks to distributed, heterogeneous computing environments. Direct ancestor of later client-server benchmarking literature."
relevance: medium
relevance_rationale: "DOPS concept anticipates modern distributed-database benchmarking; TPC-A/B are obsolete (superseded by TPC-C) but the multi-dimensional DOPS analysis pattern persists in modern microservices performance work."
prescience: high
prescience_rationale: "Correctly predicted that distributed heterogeneous systems would require multi-dimensional performance metrics — validated by TPC-C (1992) and later TPC-E, TPC-DS incorporating multi-database, multi-tier architectures."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 12
obs_count: 17
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck)

> Aberdeen Group slide deck from February 1992 (dated '2/92' in footer) presenting TPC-A and TPC-B benchmark results and introducing Aberdeen's DOPS (Distributed Online Processing Systems) framework. Highlights an 85% price decline for equivalent transaction-processing capacity from the DEC VAX 8830 (1988 best-performance, $1,800K 5-year cost for 27 tps) to the VAX 3100-80 (1992 entry-level, $280K). Compares TPC-A at 40 tps-A across Bull DPX/2, DEC VAX 4000-300, HP 9000 957LX, IBM AS/400 D70, and IBM RS/6000 530H (costs $450K-$920K). TPC-B results at 39.7-46 tps-B across Compaq 486/50L, DECsystem 5500, HP 9000 807S, Data General AViiON 4600, MIPS 3330, RS/6000 320H, and Sun SPARC Server 2 (cluster ~$100K). Introduces the DOPS environment (multiple databases, networks, hetero-geneous hardware, mixed OLTP/OLDS) with performance issues including 'Production/Snapshot/Test/Runamuck' database categories.

**Author:** Peter S. Kastner (Aberdeen Group) · **Date:** 1992-02-01 · **Type:** market-study
**Importance:** high — *Documents Aberdeen's DOPS framework — Kastner's signature analytical contribution extending TPC-A beyond single-system benchmarks to distributed, heterogeneous computing environments. Direct ancestor of later client-server benchmarking literature.*
**Prescience:** high — *Correctly predicted that distributed heterogeneous systems would require multi-dimensional performance metrics — validated by TPC-C (1992) and later TPC-E, TPC-DS incorporating multi-database, multi-tier architectures.*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[bull|Bull (Groupe Bull)]]
- [[compaq|Compaq Computer Corporation]]
- [[data-general-corporation|Data General Corporation]]
- [[digital-equipment|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm-corp|IBM Corporation]]
- [[mips-computer|MIPS Computer Systems]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]
- [[tpc|Transaction Processing Performance Council (TPC)]]

## Technologies (12)

- [[bull-dpx-2|Bull DPX/2]]
- [[dops|DOPS — Distributed Online Processing Systems (Aberdeen framework)]]
- [[hp-9000-957lx|HP 9000 957LX]]
- [[ibm-as400-d70|IBM AS/400 D70]]
- [[ibm-rs6000-530h|IBM RS/6000 530H]]
- [[olds|OLDS — Online Decision Support]]
- [[runamuck-db|Runamuck database category]]
- [[tpc-a|TPC-A benchmark]]
- [[tpc-b|TPC-B benchmark]]
- [[vax-3100-80|DEC VAX 3100-80]]
- [[vax-4000-300|DEC VAX 4000-300]]
- [[vax-8830|DEC VAX 8830]]

## Key observations (top 25)

- **1992** — DOPS five properties: End-to-End Response Time; Multiple Databases; Multiple Networks; Heterogeneous Hardware; Mixed OLTP & OLDS
- **1992** — DEC 85% price decline: VAX 8830 (1988 best) $1,800K vs VAX 3100-80 (1992 entry) $280K — 85% decline in 3.5 years for 27 tps with relational database (TPC-A-like)
- **1992** — TPC-A @ 40 tps-A cost: Bull DPX/2 at ~$450K 5-year lifecycle cost — lowest in comparison
- **1992** — AS/400 D70 TCO: IBM AS/400 D70 ~$920K 5-year cost for 40 tps-A — highest in the set
- **1992** — RS/6000 530H TCO: IBM RS/6000 530H ~$620K 5-year cost for 40 tps-A
- **1992** — HP 9000 957LX TCO: HP 9000 957LX ~$680K 5-year cost (49 tps, starred)
- **1992** — VAX 4000-300 TCO: DEC VAX 4000-300 ~$620K 5-year cost for 40 tps-A
- **1992** — Compaq 486/50L TPC-B: Compaq 486/50L: ~$110K 5-year cost at 39.7-46 tps-B
- **1992** — DECsystem 5500 TPC-B: DECsystem 5500: ~$160K — outlier high-cost
- **1992** — HP 9000 807S TPC-B: HP 9000 807S: ~$105K at 39.7-46 tps-B
- **1992** — AViiON 4600 TPC-B: Data General AViiON 4600: ~$102K at 39.7-46 tps-B
- **1992** — MIPS 3330 TPC-B: MIPS 3330: ~$110K at 39.7-46 tps-B
- **1992** — RS/6000 320H TPC-B: IBM RS/6000 320H: ~$107K at 39.7-46 tps-B
- **1992** — Sun SPARC Server 2 TPC-B: Sun SPARC Server 2: ~$102K at 39.7-46 tps-B
- **1992** — DOPS performance issues: Transactions vs Queries; Production/Snapshot/Test/Runamuck DBs; What does the client do? What does the front end do? No textbook answers
- **1992** — DOPS framework value proposition: Distributed heterogeneous environments require new multi-dimensional metrics beyond single-system TPC benchmarks
- **1992** — OLDS/OLTP workload mixing: DOPS must handle mixed OLTP and Online Decision Support workloads — precursor to HTAP (Hybrid Transactional/Analytical Processing)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-dops-tpc-1992-deck-bbe78e' ORDER BY year_observed;
```

