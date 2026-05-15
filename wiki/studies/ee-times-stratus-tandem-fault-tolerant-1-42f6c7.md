---
title: "EE Times: Stratus Challenges Tandem in Fault-Tolerant Computing — Pete Kastner on Self-Checking Hardware Strategy (May 1982)"
slug: ee-times-stratus-tandem-fault-tolerant-1-42f6c7
page_type: study
author: "EE Times (Electronic Engineering Times) staff"
date: "1982-05"
study_type: trade-press-feature
subject_domain: "fault-tolerant-computing/competitive-strategy"
methodology: "industry-reporter-with-vendor-and-vc-quotes"
importance: high
importance_rationale: "Documents Kastner's 'manager of marketing development at Stratus' title in mid-1982 — the title most cited in his pre-Aberdeen archival record (1987 Computerworld and 1987 CW OLTP article). First time Kastner's hardware-self-checking architectural argument is in the public record."
relevance: high
relevance_rationale: "Establishes Kastner's pre-Aberdeen technical-marketing voice on fault-tolerance architecture (Stratus pair-and-spare hardware vs Tandem software fault-tolerance), an argument he reprised throughout the Aberdeen years."
prescience: medium
prescience_rationale: "1982 fault-tolerant architecture debate (hardware self-checking vs software fault-tolerance) anticipated the modern HA-cluster and cloud-resilience architecture debate (hardware redundancy vs software-defined high availability), although the specific Stratus pair-and-spare approach was largely subsumed by software-based redundancy by the 2010s."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 5
obs_count: 6
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# EE Times: Stratus Challenges Tandem in Fault-Tolerant Computing — Pete Kastner on Self-Checking Hardware Strategy (May 1982)

> May 1982 Electronic Engineering Times feature on the maturing fault-tolerant computer market. Tandem Computers retains a roughly six-year lead but must expect upstart competition. Pete Kastner — quoted as 'manager of marketing development at Stratus' — argues that Stratus has 'taken a piece' out of Tandem's market with the Stratus/32 and that the Stratus self-checking-hardware-pair architecture is superior because: (a) all redundancy is in hardware (every component is self-checking each cycle), and (b) data paths remain in 16-bit mode unlike Tandem's NonStop II competing system. Kastner promises faster transaction throughput and the ability to support 'all the memory they need — up to a million kbytes'. The article also quotes investment banker Larry Roberts (whose firm backed both Stratus and Synapse Computer) and alludes to Synapse president Mark Leslie's perspective on 32-bit FT systems. This is the second-earliest Kastner Stratus quote in the archive (after the March 1982 Eagle-Tribune piece) and the first to use his 'manager of marketing development' title.

**Author:** EE Times (Electronic Engineering Times) staff · **Date:** 1982-05 · **Type:** trade-press-feature
**Importance:** high — *Documents Kastner's 'manager of marketing development at Stratus' title in mid-1982 — the title most cited in his pre-Aberdeen archival record (1987 Computerworld and 1987 CW OLTP article). First time Kastner's hardware-self-checking architectural argument is in the public record.*
**Prescience:** medium — *1982 fault-tolerant architecture debate (hardware self-checking vs software fault-tolerance) anticipated the modern HA-cluster and cloud-resilience architecture debate (hardware redundancy vs software-defined high availability), although the specific Stratus pair-and-spare approach was largely subsu…*

## Entities (8)

- [[ee-times|EE Times (Electronic Engineering Times)]]
- [[larry-roberts-investment|Larry Roberts (investment banker)]]
- [[mark-leslie-synapse|Mark Leslie]]
- [[motorola-inc|Motorola, Inc.]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[synapse-computer|Synapse Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (5)

- [[32bit-fault-tolerant-server|32-bit Fault-Tolerant Server Class]]
- [[motorola-68000|Motorola 68000 CPU]]
- [[stratus-32-cps|Stratus/32 Continuous Processing System]]
- [[stratus-self-checking-hardware|Stratus Self-Checking Hardware Pair Architecture]]
- [[tandem-nonstop-ii|Tandem NonStop II]]

## Key observations (top 25)

- **1982** — Kastner role and employer: Peter Kastner, manager of marketing development at Stratus
- **1982** — Kastner architectural argument: We're different. We've done it all in hardware. Every one of the components we use is self-checking during each operating cycle.
- **1982** — Kastner Tandem comparison: Stratus has already taken a piece out of Tandem's market; Stratus has faster computation; users can extend their FT operations more easily
- **1982** — Tandem lead: Six-year lead over upstarts; some upstart products seem more advanced
- **1982** — VC perspective: Larry Roberts (partner in firm that backed both Stratus and Synapse) cited as observing 32-bit FT segment dynamics
- **1982** — Competing FT startup: Synapse Computer cited alongside Stratus as 32-bit FT startup; Mark Leslie president

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ee-times-stratus-tandem-fault-tolerant-1-42f6c7' ORDER BY year_observed;
```

