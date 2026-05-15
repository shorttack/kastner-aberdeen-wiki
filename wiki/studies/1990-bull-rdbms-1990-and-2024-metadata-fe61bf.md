---
title: "Ingres/Sybase Customer Satisfaction Survey for Bull Corporate Strategy & Marketing"
slug: 1990-bull-rdbms-1990-and-2024-metadata-fe61bf
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1990-03-28"
study_type: survey-report
subject_domain: "RDBMS-customer-satisfaction"
methodology: "user-interviews,comparative-analysis,expert-opinion,industry-analysis"
importance: high
importance_rationale: "Rare primary-source survey of RDBMS users during the critical 1990 period when Ingres and Sybase were competing for the emerging high-performance OLTP market against Oracle; findings directly influenced Bull's RDBMS partnership strategy."
relevance: medium
relevance_rationale: "Historical benchmark for understanding RDBMS competitive dynamics in the pre-Oracle-dominance era; Aberdeen's Systems Integration business center recommendation was prescient of the managed services / professional services market that grew through the 1990s."
prescience: high
prescience_rationale: "Aberdeen correctly identified Sybase's platform support limitations (Sun-centric) and predicted Oracle's architectural weakness for high-performance OLTP, both confirmed by subsequent market outcomes; Sybase acquired by SAP for $5.8B in 2010, Ingres became Actian."
license: CC-BY-4.0
tier: 1
entity_count: 15
tech_count: 8
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Ingres/Sybase Customer Satisfaction Survey for Bull Corporate Strategy & Marketing

> This March 1990 Aberdeen Group report surveys ten leading-edge users of Ingres and Sybase relational database management systems on behalf of Bull Corporate Strategy & Marketing. The survey reveals that Ingres users are substantially more satisfied than Sybase users, with no Ingres users reporting reliability problems versus universal Sybase reliability issues. Aberdeen recommends Bull select Ingres version 6.3 as its RDBMS partner due to reliability and stability advantages, and advises establishing an Application Implementation Business Center to differentiate Bull from competitors in the emerging client-server era.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1990-03-28 · **Type:** survey-report
**Importance:** high — *Rare primary-source survey of RDBMS users during the critical 1990 period when Ingres and Sybase were competing for the emerging high-performance OLTP market against Oracle; findings directly influenced Bull's RDBMS partnership strategy.*
**Prescience:** high — *Aberdeen correctly identified Sybase's platform support limitations (Sun-centric) and predicted Oracle's architectural weakness for high-performance OLTP, both confirmed by subsequent market outcomes; Sybase acquired by SAP for $5.8B in 2010, Ingres became Actian.*

## Entities (15)

- [[e90-01|Bull S.A. (Groupe Bull)]]
- [[e90-02|Aberdeen Group]]
- [[e90-03|Ingres Corporation (RTI)]]
- [[e90-04|Sybase Inc.]]
- [[e90-05|Oracle Corporation]]
- [[e90-06|Salomon Brothers]]
- [[e90-07|Chase Manhattan Bank]]
- [[e90-08|Sanford C. Bernstein & Co.]]
- [[e90-09|Stratus Computer]]
- [[e90-10|Polaroid Corporation]]
- [[e90-11|Bowater Paper]]
- [[e90-12|ATD - American Company]]
- [[e90-13|Applied Systems Engineering (ASE)]]
- [[e90-14|Hill A&E / Artsoft]]
- [[e90-15|Sun Microsystems]]

## Technologies (8)

- [[t90-01|Ingres version 5 / version 6]]
- [[t90-02|Sybase version 3 / version 4]]
- [[t90-03|Oracle RDBMS]]
- [[t90-04|SQL (Structured Query Language)]]
- [[t90-05|Client-Server Architecture]]
- [[t90-06|Ingres Knowledge Manager (4GL/CASE tools)]]
- [[t90-07|IMS (IBM Information Management System)]]
- [[t90-08|PS/2 OS/2]]

## Key observations (top 25)

- **1990** — Ingres user satisfaction vs. Sybase user satisfaction: Ingres users extremely satisfied; many Sybase customers would prefer Ingres; no Ingres users reported reliability problems
- **1990** — Sybase platform support limitation: Sybase pro-actively supports only Sun Microsystems and PS/2-OS/2; lacks resources to support Bull's wide family of platforms
- **1990** — Oracle OLTP architectural weakness: Almost every contact volunteered rejection of Oracle due to basic architectural weaknesses for high-performance OLTP
- **1990** — Bull RDBMS recommendation: Aberdeen recommends Ingres as preferred supplier; Ingres 6.3 earliest version Bull should select; Sybase only if marketing capability is priority
- **1990** — Application Implementation Business Center recommendation: Bull should establish Application Implementation Business Center for RDBMS adoption support; revenue from training, design, implementation, upgrade support, SI
- **1990** — RDBMS acquisition/implementation cycle duration: Year 0-1: evaluate; Year 1-2: develop pilot with consultants and train staff; Year 2-3: implement pilot and continue development
- **1990** — Production state of Ingres v6 and Sybase v4 in 1990: Both Ingres v6 and Sybase v4 applications are just now going into production or within next 3 months; high-performance OLTP not yet proved at scale
- **1990** — Sybase marketing superiority over Ingres: Sybase was first RDBMS supplier to show vision of high-performance OLTP and tailor products to win customers; Ingres consistently poorer marketer
- **1990** — Salomon Brothers RDBMS decision: Trade press reported Salomon moving IMS to Sybase; Aberdeen interview revealed Salomon wished it had chosen Ingres instead
- **1990** — Mainframe OLTP performance gap with RDBMS: Even most advanced RDBMS users not achieving mainframe-level performance; high-performance OLTP migration confidence high for near term
- **1990** — Ingres long-term market position prediction: Aberdeen predicts Ingres 6.3 as reliable, stable preferred supplier for Bull; Ingres customers show higher loyalty than Sybase
- **2011** — Ingres/Actian long-term outcome: Ingres sold to ASK Group (1990), CA (1994), spun out (2005), became Actian (2011); acquired by HCL for $330M (2018); Ingres 12.0 active in 2024
- **2010** — Sybase acquisition by SAP: SAP acquired Sybase for $5.8 billion (July 2010); became SAP Adaptive Server Enterprise
- **1990** — Ingres CASE tools and Knowledge Manager satisfaction: Ingres version 6 provides all growth path customers can implement today (especially with Knowledge Manager); Cadre/Ingres CASE tools anticipated
- **1990** — SQL standardization impact on RDBMS adoption: Need for user staff to understand SQL/relational model is major adoption barrier; outside consulting needed for all surveyed companies
- **2024** — Oracle market dominance outcome: Oracle became world's largest RDBMS vendor; Oracle Database market share ~28% of RDBMS market in 2024
- **2010** — Sun Microsystems acquisition: Sun Microsystems acquired by Oracle Corporation for $7.4B in 2010
- **1990** — Hardware platform importance in RDBMS acquisition: No hardware manufacturer was part of acquisition decision making process for surveyed customers; RDBMS selected independently of hardware
- **1990** — Ingres version 5 vs. version 6 satisfaction gap: Ingres users believe deficiencies in version 5 corrected in version 6; v6 gained tremendous additional customer satisfaction and loyalty
- **1990** — Both Ingres and Sybase resource limitations: All 10 customers believed their supplier did not have resources for envisioned product functionality and support services

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1990-bull-rdbms-1990-and-2024-metadata-fe61bf' ORDER BY year_observed;
```

