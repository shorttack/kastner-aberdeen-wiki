---
title: "Migrating From Sybase SQL Server 4.9 To Informix: An Attractive Alternative"
slug: 1997-migrating-from-sybase-sql-server-4.-d7b1d0
page_type: study
author: "Aberdeen Group"
date: "1997"
study_type: Vendor Profile
subject_domain: "Database Management Systems"
methodology: "Vendor-sponsored comparative analysis; product feature review; upgrade path assessment"
importance: medium
importance_rationale: "Moderate historical importance as a vendor-profile/advocacy document from a period of intense RDBMS market consolidation. Captures the competitive dynamics between Sybase and Informix at a turning point — both companies later ceased independent existence. Documents product features and migration tooling that influenced enterprise database decisions in the late 1990s."
relevance: high
relevance_rationale: "Highly relevant to historians of enterprise database markets, RDBMS consolidation, and 1990s IT decision-making. The migration considerations (upgrade complexity, stored procedure compatibility, SMP scalability) prefigure enduring concerns in database migration. Also relevant as a case study in vendor-sponsored research."
prescience: medium
prescience_rationale: "Aberdeen correctly anticipated Sybase's decline and financial difficulties (Sybase saw major losses and market share erosion through 1997-2002). The prediction that the RDBMS market would consolidate to 2-3 major players proved accurate (Oracle, Microsoft SQL Server, IBM DB2 dominate). The suggestion that Informix was a 'strong long-term player' was partially wrong — Informix was acquired by IBM in 2001 following an accounting scandal. The emphasis on SMP scalability and object-relational capabi…"
license: CC-BY-4.0
tier: 2
entity_count: 10
tech_count: 12
obs_count: 23
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Migrating From Sybase SQL Server 4.9 To Informix: An Attractive Alternative

> Aberdeen Group recommends that Sybase SQL Server 4.9 users consider migrating to Informix as a viable alternative to upgrading to Sybase System 11. The study examines challenges of the Sybase upgrade path — hardware requirements, stored-procedure rewrites, administrator retraining — versus Informix compatibility tooling. Informix-OnLine strengths in SMP scalability, object-relational Universal Server, DataBlades, row-level locking, and VAR relationships are highlighted. Study was sponsored by Informix Software, Inc.

**Author:** Aberdeen Group · **Date:** 1997 · **Type:** Vendor Profile
**Importance:** medium — *Moderate historical importance as a vendor-profile/advocacy document from a period of intense RDBMS market consolidation. Captures the competitive dynamics between Sybase and Informix at a turning point — both companies later ceased independent existence. Documents product features and migration too…*
**Prescience:** medium — *Aberdeen correctly anticipated Sybase's decline and financial difficulties (Sybase saw major losses and market share erosion through 1997-2002). The prediction that the RDBMS market would consolidate to 2-3 major players proved accurate (Oracle, Microsoft SQL Server, IBM DB2 dominate). The suggestio…*

## Entities (10)

- [[ENT-ABD-001|Aberdeen Group Inc.]]
- [[ENT-ILL-001|Illustra Information Technologies]]
- [[ENT-INF-001|Informix Software Inc.]]
- [[ENT-MAP-001|MapInfo Corporation]]
- [[ENT-ORA-001|Oracle Corporation]]
- [[ENT-SAP-001|SAP SE]]
- [[ENT-STG-001|Stanford Technology Group]]
- [[ENT-SYB-001|Sybase Inc.]]
- [[ENT-TIV-001|Tivoli Systems Inc.]]
- [[ENT-VER-001|Verity Inc.]]

## Technologies (12)

- [[TECH-DB-001|DataBlade Modules]]
- [[TECH-DBLIB-001|Sybase DB-Library (DB-Lib)]]
- [[TECH-ESQL-001|Informix ESQL-C / SPL]]
- [[TECH-INF-NE-001|Informix-NewEra]]
- [[TECH-INF-OL-001|Informix-OnLine]]
- [[TECH-INF-US-001|Informix Universal Server]]
- [[TECH-INF-XPS-001|Informix-OnLine XPS]]
- [[TECH-ROW-001|Row-Level Locking]]
- [[TECH-SMP-001|SMP Scalability (Symmetric Multiprocessing)]]
- [[TECH-SYB11-001|Sybase System 11]]
- [[TECH-SYB49-001|Sybase SQL Server 4.9]]
- [[TECH-TSQL-001|Sybase Transact-SQL]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-migrating-from-sybase-sql-server-4.-d7b1d0' ORDER BY year_observed;
```

