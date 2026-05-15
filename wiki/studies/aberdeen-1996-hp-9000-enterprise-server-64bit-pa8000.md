---
title: "HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived"
slug: aberdeen-1996-hp-9000-enterprise-server-64bit-pa8000
page_type: study
author: "Aberdeen Group"
date: "1996-09-17"
study_type: market-study
subject_domain: "unix-enterprise-servers"
methodology: "benchmarking, competitive-profiling, industry-analysis"
importance: high
importance_rationale: "Documented the first PA-8000 TPC-C benchmark results for HP 9000 servers at a pivotal moment in Unix server competition; the 2.5x generation-over-generation performance leap and pricing data were significant inputs for IS decision-makers in 1996."
relevance: low
relevance_rationale: "The specific benchmarks and processors are entirely obsolete; the HP 9000/PA-RISC platform was discontinued in 2003. The study retains archival value for understanding 1990s Unix server competitive dynamics."
prescience: medium
prescience_rationale: "HP's short-term performance roadmap (PA-8200, PA-8500) proved accurate, but the long-term Merced/Itanium transition was delayed until 2001 and ultimately failed commercially; HP 9000 was discontinued in 2003."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 10
obs_count: 27
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived

> Aberdeen Group evaluates HP's September 1996 announcement of PA-8000-based HP 9000 enterprise servers, documenting benchmark performance results (K460 at 12,321 tpmC — a 2.5x improvement over its PA-7200 predecessor) and positioning HP's PRISM framework as the standard for Unix enterprise server selection. The study asserts HP's competitive superiority over IBM, Sun, and Digital in the Unix server market, and outlines HP's roadmap through PA-8200, PA-8500, and eventual Merced processor transitions.

**Author:** Aberdeen Group · **Date:** 1996-09-17 · **Type:** market-study
**Importance:** high — *Documented the first PA-8000 TPC-C benchmark results for HP 9000 servers at a pivotal moment in Unix server competition; the 2.5x generation-over-generation performance leap and pricing data were significant inputs for IS decision-makers in 1996.*
**Prescience:** medium — *HP's short-term performance roadmap (PA-8200, PA-8500) proved accurate, but the long-term Merced/Itanium transition was delayed until 2001 and ultimately failed commercially; HP 9000 was discontinued in 2003.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[data-general|Data General Corporation]]
- [[digital-equipment-corporation|Digital Equipment Corporation]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[ibm|IBM Corporation]]
- [[intel|Intel Corporation]]
- [[silicon-graphics|Silicon Graphics, Inc. (SGI)]]
- [[sun-microsystems|Sun Microsystems, Inc.]]
- [[transaction-processing-council|Transaction Processing Performance Council (TPC)]]

## Technologies (10)

- [[hp-9000|HP 9000 (HP-UX)]]
- [[hp-intel-merced|HP-Intel P7/Merced (Itanium)]]
- [[hp-ux|HP-UX 10.2 / 11.0]]
- [[pa-7200|PA-7200 Processor (120MHz)]]
- [[pa-8000|PA-8000 Processor (64-bit, 180MHz)]]
- [[pa-8200|PA-8200 Processor]]
- [[pa-8500|PA-8500 Processor]]
- [[rs6000-sp|IBM RS/6000 SP (Scalable PowerParallel)]]
- [[sun-ultra-enterprise|Sun Ultra Enterprise 5000]]
- [[tpc-c|TPC-C Benchmark]]

## Key observations (top 25)

- **1996** — HP K460 TPC-C performance: 12,321 tpmC at $186/tpmC (4-way, 180MHz PA-8000)
- **1996** — HP K420 TPC-C performance (predecessor): 4,939 tpmC (4-way, 120MHz PA-7200)
- **1996** — HP D370 TPC-C performance: 5,300 tpmC at ~30% better price/performance vs IBM RS/6000 R40
- **1996** — IBM RS/6000 PowerPC R40 TPC-C performance: 5,775 tpmC at $248/tpmC (8-CPU PowerPC 604, 112MHz)
- **1996** — Sun Ultra Enterprise 5000 TPC-C performance: 11,466 tpmC (12-CPU, Sun's highest published result)
- **1996** — DEC Alpha DECchip 400MHz TPC-C performance: 1,600-1,700 tpm
- **1996** — IBM PowerPC 604 112MHz TPC-C performance: 800-900 tpm
- **1996** — SGI R4400-250MHz TPC-C performance: 500-600 tpm
- **1996** — Data General Intel PentiumPro 200MHz TPC-C performance: 1,900-2,000 tpm
- **1996** — PA-8000 180MHz SPECint95 / SPECfp95: 11.8 SPECint95 / 20.2 SPECfp95 / 3,200-3,300 tpm
- **1996** — PA-8000 generation-over-generation performance improvement: 200-250% improvement from K420 to K460 within one year; industry average 35% per year
- **1996** — HP-UX version roadmap: 10.2 (PA-8000 support) → 11.0 (VLM, mid-1997) → 11.X (Merced)
- **1996** — HP PRISM framework components: Performance, Resilience, Integration, Security, Management
- **1996** — PRISM dimension: Performance: PA-8000 processor; new disk array and tape library storage; leading TPC-C results
- **1996** — PRISM dimension: Resilience: MC/ServiceGuard clustering; high-availability features in each HP-UX release
- **1996** — PRISM dimension: Security: Praesidium technology: transaction application gateways, smartcards, antivirus, non-repudiation
- **1996** — HP enterprise server competitive positioning: Performance leadership through continuous processor roadmap; investment protection via in-box upgradeability
- **1996** — HP EPS31 positioning vs IBM RS/6000 SP: Positioned as MVS Parallel Sysplex alternative for mainframe Y2K migrations
- **1997** — PA-8200 performance and delivery timeline: 50% performance increase over PA-8000; systems in 3Q97
- **1998** — PA-8500 performance and delivery timeline: 100% improvement over PA-8000 (2x); end of first-half 1998
- **1998** — HP-Intel Merced processor delivery in servers: Anticipated mid-1998 delivery in servers
- **1997** — PA-8200 delivery actual outcome: PA-8200 (240MHz) shipped 1997 as projected; PA-8500 delayed to mid-1999
- **2001** — Merced/Itanium actual delivery: Itanium (Merced) shipped in servers in 2001; 3 years later than predicted
- **2003** — HP 9000 server line fate: HP 9000 server line discontinued in 2003; replaced by Itanium-based Integrity Servers
- **1996** — HP T600 projected performance: >15,000 tpmC; shipping 1Q97

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-hp-9000-enterprise-server-64bit-pa8000' ORDER BY year_observed;
```

