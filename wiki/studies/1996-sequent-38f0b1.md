---
title: "Emerging Technologies: Assessing Strategic Benefits"
slug: 1996-sequent-38f0b1
page_type: study
author: "Peter S. Kastner"
date: "1996-05-01"
study_type: presentation
subject_domain: "enterprise-computing"
methodology: "industry-analysis, benchmarking"
importance: high
importance_rationale: "Early Aberdeen analysis of NUMA architecture vs SMP and clusters; Sequent was a pioneer whose approach proved architecturally prescient for modern multi-socket servers."
relevance: medium
relevance_rationale: "NUMA concepts remain foundational in modern server architecture; specific vendor and product details are dated but the architectural principles endure."
prescience: high
prescience_rationale: "Predicted that NUMA-Q would extend Intel-standard computing beyond mainframes while preserving software investments; this vision was validated as x86 NUMA servers replaced proprietary mainframes."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 10
obs_count: 35
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Emerging Technologies: Assessing Strategic Benefits

> Aberdeen Group presentation for the Vision 2000 conference (May 1996) analyzing enterprise superserver architectures. The study compares symmetric multiprocessing (SMP), clustering, and Sequent's emerging NUMA-Q technology, arguing that NUMA will extend Intel-standard computing beyond traditional mainframe capabilities while preserving software investments. Covers the business case for enterprise IT investment, multi-tier application architectures, and technology planning through 2001.

**Author:** Peter S. Kastner · **Date:** 1996-05-01 · **Type:** presentation
**Importance:** high — *Early Aberdeen analysis of NUMA architecture vs SMP and clusters; Sequent was a pioneer whose approach proved architecturally prescient for modern multi-socket servers.*
**Prescience:** high — *Predicted that NUMA-Q would extend Intel-standard computing beyond mainframes while preserving software investments; this vision was validated as x86 NUMA servers replaced proprietary mainframes.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[digital-equipment|Digital Equipment Corporation]]
- [[hp|Hewlett-Packard]]
- [[ibm|IBM]]
- [[intel|Intel]]
- [[oracle|Oracle]]
- [[sequent-computer|Sequent Computer Systems]]

## Technologies (10)

- [[atm-networking|ATM Networking]]
- [[clustering|Clustering]]
- [[dss|Decision Support Systems]]
- [[ibm-es9000-sysplex|IBM ES/9000 Sysplex]]
- [[ibm-sp2|IBM SP2]]
- [[intel-x86|Intel x86 Processors]]
- [[numa-q|Sequent NUMA-Q]]
- [[oltp|Online Transaction Processing]]
- [[smp|Symmetric Multiprocessing]]
- [[vaxcluster|Digital VAXcluster]]

## Key observations (top 25)

- **1996** — IT investment strategy: Technology equals productivity; superior use of technology leads to superior corporate returns
- **1996** — cost reduction strategy: Direct IS to lower SG&A by 20% for 70% PBT improvement; lower COGS by 5% for 27% PBT improvement
- **1996** — application architecture: Multi-tier (3-tier) client-server architectures demand enterprise superservers
- **1996** — SMP scalability: Good to 4 processors; fair to 8; few do more than 10 well; Sequent does very well
- **1996** — SMP architecture maturity: Well understood technology with new chip-set accelerators and inexpensive engineering
- **1996** — cluster software readiness: Today's system software and customer applications are not cluster-enabled; require re-engineering
- **1996** — cluster overhead: Message-passing burns CPU and memory cycles; messaging between nodes is very complex technology requiring time to mature
- **1996** — NUMA-Q positioning: Aimed at world's toughest commercial computing problems: OLTP, complex DSS, and messaging
- **1996** — NUMA-Q architecture merit: Engineering elegance delivering scalability with minimal overhead and no application software changes
- **1996** — NUMA-Q benchmark potential: Will be a benchmark for high-end commercial computing leadership into the 21st century
- **1996** — NUMA-Q market position: NUMA-Q will extend Intel-standard to well beyond even traditional mainframes while preserving software investments
- **1996** — information resource demand: 3x-5x increases in demand for information resources over next 5 years (by 2001)
- **1996** — CPU horsepower growth: 10x-15x more client and server CPU horsepower by 2001
- **1996** — network bandwidth forecast: Cheap, infinite network bandwidth with ATM by 2001
- **1996** — information highway status: Like 1996, the information highway will still be under construction in 2001
- **1996** — enterprise infrastructure levels: Four levels: Level 1 Client, Level 2 Workgroup, Level 3 OLTP, Level 4 IS Enterprise Operations
- **1996** — end-user job process: Four-step process: Decide, Analyze, Transact, Report -- mapped to DSS, Brain, OLTP/Workflow, Messaging
- **1996** — application system criticality: There is no time for application downtime -- the computer system is the business
- **1996** — typical IS cost as percent of revenue: 3% of total revenue (part of SG&A)
- **1996** — typical SG&A as percent of revenue: 35% of total revenue
- **1996** — SMP effective processor count: Good scaling to 4 processors; fair to 8; diminishing returns beyond 10
- **1996** — SG&A reduction PBT impact: 20% SG&A reduction yields 70% PBT improvement
- **1996** — cluster architecture outlook: Traditional SMP and cluster implementations are ill-suited to efficient scalability
- **1996** — enterprise computing direction: Enterprises harshly driven to cut SG&A while raising productivity; new multi-tier architectures demand new breed of enterprise superservers
- **1996** — IS buy vs make: Huge advantages to IS Buy vs. Make strategy

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1996-sequent-38f0b1' ORDER BY year_observed;
```

