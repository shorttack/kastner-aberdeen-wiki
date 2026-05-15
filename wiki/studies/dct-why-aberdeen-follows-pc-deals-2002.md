---
title: "Why Aberdeen Is Following Consumer PC Deals — DCT Practice Methodology"
slug: dct-why-aberdeen-follows-pc-deals-2002
page_type: study
author: "Peter S. Kastner"
date: "2002-07-01"
study_type: dct
subject_domain: "DCT,PC-retail,pricing-methodology"
methodology: "industry-analysis,market-tracking,competitive-profiling"
importance: high
importance_rationale: "Foundational methodology document underpinning dozens of subsequent weekly PC Deals commentaries; defines the Aberdeen-Kastner price-value framework."
relevance: high
relevance_rationale: "Price-value tradeoff framework remains relevant to consumer tech tracking; specific hardware thresholds (128MB RAM, 40GB HDD) are dated but useful as 2002 benchmarks."
prescience: medium
prescience_rationale: "Framework correctly anticipated rebate-driven price adjustment mechanics and HP/Compaq dual-brand challenges post-merger."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 14
obs_count: 19
tags: [type/study, importance/high, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Why Aberdeen Is Following Consumer PC Deals — DCT Practice Methodology

> Methodology paper explaining Aberdeen's Digital Consumer Technology practice approach to weekly consumer PC price tracking. Defines the research questions, six tracked brands (Compaq, Dell, eMachines, Gateway, HP, Sony), an 8-factor price-value hierarchy (CPU, memory, modem/NIC, HDD, monitor, OS, printer, software), and weekly commentary format. Acknowledges 90 days of prior tracking; explicitly excludes Apple (no head-to-head competition).

**Author:** Peter S. Kastner · **Date:** 2002-07-01 · **Type:** dct
**Importance:** high — *Foundational methodology document underpinning dozens of subsequent weekly PC Deals commentaries; defines the Aberdeen-Kastner price-value framework.*
**Prescience:** medium — *Framework correctly anticipated rebate-driven price adjustment mechanics and HP/Compaq dual-brand challenges post-merger.*

## Entities (12)

- [[aberdeen-dct-practice|Aberdeen Digital Consumer Technology Practice]]
- [[aberdeen-group|Aberdeen Group]]
- [[amd|AMD]]
- [[apple-computer|Apple Computer]]
- [[compaq|Compaq]]
- [[dell|Dell]]
- [[emachines|eMachines]]
- [[gateway-inc|Gateway]]
- [[hewlett-packard|Hewlett-Packard]]
- [[intel|Intel]]
- [[microsoft|Microsoft]]
- [[sony|Sony]]

## Technologies (14)

- [[10-100-ethernet|10/100 Ethernet]]
- [[56k-modem|56K Dial-up Modem]]
- [[color-inkjet-printer|Color Inkjet Printer]]
- [[ddr-sdram|DDR SDRAM]]
- [[flat-panel-monitor|Flat-Panel LCD Monitor]]
- [[hdd-7200rpm|7200 RPM Hard Drive]]
- [[intel-celeron|Intel Celeron]]
- [[intel-pentium-4|Intel Pentium 4]]
- [[microsoft-office|Microsoft Office]]
- [[monitor-crt|CRT Monitor]]
- [[rambus-rdram|Rambus DRAM (RDRAM)]]
- [[sdram|SDRAM]]
- [[windows-xp-home|Windows XP Home]]
- [[windows-xp-pro|Windows XP Professional]]

## Key observations (top 25)

- **2002** — Tracked brands count: 6 (Compaq, Dell, eMachines, Gateway, HP, Sony)
- **2002** — Price-value hierarchy factors: 8 (CPU, RAM, modem/NIC, HDD, monitor, OS, printer, software)
- **2002** — CPU comparison 1.8GHz: Pentium 4 beats 1.8GHz Celeron on cache
- **2002** — Memory tier threshold: 128MB significantly slower than 256MB; multimedia=512MB
- **2002** — DDR vs SDRAM: DDR faster than plain SDRAM
- **2002** — RDRAM positioning: Makes sense for high-end Pentium 4 only
- **2002** — Integrated modem requirement: 56Kb standard
- **2002** — Integrated NIC requirement: 10/100 Ethernet standard
- **2002** — HDD preference: Faster (7200 RPM) > bigger
- **2002** — HDD size baseline: 40GB entry / 80GB multimedia
- **2002** — Monitor baseline: 17 inch flat tube <$100 in bundle
- **2002** — Flat panel aspiration: 19 inch flat-panel 'to die for'
- **2002** — OS recommendation: XP Pro > XP Home for power/SMB users
- **2002** — Printer bundle price: $50 and up
- **2002** — Final price formula: List - rebates + shipping (ex-sales tax)
- **2002** — Online rebate cadence: Adjusted several times per week
- **2002** — Rebate coupon count: Six coupons low-side for store purchase
- **2002** — Apple tracking exclusion rationale: No head-to-head competition
- **2002** — HP dual-brand strategy question: Open research question (post-Compaq merger)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-why-aberdeen-follows-pc-deals-2002' ORDER BY year_observed;
```

