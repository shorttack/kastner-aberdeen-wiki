---
title: Quote 422 — Computerworld (2002-11-18)
type: quotation
slug: quote-422
row_id: 422
author: "Peter S. Kastner"
publication: "Computerworld"
date: "2002-11-18"
headline: "Blade Servers: Wait 'Til Next Year"
horizon: "SH-5y"
final_bucket: high
final_score: 4
final_confidence: 3
final_pipeline: P2
blog_scrape_contamination: false
scorer_version: quotations_corpus_v1
source_pass: quotations_corpus
tags: [quotation, prescience, kastner]
---

# Computerworld — 2002-11-18

**Headline**: Blade Servers: Wait 'Til Next Year

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-5y, pipeline=P2

## Quote

> what once could be done with an expensive eight-way or larger Intel or Unix server can now be done with a handful of powerful blades.

## Rationale

From 2002–2006, the industry did shift many workloads that previously ran on expensive 8‑way+ SMP Intel/Unix boxes onto clusters of cheaper x86 blades such as IBM BladeCenter (launched 2002) and HP BladeSystem (c‑Class in 2006), especially for web/application tiers, hosting, and HPC. Virtualization (VMware ESX, Xen) and rapidly improving multi-core x86 CPUs increased per‑blade performance and consolidation ratios, so a small number of blades could match or exceed the throughput of prior large SMP servers for many scale‑out use cases. However, high-end OLTP databases and large SAP/ERP instances remained on big Unix and large SMP x86 systems through the late 2000s, so the statement slightly overgeneralized even though its overall direction and economics were largely correct within the 4‑year horizon.

## Provenance

- **row_id**: 422
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
