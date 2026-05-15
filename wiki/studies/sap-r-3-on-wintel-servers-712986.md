---
title: "SAP R/3 on Wintel Servers: To NT or Not to NT...That is the Question"
slug: sap-r-3-on-wintel-servers-712986
page_type: study
author: "Aberdeen Group"
date: "1997-03-01"
study_type: benchmark
subject_domain: "enterprise-resource-planning-ERP"
methodology: "benchmarking, industry-analysis"
importance: high
importance_rationale: "This study is one of the earliest independent analyst assessments of SAP R/3 running on Windows NT hardware — a pivotal market event; Aberdeen's endorsement of Wintel for mid-range SAP helped legitimize the platform shift that reshaped the enterprise software hardware market through the late 1990s."
relevance: medium
relevance_rationale: "The SAP benchmarking methodology discussion (SAPS metric, three-tier architecture, benchmark limitations) remains pedagogically relevant to ERP capacity planning; specific NT/Pentium Pro benchmark numbers are dated but the analytical framework for evaluating ERP platform choice transfers to modern cloud/on-premise tradeoffs."
prescience: high
prescience_rationale: "Aberdeen predicted NT would challenge Unix at all performance levels within 12-18 months — by 1999-2000 Windows NT/2000 became the dominant SAP platform for mid-range customers; Oracle remained performance leader but SQL Server closed the gap as predicted; the mid-range Wintel ERP market grew as forecast."
license: CC-BY-4.0
tier: 1
entity_count: 13
tech_count: 10
obs_count: 23
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# SAP R/3 on Wintel Servers: To NT or Not to NT...That is the Question

> Aberdeen Group analyzes SAP R/3 Standard Application Benchmark results on Windows NT / Intel (Wintel) servers, comparing performance and price-performance against Unix alternatives. The study reviews three SAP-certified SD benchmarks from Data General and Hewlett Packard (900+ concurrent users; 4,717 SAPS peak), assesses NT's readiness for mid-range enterprise deployments of 250-500 concurrent users, and predicts that NT will challenge Unix at all performance levels within 12-18 months. Aberdeen recommends organizations with up to 500 concurrent users consider Wintel deployments while cautioning that SQL Server lags Oracle by less than 20% for mid-range use cases.

**Author:** Aberdeen Group · **Date:** 1997-03-01 · **Type:** benchmark
**Importance:** high — *This study is one of the earliest independent analyst assessments of SAP R/3 running on Windows NT hardware — a pivotal market event; Aberdeen's endorsement of Wintel for mid-range SAP helped legitimize the platform shift that reshaped the enterprise software hardware market through the late 1990s.*
**Prescience:** high — *Aberdeen predicted NT would challenge Unix at all performance levels within 12-18 months — by 1999-2000 Windows NT/2000 became the dominant SAP platform for mid-range customers; Oracle remained performance leader but SQL Server closed the gap as predicted; the mid-range Wintel ERP market grew as for…*

## Entities (13)

