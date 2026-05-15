---
title: "System saves $ for thrifty night owls (AS&E ASEP time-of-day metering)"
slug: minicomputer-news-ase-asep-1979-2b5327
page_type: study
author: "Minicomputer News staff"
date: "1979-06-21"
study_type: news-article
subject_domain: "utility-automation-energy-management"
methodology: "news-reporting, expert-quote"
importance: medium
importance_rationale: "Early documented example of utility DSM (demand-side management) via power-line communications and minicomputer control — a precursor to modern AMI/smart-grid systems. Archival value for Kastner's ADL chapter."
relevance: medium
relevance_rationale: "The time-of-day rate concept and two-way AMI architecture remain central to modern smart-grid deployments; the Data General Eclipse hardware is obsolete but the policy framework persists."
prescience: high
prescience_rationale: "DoE prediction that 'most states will be using time-of-day rates within five or six years' under-called the pace modestly but correctly identified TOU pricing as the dominant industrial/commercial tariff regime, now pervasive in U.S. regulated utility rate design."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 4
obs_count: 12
tags: [type/study, importance/medium, prescience/high, decade/1970s]
source_csv: master_studies.csv
---

# System saves $ for thrifty night owls (AS&E ASEP time-of-day metering)

> Minicomputer News (June 21, 1979) profiles the ASEP two-way power-line communications system developed by American Science & Engineering (AS&E) of Cambridge, Mass. to enable utility time-of-day metering. The system is controlled by a Data General Eclipse S-230 minicomputer with 256K core memory and is deployed by Florida Power, Florida Power and Light, Wisconsin Electric Power (154,000 homes), and utilities in Missouri, New Jersey, Minnesota and California. Article from Kastner's Arthur D. Little era (1972-1979); WEPco (Wisconsin Electric Power) appears in the filename suggesting this was an ADL client deliverable reference.

**Author:** Minicomputer News staff · **Date:** 1979-06-21 · **Type:** news-article
**Importance:** medium — *Early documented example of utility DSM (demand-side management) via power-line communications and minicomputer control — a precursor to modern AMI/smart-grid systems. Archival value for Kastner's ADL chapter.*
**Prescience:** high — *DoE prediction that 'most states will be using time-of-day rates within five or six years' under-called the pace modestly but correctly identified TOU pricing as the dominant industrial/commercial tariff regime, now pervasive in U.S. regulated utility rate design.*

## Entities (10)

- [[american-science-engineering|American Science & Engineering (AS&E)]]
- [[arthur-d-little|Arthur D. Little]]
- [[data-general-corporation|Data General Corporation]]
- [[florida-power-and-light|Florida Power and Light Company]]
- [[florida-power-corp|Florida Power Corporation]]
- [[martin-annis|Dr. Martin Annis]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[ralph-abbott|Ralph Abbott]]
- [[us-department-of-energy|U.S. Department of Energy]]
- [[wisconsin-electric-power|Wisconsin Electric Power Company (WEPco)]]

## Technologies (4)

- [[asep|ASEP Automated Station Energy Program]]
- [[data-general-eclipse-s230|Data General Eclipse S-230]]
- [[power-line-carrier|Power-line Carrier Communication]]
- [[time-of-day-rates|Time-of-day electricity tariff]]

## Key observations (top 25)

- **1979** — Time-of-day rating customer benefit: Small lifestyle change enables savings; Ralph Abbott (AS&E VP) asserts users will adopt TOU
- **1979** — DoE forecast: states using TOU rates within 5-6 years: Most U.S. states forecast to adopt TOU by 1984-1985
- **1979** — ASEP experimental deployments: Utilities in ~12 states using ASEP on experimental basis in 1979
- **1979** — WEPco ASEP water-heater control: 154,000 homes under ASEP water-heater load control
- **1979** — National-energy-conservation benefit: TOU reduces oil needed for generation — aids national energy conservation goal
- **1979** — ASEP brownout prevention capability: Can shed non-essential loads during dangerous usage spikes; only minor customer inconvenience
- **1979** — Dynamic rate pilot: Florida Power Corp. to test dynamic rate system charging peak only when peak reached
- **1979** — ASEP deployment states: Florida, Wisconsin, Missouri, New Jersey, Minnesota, California
- **1979** — ASEP metering granularity: Individual meter usage checkable as often as every 30 minutes or as infrequently as monthly
- **1979** — Kastner ADL employment era: Article dates to Kastner's Arthur D. Little tenure (1972-1979); likely an ADL reference piece on utility-automation minicomputer applications relevant to ADL clients
- **1979** — ASEP communications medium: Two-way signaling over powerlines — communications medium already in place
- **1979** — FP&L planned control applications: Residential AC/heating systems and electrical water heaters under ASEP control

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'minicomputer-news-ase-asep-1979-2b5327' ORDER BY year_observed;
```

