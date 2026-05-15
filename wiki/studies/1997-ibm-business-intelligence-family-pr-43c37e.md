---
title: "IBM Business Intelligence Family"
slug: 1997-ibm-business-intelligence-family-pr-43c37e
page_type: study
author: "Aberdeen Group"
date: "1997-06-04"
study_type: product-profile
subject_domain: "Business Intelligence / Data Warehousing"
methodology: "vendor-briefing,product-analysis,market-assessment"
importance: medium
importance_rationale: "This profile documents IBM's BI strategy during the critical transition from centralized data warehousing to distributed/departmental data marts and early web-enabled analytics. The Intelligent Decision Server evolved from Metaphor DIS — a historically significant product. IBM's BI strategy eventually led to the Cognos acquisition (2007); Intelligent Miner presaged modern machine learning tooling. This is a key archival document of the 1990s data warehousing era."
relevance: medium
relevance_rationale: "Highly relevant to the history of business intelligence and data warehousing. Concepts including data marts vs enterprise warehouses, OLAP drill-down, and data mining described here are foundations of modern BI. IBM's eventual path (acquiring Cognos 2007) and the rise of self-service BI tools validate many Aberdeen observations."
prescience: medium
prescience_rationale: "Aberdeen correctly predicted that data warehousing would expand from corporate specialists to line-of-business/remote users ('to the masses') — this describes the entire trajectory of BI from 1997 to 2020s (self-service BI, Tableau, Power BI, etc.). Aberdeen correctly identified data mining as a key growth area. The prediction of network-computing enabling broader decision support proved accurate. However, Aberdeen did not anticipate SaaS-delivered BI or the rise of columnar databases (Redshift,…"
license: CC-BY-4.0
tier: 2
entity_count: 5
tech_count: 10
obs_count: 24
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# IBM Business Intelligence Family

> Aberdeen Group profiles IBM's Business Intelligence Family — a suite spanning Information Warehouse (enterprise data warehouse), Visual Warehouse (data marts), Intelligent Decision Server (OLAP), and Intelligent Miner (data mining), all built on DB2 and Internet-enabled via Net.data. The profile evaluates IBM's strategy to expand decision support from corporate data analysts to line-of-business users and remote locations via network computing. Aberdeen concludes the BI Family differentiates through breadth, advanced OLAP, and network-computing integration.

**Author:** Aberdeen Group · **Date:** 1997-06-04 · **Type:** product-profile
**Importance:** medium — *This profile documents IBM's BI strategy during the critical transition from centralized data warehousing to distributed/departmental data marts and early web-enabled analytics. The Intelligent Decision Server evolved from Metaphor DIS — a historically significant product. IBM's BI strategy eventual…*
**Prescience:** medium — *Aberdeen correctly predicted that data warehousing would expand from corporate specialists to line-of-business/remote users ('to the masses') — this describes the entire trajectory of BI from 1997 to 2020s (self-service BI, Tableau, Power BI, etc.). Aberdeen correctly identified data mining as a key…*

## Entities (5)

- [[e5-01|IBM]]
- [[e5-02|Metaphor Computer Systems]]
- [[e5-03|Cognos Inc.]]
- [[e5-04|Aberdeen Group]]
- [[e5-05|Lotus Development Corporation]]

## Technologies (10)

- [[t5-01|IBM Information Warehouse]]
- [[t5-02|IBM Visual Warehouse]]
- [[t5-03|IBM Intelligent Decision Server (IDS)]]
- [[t5-04|IBM Intelligent Miner]]
- [[t5-05|IBM DataPropagator]]
- [[t5-06|IBM DataJoiner]]
- [[t5-07|IBM Net.data]]
- [[t5-08|IBM DB2]]
- [[t5-09|IBM DataGuide]]
- [[t5-10|IBM Tivoli Management Environment (TME)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-ibm-business-intelligence-family-pr-43c37e' ORDER BY year_observed;
```

