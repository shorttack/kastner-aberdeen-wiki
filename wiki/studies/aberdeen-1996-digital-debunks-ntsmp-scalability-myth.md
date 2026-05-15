---
title: "Digital Debunks the NT/SMP Scalability Myth"
slug: aberdeen-1996-digital-debunks-ntsmp-scalability-myth
page_type: study
author: "Aberdeen Group"
date: "1996-11-22"
study_type: market-study
subject_domain: "server-computing-NT-SMP"
methodology: "industry-analysis, benchmarking, competitive-profiling"
importance: high
importance_rationale: "This Viewpoint reframed the NT scalability debate at a critical juncture in the server market transition from Unix to Windows NT; the TPC-C benchmark data presented was industry-recognized and the analysis influenced IT purchasing decisions by repositioning 4-way servers as viable midrange replacements."
relevance: medium
relevance_rationale: "The analytical framework — evaluating price/performance tradeoffs in server markets using independent benchmarks — remains methodologically sound and applicable to cloud instance comparisons today; the specific hardware and OS references are historically dated."
prescience: high
prescience_rationale: "Aberdeen's core predictions proved largely accurate: 4-way NT servers did dominate the midrange, NT Wolfpack clustering shipped in 1997-1998, and Digital was acquired by Compaq rather than winning as independent leader; the prediction of 20,000+ tpmC NT clusters by 1999 was directionally correct though Digital itself did not survive to lead it."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 8
obs_count: 26
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Digital Debunks the NT/SMP Scalability Myth

> This Aberdeen Group Market Viewpoint (Volume 9, Number 22, November 22, 1996) argues that IT decision-makers should reconsider the widespread belief that Windows NT Server lacks SMP scalability beyond four processors. Using Transaction Processing Council TPC-C benchmark data, Aberdeen demonstrates that Digital Equipment Corporation's 4-way Pentium Pro server achieves 6,712 tpmC at $65/tpmC, outperforming established midrange Unix and proprietary servers at a fraction of the cost. Aberdeen concludes that Microsoft's real strategy is performance clustering, not 8-way SMP scaling, and that Digital is optimally positioned to lead the NT midrange server market.

**Author:** Aberdeen Group · **Date:** 1996-11-22 · **Type:** market-study
**Importance:** high — *This Viewpoint reframed the NT scalability debate at a critical juncture in the server market transition from Unix to Windows NT; the TPC-C benchmark data presented was industry-recognized and the analysis influenced IT purchasing decisions by repositioning 4-way servers as viable midrange replaceme…*
**Prescience:** high — *Aberdeen's core predictions proved largely accurate: 4-way NT servers did dominate the midrange, NT Wolfpack clustering shipped in 1997-1998, and Digital was acquired by Compaq rather than winning as independent leader; the prediction of 20,000+ tpmC NT clusters by 1999 was directionally correct tho…*

## Entities (11)

