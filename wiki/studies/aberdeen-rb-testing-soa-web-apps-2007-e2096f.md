---
title: "Testing SOA and Web Services Applications: How Different Can It Be?"
slug: aberdeen-rb-testing-soa-web-apps-2007-e2096f
page_type: study
author: "Perry Donham"
date: "2007-08-01"
study_type: research-brief
subject_domain: "soa-testing-qa-integration-orchestration"
methodology: "research-brief, best-practices-hypothesis"
importance: medium
importance_rationale: "Identifies the testing-discipline shift required for SOA — integration, orchestration, versioning, performance — that became central to API/microservices QA practice."
relevance: medium
relevance_rationale: "Contract testing, integration testing, and versioning remain core API/microservices QA disciplines."
prescience: high
prescience_rationale: "Donham's identification of integration, orchestration, and versioning as the core new test surfaces predated the contract-testing (Pact, 2013) and chaos-engineering movements that institutionalized these disciplines a decade later."
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 5
obs_count: 5
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Testing SOA and Web Services Applications: How Different Can It Be?

> Aberdeen Group research brief by Perry Donham identifying the testing/QA challenges specific to SOA and web-services applications: unit and functional tests no longer suffice — integration and orchestration testing become critical, with performance and versioning adding further complexity. Brief draws on prior ESB/Middleware (July 2006), SOA Middleware (June 2007), and Modernizing Legacy (2007) Aberdeen research.

**Author:** Perry Donham · **Date:** 2007-08-01 · **Type:** research-brief
**Importance:** medium — *Identifies the testing-discipline shift required for SOA — integration, orchestration, versioning, performance — that became central to API/microservices QA practice.*
**Prescience:** high — *Donham's identification of integration, orchestration, and versioning as the core new test surfaces predated the contract-testing (Pact, 2013) and chaos-engineering movements that institutionalized these disciplines a decade later.*

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[perry-donham-aberdeen|Perry Donham]]

## Technologies (5)

- [[integration-testing|Integration Testing]]
- [[orchestration-testing|Orchestration Testing (BPEL/workflow)]]
- [[performance-testing|Performance/Load Testing]]
- [[soa-testing|SOA Testing / QA]]
- [[versioning-testing|Service Versioning / Compatibility Testing]]

## Key observations (top 25)

- **2007** — SOA testing concern frequency: Testing/QA consistently top-of-list concern: 43% in ESB/Middleware Benchmark July 2006; 48% planned new testing strategies in SOA Middleware study June 2007
- **2007** — Integration testing criticality: Unit and functional testing no longer enough; integration testing becomes critical for SOA applications
- **2007** — Orchestration testing criticality: Orchestration testing emerges as a critical new piece of overall SOA testing strategy
- **2007** — Versioning testing criticality: Performance and versioning testing add to the mix, creating ingredients for significant QA-department change
- **2007** — Donham role 2007 (Aug): Perry Donham, Director, Enterprise Applications Research, perry.donham@aberdeen.com

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-rb-testing-soa-web-apps-2007-e2096f' ORDER BY year_observed;
```

