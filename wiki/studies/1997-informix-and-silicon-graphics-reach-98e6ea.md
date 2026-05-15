---
title: "Informix and Silicon Graphics Reach New TPC-C SMP High-Water Mark"
slug: 1997-informix-and-silicon-graphics-reach-98e6ea
page_type: study
author: "Aberdeen Group"
date: "1997-07-01"
study_type: Benchmark Analysis / Product Profile
subject_domain: "Database Performance / OLTP"
methodology: "Benchmark analysis; vendor data; TPC-C results interpretation"
importance: high
importance_rationale: "Documents a genuine benchmark milestone with specific technical data; captures both vendors at a pivotal moment; provides evidence on 64-bit SMP database trajectory"
relevance: medium
relevance_rationale: "TPC-C benchmark culture less central in cloud era; specific hardware obsolete; but SMP/NUMA scaling lessons relevant for modern in-memory databases like SAP HANA"
prescience: high
prescience_rationale: "Correctly identified SGI commercial potential (partially realized 1997-2001) and 64-bit VLM advantage (confirmed by modern HTAP systems); less accurate on long-term SGI viability"
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 9
obs_count: 25
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Informix and Silicon Graphics Reach New TPC-C SMP High-Water Mark

> Aberdeen Group analyzes the Informix-OnLine 7.3 / SGI Origin2000 TPC-C result of 25,309.20 tpmC at $139.04/tpmC — the highest non-clustered SMP result and second overall at the time. The profile documents benchmark configuration details including 28-way 195-MHz MIPS R10000 SMP, 13 GB RAM, 576 SCSI disks, and 21,500 SGI client workstations. Aberdeen argues the result signals SGI as a serious OLTP contender, validates Informix's return to benchmark leadership, and proves 64-bit VLM architectures deliver superior OLTP performance.

**Author:** Aberdeen Group · **Date:** 1997-07-01 · **Type:** Benchmark Analysis / Product Profile
**Importance:** high — *Documents a genuine benchmark milestone with specific technical data; captures both vendors at a pivotal moment; provides evidence on 64-bit SMP database trajectory*
**Prescience:** high — *Correctly identified SGI commercial potential (partially realized 1997-2001) and 64-bit VLM advantage (confirmed by modern HTAP systems); less accurate on long-term SGI viability*

## Entities (7)

- [[ENT-SGI-001|Informix Software Inc.]]
- [[ENT-SGI-002|Silicon Graphics Computer Systems (SGI)]]
- [[ENT-SGI-003|Compaq Computer]]
- [[ENT-SGI-004|Digital Equipment Corporation (DEC)]]
- [[ENT-SGI-005|BEA Systems]]
- [[ENT-SGI-006|Transaction Processing Council (TPC)]]
- [[ENT-SGI-007|Aberdeen Group]]

## Technologies (9)

- [[TECH-SGI-001|Informix-OnLine Dynamic Server 7.3]]
- [[TECH-SGI-002|Silicon Graphics Origin2000 Server]]
- [[TECH-SGI-003|TPC-C Benchmark]]
- [[TECH-SGI-004|64-bit Computing / Very Large Memory (VLM)]]
- [[TECH-SGI-005|Symmetric Multiprocessing (SMP)]]
- [[TECH-SGI-006|BEA Tuxedo 6.1 CFS]]
- [[TECH-SGI-007|IRIX (Silicon Graphics Unix)]]
- [[TECH-SGI-008|MIPS R10000 CPU]]
- [[TECH-SGI-009|Fast Ethernet]]

## Key observations (top 25)

- **1997** — TPC-C tpmC score: 25309.20
- **1997** — TPC-C price-performance: $139.04 per tpmC
- **1997** — TPC-C total system price: $3519012
- **1997** — Compaq ProLiant TPC-C score: 6842.70 tpmC at $100/tpmC
- **1997** — DEC AlphaServer TPC-C score: 13646.17 tpmC at $277/tpmC
- **1997** — SGI Origin2000 CPU count: 28 64-bit 195-MHz MIPS R10000 CPUs
- **1997** — SGI Origin2000 memory: 13 gigabytes main memory
- **1997** — SGI Origin2000 disk storage: 2.4237 terabytes (576 4.2-GB SCSI disk adapters)
- **1997** — SGI benchmark concurrent users: 21500 Silicon Graphics workstations
- **1997** — SGI commercial market entry: SGI is now a serious player in high-end commercial OLTP markets
- **2009** — SGI commercial market entry: SGI gained some commercial traction 1997-2001 but subsequently declined; filed Chapter 11 bankruptcy 2006 and 2009; assets sold to Rackable for $42.5M
- **1997** — Informix benchmark leadership restoration: New result establishes Informix leadership claim for 1997 high-end performance
- **1997** — Informix benchmark leadership restoration: Informix benchmark leadership proven by TPC-C result but accounting fraud scandal (1997) undermined company
- **1997** — 64-bit VLM architecture advantage: 64-bit hardware with VLM yields superior and usable OLTP results vs 32-bit architectures
- **2005** — 64-bit VLM architecture advantage: Confirmed: 64-bit became universal standard by 2003-2005; VLM critical for in-memory databases (SAP HANA, Exadata)
- **1997** — SMP scalability status: SMP technology has plenty of room for improvement; 28-way shows effective non-clustered scaling
- **1997** — End-user scalability in SMP: Systems handling >10000 simultaneous users can meet data-access needs of most enterprises
- **2010** — End-user scalability in SMP: Confirmed: modern OLTP systems routinely handle 100K+ concurrent users; prediction was conservative
- **1997** — BEA Tuxedo scalability validation: Tuxedo 6.1 CFS validated as performance enhancer for large SMP benchmark
- **1997** — Digital Equipment's 64-bit leadership: 64-bit field previously dominated by DEC with Sun as newer entrant
- **1997** — Wave of future benchmarks: More performance-increasing benchmarks expected from Informix and SGI
- **1998** — Wave of future benchmarks: Limited follow-through; Informix accounting scandal and SGI commercial difficulties curtailed benchmark activity
- **1997** — SGI commercial market strategy: SGI entering high-end commercial OLTP via partnership with RDBMS vendors
- **1997** — TPC-C benchmark ranking: Second overall among all TPC-C results; highest non-clustered SMP result
- **1997** — Informix-OnLine 7.x SMP product line: Continues to deliver outstanding benchmark results; 28-way SMP efficiency demonstrated

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-informix-and-silicon-graphics-reach-98e6ea' ORDER BY year_observed;
```

