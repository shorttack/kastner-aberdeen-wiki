---
title: "Stratus TP-1 Internal Transaction Benchmark"
slug: "stratus-tp1-benchmark"
page_type: "technology"
tags: ["type/technology", "category/internal-benchmark", "era/1980s"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "stratus-tp1-benchmark"
category: "internal-benchmark"
vendor: "Stratus"
era: "1980s"
lifecycle_at_study: "current-1985"
lifecycle_current: "obsolete-superseded-by-tpc-a-b-c"
occurrence_count: 2
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Stratus TP-1 Internal Transaction Benchmark

> Stratus's internal TP1; not the same as ET1; 5 reads + 2 rewrites + 1 log write per tx


## Top observations

- TP1 and ET1 are NOT the same benchmark or even a variation; vendor comparisons based on TP1-vs-ET1 results are invalid — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
- 150ms CPU loop + 5 indexed reads + 2 rewrites + 1 sequential log write; PL1 requester, COBOL server; Stratus TPF — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
- 5 indexed reads + 2 indexed rewrites + 1 sequential log write per tx; 5000-cycle requester loop, 200-cycle server loop; 30s sleep +/- 5s; no screen I/O, no comms — [[study-stratus-internal-benchmark-tuning-guide--c53e3f]]
- Task metering had no measurable effect; cache utilization significantly impacts performance; multiple server copies greatly improve performance — [[study-stratus-internal-benchmark-tuning-guide--c53e3f]]
