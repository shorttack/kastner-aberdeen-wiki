---
title: "How Aberdeen Sees the Storage Pyramid Evolving"
slug: "study-11-storage-hierarchy-presentation-e84d53"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "11-storage-hierarchy-presentation-e84d53"
author: "David Hill, Aberdeen Group"
date: "2002-10-01"
pub_year: 2002
type: "market-study"
subject_domain: "enterprise-storage"
methodology: "industry-analysis, content-taxonomy, storage-tiering-framework"
source_file: "11-Storage-Hierarchy-Presentation.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# How Aberdeen Sees the Storage Pyramid Evolving

> David Hill's Fall 2002 presentation establishing Aberdeen Group's analytical framework for the four-tier storage pyramid evolution. Introduces a content-centric approach to storage architecture based on four principles (ageing, freezing, accumulation, redundancy) and maps content types (structured/semi-structured/unstructured) to appropriate storage tiers. Provides foundational intellectual basis for the Pools of Storage and midline storage category initiative.


_Published 2002, author **David Hill, Aberdeen Group**, type **market-study**._


## Top observations

- RAM-related (memory/solid state/disk cache); High Performance Disk (FC/SCSI); Cost-Effective Disk (ATA); Tape
- Even if all four levels cost the same: FC/SCSI would prevail over ATA; RAM-based would prevail over hard disk if scaling issues addressed; hard disk replaces tape only if portability solved
- Key to change is not only price but impact upon IS processes skill sets and organizational structure
- Data: bits forming bit stream; Information: organized bits a person can recognize; Content: information used for some purpose (decision-making understanding enjoyment)
- Structured (database); Semi-structured (text documents); Unstructured (bitmaps)
- Structured: Sort; Semi-structured: Search; Unstructured: Sense
- Content (along with its distribution) is the long-term competitive differentiator; only one company owns its customer and product history data
- Ageing (value/use change as content ages); Freezing (changes from dynamic to fixed); Accumulation (very little old data discarded); Redundancy (more and more copies made)
- Conception/birth (read/write limited); Youth (high read access); Middle age (infrequent access); Old age (flatlined usage)
- Not all content even of same type ages the same; medical image quickly goes to middle age; video may have longer youth; much content is in middle age
- Content access follows Zipf's Law: frequency of access follows power law distribution from most to least frequently accessed
- Frozen content is read-only; response time depends on expectations; ATA disk appropriate for frozen content
- At pennies per megabyte it may not be cost effective to have individuals clean out regularly; policy-driven cleaning effective only in limited ways
- Physical disk failure (RAID); Logical disk failure (point-in-time copy/backup); Catastrophic site failure (remote mirroring); Unexpected archive demands (offsite archiving)
- Versioning (user copies); Test copy (PIT copy/tape); Historical analysis (data warehouse); Online production copy (broadcast/cached)
- On-site/Off-site by Online/Nearline/Offline; RAM-based: youth; High-perf disk: youth/middle age; ATA disk: middle age to old age
- High-performance: uncompleted end-user tasks/WIP/currently retrieved files/high response time frequency; Cost-effective: completed tasks/older messages/not currently required files
- Some analysts say tape is dead; Aberdeen position: there is a place for everything and everything in its place; tape meets streaming data demand
- [UNVERIFIED]
- ATA disk growing to serve active archiving and data protection functions as prices decline relative to FC/SCSI
- [UNVERIFIED]
- RAM disk: higher cost/higher capacity/faster/inflexible; FC/SCSI disk: medium cost-capacity-speed; ATA disk: lower cost/higher capacity; Tape: lowest cost/highest capacity/slowest/flexible
