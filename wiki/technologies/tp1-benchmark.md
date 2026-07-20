---
title: "TP-1 performance model (Stratus internal)"
slug: "tp1-benchmark"
page_type: "technology"
tags: ["type/technology", "category/performance-benchmark", "era/1983-1986"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "tp1-benchmark"
category: "performance-benchmark"
vendor: "Stratus internal"
era: "1983-1986"
lifecycle_at_study: "internal-tool"
lifecycle_current: "superseded"
occurrence_count: 1
prescience_max: 5.0
prescience_mean: 1.8
prescience_obs_count: 5
---

# TP-1 performance model (Stratus internal)

> Requester/Server model — COBOL/TPF requester + PL/1 server


## Top observations

- Cache utilization significant; disk type/count/file-size dominant; multiple server copies help; server priority > requester priority `[ps=5]` — [[study-stratus-tp-1-internal-benchmark-guide-19-9b51bf]]
- Requester (COBOL/TPF) + Server (PL/1) pattern; transactions on delay interval; no screen/comm I/O; duplicated servers; varied file types/sizes `[ps=4]` — [[study-stratus-tp-1-internal-benchmark-guide-19-9b51bf]]
- 2.9 `[ps=0]` — [[study-stratus-tp-1-internal-benchmark-guide-19-9b51bf]]
- 2.3 `[ps=0]` — [[study-stratus-tp-1-internal-benchmark-guide-19-9b51bf]]
- 1.8 `[ps=0]` — [[study-stratus-tp-1-internal-benchmark-guide-19-9b51bf]]
