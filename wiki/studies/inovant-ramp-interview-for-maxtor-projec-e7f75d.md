---
title: "RAMP Interview: Inovant / Visa (Maxtor Midline Storage Study)"
slug: inovant-ramp-interview-for-maxtor-projec-e7f75d
page_type: study
author: "Peter S. Kastner, David Hill"
date: "2003-04-01"
study_type: market-study
subject_domain: "enterprise-storage / financial-sector-storage / midline-disk-evaluation"
methodology: "ramp-interview, face-to-face, industry-analysis"
importance: high
importance_rationale: "Captures payment processing industry's storage requirements at the ATA/SATA transition inflection point; documents the specific financial-sector SLA barriers that defined which verticals would and would not adopt midline storage — directly relevant to later tiered-storage market segmentation."
relevance: high
relevance_rationale: "Financial sector storage requirements, compliance-driven retention, and customer-facing application SLA rigidity remain central to storage purchasing decisions; Inovant's model presaged modern banking sector's tiered-storage resistance and eventual selective cloud adoption."
prescience: high
prescience_rationale: "The study accurately predicted that customer-facing financial applications would resist low-cost disk (proven correct for primary tier through the 2000s). The image archive use case foreshadowed compliance archival as the dominant nearline workload. The study did not foresee S3/object storage eventually solving the static-image problem at extreme cost efficiency by ~2010."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 12
obs_count: 34
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# RAMP Interview: Inovant / Visa (Maxtor Midline Storage Study)

> Face-to-face RAMP interview with Paul Orleman, Department Head for Direct Exchange Infrastructure at Inovant (Visa's technology subsidiary), capturing the financial-sector perspective on ATA midline storage adoption. Inovant operated 20TB with 30% utilization, 95% Fibre Channel, and rated willingness to adopt low-cost disk at only 2/7 due to extreme SLA requirements for member bank transactions. The credit card dispute image application (10TB, 50% read-only, DB2) represented a major static-data use case that theoretically suited lower-cost storage but was protected by availability requirements too stringent to permit migration.

**Author:** Peter S. Kastner, David Hill · **Date:** 2003-04-01 · **Type:** market-study
**Importance:** high — *Captures payment processing industry's storage requirements at the ATA/SATA transition inflection point; documents the specific financial-sector SLA barriers that defined which verticals would and would not adopt midline storage — directly relevant to later tiered-storage market segmentation.*
**Prescience:** high — *The study accurately predicted that customer-facing financial applications would resist low-cost disk (proven correct for primary tier through the 2000s). The image archive use case foreshadowed compliance archival as the dominant nearline workload. The study did not foresee S3/object storage eventu…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill-aberdeen|David Hill]]
- [[dell|Dell]]
- [[emc|EMC Corporation]]
- [[ibm|IBM]]
- [[inovant|Inovant (a Visa Solutions Company)]]
- [[maxtor|Maxtor Corporation]]
- [[netapp|NetApp (Network Appliance)]]
- [[paul-orleman-inovant|Paul Orleman]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[visa|Visa Inc.]]
- [[z-force|Z-Force]]

## Technologies (12)

- [[ata-disk|ATA Disk (IDE/ATA-100)]]
- [[credit-card-dispute-image-app|Credit Card Dispute Image Application]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[ibm-3584-tape-library|IBM 3584 Tape Library]]
- [[ibm-db2|IBM DB2]]
- [[lto|LTO (Linear Tape Open)]]
- [[nas|Network Attached Storage (NAS)]]
- [[oltp-systems|Online Transaction Processing (OLTP)]]
- [[optical-storage|Optical Storage]]
- [[raid-1|RAID 1 (Mirroring)]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[virtual-tape|Virtual Tape Library (VTL)]]

## Key observations (top 25)

- **2003** — total-storage-tb: 20 TB
- **2003** — storage-utilization-pct: 30%
- **2003** — it-budget: $70M
- **2003** — os-split: 10% Windows / 90% Unix-Linux
- **2003** — storage-architecture-split: Windows=100% DAS / Unix-Linux=100% NAS
- **2003** — disk-interface-split: 5% SCSI / 95% FC
- **2003** — windows-storage-growth-12mo: 50%
- **2003** — unix-linux-storage-growth-12mo: 75%
- **2003** — willingness-higher-capacity-50pct-cost-reduction: 2 of 7
- **2003** — willingness-same-capacity-less-availability-30pct-reduction: 2 of 7
- **2003** — likelihood-of-purchase-12mo: 3 of 7
- **2003** — availability-requirement: supercritical
- **2003** — read-only-data-pct: 50%
- **2003** — dispute-image-app-size-tb: 10 TB
- **2003** — dispute-app-growth-driver: growth as more banks sign up
- **2003** — dispute-app-topology: DB2 centralized; replication planned
- **2003** — data-center-locations: San Mateo CA (15TB); McLean VA (5TB); Denver CO
- **2003** — tape-copies-onsite: 8-10
- **2003** — backup-window-status: no problem with window but jobs fail at unacceptable rate
- **2003** — restore-frequency: less than once per year
- **2003** — customer-facing-storage-thesis: Organizations running customer-facing applications with strong SLAs will not consider low-cost disk for those applications
- **2003** — decision-maker-identification-insight: Applications development organizations with cradle-to-grave responsibility may be actual storage decision makers over ops
- **2003** — adoption-change-management-challenge: Challenge is to change thinking about which applications could use low-cost disk alternatives
- **2003** — primary-storage-vendor: EMC
- **2003** — storage-staffing: dedicated full-time storage team

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'inovant-ramp-interview-for-maxtor-projec-e7f75d' ORDER BY year_observed;
```

