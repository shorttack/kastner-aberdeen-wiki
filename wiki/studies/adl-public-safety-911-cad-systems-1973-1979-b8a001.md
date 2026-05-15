---
title: "ADL Public Safety / 911 CAD Systems: Boston, Philadelphia, Minneapolis, Aurora, and St. Petersburg (1973-1979)"
slug: adl-public-safety-911-cad-systems-1973-1979-b8a001
page_type: study
author: "Peter S. Kastner"
date: "2025-08-15"
study_type: employer-record
subject_domain: "employer/arthur-d-little/public-safety-CAD"
methodology: "oral-history, document-review, industry-analysis"
importance: high
importance_rationale: "First-person primary-source documentation of an under-recorded chapter of public-safety computing history; identifies Kastner as the technical lead on four early municipal CAD installations and the St. Petersburg IBM-mainframe dispatch design."
relevance: high
relevance_rationale: "Public-safety CAD architecture, 911 dispatch fault-tolerance, and federal grant-funded municipal IT modernization remain active topics; the Boston system was replaced with a $17M modernization in 2014 and again procured in 2024-2025."
prescience: not-applicable
prescience_rationale: "Memoir / employer-record content; no forward predictions made."
license: CC-BY-4.0
tier: 1
entity_count: 20
tech_count: 9
obs_count: 23
tags: [type/study, importance/high, prescience/not-applicable, decade/2020s]
source_csv: master_studies.csv
---

# ADL Public Safety / 911 CAD Systems: Boston, Philadelphia, Minneapolis, Aurora, and St. Petersburg (1973-1979)

> Kastner's role at Arthur D. Little Systems (ADLS) on the federally-funded LEAA-grant 911 computer-aided dispatch (CAD) systems built in the 1970s. ADLS designed a fault-tolerant dual-Data-General-Eclipse minicomputer dispatch architecture first deployed in Boston, then migrated to Philadelphia, Minneapolis, and Aurora CO. As vendor support manager, Kastner led hardware configuration, procurement, burn-in, and installation for all four cities. He separately led ADL's design of the St. Petersburg FL 911 dispatch on the city's IBM 370/135 with CICS, recommending and modifying the Hampton Roads VA dispatch system for transfer.

**Author:** Peter S. Kastner · **Date:** 2025-08-15 · **Type:** employer-record
**Importance:** high — *First-person primary-source documentation of an under-recorded chapter of public-safety computing history; identifies Kastner as the technical lead on four early municipal CAD installations and the St. Petersburg IBM-mainframe dispatch design.*
**Prescience:** not-applicable — *Memoir / employer-record content; no forward predictions made.*

## Entities (20)

- [[adl-public-safety-group|ADLS Public Safety Group]]
- [[andersen-consulting|Andersen Consulting]]
- [[arthur-d-little|Arthur D. Little, Inc.]]
- [[arthur-d-little-systems|Arthur D. Little Systems, Inc. (ADLS)]]
- [[aurora-co-police-department|Aurora CO Police Department]]
- [[bapern|Boston Area Police Emergency Radio Network (BAPERN)]]
- [[boston-police-department|Boston Police Department]]
- [[ccpd|Crime Control Planning Department / Massachusetts]]
- [[data-general|Data General Corporation]]
- [[fcc|Federal Communications Commission (FCC)]]
- [[greater-boston-police-council|Greater Boston Police Council (GBPC)]]
- [[hampton-va-police-department|Hampton VA Police Department]]
- [[ibm|IBM]]
- [[leaa|Law Enforcement Assistance Administration (LEAA)]]
- [[minneapolis-police-department|Minneapolis Police Department]]
- [[motorola|Motorola]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[philadelphia-police-department|Philadelphia Police Department]]
- [[st-petersburg-fire-department|St. Petersburg FL Fire Department]]
- [[st-petersburg-police-department|St. Petersburg FL Police Department]]

