---
title: "OLTP Market Analysis for Encore Computer Series 90"
slug: encore-b7c40d
page_type: study
author: "Peter S. Kastner"
date: "1990-01-01"
study_type: market-study
subject_domain: "OLTP-applications, commercial-computing-market"
methodology: "market-research, vertical-market-analysis, application-cataloging"
importance: medium
importance_rationale: "Provides a comprehensive snapshot of commercial OLTP application landscape circa 1990, with detailed vertical-market characterizations that reflect Aberdeen's deep domain expertise in transaction processing markets of that era."
relevance: low
relevance_rationale: "The specific application vendors, transaction volume benchmarks, and hardware suppliers are largely obsolete; the document's primary value is as a historical reference for early 1990s commercial computing application patterns."
prescience: medium
prescience_rationale: "The catalog correctly anticipated continued growth of distributed OLTP across all major verticals and the importance of packaged ISV applications over custom code, trends that proved central to the enterprise software boom of the 1990s."
license: CC-BY-4.0
tier: 2
entity_count: 9
tech_count: 8
obs_count: 18
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# OLTP Market Analysis for Encore Computer Series 90

> This reference catalog, prepared for Encore Computer's Series 90 engagement, surveys OLTP application requirements across major vertical markets including manufacturing, distribution, banking, insurance, retail, and government, documenting typical transaction volumes, leading application software vendors, and competitive hardware suppliers for each segment. The catalog serves as a structured market intelligence resource mapping vertical OLTP demand to hardware capability requirements, supporting Encore's commercial go-to-market planning. Coverage spans applications from shop floor control and MRP to online banking and airline reservation systems.

**Author:** Peter S. Kastner · **Date:** 1990-01-01 · **Type:** market-study
**Importance:** medium — *Provides a comprehensive snapshot of commercial OLTP application landscape circa 1990, with detailed vertical-market characterizations that reflect Aberdeen's deep domain expertise in transaction processing markets of that era.*
**Prescience:** medium — *The catalog correctly anticipated continued growth of distributed OLTP across all major verticals and the importance of packaged ISV applications over custom code, trends that proved central to the enterprise software boom of the 1990s.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[bbn-advanced-computers|BBN Advanced Computers, Inc.]]
- [[digital-equipment|Digital Equipment Corporation]]
- [[encore-computer|Encore Computer Corporation]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (8)

- [[encore-series90|Encore Computer Series 90]]
- [[ibm-cics|IBM CICS TP Monitor]]
- [[ibm-db2|IBM DB2]]
- [[ibm-mainframe-zarch|IBM zSeries Mainframe]]
- [[oltp-systems|Online Transaction Processing (OLTP)]]
- [[rdbms|Relational Database (RDBMS)]]
- [[tpc-c|TPC-C Benchmark]]
- [[unix|UNIX (various)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'encore-b7c40d' ORDER BY year_observed;
```

