---
title: "Sun Microsystems Decision Warehouse"
slug: aberdeen-1996-sun-microsystems-decision-warehouse
page_type: study
author: "Aberdeen Group"
date: "1996-03-01"
study_type: market-study
subject_domain: "data-warehousing-Unix-servers"
methodology: "industry-analysis, competitive-profiling, benchmarking, field-research"
importance: high
importance_rationale: "Documented Sun's pivotal strategic shift toward commercial data warehousing at the UltraSPARC launch moment; influential in directing enterprise data warehouse procurement toward Sun platforms in the late 1990s."
relevance: medium
relevance_rationale: "Solaris SMP tuning principles, the Database Engineering group model, and scalability frameworks for data warehousing retain methodological relevance; specific Sun hardware/software is obsolete but the competitive analysis framework for data warehouse platform evaluation applies to modern cloud and on-premises BI infrastructure."
prescience: high
prescience_rationale: "Aberdeen's prediction that data warehouses would grow 3-5x in 18 months and require suppliers who addressed scalability holistically proved accurate; Sun did become a dominant Unix data warehouse platform through 2005. Prediction that NT Server scalability 'pales' vs Solaris was correct for the era."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 6
obs_count: 21
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Sun Microsystems Decision Warehouse

> This Aberdeen Group profile evaluates Sun Microsystems Computer Corporation's (SMCC) Decision Warehouse program, examining its UltraSPARC server architecture, SPARCstorage arrays, Solaris 2.5 SMP optimization, Database Engineering group, and partnerships with Oracle, Sybase, Informix, and other RDBMS vendors. Aberdeen concludes that SMCC has the requisite components to differentiate itself in the data warehousing market, projecting strong scalability for terabyte-class warehouses through the Enterprise Server Test Center and Competency Centers.

**Author:** Aberdeen Group · **Date:** 1996-03-01 · **Type:** market-study
**Importance:** high — *Documented Sun's pivotal strategic shift toward commercial data warehousing at the UltraSPARC launch moment; influential in directing enterprise data warehouse procurement toward Sun platforms in the late 1990s.*
**Prescience:** high — *Aberdeen's prediction that data warehouses would grow 3-5x in 18 months and require suppliers who addressed scalability holistically proved accurate; Sun did become a dominant Unix data warehouse platform through 2005. Prediction that NT Server scalability 'pales' vs Solaris was correct for the era.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[informix|Informix Software]]
- [[kpmg|KPMG]]
- [[oracle|Oracle Corporation]]
- [[price-waterhouse|Price Waterhouse]]
- [[red-brick-systems|Red Brick Systems]]
- [[sas-institute|SAS Institute]]
- [[sun-microsystems|Sun Microsystems Computer Corporation (SMCC)]]
- [[sybase|Sybase, Inc.]]

## Technologies (6)

- [[gigaplane-bus|Sun Gigaplane System Bus]]
- [[oracle7|Oracle 7]]
- [[solaris-25|Solaris 2.5]]
- [[sparcstorage-array|SPARCstorage Array 214 RSM]]
- [[ultrasparc|Sun UltraSPARC RISC Processor]]
- [[windows-nt-server|Windows NT Server]]

## Key observations (top 25)

