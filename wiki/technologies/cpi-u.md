---
title: "CPI-U (Consumer Price Index for All Urban Consumers)"
slug: cpi-u
page_type: technology
category: "framework"
vendor: "BLS"
era: "1913-present"
lifecycle_at_study: "mature"
lifecycle_current: "mature"
study_count: 1
tier: 2
tags: [type/technology, pass-a-v2, category/framework, vendor/BLS, lifecycle/mature]
source_csv: known_technologies.csv
pass_a_v2_added: true
---

# CPI-U (Consumer Price Index for All Urban Consumers)

> Inflation index; 332.407 in April 2026

**Category:** framework · **Vendor:** BLS · **Era:** 1913-present · **Lifecycle now:** mature

## Appears in 1 studies

- [[2026-kastner-prescience-methodology-demo-0cdf48]]

## DuckDB query

```sql
SELECT * FROM observations WHERE tech_id = 'cpi-u' ORDER BY year_observed;
```
