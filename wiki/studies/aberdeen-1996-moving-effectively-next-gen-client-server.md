---
title: "Moving Effectively To Next-Generation Client-Server Development"
slug: aberdeen-1996-moving-effectively-next-gen-client-server
page_type: study
author: "Aberdeen Group"
date: "1996-01-12"
study_type: white-paper
subject_domain: "client-server-development-tools-CADE"
methodology: "industry-analysis, competitive-profiling, field-research, expert-opinion"
importance: medium
importance_rationale: "This white paper captured the mid-1990s industry transition from departmental to enterprise-scale client-server development, identifying the limitations of Visual Basic and PowerBuilder that would drive the next wave of development tool adoption. The CADE evaluation framework was substantive, though the study's vendor-sponsored nature (Gupta) limits its independence."
relevance: low
relevance_rationale: "The specific products (Centura, SQLWindows, PowerBuilder) are largely obsolete. However, the scalability challenges Aberdeen described — application partitioning, deployment automation, repository-based development, 3-tier architecture — directly anticipate modern cloud-native and microservices concerns."
prescience: medium
prescience_rationale: "Aberdeen's prediction that Visual Basic and PowerBuilder shops would face serious scalability constraints proved accurate. However, the resolution was not Centura/Gupta (which was acquired by Unify 2006, then OpenText 2015) but rather Java EE, .NET, and eventually cloud-native frameworks that obviated the CADE category entirely."
license: CC-BY-4.0
tier: 2
entity_count: 10
tech_count: 8
obs_count: 30
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Moving Effectively To Next-Generation Client-Server Development

> Aberdeen Group white paper, sponsored by Gupta Technologies, argues that first-generation client-server application development environments (CADEs) such as Visual Basic and PowerBuilder are 'topping out' and recommends immediate adoption of next-generation CADEs. The study provides an evaluation framework for next-generation CADE selection and positions Gupta's Centura product as the leading choice for organizations migrating from first-generation toolsets.

**Author:** Aberdeen Group · **Date:** 1996-01-12 · **Type:** white-paper
**Importance:** medium — *This white paper captured the mid-1990s industry transition from departmental to enterprise-scale client-server development, identifying the limitations of Visual Basic and PowerBuilder that would drive the next wave of development tool adoption. The CADE evaluation framework was substantive, though…*
**Prescience:** medium — *Aberdeen's prediction that Visual Basic and PowerBuilder shops would face serious scalability constraints proved accurate. However, the resolution was not Centura/Gupta (which was acquired by Unify 2006, then OpenText 2015) but rather Java EE, .NET, and eventually cloud-native frameworks that obviat…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[borland|Borland International (Delphi)]]
- [[forte-software|Forte Software]]
- [[gupta-technologies|Gupta Technologies]]
- [[microsoft|Microsoft Corporation]]
- [[oracle-corporation|Oracle Corporation]]
- [[powersoft-sybase|Sybase/Powersoft (PowerBuilder)]]
- [[rational-software|Rational Software (Rational Rose)]]
- [[symantec|Symantec (Cafe/Visual Cafe)]]
- [[texas-instruments-ti|Texas Instruments (Information Engineering Facility)]]

## Technologies (8)

- [[data-warehousing|Data Warehousing]]
- [[gupta-centura|Gupta Centura (Team Developer)]]
- [[java|Java / Intranet Development]]
- [[powerbuilder|Powersoft/Sybase PowerBuilder]]
- [[sqlwindows|Gupta SQLWindows]]
- [[three-tier-architecture|3-Tier Client-Server Architecture]]
- [[tp-monitor|TP Monitor (Tuxedo/Encina/CICS)]]
- [[visual-basic|Microsoft Visual Basic]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-moving-effectively-next-gen-client-server' ORDER BY year_observed;
```

