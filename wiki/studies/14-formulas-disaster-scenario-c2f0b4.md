---
title: "Formulas for Disaster Recovery Scenario"
slug: 14-formulas-disaster-scenario-c2f0b4
page_type: study
author: "Aberdeen Group"
date: "2003-01-01"
study_type: case-analysis
subject_domain: "enterprise-storage"
methodology: "financial-modeling, disaster-recovery, tco-analysis"
importance: high
importance_rationale: "Companion financial model to study 13; together these documents represent the complete TCO toolkit developed by Aberdeen for the Maxtor midline category launch. Historical benchmark for enterprise disaster recovery economics in the early SAN era."
relevance: high
relevance_rationale: "Multi-stage disaster recovery time model with parallel recovery paths is directly applicable to modern hybrid cloud architectures; the formula structure (downtime = outage time + recovery time; parallel recovery advantages) is still valid for evaluating object storage vs block storage recovery."
prescience: high
prescience_rationale: "Predicted parallel recovery always outperforms single-path tape recovery; confirmed by industry adoption of disk-to-disk backup and cloud-based disaster recovery. Minimum recovery time at 1/3 of Old Way proved accurate as disk/disk became standard primary DR mechanism."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 5
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Formulas for Disaster Recovery Scenario

> Companion document to the downtime strategy formulas, applying similar financial modeling to disaster recovery scenarios. Defines a multi-stage recovery time model comparing old tape-based architecture to a new midline disk hybrid. Uses an online book/CD seller scenario (modeled on Amazon.com) with 50,000 customers/hour at $20-30/order to quantify revenue impact of improved recovery time. Models parallel disk/disk and disk/tape recovery paths to show New Way always recovers faster than Old Way, with minimum recovery time at 1/3 of Old Way.

**Author:** Aberdeen Group · **Date:** 2003-01-01 · **Type:** case-analysis
**Importance:** high — *Companion financial model to study 13; together these documents represent the complete TCO toolkit developed by Aberdeen for the Maxtor midline category launch. Historical benchmark for enterprise disaster recovery economics in the early SAN era.*
**Prescience:** high — *Predicted parallel recovery always outperforms single-path tape recovery; confirmed by industry adoption of disk-to-disk backup and cloud-based disaster recovery. Minimum recovery time at 1/3 of Old Way proved accurate as disk/disk became standard primary DR mechanism.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[amazon|Amazon.com]]
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

- **2003** — Benefits formula structure: Benefits = (admin cost savings) + (additional revenue from New solution) + (opportunity cost savings) [optionally plus acquisition cost difference]
- **2003** — Old Way acquisition cost: Cost/GB (online disk) * GB online + cost/GB (nearline tape) * GB nearline + cost/GB (offline tape) * GB offline
- **2003** — New Way acquisition cost: Cost/GB online * GB online + cost/GB midline * GB midline + cost/GB nearline disk * GB nearline disk + cost/GB nearline tape * GB nearline tape + cost/GB offline tape * GB offline tape
- **2003** — Storage conservation constraint: GB online (New) + GB midline (New) = GB online (Old); GB nearline disk (New) + GB nearline tape (New) = GB nearline tape (Old)
- **2003** — Admin cost savings rate: $100K salary * 1/10000 hours/year = $10/hour; if New Solution saves 5 hours recovery time then $50 admin savings
- **2003** — Recovery time formula: Downtime = Outage Time + Recovery Time; one-minute electrical disruption + 5 minutes boot = 6 minute constant outage time for both scenarios
- **2003** — Old Way recovery time: Recovery time (Old Way) = GB on online disk / 800 GB/hr (disk-to-tape rate)
- **2003** — New Way recovery time formula: Recovery time (New Way) = max(disk/disk recovery time, disk/tape recovery time); disk/disk: GB online / 1600 GB/hr; disk/tape: GB midline / 800 GB/hr; parallel execution
- **2003** — New Way always faster: New Way is always faster than Old Way regardless of storage allocation
- **2003** — Minimum recovery time: Absolute minimum recovery time of New Way is 1/3 of Old Way when amount on online disk (Stage 1) = 2 x amount on midline disk (Stage 1)
- **2003** — Recovery rate disk-to-tape: 800 GB/hr
- **2003** — Recovery rate disk-to-disk: 1600 GB/hr
- **2003** — Disaster scenario parameters: Online book/CD seller modeled on Amazon.com; 50000 customers/hour; $20-30/order; $1.5M revenue/hour at risk; crash during peak business hours
- **2003** — LTO-2 tape library pricing (same as study 13): $130K for 8-drive 200-slot system; $20K media; total $150K; 80TB; $1.90/GB
- **2003** — Nearline disk appliance pricing (same as study 13): 20TB nearline disk: $100K at $5/GB; 4-drive 100-slot tape library: $85K + $10K media = $95K; combo $195K
- **2003** — High-end online disk price (same as study 13): $31.60/GB (HDS 9980V with 146GB disks)
- **2003** — Midrange online disk price (same as study 13): $13.30/GB (EMC CX600 with 146GB disks)
- **2003** — Midline disk price (same as study 13): $9.30/GB
- **2003** — Additional revenue formula: Additional revenue for New Solution = customers served/hour * $/customer * recovery time saved
- **2003** — Stage clock time model: Stage 3: disk/disk recovery time (New Way); Stage 4: disk/tape - disk/disk recovery time; Stage 5: Old Way - New Way recovery time (1/2 to 2/3 of Old Way)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '14-formulas-disaster-scenario-c2f0b4' ORDER BY year_observed;
```