- **1996** — SMCC Decision Warehouse Strategy: Comprehensive data warehouse infrastructure: UltraSPARC servers + Gigaplane bus + Solaris 2.5 + SPARCstorage + Database Engineering group + RDBMS partnerships + competency centers
- **1996** — Sun FY1996 Revenue Estimate: ~$7 billion FY1996 (ending June 30); commercial sales >$1.5B (at least one-third of revenue)
- **1996** — SPARCstorage Revenue Estimate: Storage Products Group revenues estimated >$1 billion; independent P&L unit within SMCC
- **1996** — SunService Growth Rate: 40-45% annual staff growth rate for past 3 years; expects to continue; Sun ranked top 3 in customer satisfaction North America, Europe, Asia
- **1996** — Enterprise Server Test Center Investment: SMCC invested >$10 million in Enterprise Server Test Center; tested data warehouses from 20GB pilots to 5.5TB Oracle demonstration
- **1996** — Solaris 2.5 SMP Scalability Efficiency: 92-97% SMP scalability (depending on RDBMS) as CPUs added; only 3-8% overhead per added CPU vs 15-20% for typical Unix SMP and up to 30% for NT Server
- **1996** — Gigaplane Bus Architecture: 2.6 GBps system bus; thin boards with dual CPUs + memory (up to 2GB/board) + high-speed I/O channels; parallel CPU/I/O/network interconnections approaching mainframe speeds
- **1996** — Data Warehouse Size Growth Rate: Enterprise-level production data warehouses grow 3-5x in 18 months; majority >100GB now moving from pilot to full implementation; handful already over terabyte
- **1996** — Data Warehouse Growth Trajectory Prediction: Aberdeen predicts warehouse sizes approaching terabyte with hundreds of attached users; production warehouses outpacing supplier capabilities except those (like SMCC) who solved scalability issues
- **2005** — Data Warehouse Growth Trajectory Actual Outcome: Prediction proved accurate: enterprise data warehouses grew to multi-terabyte scale by 2000-2005; petabyte-scale warehouses emerged by 2010 (Teradata, Netezza, then Hadoop). Scalability became the defining vendor differentiator as Aberdeen predicted.
- **1996** — SMCC Data Warehouse Market Leadership Prediction: Aberdeen believes SMCC has requisite pieces to differentiate in data warehousing; expects Decision Warehouse customers to be 'spared the pain' of inadequate scalability
- **2005** — SMCC Data Warehouse Market Position Actual Outcome: Sun became a leading Unix data warehouse platform through the late 1990s-early 2000s; UltraSPARC/Solaris widely used for Oracle data warehouses. Sun's position weakened after 2003 as x86/Linux and commodity hardware eroded Unix server market; acquire…
- **1996** — NT Server vs Solaris for Data Warehousing: NT Server scalability 'pales' vs Solaris; NT SMP overhead up to 30% vs Solaris 3-8%; Sun competes well against NT even for small warehouse/proof-of-concept
- **1996** — SPARCstorage Array 214 RSM Specifications: Hot-swap disk modules, fans, power supplies; 4.2GB drives (3.5 inch backplane); industry-standard fiber channels; RAS Customer Action Team for storage issues; superior MTBF vs competitors
- **1996** — SMCC-Oracle Distributed Parallel Query Support: SMCC clusters support Oracle 7.3 distributed parallel query; pair of servers clustered using high-speed fiber channels; RDBMS contacts admitted product could not have been marketed without SMCC engineering involvement
- **1996** — Data Warehouse Scalability Factor: Processor Speed: UltraSPARC 64-bit delivers 2x power of prior SPARC; new high-speed servers shipping May 1996
- **1996** — Data Warehouse Scalability Factor: Bus Bandwidth: 2.6 GBps Gigaplane bus eliminates memory/disk bottleneck; multiple parallel CPU/I/O/network interconnections; exceeds anything available in comparable Unix systems
- **1996** — Data Warehouse Scalability Factor: SMP Operating System: Solaris 2.5 fine-tuned for multiprocessor; threaded I/O and networking; constant query response time as dataset and user count grow; 3-8% CPU overhead (vs up to 30% for NT)
- **1996** — Data Warehouse Scalability Factor: Storage Subsystem: SPARCstorage arrays with fiber channels; hot-swap HA features; superior MTBF; mission-critical grade I/O; sequential access optimized for data warehouse workloads
- **1996** — Data Warehouse Scalability Factor: RDBMS Partnership Depth: Bilateral engineering agreements with Oracle/Sybase/Informix; joint competency centers; bilateral optimization giving both SMCC and RDBMS supplier code improvements; classified as 'secret weapon'
- **1996** — Database Engineering Group Assessment: Aberdeen: SMCC's Database Engineering group is its 'secret weapon' — dedicated to making major database products run as fast as possible; >$10M test center investment; Solaris 2.5 SMP improvements enabled by group testing

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-sun-microsystems-decision-warehouse' ORDER BY year_observed;
```

