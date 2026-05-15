---
title: "NCR System 3000 / Model 3550 Open Cooperative Computing Brochure (1992)"
slug: ncr-system-3000-model-3550-brochure-1992-b15aed
page_type: study
author: "NCR Corporation (vendor product brochure)"
date: "1992"
study_type: vendor-product-brochure
subject_domain: "open-cooperative-computing/symmetric-multiprocessing"
methodology: "vendor-product-collateral"
importance: high
importance_rationale: "Primary-source NCR product collateral establishing the platform architecture that Aberdeen's 1991-1992 Open OLTP studies (Korean translation 3fc536, Norway seminar 7f5414, English fragments ea272f) actually evaluate. Bridges vendor positioning to analyst commentary."
relevance: high
relevance_rationale: "Documents the NCR System 3000 / Model 3550 — central platform of the NCR-Aberdeen Open OLTP analytical track that runs through Batches 21-24."
prescience: medium
prescience_rationale: "1992 vendor positioning of x86-based SMP servers as scalable mainframe alternatives anticipated the Intel-based enterprise server transition of the late 1990s and 2000s, although NCR System 3000 itself was displaced by the WorldMark line and later by commodity x86 server vendors."
license: CC-BY-4.0
tier: 1
entity_count: 3
tech_count: 7
obs_count: 6
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# NCR System 3000 / Model 3550 Open Cooperative Computing Brochure (1992)

> NCR Corporation 1992 product brochure for the NCR System 3000 family, with the NCR Model 3550 highlighted as 'the most powerful tightly-coupled system in the System 3000 family'. The brochure positions System 3000 as 'the broadest range of open, scalable systems in the computer industry today' — from uniprocessor to multiprocessor, tightly-coupled to loosely-coupled architectures — and pitches the 3550 as delivering 'several times the performance traditionally found in mainframe computers, for less cost'. Engineering specs: dual 64-bit system bus running at 25 MHz with 200 MB/sec aggregate bandwidth; up to 8 Intel486 50 MHz CPUs (claimed 320 MIPS); Micro Channel Enhanced I/O; RAID storage; hot-pluggable disks; dual-port memory; fault-resilient design. UNIX SVR4 operating system. This is the platform companion to the Batch 23 NCR 3000 cabinet engineering diagram (study fa564f) and is contemporaneous with Aberdeen's Open OLTP for Enterprise Managers white paper (study 3fc536) and the 1992-09 NCR Norge AS Open OLTP/RDBMS mini-seminar (study 7f5414).

**Author:** NCR Corporation (vendor product brochure) · **Date:** 1992 · **Type:** vendor-product-brochure
**Importance:** high — *Primary-source NCR product collateral establishing the platform architecture that Aberdeen's 1991-1992 Open OLTP studies (Korean translation 3fc536, Norway seminar 7f5414, English fragments ea272f) actually evaluate. Bridges vendor positioning to analyst commentary.*
**Prescience:** medium — *1992 vendor positioning of x86-based SMP servers as scalable mainframe alternatives anticipated the Intel-based enterprise server transition of the late 1990s and 2000s, although NCR System 3000 itself was displaced by the WorldMark line and later by commodity x86 server vendors.*

## Entities (3)

- [[att-corp|AT&T Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[ncr-corporation|NCR Corporation]]

## Technologies (7)

- [[dual-64bit-system-bus|Dual 64-bit System Bus @ 25 MHz]]
- [[intel486-50mhz|Intel486 50 MHz CPU]]
- [[micro-channel-enhanced|Micro Channel Enhanced I/O]]
- [[ncr-3550|NCR Model 3550]]
- [[ncr-system-3000-family|NCR System 3000 family]]
- [[raid-storage-1992|RAID Storage Subsystem (NCR 1992)]]
- [[unix-svr4|UNIX System V Release 4 (SVR4)]]

## Key observations (top 25)

- **1992** — Dual 64-bit bus: 200 MB/sec aggregate bandwidth at 25 MHz
- **1992** — CPU configuration: Up to 8x Intel486 50 MHz; aggregate ~320 MIPS
- **1992** — RAS features: Hot-pluggable disks; RAID; dual-port memory; fault-resilient design
- **1992** — Family scope: Uniprocessor through multiprocessor; tightly to loosely coupled
- **1992** — Operating system: UNIX System V Release 4 across System 3000 family
- **1992** — Mainframe-alternative positioning: Several times mainframe performance for less cost

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ncr-system-3000-model-3550-brochure-1992-b15aed' ORDER BY year_observed;
```

