---
title: "Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective"
slug: "study-auditor-report-4-43ad9b"
page_type: "study"
tags: ["type/study", "collection/benchmark"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "auditor-report-4-43ad9b"
author: "Peter S. Kastner"
date: "2004-04"
pub_year: 2004
type: "benchmark"
subject_domain: "Healthcare information systems / clinical software performance benchmarking"
methodology: "Independent audit of vendor-conducted benchmark; Mercury LoadRunner load simulation; 1-hour and 12-hour sustained load tests; isolation and slow-client tests"
source_file: "Archive-1/auditor_report_4.doc"
license: "CC-BY-4.0"
importance: "medium"
relevance: "medium"
study_prescience_enum: "low"
prescience_3y_enum: "medium"
prescience_5y_enum: "medium"
prescience_max: 4.0
prescience_mean: 0.29
prescience_obs_count: 21
---

# Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** medium — 3y Rule A: mean=3.43 over 21 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].
- **5-year verdict:** medium — 5y Rule A: mean=3.33 over 21 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].

> Aberdeen Group audit report commissioned by Eclipsys Corp. to independently verify performance benchmarks for SunriseXA Release 3.3, a healthcare clinical information system. Benchmark simulated a 6,000-bed hospital at peak load (5,000 orders/hour, 2.27x the busiest known real hospital rate), executing 65,637 transactions in one steady-state hour via Mercury LoadRunner. Results confirmed subsecond response times for 4 of 5 transaction categories; only administrative log-on (multi-patient download) and batch group-order transactions exceeded 1 second. Database server CPU utilization was only 40% at peak. Aberdeen concludes Eclipsys successfully resolved response time issues identified in October 2003.


_Published 2004, author **Peter S. Kastner**, type **benchmark**._


## Top observations

- Comparable scalability; capable of handling high-end volume workloads `[ps=4]`
- Viable; sufficient throughput and headroom demonstrated `[ps=3]`
- 65,637 transactions `[ps=0]`
- >1,000 transactions per minute `[ps=0]`
- 40% `[ps=0]`
- 0.54s avg (geom); 1.62s 99th pct; 6,525 transactions `[ps=0]`
- 0.12s avg (geom); 0.36s 99th pct; 17,986 transactions `[ps=0]`
- 0.09s avg (geom); 0.25s 99th pct; 21,549 transactions `[ps=0]`
- 0.11s avg (geom); 0.51s 99th pct; 13,073 transactions `[ps=0]`
- 0.18s avg (geom); 0.62s 99th pct; 6,504 transactions `[ps=0]`
- 8 of 82 transaction types `[ps=0]`
- 11.85 seconds `[ps=0]`
- 721,158 transactions over 715 minutes `[ps=0]`
- 82 different transaction types `[ps=0]`
- Acceptable; response times similar to LoadRunner results on Pentium III 750-MHz 256MB via 11-Mbps wireless `[ps=0]`
- Sub-2-second for all transaction types `[ps=0]`
- Early summer 2004 `[ps=0]`
- [UNVERIFIED] `[ps=0]`
- No perceptible change in response time or throughput when SUT disconnected from wider network `[ps=0]`
- 2.50 seconds avg; 99th percentile 6.74 seconds `[ps=0]`
- 6,000-bed hospital at 5,000 orders/hour = 2.27x busiest known real hospital (2,200 orders/hour) `[ps=-1]`
