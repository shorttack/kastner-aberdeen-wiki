---
title: "RS/6000 RDBMS Sales Training"
slug: ibm-rs6000-midran~1-88f049
page_type: study
author: "Peter S. Kastner"
date: "1995-01-01"
study_type: benchmark
subject_domain: "RDBMS-competitive-analysis, midrange-servers"
methodology: "competitive-profiling, industry-analysis, benchmarking, expert-opinion"
importance: high
importance_rationale: "Primary-source competitive intelligence document from Aberdeen Group for IBM's RS/6000 sales force; captures the mid-1990s RISC/UNIX and open-systems RDBMS market landscape with quantitative revenue and share data."
relevance: medium
relevance_rationale: "Specific competitive positions are dated but the analytical framework for positioning midrange UNIX servers against RDBMS competitors remains instructive for technology sales training."
prescience: high
prescience_rationale: "The prediction that IBM's chief competition for IS executive allegiance would come from software/solution suppliers (Oracle, SAP, Microsoft) rather than hardware suppliers proved accurate; IBM's subsequent services and software pivot confirms this."
license: CC-BY-4.0
tier: 1
entity_count: 15
tech_count: 25
obs_count: 31
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# RS/6000 RDBMS Sales Training

> An IBM sales training deck prepared by Aberdeen Group in 1995 providing competitive intelligence on the midrange RISC/UNIX market and the major RDBMS vendors. The document profiles IBM RS/6000, HP, Digital, Sun, and AT&T GIS as hardware platforms, then positions IBM's RS/6000 and DB2/6000 against Oracle, Informix, Sybase, and other database competitors. It gives IBM sales representatives detailed strengths, weaknesses, and tactical selling tips for each competitor.

**Author:** Peter S. Kastner · **Date:** 1995-01-01 · **Type:** benchmark
**Importance:** high — *Primary-source competitive intelligence document from Aberdeen Group for IBM's RS/6000 sales force; captures the mid-1990s RISC/UNIX and open-systems RDBMS market landscape with quantitative revenue and share data.*
**Prescience:** high — *The prediction that IBM's chief competition for IS executive allegiance would come from software/solution suppliers (Oracle, SAP, Microsoft) rather than hardware suppliers proved accurate; IBM's subsequent services and software pivot confirms this.*

## Entities (15)

- [[aberdeen-group|Aberdeen Group]]
- [[andersen-consulting|Andersen Consulting]]
- [[att-gis|AT&T Global Information Solutions (NCR)]]
- [[compaq|Compaq]]
- [[digital-equipment|Digital Equipment Corporation]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft]]
- [[ncr|NCR Corporation]]
- [[oracle|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sap|SAP]]
- [[sun-microsystems|Sun Microsystems]]
- [[teradata|Teradata]]

## Technologies (25)

- [[aix|IBM AIX]]
- [[alpha-axp|Digital Alpha AXP (ALPHAserver)]]
- [[att-unix-svr4|AT&T Unix System V.4 MP]]
- [[data-propagator|IBM Data Propagator]]
- [[db2-6000|IBM DB2/6000]]
- [[digital-osf1|Digital OSF/1 (UNIX)]]
- [[digital-vax|Digital VAX/OpenVMS]]
- [[hp-3000|HP 3000]]
- [[hp-9000|HP 9000]]
- [[hp-pa-risc|HP PA-RISC]]
- [[ibm-sp2|IBM SP2]]
- [[netview|IBM NetView]]
- [[netware|Novell NetWare]]
- [[openlook|Sun OpenLook GUI]]
- [[openview|HP OpenView]]
- [[oracle-rdb|Oracle Rdb]]
- [[os2|IBM OS/2]]
- [[power2-rios|IBM Power2 (RIOS)]]
- [[powerpc-601|PowerPC 601]]
- [[rs6000|IBM RS/6000]]
- [[solaris|Sun Solaris]]
- [[sparcenter-2000|Sun SPARCcenter 2000]]
- [[sparcserver-1000|Sun SPARCserver 1000]]
- [[teradata-dss|Teradata DSS Platform]]
- [[windows-nt|Microsoft Windows NT]]

## Key observations (top 25)

- **1994** — 1994 worldwide commercial multiuser RISC/UNIX market size: $10 billion
- **1994** — IBM RS/6000 RISC/UNIX market share: 19%
- **1994** — IBM RS/6000 1994 revenues: $2 billion
- **1994** — IBM RS/6000 revenue growth 1993/94: 52%
- **1994** — IBM SP2 1994 revenues: $200 million
- **1994** — HP 9000 multiuser RISC/UNIX market share: 45%
- **1994** — HP 9000 1994 revenues: $4.5 billion
- **1994** — HP 9000 revenue growth last 3 quarters: 60%
- **1994** — Digital ALPHAserver RISC/UNIX market share: 3%
- **1994** — Digital ALPHAserver revenue growth 1994: 150%
- **1994** — Digital revenues including all add-ons: ~$2.5 billion (~20% of company)
- **1994** — Digital VAX revenue decline per annum: 35% to 50% decline
- **1994** — Sun RISC/UNIX market share: 10%
- **1994** — Sun midrange server revenues: ~$1.1 billion (~20% of Sun)
- **1994** — AT&T GIS 1994 total revenues: ~$4.2 billion
- **1994** — AT&T GIS Intel multiprocessor market revenue: $1.2 billion in 1994
- **1995** — IBM chief competitive threat re-framing: IBM's chief competition for IS executive allegiance is not other hardware suppliers (HP) but software solution suppliers (Oracle, SAP, Microsoft)
- **1995** — IBM RS/6000 value proposition: IBM professional services orgs help customers implement RISC/UNIX-based open client-server computing
- **1995** — IBM SP2 commercial use cases: Complex decision support, LAN server consolidation, OLTP; 380 ISV promises to port RDBMSs and applications
- **1995** — HP competitive position: HP is mainframe alternative leader and trusted supplier for Unix transition; 3 years as Top Gun; getting arrogant and sloppy
- **1995** — Digital viability concerns: Digital not yet out of restructuring woods; has yet to establish critical mass for long-term viability; Alpha/NT looks rosy but lacks 1995 revenues to sustain
- **1995** — Oracle acquires Digital RDB: Oracle acquires RDB and installed base; Oracle and Digital increasing strategic commitments; Oracle is LIMD database
- **1995** — Sun scalability weakness: Real-world scalability of applications very poor on all Sun workstations and servers; Solaris transition problems in 1994
- **1995** — Teradata mismanagement risk: Failure to properly manage Teradata for big customers resulted in backlash and opened data warehousing/complex DSS opportunities
- **1995** — DB2/6000 competitive position: RS/6000 with DB2 is neither the fastest nor least expensive option; RDBMS ISVs fear IBM will switch customers to low-priced DB2

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ibm-rs6000-midran~1-88f049' ORDER BY year_observed;
```

