---
title: "RAMP Interview: Applied Materials (Maxtor Midline Storage Study)"
slug: applied-materials-ramp-interview-for-max-fd966d
page_type: study
author: "Peter S. Kastner, David Hill"
date: "2003-04-01"
study_type: market-study
subject_domain: "enterprise-storage / midline-disk-evaluation"
methodology: "ramp-interview, face-to-face, industry-analysis"
importance: medium
importance_rationale: "Primary market-validation data point in Aberdeen's RAMP study for Maxtor; captures enterprise ATA adoption sentiment from a major semiconductor equipment manufacturer at the exact inflection point of ATA-to-SATA transition."
relevance: high
relevance_rationale: "Storage tiering, availability SLAs, and the tension between cost reduction and reliability remain central to enterprise storage decisions; the 6/7 vs. 1/7 availability-willingness gap is still a relevant framework for flash/cloud tiering decisions."
prescience: medium
prescience_rationale: "The strong rejection of availability trade-offs (1/7) accurately predicted enterprise resistance to early ATA; however, the study underestimated how SATA would eventually resolve availability parity — and neither participant foresaw SSD/flash eliminating the cost-reliability trade-off entirely by ~2015."
license: CC-BY-4.0
tier: 2
entity_count: 10
tech_count: 13
obs_count: 32
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# RAMP Interview: Applied Materials (Maxtor Midline Storage Study)

> Face-to-face RAMP interview with Bill Foley, Director of Computing & Intranet Services at Applied Materials (Santa Clara CA), documenting enterprise storage practices and willingness-to-adopt ATA/low-cost disk alternatives. Applied Materials operated 16-20TB of Windows storage with 80% DAS / 20% SAN, rating high willingness for capacity at lower cost (6/7) but zero willingness for any availability reduction (1/7). The interview surfaced a foundational insight: IT managers perceive applications and availability holistically, making even marginal reliability trade-offs unacceptable — a signal that positioned the midline storage market.

**Author:** Peter S. Kastner, David Hill · **Date:** 2003-04-01 · **Type:** market-study
**Importance:** medium — *Primary market-validation data point in Aberdeen's RAMP study for Maxtor; captures enterprise ATA adoption sentiment from a major semiconductor equipment manufacturer at the exact inflection point of ATA-to-SATA transition.*
**Prescience:** medium — *The strong rejection of availability trade-offs (1/7) accurately predicted enterprise resistance to early ATA; however, the study underestimated how SATA would eventually resolve availability parity — and neither participant foresaw SSD/flash eliminating the cost-reliability trade-off entirely by ~2…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[applied-materials|Applied Materials Inc.]]
- [[bill-foley-applied-materials|Bill Foley]]
- [[compaq|Compaq]]
- [[david-hill-aberdeen|David Hill]]
- [[emc|EMC Corporation]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[maxtor|Maxtor Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (13)

- [[ata-disk|ATA Disk (IDE/ATA-100)]]
- [[cad-cam-software|CAD/CAM Software]]
- [[emc-symmetrix|EMC Symmetrix]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[lotus-notes|Lotus Notes]]
- [[lto|LTO (Linear Tape Open)]]
- [[nas|Network Attached Storage (NAS)]]
- [[raid-5|RAID 5 (Striping with Parity)]]
- [[san|Storage Area Network (SAN)]]
- [[sap-oracle|SAP on Oracle (Unix)]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[serial-ata|Serial ATA (SATA)]]
- [[ssd|Solid State Drives (SSD)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'applied-materials-ramp-interview-for-max-fd966d' ORDER BY year_observed;
```

