---
title: "Live Object Caching: High-Performance for Object/Relational Applications"
slug: aberdeen-1996-live-object-caching-high-performance
page_type: study
author: "Aberdeen Group"
date: "1996-08-13"
study_type: market-study
subject_domain: "object-relational-database-middleware"
methodology: "industry-analysis, competitive-profiling, field-research, expert-opinion"
importance: high
importance_rationale: "This study addressed a critical and largely unresolved technical problem at the frontier of mid-1990s software architecture: combining the emerging object-oriented paradigm with the dominant relational database infrastructure. Aberdeen's formulation of 'live object caching' as a distinct strategy was an early articulation of what would become a standard ORM pattern."
relevance: medium
relevance_rationale: "The object/relational mapping problem Aberdeen described remains fundamental to modern software architecture; frameworks such as Hibernate, JPA, and Django ORM are its direct descendants. The specific vendor (Persistence Software, acquired by Progress Software 2004) is historical, but the architectural concepts are directly applicable today."
prescience: high
prescience_rationale: "Aberdeen correctly predicted that OO/relational hybrid architecture would dominate and that pure object databases (ODBMS) would fail to achieve mainstream adoption — both proved exactly correct. The prediction that Java support would be critical to Persistence's future aligned with Enterprise JavaBeans incorporating Persistence technology in 1998."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 9
obs_count: 28
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Live Object Caching: High-Performance for Object/Relational Applications

> Aberdeen Group analyzes the performance challenge of combining object-oriented application code with relational databases, defining 'live object caching' as the solution to object-relational impedance mismatch. The study profiles Persistence Software's Object Builder and Object Server as the leading tools enabling commercial object/relational production systems, and recommends that IS organizations adopting OO development evaluate live object caching before proceeding.

**Author:** Aberdeen Group · **Date:** 1996-08-13 · **Type:** market-study
**Importance:** high — *This study addressed a critical and largely unresolved technical problem at the frontier of mid-1990s software architecture: combining the emerging object-oriented paradigm with the dominant relational database infrastructure. Aberdeen's formulation of 'live object caching' as a distinct strategy wa…*
**Prescience:** high — *Aberdeen correctly predicted that OO/relational hybrid architecture would dominate and that pure object databases (ODBMS) would fail to achieve mainstream adoption — both proved exactly correct. The prediction that Java support would be critical to Persistence's future aligned with Enterprise JavaBe…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[att|AT&T]]
- [[forte-software|Forte Software]]
- [[informix|Informix]]
- [[object-design|Object Design, Inc.]]
- [[oracle-corporation|Oracle Corporation]]
- [[persistence-software|Persistence Software, Inc.]]
- [[rational-software|Rational Software]]
- [[sun-microsystems|Sun Microsystems]]
- [[sybase|Sybase]]

## Technologies (9)

- [[corba-orb|CORBA / Object Request Broker (ORB)]]
- [[cplusplus|C++]]
- [[java|Java]]
- [[odbms|Object DBMS (ODBMS)]]
- [[persistence-object-builder|Persistence Object Builder]]
- [[persistence-object-server|Persistence Object Server]]
- [[persistence-transapp-server|Persistence TransApp Server]]
- [[rdbms|Relational DBMS (general)]]
- [[tp-monitor|TP Monitor (transaction processing monitor)]]

## Key observations (top 25)

- **1996** — Persistence Object Builder introduction year and development time reduction: Introduced 1991; reduces total build time for new C++ applications by average 30%
- **1996** — RDBMS engines supported by Persistence Object Builder: Informix, Oracle, Sybase, SQL Server, ODBC; C++ compilers: CenterLine ObjectCenter, HP SoftBench, IBM C++, Sun SparcWorks, Microsoft Visual C++
- **1996** — High-profile Persistence deployment: AT&T ASOS initiative uses Persistence; resold by Sybase and SunSoft
- **1996** — ODBMS market failure assessment: Poor marketing and lack of value proposition relegated ODBMS to few narrow markets; failed to capture significant commercial applications share
- **1996** — RDBMS dominant investment trajectory: Market continued to invest in relational technology; includes database engines, application portfolio, and programmer skillsets worldwide
- **1996** — Persistence Object Server current limitation: Allows only one client per application/object cache; TransApp Server (late 1996) will resolve multiple-client access
- **1996** — Persistence Java support roadmap: Plans to add Java support by end of 1996
- **1996** — ORB compatibility with Persistence: Persistence works with Iona Orbix, SunSoft NEO, Visigenic, and Expersoft ORBs
- **1996** — Live object caching criteria: Highly interdependent data: Objects where variables are inherently related to other complementary objects (e.g., flight crew schedules, aircraft availability)
- **1996** — Live object caching criteria: Infrequent controlled changes: Objects updated weekly/daily rather than second-by-second; frequently accessed/read, rarely updated/written
- **1996** — Live object caching criteria: Used in most transactions: Objects involved in majority of transactions across customers, suppliers, internal operations
- **1996** — Live object caching criteria: Used by multiple applications: Objects reused across billing, inventory, and customer support systems (e.g., product/service objects)
- **1996** — OO advantage: Business process alignment: Objects combine functionality and data; business rules embedded directly; consistent enforcement across enterprise
- **1996** — OO advantage: Accelerated application enhancement: Component-based architecture eliminates spaghetti code; single change to shared object updates multiple applications
- **1996** — OO advantage: Distributed systems partitioning: Object modularity enables deployment of data and functionality closer to end-user; major motivation for OO transition per Aberdeen field research
- **1996** — OO advantage: Internet architecture: Next-gen Internet/intranet applications will be OO; Java (de facto standard for internet apps) is an object language; multimedia mandate objects
- **1996** — Object Design competitive position vs. Persistence: Requires purchase of ODBMS as part of solution; less resource investment in object caching than Persistence
- **1996** — Forte Software competitive position vs. Persistence: All-in-one solution; used successfully but lacks openness of Persistence; does not support pure object programming model
- **1996** — Aberdeen assessment of Persistence competitive position: Persistence is 'the preeminent provider of tools that enable live object caching'; has distinct advantages over alternatives
- **1996** — Aberdeen architecture prediction: Architecture of the future will combine object-oriented application code running on top of database engines from the existing relational suppliers
- **1996** — Prediction: Live object caching commercial viability: Live object caching is critical breakthrough making object/relational applications viable for commercial systems; will be increasingly important factor in next-gen strategic business applications
- **1996** — Prediction: ODBMS will not achieve mainstream adoption: ODBMS relegated to few narrow markets; relational investment too strong; new solutions will layer OO code on relational engines
- **1996** — Prediction: Persistence Java and EJB relevance: Aberdeen expects additional partnerships for Persistence; Java support planned by end 1996 seen as important
- **2005** — Outcome: ODBMS market trajectory: ODBMS remained niche; major ODBMS vendors (Objectivity, Versant, Poet) never achieved commercial mainstream; relational databases with ORM layers dominated
- **2004** — Outcome: Persistence Software fate and EJB: Sun licensed Persistence technology 1998 for Enterprise JavaBeans standard; Persistence IPO on NASDAQ (PRSW) in 1999; acquired by Progress Software for $16M in 2004

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-live-object-caching-high-performance' ORDER BY year_observed;
```

