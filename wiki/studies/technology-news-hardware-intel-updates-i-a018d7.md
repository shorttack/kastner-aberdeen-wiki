---
title: "Intel Updates Itanium 2 Processors"
slug: technology-news-hardware-intel-updates-i-a018d7
page_type: study
author: "Gene J. Koprowski, TechNewsWorld"
date: "2004-04-13"
study_type: news-article
subject_domain: "64-bit-server-processors-itanium"
methodology: "product-launch-analysis, analyst-commentary"
importance: high
importance_rationale: "Documents Apr 2004 Itanium 2 refresh — at peak of Intel IA-64 strategy, with Itanium-Xeon merger signaling but not yet executed. Kastner's 'Intel drop the other shoe' prediction and 100,000-unit Itanium deployment number became widely cited analyst benchmarks for tracking Intel's subsequent 64-bit strategy shift (EM64T on Xeon the following quarter, Jun 2004)."
relevance: high
relevance_rationale: "The architecture-competing-against-ecosystem dynamic Kastner articulated — new ISA needs software volume to succeed, volume needs consumer commitment — recurs every architectural generation. Exactly the issue for ARM-on-Windows (2012-2020), Intel Optane persistent memory (2015-2022 discontinued), Apple Silicon on macOS (~2 years to mature ecosystem 2020-2022), AI-PC NPUs (2024+)."
prescience: high
prescience_rationale: "Kastner's 'not this year' prediction for mass-market 64-bit was dead-accurate: Windows XP x64 Edition didn't ship until Apr 2005. The 'drop the other shoe' framing — Intel abandoning IA-64 exclusivity for 64-bit-on-x86 — was validated in Jun 2004 with EM64T Xeon. Itanium was effectively dead by 2008 (Oracle, Red Hat, Microsoft drops); Itanium ended Jul 2021 — exactly the trajectory Kastner's 100K-units-deployed skepticism implied."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 5
obs_count: 7
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Intel Updates Itanium 2 Processors

> TechNewsWorld article (Apr 13 2004, Gene J. Koprowski) on Intel's Taipei developer-forum disclosure of two new lower-priced Itanium 2 processors (1.4 GHz and 1.6 GHz, both with 3 MB L3 cache; servers ~28% lower in price and up to 25% faster than prior Itanium 2). Intel's Richard Dracott positions this as merging Itanium and Xeon into common infrastructure. Audi AG cited as early Itanium 2 / HP Integrity adopter for automotive design simulation. Aberdeen chief research analyst Peter Kastner delivers the decisive skeptical read on 64-bit consumer demand: 'There are only about 100,000 Intel Itanium 64-bit machines on the market today, indicating that 64-bit computing will not be truly significant for users nor for software developers like Microsoft until Intel commits more wholeheartedly to the technology.' And the now-famous prediction: 'Very few consumer desktops can take advantage of 64-bit. Intel has to drop the other shoe and deem that the broad, mass market for consumers is ready for 64-bit. I predict that will not be this year.'

**Author:** Gene J. Koprowski, TechNewsWorld · **Date:** 2004-04-13 · **Type:** news-article
**Importance:** high — *Documents Apr 2004 Itanium 2 refresh — at peak of Intel IA-64 strategy, with Itanium-Xeon merger signaling but not yet executed. Kastner's 'Intel drop the other shoe' prediction and 100,000-unit Itanium deployment number became widely cited analyst benchmarks for tracking Intel's subsequent 64-bit s…*
**Prescience:** high — *Kastner's 'not this year' prediction for mass-market 64-bit was dead-accurate: Windows XP x64 Edition didn't ship until Apr 2005. The 'drop the other shoe' framing — Intel abandoning IA-64 exclusivity for 64-bit-on-x86 — was validated in Jun 2004 with EM64T Xeon. Itanium was effectively dead by 2008…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[amd|Advanced Micro Devices, Inc.]]
- [[audi-ag|Audi AG]]
- [[gene-j-koprowski-journalist|Gene J. Koprowski]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[intel-corporation|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[richard-dracott-intel|Richard Dracott]]
- [[technewsworld|TechNewsWorld / ECT News Network]]

## Technologies (5)

- [[amd64-architecture|AMD64 / x86-64 architecture (Opteron/Athlon 64)]]
- [[intel-itanium|Intel Itanium (IA-64)]]
- [[intel-xeon|Intel Xeon server processor]]
- [[windows-xp-64bit|Microsoft Windows XP 64-bit Edition / Windows XP Professional x64 Edition]]
- [[x86-architecture|x86 instruction-set architecture]]

## Key observations (top 25)

- **2004** — 100,000 Itanium units deployed: There are only about 100,000 Intel Itanium 64-bit machines on the market today, indicating that 64-bit computing will not be truly significant for users nor for software developers like Microsoft until Intel commits more wholeheartedly to the technol…
- **2004** — Not this year for mass-market 64-bit: Very few consumer desktops can take advantage of 64-bit. Intel has to drop the other shoe and deem that the broad, mass market for consumers is ready for 64-bit. I predict that will not be this year.
- **2004** — Itanium 2 refresh specs: Intel new Itanium 2: 1.4 GHz with 3 MB L3 cache (available now); 1.6 GHz same cache available May. Servers ~28% lower in price, up to 25% faster than earlier Itanium 2. Announced at developer forum in Taipei, Taiwan. Intel server architectures ~85% o…
- **2004** — Itanium-Xeon merger: Intel's Richard Dracott: In the next few years, system manufacturers will be able to design an Itanium 2 processor and Intel Xeon processor-based system using the same low-cost components. Every product and technology we roll out moves us one step cl…
- **2004** — Audi switches from RISC to Itanium: Audi AG switched from RISC-based servers to HP Integrity servers running Itanium 2 dual-processor systems for car-ventilation-system design. Audi spokesperson: 'Better price-performance and increase our ability to perform a wide range of what-if scen…
- **2005** — XP x64 ships Apr 2005: Microsoft shipped Windows XP Professional x64 Edition Apr 25 2005 on AMD64 — roughly one year after Kastner's 'not this year' prediction. Consumer 64-bit adoption waited for Windows 7 (Oct 2009) for true mass-market. Kastner's timing was exact.
- **2021** — Itanium end-of-life: Intel shipped the last Itanium processor (Kittson) in Jul 2021. Itanium volume peaked below 200,000 annually and was effectively superseded by AMD64/Intel 64 on Xeon starting Jun 2004 (3 months after this article) — directly validating Kastner's depl…

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'technology-news-hardware-intel-updates-i-a018d7' ORDER BY year_observed;
```

