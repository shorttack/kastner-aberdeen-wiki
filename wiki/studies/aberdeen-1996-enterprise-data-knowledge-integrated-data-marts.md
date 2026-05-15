---
title: "True Enterprise Data Knowledge Through Integrated Data Marts"
slug: aberdeen-1996-enterprise-data-knowledge-integrated-data-marts
page_type: study
author: "Aberdeen Group"
date: "1996-09-23"
study_type: market-study
subject_domain: "data-warehousing"
methodology: "industry-analysis, field-research, expert-opinion, document-review"
importance: high
importance_rationale: "Published at the peak of the first data mart boom (1996), this study directly addressed the fragmentation problem that would plague enterprises for years; Aberdeen's 'integrated data marts' framework anticipated the hub-and-spoke architecture that became the dominant enterprise BI pattern through the 2000s."
relevance: high
relevance_rationale: "The core problem—siloed data marts with contradictory business rules—remains acute in modern data lake and lakehouse architectures; Aberdeen's insistence on common metrics and enterprise-wide governance directly maps to current data mesh and data catalog debates."
prescience: high
prescience_rationale: "Aberdeen's prediction that uncontrolled data mart proliferation would prove 'disastrous' without enterprise governance proved correct—the 'data swamp' problem of the 2010s echoes exactly this warning; the integrated/federated warehouse architecture Aberdeen advocated became the dominant enterprise data strategy."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 6
obs_count: 25
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# True Enterprise Data Knowledge Through Integrated Data Marts

> Aberdeen Group argues that the proliferation of standalone departmental data marts—while individually successful—creates enterprise fragmentation, contradictory business rules, and ROI erosion. The study presents an iterative 'integrated data marts' architecture: building subject-specific data marts that feed a common RDBMS-based enterprise warehouse, using high-level industry templates and synchronization methodologies to deliver both business-unit autonomy and enterprise data integrity.

**Author:** Aberdeen Group · **Date:** 1996-09-23 · **Type:** market-study
**Importance:** high — *Published at the peak of the first data mart boom (1996), this study directly addressed the fragmentation problem that would plague enterprises for years; Aberdeen's 'integrated data marts' framework anticipated the hub-and-spoke architecture that became the dominant enterprise BI pattern through th…*
**Prescience:** high — *Aberdeen's prediction that uncontrolled data mart proliferation would prove 'disastrous' without enterprise governance proved correct—the 'data swamp' problem of the 2010s echoes exactly this warning; the integrated/federated warehouse architecture Aberdeen advocated became the dominant enterprise d…*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[ncr-corporation|NCR Corporation]]
- [[oracle|Oracle Corporation]]
- [[prism-solutions|Prism Solutions]]
- [[red-brick-systems|Red Brick Systems]]
- [[sybase|Sybase Inc.]]
- [[tandem-computers|Tandem Computers Inc.]]

## Technologies (6)

- [[data-mart|Data Mart]]
- [[data-warehouse|Enterprise Data Warehouse]]
- [[etl|Extract Transform Load (ETL)]]
- [[multidimensional-db|Multidimensional Database (MDDB)]]
- [[rapid-application-development|Rapid Application Deployment (RAD)]]
- [[rdbms|Relational Database Management System (RDBMS)]]

## Key observations (top 25)

- **1996** — Data mart fragmentation problem prevalence: Aberdeen field experience: enterprises that build uncontrolled standalone data marts end up with contradictory business rules and enterprise-crippling data requests
- **1996** — Revenue definition inconsistency: Most enterprises have one or more inconsistent definitions for basic enterprise expression 'revenue' across systems
- **1996** — Framework: single-subject starting point: Begin with one data mart addressing a single subject area that links into an RDBMS-driven enterprise whole
- **1996** — Framework: common metrics foundation: Enterprise must work from high-level model and common business metrics before building individual data marts
- **1996** — Framework: iterative road map: Use iterative method of building a road map for the enterprise to follow; each data mart funds the next
- **1996** — Framework: user involvement: Involve end users throughout design; data marts must reflect business drivers embedded in end-user behavior
- **1996** — Framework: synchronization management: Managing synchronization across data marts is critical; requires disciplined ETL and common data stewardship
- **1996** — Framework: rapid application deployment: Use Rapid Application Deployment to maintain business momentum; demonstrate ROI early to secure continued funding
- **1996** — NCR/Tandem/Prism positioning: NCR, Tandem, and Prism Solutions positioned as providers of industry-specific data warehouse templates and short-term consulting engagements
- **1996** — RDBMS vs multidimensional DB strategic choice: Aberdeen advocates RDBMS-based architecture over proprietary multidimensional databases for enterprise data marts; RDBMS provides flexibility and integration path
- **1996** — Standalone data mart maturity assessment: Standalone data marts: frequently commandeered by business units; adequately answer short-term objectives but prove shortsighted; risk of contradictory business rules
- **1996** — Enterprise-wide data warehouse: top-down failure mode: Early attempts at monolithic enterprise-wide warehouses failed due to rapidly changing business dynamics toppling top-down models
- **1996** — RDBMS suitability for enterprise data warehouse: RDBMS-driven technology is the preferred foundation; parallel-scalable hardware and RDBMS combine to create enterprise-capable warehouse platform
- **1996** — Fragmentation risk assessment: Enterprise policy of encouraged fragmentation could be disastrous for the business; competitive disadvantage from incompatible data marts
- **1996** — ROI self-funding model: Enterprises that followed integrated model begin generating ROI that underwrites subsequent data mart efforts; project-by-project experience creates compounding value
- **1996** — Business driver embedding requirement: IS executives must build data access systems that reflect business drivers embedded in end-user behavior; IT-driven warehouses miss this requirement
- **1996** — Integrated data marts as dominant BI architecture: Aberdeen predicts integrated data mart approach (subject-by-subject building toward enterprise warehouse) will prove superior to standalone or top-down approaches
- **2005** — Integrated data mart architecture outcome: Hub-and-spoke data warehouse architecture (matching Aberdeen's integrated model) became the dominant enterprise BI pattern through 2000s; standalone data marts caused exactly the fragmentation Aberdeen warned about
- **1996** — Uncontrolled data mart fragmentation outcome: Aberdeen: enterprises moving away from integrated spirit will squander ROI and be ill-prepared for competitive battles
- **2015** — Data fragmentation problem outcome: 'Data swamp' problem became widespread by 2013-2015 as unmanaged data lakes replicated exactly the fragmentation Aberdeen warned about; data governance and data catalog tools emerged to address this
- **1996** — Data mart thematic variants: Aberdeen identifies distinct data mart themes: sales/marketing, financial, manufacturing, supply chain — each requiring subject-specific modeling with common enterprise metrics
- **1996** — Technology foundation requirements: 'Factory ready' data infrastructure requires: parallel-scalable hardware, RDBMS, ETL tools, and data quality/transformation capabilities before data mart build
- **1996** — Data transformation specialist role: Data transformation specialists (Prism Solutions et al.) provide critical ETL capabilities; short-term consulting engagements with suppliers a viable jump-start strategy
- **1996** — Industry drivers for data architecture change: Global trading, global risk assessment, and competitive intelligence needs cited as primary business drivers accelerating data mart adoption in 1996
- **1996** — Multidimensional DB risk: Proprietary multidimensional database technologies optimize for domain-specific queries but create proprietary lock-in; RDBMS preferred for enterprise integration

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-enterprise-data-knowledge-integrated-data-marts' ORDER BY year_observed;
```

