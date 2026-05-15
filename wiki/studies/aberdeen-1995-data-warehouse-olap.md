---
title: "Data Warehouse Query Tools: Evolving to Relational OLAP"
slug: aberdeen-1995-data-warehouse-olap
page_type: study
author: "Aberdeen Group"
date: "1995-07-01"
study_type: market-study
subject_domain: "data-warehousing-OLAP"
methodology: "industry-analysis,competitive-profiling,benchmarking"
importance: high
importance_rationale: "Defined the ROLAP category and distinguished it from MOLAP/report writers at a pivotal market moment; Aberdeen's ROLAP framework directly influenced enterprise BI purchasing decisions worth hundreds of millions. MicroStrategy and Informix partnership specifically endorsed."
relevance: medium
relevance_rationale: "ROLAP vs MOLAP distinction is now historical (modern BI tools like Snowflake/BigQuery/Power BI use hybrid approaches); the analytical framework for evaluating multi-tier data warehouse architectures transfers well."
prescience: high
prescience_rationale: "Core predictions confirmed: ROLAP wave materialized by 1997-1999, MDB vendors faced consolidation pressure, RDBMS vendors integrated OLAP capabilities as forecast. Aberdeen correctly identified the winning architecture."
license: CC-BY-4.0
tier: 1
entity_count: 20
tech_count: 28
obs_count: 54
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Data Warehouse Query Tools: Evolving to Relational OLAP

> Aberdeen Group market viewpoint analyzing the evolution of data warehouse query tools toward relational OLAP (ROLAP), examining multidimensional analysis, vendor strategies, and convergence of OLAP and relational database technologies.

**Author:** Aberdeen Group · **Date:** 1995-07-01 · **Type:** market-study
**Importance:** high — *Defined the ROLAP category and distinguished it from MOLAP/report writers at a pivotal market moment; Aberdeen's ROLAP framework directly influenced enterprise BI purchasing decisions worth hundreds of millions. MicroStrategy and Informix partnership specifically endorsed.*
**Prescience:** high — *Core predictions confirmed: ROLAP wave materialized by 1997-1999, MDB vendors faced consolidation pressure, RDBMS vendors integrated OLAP capabilities as forecast. Aberdeen correctly identified the winning architecture.*

## Entities (20)

- [[ent-01|Aberdeen Group]]
- [[ent-02|MicroStrategy Inc.]]
- [[ent-03|Information Advantage Inc.]]
- [[ent-04|Stanford Technology Group]]
- [[ent-05|Arbor Software]]
- [[ent-06|Oracle Corporation]]
- [[ent-07|IRI Software]]
- [[ent-08|D&B Software]]
- [[ent-09|Pilot Software Inc.]]
- [[ent-10|Holistic Systems Inc.]]
- [[ent-11|Andyne Computing Ltd.]]
- [[ent-12|Business Objects]]
- [[ent-13|Cognos Corp.]]
- [[ent-14|IQ Software]]
- [[ent-15|Informix]]
- [[ent-16|Sybase]]
- [[ent-17|Microsoft]]
- [[ent-18|Crystal Services]]
- [[ent-19|Hewlett-Packard]]
- [[ent-20|Lotus Development]]

## Technologies (28)

- [[tech-01|Relational OLAP (ROLAP)]]
- [[tech-02|Multidimensional OLAP (MOLAP)]]
- [[tech-03|Multidimensional Database (MDB)]]
- [[tech-04|Sparse-matrix technology]]
- [[tech-05|Parallel-scalable RDBMS]]
- [[tech-06|Dimensional modeling]]
- [[tech-07|ODBC (Open Database Connectivity)]]
- [[tech-08|SQL (Structured Query Language)]]
- [[tech-09|Metadata repository / data dictionary]]
- [[tech-10|Denormalization]]
- [[tech-11|Summarization / pre-aggregation]]
- [[tech-12|Partitioning]]
- [[tech-13|Multi-pass SQL generation]]
- [[tech-14|Fat-client architecture]]
- [[tech-15|Data warehousing]]
- [[tech-16|Essbase (Arbor Software)]]
- [[tech-17|Holos (Holistic Systems)]]
- [[tech-18|Oracle Express (IRI Software)]]
- [[tech-19|Pablo (Andyne Computing)]]
- [[tech-20|BusinessObjects]]
- [[tech-21|Cognos Impromptu]]
- [[tech-22|Crystal Reports]]
- [[tech-23|Microsoft Access]]
- [[tech-24|Microsoft Excel]]
- [[tech-25|Lotus Approach]]
- [[tech-26|Intelligent agents / alerts]]
- [[tech-27|Data mining]]
- [[tech-28|Very Large Databases (VLDB)]]

## Key observations (top 25)

- **1995** — query-tool-categories: 3 categories: report writer/predefined; multidimensional OLAP; Relational OLAP
- **1995** — data-warehouse-scale: terabyte-size warehouses emerging
- **1995** — mdb-practical-size-limit: 20-50 GB
- **1995** — vldb-site-count: hundreds of sites exceeding 100GB
- **1995** — mdb-50gb-barrier: ~50 GB ceiling for MDB technology
- **1995** — relational-db-vldb-sites: 1000+ customer sites with VLDBs
- **1995** — tool-classification: high-end report writer
- **1995** — tool-classification: high-end report writer
- **1995** — fat-client-weakness: fails on thousands-of-rows margin analysis
- **1995** — report-writer-limitations: 7 identified weaknesses
- **1995** — report-writer-future: relegated to light-query status
- **1995** — molap-vertical-strength: consumer packaged goods market
- **1995** — tool-type: client-side MDB handling few megabytes
- **1995** — tool-type: server-based MDB
- **1995** — tool-type: server-based MDB
- **1995** — tool-type: server-based MDB with sparse-matrix
- **1995** — tool-type: server-based MDB with sparse-matrix
- **1995** — partnership-type: alliance with Hewlett-Packard
- **1995** — acquisition-type: Oracle acquiring IRI Software for MDB and query tools
- **1995** — mdb-market-role: major but non-mainstream path for 3-year horizon
- **1995** — rolap-competitive-impact: datamarts in 3 years
- **1995** — rolap-pioneer-status: leading ROLAP pioneer
- **1995** — rolap-pioneer-status: key ROLAP supplier
- **1995** — rolap-pioneer-status: key ROLAP supplier
- **1995** — partnership-type: ROLAP partnership with MicroStrategy

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-data-warehouse-olap' ORDER BY year_observed;
```

