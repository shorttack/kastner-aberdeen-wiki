---
title: "High-Availability / Performance Clustering"
slug: "clustering"
page_type: "technology"
tags: ["type/technology", "category/server-architecture", "era/1980s-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "clustering"
category: "server-architecture"
vendor: "multiple"
era: "1980s-present"
lifecycle_at_study: "emerging"
lifecycle_current: "{'lifecycle_current': 'active', 'notes': 'High-availability and performance clustering remains fundamental to enterprise computing. Technologies like Kubernetes, Pacemaker, and proprietary HA clustering are actively used and developed.', 'source': 'General IT infrastructure'}"
occurrence_count: 2
prescience_max: 4.0
prescience_mean: 3.5
prescience_obs_count: 4
---

# High-Availability / Performance Clustering

> Multiple independent nodes cooperating via message-passing; used for HA and resource sharing but had software bottleneck issues in 1996.


## Top observations

- Today's system software and customer applications are not cluster-enabled; require re-engineering `[ps=4]` — [[study-1996-sequent-38f0b1]]
- Message-passing burns CPU and memory cycles; messaging between nodes is very complex technology requiring time to mature `[ps=4]` — [[study-1996-sequent-38f0b1]]
- Oracle Parallel Server cited as example of cluster software complexity; requires special versions and careful architecture `[ps=4]` — [[study-1996-sequent-38f0b1]]
- near-linear scaling of transaction processing `[ps=2]` — [[study-intel-infiband-wp--edit-psk-5-22f-a2c551]]
- Traditional SMP and cluster implementations are ill-suited to efficient scalability — [[study-1996-sequent-38f0b1]]
