---
title: "PLATINUM RiskAdvisor: Insurance Data Warehousing For Intelligent Risk Management"
slug: platinum-riskadvisor-ec30de
page_type: study
author: "Aberdeen Group"
date: "1997-01-01"
study_type: market-study
subject_domain: "insurance-data-warehousing"
methodology: "industry-analysis,competitive-profiling,expert-opinion,field-research"
importance: high
importance_rationale: "In 1997 packaged vertical data warehouse solutions were at the frontier of BI market development; this profile documents one of the first industry-specific data warehouse products for insurance at a time when custom-built warehouses dominated, making it historically significant for the shift toward packaged BI."
relevance: medium
relevance_rationale: "The core argument — that packaged industry-specific data models reduce warehouse build time and cost vs. custom approaches — remains highly relevant to modern cloud data warehouse implementations (Snowflake industry editions, Databricks vertical accelerators); specific PLATINUM products are obsolete but the architectural pattern is actively debated."
prescience: medium
prescience_rationale: "Aberdeen predicted RiskAdvisor would become the prevailing trend in data warehousing and help insurers jump-start BI initiatives; PLATINUM was acquired by Computer Associates in 1999 for $3.5B and its products eventually phased out, but the packaged vertical data warehouse concept Aberdeen championed proved broadly correct."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 15
obs_count: 25
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# PLATINUM RiskAdvisor: Insurance Data Warehousing For Intelligent Risk Management

> Aberdeen Group profiles PLATINUM technology inc.'s RiskAdvisor — a packaged data warehouse application for the insurance industry built on an RDBMS star schema (RDM) with 20+ client-side modules covering premium and loss functions. The study argues that custom-built insurance data warehouses take too long and cost too much, and that RiskAdvisor's pre-built industry-specific data model dramatically accelerates deployment. Early user testimony confirms 90-120 day implementation timelines at large insurers.

**Author:** Aberdeen Group · **Date:** 1997-01-01 · **Type:** market-study
**Importance:** high — *In 1997 packaged vertical data warehouse solutions were at the frontier of BI market development; this profile documents one of the first industry-specific data warehouse products for insurance at a time when custom-built warehouses dominated, making it historically significant for the shift toward…*
**Prescience:** medium — *Aberdeen predicted RiskAdvisor would become the prevailing trend in data warehousing and help insurers jump-start BI initiatives; PLATINUM was acquired by Computer Associates in 1999 for $3.5B and its products eventually phased out, but the packaged vertical data warehouse concept Aberdeen champione…*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates International Inc.]]
- [[insurance-200|Insurance 200]]
- [[large-insurer-customer|Large Insurance Customer (anonymous)]]
- [[platinum-technology|PLATINUM technology inc.]]

## Technologies (15)

- [[ibm-db2|IBM DB2]]
- [[informix|Informix]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[oracle-db|Oracle Database]]
- [[platinum-forest-trees|PLATINUM Forest & Trees]]
- [[platinum-infopump|PLATINUM InfoPump]]
- [[platinum-inforefiner|PLATINUM InfoRefiner]]
- [[platinum-poems|PLATINUM Open Enterprise Management System (POEMS)]]
- [[platinum-riskadvisor|PLATINUM RiskAdvisor]]
- [[rdbms-star-schema|RDBMS Star Schema]]
- [[red-brick|Red Brick Systems]]
- [[riskadvisor-data-model|RiskAdvisor Data Model (RDM)]]
- [[sybase|Sybase SQL Server]]
- [[vsam|VSAM (Virtual Storage Access Method)]]
- [[windows-31|Microsoft Windows 3.1]]

## Key observations (top 25)

- **1997** — Product positioning: Packaged vertical data warehouse application for insurance industry targeting largest insurers with $100M-$30B annual net premiums written
- **1997** — Core data model architecture: Highly refined RDBMS star schema (RDM) organizing insurer data by master policy and claim records with premium/claim financial transactions
- **1997** — Client-side module count: 20+ client-side modules covering most premium- and loss-related tasks
- **1997** — PLATINUM employee count (consultants): 500 consultants
- **1997** — Target insurer net premiums minimum: $100 million annual net premiums written (minimum target)
- **1997** — Target insurer net premiums maximum: $30 billion annual net premiums written (maximum target)
- **1997** — Risk exposure per commercial customer failure: Between $50M and $100M risk if commercial customer not effectively serviced
- **1997** — Implementation time to first results: 90 to 120 days typical for comprehensive RiskAdvisor installation to begin returning enterprise-enhancing results
- **1997** — Anonymous early adopter testimony: Large insurer ($3.5B+ net premiums) praised rapid installation; learned what information to include/exclude; system instantly received at senior executive level; now bringing subsidiaries into RiskAdvisor
- **1997** — Early adopter historical data depth: Managed nearly 25 years of historical risk management data in RiskAdvisor
- **1997** — Metadata architecture: Metadata layer provides point-and-click adjustment to system changes; automatically updates desktop modules when server-side changes occur; reduces ongoing maintenance
- **1997** — Desktop module technology base: RiskAdvisor desktop modules based on PLATINUM Forest & Trees decision-support software; Windows 3.1+; approx 300 different views of information
- **1997** — Three interaction levels — Executive Summary: Executive Level Summaries: back-end triggers/alerts with drill-down via direct access buttons for senior executives
- **1997** — Three interaction levels — Operational Flow: Operational Flow: organizational structure drill-down from parent to individual companies and lines of business into modules
- **1997** — Three interaction levels — Free Flow: Free Flow: menu-driven open access to all RiskAdvisor modules broken down by business function for designated users
- **1997** — PLATINUM vertical industry strategy: PLATINUM planned to verticalize industries including finance / healthcare / telecommunications following RiskAdvisor insurance model
- **1997** — PLATINUM founding and IPO: Founded 1987; public company NASDAQ:PLAT since 1991; growth strategy of acquiring and refining software
- **1997** — Supported RDBMS targets: IBM DB2, Informix, Microsoft SQL Server, Oracle, Red Brick, Sybase; also DB2 for OS/2 and AIX, Lotus Notes, HP Allbase/Image, dBase, Paradox
- **1997** — Aberdeen prevailing trend prediction: RiskAdvisor embodies what should become the prevailing trend in data warehousing: deep industry-specific content delivered via strong technology backbone to different user classes
- **1997** — PLATINUM market viability prediction: Aberdeen encourages enterprises to introduce RiskAdvisor as point of comparison when evaluating insurance data warehousing; PLATINUM well established in insurance
- **1997** — Vertical data warehouse concept viability: Aberdeen predicts packaged industry-specific data warehousing will become the prevailing trend vs. custom build-your-own approach
- **1999** — PLATINUM acquisition by Computer Associates: Computer Associates acquired PLATINUM technology for $3.5B in 1999 — largest software industry deal at that time; PLATINUM FY1998 revenue was $968M
- **2002** — PLATINUM product fate post-CA acquisition: PLATINUM RiskAdvisor and related products gradually discontinued under Computer Associates ownership; CA absorbed PLATINUM's infrastructure and mainframe tools; BI/data warehouse products were not continued as strategic investments
- **2026** — Star schema data model longevity: RDBMS star schema pattern for analytical data warehouses remains the dominant design paradigm in 2026 (Kimball dimensional modeling); directly validates Aberdeen's architectural observation
- **1997** — Insurance warehouse complexity challenge: Largest insurers typically multinational, geographically dispersed; $50-100M risk per commercial customer failure; requires analysis tools for premiums/claims/investments/brokers/agents/loss-reserves

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'platinum-riskadvisor-ec30de' ORDER BY year_observed;
```

