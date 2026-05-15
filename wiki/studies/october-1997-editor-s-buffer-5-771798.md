---
title: "Editor's Buffer (October 1997)"
slug: october-1997-editor-s-buffer-5-771798
page_type: study
author: "Editor, Database Programming & Design (Miller Freeman)"
date: "1997-10-01"
study_type: editorial
subject_domain: "database-market"
methodology: "industry-analysis, editorial-commentary"
importance: medium
importance_rationale: "Captures the late-1990s database market consolidation thesis (IBM/Oracle/Microsoft vs. everyone else) that defined the following decade."
relevance: medium
relevance_rationale: "DBMS market has since added cloud players (AWS, Google, Azure, Snowflake) but the top-three consolidation thesis largely held through 2010s."
prescience: high
prescience_rationale: "Kastner's 'tough competition for anyone not IBM/Oracle/Microsoft' framing proved correct: Sybase, Informix, Ingres, NonStop SQL, and most second-tier DBMS vendors were acquired or marginalized within a decade."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 4
obs_count: 6
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Editor's Buffer (October 1997)

> October 1997 editor's column in Database Programming & Design previewing the 1998 Object/Relational Summit. Notes 'The Aberdeen Group's Peter Kastner described well the tough competition facing database vendors not named IBM, Oracle, or Microsoft,' and discusses ODBMS adoption (Thomas Atwood) and Java's JDBC-first orientation.

**Author:** Editor, Database Programming & Design (Miller Freeman) · **Date:** 1997-10-01 · **Type:** editorial
**Importance:** medium — *Captures the late-1990s database market consolidation thesis (IBM/Oracle/Microsoft vs. everyone else) that defined the following decade.*
**Prescience:** high — *Kastner's 'tough competition for anyone not IBM/Oracle/Microsoft' framing proved correct: Sybase, Informix, Ingres, NonStop SQL, and most second-tier DBMS vendors were acquired or marginalized within a decade.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[ibm|International Business Machines Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[miller-freeman|Miller Freeman Inc.]]
- [[obj-relational-summit|Object/Relational Summit]]
- [[object-design-inc|Object Design, Inc.]]
- [[oracle-corp|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[thomas-atwood|Thomas Atwood]]

## Technologies (4)

- [[commercial-rdbms|Commercial Relational Database Management Systems]]
- [[java-platform|Java Platform]]
- [[jdbc|JDBC (Java Database Connectivity)]]
- [[odbms|Object Database Management System (ODBMS)]]

## Key observations (top 25)

- **1997** — DBMS vendor competition thesis: Tough competition facing database vendors not named IBM, Oracle, or Microsoft.
- **1997** — ODBMS economics and marketing: Atwood cites economics and marketing as the major reasons ODBMS has yet to impact the mainstream.
- **1997** — Java promise for ODBMS: Java was thought to offer ODBMS vendors an excellent opportunity — but this was compromised by economic necessity with JDBC-first orientation.
- **1997** — Top-three DBMS vendor consolidation: Kastner framing implies that commercial RDBMS market will consolidate to IBM / Oracle / Microsoft dominance over the following 5-10 years.
- **2010** — Top-three DBMS market outcome: By 2010 IBM (DB2), Oracle, and Microsoft SQL Server dominated commercial RDBMS; Sybase acquired by SAP (2010), Informix by IBM (2001), Ingres by CA then independent. Cloud players (AWS RDS, etc.) entered thereafter.
- **2005** — ODBMS niche outcome: ODBMS did not displace RDBMS; Object Design was acquired by Progress (2003); remaining ODBMS tools became niche embedded/edge solutions.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'october-1997-editor-s-buffer-5-771798' ORDER BY year_observed;
```

