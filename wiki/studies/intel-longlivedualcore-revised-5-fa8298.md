---
title: "Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)"
slug: intel-longlivedualcore-revised-5-fa8298
page_type: study
author: "Nathan Brookwood (Insight 64)"
date: "2004-09-16"
study_type: market-study
subject_domain: "microprocessors/multicore-transition"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
importance: high
importance_rationale: "First-class contemporaneous analyst interpretation of the industry-defining 2004 pivot from frequency scaling to multi-core parallelism. Brookwood's framing ('Megahertz is Dead, Long Live Dual-Core') became a widely adopted shorthand for the transition."
relevance: medium
relevance_rationale: "Technical detail is historical, but the architectural lessons (parallelism over frequency, power/thermal ceilings, bus capacitance in multi-CPU designs) remain foundational for modern CPU and GPU design."
prescience: high
prescience_rationale: "Predictions proved highly accurate: multi-core became universal 2005-2010, AMD's bandwidth advantage held for ~18 months, and Intel's Core microarchitecture (2006) confirmed the design-over-frequency thesis."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 13
obs_count: 18
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)

> Insight 64 analyst report by Nathan Brookwood on Intel Fall 2004 IDF. Paul Otellini officially closed two decades of MHz-driven CPU scaling and announced the shift to multi-core parallelism. Analyzes the NetBurst power/performance trend, Pentium M Dothan (2GHz/21W, 140M transistors) versus Prescott (3.2GHz/82W, 125M) as exemplars of architecture over brute-force frequency, and the competitive bus-bandwidth disadvantage (3.2GB/s versus AMD's 13.2GB/s) if Intel used an inelegant dual-core design. Preserved in the Kastner archive as external reference material.

**Author:** Nathan Brookwood (Insight 64) · **Date:** 2004-09-16 · **Type:** market-study
**Importance:** high — *First-class contemporaneous analyst interpretation of the industry-defining 2004 pivot from frequency scaling to multi-core parallelism. Brookwood's framing ('Megahertz is Dead, Long Live Dual-Core') became a widely adopted shorthand for the transition.*
**Prescience:** high — *Predictions proved highly accurate: multi-core became universal 2005-2010, AMD's bandwidth advantage held for ~18 months, and Intel's Core microarchitecture (2006) confirmed the design-over-frequency thesis.*

## Entities (12)

- [[amd|Advanced Micro Devices (AMD)]]
- [[bill-siu|Bill Siu]]
- [[gordon-moore|Gordon Moore]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[insight-64|Insight 64]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[nathan-brookwood|Nathan Brookwood]]
- [[paul-otellini|Paul Otellini]]
- [[pci-sig|PCI Special Interest Group]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (13)

- [[amd-hammer|AMD Hammer (K8) architecture]]
- [[amd-opteron|AMD Opteron]]
- [[hyperthreading|Intel HyperThreading Technology]]
- [[ibm-power-4|IBM POWER4]]
- [[intel-915-grantsdale|Intel 915 (Grantsdale) chipset]]
- [[intel-itanium-montecito|Intel Itanium Montecito (dual-core)]]
- [[intel-netburst|Intel NetBurst Architecture]]
- [[intel-pentium-4-prescott|Intel Pentium 4 Prescott]]
- [[intel-pentium-m-dothan|Intel Pentium M Dothan]]
- [[intel-xeon-dp|Intel Xeon (dual-processor)]]
- [[moores-law|Moore's Law]]
- [[pci-express|PCI Express (PCI-E)]]
- [[sun-ultrasparc-iii|Sun UltraSPARC III (dual-core)]]

## Key observations (top 25)

- **2004** — otellini-ends-mhz-race: Paul Otellini at Fall 2004 IDF officially lowered the curtain on two decades of ever-increasing clock frequencies as the principal tactic for increasing PC/server performance — shifting to parallelism (multi-core).
- **2004** — amd-6q-advantage: Insight 64 believes AMD may have a technology advantage over the next six quarters if it continues smooth execution; Intel and AMD remain in a 'bitter dogfight.'
- **2004** — user-performance-segmentation: Users segment into (a) ~70% basic productivity/Internet/email (any system suffices) and (b) power users (large DB updates, risk arb, multi-player games, video/DVD editing) who truly benefit from increased CPU performance.
- **2004** — moores-law-density-not-frequency: Moore's Law (1965) specified transistor-density doubling via lithography, not clock frequency. Moore never specified what designers should do with extra transistors — basic economics dictated value-add via performance or function.
- **2004** — 90nm-tradeoff: At 90nm generation, chip designers could only achieve 2 of 3 attributes (smaller, faster, less power). Products relying on architectural parallelism will have inherent advantages over brute-force (MHz) products.
- **2004** — netburst-4yr-trend: Over 4 years (2000-2004), NetBurst processors increased performance 3.2x while max TDP rose 2.1x. Each 100MHz adds 2.5W; fastest P4s consume almost 110W.
- **2004** — dothan-vs-prescott: Pentium M Dothan: 2GHz, 21W, 140M transistors — matches 3.2GHz Prescott (82W, 125M transistors) performance at ~1/4 the power. Dothan uses slightly slower transistors, a dramatic power-consumption win.
- **2004** — intel-dual-core-projection: Projection: Intel dual-core desktop at 2.5GHz per core @ 40W each → combined ~2400 SPECint at 100W. A single-core equivalent would need 4.6GHz and 130W+.
- **2004** — intel-dual-core-actual: [UNVERIFIED]
- **2004** — sw-visibility-multicore: Transition to multi-core raises few software-visible issues. All major x86 OSes (Windows, Linux, UNIX) already support multiprocessor configurations; HyperThreading investments apply directly to dual-core.
- **2004** — ibm-dual-core-precedent: IBM delivered first dual-core POWER4-based systems three years prior (2001); second-generation dual-core shipped spring 2004.
- **2004** — sun-hp-dual-core-feb-2004: Sun and HP began deliveries of dual-core RISC systems in February 2004.
- **2004** — amd-dual-core-design-simpler: AMD started with dual-core chip designs (Hammer/POWER4 style); initial 130nm Opteron had room for only one core but slots for second already present. Replication of CPU0+L2 cache boxes was trivially simple compared to Sun/Intel retrofits.
- **2004** — montecito-demo-idf: Intel demonstrated dual-core Itanium (Montecito) at Fall 2004 IDF alongside Xeon roadmap entries.
- **2004** — bus-capacitance-risk: Physics concern: if Intel connects both on-die cores to the external bus directly, a two-socket four-core Xeon sees capacitance of 4 CPUs and a four-socket eight-core system sees 8 CPUs. Today's DP (3 loads) runs at 800MHz; 4-way (5 loads) runs at 40…
- **2004** — bus-capacitance-actual: [UNVERIFIED]
- **2004** — idf-demo-dual-core: Bill Siu (GM Intel Desktop Platforms) narrated dual-core demo on 915 Grantsdale platform, described as 'engineering prototype' with 'real silicon.' Three possibilities: (1) first-silicon production sample (discounted); (2) multi-chip package of two P…
- **2004** — windows-64bit-hold: Unlike 64-bit x86 computing (on hold pending Windows for 64-bit Extended x86 release), there is little Microsoft can do to slow multi-core migration — other than raising prices on multi-processor OS versions.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'intel-longlivedualcore-revised-5-fa8298' ORDER BY year_observed;
```

