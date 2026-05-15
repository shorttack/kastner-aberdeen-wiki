---
title: "Oracle8: The Database For Network Computing"
slug: 1997-oracle8-the-database-for-network-computing-674c9d
page_type: study
author: "Peter S. Kastner"
date: "1997-12-10"
study_type: market-study
subject_domain: "database-technology"
methodology: "industry-analysis, competitive-profiling, expert-opinion, benchmarking"
importance: high
importance_rationale: "Peter S. Kastner's Oracle8 assessment was published just after Oracle8's June 1997 GA release and provided one of the first independent analyst evaluations of the object-relational database model; widely cited in the Oracle community and influential in enterprise database procurement decisions of 1997-1999."
relevance: high
relevance_rationale: "The three-dimensional database evaluation framework (scalability/flexibility/manageability) articulated in this study remains the dominant framework used to evaluate modern cloud databases; Oracle8's object-relational innovations evolved directly into modern Oracle Database and influenced PostgreSQL's type system."
prescience: high
prescience_rationale: "Kastner predicted Oracle would add further object-relational features and improve object access performance over 1-2 years; this proved correct as Oracle8i (1998) delivered Java VM integration, and subsequent versions progressively enhanced object-relational capabilities through Oracle9i and beyond."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 9
obs_count: 22
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Oracle8: The Database For Network Computing

> This 1997 Aberdeen Group profile authored by Peter S. Kastner evaluates Oracle8, the then-upcoming next generation of the Oracle database. Kastner argues that Oracle8 defines a new standard for network computing databases with its three-dimensional design framework: scalability (10,000+ users, hundreds of terabytes), flexibility (object-relational technology and extensible data cartridges), and manageability (partition-based backup/recovery, automated failover). The study positions Oracle8 as a foundational component of Oracle's Network Computing Architecture and predicts continued evolution of object-relational capabilities over 1-2 years.

**Author:** Peter S. Kastner · **Date:** 1997-12-10 · **Type:** market-study
**Importance:** high — *Peter S. Kastner's Oracle8 assessment was published just after Oracle8's June 1997 GA release and provided one of the first independent analyst evaluations of the object-relational database model; widely cited in the Oracle community and influential in enterprise database procurement decisions of 19…*
**Prescience:** high — *Kastner predicted Oracle would add further object-relational features and improve object access performance over 1-2 years; this proved correct as Oracle8i (1998) delivered Java VM integration, and subsequent versions progressively enhanced object-relational capabilities through Oracle9i and beyond.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[bristol-myers|Bristol-Myers Squibb]]
- [[microsoft|Microsoft Corporation]]
- [[oracle-corporation|Oracle Corporation]]
- [[pacific-bell|Pacific Bell]]

## Technologies (9)

- [[advanced-queuing|Oracle Advanced Queuing]]
- [[corba|CORBA]]
- [[java|Java]]
- [[object-relational-db|Object-Relational Database]]
- [[oracle-nca|Oracle Network Computing Architecture]]
- [[oracle7|Oracle7 Database]]
- [[oracle8|Oracle8 Database]]
- [[oracle8i|Oracle8i Database]]
- [[plsql|PL/SQL]]

## Key observations (top 25)

- **1997** — key-criteria-scalability: Database must scale in users, database size, and performance; Oracle8 targets all three
- **1997** — key-criteria-flexibility: Database must deliver support for rapid change via relational and object-relational data models
- **1997** — key-criteria-manageability: Database must cut deployment/administration/maintenance costs; Oracle8 targets with partitioning and automated backup
- **1997** — per-user-memory-reduction: Oracle8 reduces per-user memory requirements by approximately 50% vs Oracle7 via pooled and multiplexed connections
- **1997** — max-users-per-node: Oracle8 supports more than 10,000 end users per node; dramatic increase over Oracle7
- **1997** — star-query-performance: Oracle8 improves performance on 2.7-million row star query by order of magnitude over Oracle 7.3, two orders of magnitude over Oracle 7.0
- **1997** — replication-speed: Oracle8 parallelized replication delivers speeds an order of magnitude faster in tests
- **1997** — beta-program-size: Oracle8 underwent 10-month beta test with nearly 100 partners and over 1,000 customers
- **1997** — upgrade-path: Upgrade from Oracle7 to Oracle8 is relatively fast and simple; existing applications work without change
- **1997** — object-relational-value: Object-relational value lies in increased developer productivity via richer data model, not primarily in multimedia
- **1997** — data-cartridges: Oracle8 extensibility mechanism allows ISV/IS-created data cartridges to access core RDBMS functions including query optimizer and indexing
- **1997** — advanced-queuing: Oracle8 Advanced Queuing places messaging in the database engine, reducing middleware complexity and improving performance
- **1997** — partitioning: Oracle8 table partitioning allows dividing tables into smaller chunks for manageability, performance, and reduced downtime
- **1997** — multimedia-support: Oracle8 adds support for images and time-series data beyond Oracle7's text/spatial/video; plus extensibility for custom types
- **1996** — oracle7-multimedia-customer: Bristol Myers cited as large-scale real-world customer using Oracle7 multimedia capabilities
- **1996** — oracle7-spatial-customer: Pacific Bell cited as large-scale real-world customer using Oracle7 spatial data capabilities
- **1997** — object-relational-evolution: Oracle will add further object-relational features, further integrate relational and object data, and improve object-access performance over next 1-2 years
- **1998** — object-relational-evolution: Oracle8i (1998) delivered Java VM integration, XML support, and further OR enhancements; Oracle9i (2001) added RAC and XML DB; predictions proved substantially correct
- **1997** — psk-overall-rating: Aberdeen/Kastner concludes Oracle8 is 'powerful and profound' — sets new standard for handling exceptionally broad range of customer needs
- **1997** — nca-standards: Oracle NCA incorporates major standards including Java and CORBA with open interfaces
- **1997** — java-future-support: Java access to Oracle8 object data to be supported in Oracle 8.1
- **1997** — max-data-volume: Oracle8 can support hundreds of terabytes of data

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-oracle8-the-database-for-network-computing-674c9d' ORDER BY year_observed;
```

