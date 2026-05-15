---
title: "New LIMD Technology: Speed Plus Real-World Experience"
slug: aberdeen-1995-limd-technology
page_type: study
author: "Aberdeen Group"
date: "1995-12-01"
study_type: market-study
subject_domain: "database-performance-technology"
methodology: "industry-analysis,benchmarking,field-research"
importance: high
importance_rationale: "Pioneering analysis of large-scale in-memory database technology at 64-bit RISC adoption inflection; Aberdeen quantified 10-100x performance improvements and documented the TPC-C benchmark correlation between RAM and throughput that became foundational to modern in-memory computing."
relevance: high
relevance_rationale: "LIMD's core insight—that main memory databases offer order-of-magnitude performance gains—remains highly relevant; SAP HANA (2011) is the direct commercial realization; modern in-memory databases (Redis, VoltDB, MemSQL/SingleStore) confirm Aberdeen's 1995 architectural thesis."
prescience: high
prescience_rationale: "Aberdeen correctly identified that 64-bit LIMD would deliver 10-100x performance improvements and that ISV apps would be rewritten for LIMD over 2 years; the prediction of database size growth and in-memory as standard proved fully correct; SAP HANA's 2011 launch validated the prescience at scale."
license: CC-BY-4.0
tier: 1
entity_count: 14
tech_count: 20
obs_count: 52
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# New LIMD Technology: Speed Plus Real-World Experience

> Technology Viewpoint analyzing Large-Scale In-Memory Database (LIMD) technology, examining how 64-bit architectures and large main memories deliver 10-100x performance improvements for data warehousing, OLTP, and decision support.

**Author:** Aberdeen Group · **Date:** 1995-12-01 · **Type:** market-study
**Importance:** high — *Pioneering analysis of large-scale in-memory database technology at 64-bit RISC adoption inflection; Aberdeen quantified 10-100x performance improvements and documented the TPC-C benchmark correlation between RAM and throughput that became foundational to modern in-memory computing.*
**Prescience:** high — *Aberdeen correctly identified that 64-bit LIMD would deliver 10-100x performance improvements and that ISV apps would be rewritten for LIMD over 2 years; the prediction of database size growth and in-memory as standard proved fully correct; SAP HANA's 2011 launch validated the prescience at scale.*

## Entities (14)

- [[aberdeen-group|Aberdeen Group]]
- [[aberdeen-group-publisher|Aberdeen Group (publisher)]]
- [[ca-ingres|CA-Ingres]]
- [[digital-equipment-corporation|Digital Equipment Corporation]]
- [[hewlett-packard-hp|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[informix|Informix]]
- [[merrill-lynch|Merrill Lynch]]
- [[oracle-corporation|Oracle Corporation]]
- [[silicon-graphics-inc-sgi|Silicon Graphics Inc. (SGI)]]
- [[software-ag|Software AG]]
- [[sun-microsystems|Sun Microsystems]]
- [[sybase|Sybase]]
- [[tandem-computers|Tandem Computers]]

## Technologies (20)

- [[32-bit-computing-architecture|32-bit computing architecture]]
- [[64-bit-computing-architecture|64-bit computing architecture]]
- [[alpha-chip-dec-alpha|Alpha chip (DEC Alpha)]]
- [[atm-asynchronous-transfer-mode-networking|ATM (Asynchronous Transfer Mode) networking]]
- [[informix-online-7-x-8-0|Informix-OnLine 7.x / 8.0]]
- [[limd-large-scale-in-memory-database|LIMD (Large-Scale In-Memory Database)]]
- [[memory-channel-bus|Memory Channel bus]]
- [[mips-64-bit-sgi-r8000-r10000|MIPS 64-bit (SGI R8000/R10000)]]
- [[mpp-massively-parallel-processing|MPP (Massively Parallel Processing)]]
- [[nonstop-guardian-tandem|NonStop Guardian (Tandem)]]
- [[oracle-rdb|Oracle Rdb]]
- [[oracle-rdbms-7-x|Oracle RDBMS 7.x]]
- [[pa-risc-hp-pa-8000|PA-RISC (HP PA-8000)]]
- [[powerpc-64-bit-ibm-motorola|PowerPC 64-bit (IBM/Motorola)]]
- [[smp-symmetric-multiprocessing|SMP (Symmetric MultiProcessing)]]
- [[sybase-iq-accelerator|Sybase IQ Accelerator]]
- [[sybase-system-11|Sybase System 11]]
- [[tpc-c-benchmark|TPC-C benchmark]]
- [[ultrasparc-64-bit-sun|UltraSPARC 64-bit (Sun)]]
- [[vlm64-architecture|VLM64 architecture]]

## Key observations (top 25)

- **1995** — database-size-growth-rate: 
- **1995** — large-databases-count-growth: 7 fold-increase
- **1995** — databases-over-100GB-count: 0 count
- **1995** — databases-over-100GB-count: 100 count
- **1995** — performance-improvement-range: 10 x-times
- **1995** — performance-improvement-range: 100 x-times
- **1995** — limd-min-memory-threshold: 5 gigabytes
- **1995** — 32-bit-memory-ceiling: 2 gigabytes
- **1995** — tpc-c-score: 1300 tpmC-per-GB
- **1995** — non-limd-scaling-ceiling: 5000 tpmC
- **1995** — digital-alpha-tpc-c-range-low: 10000 tpmC
- **1995** — digital-alpha-tpc-c-range-high: 12000 tpmC
- **1995** — real-world-performance-improvement-low: 20 x-times
- **1995** — real-world-performance-improvement-high: 40 x-times
- **1995** — 5-way-join-speedup: 105 x-times
- **1995** — max-concurrent-users-single-server: 10000 users
- **1995** — backup-throughput: 100 GB-per-hour
- **1995** — digital-oracle-tpc-c-record: 11456 tpmC
- **1995** — digital-oracle-price-performance: 286 USD-per-tpmC
- **1995** — alpha-8200-max-memory: 6 gigabytes
- **1995** — alpha-8400-max-memory: 14 gigabytes
- **1995** — alpha-8200-max-cpus: 6 CPUs
- **1995** — alpha-8400-max-cpus: 12 CPUs
- **1995** — alpha-8x00-max-storage: 8.5 terabytes
- **1995** — memory-channel-bandwidth: 100 MB-per-second

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-limd-technology' ORDER BY year_observed;
```

