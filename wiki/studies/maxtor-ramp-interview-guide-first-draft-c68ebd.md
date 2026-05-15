---
title: "Maxtor RAMP Interview Guide: First Draft"
slug: maxtor-ramp-interview-guide-first-draft-c68ebd
page_type: study
author: "Peter S. Kastner; David Hill (Aberdeen Group)"
date: "2003-03-01"
study_type: market-study
subject_domain: "enterprise-storage / disk-tiering / ILM"
methodology: "interview-design, ramp-survey-design, qualitative-research"
importance: high
importance_rationale: "First known structured qualitative instrument purpose-built to validate the market hypothesis that enterprises would accept a midline ATA disk tier — an idea that became the modern SATA nearline/midline tier adopted industry-wide by 2006."
relevance: medium
relevance_rationale: "The taxonomy of application I/O classes (OLTP write-intensive vs. BI read-intensive vs. large-file read-only) embedded in the guide remains a valid framework for storage tiering decisions; specific ATA/SCSI/FC distinctions are superseded by NVMe/SSD/SATA tiers."
prescience: high
prescience_rationale: "The interview framework anticipated storage tiering by activity classification, data retention lifecycle management, and cost/performance tradeoffs that became foundational to ILM (Information Lifecycle Management), HSM (Hierarchical Storage Management), and modern cloud storage classes (hot/cool/archive). The question on whether a \"storage hierarchy\" layer exists between performance disk and tape directly predicted the nearline tier now universally deployed."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 18
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Maxtor RAMP Interview Guide: First Draft

> Structured face-to-face interview guide developed by Aberdeen Group for the Maxtor RAMP (Rapid Accurate Market Prediction) project validating a proposed midline ATA disk storage tier. The guide covers 16 general storage questions and 18 per-application questions across three application tiers (primary database, primary file-based, and third application), plus miscellaneous questions on terminology awareness and CIO reporting lines. The instrument was designed to probe enterprise storage architectures (DAS/SAN/NAS), data activity patterns, backup/recovery regimes, retention policies, and willingness to trade availability for cost savings on cold data.

**Author:** Peter S. Kastner; David Hill (Aberdeen Group) · **Date:** 2003-03-01 · **Type:** market-study
**Importance:** high — *First known structured qualitative instrument purpose-built to validate the market hypothesis that enterprises would accept a midline ATA disk tier — an idea that became the modern SATA nearline/midline tier adopted industry-wide by 2006.*
**Prescience:** high — *The interview framework anticipated storage tiering by activity classification, data retention lifecycle management, and cost/performance tradeoffs that became foundational to ILM (Information Lifecycle Management), HSM (Hierarchical Storage Management), and modern cloud storage classes (hot/cool/ar…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[ibm|IBM]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[microsoft|Microsoft]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (18)

- [[ata-disk|ATA Hard Disk Drive]]
- [[cad-cam|CAD/CAM and Interactive Design]]
- [[das-external|External Direct-Attached Storage (DAS)]]
- [[das-internal|Internal Direct-Attached Storage (DAS)]]
- [[data-warehousing|Data Warehousing]]
- [[email-storage|Enterprise E-Mail Storage]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[nas|Network Attached Storage (NAS)]]
- [[oltp-app|Online Transaction Processing (OLTP)]]
- [[point-in-time-copy|Point-in-Time Copy / Snapshot]]
- [[raid-1|RAID 1 (Local Mirroring)]]
- [[raid-5|RAID 5 (Parity RAID)]]
- [[remote-mirroring|Remote Mirroring]]
- [[san|Storage Area Network (SAN)]]
- [[sap-r3|SAP R/3]]
- [[scsi-disk|SCSI Hard Disk Drive]]
- [[serial-ata|Serial ATA (SATA)]]
- [[tape-automation|Tape Automation]]

## Key observations (top 25)

- **2003** — Instrument type: Face-to-face structured RAMP interview guide
- **2003** — Storage architecture taxonomy — categories probed: Internal DAS / External DAS / SAN / NAS — four-way breakout
- **2003** — Disk technology taxonomy probed: SCSI / Fibre Channel / ATA — three technology types; size (GB) and rotational speed
- **2003** — Storage bottleneck hypothesis frame: Performance bottleneck sources: CPU / network / storage — three-way choice
- **2003** — SLA formalization — assumption: Not all enterprises have formal SLAs; probe for informal vs. formal availability/performance criteria
- **2003** — Tape automation infrastructure probed: Number of tape automation products / number of drives / number of slots
- **2003** — Backup window as pain point: Running out of backup window or jobs failing to complete — explicitly surfaced as known issue
- **2003** — Data retention policies probed: Retention criteria: age / transaction closure / regulatory — open-ended
- **2003** — Multi-copy data protection topology probed: On-disk copies / on-site tape copies / offsite DR tape copies — three-location model
- **2003** — Storage hierarchy gap hypothesis: Probes whether any storage tier exists BETWEEN high-performance disk and tape
- **2003** — Application classification framework: Eight application types across Database/File categories with I/O signatures
- **2003** — OLTP I/O signature — traditional: Update-intensive (both reads and writes; focus on writes)
- **2003** — Contemporary OLTP I/O signature: Mixed reads and writes — updating for transactions but also random reads (SAP R/3 cited)
- **2003** — Business Intelligence I/O signature: Query-intensive (primarily sequential reads)
- **2003** — E-mail storage I/O signature: Write-once / read-once-to-many times — personal productivity category
- **2003** — Midline migration acceptability — option A: Higher capacity disks with slightly lesser performance and availability — option for data migration
- **2003** — Data migration benefit framing — manageability vs. cost: Q18 probes whether benefit is manageability-focused or cost-focused
- **2003** — Storage array sharing assumption: Q7 probes whether arrays are shared across applications — and WHY if not
- **2003** — Cold data identification — phrasing: \"Data that spins around\" — closed transactions / old e-mail as migration candidates; estimated % of total
- **2003** — Third application threshold criteria: Must be ≥10% of total storage OR ≥0.5 TB to qualify for third application slot
- **2003** — Terminology awareness test — nearline storage: Term \"\"nearline storage\"\" tested for awareness
- **2003** — Terminology awareness test — active archiving: Term \"\"active archiving\"\" tested for awareness
- **2003** — Terminology awareness test — mezzanine storage: Term \"\"mezzanine storage\"\" tested for awareness
- **2003** — Disk capacity growth vs. speed divergence: Disk capacity increasing faster than rotational speed — acknowledged as a known tension
- **2003** — Disk capacity-speed divergence — outcome: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'maxtor-ramp-interview-guide-first-draft-c68ebd' ORDER BY year_observed;
```

