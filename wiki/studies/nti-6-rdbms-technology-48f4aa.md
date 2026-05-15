---
title: "RDBMS Report Card"
slug: nti-6-rdbms-technology-48f4aa
page_type: study
author: "Peter S. Kastner, John Logan, Thomas Willmott"
date: "1993-04-01"
study_type: market-study
subject_domain: "relational-database-management"
methodology: "industry-analysis, technology-assessment, vendor-profiling"
importance: high
importance_rationale: "One of the earliest structured vendor report cards for enterprise RDBMS in the client-server era; shaped buying decisions by IS executives at Fortune 500 enterprises in 1993."
relevance: medium
relevance_rationale: "The vendor landscape has changed dramatically (Ingres absorbed, Sybase acquired by SAP, Informix by IBM) but the evaluation framework and RDBMS functional criteria remain instructive for database selection today."
prescience: high
prescience_rationale: "Oracle's predicted dominance proved accurate; the forecast that RDBMS would become the primary enterprise application platform was fully borne out by the ERP and data-warehouse booms of the mid-to-late 1990s."
license: CC-BY-4.0
tier: 1
entity_count: 16
tech_count: 18
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# RDBMS Report Card

> Aberdeen Group evaluates the role of relational database management systems (RDBMS) in enterprise computing, covering their use in OLTP and decision support. The study profiles six leading independent RDBMS vendors—Oracle, Ingres, Sybase, Informix, Software AG, and Progress—against seven functional criteria and produces a best-in-class report card. Aberdeen concludes that RDBMS has become the central application platform for enterprises and that Oracle leads the market while IBM's DB2 trails all competitors.

**Author:** Peter S. Kastner, John Logan, Thomas Willmott · **Date:** 1993-04-01 · **Type:** market-study
**Importance:** high — *One of the earliest structured vendor report cards for enterprise RDBMS in the client-server era; shaped buying decisions by IS executives at Fortune 500 enterprises in 1993.*
**Prescience:** high — *Oracle's predicted dominance proved accurate; the forecast that RDBMS would become the primary enterprise application platform was fully borne out by the ERP and data-warehouse booms of the mid-to-late 1990s.*

## Entities (16)

- [[aberdeen-group|Aberdeen Group]]
- [[ask-group|ASK Group]]
- [[digital-equipment-corporation|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[informix|Informix Corporation]]
- [[ingres|Ingres (ASK Group)]]
- [[john-logan|John Logan]]
- [[oracle|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[progress-software|Progress Software Corporation]]
- [[software-ag|Software AG]]
- [[sybase|Sybase, Inc.]]
- [[tandem-computers|Tandem Computers]]
- [[thomas-willmott|Thomas Willmott]]
- [[transaction-processing-council|Transaction Processing Performance Council (TPC)]]

## Technologies (18)

- [[adabas|ADABAS]]
- [[allbase-sql|ALLBASE/SQL]]
- [[as400|IBM AS/400]]
- [[db2|IBM DB2]]
- [[mvs|IBM MVS]]
- [[natural-4gl|Natural (4GL)]]
- [[netware|Novell NetWare]]
- [[nonstop-sql|NonStop SQL]]
- [[oltp|Online Transaction Processing (OLTP)]]
- [[oracle-v7|Oracle Version 7]]
- [[os2-data-manager|OS/2 Data Manager]]
- [[progress-4gl|Progress 4GL]]
- [[qs400|QS/400]]
- [[rdbms|Relational Database Management System (RDBMS)]]
- [[sql|Structured Query Language (SQL)]]
- [[sybase-system-10|Sybase System 10]]
- [[two-phase-commit|Two-Phase Commit]]
- [[vax-rdb|VAX/Rdb]]

## Key observations (top 25)

- **1993** — RDBMS enterprise role: Primary software platform for enterprise IS infrastructure; unifies mainframe, midrange, and desktop
- **1993** — RDBMS OLTP capability: Can support 99.99% of all real-world OLTP applications
- **1993** — Rules and policies functionality: Reduces application development code by up to 35%
- **1992** — Oracle revenues: Over $1.2 billion
- **1993** — Oracle RDBMS market position: Market leader; largest installed base
- **1993** — Oracle Version 7 technical leadership: First time Oracle demonstrated true technical leadership
- **1992** — Ingres revenues: Approximately $250 million
- **1993** — Ingres client-server leadership potential: Aggressive MS-Windows client support; best-in-class client-server dev tools
- **1993** — Sybase revenues: $300+ million (public company)
- **1993** — Sybase System 10 strategic intent: Challenge Oracle for enterprise-class RDBMS leadership; gateways, replication server, network admin
- **1993** — Informix market position: Unix RDBMS standard; champion of speed and portability; VAR tool of choice at low end
- **1993** — Software AG R&D investment rate: 25% of revenues invested in R&D
- **1992** — Progress Software revenues: $80 million
- **1993** — IBM RDBMS rating: Worst-in-class across all platforms (DB2, QS/400, OS/2 Data Manager)
- **1993** — Best-in-class: Mission Critical Applications: Oracle best-in-class; none lacking
- **1993** — Best-in-class: Performance: Software AG, Informix, Oracle lead; none lacking for 95%+ of applications
- **1993** — Best-in-class: Business Rules: Sybase and Ingres best-in-class; Progress lacking
- **1993** — Best-in-class: Data Extensibility: Informix and Ingres best; Progress least capable
- **1993** — Best-in-class: Client-Server Application Development: Ingres best-in-class; all others far behind
- **1993** — Best-in-class: Upper CASE Tools: Oracle indisputable best-in-class
- **1993** — Best-in-class: Open Technology (SQL/Non-SQL gateway, Open Server): Oracle best-in-class in open interfaces; truly committed to openness
- **1993** — Two-phase commit maturity: All major vendors implementing; no single implementation stands out
- **1993** — Best-in-class: Distributed Operations: Ingres, Oracle, Informix all best-in-class; none lacking
- **1993** — RDBMS market divergence prediction: Continued divergence among leading suppliers in approaching client-server marketplace over next 5 years
- **1998** — RDBMS market divergence — outcome: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'nti-6-rdbms-technology-48f4aa' ORDER BY year_observed;
```

