---
title: "Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities"
slug: 1997-digital-s-terabyte-hour-nonstop-vld-ce92ca
page_type: study
author: "Aberdeen Group"
date: "1997-05-20"
study_type: Viewpoint
subject_domain: "Database Storage / Very Large Database Management"
methodology: "Aberdeen benchmark analysis; vendor briefing; technical architecture assessment; market research"
importance: medium
importance_rationale: "Highly prescient recognition of backup/restore as a strategic enterprise capability. The architectural thinking in this study — backup as a data movement and reorganization tool, not just insurance — became standard enterprise data management practice. Directly anticipates concepts like continuous data protection, SAN replication, and cloud backup strategies."
relevance: medium
relevance_rationale: "Highly relevant to understanding the evolution of enterprise data management from 1997 VLDB to modern cloud data platforms. The 'backup/restore goes strategic' thesis is foundational to modern data lake and data warehouse architectures."
prescience: medium
prescience_rationale: "Aberdeen's core technical insights proved remarkably accurate: fast backup/restore did become strategic; the architectural use cases Aberdeen described (rolling backup, data migration, disaster tolerance, database reorganization) are now standard practice. The specific technology (NonStop VLDB on Alpha) did not survive DEC's acquisition, but the architectural vision was validated by SAN/NAS, tape automation, deduplication, snapshot, and cloud backup technologies that delivered similar order-of-m…"
license: CC-BY-4.0
tier: 2
entity_count: 13
tech_count: 10
obs_count: 30
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities

> Aberdeen Group assessed Digital Equipment Corporation's NonStop VLDB backup/restore solution in May 1997, which delivered 400-750+ GB/hour rates — an order-of-magnitude improvement. Aberdeen predicted this technology would 'go strategic,' removing backup/restore as a database scaling barrier and enabling new architectures for data migration, disaster tolerance, and rolling VLDB operations.

**Author:** Aberdeen Group · **Date:** 1997-05-20 · **Type:** Viewpoint
**Importance:** medium — *Highly prescient recognition of backup/restore as a strategic enterprise capability. The architectural thinking in this study — backup as a data movement and reorganization tool, not just insurance — became standard enterprise data management practice. Directly anticipates concepts like continuous d…*
**Prescience:** medium — *Aberdeen's core technical insights proved remarkably accurate: fast backup/restore did become strategic; the architectural use cases Aberdeen described (rolling backup, data migration, disaster tolerance, database reorganization) are now standard practice. The specific technology (NonStop VLDB on Al…*

## Entities (13)

- [[ENT-S5-001|Digital Equipment Corporation (DEC)]]
- [[ENT-S5-002|SCH Technologies]]
- [[ENT-S5-003|Open Vision Technologies]]
- [[ENT-S5-004|Spectralogic Corporation]]
- [[ENT-S5-005|Cheyenne Software]]
- [[ENT-S5-006|Legato Systems]]
- [[ENT-S5-007|Oracle Corporation]]
- [[ENT-S5-008|Informix Software]]
- [[ENT-S5-009|Sybase Inc.]]
- [[ENT-S5-010|SAP AG]]
- [[ENT-S5-011|Silicon Graphics Inc. (SGI)]]
- [[ENT-S5-012|Hewlett-Packard]]
- [[ENT-S5-013|Sun Microsystems]]

## Technologies (10)

- [[TECH-S5-001|NonStop VLDB]]
- [[TECH-S5-002|AlphaServer 8400 (TurboLaser)]]
- [[TECH-S5-003|TLIOP I/O Channel]]
- [[TECH-S5-004|Parallelized Online Backup/Restore]]
- [[TECH-S5-005|SAP R/3]]
- [[TECH-S5-006|Legato NetWorker]]
- [[TECH-S5-007|ARCserve (Cheyenne)]]
- [[TECH-S5-008|Digital Unix (Tru64)]]
- [[TECH-S5-009|Data Deduplication]]
- [[TECH-S5-010|Cloud Backup]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-digital-s-terabyte-hour-nonstop-vld-ce92ca' ORDER BY year_observed;
```