## Technologies (9)

- [[data-general-eclipse|Data General Eclipse minicomputer]]
- [[fault-tolerant-architecture|Dual-redundant fault-tolerant minicomputer architecture]]
- [[ibm-360|IBM System/360]]
- [[ibm-370|IBM System/370]]
- [[ibm-cics|IBM Customer Information Control System (CICS)]]
- [[leaa-grant-funded-cad|LEAA-Grant-Funded Computer-Aided Dispatch]]
- [[mobile-status-terminal|Mobile Status Terminal (MST)]]
- [[pre-fire-plan-database|Pre-fire-plan geographic database]]
- [[uhf-t-band|UHF T-band police radio]]

## Key observations (top 25)

- **1974** — BAPERN deployment year: Boston Area Police Emergency Radio Network entered service in 1974
- **1971** — GBPC formation: Greater Boston Police Council formed 1971 to coordinate regional police communications planning that culminated in BAPERN
- **1971** — FCC Docket 18261: FCC Docket 18261 (1971) allocated UHF T-band spectrum used by BAPERN
- **1975** — Boston dispatch primary platform: Dual Data General Eclipse minicomputers in fault-tolerant configuration
- **1975** — Reliability design: Fault-tolerant pair-of-Eclipses with hot standby for life-safety dispatch
- **1973** — LEAA federal grant: LEAA federal grants funded development and deployment of the ADL public-safety CAD systems
- **1975** — First city deployment: Boston was first municipal customer of the ADL dual-Eclipse 911 CAD
- **1976** — Second city deployment: Philadelphia received migrated ADL dual-Eclipse CAD
- **1977** — Third city deployment: Minneapolis received migrated ADL dual-Eclipse CAD
- **1978** — Fourth city deployment: Aurora CO received migrated ADL dual-Eclipse CAD
- **1975** — Kastner role on four-city CAD program: Peter S. Kastner was the ADL team member responsible for hardware configuration, procurement, burn-in, and development operations for the four cities' systems
- **1976** — Kastner role on St. Petersburg dispatch: Kastner led ADL design of mainframe-based 911 dispatch on city's IBM 370/135 with CICS upgrade
- **1976** — Hampton Roads system reuse: ADL recommended migration of Hampton Roads VA dispatch system to St. Petersburg under CICS, with modifications
- **1977** — St. Petersburg PD CAD: St. Petersburg PD CAD deployed on city IBM 370/135 with CICS, derived from Hampton Roads VA
- **1977** — Fire CAD with MSTs: St. Petersburg fire CAD design included pre-fire-plan database transmitted to mobile status terminals enroute
- **2014** — Boston dispatch modernization: Boston Police $17M dispatch modernization replaced original ADL system in 2014
- **2024** — Boston Police 2024 RFP: Boston Police RFP issued December 2024 for next-generation dispatch
- **2025** — Boston Police 2025 transition: Boston Police completed dispatch transition August 9, 2025
- **1975** — ADLS practice scope: ADLS Public Safety Group built custom fault-tolerant minicomputer systems for police dispatching including Boston, Philadelphia, Minneapolis, Aurora CO, and St. Petersburg FL
- **1977** — Vendor support manager: Kastner managed OEM relationship with Data General, Digital Equipment, and Hewlett-Packard for ADLS minicomputer configuration, procurement, manufacturability, site planning, and installation
- **1979** — Security clearance: Mr. Kastner has a secret clearance and serves as the Security Officer of ADLS
- **1979** — Practice scope: ADLS Public Safety Group projects 'developed under federal funding and LEAA regulations' typically used 'state-of-the-art mobile communications to police (and fire) units'
- **1975** — ADLS practice contribution: ADLS pioneered municipal fault-tolerant CAD architecture in 1970s using paired-minicomputer redundancy

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'adl-public-safety-911-cad-systems-1973-1979-b8a001' ORDER BY year_observed;
```

