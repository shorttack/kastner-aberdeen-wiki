---
title: "Live Object Caching: High-Performance for Object/Relational Applications"
slug: "study-aberdeen-1996-live-object-caching-high-performance"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-live-object-caching-high-performance"
author: "Aberdeen Group"
date: "1996-08-13"
pub_year: 1996
type: "market-study"
subject_domain: "object-relational-database-middleware"
methodology: "industry-analysis, competitive-profiling, field-research, expert-opinion"
source_file: "1996 Live Object Caching_ High-Performance for Object_Relational Applications tvp.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_3y_enum: ""
prescience_5y_enum: ""
prescience_max: 5.0
prescience_mean: 2.5
prescience_obs_count: 28
---

# Live Object Caching: High-Performance for Object/Relational Applications

> Aberdeen Group analyzes the performance challenge of combining object-oriented application code with relational databases, defining 'live object caching' as the solution to object-relational impedance mismatch. The study profiles Persistence Software's Object Builder and Object Server as the leading tools enabling commercial object/relational production systems, and recommends that IS organizations adopting OO development evaluate live object caching before proceeding.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- Poor marketing and lack of value proposition relegated ODBMS to few narrow markets; failed to capture significant commercial applications share `[ps=5]`
- Market continued to invest in relational technology; includes database engines, application portfolio, and programmer skillsets worldwide `[ps=5]`
- Architecture of the future will combine object-oriented application code running on top of database engines from the existing relational suppliers `[ps=5]`
- ODBMS relegated to few narrow markets; relational investment too strong; new solutions will layer OO code on relational engines `[ps=5]`
- ODBMS remained niche; major ODBMS vendors (Objectivity, Versant, Poet) never achieved commercial mainstream; relational databases with ORM layers dominated `[ps=5]`
- Object/relational mapping became dominant architecture; Hibernate (2001), JPA (2006), ActiveRecord, Django ORM all implement the pattern Aberdeen described `[ps=5]`
- Applications with multiple-reads-to-one-write transaction pattern (many-read:1-write); poor fit for classic 1-read:1-write OLTP (e.g., teller transactions) `[ps=5]`
- Objects involved in majority of transactions across customers, suppliers, internal operations `[ps=4]`
- Objects reused across billing, inventory, and customer support systems (e.g., product/service objects) `[ps=4]`
- Next-gen Internet/intranet applications will be OO; Java (de facto standard for internet apps) is an object language; multimedia mandate objects `[ps=4]`
- Live object caching is critical breakthrough making object/relational applications viable for commercial systems; will be increasingly important factor in next-gen strategic business applications `[ps=4]`
- Aberdeen expects additional partnerships for Persistence; Java support planned by end 1996 seen as important `[ps=4]`
- Objects updated weekly/daily rather than second-by-second; frequently accessed/read, rarely updated/written `[ps=3]`
- Objects combine functionality and data; business rules embedded directly; consistent enforcement across enterprise `[ps=3]`
- Object modularity enables deployment of data and functionality closer to end-user; major motivation for OO transition per Aberdeen field research `[ps=3]`
- Component-based architecture eliminates spaghetti code; single change to shared object updates multiple applications `[ps=2]`
- Requires purchase of ODBMS as part of solution; less resource investment in object caching than Persistence `[ps=2]`
- Persistence is 'the preeminent provider of tools that enable live object caching'; has distinct advantages over alternatives `[ps=2]`
- Introduced 1991; reduces total build time for new C++ applications by average 30% `[ps=0]`
- Informix, Oracle, Sybase, SQL Server, ODBC; C++ compilers: CenterLine ObjectCenter, HP SoftBench, IBM C++, Sun SparcWorks, Microsoft Visual C++ `[ps=0]`
- AT&T ASOS initiative uses Persistence; resold by Sybase and SunSoft `[ps=0]`
- Allows only one client per application/object cache; TransApp Server (late 1996) will resolve multiple-client access `[ps=0]`
- Plans to add Java support by end of 1996 `[ps=0]`
- Persistence works with Iona Orbix, SunSoft NEO, Visigenic, and Expersoft ORBs `[ps=0]`
- Objects where variables are inherently related to other complementary objects (e.g., flight crew schedules, aircraft availability) `[ps=0]`
