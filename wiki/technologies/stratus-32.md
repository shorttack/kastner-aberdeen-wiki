---
title: "Stratus/32 Continuous Processing System"
slug: "stratus-32"
page_type: "technology"
tags: ["type/technology", "category/computing-system", "era/1981-1990s"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "stratus-32"
category: "computing-system"
vendor: "Stratus Computer"
era: "1981-1990s"
lifecycle_at_study: "introduced"
lifecycle_current: "obsolete"
occurrence_count: 2
prescience_max: 5.0
prescience_mean: 1.23
prescience_obs_count: 13
---

# Stratus/32 Continuous Processing System

> 32-module fault-tolerant supermini for OLTP. Up to 32 processing modules per system; each module has 2 software-visible Motorola 68000 CPUs and up to 16MB memory.


## Top observations

- Ad asserts hardware-component cost trajectory continues downward while software/people costs rise `[ps=5]` — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- Fully redundant / partially redundant / non-redundant; configurable per module; reconfiguration on-line without affecting running programs `[ps=4]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- A failed board can be replaced in a running system by a non-technical person without special tools and without affecting any user's program; VOS dynamically reconfigures `[ps=4]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Single CPU board = 4 Motorola 68000s organized as 2 software-visible CPUs; redundant virtual/physical address-translation maps; redundant partner CPU board for board-level fault tolerance `[ps=2]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- 'Multiple modules are used only to achieve greater system capacity; they never serve as backup for other modules.' `[ps=1]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Up to 32 processing modules per Stratus system, connected via StrataLINK high-speed coax `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Memory + 2 Motorola 68000 CPUs (software-visible) + ≥1 disk + peripheral controllers; CPU board contains 4 actual 68000 dies (2 self-checking pairs) `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Single 125 nsec cycle-time high-speed bus implemented as two parallel buses with independent data and control-logic paths `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Each board runs two parallel sets of logic; on output, results are compared; mismatch lights red LED, raises bus interrupt, takes board off-line; redundant partner continues; no other component is aware `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Redundant config: N MB program-visible memory implemented as 2N MB physical, split across 2 controllers; 64K RAMs on 2MB boards; 375 nsec read cycle; 4-way interleaved; redundancy can be turned on/off dynamically `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- $130,000 fully-duplexed, 2MB memory, peripherals, and software included `[ps=0]` — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- 17 Strathmore Road, Natick MA 01760; HQ marketing 617-653-1466 ext. 32 `[ps=0]` — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- Ad dates to Kastner's Stratus Computer marketing tenure (early 1980s) `[ps=0]` — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
