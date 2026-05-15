---
title: "Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads"
slug: perspective-041304-e4be4c
page_type: study
author: "Peter S. Kastner"
date: "April 13, 2004"
study_type: topic-analysis
subject_domain: "Enterprise Computing / Server Platforms / Mainframe Migration"
methodology: "Q1-2004 in-depth qualitative interviews with U.S., European, and Asian users; quantitative survey of 98 qualified mainframe users"
importance: high
importance_rationale: "Timely 2004 research at a critical inflection point in the mainframe-vs-Intel migration debate; backed by empirical user survey data."
relevance: high
relevance_rationale: "Directly in Kastner's enterprise computing coverage area; reflects Aberdeen's Intel-sponsored research at peak of Itanium commercial momentum."
prescience: medium
prescience_rationale: "Partially prescient: correctly identified mainframe TCO pressure and Intel platform advantages, but Itanium ultimately failed commercially; Windows Server/x86 on Xeon (not Itanium) became the mainframe alternative."
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 14
obs_count: 20
tags: [type/study, importance/high, prescience/medium]
source_csv: master_studies.csv
---

# Intel's Itanium: Ready and Desirable for Mainframe-Class Workloads

> This Aberdeen Perspective piece evaluates whether Intel Itanium 2-based platforms can handle mainframe-class workloads and compares them to IBM zSeries mainframes. Drawing on Q1-2004 interviews and a survey of 98 mainframe users, the paper concludes that Itanium platforms are not only capable but in many cases desirable: users report superior performance/scalability, lower TCO, greater flexibility, and comparable robustness. Key findings include that ~40% of mainframe users are open to shifting to Itanium-based platforms; Xeon handles migrated mainframe workloads already in production; COBOL/FORTRAN/DB2 migration is surprisingly straightforward; and CICS/DL1/assembler migration requires significant effort. Aberdeen recommends 'surround, offload, or migrate' strategies over full 'replace' initiatives.

**Author:** Peter S. Kastner · **Date:** April 13, 2004 · **Type:** topic-analysis
**Importance:** high — *Timely 2004 research at a critical inflection point in the mainframe-vs-Intel migration debate; backed by empirical user survey data.*
**Prescience:** medium — *Partially prescient: correctly identified mainframe TCO pressure and Intel platform advantages, but Itanium ultimately failed commercially; Windows Server/x86 on Xeon (not Itanium) became the mainframe alternative.*

## Entities (2)

- [[ibm-zseries|IBM zSeries (z990)]]
- [[sas-institute|SAS Institute]]

## Technologies (14)

- [[amd-opteron|AMD Opteron (64-bit)]]
- [[cics|CICS (Customer Information Control System)]]
- [[cobol|COBOL]]
- [[data-warehousing-analytics|Data Warehousing and Analytics]]
- [[db2|IBM DB2]]
- [[dl1|DL/1 (Data Language 1) / IMS]]
- [[fortran|FORTRAN]]
- [[ibm-assembler|IBM Mainframe Assembler Code]]
- [[ibm-mainframe-zarch|IBM zSeries Mainframe (z900/z990)]]
- [[itanium2|Intel Itanium 2 Processor]]
- [[linux-on-mainframe|Linux on Mainframe (IBM zLinux)]]
- [[tpc-benchmark|TPC (Transaction Processing Performance Council) Benchmarks]]
- [[virtual-machine-mainframe|Virtual Machine (VM) on Mainframe]]
- [[xeon-server|Intel Xeon Server Platform]]

## Key observations (top 25)

- **2004** — mainframe-users-open-to-itanium-pct: ~40% of mainframe users
- **2004** — mainframe-offload-interest: 40% looking to offload or surround mainframes
- **2004** — itanium-vs-mainframe-performance: Itanium 2 superior to Xeon; comparable or superior to mainframe
- **2004** — xeon-mainframe-workload-production: Xeon-based mainframe solutions already in production 1+ years
- **2004** — cobol-db2-fortran-migration-effort: Straightforward; no code changes required
- **2004** — cics-dl1-assembler-migration-effort: Significant but doable
- **2004** — ibm-mainframe-discounting: IBM increasingly discounting mainframe prices
- **2004** — mainframe-tco-perception: Mainframe hardware + software licensing perceived as more expensive than open systems
- **2004** — cpu-intensive-payback-itanium: Largest payback: CPU-intensive workloads (batch, data warehousing, analytics)
- **2004** — intel-platform-advantages-summary: More scalable, more cost-effective, more flexible, smaller footprint, more programmer-productive
- **2004** — amd-opteron-less-tested: AMD Opteron seen as less real-world-tested
- **2004** — linux-on-mainframe-assessment: Linux on mainframe less manageable and less performant
- **2004** — migration-strategy-taxonomy: Surround / Offload / Replace / Migrate
- **2004** — itanium-mainframe-displacement-prediction: Itanium will increasingly host former mainframe workloads
- **2004** — itanium-mainframe-displacement-actual: [UNVERIFIED]
- **2004** — replace-strategy-risks: Replace strategy has cultural resistance and long implementation time
- **2004** — mainframe-user-survey-size: 98 qualified mainframe users surveyed
- **2004** — itanium-ecosystem-maturity: Itanium ecosystem matured; nearly all major EBAs support Itanium with customers in production
- **2004** — itanium-case-studies-newly-arrived: Most success stories just reaching production in Q1-2004
- **2004** — db2-intel-vs-mainframe-vm-cost: DB2 on Intel multiprocessor more cost-effective than mainframe VM-based allocation

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'perspective-041304-e4be4c' ORDER BY year_observed;
```

