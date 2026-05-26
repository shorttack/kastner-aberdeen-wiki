---
title: "Maxtor RAMP Interview Guide: First Draft"
slug: "study-maxtor-ramp-interview-guide-first-draft-c68ebd"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "maxtor-ramp-interview-guide-first-draft-c68ebd"
author: "Peter S. Kastner; David Hill (Aberdeen Group)"
date: "2003-03-01"
pub_year: 2003
type: "market-study"
subject_domain: "enterprise-storage / disk-tiering / ILM"
methodology: "interview-design, ramp-survey-design, qualitative-research"
source_file: "Maxtor RAMP Interview Guide First Draft.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Maxtor RAMP Interview Guide: First Draft

> Structured face-to-face interview guide developed by Aberdeen Group for the Maxtor RAMP (Rapid Accurate Market Prediction) project validating a proposed midline ATA disk storage tier. The guide covers 16 general storage questions and 18 per-application questions across three application tiers (primary database, primary file-based, and third application), plus miscellaneous questions on terminology awareness and CIO reporting lines. The instrument was designed to probe enterprise storage architectures (DAS/SAN/NAS), data activity patterns, backup/recovery regimes, retention policies, and willingness to trade availability for cost savings on cold data.


_Published 2003, author **Peter S. Kastner; David Hill (Aberdeen Group)**, type **market-study**._


## Top observations

- Face-to-face structured RAMP interview guide
- Internal DAS / External DAS / SAN / NAS — four-way breakout
- SCSI / Fibre Channel / ATA — three technology types; size (GB) and rotational speed
- Performance bottleneck sources: CPU / network / storage — three-way choice
- Not all enterprises have formal SLAs; probe for informal vs. formal availability/performance criteria
- Number of tape automation products / number of drives / number of slots
- Running out of backup window or jobs failing to complete — explicitly surfaced as known issue
- Retention criteria: age / transaction closure / regulatory — open-ended
- On-disk copies / on-site tape copies / offsite DR tape copies — three-location model
- Probes whether any storage tier exists BETWEEN high-performance disk and tape
- Eight application types across Database/File categories with I/O signatures
- Update-intensive (both reads and writes; focus on writes)
- Mixed reads and writes — updating for transactions but also random reads (SAP R/3 cited)
- Query-intensive (primarily sequential reads)
- Write-once / read-once-to-many times — personal productivity category
- Higher capacity disks with slightly lesser performance and availability — option for data migration
- Q18 probes whether benefit is manageability-focused or cost-focused
- Q7 probes whether arrays are shared across applications — and WHY if not
- "Data that spins around" — closed transactions / old e-mail as migration candidates; estimated % of total
- Must be ≥10% of total storage OR ≥0.5 TB to qualify for third application slot
- Term ""nearline storage"" tested for awareness
- Term ""active archiving"" tested for awareness
- Term ""mezzanine storage"" tested for awareness
- Disk capacity increasing faster than rotational speed — acknowledged as a known tension
- [UNVERIFIED]
