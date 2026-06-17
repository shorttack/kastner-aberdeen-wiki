---
title: "DECdta (Digital Distributed Transaction Architecture)"
slug: "decdta"
page_type: "technology"
tags: ["type/technology", "category/framework", "era/1988-1998"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "decdta"
category: "framework"
vendor: "DEC"
era: "1988-1998"
lifecycle_at_study: "growth"
lifecycle_current: "legacy-discontinued"
occurrence_count: 1
prescience_max: 4.0
prescience_mean: 2.75
prescience_obs_count: 4
---

# DECdta (Digital Distributed Transaction Architecture)

> Defines modularization and distribution structure common to DECtp products; six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager; client/server model


## Top observations

- Six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Atomicity, Serializability, Durability — the three transaction properties `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Communication managers separated from transaction managers; communication manager propagates 2PC messages to remote nodes; enables multiple commit protocols (IBM SNA LU6.2, OSI-TP) simultaneously `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- This combination of architecture, software, hardware technology, and support for emerging industry standards places Digital in excellent position to become industry leader for distributed portable transaction processing systems `[ps=1]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
