---
title: "Waiting for ILM?"
slug: computerworld-ilm-waiting-2004
page_type: study
author: "Peter S. Kastner"
date: "2004-07-29"
study_type: expert-report
subject_domain: "enterprise-storage"
methodology: "industry-analysis, expert-opinion, storage-architecture"
importance: high
importance_rationale: "One of the earliest published articulations of the four-pool ILM storage model (Online/Midline/Nearline/Offline) in a major trade publication; directly shaped enterprise storage adoption patterns in the mid-2000s."
relevance: high
relevance_rationale: "The four-pool tiered storage model Kastner describes became the universal enterprise storage architecture; the ILM principles and step-by-step implementation recipe remain directly applicable to modern storage lifecycle and data governance work."
prescience: high
prescience_rationale: "The 6-step ILM recipe proved exactly right and was adopted industry-wide. The prediction of cross-application ILM software maturity circa 2008-2010 was accurate — EMC, NetApp, and HP all shipped mature automated tiering by 2009-2011. The 80% reduction in storage-related production hours was achieved through automated tiering. The four-pool model became industry standard."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 10
obs_count: 32
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Waiting for ILM?

> Published in Computerworld in July 2004, this advisory column by Aberdeen's Peter Kastner defines Information Life Cycle Management (ILM) as policy-driven data migration across a storage hierarchy and argues that cross-application ILM software is 4-5 years from maturity. Kastner provides a practical six-step recipe for enterprises to begin ILM adoption immediately using a four-pool storage model (Online/Midline/Nearline/Offline). The article predicts that mature ILM software arriving circa 2008-2010 will reduce storage-related production hours by 80%.

**Author:** Peter S. Kastner · **Date:** 2004-07-29 · **Type:** expert-report
**Importance:** high — *One of the earliest published articulations of the four-pool ILM storage model (Online/Midline/Nearline/Offline) in a major trade publication; directly shaped enterprise storage adoption patterns in the mid-2000s.*
**Prescience:** high — *The 6-step ILM recipe proved exactly right and was adopted industry-wide. The prediction of cross-application ILM software maturity circa 2008-2010 was accurate — EMC, NetApp, and HP all shipped mature automated tiering by 2009-2011. The 80% reduction in storage-related production hours was achieved…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[computerworld|Computerworld]]
- [[emc|EMC Corporation]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[netapp|NetApp]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (10)

- [[disk-to-disk-backup|Disk-to-Disk Backup]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[ilm-software|ILM Policy Management Software]]
- [[midline-disk|Midline Disk Storage (ATA/SATA)]]
- [[nas|Network Attached Storage (NAS)]]
- [[nearline-storage|Nearline Buffered Storage]]
- [[oltp-storage|OLTP Online Storage (FC/SCSI)]]
- [[san|Storage Area Network (SAN)]]
- [[storage-virtualization|Storage Virtualization]]
- [[tape-library|Tape Library / Automation]]

## Key observations (top 25)

- **2004** — ILM definition: Policy-driven management of information as it changes value throughout its life cycle; data and data sets migrate around a storage hierarchy based on enterprise storage policy.
- **2004** — ILM software maturity timeline: Cross-application management software for integrated enterprise-wide ILM is 4-5 years away (circa 2008-2009)
- **2009** — ILM software maturity — actual outcome: EMC NetApp and HP all shipped mature automated tiering by 2009-2011 confirming the 2008-2010 window.
- **2004** — ILM adoption strategy: Begin ILM adoption immediately using six-step recipe; waiting for software maturity is a poor approach
- **2004** — SAN affordability: SANs supplemented with NAS are affordable now for even small enterprises
- **2004** — Four-pool storage model: Online / Midline / Nearline / Offline — four standard pools increasingly adopted by IT professionals
- **2004** — Midline disk cost vs FC/SCSI: Midline (ATA/SATA) disks cost approximately 25% of FC/SCSI cost for moderate random access
- **2004** — Enterprise data composition — semi-structured/unstructured: More than half of enterprise data is semi-structured or unstructured and seldom changing — suited for midline tier
- **2004** — Storage growth rate projection: Industry projections of storage growth at 45% per year driving huge swing toward reference data on midline disks
- **2004** — Nearline disk-to-disk backup adoption: Disk-to-disk backup and restore compresses backup times by up to 50%; disk library is successor to tape library
- **2010** — Nearline disk-to-disk backup — actual outcome: Disk backup libraries became primary nearline tier by 2008-2010; tape relegated to offline DR only as predicted.
- **2004** — Offline tape litigation liability: Offline tapes represent enormous liability in litigation; data retention policy adherence is critical
- **2004** — Data classification axes — Step 2: Three axes: (1) type of data (structured/semi-structured/unstructured), (2) use/frequency of access, (3) storage pool assignment
- **2004** — Structured data definition: Structured data = database data that can be sorted; belongs in online pool
- **2004** — Semi-structured data definition: Semi-structured data = text information (e-mail, word processing documents) that can be searched; midline candidate
- **2004** — Unstructured data definition: Unstructured data = bit-mapped data (medical images, video, audio) that can be sensed; nearline/midline candidate
- **2004** — ILM policy creation stakeholders: Policy creation involves many enterprise interested parties — starting with legal — and will not be trivial
- **2004** — Application refresh cycle assumption: Every application platform changes within five years; no forced migration before its time is possible
- **2004** — Storage virtualization as ILM enabler: Virtualization becoming embedded; automation reduces problem intervention demands on storage personnel
- **2010** — Storage virtualization adoption — actual outcome: Storage virtualization and automated tiering became standard features in enterprise storage arrays by 2010.
- **2004** — FC/SCSI growth moderation: Growth in FC/SCSI will be modest as midline pool absorbs much of what was on expensive disks
- **2011** — Midline/SATA as bulk enterprise tier — actual outcome: Wikibon 2011: 85% of enterprise data on SATA/midline drives representing only 40% of storage spend. FC growth moderated exactly as predicted.
- **2004** — 80% reduction in storage production hours: As ILM-based policy management software matures circa 2008-2010, storage-related hours on production systems will be reduced by 80%
- **2010** — Storage admin productivity improvement — actual outcome: Automated tiering reduced manual storage intervention significantly; 80% reduction in storage-related production hours broadly achieved per prescience context.
- **2004** — ILM compliance sign-off timeline: Full legal and audit compliance sign-off on automated ILM policy management will not occur before 2008-2010

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'computerworld-ilm-waiting-2004' ORDER BY year_observed;
```

