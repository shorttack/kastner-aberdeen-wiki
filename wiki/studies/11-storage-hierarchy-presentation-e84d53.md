---
title: "How Aberdeen Sees the Storage Pyramid Evolving"
slug: 11-storage-hierarchy-presentation-e84d53
page_type: study
author: "David Hill, Aberdeen Group"
date: "2002-10-01"
study_type: market-study
subject_domain: "enterprise-storage"
methodology: "industry-analysis, content-taxonomy, storage-tiering-framework"
importance: high
importance_rationale: "Foundational theoretical document for the midline category creation project; establishes the intellectual infrastructure (content principles and storage pyramid) that the entire Maxtor/Aberdeen engagement was built upon. David Hill's framework predated and enabled the Pools of Storage framework."
relevance: high
relevance_rationale: "Content lifecycle principles (ageing freezing accumulation redundancy) are more relevant than ever in cloud/object storage era; tiered storage mapping is core to modern storage architecture including S3 Intelligent-Tiering. Zipf's Law application to content access frequency is still cited in storage economics."
prescience: high
prescience_rationale: "Predicted that ATA cost-effective disk would displace tape for many archival functions; confirmed. Predicted content-based storage tiering would drive enterprise storage decisions; confirmed by ILM movement and cloud tiering. Predicted tape would not die but find its specific niche; tape remains active for deep archive."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 6
obs_count: 22
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# How Aberdeen Sees the Storage Pyramid Evolving

> David Hill's Fall 2002 presentation establishing Aberdeen Group's analytical framework for the four-tier storage pyramid evolution. Introduces a content-centric approach to storage architecture based on four principles (ageing, freezing, accumulation, redundancy) and maps content types (structured/semi-structured/unstructured) to appropriate storage tiers. Provides foundational intellectual basis for the Pools of Storage and midline storage category initiative.

**Author:** David Hill, Aberdeen Group · **Date:** 2002-10-01 · **Type:** market-study
**Importance:** high — *Foundational theoretical document for the midline category creation project; establishes the intellectual infrastructure (content principles and storage pyramid) that the entire Maxtor/Aberdeen engagement was built upon. David Hill's framework predated and enabled the Pools of Storage framework.*
**Prescience:** high — *Predicted that ATA cost-effective disk would displace tape for many archival functions; confirmed. Predicted content-based storage tiering would drive enterprise storage decisions; confirmed by ILM movement and cloud tiering. Predicted tape would not die but find its specific niche; tape remains act…*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[data-general|Data General]]
- [[david-hill|David Hill]]
- [[emc|EMC Corporation]]

## Technologies (6)

- [[ata|ATA (Advanced Technology Attachment)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[nas|Network Attached Storage (NAS)]]
- [[raid|RAID Disk Storage]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[storage-pyramid|Storage Pyramid Framework]]

## Key observations (top 25)

- **2002** — Four storage pyramid tiers: RAM-related (memory/solid state/disk cache); High Performance Disk (FC/SCSI); Cost-Effective Disk (ATA); Tape
- **2002** — Storage hierarchy persistence analysis: Even if all four levels cost the same: FC/SCSI would prevail over ATA; RAM-based would prevail over hard disk if scaling issues addressed; hard disk replaces tape only if portability solved
- **2002** — Storage hierarchy change drivers: Key to change is not only price but impact upon IS processes skill sets and organizational structure
- **2002** — Content definition vs data vs information: Data: bits forming bit stream; Information: organized bits a person can recognize; Content: information used for some purpose (decision-making understanding enjoyment)
- **2002** — Three content types: Structured (database); Semi-structured (text documents); Unstructured (bitmaps)
- **2002** — Content capability requirements: Structured: Sort; Semi-structured: Search; Unstructured: Sense
- **2002** — Content competitive advantage: Content (along with its distribution) is the long-term competitive differentiator; only one company owns its customer and product history data
- **2002** — Four principles of enterprise content: Ageing (value/use change as content ages); Freezing (changes from dynamic to fixed); Accumulation (very little old data discarded); Redundancy (more and more copies made)
- **2002** — Content ageing lifecycle stages: Conception/birth (read/write limited); Youth (high read access); Middle age (infrequent access); Old age (flatlined usage)
- **2002** — Heterogeneous ageing rates: Not all content even of same type ages the same; medical image quickly goes to middle age; video may have longer youth; much content is in middle age
- **2002** — Zipf's Law applied to content access: Content access follows Zipf's Law: frequency of access follows power law distribution from most to least frequently accessed
- **2002** — Freezing content storage implication: Frozen content is read-only; response time depends on expectations; ATA disk appropriate for frozen content
- **2002** — Accumulation economics: At pennies per megabyte it may not be cost effective to have individuals clean out regularly; policy-driven cleaning effective only in limited ways
- **2002** — Redundancy table - protection uses: Physical disk failure (RAID); Logical disk failure (point-in-time copy/backup); Catastrophic site failure (remote mirroring); Unexpected archive demands (offsite archiving)
- **2002** — Redundancy table - normal business uses: Versioning (user copies); Test copy (PIT copy/tape); Historical analysis (data warehouse); Online production copy (broadcast/cached)
- **2002** — Where content lives framework: On-site/Off-site by Online/Nearline/Offline; RAM-based: youth; High-perf disk: youth/middle age; ATA disk: middle age to old age
- **2002** — High-performance vs cost-effective disk boundary: High-performance: uncompleted end-user tasks/WIP/currently retrieved files/high response time frequency; Cost-effective: completed tasks/older messages/not currently required files
- **2002** — Future of tape assessment: Some analysts say tape is dead; Aberdeen position: there is a place for everything and everything in its place; tape meets streaming data demand
- **2002** — Tape survival in storage hierarchy: [UNVERIFIED]
- **2002** — Cost-effective disk role expansion: ATA disk growing to serve active archiving and data protection functions as prices decline relative to FC/SCSI
- **2002** — Cost-effective disk role expansion: [UNVERIFIED]
- **2002** — Random vs sequential access technology comparison: RAM disk: higher cost/higher capacity/faster/inflexible; FC/SCSI disk: medium cost-capacity-speed; ATA disk: lower cost/higher capacity; Tape: lowest cost/highest capacity/slowest/flexible

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '11-storage-hierarchy-presentation-e84d53' ORDER BY year_observed;
```

