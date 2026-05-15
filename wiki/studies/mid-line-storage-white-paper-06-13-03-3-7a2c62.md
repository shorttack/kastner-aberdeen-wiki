---
title: "Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity"
slug: mid-line-storage-white-paper-06-13-03-3-7a2c62
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "2003-06-13"
study_type: white-paper
subject_domain: "Enterprise Storage / Information Lifecycle Management"
methodology: "Primary market research; 75 face-to-face and telephone interviews with storage managers at companies $1B+ revenue; survey research; analyst field research"
importance: high
importance_rationale: "Seminal white paper that defined and marketed the \"midline storage\" concept; co-invented by Kastner and Maxtor CMO Stephen DiFranco; shaped enterprise storage strategy for years to come"
relevance: high
relevance_rationale: "Serial ATA in enterprise storage became a massive market; this paper was ahead of the curve and accurately forecast SATA adoption"
prescience: high
prescience_rationale: "The midline storage concept proved enormously successful; SATA drives became the standard enterprise storage tier; ILM terminology became industry standard"
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 15
obs_count: 40
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Mid-Line Disk Storage: Emerging as Significant Cost-Saving Opportunity

> Seminal Aberdeen Group white paper defining \"mid-line storage\" as a new enterprise storage tier between high-performance Fibre Channel/SCSI disks and tape. Based on primary research with 75 storage managers at $1B+ enterprises. Defines four-level storage pyramid with mid-line ATA disks as a distinct tier. Key findings: ATA disks offer 2-8x capacity of FC/SCSI at ~half the cost per GB; 75% of storage buyers moderately or highly likely to purchase mid-line storage; over 60% report data restorations more than once a year; over 80% face backup window problems. Introduces Information Lifecycle Management (ILM) framework. Authored by Peter Kastner and David Hill of Aberdeen Group; sponsored by Maxtor Corporation.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 2003-06-13 · **Type:** white-paper
**Importance:** high — *Seminal white paper that defined and marketed the \"midline storage\" concept; co-invented by Kastner and Maxtor CMO Stephen DiFranco; shaped enterprise storage strategy for years to come*
**Prescience:** high — *The midline storage concept proved enormously successful; SATA drives became the standard enterprise storage tier; ILM terminology became industry standard*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill-aberdeen|David Hill]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (15)

- [[continuous-data-protection|Continuous Data Protection (CDP)]]
- [[data-warehouse|Data Warehouse / Business Intelligence]]
- [[disk-based-backup-appliance|Disk-Based Backup Appliance (ATA)]]
- [[fibre-channel-disk|Fibre Channel (FC) Disk]]
- [[magnetic-tape|Magnetic Tape (off-line storage)]]
- [[nas|Network Attached Storage (NAS)]]
- [[oltp-systems|Online Transaction Processing (OLTP)]]
- [[raid|RAID (Redundant Array of Independent Disks)]]
- [[ram-storage|RAM-based Storage (volatile)]]
- [[san|Storage Area Network (SAN)]]
- [[sap-r3|SAP R/3 (mixed applications)]]
- [[scsi-disk|SCSI Disk]]
- [[serial-ata|Serial ATA (SATA) / ATA Disks]]
- [[solid-state-disk|Solid State Disk (SSD)]]
- [[storage-management-software|Storage Management / HSM Software]]

## Key observations (top 25)

- **2003** — enterprises_using_fc_scsi_only: >50%
- **2003** — enterprise_data_eligible_for_midline: >20% immediately; >50% eventually
- **2003** — likely_to_purchase_midline: 75%
- **2003** — data_restoration_more_than_once_per_year: >60%
- **2003** — data_restore_monthly_or_more: 20%
- **2003** — restore_takes_longer_than_desired: ~67%
- **2003** — backup_management_burden: ~50%
- **2003** — cannot_guarantee_full_restore: ~50%
- **2003** — backup_window_problem: >80%
- **2003** — ata_capacity_vs_fc_scsi: 2x to 8x; up to 300 GB per ATA vs 142/72/36 GB per FC/SCSI
- **2003** — ata_cost_vs_fc_scsi_per_gb: ~half the cost per GB
- **2003** — scsi_vs_ata_cost_ratio: up to 5x higher
- **2003** — ata_backup_appliance_2tb_price: $7,000-$10,000
- **2003** — scsi_backup_appliance_2tb_price: $15,000-$20,000
- **2003** — midline_savings_large_environment: >$100,000 off deals formerly $500,000+
- **2003** — high_willingness_to_buy_midline: >25%
- **2003** — moderate_willingness_to_buy_midline: ~50%
- **2003** — supplier_discussed_low_cost_storage: 60%
- **2003** — highly_likely_to_buy_low_cost_storage: ~40%
- **2003** — enterprises_with_static_large_data: 60%
- **2003** — survey_sample_size: 75
- **2003** — ilm_principles: Ageing, Freezing, Accumulation, Redundancy
- **2003** — storage_pyramid_tiers: RAM (volatile), High-Perf Disk (FC/SCSI), Mid-Line Disk (ATA), Tape (off-line)
- **2003** — oltp_closed_transactions_midline: Eligible after transaction closure (shipped orders etc.)
- **2003** — data_warehouse_midline_applicability: High — query intensive, primarily sequential reads; cost-per-GB compelling

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'mid-line-storage-white-paper-06-13-03-3-7a2c62' ORDER BY year_observed;
```

