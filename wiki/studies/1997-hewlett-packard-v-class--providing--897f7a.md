---
title: "Hewlett-Packard V-Class: Providing Enterprise Customers With the Power Path They Need"
slug: 1997-hewlett-packard-v-class--providing--897f7a
page_type: study
author: "Aberdeen Group"
date: "1997-05-22"
study_type: product-profile
subject_domain: "Enterprise Server Hardware"
methodology: "vendor-briefing,benchmark-analysis,competitive-assessment"
importance: low
importance_rationale: "Documents HP's strategic repositioning in the high-end UNIX server market using Convex supercomputing technology. The V-Class represented HP's competitive response to Sun and IBM; the HP 9000 line was eventually discontinued in 2003 after HP's Itanium-based Integrity servers emerged."
relevance: low
relevance_rationale: "Illustrates the intense UNIX server performance wars of the late 1990s and the Y2K mainframe replacement cycle. The crossbar interconnect technology foreshadowed modern high-bandwidth memory fabric architectures."
prescience: low
prescience_rationale: "Aberdeen correctly predicted that OLTP performance demands would continue to grow and that V-Class would displace mainframe workloads. HP did ship the V2200 approximately on schedule. However, the prediction that NT would not be viable for enterprise workloads \"this millennium\" proved wrong — NT/Windows 2000 gained significant enterprise traction by 1999-2001. The Merced/IA-64 prediction for 1999 was also delayed; Itanium shipped in 2001."
license: CC-BY-4.0
tier: 2
entity_count: 7
tech_count: 9
obs_count: 21
tags: [type/study, importance/low, prescience/low, decade/1990s]
source_csv: master_studies.csv
---

# Hewlett-Packard V-Class: Providing Enterprise Customers With the Power Path They Need

> Aberdeen Group evaluates HP's newly announced V-Class HP 9000 enterprise SMP servers (announced May 22, 1997). Based on supercomputing crossbar technology acquired from Convex, the V2200 Enterprise Server promises a 50% improvement in OLTP performance over existing top SMP systems. Aberdeen examines HP's roadmap through 1999 including NUMA extensions, competitive positioning against Sun, IBM, and Digital, and recommends enterprise IS executives evaluate V-Class for mainframe replacement and high-end production workloads.

**Author:** Aberdeen Group · **Date:** 1997-05-22 · **Type:** product-profile
**Importance:** low — *Documents HP's strategic repositioning in the high-end UNIX server market using Convex supercomputing technology. The V-Class represented HP's competitive response to Sun and IBM; the HP 9000 line was eventually discontinued in 2003 after HP's Itanium-based Integrity servers emerged.*
**Prescience:** low — *Aberdeen correctly predicted that OLTP performance demands would continue to grow and that V-Class would displace mainframe workloads. HP did ship the V2200 approximately on schedule. However, the prediction that NT would not be viable for enterprise workloads \"this millennium\" proved wrong — NT/Win…*

## Entities (7)

- [[e2-01|Hewlett-Packard Company]]
- [[e2-02|Convex Computer Corporation]]
- [[e2-03|Sun Microsystems]]
- [[e2-04|IBM]]
- [[e2-05|Digital Equipment Corporation]]
- [[e2-06|Storage Technology Corporation]]
- [[e2-07|EMC Corporation]]

## Technologies (9)

- [[t2-01|HP 9000 V-Class (V2200)]]
- [[t2-02|HyperPlane Crossbar Backplane]]
- [[t2-03|HP PA-RISC (PA-8200/PA-8500)]]
- [[t2-04|NUMA (Non-Uniform Memory Access)]]
- [[t2-05|Intel Merced (IA-64)]]
- [[t2-06|HP EPS (Enterprise Parallel Server)]]
- [[t2-07|HP-UX 11.0]]
- [[t2-08|TPC-D Benchmark]]
- [[t2-09|Windows NT Server]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-hewlett-packard-v-class--providing--897f7a' ORDER BY year_observed;
```

