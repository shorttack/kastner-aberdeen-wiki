---
title: "A.T. Kearney Benchmark: Flagship Business Desktop Price Tracking, Aug 2002 – Mar 2003"
slug: dct-at-kearney-business-pc-prices
page_type: study
author: "Peter S. Kastner"
date: "2003-03-10"
study_type: dct
subject_domain: "dct"
methodology: "benchmarking"
importance: medium
importance_rationale: "A.T. Kearney-commissioned quantitative benchmark capturing the sharp Q4 2002 price rebound and the spread between aggressive (Dell, IBM) and price-retreating (Gateway, HP) vendors."
relevance: low
relevance_rationale: "Narrow benchmark snapshot; useful for consultants studying 2002-2003 enterprise PC pricing dynamics."
prescience: not-applicable
prescience_rationale: "Price-tracking benchmark; no predictive content."
license: CC-BY-4.0
tier: 2
entity_count: 5
tech_count: 2
obs_count: 33
tags: [type/study, importance/medium, prescience/not-applicable, decade/2000s]
source_csv: master_studies.csv
---

# A.T. Kearney Benchmark: Flagship Business Desktop Price Tracking, Aug 2002 – Mar 2003

> Six-date longitudinal price benchmark (Aug 20, Oct 2, Nov 8, Dec 2, Dec 17, 2002; Mar 10, 2003) tracking five flagship business desktop configurations on a standardized config (2.4 GHz P4, 256 MB DDR, 40 GB 7200 RPM HDD, CD-ROM, no monitor): Dell Optiplex GX260, Gateway E-4000 Special Deluxe, HP Compaq Evo D510 minitower (both SB and standard variants), and IBM NetVista M42 8303. Built for an A.T. Kearney consulting engagement to quantify the 7-month delta in street prices across Tier-1 vendors. Dell's price moved +$40 (+3%), Gateway +$350 (+35%), HP Compaq SB variant +$333, IBM -$20, HP standard +$196.

**Author:** Peter S. Kastner · **Date:** 2003-03-10 · **Type:** dct
**Importance:** medium — *A.T. Kearney-commissioned quantitative benchmark capturing the sharp Q4 2002 price rebound and the spread between aggressive (Dell, IBM) and price-retreating (Gateway, HP) vendors.*
**Prescience:** not-applicable — *Price-tracking benchmark; no predictive content.*

## Entities (5)

- [[at-kearney|A.T. Kearney]]
- [[dell|Dell]]
- [[gateway-inc|Gateway, Inc.]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]

## Technologies (2)

- [[ddr-sdram|DDR SDRAM (256 MB)]]
- [[intel-pentium-4|Intel Pentium 4 (2.4 GHz)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-at-kearney-business-pc-prices' ORDER BY year_observed;
```

