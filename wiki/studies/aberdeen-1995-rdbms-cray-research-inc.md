---
title: "Cray Research, Inc.: RDBMS and Commercial Database Market Position"
slug: aberdeen-1995-rdbms-cray-research-inc
page_type: study
author: "Aberdeen Group"
date: "1995-01-01"
study_type: product-profile
subject_domain: "high-performance computing / RDBMS"
methodology: "vendor analysis"
importance: medium
importance_rationale: "The study documents Cray Research's commercial database pivot at a historically significant moment, just months before its acquisition by SGI in February 1996. It captures the market dynamics of high-end UNIX SMP servers competing for VLDB workloads."
relevance: high
relevance_rationale: "Directly relevant to enterprise database infrastructure and high-performance computing market evolution, covering real commercial competitors and observable outcomes in a well-documented technology transition."
prescience: high
prescience_rationale: "Aberdeen's prediction that Cray would become 'a major force' in commercial databases was largely invalidated by SGI's acquisition and divestiture of the Superservers business to Sun in 1996. However, the analysis of SMP architecture as the dominant path for VLDB proved prescient—Sun's resulting Enterprise 10000 became highly successful."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 6
obs_count: 28
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Cray Research, Inc.: RDBMS and Commercial Database Market Position

> Aberdeen Group profile of Cray Research's pivot to commercial RDBMS markets via its CS6400 SMP server platform. Examines market positioning against IBM SP2 and AT&T GIS 3600, organizational restructuring into the Business Systems Division, and product capabilities for very large database (VLDB) workloads.

**Author:** Aberdeen Group · **Date:** 1995-01-01 · **Type:** product-profile
**Importance:** medium — *The study documents Cray Research's commercial database pivot at a historically significant moment, just months before its acquisition by SGI in February 1996. It captures the market dynamics of high-end UNIX SMP servers competing for VLDB workloads.*
**Prescience:** high — *Aberdeen's prediction that Cray would become 'a major force' in commercial databases was largely invalidated by SGI's acquisition and divestiture of the Superservers business to Sun in 1996. However, the analysis of SMP architecture as the dominant path for VLDB proved prescient—Sun's resulting Ente…*

## Entities (10)

- [[ABERDEEN-GROUP|Aberdeen Group]]
- [[ATT-GIS|AT&T Global Information Solutions (formerly NCR)]]
- [[CRAY-BSD|Cray Research Business Systems Division]]
- [[CRAY-RESEARCH|Cray Research Inc.]]
- [[IBM-SP2|IBM SP2]]
- [[INFORMIX|Informix Software]]
- [[NCUBE|nCUBE Corporation]]
- [[ORACLE|Oracle Corporation]]
- [[SUN-MICROSYSTEMS|Sun Microsystems]]
- [[SYBASE|Sybase Inc.]]

## Technologies (6)

- [[CS6400|Cray CS6400 SMP Server]]
- [[SMP|Symmetric Multiprocessing]]
- [[SOLARIS-CX|Cray-Enhanced Solaris OS]]
- [[SPARC|Sun SPARC Architecture]]
- [[T3D|Cray T3D Massively Parallel Processor]]
- [[VLDB|Very Large Database (VLDB) Technology]]

## Key observations (top 25)

- **1995** — commercial_revenue_share: 50%
- **1995** — database_revenue_share: 10%
- **1995** — max_online_storage: 5TB
- **1995** — max_cpus: 64
- **1995** — internal_bandwidth_gbps: 1.76
- **1995** — max_physical_memory_gb: 16
- **1995** — isv_application_count: 10000
- **1995** — target_db_size_range: 20GB-500GB
- **1995** — strategic_move: commercial_database_pivot
- **1995** — bsd_formation: merger_of_subsidiaries
- **1995** — market_viability_prediction: major_force_in_commercial_db
- **1996** — acquisition_outcome: acquired_by_SGI
- **1995** — fiscal_1995_revenue_loss: 226400000
- **1995** — competitive_position: primary_competitor_to_cs6400
- **1995** — competitive_position: secondary_competitor_with_3600
- **1995** — competitive_position: ncube2_ncube3_competitor
- **1995** — smp_commercial_viability_prediction: smp_will_dominate_enterprise_db
- **1996** — cs6400_successor: sun_enterprise_10000
- **1995** — i64_io_channels: 64
- **1995** — supercomputer_market_share_above_5m: 70%
- **1995** — solaris_feature: processor_partitioning
- **1995** — solaris_feature: hot_swap_capability
- **1995** — ceo_hire: j_phillip_samper
- **1995** — bsd_gm: bobbi_hazard_vp_gm
- **1995** — t3d_use_case: scientific_above_5tb

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-rdbms-cray-research-inc' ORDER BY year_observed;
```

