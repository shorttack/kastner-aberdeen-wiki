---
title: "Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)"
slug: mini-micro-stratus-32-arch-freiburghouse-6dc03e
page_type: study
author: "Robert Freiburghouse (Stratus Computer)"
date: "1982"
study_type: trade-press-architectural-feature
subject_domain: "fault-tolerant-computing/computer-architecture"
methodology: "vendor-architect-byline-trade-press"
importance: high
importance_rationale: "Authoritative bylined Stratus architecture reference from Freiburghouse himself — the technical primary source backing Kastner's marketing claims in the parallel 1982 quote corpus."
relevance: high
relevance_rationale: "Companion architectural reference for the Stratus/32 system that anchors Kastner's pre-Aberdeen marketing voice; technical baseline for fault-tolerant architecture discussions across the archive."
prescience: high
prescience_rationale: "Stratus/32's pair-and-spare hardware redundancy + transparent single-system-image distributed OS (VOS) prefigured: (1) modern RAS-class server hardware (e.g., IBM Z mainframes' lockstep processors); (2) software-defined HA clusters as the dominant successor pattern; (3) hot-pluggable component replacement ubiquitous in modern data-center hardware."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 8
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)

> 1982 Mini-Micro Systems bylined feature article by Robert Freiburghouse (Stratus Computer's principal software architect, formerly of Multics PL/I compiler design) detailing the Stratus/32 architecture and 'continuous processing' design philosophy. Key architecture facts documented: up to 32 processing modules connected via StrataLINK high-speed coaxial link (32 Mbits/sec; 2.8 MB/sec dual / 1.4 MB/sec single); each processing module configurable as fully redundant, partially redundant, or non-redundant; each module contains two Motorola 68000 CPUs sharing memory plus one Z80 per peripheral controller; high-speed bus 125-nsec cycle, two parallel data/control paths 32-bit wide, 32 MB/sec potential (16 MB/sec actual at processor/memory boards) — vs VAX 11/780 at 13 MB/sec; CPU board self-checking with paired logic, full-redundant module survives any component failure without performance/data loss; failed boards replaceable by non-technical personnel without tools while system running; VOS distributed virtual OS makes all modules appear as single virtual computer; per-process address space 16 MB (4 MB VOS + 12 MB user). Typical Stratus/32 priced at $172,000 (4 MB memory, dual i43MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses). This is the canonical first-party architectural reference for the Stratus/32 platform throughout the 1982 Stratus quote corpus (studies 1-3 of Batch 25).

**Author:** Robert Freiburghouse (Stratus Computer) · **Date:** 1982 · **Type:** trade-press-architectural-feature
**Importance:** high — *Authoritative bylined Stratus architecture reference from Freiburghouse himself — the technical primary source backing Kastner's marketing claims in the parallel 1982 quote corpus.*
**Prescience:** high — *Stratus/32's pair-and-spare hardware redundancy + transparent single-system-image distributed OS (VOS) prefigured: (1) modern RAS-class server hardware (e.g., IBM Z mainframes' lockstep processors); (2) software-defined HA clusters as the dominant successor pattern; (3) hot-pluggable component repla…*

## Entities (5)

- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[mini-micro-systems|Mini-Micro Systems]]
- [[motorola-inc|Motorola, Inc.]]
- [[robert-freiburghouse|Robert A. Freiburghouse]]
- [[stratus-computer|Stratus Computer]]

## Technologies (8)

- [[hot-plug-board-replacement|Hot-Pluggable Board Replacement (no tools, non-tech personnel)]]
- [[motorola-68000-pair|Paired Motorola 68000 CPUs (Stratus Module)]]
- [[stratalink|StrataLINK Inter-Module High-Speed Coaxial Link]]
- [[stratus-32-cps|Stratus/32 Continuous Processing System]]
- [[stratus-internal-bus|Stratus Dual-Path 32-bit Parallel Bus (125-nsec cycle)]]
- [[stratus-self-checking-hardware|Stratus Self-Checking Hardware Pair Architecture]]
- [[stratus-vos|Stratus VOS (Virtual Operating System)]]
- [[zilog-z80-peripheral|Zilog Z80 Peripheral Controller Coprocessor]]

## Key observations (top 25)

- **1982** — Freiburghouse role: Robert Freiburghouse, Stratus Computer (architect; bylined author)
- **1982** — Module count: Up to 32 processing modules per system
- **1982** — Bus performance: 32 MB/sec potential, 16 MB/sec actual; 125-nsec cycle; 32-bit data path
- **1982** — VAX comparison: VAX 11/780 bus runs at 13 MB/sec — Stratus internal bus comparison
- **1982** — Interconnect performance: Dual link 2.8 MB/sec; single link 1.4 MB/sec
- **1982** — Per-process address space: 16 MB total (4 MB VOS + 12 MB user)
- **1982** — Field-replacement model: Failed board can be replaced in running system by nontechnical person without special tools
- **1982** — Typical configuration price: $172,000 typical: 4 MB memory, dual i43 MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'mini-micro-stratus-32-arch-freiburghouse-6dc03e' ORDER BY year_observed;
```

