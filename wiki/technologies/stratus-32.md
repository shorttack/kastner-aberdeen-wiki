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
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Stratus/32 Continuous Processing System

> 32-module fault-tolerant supermini for OLTP. Up to 32 processing modules per system; each module has 2 software-visible Motorola 68000 CPUs and up to 16MB memory.


## Top observations

- Up to 32 processing modules per Stratus system, connected via StrataLINK high-speed coax — [[study-ieee-db-stratus-32-psk-1d4564]]
- Memory + 2 Motorola 68000 CPUs (software-visible) + ≥1 disk + peripheral controllers; CPU board contains 4 actual 68000 dies (2 self-checking pairs) — [[study-ieee-db-stratus-32-psk-1d4564]]
- Fully redundant / partially redundant / non-redundant; configurable per module; reconfiguration on-line without affecting running programs — [[study-ieee-db-stratus-32-psk-1d4564]]
- 'Multiple modules are used only to achieve greater system capacity; they never serve as backup for other modules.' — [[study-ieee-db-stratus-32-psk-1d4564]]
- Single 125 nsec cycle-time high-speed bus implemented as two parallel buses with independent data and control-logic paths — [[study-ieee-db-stratus-32-psk-1d4564]]
- Each board runs two parallel sets of logic; on output, results are compared; mismatch lights red LED, raises bus interrupt, takes board off-line; redundant partner continues; no other component is aware — [[study-ieee-db-stratus-32-psk-1d4564]]
- Single CPU board = 4 Motorola 68000s organized as 2 software-visible CPUs; redundant virtual/physical address-translation maps; redundant partner CPU board for board-level fault tolerance — [[study-ieee-db-stratus-32-psk-1d4564]]
- Redundant config: N MB program-visible memory implemented as 2N MB physical, split across 2 controllers; 64K RAMs on 2MB boards; 375 nsec read cycle; 4-way interleaved; redundancy can be turned on/off dynamically — [[study-ieee-db-stratus-32-psk-1d4564]]
- A failed board can be replaced in a running system by a non-technical person without special tools and without affecting any user's program; VOS dynamically reconfigures — [[study-ieee-db-stratus-32-psk-1d4564]]
- Ad asserts hardware-component cost trajectory continues downward while software/people costs rise — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- $130,000 fully-duplexed, 2MB memory, peripherals, and software included — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- 17 Strathmore Road, Natick MA 01760; HQ marketing 617-653-1466 ext. 32 — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
- Ad dates to Kastner's Stratus Computer marketing tenure (early 1980s) — [[study-stratus-fault-tolerant-revolution-ad-198-797e0e]]