- [[aberdeen-group|Aberdeen Group]]
- [[baan|Baan Company]]
- [[data-general|Data General Corporation]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[intel|Intel Corporation]]
- [[jba-international|JBA International]]
- [[jd-edwards|J.D. Edwards & Company]]
- [[microsoft|Microsoft Corporation]]
- [[oracle|Oracle Corporation]]
- [[peoplesoft|PeopleSoft Inc.]]
- [[sap-ag|SAP AG]]
- [[ssa-gt|SSA GT (System Software Associates)]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (10)

- [[adabas|ADABAS]]
- [[data-general-avion-4900|Data General Avion 4900]]
- [[hp-netserver-lx-pro|HP NetServer LX Pro]]
- [[intel-pentium-pro|Intel Pentium Pro 200MHz]]
- [[ms-sql-server-65|Microsoft SQL Server 6.5]]
- [[oracle7|Oracle7 RDBMS]]
- [[sap-r3|SAP R/3]]
- [[sun-ultrae6000|Sun UltraEnterprise 6000]]
- [[tpc-c|TPC-C Benchmark]]
- [[windows-nt|Windows NT]]

## Key observations (top 25)

- **1996** — SAP SD benchmark — HP NetServer LX Pro / Oracle7 (May 1996): 900 users; 4,544 SAPS; 272,667 dialogue steps/hour; WinNT 3.51; 2,048 MB RAM
- **1996** — SAP SD benchmark — HP NetServer LX Pro / SQL Server 6.5 (August 1996): 774 users; 3,900 SAPS; 234,000 dialogue steps/hour; WinNT 4.0; 2,048 MB RAM
- **1996** — SAP SD benchmark — Data General Avion 4900 / Oracle7 (November 1996): 936 users; 4,717 SAPS; 283,000 dialogue steps/hour; WinNT 3.51; 512 MB RAM
- **1997** — SAP SD benchmark champion — Sun UltraEnterprise 6000 (Unix): 1,800 users; 20-way UltraSPARC 167MHz SMP; 5,632 MB RAM; Oracle7; 9x8-way application servers
- **1997** — SAP R/3 NT installed base: >2,000 SAP systems installed in NT environments as of Q1 1997
- **1996** — Percentage of new R/3 licenses on NT in Q4 1996: 40% of all new R/3 licenses shipped in Q4 1996 were NT
- **1997** — SAP SD benchmark SAPS definition: 100 SAPS = 2000 order line items fully processed per hour = 6000 dialogue steps + 2400 SAP transactions
- **1997** — Wintel vs Unix price-performance ratio (TPC-C): Wintel with SQL Server: 35-50% of Unix absolute throughput at 1/4 to 1/10 the cost
- **1997** — SQL Server vs Oracle7 performance gap for R/3 NT: SQL Server v6.5 achieves within 20% of Oracle7 performance in SAP SD benchmark
- **1997** — NT capability trajectory prediction: NT will challenge Unix at all performance levels within next 12-18 months (i.e., by late 1998 / early 1999)
- **1999** — NT (Windows 2000) vs Unix for SAP ERP outcome: Windows 2000 Server became dominant SAP mid-range platform by 2000; NT/Wintel dominated mid-range ERP market as predicted
- **1997** — NT for mid-range R/3 readiness assessment: NT suitable for organizations with up to 250-500 concurrent users per data server as of Q1 1997
- **1997** — Oracle7 vs SQL Server for R/3 NT: Oracle7 current performance leader for R/3-for-NT; SQL Server rapidly narrowing gap
- **1997** — SAP Benchmark Council certifications at time of publication: 27+ Standard Application Benchmarks certified; 6 Wintel; 30+ total by publication
- **1997** — SAP benchmark limitation: OLTP-only: SAP SD benchmarks reflect only OLTP; real world mixes OLTP/reporting/DSS
- **1997** — SAP benchmark limitation: single application: Benchmarks test single R/3 module (SD); real world runs multiple concurrent modules
- **1997** — SAP benchmark limitation: no site-specific customization: Application customization and user behavior create significant real-world variance
- **1997** — SAP competitive strategy for mid-range: Goliath moving down the food chain; premium product — both functionally and price-wise — entering mid-range market
- **1997** — J.D. Edwards strategic vulnerability: Slow to make no-holds-barred commitment to NT; AS/400 roots create competitive risk
- **1997** — Aberdeen overall R/3 on NT verdict: Wintel confirmed as viable enterprise platform for mid-range SAP; organizations should evaluate for deployments under 500 users
- **1997** — SAP SD benchmark response time standard: <2 second average response time standard for all published SAP benchmarks
- **1997** — SQL Server mid-range viability prediction: Microsoft SQL Server has gained sufficient scalability into mid-range; viable alternative for many medium-sized R/3 NT implementations
- **2000** — Microsoft SQL Server market position for SAP: SQL Server became leading database for SAP NT deployments by 2000; closed performance gap as predicted

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sap-r-3-on-wintel-servers-712986' ORDER BY year_observed;
```

