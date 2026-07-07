---
title: "Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)"
slug: "study-intel-longlivedualcore-revised-5-fa8298"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "intel-longlivedualcore-revised-5-fa8298"
author: "Nathan Brookwood (Insight 64)"
date: "2004-09-16"
pub_year: 2004
type: "market-study"
subject_domain: "microprocessors/multicore-transition"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
source_file: "Intel-LongLiveDualCore-Revised-5.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 3.71
prescience_obs_count: 14
---

# Intel's Fall Developer Forum (IDF): Megahertz is Dead, Long Live Dual-Core (Revised)

> Insight 64 analyst report by Nathan Brookwood on Intel Fall 2004 IDF. Paul Otellini officially closed two decades of MHz-driven CPU scaling and announced the shift to multi-core parallelism. Analyzes the NetBurst power/performance trend, Pentium M Dothan (2GHz/21W, 140M transistors) versus Prescott (3.2GHz/82W, 125M) as exemplars of architecture over brute-force frequency, and the competitive bus-bandwidth disadvantage (3.2GB/s versus AMD's 13.2GB/s) if Intel used an inelegant dual-core design. Preserved in the Kastner archive as external reference material.


_Published 2004, author **Nathan Brookwood (Insight 64)**, type **market-study**._


## Top observations

- Paul Otellini at Fall 2004 IDF officially lowered the curtain on two decades of ever-increasing clock frequencies as the principal tactic for increasing PC/server performance — shifting to parallelism (multi-core). `[ps=5]`
- At 90nm generation, chip designers could only achieve 2 of 3 attributes (smaller, faster, less power). Products relying on architectural parallelism will have inherent advantages over brute-force (MHz) products. `[ps=5]`
- Pentium M Dothan: 2GHz, 21W, 140M transistors — matches 3.2GHz Prescott (82W, 125M transistors) performance at ~1/4 the power. Dothan uses slightly slower transistors, a dramatic power-consumption win. `[ps=5]`
- First-generation dual-core Xeon (Paxville DP, November 2005, Lindenhurst platform) had a known front-side bus bottleneck. The shared FSB architecture meant both cores competed for memory bandwidth. The Paxville/Lindenhurst platform used DDR2 with a single shared bus per processor pair, resulting in bandwidth contention confirmed by benchmark reviews. `[ps=5]`
- Users segment into (a) ~70% basic productivity/Internet/email (any system suffices) and (b) power users (large DB updates, risk arb, multi-player games, video/DVD editing) who truly benefit from increased CPU performance. `[ps=4]`
- Over 4 years (2000-2004), NetBurst processors increased performance 3.2x while max TDP rose 2.1x. Each 100MHz adds 2.5W; fastest P4s consume almost 110W. `[ps=4]`
- Projection: Intel dual-core desktop at 2.5GHz per core @ 40W each → combined ~2400 SPECint at 100W. A single-core equivalent would need 4.6GHz and 130W+. `[ps=4]`
- Intel's first-generation dual-core (Pentium D/Paxville) delivered disappointing performance-per-watt. Pentium D ran hot and power-inefficient under 90nm process. Core 2 Duo (Conroe/Merom, July 2006) delivered the significant performance-per-watt improvement. The prediction that dual-core would bring meaningful efficiency gains was validated by Core 2, though the first-gen Pentium D was inefficient `[ps=4]`
- Unlike 64-bit x86 computing (on hold pending Windows for 64-bit Extended x86 release), there is little Microsoft can do to slow multi-core migration — other than raising prices on multi-processor OS versions. `[ps=4]`
- Moore's Law (1965) specified transistor-density doubling via lithography, not clock frequency. Moore never specified what designers should do with extra transistors — basic economics dictated value-add via performance or function. `[ps=3]`
- Transition to multi-core raises few software-visible issues. All major x86 OSes (Windows, Linux, UNIX) already support multiprocessor configurations; HyperThreading investments apply directly to dual-core. `[ps=3]`
- Sun and HP began deliveries of dual-core RISC systems in February 2004. `[ps=3]`
- AMD started with dual-core chip designs (Hammer/POWER4 style); initial 130nm Opteron had room for only one core but slots for second already present. Replication of CPU0+L2 cache boxes was trivially simple compared to Sun/Intel retrofits. `[ps=3]`
- Intel demonstrated dual-core Itanium (Montecito) at Fall 2004 IDF alongside Xeon roadmap entries. `[ps=0]`
- Insight 64 believes AMD may have a technology advantage over the next six quarters if it continues smooth execution; Intel and AMD remain in a 'bitter dogfight.'
- IBM delivered first dual-core POWER4-based systems three years prior (2001); second-generation dual-core shipped spring 2004.
- Physics concern: if Intel connects both on-die cores to the external bus directly, a two-socket four-core Xeon sees capacitance of 4 CPUs and a four-socket eight-core system sees 8 CPUs. Today's DP (3 loads) runs at 800MHz; 4-way (5 loads) runs at 400MHz. Two-socket four-core Xeon may see only 3.2GB/s bus bandwidth — step down from current 6.4GB/s; AMD can deliver 13.2GB/s.
- Bill Siu (GM Intel Desktop Platforms) narrated dual-core demo on 915 Grantsdale platform, described as 'engineering prototype' with 'real silicon.' Three possibilities: (1) first-silicon production sample (discounted); (2) multi-chip package of two Pentium chips; (3) more likely — custom DP motherboard around 915 chipset (normally uniprocessor-only).
