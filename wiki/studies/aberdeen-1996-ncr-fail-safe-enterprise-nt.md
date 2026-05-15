---
title: "NCR: Finally a Fail-Safe Choice For Enterprise NT"
slug: aberdeen-1996-ncr-fail-safe-enterprise-nt
page_type: study
author: "Aberdeen Group"
date: "1996-05-25"
study_type: market-study
subject_domain: "enterprise-NT-OLTP"
methodology: "field-research, industry-analysis, competitive-profiling"
importance: high
importance_rationale: "Published at a pivotal moment when Windows NT was challenging Unix and mainframes for enterprise OLTP workloads; NCR (formerly AT&T GIS) was the leading enterprise NT integrator and this Aberdeen Viewpoint shaped early-adopter decisions in 1996."
relevance: medium
relevance_rationale: "NT-specific product details are obsolete, but the study's framework for evaluating RAS (Reliability, Availability, Serviceability) requirements for OS platform transitions remains applicable to modern cloud/edge migration decisions."
prescience: high
prescience_rationale: "Aberdeen's prediction that NT SMP scalability would reach 8-12 CPUs by mid-1997 proved accurate with NT Server 4.0 Enterprise Edition and SQL Server 6.5/7.0; Windows NT's enterprise dominance over Unix for OLTP by 2000 also materialized."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 7
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# NCR: Finally a Fail-Safe Choice For Enterprise NT

> Aberdeen Group evaluates NCR's Windows NT Server products for mission-critical OLTP applications based on user interviews with early adopters. The study finds that NCR's LifeKeeper, TOP END, and WorldMark servers address NT's enterprise weaknesses in reliability, scalability, and manageability. Aberdeen concludes that NCR has delivered on its 1994 promise and is a 'fail-safe choice' for NT-based OLTP deployment in retail, finance, telecom, and transportation industries.

**Author:** Aberdeen Group · **Date:** 1996-05-25 · **Type:** market-study
**Importance:** high — *Published at a pivotal moment when Windows NT was challenging Unix and mainframes for enterprise OLTP workloads; NCR (formerly AT&T GIS) was the leading enterprise NT integrator and this Aberdeen Viewpoint shaped early-adopter decisions in 1996.*
**Prescience:** high — *Aberdeen's prediction that NT SMP scalability would reach 8-12 CPUs by mid-1997 proved accurate with NT Server 4.0 Enterprise Edition and SQL Server 6.5/7.0; Windows NT's enterprise dominance over Unix for OLTP by 2000 also materialized.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[att-gis|AT&T Global Information Solutions (AT&T GIS)]]
- [[microsoft|Microsoft Corporation]]
- [[ncr-corporation|NCR Corporation]]
- [[teradata|Teradata Corporation]]

## Technologies (7)

- [[microsoft-sql-server|Microsoft SQL Server]]
- [[ncr-lifekeeper|NCR LifeKeeper]]
- [[ncr-smp-utilization-manager|NCR SMP Utilization Manager for NT]]
- [[ncr-top-end|NCR TOP END]]
- [[ncr-worldmark|NCR WorldMark Servers]]
- [[teradata-data-warehouse|Teradata Data Warehouse]]
- [[windows-nt-server|Windows NT Server]]

## Key observations (top 25)

- **1996** — NCR NT enterprise strategy: RAS-augmentation: add enterprise-grade HA/clustering/TP-monitor on top of NT
- **1996** — LifeKeeper failover capability: Automatic failover in 2 seconds to 5 minutes; up to 3-node NT cluster
- **1996** — TOP END transaction routing: Redirects client transactions around failed servers, apps, or network nodes
- **1995** — RAD schedule reduction: 20-25% reduction in OLTP application deployment time; some sites reported 50%
- **1996** — SQL Server cost advantage vs alternatives: Microsoft SQL Server 6.5 on NT up to 90% less costly than Unix/OpenVMS/MVS RDBMS alternatives
- **1996** — NT SMP scalability roadmap: NT/SQL Server to scale to 8 CPUs with NT Server 4.0 (fall 1996); 12-16 CPUs by mid-1997
- **1997** — NT SMP scalability achieved: Windows NT Server 4.0 Enterprise Edition (Sept 1997) supported 8-way SMP clustering; SQL Server 7.0 (1998) supported 8+ CPUs
- **1996** — SMP Utilization Manager release: NCR to introduce SMP Utilization Manager for NT in 1996 for 16-way WorldMark systems
- **1997** — SMP Utilization Manager actual delivery: NCR delivered SMP management tools; absorbed into later Teradata and NT product lines; specific 'Utilization Manager' branding not widely documented post-1997
- **1996** — NT data mart market entry: NCR to provide NT-based data mart solutions starting with NT Server 4.0; data-mart-up/down routing to Teradata
- **1999** — NCR data mart market outcome: NCR/Teradata became leading enterprise data warehouse platform in late 1990s; NT-based data marts proliferated broadly as predicted
- **1996** — Aberdeen overall verdict on NCR NT: NCR is an 'experienced, fail-safe choice for NT-based OLTP application deployments'
- **1994** — AT&T GIS enterprise NT commitment announcement: August 1994: AT&T GIS announced plan to bring NT into enterprise with scalability, manageability, reliability, serviceability features
- **1996** — NT OLTP benefit factor 1: Time to market: IT decision makers primary motivation: NT enables faster competitive response than legacy mainframe
- **1996** — NT OLTP benefit factor 2: Service level agreements: NCR LifeKeeper/TOP END enabled IS to commit to enterprise-grade SLAs, including external customer-facing guarantees
- **1996** — NT OLTP benefit factor 3: Homogeneous environment: IS decision makers sought single standard OS platform across hardware; reduced management complexity
- **1996** — NT OLTP benefit factor 4: Desktop synergy: Business-line managers wanted OLTP on NT to align with desktop Windows; reduced training, OLE object reuse
- **1996** — NCR Microsoft Authorized Consulting Partner status: Aberdeen predicts NCR will become one of select Microsoft Authorized Consulting Partners for NT
- **1998** — NCR Microsoft partnership outcome: NCR became major Microsoft partner for enterprise solutions; Teradata/NT integration was commercially successful through late 1990s
- **1995** — NCR NT/OLTP early adopter industries: Primary: retail, finance, telecommunications, transportation

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-ncr-fail-safe-enterprise-nt' ORDER BY year_observed;
```

