---
title: "Sun Unveils UltraSPARC IV Processor"
slug: technology-news-hardware-sun-unveils-ult-4a76bb
page_type: study
author: "Jay Lyman, TechNewsWorld"
date: "2003-10-13"
study_type: news-article
subject_domain: "server-processors"
methodology: "product-analysis, analyst-commentary"
importance: medium
importance_rationale: "Documents Sun's pivot to multithreading/throughput computing at a moment when industry consensus was turning against Sun's continued processor investment — a critical inflection in SPARC's long decline."
relevance: medium
relevance_rationale: "CPU-strategy analysis remains a template for vendor evaluations (AMD Zen, Apple Silicon, ARM servers); specific UltraSPARC IV details dated."
prescience: high
prescience_rationale: "Kastner defended Sun's processor investment; Reynolds called for exit. Reynolds was directionally correct — Sun was acquired by Oracle in 2010, UltraSPARC shipments declined through the 2010s, and Oracle discontinued SPARC processor development by 2017. Kastner's installed-base-continuity argument was also validated in that existing Sun customers did stay on SPARC through the 2010s."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 8
obs_count: 13
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Sun Unveils UltraSPARC IV Processor

> TechNewsWorld article (Oct 13 2003, Jay Lyman) reporting Sun Microsystems' UltraSPARC IV unveiling at the 16th annual Microprocessor Forum in San Jose. The dual-threaded chip (two UltraSPARC III cores, on-chip memory controller supporting 16 GB DRAM, 8 MB L2 tags per core) was positioned as Sun's 'Throughput Computing' answer to Intel Itanium and IBM Power. Aberdeen Group research director Peter Kastner is a central skeptical-but-defensive voice: 'To Sun's installed base, UltraSPARC IV has to be competitive. It doesn't have to be world-beating,' and it would be 'foolish for Sun to exit processors' given 20 years of investment. Gartner VP Martin Reynolds argues the opposite — that Sun should exit chips. Harlan McGhan (Sun) previews 90nm with Texas Instruments and an 8-core/32-thread future chip.

**Author:** Jay Lyman, TechNewsWorld · **Date:** 2003-10-13 · **Type:** news-article
**Importance:** medium — *Documents Sun's pivot to multithreading/throughput computing at a moment when industry consensus was turning against Sun's continued processor investment — a critical inflection in SPARC's long decline.*
**Prescience:** high — *Kastner defended Sun's processor investment; Reynolds called for exit. Reynolds was directionally correct — Sun was acquired by Oracle in 2010, UltraSPARC shipments declined through the 2010s, and Oracle discontinued SPARC processor development by 2017. Kastner's installed-base-continuity argument w…*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[gartner-inc|Gartner, Inc.]]
- [[harlan-mcghan-sun|Harlan McGhan]]
- [[ibm-corp|IBM Corporation]]
- [[intel-corp|Intel Corporation]]
- [[jay-lyman-journalist|Jay Lyman]]
- [[martin-reynolds-gartner|Martin Reynolds]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]
- [[technewsworld|TechNewsWorld]]
- [[texas-instruments|Texas Instruments]]

## Technologies (8)

- [[ibm-power|IBM POWER]]
- [[intel-itanium|Intel Itanium (IA-64)]]
- [[intel-xeon|Intel Xeon]]
- [[solaris-os|Sun Solaris]]
- [[throughput-computing|Sun Throughput Computing strategy]]
- [[ultrasparc-iii|Sun UltraSPARC III]]
- [[ultrasparc-iiii|Sun UltraSPARC IIIi]]
- [[ultrasparc-iv|Sun UltraSPARC IV]]

## Key observations (top 25)

- **2003** — Sun UltraSPARC IV does not need to beat rivals, only compete: To Sun's installed base, UltraSPARC IV has to be competitive. It doesn't have to be world-beating.
- **2003** — Installed-base investment justifies continued processor R&D: Sun's customers want UltraSPARC IV to be successful so they can continue to feel comfortable investing in Sun and in Sun's real strength, which is Solaris.
- **2003** — Foolish for Sun to abandon 20 years of chip R&D: The big picture is Sun has more to gain at this time by delivering a world-beating UltraSPARC IV than by abandoning 20 years of work in chip research.
- **2003** — Sun should reconsider the processor business: Certainly, the message is Sun should reconsider what it's doing with processors. Sun's value doesn't lie in the processor anymore. It lies in the robust systems and infrastructure they're capable of providing.
- **2003** — UltraSPARC IV performance vs UltraSPARC III: 2x performance via multithreading (two UltraSPARC III cores on single die)
- **2006** — Next-gen chip multithreading will deliver 15x UltraSPARC IIIi throughput: more radical chip multithreading design by 2006, which may increase throughput of today's UltraSPARC IIIi by as many as 15 times
- **2005** — UltraSPARC T1 Niagara shipped 2005 with 8 cores/32 threads: Sun UltraSPARC T1 (Niagara) shipped Nov 2005 with 8 cores, 4 threads/core = 32 threads; design target partially met a year earlier than predicted
- **2004** — UltraSPARC IV shipping target: begin shipping in systems during the first half of 2004
- **2003** — Sun multithreading technology is untested in practice: praised the additional cache Sun built into the new UltraSPARC IV, Reynolds said Sun's multithreading technology is still untested in practice
- **2003** — Intel Xeon squeezing Sun large-server market: Intel's Xeon processor is taking a toll on all competitors; the large server market where Sun has historically played well is suffering from the increasing share of lower-cost servers
- **2006** — Sun plans 8-core single-die chip executing 32 threads: a processor with eight cores on a single-chip die. That's a single chip that can actually execute 32 threads in parallel
- **2017** — Oracle discontinued SPARC processor development: Oracle confirmed SPARC M8 (2017) as its final SPARC CPU and canceled its M8 successor; effectively ended SPARC roadmap
- **2010** — Sun acquired by Oracle: Oracle completed acquisition of Sun Microsystems for $7.4B on 2010-01-27

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'technology-news-hardware-sun-unveils-ult-4a76bb' ORDER BY year_observed;
```