- [[compaq|Compaq Computer Corporation]]
- [[digital-equipment-corporation|Digital Equipment Corporation]]
- [[hp-hewlett-packard|Hewlett-Packard Company]]
- [[ibm|IBM Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[ncr|NCR Corporation]]
- [[sequent|Sequent Computer Systems]]
- [[stratus-technologies|Stratus Technologies]]
- [[sun-microsystems|Sun Microsystems]]
- [[tandem-computers|Tandem Computers]]
- [[transaction-processing-council|Transaction Processing Council (TPC)]]

## Technologies (8)

- [[alpha-processor|Digital Alpha Processor]]
- [[digital-prioris-zx-6200mp|Digital Prioris ZX 6200MP (4-way)]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[nt-wolfpack-clustering|Windows NT Wolfpack Clustering]]
- [[numa-architecture|Non-Uniform Memory Access (NUMA)]]
- [[pentium-pro|Intel Pentium Pro]]
- [[tpc-c-benchmark|TPC-C Benchmark]]
- [[windows-nt-server|Microsoft Windows NT Server]]

## Key observations (top 25)

- **1996** — Digital Prioris ZX 6200MP TPC-C performance: 6,712 tpmC at $65/tpmC (NT, 4-way Pentium Pro, Microsoft SQL Server)
- **1996** — Compaq ProLiant 5000 NT/SQL Server TPC-C: 6,671 tpmC at $90/tpmC (NT, 4-way, Microsoft SQL Server)
- **1996** — Compaq ProLiant 5000 UnixWare/Sybase TPC-C: 8,311 tpmC at $95/tpmC (UnixWare, 4-way, Sybase SQL Server with Tuxedo)
- **1996** — IBM RS/6000 J40 TPC-C: 5,774 tpmC at $198/tpmC (AIX, 8-way, Sybase SQL Server)
- **1996** — HP 9000 K420 TPC-C: 4,939 tpmC at $232/tpmC (HP/UX, 4-way, Oracle 7)
- **1996** — IBM AS/400 9406 53S TPC-C: 1,496 tpmC at $320/tpmC (OS/400, 1-CPU, DB2/400)
- **1996** — Digital AlphaServer Unix cluster TPC-C: Exceeds 30,000 tpmC (Unix-based AlphaServer clusters)
- **1995** — Compaq NT TPC-C benchmark baseline (Nov 1995): 2,400 tpmC at $242/tpmC (Compaq ProLiant Intel-based)
- **1996** — Server market sweet spot transaction range: 2,000 to 15,000 tpmC (midrange); below 2,500 tpmC (workgroup); above 15,000 tpmC (high-end/enterprise)
- **1996** — NT server market volume distribution by CPU count: Over 90% of all server systems sold are 4-way-or-less
- **1996** — Microsoft NT performance strategy: Three-pronged: (1) maximize 4-way performance via CPU tuning; (2) continue limited SMP beyond 4-way; (3) pursue high-end via performance clustering (Wolfpack)
- **1996** — Digital NT competitive strategy: Build highly-tuned 4-way NT servers and performance clusters to capture large midrange market segments; Microsoft-aligned
- **1996** — Digital NT channel and services strategy: Broadest NT product line; largest MS training org in world; 2,000+ Microsoft-certified specialists; tight Microsoft alliance
- **1996** — Aberdeen explanation for NT SMP scalability gap: NT scalability limits beyond 4-way are not engineering-based but are a deliberate market economics decision by Microsoft
- **1996** — Digital NT clustering heritage advantage: Digital has clustering core expertise since VAX clusters (1980s); early NT cluster leader; high-availability clusters already at market debut
- **1996** — Aberdeen pricing attribution: Digital's $65/tpmC pricing driven by manufacturing economies of scale plus Internet-technology transaction handling that eliminates expensive Tuxedo front-end
- **1996** — 4-way NT server TPC-C projection by end of 1998: 4-way NT servers will at least double and perhaps triple in speed by year-end 1998, reaching 11,000-16,000 tpmC range
- **1998** — 4-way NT server TPC-C by 1998 - actual outcome: By 1998, 4-way Pentium II/Xeon NT servers exceeded 15,000 tpmC; prediction substantially correct; however DEC was acquired by Compaq January 1998 before full realization
- **1996** — NT performance cluster deployment prediction by 1999: More than 100,000 NT high-availability/performance clusters deployed by year-end 1999; NT performance clusters exceed 20,000 tpmC by early 1999
- **1999** — NT performance cluster deployment - actual outcome: Microsoft Cluster Service (MSCS) shipped in Windows NT 4.0 Enterprise Edition 1997; Windows 2000 Advanced Server extended to 4-node clusters; HA clustering widely adopted by 1999 though performance clustering adoption was slower than 100,000 unit pro…
- **1996** — Digital NT market leadership viability: Making a Digital NT server decision should prove irresistible to many IT decision makers; Aberdeen expects Digital to lead NT midrange charge
- **1998** — Digital NT market leadership - actual outcome: Digital acquired by Compaq January 1998 for $9.6B; Digital's NT product line and expertise absorbed into Compaq; Digital did not achieve independent NT market leadership
- **1996** — NT high-way SMP market assessment: 8-way and beyond NT systems: high-margin, low-volume; primarily for decision support, data warehousing, and consolidation servers
- **1996** — NT 32-bit architecture limitation assessment: NT 8-way+ systems will remain low-volume as long as NT is 32-bit; 64-bit NT needed for full high-end capability
- **1996** — NCR NT SMP achievements: NCR scaled NT on sixteen processors

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-digital-debunks-ntsmp-scalability-myth' ORDER BY year_observed;
```

