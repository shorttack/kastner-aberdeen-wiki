---
title: "Waiting for ILM?"
slug: computerworld-ilm-article-15f604
page_type: study
author: "Peter S. Kastner"
date: "2004-07-29"
study_type: expert-report
subject_domain: "Enterprise Storage / Information Lifecycle Management"
methodology: "Practitioner advisory; prescriptive six-step framework based on industry observation"
importance: high
importance_rationale: "ILM was a defining storage strategy concept of the mid-2000s; Kastner's framework was widely read and shaped enterprise storage planning."
relevance: high
relevance_rationale: "Directly authored by Peter S. Kastner, published as Computerworld column; core Kastner collection piece on enterprise IT strategy."
prescience: high
prescience_rationale: "Predicted cross-application ILM maturity by 2008-2010 and 45% annual storage growth; the midline disk tier (now 'nearline SAS') became the dominant enterprise tier, and ILM capabilities did mature in that timeframe."
license: CC-BY-4.0
tier: 1
entity_count: 3
tech_count: 9
obs_count: 16
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Waiting for ILM?

> Published in Computerworld on 29 July 2004, this advisory article argues that integrated cross-application ILM software is 4-5 years away from maturity but that enterprises should begin evolving toward ILM now using a six-step recipe: (1) centralize storage into SANs/NAS, (2) classify data across three axes (type/access/pool), (3) create lifecycle policies, (4) populate new applications on appropriate pools, (5) drive economies of scale via virtualization, (6) implement intelligent ILM circa 2008-2010. The article introduces the four-pool storage model (online FC/SCSI, midline, nearline, offline tape) and projects 45% annual storage growth driving a swing toward midline disk for reference data.

**Author:** Peter S. Kastner · **Date:** 2004-07-29 · **Type:** expert-report
**Importance:** high — *ILM was a defining storage strategy concept of the mid-2000s; Kastner's framework was widely read and shaped enterprise storage planning.*
**Prescience:** high — *Predicted cross-application ILM maturity by 2008-2010 and 45% annual storage growth; the midline disk tier (now 'nearline SAS') became the dominant enterprise tier, and ILM capabilities did mature in that timeframe.*

## Entities (3)

- [[aberdeen-group|Aberdeen Group Inc.]]
- [[computerworld|Computerworld]]
- [[peter-kastner|Peter S. Kastner]]

## Technologies (9)

- [[disk-to-disk-backup|Disk-to-Disk Backup (D2D)]]
- [[fc-scsi-disk|Fibre Channel / SCSI Disk (Online Tier)]]
- [[ilm-policy-software|Cross-Application ILM Policy Management Software]]
- [[midline-disk|Midline Disk Storage]]
- [[network-attached-storage|Network Attached Storage (NAS)]]
- [[oltp-systems|Online Transaction Processing (OLTP)]]
- [[storage-area-network|Storage Area Network (SAN)]]
- [[storage-virtualization|Storage Virtualization]]
- [[tape-backup|Sequential Tape (Offline / Disaster Recovery)]]

## Key observations (top 25)

- **2004** — ILM Cross-Application Software Maturity Timeline: Integrated cross-application ILM software is 4-5 years from practical enterprise-wide maturity (circa 2008-2009)
- **2009** — ILM Software Maturity Actual Outcome: [UNVERIFIED]
- **2004** — SAN/NAS Affordability: SANs supplemented with NAS now affordable for even small enterprises
- **2004** — Midline Disk Cost vs FC/SCSI: Midline disk at approximately 25% of FC/SCSI cost for moderate random access workloads
- **2004** — Semi-Structured / Unstructured Data Share: More than 50% of enterprise data is semi-structured or unstructured and seldom changing
- **2004** — Enterprise Storage Growth Rate: 45% per year (industry projection)
- **2004** — D2D Backup Time Compression: Midline disk-to-disk backup compresses backup times by up to 50% vs tape
- **2004** — Offline Tape Litigation Liability: Offline tapes represent an enormous liability in litigation; data retention policy adherence required
- **2004** — Application Platform Refresh Cycle: Every application platform changes within 5 years; use refresh points to migrate data to proper pool
- **2004** — Storage Administrator Productivity via Virtualization: Rising terabytes-per-admin ratio as virtualization becomes embedded and automation reduces intervention
- **2004** — ILM Production System Hours Reduction: Storage-related hours on production systems reduced by 80% when ILM matures circa 2008-2010
- **2010** — ILM 80% Hours Reduction Actual Outcome: [UNVERIFIED]
- **2004** — FC/SCSI Growth Moderation: FC/SCSI growth projected to be modest as midline pool absorbs workloads previously on expensive disks
- **2004** — ILM Adoption Sequence Prescription: Six steps must be taken in order; each step implies existence of the prior one
- **2004** — Four-Pool Storage Model Adoption: Increasing number of IT professionals standardizing on four-pool storage model
- **2004** — Data Classification Complexity: Systematically analyzing which pool data belongs in is messy but enormously beneficial

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'computerworld-ilm-article-15f604' ORDER BY year_observed;
```

