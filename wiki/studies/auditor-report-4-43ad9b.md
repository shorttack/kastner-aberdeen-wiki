---
title: "Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective"
slug: auditor-report-4-43ad9b
page_type: study
author: "Peter S. Kastner"
date: "2004-04"
study_type: benchmark
subject_domain: "Healthcare information systems / clinical software performance benchmarking"
methodology: "Independent audit of vendor-conducted benchmark; Mercury LoadRunner load simulation; 1-hour and 12-hour sustained load tests; isolation and slow-client tests"
importance: medium
importance_rationale: "Provides primary benchmark data for a healthcare IT system at scale circa 2004; historically significant as independent audit of clinical system performance claims."
relevance: medium
relevance_rationale: "Relevant to healthcare IT performance evaluation, benchmarking methodology, and Microsoft platform enterprise scalability topics in the Kastner collection."
prescience: medium
prescience_rationale: "Correctly identifies Windows/SQL Server platform scalability parity with Unix for enterprise workloads; benchmark methodology (LoadRunner, TPC-style auditing) reflects enduring best practices."
license: CC-BY-4.0
tier: 2
entity_count: 9
tech_count: 11
obs_count: 21
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Eclipsys SunriseXA 3.3 Meets Subsecond Response Time Objective

> Aberdeen Group audit report commissioned by Eclipsys Corp. to independently verify performance benchmarks for SunriseXA Release 3.3, a healthcare clinical information system. Benchmark simulated a 6,000-bed hospital at peak load (5,000 orders/hour, 2.27x the busiest known real hospital rate), executing 65,637 transactions in one steady-state hour via Mercury LoadRunner. Results confirmed subsecond response times for 4 of 5 transaction categories; only administrative log-on (multi-patient download) and batch group-order transactions exceeded 1 second. Database server CPU utilization was only 40% at peak. Aberdeen concludes Eclipsys successfully resolved response time issues identified in October 2003.

**Author:** Peter S. Kastner · **Date:** 2004-04 · **Type:** benchmark
**Importance:** medium — *Provides primary benchmark data for a healthcare IT system at scale circa 2004; historically significant as independent audit of clinical system performance claims.*
**Prescience:** medium — *Correctly identifies Windows/SQL Server platform scalability parity with Unix for enterprise workloads; benchmark methodology (LoadRunner, TPC-style auditing) reflects enduring best practices.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[baragwanath-hospital|Baragwanath Hospital]]
- [[eclipsys-corp|Eclipsys Corp.]]
- [[memorial-hermann-healthcare-system|Memorial Hermann Healthcare System]]
- [[mercury-interactive|Mercury Interactive (LoadRunner)]]
- [[new-york-presbyterian|New York Presbyterian]]
- [[sap|SAP]]
- [[transaction-processing-council|Transaction Processing Council (TPC)]]
- [[unisys|Unisys]]

## Technologies (11)

- [[eclipsys-sunrisexa-3-3|Eclipsys SunriseXA Release 3.3]]
- [[emc-navisphere|EMC Navisphere 6.4.0.5.2]]
- [[emc-powerpath|EMC PowerPath 3.02]]
- [[hl7-messaging|HL7 Messaging Standard]]
- [[mercury-loadrunner|Mercury LoadRunner]]
- [[microsoft-dotnet-1-0|Microsoft .Net 1.0.3705]]
- [[sql-server-2000|SQL Server 2000 (v8.00.850)]]
- [[sunrise-clinical-manager-3-04|Sunrise Clinical Manager 3.04 workflow engine]]
- [[unisys-es7000|Unisys ES7000 Database Server]]
- [[windows-2000-advanced-server-sp4|Windows 2000 Advanced Server SP4]]
- [[windows-2000-datacenter-sp4|Windows 2000 Data Center SP4]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'auditor-report-4-43ad9b' ORDER BY year_observed;
```

