---
title: "Maxtor ILM Pools of Storage Strategy Event Data Collection Template"
slug: 18-maxtor-strategy-event-template-faeb40
page_type: study
author: "Aberdeen Group"
date: "2003-01-01"
study_type: employer-record
subject_domain: "storage-strategy / interactive-tool"
methodology: "document-review"
importance: high
importance_rationale: "Provides the technical specification of the Hardware Hawker tool's scenario engine — the core mechanism by which Aberdeen and Maxtor translated ILM storage theory into customer-specific ROI models; documents the first purpose-built ILM cost justification tool."
relevance: medium
relevance_rationale: "The data model — structured vs. semi-structured vs. unstructured data volumes mapped to tiered storage costs and bottom-line benefits — remains the standard ROI framework for storage tiering and cloud storage migration analyses."
prescience: high
prescience_rationale: "Predicted that enterprise customers would respond to quantified cost-per-GB and bottom-line-benefit models as the primary ILM adoption driver; this TCO/ROI approach to storage decisions became standard in cloud migration and storage modernization sales by 2010."
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 8
obs_count: 16
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Maxtor ILM Pools of Storage Strategy Event Data Collection Template

> A template specification extracted from the Hardware Hawker (HH) ILM/Pools of Storage interactive sales tool, defining the data input fields and scenario structure for Strategy Events. Each Strategy Event models a customer's data environment across structured, semi-structured, and unstructured data; storage tiers (online disk, nearline tape, offline tape, midline disk, nearline disk); cost-per-GB parameters; and workflow flow directions. The template supports iterative scenario modeling with duplicate slides for sequential steps, quantifying bottom-line benefits from storage tier migration including downtime savings, admin management savings, opportunity cost savings, and revenue operations improvements.

**Author:** Aberdeen Group · **Date:** 2003-01-01 · **Type:** employer-record
**Importance:** high — *Provides the technical specification of the Hardware Hawker tool's scenario engine — the core mechanism by which Aberdeen and Maxtor translated ILM storage theory into customer-specific ROI models; documents the first purpose-built ILM cost justification tool.*
**Prescience:** high — *Predicted that enterprise customers would respond to quantified cost-per-GB and bottom-line-benefit models as the primary ILM adoption driver; this TCO/ROI approach to storage decisions became standard in cloud migration and storage modernization sales by 2010.*

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[maxtor|Maxtor Corporation]]

## Technologies (8)

- [[hardware-hawker|Hardware Hawker (HH) Tool]]
- [[ilm|Information Lifecycle Management (ILM)]]
- [[midline-storage|Midline Storage]]
- [[nearline-disk|Nearline Disk Storage]]
- [[nearline-tape|Nearline Tape Storage]]
- [[offline-tape|Offline Tape Storage]]
- [[online-disk|Online Disk Storage]]
- [[pools-of-storage|Pools of Storage (PoS)]]

## Key observations (top 25)

- **2003** — Tool scenario structure: One Strategy Event = one scenario; each with sequential Steps duplicated from slide master
- **2003** — Data classification dimensions in tool model: Three data types: Structured; Semi-Structured; Unstructured — each with percentage allocation
- **2003** — Storage tier dimensions in tool model: Seven tiers modeled: Online disk; Nearline tape; Offline tape; Online disk; Nearline tape; Offline tape; Midline disk; Nearline disk
- **2003** — Cost model parameters per tier: Cost/GB specified for each of seven storage tiers
- **2003** — Volume model parameters: Master Volume (GB/hr) and Size (GB) plus GB stored for each tier
- **2003** — Bottom-line benefit categories modeled: Four categories: Downtime; Admin Management; Opportunity Cost Savings; Revenue Operations
- **2003** — Benefit value structure per category: Old value and New value captured for each of the four bottom-line categories
- **2003** — Flow Direction parameter: Data flow direction (L or R) specified for each tier transition in each step
- **2003** — Step Duration parameter: Real-world minutes per step modeled
- **2003** — Step description text: Free-text dialog box content per step
- **2003** — Tool deployment constraints: Slides cannot be copied into another deck because diagram is in slide master
- **2003** — ROI modeling approach as ILM adoption driver: Quantified cost-per-GB and bottom-line benefit model will be primary mechanism for customer ILM adoption
- **2023** — TCO/ROI model adoption for storage decisions: [UNVERIFIED]
- **2003** — Midline disk as distinct modeled tier: Midline disk appears as seventh tier alongside traditional online/nearline/offline options
- **2003** — Nearline disk as new modeled tier: Nearline disk modeled alongside nearline tape as a distinct tier
- **2003** — Template reuse instruction: Rinse and repeat — use as many slides as it takes

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '18-maxtor-strategy-event-template-faeb40' ORDER BY year_observed;
```

