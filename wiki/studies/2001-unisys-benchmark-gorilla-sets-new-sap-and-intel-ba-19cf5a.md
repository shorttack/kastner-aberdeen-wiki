---
title: "Unisys 'Benchmark Gorilla' Sets New SAP Standard on Windows- and Intel-based ES7000 Database Server"
slug: 2001-unisys-benchmark-gorilla-sets-new-sap-and-intel-ba-19cf5a
page_type: study
author: "Robert Dorin"
date: "2001-11-01"
study_type: market-study
subject_domain: "enterprise-servers"
methodology: "benchmarking"
importance: medium
importance_rationale: "Captured Unisys at its peak of Windows/Intel server benchmark dominance; relevant to the enterprise debate over Windows vs Unix for mission-critical SAP deployments. The 24000 SD users result was a notable industry milestone in 2001."
relevance: low
relevance_rationale: "The specific hardware architecture (32-processor Xeon on Windows Server 2000) is entirely superseded; modern SAP HANA runs on fundamentally different infrastructure. The performance debate has shifted to cloud and in-memory databases."
prescience: medium
prescience_rationale: "Unisys did maintain relevance in the high-end Windows server market through the mid-2000s and ES7000 line continued. However Unisys eventually exited the hardware business and Windows/Intel ultimately did not displace Unix/RISC for the highest-end SAP workloads — HANA on Linux dominated instead."
license: CC-BY-4.0
tier: 2
entity_count: 5
tech_count: 5
obs_count: 11
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Unisys 'Benchmark Gorilla' Sets New SAP Standard on Windows- and Intel-based ES7000 Database Server

> In November 2001, Aberdeen Group profiled Unisys Corporation's achievement of 24,000 SD concurrent users on a 32-processor ES7000 Windows/Intel server running SAP. The study positions Unisys as the 'benchmark gorilla' for Windows-based enterprise scalability and argues that Unisys's combination of extreme performance, high availability (Datacenter 2000 and SQL Server 2000), and price-performance advantages over Unix makes the ES7000 an attractive platform for high-end applications.

**Author:** Robert Dorin · **Date:** 2001-11-01 · **Type:** market-study
**Importance:** medium — *Captured Unisys at its peak of Windows/Intel server benchmark dominance; relevant to the enterprise debate over Windows vs Unix for mission-critical SAP deployments. The 24000 SD users result was a notable industry milestone in 2001.*
**Prescience:** medium — *Unisys did maintain relevance in the high-end Windows server market through the mid-2000s and ES7000 line continued. However Unisys eventually exited the hardware business and Windows/Intel ultimately did not displace Unix/RISC for the highest-end SAP workloads — HANA on Linux dominated instead.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[sap-ag|SAP AG]]
- [[unisys|Unisys Corporation]]

## Technologies (5)

- [[intel-xeon|Intel Xeon (32-processor)]]
- [[sap-sd-benchmark|SAP SD Benchmark]]
- [[sql-server-2000|SQL Server 2000]]
- [[unisys-es7000|Unisys ES7000]]
- [[windows-datacenter-2000|Windows 2000 Datacenter Server]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2001-unisys-benchmark-gorilla-sets-new-sap-and-intel-ba-19cf5a' ORDER BY year_observed;
```

