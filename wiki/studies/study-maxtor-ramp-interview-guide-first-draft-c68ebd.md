---
title: "Maxtor RAMP Interview Guide: First Draft"
slug: "study-maxtor-ramp-interview-guide-first-draft-c68ebd"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
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
study_prescience_enum: "low"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 1.83
prescience_obs_count: 30
---

# Maxtor RAMP Interview Guide: First Draft


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.87 over 30 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.27 over 30 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Structured face-to-face interview guide developed by Aberdeen Group for the Maxtor RAMP (Rapid Accurate Market Prediction) project validating a proposed midline ATA disk storage tier. The guide covers 16 general storage questions and 18 per-application questions across three application tiers (primary database, primary file-based, and third application), plus miscellaneous questions on terminology awareness and CIO reporting lines. The instrument was designed to probe enterprise storage architectures (DAS/SAN/NAS), data activity patterns, backup/recovery regimes, retention policies, and willingness to trade availability for cost savings on cold data.


_Published 2003, author **Peter S. Kastner; David Hill (Aberdeen Group)**, type **market-study**._


## Top observations

- Disk capacity increasing faster than rotational speed — acknowledged as a known tension `[ps=5]`
- Performance bottleneck sources: CPU / network / storage — three-way choice `[ps=4]`
- Not all enterprises have formal SLAs; probe for informal vs. formal availability/performance criteria `[ps=4]`
- Retention criteria: age / transaction closure / regulatory — open-ended `[ps=4]`
- Probes whether any storage tier exists BETWEEN high-performance disk and tape `[ps=4]`
- Mixed reads and writes — updating for transactions but also random reads (SAP R/3 cited) `[ps=4]`
- Higher capacity disks with slightly lesser performance and availability — option for data migration `[ps=4]`
- Maximum acceptable % full for disk storage — probed as management policy `[ps=4]`
- Internal DAS / External DAS / SAN / NAS — four-way breakout `[ps=3]`
- Running out of backup window or jobs failing to complete — explicitly surfaced as known issue `[ps=3]`
- On-disk copies / on-site tape copies / offsite DR tape copies — three-location model `[ps=3]`
- "Data that spins around" — closed transactions / old e-mail as migration candidates; estimated % of total `[ps=3]`
- Term ""active archiving"" tested for awareness `[ps=3]`
- SCSI / Fibre Channel / ATA — three technology types; size (GB) and rotational speed `[ps=2]`
- Must be ≥10% of total storage OR ≥0.5 TB to qualify for third application slot `[ps=2]`
- OS breakout: IBM mainframe / Unix / Windows / Other — matched to storage architecture and capacity `[ps=2]`
- Write-once / read-once-to-many times — personal productivity category `[ps=1]`
- Face-to-face structured RAMP interview guide `[ps=0]`
- Number of tape automation products / number of drives / number of slots `[ps=0]`
- Eight application types across Database/File categories with I/O signatures `[ps=0]`
- Update-intensive (both reads and writes; focus on writes) `[ps=0]`
- Query-intensive (primarily sequential reads) `[ps=0]`
- Q18 probes whether benefit is manageability-focused or cost-focused `[ps=0]`
- Q7 probes whether arrays are shared across applications — and WHY if not `[ps=0]`
- Term ""nearline storage"" tested for awareness `[ps=0]`
