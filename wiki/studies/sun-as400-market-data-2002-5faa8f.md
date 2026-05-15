---
title: "Sun AS/400 RAMP Supporting Data: IBM Revenue, iSeries Pricing Benchmarks, Installed Base, and US Business Size Statistics"
slug: sun-as400-market-data-2002-5faa8f
page_type: study
author: "Peter Kastner"
date: "2002-04-20"
study_type: benchmark
subject_domain: "server-market-data"
methodology: "market-sizing, benchmarking, document-review"
importance: high
importance_rationale: "Defining quantitative foundation for the Sun AS/400 RAMP; model-level pricing and benchmarks rare in the archival record."
relevance: medium
relevance_rationale: "2002-vintage data; analytical frameworks (platform-share, addressable-market yield factor, segment-CAGR) remain reusable templates."
prescience: medium
prescience_rationale: "Addressable-market sizing ($1.87B) was the central prediction; refuted in subsequent Sun execution but framework was sound."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 13
obs_count: 45
tags: [type/study, importance/high, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Sun AS/400 RAMP Supporting Data: IBM Revenue, iSeries Pricing Benchmarks, Installed Base, and US Business Size Statistics

> Consolidated analytical dataset backing the Sun AS/400 RAMP engagement. Includes: (a) IBM 2002 hardware financials — $33.4B revenue, $24.1B cost, $9.3B gross profit, 27.7% GM; platform revenue breakdown (zSeries $8.35B, iSeries $7.68B, pSeries $5.01B, xSeries $5.01B); iSeries model-to-Sun-equivalent mapping (250→Ultra 10, 270→220R, 820→V880, 830→4800, 840→6800); regional iSeries revenue breakdowns; enterprise app category CAGRs 2001-2005 (CRM 22%, EAS 12%, SCM 23%, B2B 26%); and Aberdeen's addressable-market decomposition ($1.87B total). (b) Detailed iSeries pricing benchmarks (181-row Appendix C) with TPM-C, SAP SD, and Notes benchmark estimates for each SKU. (c) World IT spending forecast 1999-2005 by region. (d) U.S. Business Statistics 1999 by firm size for IBM customer-size modeling.

**Author:** Peter Kastner · **Date:** 2002-04-20 · **Type:** benchmark
**Importance:** high — *Defining quantitative foundation for the Sun AS/400 RAMP; model-level pricing and benchmarks rare in the archival record.*
**Prescience:** medium — *Addressable-market sizing ($1.87B) was the central prediction; refuted in subsequent Sun execution but framework was sound.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[ibm|IBM]]
- [[peter-kastner|Peter Kastner]]
- [[sun-microsystems|Sun Microsystems]]
- [[us-census-bureau|U.S. Census Bureau]]

## Technologies (13)

- [[ibm-pseries|IBM pSeries]]
- [[ibm-xseries|IBM xSeries]]
- [[ibm-zseries|IBM zSeries]]
- [[iseries|IBM iSeries]]
- [[notes-benchmark|Notes Benchmark]]
- [[sap-sd|SAP SD Benchmark]]
- [[sparc|SPARC]]
- [[sun-220r|Sun Enterprise 220R]]
- [[sun-fire-4800|Sun Fire 4800]]
- [[sun-fire-6800|Sun Fire 6800]]
- [[sun-ultra-10|Sun Ultra 10]]
- [[sun-v880|Sun Fire V880]]
- [[tpm-c|TPC-C Benchmark]]

## Key observations (top 25)

- **2001** — hw-revenue: $33.392B
- **2001** — hw-cost: $24.137B
- **2001** — gross-profit: $9.255B
- **2001** — gross-margin: 27.7%
- **2000** — hw-revenue: $37.777B
- **1999** — hw-revenue: $37.888B
- **1998** — hw-revenue: $36.096B
- **2002** — hw-revenue-q2: $6.700B
- **2001** — platform-revenue: $8.348B
- **2001** — platform-revenue: $7.680B
- **2001** — platform-revenue: $5.009B
- **2001** — platform-revenue: $5.009B
- **2002** — platform-growth: -19%
- **2002** — platform-growth: -26%
- **2002** — platform-growth: -27%
- **2002** — platform-growth: +13%
- **2002** — iseries-equivalent: iSeries 250 (1-way, $9-14K base, $250M revenue) ↔ Sun Ultra 10
- **2002** — iseries-equivalent: iSeries 270 (1-2 way, $12-33K base, $3.5B revenue) ↔ Sun 220R
- **2002** — iseries-equivalent: iSeries 820 (1-4 way, $64-267K, $2.5B revenue) ↔ Sun V880
- **2002** — iseries-equivalent: iSeries 830 (1-8 way, $145-580K, $2.018B revenue) ↔ Sun Fire 4800
- **2002** — iseries-equivalent: iSeries 840 (1-24 way, $860-1,555K, $2.0B revenue) ↔ Sun Fire 6800
- **2001** — iseries-total: $10.268B
- **2001** — iseries-na: $3.962B (38%)
- **2001** — iseries-emea: $4.007B (39%)
- **2001** — iseries-apac: $2.299B (22%)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sun-as400-market-data-2002-5faa8f' ORDER BY year_observed;
```

