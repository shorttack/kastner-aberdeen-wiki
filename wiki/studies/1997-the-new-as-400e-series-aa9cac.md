---
title: "The New AS/400e series: Breaking Current Enterprise Scalability Barriers And Historic Perceptions"
slug: 1997-the-new-as-400e-series-aa9cac
page_type: study
author: "Aberdeen Group"
date: "1997-08-19"
study_type: announcement-profile
subject_domain: "IBM-midrange-computing-enterprise-server"
methodology: "benchmarking, competitive-profiling, industry-analysis, document-review"
importance: high
importance_rationale: "Published on IBM announcement day, this is a primary analytical record of the AS/400e transition — the moment IBM broke the 4-CPU scalability ceiling that had constrained the platform for years. Aberdeen's 3,843-word analysis provides detailed benchmark data and competitive context unavailable in IBM marketing materials."
relevance: high
relevance_rationale: "The study documents architectural decisions (64-bit PowerPC, SMP scalability, TIMI portability) that underpin the IBM i/Power Systems platform still in active production today; benchmark methodology and competitive framing directly inform modern midrange server evaluations."
prescience: high
prescience_rationale: "Aberdeen's prediction that IBM would re-ignite AS/400 revenue growth proved directionally correct — the platform survived and thrived through multiple rebrands (iSeries 2000, System i 2006, Power Systems 2008, IBM i active through IBM i 7.5 in 2022), and the 70% performance improvement claim for end-of-1998 was also consistent with IBM's subsequent roadmap execution."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 11
obs_count: 26
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# The New AS/400e series: Breaking Current Enterprise Scalability Barriers And Historic Perceptions

> Aberdeen Group provides a day-of-announcement analysis of IBM's new AS/400e series (August 19, 1997), evaluating its breakthrough 12-way PowerPC SMP architecture, new OS/400 V4.1, and benchmark results showing over 25,000 TPC-C tpm — exceeding Sun UltraEnterprise 6000 (16-CPU) performance. Aberdeen concludes the AS/400e series has fixed the platform's most glaring limitation (scalability) and positions IBM to re-ignite AS/400 revenue growth at 20%+ annually, with particularly compelling cases for electronic business, Year 2000 replacement, and SAP R/3 deployments.

**Author:** Aberdeen Group · **Date:** 1997-08-19 · **Type:** announcement-profile
**Importance:** high — *Published on IBM announcement day, this is a primary analytical record of the AS/400e transition — the moment IBM broke the 4-CPU scalability ceiling that had constrained the platform for years. Aberdeen's 3,843-word analysis provides detailed benchmark data and competitive context unavailable in IB…*
**Prescience:** high — *Aberdeen's prediction that IBM would re-ignite AS/400 revenue growth proved directionally correct — the platform survived and thrived through multiple rebrands (iSeries 2000, System i 2006, Power Systems 2008, IBM i active through IBM i 7.5 in 2022), and the 70% performance improvement claim for end…*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[digital-equipment-corporation|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM Corporation]]
- [[jd-edwards|J.D. Edwards & Company]]
- [[lotus-development|Lotus Development Corporation]]
- [[netscape|Netscape Communications]]
- [[sap-ag|SAP AG]]
- [[silicon-graphics|Silicon Graphics (SGI)]]
- [[ssa-gt|SSA GT (Systems Software Associates)]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (11)

- [[as400e-series|IBM AS/400e Series]]
- [[db2-400|DB2/400]]
- [[ibm-network-station|IBM Network Station]]
- [[java|Java]]
- [[lotus-domino|Lotus Domino]]
- [[os400-v4r1|OS/400 Version 4.1]]
- [[powerpc-as-apache|PowerPC AS (Apache) CPU]]
- [[sap-r3|SAP R/3]]
- [[tpc-c|TPC-C Benchmark]]
- [[unix-servers|Unix Servers (RISC)]]
- [[windows-nt-server|Windows NT Server]]

## Key observations (top 25)

- **1997** — TPC-C throughput (12-way 650): 25,000+ transactions per minute
- **1997** — TPC-C throughput (Sun UltraEnterprise 6000, 16-CPU): Slightly over 23,000 tpm
- **1997** — SAP R/3 SD benchmark (3-tier, 12-way 650): 2,400 concurrent users
- **1997** — Performance improvement vs prior AS/400: 4.6x (overall); 2x per-processor uniprocessor throughput
- **1997** — High-end performance improvement projection for end-1998: 70% further improvement over current 12-way
- **1997** — OS/400 V4R1 recovery time improvement: 40% faster system rebuild; 60% faster IPL
- **1997** — Maximum memory (high-end 650): 20 GB main memory
- **1997** — AS/400 installed base at time of announcement: 450,000 systems shipped to date
- **1997** — System/36 installed base still operating: 85,000-100,000 System/36s still in production
- **1997** — Proprietary midrange replacement opportunity: ~250,000 proprietary midrange computers needing Y2K replacement
- **1997** — IBM marketing repositioning: Targeting: e-business, Y2K replacement, fast-growing enterprises, data warehousing, central OLTP
- **1997** — AS/400e vs Unix design philosophy: AS/400e = integrated OS+DB+hardware; Unix/NT = component building blocks
- **1997** — Netscape endorsement: Publicly declared intent to port all server-based applications to AS/400e
- **1997** — Java and Domino availability: Lotus Domino and Java scheduled for general availability Q1 1998 in native mode
- **1997** — AS/400e revenue growth potential: IBM has every possibility of re-igniting AS/400 revenue growth to over 20% per year for at least several years
- **1997** — Platform competitive positioning: Positioned in top 3-5 absolute commercial performance leaders for real-world production
- **2000** — AS/400 rebranded as eServer iSeries: IBM rebranded AS/400 to eServer iSeries in 2000; continued to gain e-business workloads
- **2008** — OS/400 renamed IBM i: OS/400 renamed i5/OS (2004) then IBM i (2008); still in active development IBM i 7.5 (2022)
- **2008** — Platform consolidated into IBM Power Systems: System i and System p merged into IBM Power Systems in April 2008; IBM i continues as OS option
- **2010** — Sun Microsystems acquired by Oracle: Sun acquired by Oracle for $7.4B in 2010; Solaris/SPARC platform declining
- **1997** — e-business advantage: scalability: Never having to say 'sorry, out of capacity' — 12-way SMP eliminates NT prototype failure mode
- **1997** — e-business advantage: rapid deployment: Never having to say 'ready in 6-12 months' — integrated stack enables fast Unix-competing deployment
- **1997** — e-business advantage: security: Ethical Hackers Association unable to penetrate AS/400e web security
- **1997** — e-business advantage: Domino/DB2 integration: Native Domino allows dynamic DB2/400 data pull into web-based e-business applications
- **1997** — e-business advantage: native Java: IBM porting each new Java release to AS/400e as soon as possible; object-based OS/400 highly complementary

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-the-new-as-400e-series-aa9cac' ORDER BY year_observed;
```

