---
title: "VTAM (Virtual Telecommunications Access Method)"
slug: "vtam"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/1974-"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "vtam"
category: "platform"
vendor: "IBM"
era: "1974-"
lifecycle_at_study: "mature"
lifecycle_current: "legacy-supported"
occurrence_count: 1
prescience_max: 0.0
prescience_mean: 0.0
prescience_obs_count: 1
---

# VTAM (Virtual Telecommunications Access Method)

> IBM's mainframe communications manager for SNA; required 1+ CPU-second to initialize each 3270 terminal session — the source of the SNA Tax at scale.


## Top observations

- 100 TPS benchmark required 10,000 virtual terminals × 1 CPU-second = 10,000 CPU-seconds of session overhead; over an hour of clock time on a 4-processor 3090-400 before a single transaction. `[ps=0]` — [[study-volume-1-ch06-dec-mainframes-last-stand-1987-1988]]
- VTAM (IBM's mainframe communications manager) required more than one full 3090 CPU-second just to log in a single 3270 terminal session. — [[study-volume-1-ch06-dec-mainframes-last-stand-1987-1988]]
