---
title: "Object Databases Such As O2 ODMG: Time To Take A Second Look"
slug: 1997-object-databases-such-as-o2-odmg--t-c98c72
page_type: study
author: "Wayne Kernochan / Aberdeen Group"
date: "1997-01-01"
study_type: Product Viewpoint (Abstract)
subject_domain: "Database Technology / Object-Oriented Systems"
methodology: "Analyst product evaluation; market analysis"
importance: low
importance_rationale: "Documents Aberdeen's recommendation to mainstream object databases at a pivotal moment when OODBMSs still held promise — before relational and object-relational databases ultimately dominated. O2 Technology was acquired by Informix in 1998 and the technology absorbed into IBM's portfolio."
relevance: low
relevance_rationale: "Relevant to NoSQL and document database trends that emerged in the 2000s and to ongoing debates about polyglot persistence. The use cases Aberdeen identified — complex data, Internet applications, rapid schema change — were ultimately addressed by document stores and object-relational mapping rather than pure OODBMSs."
prescience: low
prescience_rationale: "Aberdeen was correct that complex data and Internet applications needed better than pure relational models — prescient about the problem space. However the solution path through ODMG-compliant OODBMSs proved incorrect; the market went to object-relational (Oracle IBM) and eventually NoSQL document databases."
license: CC-BY-4.0
tier: 2
entity_count: 4
tech_count: 5
obs_count: 12
tags: [type/study, importance/low, prescience/low, decade/1990s]
source_csv: master_studies.csv
---

# Object Databases Such As O2 ODMG: Time To Take A Second Look

> Argues that IS buyers should reconsider object databases and OODBMSs given advancing scalability and Internet-driven demand for complex data. Uses O2 Technology's O2 ODMG Database System as a leading example. Identifies advantages for complex-data support in data marts, multimedia Internet applications, and rapidly-changing application environments. Recommends factoring object databases into a wider range of buying decisions beyond traditional CAD/CAM niches.

**Author:** Wayne Kernochan / Aberdeen Group · **Date:** 1997-01-01 · **Type:** Product Viewpoint (Abstract)
**Importance:** low — *Documents Aberdeen's recommendation to mainstream object databases at a pivotal moment when OODBMSs still held promise — before relational and object-relational databases ultimately dominated. O2 Technology was acquired by Informix in 1998 and the technology absorbed into IBM's portfolio.*
**Prescience:** low — *Aberdeen was correct that complex data and Internet applications needed better than pure relational models — prescient about the problem space. However the solution path through ODMG-compliant OODBMSs proved incorrect; the market went to object-relational (Oracle IBM) and eventually NoSQL document d…*

## Entities (4)

- [[ENT-O2-001|O2 Technology]]
- [[ENT-O2-002|Informix Corporation]]
- [[ENT-O2-003|IBM]]
- [[ENT-O2-004|Object Data Management Group (ODMG)]]

## Technologies (5)

- [[TECH-O2-001|O2 ODMG Database System]]
- [[TECH-O2-002|ODMG Standard (Object Database Management Group)]]
- [[TECH-O2-003|Object-Oriented Database Management System (OODBMS)]]
- [[TECH-O2-004|Relational Database Management System (RDBMS)]]
- [[TECH-O2-005|Object Query Language (OQL)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-object-databases-such-as-o2-odmg--t-c98c72' ORDER BY year_observed;
```

