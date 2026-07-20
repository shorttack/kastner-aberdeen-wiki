---
title: "ET1 Debit-Credit Benchmark"
slug: "et1-debit-credit"
page_type: "technology"
tags: ["type/technology", "category/transaction-processing-benchmark", "era/1985-1989"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "et1-debit-credit"
category: "transaction-processing-benchmark"
vendor: "industry / Anon-et-al / Datamation"
era: "1985-1989"
lifecycle_at_study: "current-1985"
lifecycle_current: "superseded-by-tpc-a"
occurrence_count: 2
prescience_max: 5.0
prescience_mean: 1.67
prescience_obs_count: 3
---

# ET1 Debit-Credit Benchmark

> Datamation April 1985 anon-et-al; subject of FTSN-33 cross-vendor reporting


## Top observations

- MIPS and Whetstone are inadequate for OLTP; with multiprocessor, MIPS changes as I/O processors are added; transaction benchmarks needed `[ps=5]` — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
- 1.0-1.1 tps/CPU (cross-reference from FTSN-32) `[ps=0]` — [[study-ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530]]
- 2M account records, 2K teller records, 200 branch records (1/5 anon-et-al spec) `[ps=0]` — [[study-ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530]]
