---
title: "Disk Mirroring (RAID-1 precursor)"
slug: "disk-mirroring"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/1980-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "disk-mirroring"
category: "platform"
vendor: "industry"
era: "1980-present"
lifecycle_at_study: "emerging"
lifecycle_current: "mature"
occurrence_count: 1
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Disk Mirroring (RAID-1 precursor)

> Each Stratus disk has a duplicate on a separate controller; OS chooses less-busy or better-positioned disk for reads; transparent to applications.


## Top observations

- Each disk can have a duplicate on a separate controller; writes go to both; reads come from the disk that is not busy or whose heads are best positioned; read errors retried from mirror — [[study-ieee-db-stratus-32-psk-1d4564]]
- Verified: disk mirroring (RAID-1) was formalized by Patterson/Gibson/Katz 1988 and became the default redundancy mode for transactional systems through the 2010s; SSD/NVMe and erasure coding now dominate at hyperscale but mirroring remains in transactional tiers — [[study-ieee-db-stratus-32-psk-1d4564]]
