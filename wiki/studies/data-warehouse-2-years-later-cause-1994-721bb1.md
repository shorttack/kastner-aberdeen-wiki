---
title: "The Data Warehouse: 2 Years Later... Lessons Learned"
slug: data-warehouse-2-years-later-cause-1994-721bb1
page_type: study
author: "John D. Porter and John J. Rome, Arizona State University"
date: "1994-12-01"
study_type: conference-paper
subject_domain: "higher-education-data-warehousing"
methodology: "case-study, lessons-learned-retrospective"
importance: high
importance_rationale: "Landmark early-1990s case study documenting client-server data-warehouse implementation in higher education — a foundational reference for the BI/analytics industry's 1995-2005 boom. ASU's warehouse was among the earliest university-wide integrated warehouses."
relevance: medium
relevance_rationale: "Lessons on data governance, data definition, and cross-functional marketing of analytics initiatives remain relevant to modern data-lake/lakehouse and self-service BI projects; specific technology choices (client-server 1994) are dated."
prescience: high
prescience_rationale: "Kastner's 'All companies will build a data warehouse in the next five years' prediction (ca. 1994) was substantially correct — by 1999 data warehousing was mainstream across the Fortune 1000, Teradata/Oracle/IBM DB2 warehouse deployments exploded 1995-2000, and by 2005 warehouses were ubiquitous in enterprises. The prediction has since extended through data lakes, lakehouses, and cloud warehouses (Snowflake, BigQuery, Redshift) — now 'every company' builds analytical data platforms."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 2
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# The Data Warehouse: 2 Years Later... Lessons Learned

> CAUSE 1994 Annual Conference paper (Orlando FL, Nov 29 - Dec 2 1994) by John D. Porter and John J. Rome of Arizona State University, retrospectively analyzing ASU's two-year-old integrated data warehouse project. The warehouse combined student, financial, and HR data — one of the first major client-server data warehouses in US higher education. Lessons-learned sections cover learning new technologies, understanding warehousing concepts, integrating data, designing the warehouse, marketing the idea, finding resources, 'officialness' of data, data administration impact, and data definition. Notable Kastner citation (Aberdeen Group): 'All companies will build [a data warehouse] in the next five years.' — an aggressive 1994 prediction about universal enterprise data-warehouse adoption.

**Author:** John D. Porter and John J. Rome, Arizona State University · **Date:** 1994-12-01 · **Type:** conference-paper
**Importance:** high — *Landmark early-1990s case study documenting client-server data-warehouse implementation in higher education — a foundational reference for the BI/analytics industry's 1995-2005 boom. ASU's warehouse was among the earliest university-wide integrated warehouses.*
**Prescience:** high — *Kastner's 'All companies will build a data warehouse in the next five years' prediction (ca. 1994) was substantially correct — by 1999 data warehousing was mainstream across the Fortune 1000, Teradata/Oracle/IBM DB2 warehouse deployments exploded 1995-2000, and by 2005 warehouses were ubiquitous in…*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[arizona-state-university|Arizona State University]]
- [[cause-organization|CAUSE (the association for managing and using information resources in higher education)]]
- [[educause|EDUCAUSE]]
- [[john-d-porter-asu|John D. Porter]]
- [[john-j-rome-asu|John J. Rome]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (2)

- [[client-server-computing|Client-Server Computing]]
- [[data-warehouse|Data Warehouse]]

## Key observations (top 25)

- **1994** — All companies will build a data warehouse within 5 years: All companies will build [a data warehouse] in the next five years.
- **1994** — The question is when to build, not whether: The question for corporations and higher education is not simply whether to build a warehouse, but when.
- **1992** — ASU warehouse project inception: Two years ago, ASU initiated a project that brought together student, financial and human resources data in an integrated data warehouse.
- **1994** — Data warehouse often first client-server application: A data warehouse is often the first client/server application that institutions attempt.
- **1999** — Universal data-warehouse adoption by 1999: All companies will build [a data warehouse] in the next five years = universal adoption by 1999
- **2000** — Data warehousing became mainstream 1995-2000: By 2000, enterprise data warehouses were standard across Fortune 1000; Teradata, Oracle, IBM DB2, Sybase IQ, Red Brick all had large installed bases; warehouse industry revenue exceeded $5B annually by 1999
- **2020** — Cloud data warehouses dominate 2020s: Snowflake IPO (2020) at $70B+; Google BigQuery, Amazon Redshift, Databricks lakehouse all multi-billion-dollar platforms by 2024; 'every company' runs data warehouses
- **1998** — CAUSE merged into EDUCAUSE: CAUSE merged with Educom on 1998-07-01 to form EDUCAUSE; represents consolidation of higher-ed IT professional associations

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'data-warehouse-2-years-later-cause-1994-721bb1' ORDER BY year_observed;
```

