---
title: "Safeway Damages Report: Expert Opinion on Consonus Data Center Incident"
slug: safeway-damages-report-draft-b502f4
page_type: study
author: "Hugh Bishop with Peter Kastner"
date: "2003-12-01"
study_type: expert-report
subject_domain: "it-disaster-recovery"
methodology: "document-review, field-research, benchmarking"
importance: high
importance_rationale: "Provides detailed expert valuation methodology for enterprise data warehouse disaster damage; rare documented case of Teradata system failure analysis."
relevance: medium
relevance_rationale: "Disaster recovery valuation frameworks and business continuity assessment methods remain applicable; specific Teradata hardware details are dated."
prescience: high
prescience_rationale: "Correctly assessed Teradata's strategic importance to retail analytics, which grew significantly; data warehouse as mission-critical asset prediction validated."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 8
obs_count: 40
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Safeway Damages Report: Expert Opinion on Consonus Data Center Incident

> Expert damages opinion by Aberdeen Group (Hugh Bishop with Peter Kastner) analyzing the impact of a February 2002 fire suppression system discharge at the Consonus data center on Safeway Inc.'s 40-node Teradata data warehouse system. Assesses hardware damage valuation, business interruption costs, data recovery efforts, and the strategic importance of Teradata to Safeway's retail operations.

**Author:** Hugh Bishop with Peter Kastner · **Date:** 2003-12-01 · **Type:** expert-report
**Importance:** high — *Provides detailed expert valuation methodology for enterprise data warehouse disaster damage; rare documented case of Teradata system failure analysis.*
**Prescience:** high — *Correctly assessed Teradata's strategic importance to retail analytics, which grew significantly; data warehouse as mission-critical asset prediction validated.*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[albertsons|Albertsons Companies]]
- [[consonus|Consonus Inc.]]
- [[dewsnup-king-olsen|Dewsnup King & Olsen]]
- [[informix|Informix Corporation]]
- [[kroger|The Kroger Co.]]
- [[ncr-teradata|NCR Corporation / Teradata Division]]
- [[safeway|Safeway Inc.]]
- [[sun-microsystems|Sun Microsystems]]
- [[walmart|Walmart Inc.]]

## Technologies (8)

- [[data-warehouse-appliance|Data Warehouse Appliance]]
- [[fire-suppression|FM-200 Fire Suppression System]]
- [[ibm-mainframe|IBM Mainframe]]
- [[informix-db|Informix Database]]
- [[operational-data-store|Operational Data Store (ODS)]]
- [[sun-solaris|Sun Solaris / SPARC]]
- [[teradata-dw|Teradata Data Warehouse]]
- [[trickle-feed|Trickle Feed (Safeway Custom)]]

## Key observations (top 25)

- **2002** — annual-revenue: $1.226 billion Teradata division revenue
- **2002** — installed-base: Approximately 700 Teradata systems installed worldwide; ~100 new systems per year
- **2002** — system-configuration: 40-node Teradata system; grown from original 28 nodes (1997) to 34 (2000) to 40 (2002)
- **2002** — hardware-investment: $16.7 million total Teradata hardware investment ($10.2M original + $6.5M expansions)
- **2002** — application-portfolio: 25+ applications in 3 classes: Class 1 (static/ad-hoc); Class 2 (daily batch); Class 3 (ODS real-time)
- **2002** — incident-date: FM-200 fire suppression system discharged on February 22 2002 at Consonus Portland data center
- **2002** — downtime-hours: 144+ hours of complete system downtime following the fire suppression discharge
- **2002** — degraded-hours: 111 hours of degraded performance after initial recovery
- **2002** — staff-recovery-hours: 359.5 person-hours of IT staff time for incident recovery
- **2002** — application-rewrites: Multiple applications required partial or complete rewrites after data corruption from the incident
- **2002** — delayed-rollouts: Planned application rollouts delayed by the incident — opportunity cost beyond direct damages
- **2002** — data-confidence-risk: Risk of permanent loss of data confidence — users may not trust data warehouse outputs after corruption event
- **2002** — data-loss-risk: Risk of undetected data loss — some corrupted data may not be identified until much later
- **2002** — business-interruption-risk: Business interruption during recovery — grocery retail operations depend on daily/weekly data cycles
- **2002** — ncr-maintenance-risk: Risk of losing NCR maintenance coverage — incident may have voided warranty or maintenance terms
- **2002** — evolution-inability: Inability to evolve the system during recovery period — platform frozen while competitors advanced
- **2003** — direct-recovery-cost: $1,311,542.76 in direct recovery costs (labor; hardware repair/replacement; emergency services)
- **2003** — direct-replacement-cost: $11,742,608.18 in direct replacement costs (new hardware; new software; migration; installation)
- **2003** — business-interruption-cost: $2,939,903.00 in business interruption damages (lost productivity; delayed projects; opportunity cost)
- **2003** — total-damages: $15,994,053.94 total damages claimed (direct recovery + direct replacement + business interruption)
- **2000** — platform-migration: Safeway migrated from Informix/Sun to Teradata due to Informix performance limitations and Sun hardware constraints
- **2001** — acquisition: Informix acquired by IBM in 2001 for $1B — validating Safeway's decision to migrate away
- **2010** — acquisition: Sun Microsystems acquired by Oracle in 2010 for $7.4B — SPARC platform eventually discontinued
- **2007** — spinoff: Teradata spun off from NCR as independent company in 2007; became publicly traded on NYSE
- **2015** — acquisition: Safeway acquired by Albertsons/Cerberus Capital Management in 2015 for $9.4B

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'safeway-damages-report-draft-b502f4' ORDER BY year_observed;
```

