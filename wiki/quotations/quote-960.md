---
title: Quote 960 — Computerworld (1993-08-02)
type: quotation
page_type: quotation
slug: quote-960
row_id: 960
author: "Peter S. Kastner"
publication: "Computerworld"
date: "1993-08-02"
headline: "NetFrame gives servers flexibility"
horizon: "SH-3y"
final_bucket: high
final_score: 4
final_confidence: 3
final_pipeline: P2
blog_scrape_contamination: false
scorer_version: quotations_corpus_v1
source_pass: quotations_corpus
tags: [quotation, prescience, kastner]
---

# Computerworld — 1993-08-02

**Headline**: NetFrame gives servers flexibility

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> The [concept] of having multiple peripherals running under different [operating systems] sharing main memory on a single server is very complex.

## Rationale

In the mid-1990s, commercial attempts at tightly coupling multiple processors or peripheral subsystems under different operating systems with shared memory, such as NetFrame’s Concerto-like designs and various ccNUMA and multi-OS research systems, remained niche because of their engineering and performance complexity. Mainstream enterprise evolution instead favored single-OS SMP servers and, later, hypervisor-based virtualization (e.g., VMware from 1999, IBM PR/SM and z/VM LPARs) that required significant kernel and hardware support to safely multiplex memory across OS instances, confirming that true multi-OS shared-memory architectures were technically demanding well beyond the 3-year horizon. Even by the 2010s–2020s, scenarios where independent OS images directly share the same physical memory without a virtualization or partitioning layer are rare and confined to specialized platforms, underscoring that the underlying concept Kastner flagged stayed complex over time.

## Provenance

- **row_id**: 960
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
