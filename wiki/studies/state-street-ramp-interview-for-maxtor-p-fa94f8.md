---
title: "State Street RAMP Interview for Maxtor Project"
slug: state-street-ramp-interview-for-maxtor-p-fa94f8
page_type: study
author: "Peter S. Kastner; David Hill"
date: "2003-04-01"
study_type: market-study
subject_domain: "enterprise-storage / financial-services"
methodology: "face-to-face-interview, market-research, vendor-evaluation"
importance: high
importance_rationale: "First-person face-to-face interview with a senior financial services IT executive on ATA/low-cost disk adoption; rare primary source capturing banking-sector storage decision-making in 2003 at a systemically important institution (State Street). Provides ground-truth demand signal for the nascent midline storage market."
relevance: high
relevance_rationale: "Financial sector storage consolidation onto SAN, TCO-driven purchasing pressure, multi-decision-maker enterprise buying patterns, and the tension between SLA obligations and cost reduction remain directly applicable to storage procurement and vendor positioning today."
prescience: high
prescience_rationale: "Thakuria's willingness to adopt low-cost disk even for SLA-bound production workloads serving Fidelity proved prescient: financial services became one of the earliest and largest adopters of SATA/nearline SAS; TCO-driven consolidation onto tiered SAN architectures is now universal. His insight about siloed purchasing decision-making in large enterprises presaged the decades-long struggle vendors faced penetrating multi-platform accounts."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 10
obs_count: 35
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# State Street RAMP Interview for Maxtor Project

> Face-to-face RAMP (Rapid Analysis Market Profiling) interview with Prithwi R. Thakuria, VP Information Technology Data Management Services at State Street (Westwood MA), covering Unix SAN storage architecture, willingness to adopt low-cost ATA disk, EMC Symmetrix/DMX infrastructure, and backup/restore practices. State Street had ~1TB Unix storage, all on SAN, 70-80% FC, with EMC Symmetrix RAID-1 and planned DMX upgrade. Thakuria rated 7/7 likelihood to purchase low-cost disk despite SLA obligations to investment management clients, citing TCO savings. The interview captures the financial sector's early-mover posture toward midline storage and the multi-silo purchasing decision structure of large banks.

**Author:** Peter S. Kastner; David Hill · **Date:** 2003-04-01 · **Type:** market-study
**Importance:** high — *First-person face-to-face interview with a senior financial services IT executive on ATA/low-cost disk adoption; rare primary source capturing banking-sector storage decision-making in 2003 at a systemically important institution (State Street). Provides ground-truth demand signal for the nascent mi…*
**Prescience:** high — *Thakuria's willingness to adopt low-cost disk even for SLA-bound production workloads serving Fidelity proved prescient: financial services became one of the earliest and largest adopters of SATA/nearline SAS; TCO-driven consolidation onto tiered SAN architectures is now universal. His insight about…*

## Entities (8)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[emc|EMC Corporation]]
- [[fidelity-investments|Fidelity Investments]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[prithwi-r-thakuria|Prithwi R. Thakuria]]
- [[state-street|State Street Corporation]]

## Technologies (10)

- [[ata-disk|ATA (IDE) Disk / Low-Cost Disk]]
- [[emc-dmx|EMC DMX (Symmetrix DMX)]]
- [[emc-symmetrix|EMC Symmetrix]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[lotus-notes|Lotus Notes]]
- [[microsoft-exchange|Microsoft Exchange]]
- [[raid-1|RAID-1 (Mirroring)]]
- [[san|Storage Area Network (SAN)]]
- [[scsi-disk|SCSI Disk]]
- [[tape-library|Tape Library]]

## Key observations (top 25)

- **2003** — Company revenue: Greater than $5 billion
- **2003** — Total IT budget: $129 million
- **2003** — CIO reporting line: Reports to President/CEO
- **2003** — Unix storage available: Approximately 1 TB
- **2003** — Unix storage allocated: Approximately 600 GB
- **2003** — Expected Unix storage growth (12 months): 15%
- **2003** — Maximum desired storage utilization: 80%
- **2003** — Storage network topology: 100% SAN (Unix)
- **2003** — FC percentage of Unix storage: 70-80%
- **2003** — SCSI percentage of Unix storage: 20-30%
- **2003** — Primary storage platform: EMC Symmetrix (RAID-1)
- **2003** — Planned platform upgrade: EMC Symmetrix → DMX
- **2003** — Actual outcome: EMC DMX adoption in financial services: [UNVERIFIED]
- **2003** — Disaster recovery strategy: All production systems replicated to second data center
- **2003** — OLTP data profile: Read-write (not seldom-written)
- **2003** — Data warehouse data profile: Read-only
- **2003** — Email data classification (view): Read-only or seldom-written
- **2003** — Corporate Actions blob/large-object classification: Not read-only (part of workflow)
- **2003** — Willingness: higher capacity + 50% cost reduction + slight availability reduction (7-point scale): 6 out of 7
- **2003** — Willingness: same capacity + 30% cost reduction + slight availability reduction (7-point scale): 2 out of 7
- **2003** — Likelihood to purchase low-cost disk in next 12 months (7-point scale): 7 out of 7 — maximum likelihood
- **2003** — Storage vendor discussion of low-cost options: Not yet discussed
- **2003** — Backup window: 12 AM to 6 AM (6 hours)
- **2003** — Backup generations retained: 3 generations
- **2003** — Data retention period: 10 years

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'state-street-ramp-interview-for-maxtor-p-fa94f8' ORDER BY year_observed;
```

