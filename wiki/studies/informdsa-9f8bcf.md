---
title: "Can Parallel-Scalable RDBMSs Break the Downsizing Logjam?"
slug: informdsa-9f8bcf
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1995"
study_type: consulting-report
subject_domain: "database technology; parallel computing; RDBMS architecture"
methodology: "expert-analysis; vendor briefing"
importance: high
importance_rationale: "Core Informix sales training material from Aberdeen Group; articulates the architectural rationale for DSA parallel-scalable technology."
relevance: medium
relevance_rationale: "Historical analysis of RDBMS parallelism trends; still instructive for understanding the SMP-to-MPP transition period of the mid-1990s."
prescience: high
prescience_rationale: "Correctly predicted 3-5x growth in information demand by late 1990s; correctly forecast SMP dominance followed by cluster/MPP adoption; parallel-scalable RDBMS as a 'free hardware upgrade' proved prescient."
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 5
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Can Parallel-Scalable RDBMSs Break the Downsizing Logjam?

> Aberdeen Group analysis arguing that parallel-scalable RDBMS technology can resolve the 'downsizing logjam' caused by exploding information demand. Covers SMP, cluster and MPP architectures; fine-grain multiprocessor support; parallel administration; dynamic resource scalability; and selection criteria for parallel-scalable RDBMSs. 23-slide deck used in Informix sales training.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1995 · **Type:** consulting-report
**Importance:** high — *Core Informix sales training material from Aberdeen Group; articulates the architectural rationale for DSA parallel-scalable technology.*
**Prescience:** high — *Correctly predicted 3-5x growth in information demand by late 1990s; correctly forecast SMP dominance followed by cluster/MPP adoption; parallel-scalable RDBMS as a 'free hardware upgrade' proved prescient.*

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (5)

- [[client-server|Client-Server Architecture]]
- [[decision-support|Decision Support / Business Intelligence]]
- [[oltp|Online Transaction Processing]]
- [[rdbms|Relational Database (RDBMS)]]
- [[unix-server|Unix Enterprise Servers]]

## Key observations (top 25)

- **1995** — projected_info_demand_increase: 3x-5x by late 1990s
- **1995** — key_technology_gaps: Coarse-grain multiprocessor support; administration bottlenecks; poor scaleup
- **1995** — parallel_rdbms_evaluation: IS should take hard look at parallel-scalable solutions now
- **1995** — smp_architecture_status: SMP is today's most prevalent hardware architecture
- **1995** — cluster_mpp_timeline: SMP now; clusters and MPP soon (post-1995)
- **2000** — cluster_mpp_timeline: unknown
- **1995** — parallel_rdbms_benefit: Parallel-scalable RDBMS equivalent to free hardware upgrade
- **1995** — selection_criteria: Hardware adaptation (SMP/cluster/MPP); parallelization breadth; benchmarks; administration
- **1995** — info_demand_drivers: OLTP; production queries; new C-S apps; desktop automation; ad hoc queries
- **1995** — parallel_capabilities: Fine-grain multiprocessor; parallel admin; dynamic resource scalability; batch speedup
- **1995** — midrange_tech_ingredients: Many microprocessors; lots of memory; fast I/O buses; intelligent controllers; Unix
- **1995** — parallel_admin_capabilities: Bulk loading/unloading; backup/recovery; index building; mass updates; alter/reorg
- **1995** — technology_goals: Excellent cost-performance; scalability; availability; fast response; open infra; dev tools; easy admin
- **1995** — market_readiness: Parallel-scalable RDBMS technology now being rolled out by RDBMS leaders
- **1995** — user_empowerment_drivers: Personnel downsizing; improved computer literacy; increased job productivity; users as decision makers
- **1995** — smp_timeline: SMP will still be maturing in 5 years (i.e., ~2000)
- **2000** — smp_timeline: unknown
- **1995** — decision_support_value: Correct decision on 1000 red summer dresses drops directly to bottom line
- **1995** — parallel_scalable_benefits: Improved performance; increased robustness/availability; lower-cost configuration; improved scalability
- **1995** — distributed_computing_tiers: Four tiers: PC/workstation; PC LAN server; division/department; massively parallel

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'informdsa-9f8bcf' ORDER BY year_observed;
```

