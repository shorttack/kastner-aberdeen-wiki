---
title: "Informix Software Overview"
slug: inforx95-3-9a45fe
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1995"
study_type: consulting-report
subject_domain: "RDBMS product portfolio; competitive positioning; Informix software architecture"
methodology: "expert-analysis; product briefing"
importance: high
importance_rationale: "Core product-portfolio briefing for Informix sales reps; provides financial metrics, product positioning, and competitive comparisons as of 1995."
relevance: medium
relevance_rationale: "Historical product/company snapshot; instructive for understanding Informix's competitive differentiation vs. Oracle and Sybase in mid-1990s RDBMS market."
prescience: high
prescience_rationale: "Correctly positioned Informix OnLine DSA as SMP performance leader; correctly forecast XPS/MPP trajectory; NewEra prediction as OO GUI tool of the future was partially accurate before Informix's 1997 crisis."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 17
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Informix Software Overview

> Aberdeen Group overview of Informix Software for sales training. Covers company profile (Top-10 ISV, fastest-growing RDBMS company), full product portfolio (SE, OnLine, Dynamic Server, XPS, specialized variants), parallel DSA technology architecture, database middleware (replication, connectivity), tools revenue ($150M of $470M in 1994, 500K+ licenses), application development tools (NewEra, 4GL, SQL Suite, CLI/ESQL), end-user access, and services. 38-slide deck used in Informix sales training.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1995 · **Type:** consulting-report
**Importance:** high — *Core product-portfolio briefing for Informix sales reps; provides financial metrics, product positioning, and competitive comparisons as of 1995.*
**Prescience:** high — *Correctly positioned Informix OnLine DSA as SMP performance leader; correctly forecast XPS/MPP trajectory; NewEra prediction as OO GUI tool of the future was partially accurate before Informix's 1997 crisis.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates]]
- [[ibm-corporation|International Business Machines Corporation]]
- [[microsoft-corporation|Microsoft Corporation]]
- [[oracle-corporation|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sybase|Sybase]]

## Technologies (17)

- [[ca-ingres|CA-Ingres (OpenIngres)]]
- [[decision-support|Decision Support / Business Intelligence]]
- [[ibm-db2|IBM DB2]]
- [[ibm-sp2|IBM SP2]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[oltp|Online Transaction Processing]]
- [[oracle-7|Oracle 7.x]]
- [[oracle-parallel-server|Oracle Parallel Server]]
- [[ordbms|Object-Relational DBMS (ORDBMS)]]
- [[rdbms|Relational Database (RDBMS)]]
- [[red-brick-rdbms|Red Brick RDBMS]]
- [[rs6000-smp|IBM RS/6000 SMP]]
- [[sybase-iq|Sybase IQ Accelerator]]
- [[sybase-powerbuilder|Sybase PowerBuilder]]
- [[sybase-sql-server|Sybase SQL Server / System 11]]
- [[tpc-c|TPC-C Benchmark]]
- [[unix|UNIX (various)]]

## Key observations (top 25)

- **1994** — informix_revenue: $469 million total 1994 corporate revenue; up 33% from 1993
- **1994** — informix_trailing_12mo_revenue: $568 million (last 12 months as of mid-1995)
- **1995** — informix_market_cap: $4.3 billion (up from $1.5B in 1994)
- **1995** — informix_stock_gain: Up 207% in last 52 weeks (as of 7/29/95)
- **1994** — informix_tools_revenue: $150M of $470M total in 1994
- **1994** — informix_licenses_sold: Over 500,000 licenses sold
- **1994** — informix_partner_tool_usage: 75% of partner applications use Informix tools
- **1994** — informix_market_rank: Third-largest RDBMS supplier
- **1994** — oracle_revenue: $2.4 billion total 1994 corporate revenue; up 40% from 1993
- **1995** — oracle_market_cap: $18.7 billion (up 100% from 1994)
- **1995** — oracle_projected_revenue: On track for $3.6+ billion in revenues in fiscal 1996
- **1994** — sybase_revenue: $826 million total 1994 corporate revenue; up 71% from 1993
- **1995** — sybase_market_cap: $2.4 billion (July 28, 1995)
- **1995** — sybase_stock_drop: 41% stock price drop -- first week April 1995
- **1994-1995** — ca_revenue: $2.74 billion; 22.2% net profit margin (best in database industry)
- **1994-1995** — ca_cs_revenue_share: Client-server now 30% of CA business; remainder mainframe
- **1995** — informix_tpc_performance: Informix-OnLine frequently highest performing midrange-server database on TPC-C benchmarks
- **1995** — informix_dsa_strengths: Infinite scalability (shared-nothing); excellent parallel SQL on SMP; high availability; full RDBMS functionality
- **1995** — informix_xps_delivery: XPS just being delivered in Q4-1995; competes with IBM DB2/6000, Oracle, Sybase plus AT&T Teradata
- **1996** — informix_xps_delivery: unknown
- **1995** — informix_secret_success: Informix is a secret success -- strong DSA architecture; advanced tools led by NewEra
- **1995** — informix_market_position: Top-10 ISV; fastest-growing independent RDBMS company; respected rival of Oracle and Sybase
- **1995** — informix_replication_gap: Informix behind in replication and will remain so; better next year
- **1995** — informix_gateway_position: DRDA client; limited gateways; IBI ties; improving APIs
- **1995** — informix_newera_assessment: NewEra only challenged by Ingres OPENROAD; best high-productivity commercial application tool

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'inforx95-3-9a45fe' ORDER BY year_observed;
```

