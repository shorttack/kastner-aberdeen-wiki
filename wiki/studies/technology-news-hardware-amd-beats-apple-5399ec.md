---
title: "AMD Beats Apple's G5 and Intel's P4"
slug: technology-news-hardware-amd-beats-apple-5399ec
page_type: study
author: "Jay Lyman, TechNewsWorld"
date: "2003-10-15"
study_type: news-article
subject_domain: "64-bit-desktop-processors"
methodology: "product-analysis, benchmark-commentary, analyst-commentary"
importance: medium
importance_rationale: "Documents the Oct 2003 inflection when 64-bit desktop computing became contested between Apple/IBM PowerPC, AMD AMD64, and Intel x86-32 — with Kastner articulating the canonical \"no 64-bit software yet\" critique that held for the next 2-3 years."
relevance: medium
relevance_rationale: "Benchmark-timing and new-ISA-needs-new-software-to-matter dynamics recur in every subsequent architectural transition: Intel Core 2 vs AMD K8 (2006), ARM vs x86 in servers (2020s), Apple Silicon M1 vs Intel (2020), and now AI accelerators (2023-2025)."
prescience: high
prescience_rationale: "Kastner's \"wait a year for real 64-bit apps\" prediction was directionally correct — Windows XP x64 Edition shipped Apr 2005 (~18 months later), and mainstream 64-bit adoption still took through Windows 7 (2009) to reach consumers. His framing of AMD64 as winning despite unclear market outcomes was correct: AMD64 became the dominant desktop/server ISA; Apple abandoned PowerPC for Intel in 2006."
license: CC-BY-4.0
tier: 1
entity_count: 14
tech_count: 7
obs_count: 9
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# AMD Beats Apple's G5 and Intel's P4

> TechNewsWorld article (Oct 15 2003, Jay Lyman) on PC World benchmarks showing AMD's Athlon 64 and dual Opteron processors beating Apple's Power Mac G5 and Intel's Pentium 4 on Word, Premiere 6, Quake III, and Photoshop 7.0.1. Aberdeen chief research officer Peter Kastner provides the central skeptical voice: 'Tune in a year from now, and then we'll have a better idea of how these chips run on real-world, 64-bit applications' — noting the PC World tests did not use 64-bit software, so 'users really aren't getting any benefit out of 64-bit instructions on Athlon or Apple.' Kastner calls Athlon 'a very competitive chip priced at a heady level for AMD' and predicts Apple developers will quickly optimize for 64-bit while Athlon64's market remains unclear pending 64-bit Windows XP. IDC's Shane Rau and Gartner's Martin Reynolds add benchmark-timing and memory-bandwidth context.

**Author:** Jay Lyman, TechNewsWorld · **Date:** 2003-10-15 · **Type:** news-article
**Importance:** medium — *Documents the Oct 2003 inflection when 64-bit desktop computing became contested between Apple/IBM PowerPC, AMD AMD64, and Intel x86-32 — with Kastner articulating the canonical \"no 64-bit software yet\" critique that held for the next 2-3 years.*
**Prescience:** high — *Kastner's \"wait a year for real 64-bit apps\" prediction was directionally correct — Windows XP x64 Edition shipped Apr 2005 (~18 months later), and mainstream 64-bit adoption still took through Windows 7 (2009) to reach consumers. His framing of AMD64 as winning despite unclear market outcomes was c…*

## Entities (14)

- [[aberdeen-group|Aberdeen Group]]
- [[amd|Advanced Micro Devices, Inc.]]
- [[apple-computer|Apple Computer / Apple Inc.]]
- [[gartner-inc|Gartner, Inc.]]
- [[ibm|International Business Machines Corporation]]
- [[idc-corp|International Data Corporation (IDC)]]
- [[intel-corporation|Intel Corporation]]
- [[jay-lyman-journalist|Jay Lyman]]
- [[martin-reynolds-analyst|Martin Reynolds]]
- [[microsoft|Microsoft Corporation]]
- [[pc-world-magazine|PC World magazine]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[shane-rau-idc|Shane Rau]]
- [[technewsworld|TechNewsWorld / ECT News Network]]

## Technologies (7)

- [[amd-athlon-64|AMD Athlon 64 processor]]
- [[amd-opteron|AMD Opteron server processor]]
- [[amd64-architecture|AMD64 / x86-64 architecture (Opteron/Athlon 64)]]
- [[apple-powerpc-g5|Apple/IBM PowerPC G5 (PowerPC 970)]]
- [[intel-pentium-4|Intel Pentium 4 processor]]
- [[windows-xp-64bit|Microsoft Windows XP 64-bit Edition / Windows XP Professional x64 Edition]]
- [[x86-architecture|x86 instruction-set architecture]]

## Key observations (top 25)

- **2003** — Wait a year for 64-bit apps: Tune in a year from now, and then we'll have a better idea of how these chips run on real-world, 64-bit applications.
- **2003** — Athlon64 market unknown pending 64-bit XP: Apple developers are sure to develop programs quickly to take advantage of 64-bit computing. But for Athlon64, the market is still unknown because Microsoft's 64-bit version of Windows XP has yet to arrive.
- **2003** — Athlon competitive at heady price: Apple's G5 might in fact have been the fastest PC on the day it was made available; AMD's Athlon is a very competitive chip priced at a heady level for AMD.
- **2003** — No 64-bit software yet: That means users really aren't getting any benefit out of 64-bit instructions on Athlon or Apple. Neither Apple nor AMD users are truly taking advantage of 64-bit computing at this point, largely because of the lack of applications optimized for the…
- **2003** — Athlon 64 benchmarks beat G5/P4: PC World tests: Athlon 64 beat Apple Power Mac G5 and Intel Pentium 4 on Word, Premiere 6, Quake III frames-per-second, and (Opteron dual) Photoshop 7.0.1.
- **2003** — Memory bandwidth key to Opteron Photoshop win: Gartner's Martin Reynolds: memory bandwidth rather than raw processing speed delivered Opteron's Photoshop win; Apple's value is well beyond pure processor speed.
- **2006** — Apple abandons PowerPC: Apple announced Intel transition WWDC Jun 2005, shipped first Intel Macs Jan 2006, completed transition by Aug 2006 — validating Kastner's implicit skepticism that PowerPC G5 would retain a unique performance position. Power Mac Pro with Intel Xeon s…
- **2005** — AMD64 becomes mainstream: AMD64/x86-64 became the dominant desktop and server ISA: Windows XP x64 Edition shipped Apr 2005, Intel adopted EM64T 2004, AMD64 displaced IA-64 in server market by 2006 — fully validating the 2003 inflection.
- **2005** — 64-bit XP arrived 18 months later: Microsoft shipped Windows XP Professional x64 Edition Apr 25 2005 — roughly 18 months after this article, matching Kastner's 'tune in a year from now' call. But mainstream 64-bit consumer adoption waited until Windows 7 (Oct 2009).

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'technology-news-hardware-amd-beats-apple-5399ec' ORDER BY year_observed;
```

