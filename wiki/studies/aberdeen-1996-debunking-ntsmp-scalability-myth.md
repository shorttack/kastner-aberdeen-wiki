---
title: "Debunking the NT/SMP Scalability Myth"
slug: aberdeen-1996-debunking-ntsmp-scalability-myth
page_type: study
author: "Aberdeen Group"
date: "1996-11-26"
study_type: white-paper
subject_domain: "server-computing"
methodology: "industry-analysis, benchmarking, competitive-profiling"
importance: high
importance_rationale: "Published at a pivotal inflection point in the mid-range server market, this Viewpoint directly challenged conventional wisdom that NT could not compete with Unix and proprietary SMP systems. Aberdeen's TPC-C analysis was highly influential in legitimizing NT for enterprise IS planning in 1997-1998."
relevance: medium
relevance_rationale: "The analytical framework—using transaction benchmarks to segment server markets and project performance trajectories—remains methodologically sound and applicable to current cloud/on-premises performance debates. The specific hardware predictions are dated but the market dynamics analysis transfers well."
prescience: high
prescience_rationale: "Aberdeen's core predictions proved largely accurate: NT/Windows Server did dominate the mid-range market by 2000-2002 (IDC data confirms), 4-way NT performance exceeded 16,000 tpmC by 1998 (Microsoft/Compaq TPC-C results), and NT availability clusters (Wolfpack/MSCS) shipped in 1997. Performance cluster prediction at 20,000+ tpmC was also validated."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 7
obs_count: 24
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Debunking the NT/SMP Scalability Myth

> Aberdeen Group's November 1996 Viewpoint argues that IS decision-makers should reconsider Windows NT's SMP scalability limitations, framing them as a deliberate Microsoft market strategy rather than an engineering constraint. Using TPC-C benchmark data, Aberdeen demonstrates that 4-way NT servers had already reached mid-range performance levels (6,712 tpmC at $65/tpmC), and projects NT will achieve 16,000 tpmC on 4-way platforms by 1998 while NT performance clusters will exceed 20,000 tpmC by early 1999. The study positions NT as an irresistible force in the mid-range server market based on price/performance momentum.

**Author:** Aberdeen Group · **Date:** 1996-11-26 · **Type:** white-paper
**Importance:** high — *Published at a pivotal inflection point in the mid-range server market, this Viewpoint directly challenged conventional wisdom that NT could not compete with Unix and proprietary SMP systems. Aberdeen's TPC-C analysis was highly influential in legitimizing NT for enterprise IS planning in 1997-1998.*
**Prescience:** high — *Aberdeen's core predictions proved largely accurate: NT/Windows Server did dominate the mid-range market by 2000-2002 (IDC data confirms), 4-way NT performance exceeded 16,000 tpmC by 1998 (Microsoft/Compaq TPC-C results), and NT availability clusters (Wolfpack/MSCS) shipped in 1997. Performance clu…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq-computer|Compaq Computer Corporation]]
- [[digital-equipment|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[intel-corporation|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[ncr-corporation|NCR Corporation]]
- [[sequent-computer|Sequent Computer Systems]]
- [[tandem-computers|Tandem Computers]]
- [[tpc-council|Transaction Processing Performance Council (TPC)]]

## Technologies (7)

- [[alpha-processor|DEC Alpha Processor]]
- [[intel-pentium-pro|Intel Pentium Pro / Klamath / Deschutes]]
- [[microsoft-sql-server|Microsoft SQL Server 6.5]]
- [[nt-wolfpack-clusters|Microsoft Wolfpack NT Clustering]]
- [[numa-architecture|Non-Uniform Memory Access (NUMA)]]
- [[tpcc-benchmark|TPC-C Benchmark]]
- [[windows-nt-4|Windows NT Server 4.0]]

## Key observations (top 25)

- **1996** — Server market 4-way-or-less share: 90% of all servers sold are 4-processor-or-less
- **1995** — NT baseline TPC-C (November 1995): 2,454 tpmC at $242/tpmC (Compaq 4-way Intel)
- **1996** — NT 4-way TPC-C (November 1996): 6,712 tpmC at $65/tpmC (4-way NT Server 4.0 / SQL Server 6.5)
- **1996** — DEC 32-processor AlphaServer TPC-C: >20,000 tpmC at $305/tpmC (AlphaServer 5/35)
- **1996** — HP 48-processor HP 9000 EPS30 TPC-C: >20,000 tpmC at $396/tpmC
- **1996** — NT 4.0 4-way scaling efficiency (NCR testing): ~90% utilization across 4 processors on NT 4.0
- **1996** — 4-way NT scaling efficiency range across vendors: 50% (PC vendors learning) to 90% (enterprise-experienced SMP vendors)
- **1996** — Maximum NT SMP processor count demonstrated: Sequent: 28 processors; sold 14-processor NT systems; NCR: 16 processors
- **1996** — Microsoft NT SMP market strategy: 3-phase: (1) Maximize 4-way performance, (2) Continue SMP non-aggressively, (3) High-end via performance clustering
- **1996** — NT clustering strategy sequence: HA clusters first (1997 Wolfpack), then performance clusters (late 1997 to 1999)
- **1996** — Server tier: Workgroup (low-end): <2,500 tpmC; file read/write/print activities
- **1996** — Server tier: Departmental/Mid-range: 2,500-15,000 tpmC; HP 9000, DEC AlphaServer, IBM RS/6000, AS/400, Sun Ultra
- **1996** — Server tier: Enterprise (high-end): >15,000 tpmC; DEC 32-way AlphaServer, HP 48-way EPS30; up to 50,000 tpmC for heaviest OLTP
- **1996** — NT 4-way TPC-C projection by end 1998: 4-way NT servers will reach 11,000-16,000 tpmC range by end of 1998
- **1996** — NT HA cluster shipments by end 1998: More than 100,000 NT/HA servers will have been sold by end 1998
- **1996** — NT performance cluster tpmC by early 1999: NT performance clusters (two 4-way servers) will exceed 20,000 tpmC by early 1999
- **1996** — NT mid-range market dominance prediction: NT/SMP scalability should no longer prevent adoption of NT in enterprise; NT will dominate mid-range
- **1996** — NT 8-way server market arrival: NT 8-way servers that scale well are imminent; probably by early 1997
- **1998** — NT 4-way TPC-C actual performance by 1998: Compaq/Microsoft exceeded 16,000 tpmC on 4-way NT by 1998; prediction verified
- **1997** — NT Wolfpack clustering release: Microsoft released MSCS (Wolfpack) in Windows NT 4.0 Enterprise Edition in Q4 1997 as predicted
- **2002** — NT/Windows Server mid-range market outcome: Windows 2000/2003 Server became market leader in mid-range by 2002; Unix declined by 3 percentage points per IDC
- **1996** — Real NT scalability constraint: Applications tuning to take advantage of NT SMP will be the next bottleneck after hardware is tuned
- **1996** — IS managers' priority: reliability > performance: Performance is secondary to reliability in mission-critical environments
- **1996** — IS manager mainframe comparison: Many IS managers claim today's NT tpmC >6,750 rivals computing power of their existing mainframe systems

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-debunking-ntsmp-scalability-myth' ORDER BY year_observed;
```

