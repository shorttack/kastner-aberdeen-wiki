---
title: "IBM Information Integration Family"
slug: 1997-ibm-information-integration-family--29351c
page_type: study
author: "Aberdeen Group"
date: "1997-06-04"
study_type: Profile
subject_domain: "Data Integration / Network Computing"
methodology: "Vendor product analysis with technology assessment"
importance: high
importance_rationale: "The study documents the emergence of data federation and replication middleware as enterprise imperatives at the dawn of the Internet era. DataJoiner's federated query model directly anticipates IBM InfoSphere Federation Server and later Apache Drill/Presto-style query engines. The insight that enterprises need to reuse middleware across recurring data-integration projects — rather than build one-offs — is foundational to modern ELT/ETL platforms."
relevance: high
relevance_rationale: "Highly relevant to contemporary data integration, ETL/ELT, and data mesh discussions. The 'data archipelago' metaphor and the need to federate heterogeneous data sources anticipate modern data lakehouse architecture. DataPropagator's log-based CDC (Change Data Capture) approach is now the dominant pattern in tools like Debezium and AWS DMS. Net.data's web-to-database dynamic query pattern anticipated REST APIs and GraphQL."
prescience: high
prescience_rationale: "Aberdeen accurately predicted: (1) DataPropagator would add further traditional RDBMS scalability technologies (confirmed — evolved into DB2 Replication Services); (2) a Visual Programming Environment for rapid development would be added (partially confirmed via IBM Rational tools); (3) administrative tools would improve toward near-lights-out ease of use (confirmed — IBM InfoSphere CDC and modern cloud tools). The prediction that information integration products would be reused across wider var…"
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 6
obs_count: 25
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# IBM Information Integration Family

> Aberdeen Group evaluates IBM's Information Integration product family — DataJoiner (heterogeneous federated query), DataPropagator (log-based replication), Net.data (web-to-database middleware), and MQSeries — assessing their ability to coordinate data across distributed network-computing databases. Aberdeen concludes the family excels in heterogeneity and scalability, and recommends it for enterprises with multiple-supplier database environments.

**Author:** Aberdeen Group · **Date:** 1997-06-04 · **Type:** Profile
**Importance:** high — *The study documents the emergence of data federation and replication middleware as enterprise imperatives at the dawn of the Internet era. DataJoiner's federated query model directly anticipates IBM InfoSphere Federation Server and later Apache Drill/Presto-style query engines. The insight that ente…*
**Prescience:** high — *Aberdeen accurately predicted: (1) DataPropagator would add further traditional RDBMS scalability technologies (confirmed — evolved into DB2 Replication Services); (2) a Visual Programming Environment for rapid development would be added (partially confirmed via IBM Rational tools); (3) administrati…*

## Entities (6)

- [[ent-iif-001|IBM Corporation]]
- [[ent-iif-002|Aberdeen Group]]
- [[ent-iif-003|Oracle Corporation]]
- [[ent-iif-004|Informix Corporation]]
- [[ent-iif-005|Sybase Inc.]]
- [[ent-iif-006|Microsoft Corporation]]

## Technologies (6)

- [[tech-iif-001|DataJoiner]]
- [[tech-iif-002|DataPropagator (Relational and NonRelational)]]
- [[tech-iif-003|Net.data (DB2 WWW Connection)]]
- [[tech-iif-004|MQSeries]]
- [[tech-iif-005|DB2 (Database Server)]]
- [[tech-iif-006|DataRefresher]]

## Key observations (top 25)

- **1997** — DataJoiner supported databases: DB2, Oracle, Informix, Sybase, Microsoft SQL Server, IMS, VSAM
- **1997** — DataPropagator replication architecture: Log-based capture to staging area then apply to destination; minimizes production database impact
- **1997** — DataPropagator heterogeneous support: DB2-to-Sybase, DB2-to-Oracle, Oracle-to-DB2, Oracle-to-Oracle confirmed customer deployments
- **1997** — Net.data web-database interaction: Dynamic HTML/SQL macros for browser-to-backend-database interaction without bypassing web server
- **1997** — Net.data variable substitution: State management via variable substitution for OLTP transactions across web connections
- **1997** — Data warehousing lesson: Full enterprise data integration is 'difficult if not impossible'; focused data marts achieve competitive advantage
- **1997** — Data archipelago proliferation: Enterprises facing proliferating data archipelagoes requiring ever-faster merging of larger data streams
- **1997** — Middleware reuse imperative: Key value: reuse information integration middleware across recurring projects vs. one-off builds
- **1997** — DataJoiner SQL-3 support planned: 1997 plans to add SQL-3 standard support and mimic advanced operations on DBMSs lacking them
- **1997** — DataJoiner location transparency: Applications do not change when underlying architecture changes — open-server API features
- **1997** — DataJoiner future direction: Will enable 'write-once' apps accessing multiple legacy backend databases over Intranet
- **2002** — DataJoiner superseded: DataJoiner absorbed into IBM DB2 Information Integrator (~2002); later InfoSphere Federation Server
- **1997** — DataPropagator scalability evolution: Will add further support for traditional RDBMS scalability technologies such as cursors and governors
- **2005** — DataPropagator lifecycle outcome: Absorbed into IBM DB2 Replication; log-based CDC pattern validated by entire industry
- **1997** — Net.data VPE development: Visual Programming Environment due next year (1998) for rapid development; further Java capabilities
- **2000** — Net.data superseded: Net.data superseded by WebSphere Application Server and JSP/servlet model circa 2000-2002
- **1997** — Log-based CDC as replication pattern: DataPropagator's log-based architecture will deliver performance and isolation advantages in network computing
- **2020** — Log-based CDC industry dominance: Log-based CDC became dominant pattern for enterprise data replication across all major cloud and on-premises tools
- **1997** — DB2 role in information integration: DB2 serves as hub for heterogeneous replication when combined with DataJoiner and DataPropagator
- **1997** — Informix as DataJoiner target: Informix named as supported DataJoiner join target via open-server operations
- **1997** — DataPropagator mobile replication: Supports push from laptop or pull from central server for mobile/laptop replication
- **1997** — Information integration market positioning: Targets enterprises with multiple-supplier databases; positions reuse as competitive differentiator
- **1997** — Aberdeen recommendation on information integration: Outstanding example of IBM winning by the details; majority of enterprises should evaluate
- **1997** — Sybase as DataJoiner target: Sybase SQL Server supported as DataJoiner target; PowerBuilder can invoke DataJoiner
- **1997** — MQSeries role in information integration: Enables data movement and application location independence as part of information integration

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-ibm-information-integration-family--29351c' ORDER BY year_observed;
```

