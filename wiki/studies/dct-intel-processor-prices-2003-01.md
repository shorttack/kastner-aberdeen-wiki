---
title: "Analysis of Intel Processor Prices in PC Deals (January 2003)"
slug: dct-intel-processor-prices-2003-01
page_type: study
author: "Peter S. Kastner"
date: "2003-01-15"
study_type: dct
subject_domain: "dct"
methodology: "market-tracking, price-series-analysis"
importance: high
importance_rationale: "Rare contemporaneous analysis of Intel CPU price-band dynamics during a pivotal transition (hyperthreading launch and 533 MHz FSB adoption) using Kastner's PC Deals retail tracking."
relevance: medium
relevance_rationale: "Historical methodology example of price-tier analysis in the PC retail channel; specific CPUs long EOL."
prescience: high
prescience_rationale: "Correctly predicted the 2.0 GHz P4 obsolescence and the divergent pricing of 400 vs 533 MHz FSB families; called the start of a new high-end $2200-$3000 tier around the 3.06 GHz hyperthreading P4."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 18
obs_count: 19
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Analysis of Intel Processor Prices in PC Deals (January 2003)

> Analysis of Intel Celeron and Pentium 4 processor price tiers observed in Aberdeen's PC Deals tracking from August 2002 through January 2003. Documents the bifurcation of P4 into 400 MHz and 533 MHz front-side-bus families, the introduction of hyperthreading 3.06 GHz P4, and the mechanics of older CPUs being pushed down price bands by new releases. Predicts near-term obsolescence of the P4 2.0 GHz.

**Author:** Peter S. Kastner · **Date:** 2003-01-15 · **Type:** dct
**Importance:** high — *Rare contemporaneous analysis of Intel CPU price-band dynamics during a pivotal transition (hyperthreading launch and 533 MHz FSB adoption) using Kastner's PC Deals retail tracking.*
**Prescience:** high — *Correctly predicted the 2.0 GHz P4 obsolescence and the divergent pricing of 400 vs 533 MHz FSB families; called the start of a new high-end $2200-$3000 tier around the 3.06 GHz hyperthreading P4.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[dell|Dell, Inc.]]
- [[intel|Intel Corporation]]
- [[peter-kastner|Peter S. Kastner]]

## Technologies (18)

- [[fsb-400mhz|400 MHz front-side bus]]
- [[fsb-533mhz|533 MHz front-side bus]]
- [[hyperthreading|Intel Hyper-Threading]]
- [[intel-celeron|Intel Celeron]]
- [[intel-celeron-17ghz|Intel Celeron 1.7 GHz]]
- [[intel-celeron-18ghz|Intel Celeron 1.8 GHz]]
- [[intel-celeron-20ghz|Intel Celeron 2.0 GHz]]
- [[intel-pentium-4|Intel Pentium 4]]
- [[intel-pentium-4-18|Intel Pentium 4 1.8 GHz]]
- [[intel-pentium-4-20|Intel Pentium 4 2.0 GHz]]
- [[intel-pentium-4-226|Intel Pentium 4 2.26 GHz]]
- [[intel-pentium-4-24|Intel Pentium 4 2.4 GHz]]
- [[intel-pentium-4-253|Intel Pentium 4 2.53 GHz]]
- [[intel-pentium-4-26|Intel Pentium 4 2.6 GHz]]
- [[intel-pentium-4-266|Intel Pentium 4 2.66 GHz]]
- [[intel-pentium-4-28|Intel Pentium 4 2.8 GHz]]
- [[intel-pentium-4-306|Intel Pentium 4 3.06 GHz HT]]
- [[pc-deals|Aberdeen PC Deals]]

## Key observations (top 25)

- **2002** — price-position: Celeron CPUs consistently hold lowest price point under $600
- **2002** — price-drop-month: P4 1.8 GHz dropped below $900 in August 2002
- **2002** — launch-date: 2002-06-12
- **2002** — launch-date: 2002-08-26
- **2002** — debut-price-band: Celeron 2.0 GHz entered $600 category in November 2002
- **2002** — price-ceiling: Celeron 1.7 GHz PCs held under $450
- **2002** — launch-date: 2002-08-26 (P4 2.6, 2.66, 2.8 GHz simultaneous release)
- **2002** — price-drop-extent: new P4s pushed 1.8/2.0 GHz P4s down $150 to $900 in one month
- **2002** — obsolescence-month: P4 2.26 GHz disappeared from PC Deals by October 2002
- **2002** — price-pattern: 533 MHz FSB P4 pricing falls independently of 400 MHz FSB P4 pricing
- **2002** — launch-month: 2002-11 (P4 3.06 GHz HT introduction)
- **2003** — expected-outcome: near end for 2.0 GHz P4 following 2.4 GHz price drop
- **2002** — product-line-structure: Intel simultaneously ships three differently-structured P4 variants (400MHz FSB, 533MHz FSB, HT)
- **2002** — price-stability: 2.66 and 2.8 GHz P4 remained in same price category for 4+ months after launch
- **2002** — new-price-tier: 3.06 GHz HT creates new $2200-$3000 PC price category
- **2003** — mid-range-impact: HT processors will NOT eliminate middle 533 MHz P4s like 2.53 GHz anytime soon
- **2002** — seasonal-pattern: Back-to-school period had best PC deals; Christmas saw price increases
- **2002** — holiday-pricing: Dell among sources raising prices during holiday 2002
- **2003** — spring-outlook: Q1 2003 spring quarter will force price cuts to move inventory

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-intel-processor-prices-2003-01' ORDER BY year_observed;
```

