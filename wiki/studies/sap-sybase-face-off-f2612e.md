---
title: "SAP, Sybase Face Off"
slug: sap-sybase-face-off-f2612e
page_type: study
author: "Doug Bartholomew, InformationWeek (Issue #564)"
date: "1996-01-29"
study_type: news-article
subject_domain: "enterprise-database-ERP"
methodology: "industry-analysis, analyst-commentary"
importance: medium
importance_rationale: "Documents Kastner's 1996 framing of the Sybase strategic error in SAP R/3 database certification — a turning point that accelerated Oracle's dominance of enterprise ERP databases over the next decade."
relevance: medium
relevance_rationale: "Database-vendor competition for ERP certification remains strategically central (Oracle, SAP HANA, Azure SQL); Sybase and Informix both ultimately lost enterprise-database leadership, as Kastner implicitly predicted."
prescience: high
prescience_rationale: "Kastner's 'missing a huge amount of business' assessment proved correct: Sybase failed to recover enterprise-database share, was acquired by SAP itself in 2010 for $5.8B (ironically), and the SAP-on-Oracle installed base grew to tens of thousands of customers. Informix also lost and was acquired by IBM in 2001."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 5
obs_count: 6
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# SAP, Sybase Face Off

> InformationWeek news story (Jan 29 1996, Issue #564) on a feud between SAP AG and Sybase Inc. over database support for SAP's R/3 ERP system. Sybase had promised in October 1995 that SAP R/3 would support its SQL Server System 11 database, but the support does not appear imminent: Mike Regan (GM applications support, Sybase Emeryville) says SAP decides the timing; Paul Wahl (EVP international marketing, SAP Walldorf) says the ball is in Sybase's court. The dispute centers on row-level locking, which Sybase System 10/11 does not support; SAP R/3 requires it for satisfactory multi-user performance. An anonymous former Sybase source describes row-level locking as 'a deal-breaker' for SAP. Peter Kastner, VP and analyst at Aberdeen Group Inc. in Boston, comments: 'There is no doubt Sybase is missing a huge amount of business with SAP. Just look at what a great business SAP has been for Informix.'

**Author:** Doug Bartholomew, InformationWeek (Issue #564) · **Date:** 1996-01-29 · **Type:** news-article
**Importance:** medium — *Documents Kastner's 1996 framing of the Sybase strategic error in SAP R/3 database certification — a turning point that accelerated Oracle's dominance of enterprise ERP databases over the next decade.*
**Prescience:** high — *Kastner's 'missing a huge amount of business' assessment proved correct: Sybase failed to recover enterprise-database share, was acquired by SAP itself in 2010 for $5.8B (ironically), and the SAP-on-Oracle installed base grew to tens of thousands of customers. Informix also lost and was acquired by…*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[informationweek|InformationWeek / TechWeb]]
- [[informix|Informix Software]]
- [[mike-regan-sybase|Mike Regan]]
- [[oracle-corp|Oracle Corporation]]
- [[paul-wahl-sap|Paul Wahl]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sap-ag|SAP AG (later SAP SE)]]
- [[sybase|Sybase, Inc.]]

## Technologies (5)

- [[client-server|Client-Server Computing]]
- [[oracle-database|Oracle Database 7/8i/9i/10g/11g]]
- [[row-level-locking|Row-level locking (DBMS concurrency)]]
- [[sap-r3|SAP R/3 ERP system]]
- [[sybase-sql-server|Sybase SQL Server System 10 / 11 (ASE)]]

## Key observations (top 25)

- **1996** — Sybase missing SAP R/3 business: There is no doubt Sybase is missing a huge amount of business with SAP. Just look at what a great business SAP has been for Informix.
- **1996** — Row-level locking deal-breaker: Sybase's not supporting row-level locking was a deal-breaker for SAP. There was a lot of hope at Sybase that they would be able to do some sort of patch to enable SAP to work with their database, but it did not happen.
- **1996** — Sybase 11 has not proven performance for R/3: They have not proven to SAP that Sybase 11 can perform to the level we would need for R/3 to be made available on Sybase.
- **2001** — SAP never ran production R/3 on Sybase ASE at scale: SAP R/3 ASE support eventually arrived but Sybase was never a major share-holder of the SAP database installed base. SAP customers continued to split between Oracle, IBM DB2, SQL Server, and later SAP HANA.
- **2010** — SAP acquires Sybase: SAP AG acquired Sybase in 2010 for approximately $5.8 billion, integrating Sybase ASE / IQ / Replication Server / mobile platform into SAP's product line — ironic outcome to the 1996 database-certification feud.
- **2001** — Informix acquired by IBM: Informix Software was acquired by IBM in 2001 for approximately $1 billion — consistent with Kastner\"s implied view that the entire non-Oracle RDBMS tier was losing share.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sap-sybase-face-off-f2612e' ORDER BY year_observed;
```

