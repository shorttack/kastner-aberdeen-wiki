---
title: Quote 163 — Computerworld (1994-12-12)
type: quotation
slug: quote-163
row_id: 163
author: "Peter S. Kastner"
publication: "Computerworld"
date: "1994-12-12"
headline: "Developers extend user support with PowerBuilder"
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

# Computerworld — 1994-12-12

**Headline**: Developers extend user support with PowerBuilder

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-5y, pipeline=P2

## Quote

> ose caveats, the three-tier architecture is now becoming the de facto topology of choice for serious [on-line transaction processing]-based applications.'' Developers who opt for the creation of three-tier applications with PowerBuilder must be prepared for some “serious system integration,'' Kastner added, because they will be dealing with from multiple vendors and managing multiple tiers.

## Rationale

Within about five years of 1994, three-tier (presentation, application, data) architectures had become the standard pattern for scalable, internet-facing OLTP systems such as banking and e‑commerce, and are still described as the most common form of multitier architecture for such applications.[6][2][3] Kastner’s warning about “serious system integration” across multiple vendors also held up: three-tier designs typically involve distinct web/UI, application/middleware, and database products, increasing integration overhead compared with simpler two-tier client/server setups.[4][7] The only caveat is that many departmental and legacy client/server OLTP systems remained two-tier through the late 1990s, so calling three-tier the de facto choice was somewhat ahead of broad practice, even though it correctly anticipated where serious, high-scale transactional development was heading.[6][8]

## Provenance

- **row_id**: 163
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
