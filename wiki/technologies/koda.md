---
title: "KODA (database kernel)"
slug: "koda"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/1985-1998"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "koda"
category: "platform"
vendor: "DEC"
era: "1985-1998"
lifecycle_at_study: "mature"
lifecycle_current: "legacy-discontinued"
occurrence_count: 1
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# KODA (database kernel)

> Physical subsystem shared by Rdb/VMS and VAX DBMS; handles all I/O, buffer management, concurrency control, transaction consistency, locking, journaling, access methods; provides group commit processing


## Top observations

- 300 TPS — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- 464 TPS — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- 500 TPS — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Up to 66 percent improvement in transaction throughput using more efficient grouping designs — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Rdb/VMS and VAX DBMS share KODA kernel providing transaction capabilities and commit processing; data access independent of data model — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- For short TP transactions (modify 1 record): commit processing represents 36 percent of total transaction duration; for batch transactions (modify 500 records): commit processing only 0.2 percent — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
