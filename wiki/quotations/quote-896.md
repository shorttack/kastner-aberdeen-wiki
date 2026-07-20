---
title: Quote 896 — Computerworld (1991-07-22)
type: quotation
page_type: quotation
slug: quote-896
row_id: 896
author: "Peter S. Kastner"
publication: "Computerworld"
date: "1991-07-22"
headline: "Sybase Serves up a new SQL"
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

# Computerworld — 1991-07-22

**Headline**: Sybase Serves up a new SQL

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> did not share the CPU graciously with competing batch jobs or other applications. It did best when you threw the whole machine at it.

## Rationale

Kastner’s characterization that Sybase SQL Server performed best when it had the whole machine largely held over the next several years, as client/server OLTP deployments typically ran Sybase on dedicated VAX and Unix servers rather than sharing them heavily with batch or miscellaneous applications. Sybase SQL Server 4.8 (1992) and then System 10 (mid‑1990s) added SMP support and better scalability, but the ASE engine architecture continued to be CPU‑intensive, with engines effectively pinning CPUs and best‑practice guidance still favoring machines primarily dedicated to the database workload rather than general mixed use. This makes his comment more an enduring description of how Sybase was actually used through the early to mid‑1990s than a transient quirk that was quickly engineered away.

## Provenance

- **row_id**: 896
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
