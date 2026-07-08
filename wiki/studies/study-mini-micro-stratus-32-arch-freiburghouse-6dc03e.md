---
title: "Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)"
slug: "study-mini-micro-stratus-32-arch-freiburghouse-6dc03e"
page_type: "study"
tags: ["type/study", "collection/trade-press-architectural-feature"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "mini-micro-stratus-32-arch-freiburghouse-6dc03e"
author: "Robert Freiburghouse (Stratus Computer)"
date: "1982"
pub_year: 1982
type: "trade-press-architectural-feature"
subject_domain: "fault-tolerant-computing/computer-architecture"
methodology: "vendor-architect-byline-trade-press"
source_file: "Stratus-Arch-Freiburghouse-1982-Mini-Micro-Systems-5.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 0.0
prescience_mean: 0.0
prescience_obs_count: 6
---

# Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=4.12 over 8 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.00 over 8 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> 1982 Mini-Micro Systems bylined feature article by Robert Freiburghouse (Stratus Computer's principal software architect, formerly of Multics PL/I compiler design) detailing the Stratus/32 architecture and 'continuous processing' design philosophy. Key architecture facts documented: up to 32 processing modules connected via StrataLINK high-speed coaxial link (32 Mbits/sec; 2.8 MB/sec dual / 1.4 MB/sec single); each processing module configurable as fully redundant, partially redundant, or non-redundant; each module contains two Motorola 68000 CPUs sharing memory plus one Z80 per peripheral controller; high-speed bus 125-nsec cycle, two parallel data/control paths 32-bit wide, 32 MB/sec potential (16 MB/sec actual at processor/memory boards) — vs VAX 11/780 at 13 MB/sec; CPU board self-checking with paired logic, full-redundant module survives any component failure without performance/data loss; failed boards replaceable by non-technical personnel without tools while system running; VOS distributed virtual OS makes all modules appear as single virtual computer; per-process address space 16 MB (4 MB VOS + 12 MB user). Typical Stratus/32 priced at $172,000 (4 MB memory, dual i43MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses). This is the canonical first-party architectural reference for the Stratus/32 platform throughout the 1982 Stratus quote corpus (studies 1-3 of Batch 25).


_Published 1982, author **Robert Freiburghouse (Stratus Computer)**, type **trade-press-architectural-feature**._


## Top observations

- Robert Freiburghouse, Stratus Computer (architect; bylined author) `[ps=0]`
- Up to 32 processing modules per system `[ps=0]`
- VAX 11/780 bus runs at 13 MB/sec — Stratus internal bus comparison `[ps=0]`
- Dual link 2.8 MB/sec; single link 1.4 MB/sec `[ps=0]`
- 16 MB total (4 MB VOS + 12 MB user) `[ps=0]`
- $172,000 typical: 4 MB memory, dual i43 MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses `[ps=0]`
- 32 MB/sec potential, 16 MB/sec actual; 125-nsec cycle; 32-bit data path
- Failed board can be replaced in running system by nontechnical person without special tools
