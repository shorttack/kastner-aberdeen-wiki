---
title: "Who Cares If The Computer Breaks?"
slug: ft-mitfor~1-a56a9d
page_type: study
author: "Peter S. Kastner"
date: "1995-10-01"
study_type: white-paper
subject_domain: "fault-tolerance, high-availability"
methodology: "industry-analysis, expert-opinion"
importance: medium
importance_rationale: "One of the earlier synthesized frameworks for classifying high-availability tiers for commercial computing; delivered to a technically sophisticated MIT audience."
relevance: high
relevance_rationale: "High-availability architecture principles described remain foundational; downtime cost analysis and availability percentage ladders are still used in SLA design today."
prescience: high
prescience_rationale: "The prediction that most future availability improvements would depend on system software (rather than hardware alone) proved correct — the subsequent decade saw HA clustering middleware and application-layer failover dominate the market."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 7
obs_count: 24
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Who Cares If The Computer Breaks?

> A presentation delivered at the MIT Forum in October 1995 examining why computer failures are increasingly catastrophic as society's dependence on computing grows. Kastner surveys the causes of hardware, software, and network failure, then presents a spectrum of high-availability and fault-tolerance strategies ranging from RAID to fully redundant failover architectures. The talk concludes that future availability gains will depend on system software enabling application failover without prohibitive development costs.

**Author:** Peter S. Kastner · **Date:** 1995-10-01 · **Type:** white-paper
**Importance:** medium — *One of the earlier synthesized frameworks for classifying high-availability tiers for commercial computing; delivered to a technically sophisticated MIT audience.*
**Prescience:** high — *The prediction that most future availability improvements would depend on system software (rather than hardware alone) proved correct — the subsequent decade saw HA clustering middleware and application-layer failover dominate the market.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[digital-equipment|Digital Equipment Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (7)

- [[client-server|Client-Server Architecture]]
- [[desktop-software|Desktop Software]]
- [[heartbeat-failover|Heartbeat Failover Protocol]]
- [[oltp|Online Transaction Processing]]
- [[raid|RAID Disk Storage]]
- [[rdbms|Relational Database Management System]]
- [[systems-management-software|Systems Management Software]]

## Key observations (top 25)

- **1995** — PC workforce penetration: 45% of U.S. workers now using PCs
- **1995** — Computing shift from batch to real-time: Commercial computers transitioned from book-keeping to money-making role; failures now catastrophic
- **1995** — Hardware reliability trend: Unit reliability improves; system reliability declines due to more components
- **1995** — Software failure causes: Software fails due to complexity exceeding human capacity, poor design/testing, repeated rework
- **1995** — Network reliability issue: Network availability is a key inhibitor to growth of distributed computing
- **1995** — Availability floor for business: 99.9% uptime is a floor not the ceiling in today's business world
- **1995** — Downtime at 99.0% uptime: 5,259.6 minutes per year
- **1995** — Downtime at 99.9% uptime: 526.0 minutes per year
- **1995** — Downtime at 99.99% uptime: 52.6 minutes per year
- **1995** — Downtime at 99.999% uptime: 5.3 minutes per year
- **1995** — Downtime at 99.9999% uptime: 0.5 minutes per year
- **1995** — RAID as HA option: RAID disk storage is a recommended hardware approach to minimize downtime
- **1995** — Classic failover architecture: Primary/secondary heartbeat failover: primary saves key data, sends heartbeat; secondary monitors and restarts
- **1995** — Stratus positioning: Stratus exemplifies hardware self-checking failover architecture
- **1995** — Tandem positioning: Tandem exemplifies N+1 failover architecture
- **1995** — DEC shared-disk positioning: Digital Equipment exemplifies shared disk failover architecture
- **1995** — RDBMS role in availability: RDBMS and OLTP software ensures data recoverability
- **1995** — Future HA improvement driver: Most future availability improvements will depend on system software enabling application failover without dramatic cost/complexity increase
- **2005** — Future HA improvement driver - outcome: Confirmed — systems management/monitoring became multi-billion-dollar market (Tivoli, BMC, CA, now Datadog, Splunk, Dynatrace)
- **1995** — Buyer contradiction on HA spending: Buyers want highest availability but unwilling to pay much more than commodity prices
- **1995** — Self-repairing networks opportunity: Self-repairing networks identified as an emerging opportunity
- **1995** — Systems management tools opportunity: Systems management tools down to application-object level represent opportunity
- **1995** — Disaster backup for client-server: Disaster backup services for client-server applications identified as new business opportunity
- **2005** — Disaster backup for client-server - outcome: Confirmed — disaster recovery for distributed systems became standard practice; cloud DR services now mainstream

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ft-mitfor~1-a56a9d' ORDER BY year_observed;
```

