---
title: "Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity"
slug: 04-mid-line-storage-v2-whitepaper-7db9bc
page_type: study
author: "Aberdeen Group"
date: "2003-08-01"
study_type: white-paper
subject_domain: "midline-storage / enterprise-storage / ILM"
methodology: "primary-research,industry-analysis"
importance: high
importance_rationale: "The published deliverable of the Aberdeen-Maxtor SOW engagement — the formal launch artifact of the midline storage category. Aberdeen's first major published articulation of the mid-line tier concept backed by 75 enterprise interviews. This white paper is the intellectual foundation of the broader Pools of Storage program."
relevance: high
relevance_rationale: "ILM tiered storage and the concept of aligning data to cost-appropriate storage based on access patterns remain current enterprise architecture principles. The white paper's four ILM principles (Aging/Freezing/Accumulation/Redundancy) are still analytically valid. ATA-based midline storage is now the standard (SATA SSDs and HDDs dominate secondary tiers)."
prescience: high
prescience_rationale: ""
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 10
obs_count: 34
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Mid-Line Disk Storage Emerging As Significant Cost-Saving Opportunity

> Aberdeen Group's Executive White Paper presenting the case for a new 'mid-line' disk storage tier using ATA technology positioned between high-performance FC/SCSI disk arrays and tape. Based on 75 face-to-face and telephone interviews with Fortune-class storage managers. The paper defines four tiers of the storage pyramid (high-performance disk / mid-line / near-line / tape) and argues that mid-line ATA disk can serve at least 20% of enterprise data — and potentially over half — at 50% lower cost per gigabyte. It also introduces information lifecycle management (ILM) as the strategic framework for multi-tier storage.

**Author:** Aberdeen Group · **Date:** 2003-08-01 · **Type:** white-paper
**Importance:** high — *The published deliverable of the Aberdeen-Maxtor SOW engagement — the formal launch artifact of the midline storage category. Aberdeen's first major published articulation of the mid-line tier concept backed by 75 enterprise interviews. This white paper is the intellectual foundation of the broader…*
**Prescience:** high — **

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[maxtor|Maxtor Corporation]]

## Technologies (10)

- [[ata|ATA / PATA Disk Interface]]
- [[continuous-data-protection|Continuous Data Protection (CDP)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[ilm|Information Lifecycle Management (ILM)]]
- [[maxline|MaXLine ATA Disk Drives]]
- [[nas|Network-Attached Storage (NAS)]]
- [[raid|RAID (Redundant Array of Independent Disks)]]
- [[san|Storage Area Network (SAN)]]
- [[scsi|SCSI Disk Interface]]
- [[solid-state-disk|Solid-State Disk (SSD)]]

## Key observations (top 25)

- **2003** — ATA vs FC/SCSI capacity advantage: ATA disk up to 300 GB per disk vs 142/72/36 GB per FC/SCSI disk — 2x to 8x capacity advantage
- **2003** — ATA vs FC/SCSI cost advantage: ATA disks cost approximately half the price per gigabyte compared to FC/SCSI disks
- **2003** — Enterprise data in mid-line category: At least 20% of enterprise data fits mid-line definition per survey respondents — Aberdeen believes more than half will eventually fall into mid-line
- **2003** — Data restoration frequency: More than 60% of respondents report data restorations performed more than once a year; 20% monthly or more frequently
- **2003** — Backup window adequacy: More than 80% said when offline backups are used they could have a problem with the length of the backup window
- **2003** — Data restoration speed satisfaction: Nearly two-thirds of respondents said restoring critical data takes longer than they would like
- **2003** — Backup management burden: About half said operational management required for backup is a burden and management concern
- **2003** — Data restoration guarantee: Close to half would not guarantee all critical data can be restored on a given day
- **2003** — Fixed content prevalence: 60% of respondents reported having applications with very large non-changing/static data such as video images data warehouse detail data and old email
- **2003** — Low-cost storage purchase likelihood: 75% of storage buyers moderately or highly likely to buy mid-line storage in the coming year (40% highly likely; 33% moderately likely)
- **2003** — Current storage supplier discussion: 60% of respondents reported their current storage supplier had discussed low-cost storage options with them
- **2003** — Willingness to purchase higher-capacity lower-performance disks: More than one quarter showed high willingness; nearly half showed moderate willingness; only one quarter showed little or no willingness
- **2003** — Mid-line tier adoption outlook: Mid-line storage emerging in spite of storage buyer inertia with support of major disk drive manufacturers storage systems suppliers and early adopters
- **2007** — Mid-line storage adoption by 2007: [UNVERIFIED]
- **2003** — Cost comparison: 2TB backup appliance SCSI vs ATA: SCSI-based 2TB disk backup appliance: $15000-$20000; ATA-based equivalent: $7000-$10000 — roughly half price
- **2003** — Cost comparison: large FC array: In large FC-based disk array environments (>30 TB) saving more than $100000 off a $500000 deal still very significant even if percentage savings less dramatic
- **2003** — ILM adoption requirement: IT organizations need to focus on information life cycle and how content progressively moves through storage tiers as a function of value and access requirements
- **2006** — ILM adoption as standard enterprise planning: [UNVERIFIED]
- **2003** — ILM Principle 1 — Aging: Value and use of content change as content ages (birth/youth/middle age/old age); access drops dramatically as data ages
- **2003** — ILM Principle 2 — Freezing: Content changes from dynamic to fixed as updates cease — becoming read-only and therefore fixed content
- **2003** — ILM Principle 3 — Accumulation: As data amount increases frequency of access to particular piece drops; compliance with new regulations will further reinforce this tendency
- **2003** — ILM Principle 4 — Redundancy: More copies being made of content to ensure faster access and better data protection
- **2003** — Mid-line market size prediction: Aberdeen believes more than half of enterprise data will eventually fall into mid-line tier
- **2010** — 50%+ enterprise data in mid-line/SATA tier: [UNVERIFIED]
- **2003** — Survey methodology: 75 face-to-face and telephone interviews with storage managers at companies with $1B+ revenue including several Fortune 50-size businesses; financial services over-represented; US focus

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '04-mid-line-storage-v2-whitepaper-7db9bc' ORDER BY year_observed;
```

