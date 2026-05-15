---
title: "Pilot Internet Publisher: A Foundation for Web-Enabled OLAP"
slug: pilot-internet-publisher-51e601
page_type: study
author: "Aberdeen Group"
date: "1997-02-01"
study_type: market-study
subject_domain: "business-intelligence-OLAP"
methodology: "industry-analysis,competitive-profiling,expert-opinion"
importance: high
importance_rationale: "This 1997 study is an early and detailed treatment of web-enabled OLAP architecture at a pivotal moment when enterprises were determining whether to deploy BI via browser or fat client; it captures the first-generation technical tradeoffs with specificity. Aberdeen's detailed vendor profile of a leading OLAP player in a rapidly consolidating market gives it historical significance."
relevance: medium
relevance_rationale: "The architectural tradeoffs between server-centric and client-centric BI delivery remain relevant to modern cloud BI deployments; the specific Pilot products are obsolete but the conceptual framework for thin-client analytical access translates directly to modern SaaS BI tools like Tableau Online and Power BI Service."
prescience: medium
prescience_rationale: "Aberdeen predicted Pilot would continue as a solid cost-effective OLAP choice; Pilot was sold by Cognizant in 1997 to Platinum Equity then to Accrue Software (2000) and finally acquired by SAP in 2007 — surviving but through multiple ownership changes, not as an independent leader."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 14
obs_count: 23
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Pilot Internet Publisher: A Foundation for Web-Enabled OLAP

> Aberdeen Group profiles Pilot Software's web-enabled OLAP product combining the Pilot Internet Publisher (front-end) with the Pilot Analysis Server (multidimensional back-end). The study argues that web-enabled OLAP dramatically reduces costs of deploying business intelligence to large user populations by eliminating fat-client software. Aberdeen endorses Pilot as delivering more analytical functionality than most web-based competitors while achieving Web economics.

**Author:** Aberdeen Group · **Date:** 1997-02-01 · **Type:** market-study
**Importance:** high — *This 1997 study is an early and detailed treatment of web-enabled OLAP architecture at a pivotal moment when enterprises were determining whether to deploy BI via browser or fat client; it captures the first-generation technical tradeoffs with specificity. Aberdeen's detailed vendor profile of a lea…*
**Prescience:** medium — *Aberdeen predicted Pilot would continue as a solid cost-effective OLAP choice; Pilot was sold by Cognizant in 1997 to Platinum Equity then to Accrue Software (2000) and finally acquired by SAP in 2007 — surviving but through multiple ownership changes, not as an independent leader.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[blue-isle-software|Blue Isle Software]]
- [[cognizant-corporation|Cognizant Corporation]]
- [[dun-bradstreet|Dun & Bradstreet Corporation]]
- [[pilot-software|Pilot Software Inc.]]

## Technologies (14)

- [[activex|ActiveX]]
- [[db2|IBM DB2]]
- [[html|HTML (Hypertext Markup Language)]]
- [[java|Java]]
- [[javascript|JavaScript]]
- [[microsoft-iis|Microsoft Internet Information Server (IIS)]]
- [[microsoft-isapi|Microsoft ISAPI]]
- [[olap|Online Analytical Processing (OLAP)]]
- [[oracle-db|Oracle Database]]
- [[pilot-analysis-server|Pilot Analysis Server]]
- [[pilot-decision-support-suite|Pilot Decision Support Suite]]
- [[pilot-internet-publisher|Pilot Internet Publisher]]
- [[sybase|Sybase SQL Server]]
- [[windows-nt|Windows NT Server]]

## Key observations (top 25)

- **1997** — Web-OLAP architecture model: Multi-tiered server-centric architecture: browser -> Web Server -> Pilot Internet Publisher -> Pilot Analysis Server -> MDB
- **1997** — CGI avoidance strategy: Pilot rejected standard CGI in favor of Microsoft ISAPI for faster and more secure query responses
- **1997** — UNIX platform support: AT&T UNIX SVR4, Digital UNIX, HP UX, IBM AIX, Sequent DYNIX, Sun Solaris
- **1997** — Database connectivity: Native connections to Oracle and Sybase; ODBC to SQL Server / Informix / IBM DB2
- **1997** — Pilot Internet Publisher pricing: $10000 per Windows NT Server plus $695/user
- **1997** — Pilot Analysis Server pricing: $20000 per Windows NT Server or $30000 per UNIX server
- **1997** — Pilot Software employee count: 350 employees worldwide
- **1997** — Cognizant Corporation annual revenue: $1.5 billion
- **1997** — Web-OLAP cost savings drivers: Three areas: reduced maintenance/installation; cost avoidance (no fat-client); desktop platform independence
- **1997** — Product portfolio strategy: Comprehensive suite: Internet Publisher + Analysis Server + Discovery Server (data mining) + Desktop + Designer + Sales & Marketing Library + Excel Add-In
- **1997** — Vertical market focus: Specifically tuned for retail and financial services — promotional effectiveness and risk management
- **1997** — User interaction model: Stateless model enabling advanced browser features: move/resize/tile windows and bookmarking
- **1997** — Personal cube capability: Distribution of personal cubes (exported MDB subsets) via email as compressed self-extracting files for offline analysis
- **1997** — Analysis functions delivered: Exceptions analysis (color-coded); Ranking analysis (ascending/descending); 80/20 analysis (Pareto segmentation) — all as source code modules
- **1997** — Pilot market position prediction: Aberdeen predicts Pilot will continue to offer a solid cost-effective choice for distributed OLAP through upcoming months and years
- **1997** — Web-OLAP adoption prediction: Web-driven functionality will extend OLAP to more users than enterprises have been able to cost-justify in the past
- **2007** — Pilot Software acquisition: Pilot Software acquired by SAP AG in February 2007; product rebranded SAP Strategy Management
- **1999** — Web-OLAP market outcome: Microsoft OLAP Services (1999) and later SQL Server Analysis Services became dominant web-OLAP platform; Pilot's web-OLAP approach was commercially validated but market consolidated to Microsoft/Oracle/IBM
- **1997** — Java/ActiveX evolution plan: Pilot planned mid-1997 delivery of advanced Selector Object using Java and ActiveX for hierarchical dimension navigation
- **1997** — Cognizant Corporation focus: Integrates information and technology to create business insight; focuses on healthcare / media / high-tech growth markets
- **1997** — Aberdeen overall recommendation: For enterprises needing to support large populations with multidimensional data access, combination of Pilot Internet Publisher and Pilot Analysis Server delivers complete Web-enabled OLAP solution
- **1997** — MDB architecture factor: Multidimensional Database (MDB) organizes data in typical business terms: revenues/costs/gross margins vs. customers/products/regions/time
- **1997** — Web-OLAP cost avoidance factor: Adding new user requires only browser and network access — not fat-client software installation — enabling large-population deployment cost-justification

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'pilot-internet-publisher-51e601' ORDER BY year_observed;
```

