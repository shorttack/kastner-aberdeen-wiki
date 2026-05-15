---
title: "ADL Client AS&E ASEP: Two-Way Power-Line Communications and Time-of-Day Metering (1979)"
slug: adl-ase-asep-two-way-power-communications-1979-b8c001
page_type: study
author: "Peter S. Kastner"
date: "1979-01-01"
study_type: employer-record
subject_domain: "employer/arthur-d-little/utility-systems"
methodology: "document-review"
importance: medium
importance_rationale: "Documents an early commercial deployment of two-way power-line communications and demand-response in residential utility metering — a topic now central to smart-grid initiatives."
relevance: high
relevance_rationale: "Time-of-day pricing, demand response, residential load control, and power-line communications all remain core smart-grid concepts; AS&E's ASEP was a 1970s precursor."
prescience: high
prescience_rationale: "Department of Energy projection that 'most states will be using time-of-day rates within five or six years' was directionally correct over 30+ years; demand-response programs in 154,000 Wisconsin Electric homes presaged modern utility load-management programs."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 5
obs_count: 11
tags: [type/study, importance/medium, prescience/high, decade/1970s]
source_csv: master_studies.csv
---

# ADL Client AS&E ASEP: Two-Way Power-Line Communications and Time-of-Day Metering (1979)

> Trade-press article (likely Computerworld 1979) profiling American Science & Engineering's ASEP system, a two-way power-line communications system controlled by a Data General Eclipse S-230 minicomputer with 256K core memory. Used by utilities (Florida Power Corp, Florida Power & Light, Wisconsin Electric Power, etc.) for time-of-day metering, residential air-conditioning/water-heater control, and brownout/blackout prevention. AS&E was a Cambridge MA Kastner-adjacent ADL client.

**Author:** Peter S. Kastner · **Date:** 1979-01-01 · **Type:** employer-record
**Importance:** medium — *Documents an early commercial deployment of two-way power-line communications and demand-response in residential utility metering — a topic now central to smart-grid initiatives.*
**Prescience:** high — *Department of Energy projection that 'most states will be using time-of-day rates within five or six years' was directionally correct over 30+ years; demand-response programs in 154,000 Wisconsin Electric homes presaged modern utility load-management programs.*

## Entities (7)

- [[american-science-and-engineering|American Science & Engineering, Inc. (AS&E)]]
- [[florida-power-and-light|Florida Power & Light]]
- [[florida-power-corp|Florida Power Corporation]]
- [[martin-annis|Dr. Martin Annis]]
- [[ralph-abbott|Ralph Abbott]]
- [[us-doe|US Department of Energy]]
- [[wisconsin-electric|Wisconsin Electric Power Company]]

## Technologies (5)

- [[asep-system|ASEP — Two-Way Power-Line Communications System]]
- [[data-general-eclipse-s-230|Data General Eclipse S-230 minicomputer]]
- [[demand-response|Demand Response]]
- [[powerline-comms|Power-line communications (PLC)]]
- [[time-of-day-metering|Time-of-Day Metering]]

## Key observations (top 25)

- **1979** — ASEP architecture: ASEP was a two-way power-line communications system controlled by a Data General Eclipse S-230 minicomputer with 256K core memory
- **1979** — Controller platform: Data General Eclipse S-230 with 256K core memory served as ASEP system controller
- **1979** — Florida Power dynamic rate test: Florida Power Corp piloted dynamic rate system charging customers peak rates only when peak levels actually reached, polling meters as often as every 30 minutes
- **1979** — Wisconsin Electric water-heater control: Wisconsin Electric used ASEP to control water heaters in 154,000 homes plus remotely meter customers
- **1979** — FPL residential load control: Florida Power & Light planned ASEP for residential AC/heating system and electrical-water-heater control
- **1979** — DoE ToD adoption forecast: DoE estimated most US states would use time-of-day rates within five or six years
- **1979** — Brownout-prevention claim: Abbott (AS&E VP): 'If electrical usage reaches dangerous levels, the system is capable of turning off blocks of non-essential electrical loads' to avert major problems
- **1979** — ToD national-goals statement: Annis (AS&E president): time-of-day rating supports the national goal of energy conservation
- **1979** — Multi-state ASEP adoption: Utilities in Missouri, New Jersey, Minnesota, and California also implemented ASEP; ~12 states using such systems experimentally
- **1979** — Consumer demand-shift: Time-of-day rates intended to enable consumers to save by shifting washing-machine, dryer, and water-heater use to evenings or weekends
- **1979** — Two-way comms benefit: Two-way ASEP system prevents electrical brownouts and blackouts by operating over existing power lines, an already-in-place communications medium

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'adl-ase-asep-two-way-power-communications-1979-b8c001' ORDER BY year_observed;
```

