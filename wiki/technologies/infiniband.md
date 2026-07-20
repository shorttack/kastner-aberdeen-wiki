---
title: "InfiniBand Architecture (IBA)"
slug: "infiniband"
page_type: "technology"
tags: ["type/technology", "category/high-performance-interconnect", "era/1999-present"]
tier: 1
source_csv: "_master_technologies.csv"
tech_id: "infiniband"
category: "high-performance-interconnect"
vendor: "InfiniBand Trade Association"
era: "1999-present"
lifecycle_at_study: "production-shipping"
lifecycle_current: "{'lifecycle_current': 'active', 'notes': 'Dominant interconnect in HPC and AI data centers. InfiniBand switch sales surged Q2 2025 driven by NVIDIA Blackwell Ultra. NVIDIA continues manufacturing HDR/NDR InfiniBand products.', 'source': 'https://www.delloro.com/news/infiniband-switch-sales-surged-in-2q-2025-while-ethernet-maintains-market-lead-for-ai-back-end-networks/'}"
occurrence_count: 6
prescience_max: 5.0
prescience_mean: 1.96
prescience_obs_count: 47
---

# InfiniBand Architecture (IBA)

> High-speed low-latency data center I/O interconnect; became standard in HPC and AI training clusters; owned by NVIDIA since 2020


## Summary




## Top observations

- NVIDIA acquired Mellanox for $7 billion in 2020 making NVIDIA the InfiniBand market owner `[ps=5]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- 2.5 Gbps to 10 Gbps today; expected to reach up to 30 Gbps as it evolves `[ps=5]` — [[study-infiniband-and-beyond-computerworld-supp-200261]]
- Mixed — did NOT broadly displace TCP/IP in enterprise server-to-server. Substantively validated in HPC (top-500 supercomputers majority-InfiniBand by 2010s) and AI-training clusters (NVIDIA acquired Mellanox 2019 for $6.9B; InfiniBand HDR/NDR the dominant fabric for GPU training 2022-2026). Enterprise storage adopted RoCE/iWARP-over-Ethernet as alternative. `[ps=5]` — [[study-infiniband-and-beyond-computerworld-supp-200261]]
- Bandwidth scales as number of I/O ports increases; IBA overcomes shared bus bandwidth ceiling `[ps=5]` — [[study-infiniband-data-center-wp-2002]]
- Intel's exit is good for the InfiniBand ecosystem (contrary to other opinions) `[ps=4]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- InfiniBand initiative will not be damaged by Intel's exit `[ps=4]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- 'InfiniBand works at very high speeds with very low latency and is a very efficient and transparent protocol.' Plus: parallel connections with low CPU use, enabling huge I/O bandwidth; low-latency blade-to-blade messaging for clustering. `[ps=4]` — [[study-infiniband-and-beyond-computerworld-supp-200261]]
- 500 MB/s per link minimum scaling to 6 GB/s; 12-wire config reaches 30 Gb/s `[ps=4]` — [[study-infiniband-data-center-wp-2002]]
- Virtual Lanes allow QoS multiplexing on same physical link; every switch acts as QoS director `[ps=4]` — [[study-infiniband-data-center-wp-2002]]
- Decouples CPU from I/O controller; extends distance from inches to kilometers `[ps=4]` — [[study-infiniband-data-center-wp-2002]]
- Enterprise production deployment possible starting 2003; first-gen HW/SW available late 2002 `[ps=4]` — [[study-infiniband-data-center-wp-2002]]
- IBA well positioned to become transport of choice for inter-processor communications and server clustering `[ps=4]` — [[study-infiniband-data-center-wp-2002]]
- Many industry observers believe Intel's decision will cause InfiniBand to stall `[ps=3]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- Intel's decision is good for Intel `[ps=3]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- Important next-generation data-center I/O initiative supported by IT industry broadly `[ps=3]` — [[study-2002-does-intel-s-decision-not-to-manufactur-iniband-si-0bd64b]]
- 'InfiniBand Architecture: Planning the Next Generation Data Centre' — published 2002 `[ps=3]` — [[study-infiniband-and-beyond-computerworld-supp-200261]]
- Phased deployment beginning 2003; HCA silicon on system board by late 2003 `[ps=3]` — [[study-infiniband-data-center-wp-2002]]
- Large enterprise and research data centers where greatest need for expanded I/O bandwidth exists `[ps=3]` — [[study-infiniband-data-center-wp-2002]]
- IBA >70% of TOP500 supercomputers by mid-2010s; dominant AI/ML training cluster fabric `[ps=3]` — [[study-infiniband-data-center-wp-2002]]
- Multiple different cables in enterprise rack replaced with single common cable per server/storage unit `[ps=3]` — [[study-infiniband-data-center-wp-2002]]
