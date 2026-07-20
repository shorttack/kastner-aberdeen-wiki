---
title: "VAXft 3000"
slug: "vaxft-3000"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/1990-1998"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "vaxft-3000"
category: "platform"
vendor: "DEC"
era: "1990-1998"
lifecycle_at_study: "new-product"
lifecycle_current: "legacy-discontinued"
occurrence_count: 2
prescience_max: 3.0
prescience_mean: 2.0
prescience_obs_count: 3
---

# VAXft 3000

> First fault-tolerant VAX system; dual-zone architecture with duplicate hardware; four-phase verification strategy; uses FTSS software for error recovery; designed for continuous operation TP environments


## Top observations

- System comprises two duplicate zones (Zone A and Zone B); each zone is fully functional computer; connected by duplicate cross-link cables; dual-rail + single-rail design `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Phase 1: hardware simulation with fault insertion; Phase 2: hardware verification with system exerciser and fault insertion; Phase 3: system software verification with fault insertion; Phase 4: application verification with fault insertion `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Designed to recover from any single point of hardware failure; fault tolerance provided transparently for all VMS applications `[ps=0]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
