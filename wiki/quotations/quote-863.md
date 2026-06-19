---
title: Quote 863 — Computerworld (1989-02-27)
type: quotation
slug: quote-863
row_id: 863
author: "Peter S. Kastner"
publication: "Computerworld"
date: "1989-02-27"
headline: "RDBMS show they can pull OLTP weight"
horizon: "SH-3y"
final_bucket: high
final_score: 5
final_confidence: 3
final_pipeline: P2
blog_scrape_contamination: false
scorer_version: quotations_corpus_v1
source_pass: quotations_corpus
tags: [quotation, prescience, kastner]
---

# Computerworld — 1989-02-27

**Headline**: RDBMS show they can pull OLTP weight

**Verdict**: HIGH prescience — score=5, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> the flexibility of the relational model and a lot of overhead,

## Rationale

Kastner’s remark describes early relational DBMS implementations as offering strong model flexibility but incurring significant overhead, especially in their initial decision-support–oriented incarnations; this aligns with well-documented history that first-generation systems such as IBM’s System R and early Ingres/Oracle prototypes traded performance for the relational abstraction and SQL portability.[1][3] By the late 1980s and into the early 1990s (within the 3‑year horizon), major vendors (Oracle, IBM DB2, Informix, Sybase) were explicitly focused on adding query optimizers, indexing strategies, and other ‘go‑fast tricks’ to reduce this overhead and make RDBMS viable for high-throughput OLTP, implicitly confirming that early systems had indeed been flexible but comparatively heavy and slow.[2][5] This retrospective characterization of early RDBMS behavior remained consistent with how database history was summarized in technical and historical accounts through the 2000s and 2010s, so it held up over time rather than being contradicted by later evidence.[1][6]

## Provenance

- **row_id**: 863
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
