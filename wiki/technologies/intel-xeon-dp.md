---
title: "Intel Xeon (dual-processor)"
slug: "intel-xeon-dp"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/2001-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "intel-xeon-dp"
category: "platform"
vendor: "Intel"
era: "2001-present"
lifecycle_at_study: "mature"
lifecycle_current: "active"
occurrence_count: 1
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Intel Xeon (dual-processor)

> Server CPU line; bus loading issue analyzed.


## Top observations

- Physics concern: if Intel connects both on-die cores to the external bus directly, a two-socket four-core Xeon sees capacitance of 4 CPUs and a four-socket eight-core system sees 8 CPUs. Today's DP (3 loads) runs at 800MHz; 4-way (5 loads) runs at 400MHz. Two-socket four-core Xeon may see only 3.2GB/s bus bandwidth — step down from current 6.4GB/s; AMD can deliver 13.2GB/s. — [[study-intel-longlivedualcore-revised-5-fa8298]]
- First-generation dual-core Xeon (Paxville DP, November 2005, Lindenhurst platform) had a known front-side bus bottleneck. The shared FSB architecture meant both cores competed for memory bandwidth. The Paxville/Lindenhurst platform used DDR2 with a single shared bus per processor pair, resulting in bandwidth contention confirmed by benchmark reviews. — [[study-intel-longlivedualcore-revised-5-fa8298]]
