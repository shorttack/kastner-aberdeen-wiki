---
title: "Time Compression - Downtime Strategy: Formulas and Business Case"
slug: 13-hh-time-compression-downtime-strategy-4e50c9
page_type: study
author: "David Hill (HH), Aberdeen Group"
date: "2003-01-01"
study_type: case-analysis
subject_domain: "enterprise-storage"
methodology: "financial-modeling, tco-analysis, benchmark"
importance: high
importance_rationale: "Primary quantitative tool developed to justify enterprise adoption of midline storage; shows how Aberdeen constructed ROI arguments for the Pools of Storage/midline category; pricing benchmarks from 2003/2004 provide valuable historical record of enterprise storage economics."
relevance: high
relevance_rationale: "Financial modeling methodology for storage TCO using backup time savings and customer revenue impact per hour is still directly applicable; the basic formula structure (old way vs new way cost comparison with opportunity cost factor) remains standard in storage business case analysis."
prescience: high
prescience_rationale: "Predicted midline disk at approximately 70% of midrange online disk cost ($9.30/GB vs $13.30/GB); SATA enterprise pricing did track at similar discounts to FC/SCSI. Backup time compression modeling correctly anticipated the parallel backup strategies that became standard in enterprise storage architectures."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 5
obs_count: 18
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Time Compression - Downtime Strategy: Formulas and Business Case

> Working document containing financial formulas and a detailed business case for demonstrating TCO savings from migrating from traditional tape-based nearline storage to a midline disk plus tape combination. Models downtime reduction for a large financial services company with 1 million customers by quantifying backup time savings and customer revenue impact. Provides specific dollar-per-GB pricing for online (HDS 9980V at $31.60/GB) midline ($9.30/GB) and nearline disk/tape systems.

**Author:** David Hill (HH), Aberdeen Group · **Date:** 2003-01-01 · **Type:** case-analysis
**Importance:** high — *Primary quantitative tool developed to justify enterprise adoption of midline storage; shows how Aberdeen constructed ROI arguments for the Pools of Storage/midline category; pricing benchmarks from 2003/2004 provide valuable historical record of enterprise storage economics.*
**Prescience:** high — *Predicted midline disk at approximately 70% of midrange online disk cost ($9.30/GB vs $13.30/GB); SATA enterprise pricing did track at similar discounts to FC/SCSI. Backup time compression modeling correctly anticipated the parallel backup strategies that became standard in enterprise storage archit…*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[emc|EMC Corporation]]
- [[hitachi-data-systems|Hitachi Data Systems]]

## Technologies (5)

- [[emc-cx600|EMC CLARiiON CX600]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[hds-9980v|HDS StorageWorks 9980V]]
- [[lto|LTO (Linear Tape Open)]]
- [[midline-storage|Midline Storage]]

## Key observations (top 25)

- **2003** — Total savings formula structure: Savings 1 (initial cost savings) + Savings 2 (backup time compression savings); includes opportunity cost savings at 0.6 multiplier
- **2003** — Old Way storage cost formula: CostO = cost(E GB online disk) + cost(G GB nearline tape) + cost(H GB offline tape)
- **2003** — New Way storage cost formula: CostN = cost(E/2 online disk) + cost(E/2 midline disk) + cost(G/2 nearline disk) + cost(G/2 nearline tape) + cost(H offline tape); assumes online disk split in half and nearline tape split in half
- **2003** — Opportunity cost multiplier: Opportunity cost savings = 0.6 * direct cost savings from New solution
- **2003** — Backup time savings formula: Old Way: A = M/X hours; New Way: B = M/(2X) hours (parallel backup); backup time saved = A - B = M/(2X)
- **2003** — Backup disk-to-tape rate: X = 800 GB/hr
- **2003** — Backup disk-to-disk rate: Y = 1600 GB/hr
- **2003** — Financial services example parameters: Medium/large financial services company; 1 million customers; 100K overseas business customers; 120 customers served/hour; $100/customer
- **2003** — Critical data volume assumption: E = 3 TB critical data requiring backup
- **2003** — LTO-2 tape library pricing: $130K for 8-drive 200-slot system; LTO-2 (400MB/cartridge at 40MB/sec 2:1 compression); $20K media (100/cartridge); total $150K; 80TB capacity; $1.90/GB
- **2003** — Nearline disk appliance pricing: 20TB nearline disk: $100K at $5/GB; 4-drive 100-slot tape library: $85K + $10K media = $95K; 40TB tape capacity at $2.50/GB; total combo: $195K
- **2003** — High-end online disk price: $31.60/GB (HDS 9980V with 146GB disks)
- **2003** — Midrange online disk price: $13.30/GB (EMC CX600 with 146GB disks)
- **2003** — Midline disk price: $9.30/GB (70% of EMC midrange price)
- **2003** — Admin cost rate: $10/hour ($100K salary * 1/10000 hours per year)
- **2003** — Customer revenue impact formula: Savings 2 = (customers served/hour * $/customer * backup time saved) + ($10 * backup time saved in hours)
- **2003** — Midline disk cost advantage persistence: Midline disk at 70% of midrange ($9.30/GB vs $13.30/GB) will enable measurable TCO savings in New Way architecture
- **2003** — Midline cost advantage verification: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '13-hh-time-compression-downtime-strategy-4e50c9' ORDER BY year_observed;
```

