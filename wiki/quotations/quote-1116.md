---
title: Quote 1116 — AP ()
type: quotation
page_type: quotation
slug: quote-1116
row_id: 1116
author: "Peter S. Kastner"
publication: "AP"
date: ""
headline: "Koo says AOL expects to deploy a considerable number of blade servers during the next few years and will likely test"
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

# AP — 

**Headline**: Koo says AOL expects to deploy a considerable number of blade servers during the next few years and will likely test

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> expects to deploy a considerable number of blade servers during the next few years and will likely test blades running other data center applications, such as data warehousing, as well. Melding Servers While standards are sorely needed, Aberdeen's Kastner says it's becoming increasingly clear that "what once could be done with an expensive eight-way or larger Intel or Unix server can now be done with a handful of powerful blades." However, it's still unclear how data centers will monitor and manage

## Rationale

Within roughly three years of this statement, blade platforms like IBM BladeCenter and early HP/Dell blade systems were widely adopted to run many workloads that had previously justified costly 8‑way (and larger) Unix or Intel SMP servers, especially in web, application, and general-purpose enterprise tiers.[1][4][5][8] Industry reports from the mid‑2000s emphasize blades’ high density, shared infrastructure, and maturing multi‑socket designs, which enabled organizations to replace single large SMP boxes with a small cluster of blades for many (though not all) workloads.[1][4][5] However, very large monolithic database and OLTP systems remained on high-end Unix or proprietary SMP platforms longer, so the claim slightly overgeneralizes even though its overall direction—scale-out blade clusters displacing big SMP machines—proved correct over the horizon.

## Provenance

- **row_id**: 1116
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
