---
title: "Computerworld: Stratus Readies XA2000 Series to Take on Tandem High-End — Pete Kastner on Floating-Point + Yankee Group's Henkel on VLX/3090 Class (February 1987)"
slug: computerworld-stratus-xa2000-launch-1987-d9d143
page_type: study
author: "James Connolly (Computerworld staff)"
date: "1987-02"
study_type: trade-press-product-launch
subject_domain: "fault-tolerant-computing/product-launch"
methodology: "industry-reporter-with-vendor-and-analyst-quotes"
importance: high
importance_rationale: "Documents Kastner's pre-Aberdeen 'manager of marketing support programs for Stratus' title (a third pre-Aberdeen Stratus title in his career arc, after 'communications director' 1982-03 and 'manager of marketing development' 1982-05/06, 1987-03). Yankee Group's Henkel quoted as comparable analyst voice."
relevance: high
relevance_rationale: "Final pre-Aberdeen Kastner title at Stratus (he founded Aberdeen in 1988); details Stratus's most ambitious 1987 product launch (XA2000) plus IBM System/88 OEM relationship."
prescience: high
prescience_rationale: "Foster's 'insatiable appetite for tps' framing + 45%/yr OLTP growth assumption proved directionally correct for the late 1980s and 1990s. The XA2000's modular on-line CPU expansion + scaling up to 64 MB / 128 MB virtual / 46 GB disk anticipated modern hyperscale linear-scale architectures."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 8
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Computerworld: Stratus Readies XA2000 Series to Take on Tandem High-End — Pete Kastner on Floating-Point + Yankee Group's Henkel on VLX/3090 Class (February 1987)

> February 1987 Computerworld product-launch story by James Connolly on the Stratus XA2000 series (Models 100-140), positioned to take on Tandem's 10-month-old NonStop VLX. Both companies claim peak rates over 50 tps. Stratus officials anticipate near-simultaneous announcement of XA2000 inclusion in IBM's System/88 line (IBM resells Stratus-built FT systems as System/88). Stratus CEO William E. Foster: 'We are selling into a market that has an insatiable appetite for transactions per second' and cites the design assumption of 45% annual growth in OLTP over the next five years. Pete S. Kastner — quoted as 'manager of marketing support programs for Stratus' — explains the new Motorola 68881 floating-point coprocessor is intended to help OLTP users perform tasks like financial modeling, NOT to enter scientific/engineering markets. Hardware: 16 MHz Motorola 68020 processors (vs prior 68010), 64 MB memory, 64 KB cache, 128 MB virtual address space, 46 GB disk. Model 140 has four tightly-coupled duplicated CPUs and is rated 15 / 27-29 / 37-40 / 47-53 tps for Models 110/120/130/140 on ET-1; Model 140 is 3x XA600 ET-1 and 2.5x XA600 TP-1. Pricing: $260K-$500K (Model 110) up to $770K-$1.1M (Model 140). Stratus claims tps cost is half that of earlier products. Yankee Group analyst Thomas Henkel: 'This is really the first time they have gotten into the VLX or IBM 3090 class' — but questions IBM's relationship with Stratus and Stratus's app/database software depth in growth areas like manu…

**Author:** James Connolly (Computerworld staff) · **Date:** 1987-02 · **Type:** trade-press-product-launch
**Importance:** high — *Documents Kastner's pre-Aberdeen 'manager of marketing support programs for Stratus' title (a third pre-Aberdeen Stratus title in his career arc, after 'communications director' 1982-03 and 'manager of marketing development' 1982-05/06, 1987-03). Yankee Group's Henkel quoted as comparable analyst vo…*
**Prescience:** high — *Foster's 'insatiable appetite for tps' framing + 45%/yr OLTP growth assumption proved directionally correct for the late 1980s and 1990s. The XA2000's modular on-line CPU expansion + scaling up to 64 MB / 128 MB virtual / 46 GB disk anticipated modern hyperscale linear-scale architectures.*

## Entities (8)

- [[computerworld|Computerworld]]
- [[ibm|IBM Corporation]]
- [[motorola-inc|Motorola, Inc.]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[william-e-foster|William E. Foster]]
- [[yankee-group|The Yankee Group]]

## Technologies (8)

- [[ibm-system-88|IBM System/88]]
- [[motorola-68020|Motorola 68020 16 MHz CPU]]
- [[motorola-68881|Motorola 68881 Floating-Point Coprocessor]]
- [[oltp-45pct-growth-forecast|OLTP 45%/yr Growth Forecast (Stratus 1987 Foster)]]
- [[stratus-vos-6|Stratus VOS Release 6.0]]
- [[stratus-xa2000-140|Stratus XA2000 Model 140]]
- [[stratus-xa2000-series|Stratus XA2000 Series (Models 100-140)]]
- [[tandem-nonstop-vlx|Tandem NonStop VLX]]

## Key observations (top 25)

- **1987** — Kastner role and employer: Peter S. Kastner, manager of marketing support programs for Stratus
- **1987** — Kastner FP coprocessor framing: 68881 designed to help OLTP users perform financial modeling; NO plans to enter scientific or engineering markets
- **1987** — Foster Stratus role: William E. Foster, Stratus Chief Executive Officer
- **1987** — Foster OLTP forecast: Selling into a market that has an insatiable appetite for tps; 45% annual growth over next 5 years
- **1987** — Henkel VLX/3090 class framing: First time Stratus has gotten into the VLX or IBM 3090 class in OLTP performance
- **1987** — Henkel IBM/Stratus question: Questioned how long IBM will maintain its relationship with Stratus if Stratus continues to compete with 3090 mainframes
- **1987** — ET-1 ratings (Models 110-140): 15 / 27-29 / 37-40 / 47-53 tps for Models 110 / 120 / 130 / 140
- **1987** — Performance multiplier vs XA600: 3x XA600 ET-1; 2.5x XA600 TP-1
- **1987** — Memory and storage: Up to 64 MB memory, 64 KB cache, 128 MB virtual address space, 46 GB disk
- **1987** — Pricing: $260K-$500K Model 110; $770K-$1.1M Model 140; transaction-per-second cost half of earlier products

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'computerworld-stratus-xa2000-launch-1987-d9d143' ORDER BY year_observed;
```

