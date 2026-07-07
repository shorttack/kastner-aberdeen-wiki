---
title: "Debunking the NT/SMP Scalability Myth"
slug: "study-aberdeen-1996-debunking-ntsmp-scalability-myth"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-debunking-ntsmp-scalability-myth"
author: "Aberdeen Group"
date: "1996-11-26"
pub_year: 1996
type: "white-paper"
subject_domain: "server-computing"
methodology: "industry-analysis, benchmarking, competitive-profiling"
source_file: "1996 debunking NTSMP scalability myth.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 2.33
prescience_obs_count: 21
---

# Debunking the NT/SMP Scalability Myth

> Aberdeen Group's November 1996 Viewpoint argues that IS decision-makers should reconsider Windows NT's SMP scalability limitations, framing them as a deliberate Microsoft market strategy rather than an engineering constraint. Using TPC-C benchmark data, Aberdeen demonstrates that 4-way NT servers had already reached mid-range performance levels (6,712 tpmC at $65/tpmC), and projects NT will achieve 16,000 tpmC on 4-way platforms by 1998 while NT performance clusters will exceed 20,000 tpmC by early 1999. The study positions NT as an irresistible force in the mid-range server market based on price/performance momentum.


_Published 1996, author **Aberdeen Group**, type **white-paper**._


## Top observations

- 90% of all servers sold are 4-processor-or-less `[ps=5]`
- HA clusters first (1997 Wolfpack), then performance clusters (late 1997 to 1999) `[ps=5]`
- NT/SMP scalability should no longer prevent adoption of NT in enterprise; NT will dominate mid-range `[ps=5]`
- Microsoft released MSCS (Wolfpack) in Windows NT 4.0 Enterprise Edition in Q4 1997 as predicted `[ps=5]`
- ~90% utilization across 4 processors on NT 4.0 `[ps=4]`
- 3-phase: (1) Maximize 4-way performance, (2) Continue SMP non-aggressively, (3) High-end via performance clustering `[ps=4]`
- 4-way NT servers will reach 11,000-16,000 tpmC range by end of 1998 `[ps=4]`
- Windows 2000/2003 Server became market leader in mid-range by 2002; Unix declined by 3 percentage points per IDC `[ps=4]`
- Applications tuning to take advantage of NT SMP will be the next bottleneck after hardware is tuned `[ps=4]`
- Performance is secondary to reliability in mission-critical environments `[ps=4]`
- NT 8-way servers that scale well are imminent; probably by early 1997 `[ps=3]`
- <2,500 tpmC; file read/write/print activities `[ps=2]`
- More than 100,000 NT/HA servers will have been sold by end 1998 `[ps=2]`
- 6,712 tpmC at $65/tpmC (4-way NT Server 4.0 / SQL Server 6.5) `[ps=0]`
- >20,000 tpmC at $305/tpmC (AlphaServer 5/35) `[ps=0]`
- >20,000 tpmC at $396/tpmC `[ps=0]`
- Sequent: 28 processors; sold 14-processor NT systems; NCR: 16 processors `[ps=0]`
- 2,500-15,000 tpmC; HP 9000, DEC AlphaServer, IBM RS/6000, AS/400, Sun Ultra `[ps=0]`
- Compaq/Microsoft exceeded 16,000 tpmC on 4-way NT by 1998; prediction verified `[ps=0]`
- >15,000 tpmC; DEC 32-way AlphaServer, HP 48-way EPS30; up to 50,000 tpmC for heaviest OLTP `[ps=-1]`
- NT performance clusters (two 4-way servers) will exceed 20,000 tpmC by early 1999 `[ps=-1]`
- 2,454 tpmC at $242/tpmC (Compaq 4-way Intel)
- 50% (PC vendors learning) to 90% (enterprise-experienced SMP vendors)
- Many IS managers claim today's NT tpmC >6,750 rivals computing power of their existing mainframe systems
