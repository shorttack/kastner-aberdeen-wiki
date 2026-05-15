---
title: "DB2 Common Server Relational Database Management System"
slug: aberdeen-1995-ibm-db2-common-server
page_type: study
author: "Aberdeen Group"
date: "1995-01-01"
study_type: product-profile
subject_domain: "relational-database-management"
methodology: "industry-analysis, competitive-profiling, benchmarking"
importance: high
importance_rationale: "Evaluated DB2 v2 at the critical juncture when it achieved functional parity with Oracle/Sybase/Informix; Aberdeen's DORS framework and recommendation drove enterprise purchasing at IBM's $64B revenue scale; the study's assessment accurately captured DB2's competitive positioning in the $11B IBM software business."
relevance: medium
relevance_rationale: "IBM Db2 remains an active enterprise database platform in 2026, and DataPropagator/replication technology concepts survive in IBM's replication suite; however specific products (OS/2, RS/6000) are obsolete and the competitive landscape has transformed with cloud databases."
prescience: high
prescience_rationale: "DB2 delivered on roadmap promises (Relational Extenders, DataPropagator update-anywhere, Lotus integration); DB2 revenue grew 73% in 2000 vs industry 3x faster (IBM Annual Report 2000); approximately 1,000 Oracle customers switched to DB2 by 2000—validating Aberdeen's recommendation."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 35
obs_count: 58
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# DB2 Common Server Relational Database Management System

> Aberdeen Group profile evaluating IBM's DB2 Common Server, a distributed relational database management system designed to provide a common SQL interface across multiple platforms. Examines competitive positioning against Oracle, Sybase, and Informix.

**Author:** Aberdeen Group · **Date:** 1995-01-01 · **Type:** product-profile
**Importance:** high — *Evaluated DB2 v2 at the critical juncture when it achieved functional parity with Oracle/Sybase/Informix; Aberdeen's DORS framework and recommendation drove enterprise purchasing at IBM's $64B revenue scale; the study's assessment accurately captured DB2's competitive positioning in the $11B IBM sof…*
**Prescience:** high — *DB2 delivered on roadmap promises (Relational Extenders, DataPropagator update-anywhere, Lotus integration); DB2 revenue grew 73% in 2000 vs industry 3x faster (IBM Annual Report 2000); approximately 1,000 Oracle customers switched to DB2 by 2000—validating Aberdeen's recommendation.*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates]]
- [[ibm|IBM]]
- [[informix|Informix]]
- [[lotus|Lotus Development]]
- [[lotus-notes|Lotus Notes / Domino]]
- [[novell|Novell]]
- [[oracle|Oracle]]
- [[powersoft|Powersoft]]
- [[seer-technologies|Seer Technologies]]
- [[sybase|Sybase]]
- [[transarc|Transarc]]

## Technologies (35)

- [[adsm|ADSM (Adstar Distributed Storage Manager)]]
- [[aix|AIX]]
- [[cics|CICS]]
- [[databasic|DataBasic (Stored Procedure Builder)]]
- [[datahub|DataHub]]
- [[datajoiner|DataJoiner]]
- [[datapropagator|DataPropagator]]
- [[datarefresher|DataRefresher]]
- [[db2-common-server|DB2 Common Server]]
- [[db2-mvs|DB2/MVS]]
- [[db2-parallel-edition|DB2 Parallel Edition]]
- [[drda|DRDA (Distributed Relational Database Architecture)]]
- [[encina|Encina]]
- [[flowmark|IBM FlowMark]]
- [[hacmp|HACMP]]
- [[lotus-approach|Lotus Approach]]
- [[lotus-notes|Lotus Notes]]
- [[notespump|NotesPump]]
- [[odbc|ODBC]]
- [[os2|OS/2 Warp]]
- [[powerbuilder|PowerBuilder]]
- [[racf|RACF]]
- [[rexx|REXX]]
- [[rs6000|IBM RS/6000]]
- [[rs6000-sp|IBM RS/6000 SP]]
- [[sna-lu62|SNA LU6.2 (APPC/APPN)]]
- [[snmp|SNMP]]
- [[sql|SQL]]
- [[tcp-ip|TCP/IP]]
- [[tpc-c|TPC-C]]

## Key observations (top 25)

- **1995** — is: client-server version of DB2/MVS RDBMS running on RS/6000 (AIX) and OS/2 Warp/Warp Connect
- **1995** — ported to: HP-UX and Sun Solaris; porting in progress to Siemens Nixdorf, Windows NT, and PowerPC
- **1995** — is characterized as: major player and strong competitor in the DORS market, especially in the IBM-workstation-server market
- **1995** — includes: core DB2 RDBMS plus DataPropagator, DataRefresher, DataJoiner, DataHub, Visualizer, DB2 Parallel Edition
- **1995** — recommended for: databases requiring connectivity to other IBM platforms; middle tier of three-tier solutions; medium-to-large-scale data-warehousing; mission-critical OLTP
- **1995** — compared to competitors: has added functionality to compete on equal technological basis with, and in some cases surpass, other major DORS suppliers
- **1995** — advises: IS buyers should take a new and closer look at DB2 for distributed, open production systems
- **1995** — available on: OS/2, AIX, Windows NT servers; beta on HP-UX, Solaris, Sinix; DB2 Web server support upcoming
- **1995** — supports protocols: TCP/IP, SPX/IPX, NetBIOS, SNA LU6.2 (APPC/APPN); interconnection to MVS, OS/400, VSE, VM via DRDA
- **1995** — adopted by: 11.0 suppliers
- **1995** — sells DB2 via: vast global direct-sales force, often bundled with IBM hardware and services; channel-enabling for version 2
- **1995** — experience: 10.0 years
- **1995** — TPC-C result: 3119.16 tpmC
- **1995** — TPC-C price-performance: 349.0 USD/tpmC
- **1995** — adds SMP enablement: multithreading support for SMP scalability matching other major DORS suppliers
- **1995** — enhanced in v2: query rewrite, more alternatives, better non-uniform data distribution detection, pre-fetching, parallel I/O, asynchronous writes
- **1995** — available on: loosely-coupled RS/6000s with HACMP or LAN, and IBM RS/6000 SP MPP systems; parallelizes joins, inserts, updates, deletes, index, backup
- **1995** — large database support: parallel backup/restore on tablespace basis; integration with ADSM for mainframe and AS/400 backup
- **1995** — replication architecture: capture-stage to staging area then apply-stage to destination; log-based; minimal overhead; operates in virtual isolation
- **1995** — replication interval: supports time-interval-based replication (e.g., hourly or daily mass refresh) across DRDA-supporting DBMSs
- **1995** — advanced features: hotspot reduction, load balancing, fan-out, update batching, push-pull for mobile, data compression before transfer
- **1995** — upcoming: upcoming version will deliver update-anywhere robustness to ensure global data consistency
- **1995** — capability: supports distributed joins across relational, IMS, and VSAM; cost-based global optimizer considers networks and I/O speed; provides location/network transparency
- **1995** — accessible from: Visualizer, Lotus Approach, Microsoft Access; IBM VisualAge; Sybase/Powersoft PowerBuilder
- **1995** — synchronous replication: two-phase commit across LAN internetworks and IBM hardware including RS/6000, PCs, AS/400 (OS/400), mainframes (MVS) via CICS, Encina, or Tuxedo TP monitors

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-ibm-db2-common-server' ORDER BY year_observed;
```

