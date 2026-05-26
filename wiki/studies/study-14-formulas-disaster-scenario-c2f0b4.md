---
title: "Formulas for Disaster Recovery Scenario"
slug: "study-14-formulas-disaster-scenario-c2f0b4"
page_type: "study"
tags: ["type/study", "collection/case-analysis"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "14-formulas-disaster-scenario-c2f0b4"
author: "Aberdeen Group"
date: "2003-01-01"
pub_year: 2003
type: "case-analysis"
subject_domain: "enterprise-storage"
methodology: "financial-modeling, disaster-recovery, tco-analysis"
source_file: "14-Formulas-Disaster-Scenario.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Formulas for Disaster Recovery Scenario

> Companion document to the downtime strategy formulas, applying similar financial modeling to disaster recovery scenarios. Defines a multi-stage recovery time model comparing old tape-based architecture to a new midline disk hybrid. Uses an online book/CD seller scenario (modeled on Amazon.com) with 50,000 customers/hour at $20-30/order to quantify revenue impact of improved recovery time. Models parallel disk/disk and disk/tape recovery paths to show New Way always recovers faster than Old Way, with minimum recovery time at 1/3 of Old Way.


_Published 2003, author **Aberdeen Group**, type **case-analysis**._


## Top observations

- Benefits = (admin cost savings) + (additional revenue from New solution) + (opportunity cost savings) [optionally plus acquisition cost difference]
- Cost/GB (online disk) * GB online + cost/GB (nearline tape) * GB nearline + cost/GB (offline tape) * GB offline
- Cost/GB online * GB online + cost/GB midline * GB midline + cost/GB nearline disk * GB nearline disk + cost/GB nearline tape * GB nearline tape + cost/GB offline tape * GB offline tape
- GB online (New) + GB midline (New) = GB online (Old); GB nearline disk (New) + GB nearline tape (New) = GB nearline tape (Old)
- $100K salary * 1/10000 hours/year = $10/hour; if New Solution saves 5 hours recovery time then $50 admin savings
- Downtime = Outage Time + Recovery Time; one-minute electrical disruption + 5 minutes boot = 6 minute constant outage time for both scenarios
- Recovery time (Old Way) = GB on online disk / 800 GB/hr (disk-to-tape rate)
- Recovery time (New Way) = max(disk/disk recovery time, disk/tape recovery time); disk/disk: GB online / 1600 GB/hr; disk/tape: GB midline / 800 GB/hr; parallel execution
- New Way is always faster than Old Way regardless of storage allocation
- Absolute minimum recovery time of New Way is 1/3 of Old Way when amount on online disk (Stage 1) = 2 x amount on midline disk (Stage 1)
- 800 GB/hr
- 1600 GB/hr
- Online book/CD seller modeled on Amazon.com; 50000 customers/hour; $20-30/order; $1.5M revenue/hour at risk; crash during peak business hours
- $130K for 8-drive 200-slot system; $20K media; total $150K; 80TB; $1.90/GB
- 20TB nearline disk: $100K at $5/GB; 4-drive 100-slot tape library: $85K + $10K media = $95K; combo $195K
- $31.60/GB (HDS 9980V with 146GB disks)
- $13.30/GB (EMC CX600 with 146GB disks)
- $9.30/GB
- Additional revenue for New Solution = customers served/hour * $/customer * recovery time saved
- Stage 3: disk/disk recovery time (New Way); Stage 4: disk/tape - disk/disk recovery time; Stage 5: Old Way - New Way recovery time (1/2 to 2/3 of Old Way)
