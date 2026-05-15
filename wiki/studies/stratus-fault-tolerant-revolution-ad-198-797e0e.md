---
title: "The Fault Tolerant Revolution — Stratus/32 launch advertisement"
slug: stratus-fault-tolerant-revolution-ad-198-797e0e
page_type: study
author: "Stratus Computer, Inc. (marketing; Peter S. Kastner era)"
date: "1981-07-01"
study_type: marketing-material
subject_domain: "fault-tolerant-computing-market-launch"
methodology: "advertising-copy, competitive-positioning"
importance: high
importance_rationale: "This is the launch marketing salvo for Stratus's hardware-fault-tolerant architecture — the product category Kastner would cover, market, and ultimately analyze across a 25-year career spanning Stratus, Aberdeen, and the TPC-benchmark era."
relevance: medium
relevance_rationale: "The hardware-vs-software fault-tolerance debate still frames modern availability-engineering literature (lockstep CPUs, dual-modular redundancy); specifics of the Stratus/32 hardware are historical."
prescience: high
prescience_rationale: "Ad predicted 'hardware costs will continue to fall' while 'software [people] costs will rise' — subsequently validated as Moore's Law and salary inflation tracked exactly as claimed for 40+ years."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 5
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# The Fault Tolerant Revolution — Stratus/32 launch advertisement

> Full-page Computerworld launch advertisement for the Stratus/32 Continuous Processing system circa mid-1981 — the advertising debut of Stratus Computer's hardware-based approach to fault tolerance. The ad contrasts Stratus's duplicate-hardware, tightly-coupled lockstep design with Tandem's software-checkpoint approach, claims price/performance competitive with non-fault-tolerant systems, and quotes a fully-duplexed configuration at under $130,000 including software. Artifact from Kastner's Stratus marketing tenure; documents the company's first broad-market positioning statement.

**Author:** Stratus Computer, Inc. (marketing; Peter S. Kastner era) · **Date:** 1981-07-01 · **Type:** marketing-material
**Importance:** high — *This is the launch marketing salvo for Stratus's hardware-fault-tolerant architecture — the product category Kastner would cover, market, and ultimately analyze across a 25-year career spanning Stratus, Aberdeen, and the TPC-benchmark era.*
**Prescience:** high — *Ad predicted 'hardware costs will continue to fall' while 'software [people] costs will rise' — subsequently validated as Moore's Law and salary inflation tracked exactly as claimed for 40+ years.*

## Entities (4)

- [[computerworld|Computerworld (IDG)]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (5)

- [[hardware-fault-tolerance|Hardware-based fault tolerance]]
- [[software-fault-tolerance|Software-based fault tolerance (checkpointing)]]
- [[stratus-32|Stratus/32 Continuous Processing system]]
- [[stratus-processing-module|Stratus Processing Module (CPU+memory+controllers+IO)]]
- [[vos|Stratus VOS (Virtual Operating System)]]

## Key observations (top 25)

- **1981** — Hardware costs will continue to fall: Ad asserts hardware-component cost trajectory continues downward while software/people costs rise
- **1981** — Hardware FT vs software FT positioning: Software FT 'robs' system resources via checkpointing at 4 levels (OS, user, file, terminal); hardware FT eliminates this burden
- **1981** — Stratus/32 entry price: $130,000 fully-duplexed, 2MB memory, peripherals, and software included
- **1981** — Stratus/32 scalability: 1 to 32 Processing Modules per local system; hot-add while processing
- **1981** — Stratus VOS feature set: VOS with DMS, CRT command language, COBOL, Basic, PL/1, X.25 networking, IBM communications, full-screen editor, symbolic debugger, word processing
- **1981** — Tandem SW FT developer complexity: Analyst/programmer works with two computer systems; risk of checkpointing too often destroying performance
- **1981** — Stratus hardware checking logic benefits: 3 benefits: (1) prevent fault contamination, (2) eliminate complex recovery software, (3) reduce repair time via failed-component pinpointing
- **1981** — Stratus contact HQ: 17 Strathmore Road, Natick MA 01760; HQ marketing 617-653-1466 ext. 32
- **1981** — Kastner Stratus marketing era: Ad dates to Kastner's Stratus Computer marketing tenure (early 1980s)
- **1981** — Computerworld as launch venue: Ad appears in Computerworld — the dominant IT trade weekly in 1981

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-fault-tolerant-revolution-ad-198-797e0e' ORDER BY year_observed;
```

