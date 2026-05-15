---
title: "Universal Servers: RDBMS Technology for the Next Decade"
slug: aberdeen-1995-universal-servers-rdbms-technology-next-decade
page_type: study
author: "Peter S. Kastner, Wayne Kernochan (Aberdeen Group)"
date: "1995-06-03"
study_type: technology-viewpoint
subject_domain: "relational database management systems and object-relational extensions"
methodology: "analyst-assessment,vendor-briefing,user-interviews"
importance: high
importance_rationale: "This report precisely documents the 1995 emergence of object-relational databases — a foundational transition in database technology history. Aberdeen's analysis of Informix/Illustra DataBlade architecture and its comparison to Oracle and IBM is primary source documentation of this technology inflection."
relevance: high
relevance_rationale: "Universal Server concepts (complex data types, extensibility, ROLAP) directly anticipate modern database capabilities including PostgreSQL extensions, vector databases, and modern multi-model databases. The framework remains analytically useful for assessing database extensibility."
prescience: high
prescience_rationale: "Aberdeen's core predictions proved remarkably accurate: RDBMS survived OODBMSs, complex data types did become standard (object-relational became mainstream via PostgreSQL and Oracle), ROLAP became major BI architecture, and LDAP/Internet data integration happened. However, Informix's predicted leadership was disrupted by its 2001 acquisition by IBM."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 9
obs_count: 28
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Universal Servers: RDBMS Technology for the Next Decade

> Aberdeen examines the emergence of Universal Servers — RDBMS extensions supporting complex data types (text, video, spatial, ROLAP, user-defined) — as the next major RDBMS evolution beyond simple numeric data. The study positions Informix (via Illustra DataBlade acquisition) as the leader, assesses Oracle 7.3, IBM DB2, Sybase, Computer Associates, and Microsoft, and predicts Universal Server technology will become widespread within 2-3 years and be the most significant RDBMS advance for the next decade.

**Author:** Peter S. Kastner, Wayne Kernochan (Aberdeen Group) · **Date:** 1995-06-03 · **Type:** technology-viewpoint
**Importance:** high — *This report precisely documents the 1995 emergence of object-relational databases — a foundational transition in database technology history. Aberdeen's analysis of Informix/Illustra DataBlade architecture and its comparison to Oracle and IBM is primary source documentation of this technology inflec…*
**Prescience:** high — *Aberdeen's core predictions proved remarkably accurate: RDBMS survived OODBMSs, complex data types did become standard (object-relational became mainstream via PostgreSQL and Oracle), ROLAP became major BI architecture, and LDAP/Internet data integration happened. However, Informix's predicted leade…*

## Entities (9)

- [[ENT-CA-INGRES|Computer Associates (CA-Ingres + Jasmine)]]
- [[ENT-IBM-DB2|IBM DB2]]
- [[ENT-ILLUSTRA|Illustra Information Technologies]]
- [[ENT-INFORMIX|Informix Corporation]]
- [[ENT-MAPINFO|MapInfo Corporation]]
- [[ENT-MSFT-SQL|Microsoft SQL Server]]
- [[ENT-ORACLE-DB4|Oracle Corporation]]
- [[ENT-SYBASE-DB|Sybase Inc.]]
- [[ENT-VERITY|Verity Inc.]]

## Technologies (9)

- [[TECH-DATABLADE|Informix DataBlade Modules]]
- [[TECH-FULL-TEXT|Full-Text Search Database Extensions]]
- [[TECH-INTRANET|Corporate Intranet Architecture]]
- [[TECH-OODBMS|Object-Oriented DBMS (OODBMS)]]
- [[TECH-RDBMS|Relational Database Management System (RDBMS)]]
- [[TECH-ROLAP|Relational OLAP (ROLAP)]]
- [[TECH-SPATIAL-DB|Spatial/Geographic Database Extensions]]
- [[TECH-UDT|User-Defined Data Types (UDT)]]
- [[TECH-UNIVERSAL-SERVER|Universal Server (Object-Relational DBMS)]]

## Key observations (top 25)

- **1995** — RDBMS dominance: 5 of top-10 ISVs sell RDBMS: Microsoft, CA, Oracle, Sybase, Informix (plus IBM DB2)
- **1995** — OODBMS market verdict: market voted OODBMSs are niche; not appropriate for large-scale or mission-critical applications
- **1995** — Universal Server definition: RDBMS offering efficient access to complex data types and open extensible user-defined data types
- **1995** — Informix Universal Server leadership: Illustra+Informix-OnLine combination leads in Universal Server; 25 DataBlade modules expected by end of 1995
- **1995** — Oracle 7.3 Universal Server assessment: video, text (ConText), spatial options added but still distinct servers not fully integrated; extensibility requires future Oracle Universal Database release
- **1995** — IBM DB2 Universal Server assessment: DB2 Relational Extenders for text/imaging/audio/video; not yet deep in architecture or sophisticated client-server toolset
- **1995** — CA Universal Server strategy: CA has dual strategy (Jasmine OODBMS + CA-Ingres); no plans to combine or offer Universal Server functionality
- **1995** — Sybase Universal Server readiness: not yet implemented comparable complex-data-type support; Adaptive Server + Object-Connect middleware planned
- **1995** — Universal Server adoption timeline: Universal Server technology will become widespread within 2-3 years as RDBMS suppliers bring products to market
- **1995** — RDBMS investment protection: Universal Server will provide RDBMS investment protection beyond 2005
- **1995** — Informix market leadership sustainability: Informix still the leader that others must follow in Universal Server technology
- **2001** — Informix fate: IBM acquired Informix database assets for $1B in April 2001; Informix leadership ended
- **2000** — Oracle object-relational outcome: Oracle8/8i/9i delivered full object-relational features; Oracle became dominant RDBMS vendor
- **2005** — ROLAP market outcome: ROLAP became standard BI architecture; implemented in every major RDBMS by 2000
- **2005** — Spatial database extensions outcome: Spatial extensions became standard: PostGIS (2001), Oracle Spatial, SQL Server Spatial; foundational to GIS
- **2000** — UDT standardization outcome: UDTs standardized in SQL:1999; implemented in PostgreSQL, DB2, Oracle; foundational to extension ecosystems
- **1995** — Intranet as database integration driver: Internet/Intranet demands text and graphic data types that challenge RDBMS integration
- **1995** — Universal Server evaluation criteria: Extensibility/flexibility + Core RDBMS integration + Performance + Administration + Transparency
- **1995** — DataBlade SAP/PeopleSoft/Baan migration promise: SAP, PeopleSoft, Baan announced as able to migrate to Informix Universal Server without app-code changes
- **1995** — Text search as Universal Server use case: text-search on comments fields can extract repeated information defying today RDBMS query capabilities
- **1995** — RDBMS technology pressure sources: ROLAP multidimensional data, Internet/Intranet text+graphics, OOP development toolsets all pressure simple-data RDBMS
- **1995** — Programmer productivity benefit: Universal Server will significantly improve programmer productivity for large-scale data-intensive applications
- **1995** — ROLAP current limitations: today ROLAP/RDBMS bitmap indexing+star schemas deliver order-of-magnitude complex-query speedups; further improvement requires UDT in core optimizer
- **1995** — Informix-OnLine TPC benchmark standing: Informix-OnLine architecture regarded as leader in parallel scalability; hardware suppliers favor for TPC benchmarking
- **1995** — study publication details: Volume 9/Number 13, June 3, 1995

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-universal-servers-rdbms-technology-next-decade' ORDER BY year_observed;
```

