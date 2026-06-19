---
title: Quote 1159 — AP ()
type: quotation
slug: quote-1159
row_id: 1159
author: "Peter S. Kastner"
publication: "AP"
date: ""
headline: "Sixty-four-bit architectures can theoretically address millions of terabytes worth of memory, which translates directly"
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

**Headline**: Sixty-four-bit architectures can theoretically address millions of terabytes worth of memory, which translates directly

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> into better performance for complex applications. "If you're running a relational database and you can do all of your math computations in memory, your performance can be several times faster than if you have to write everything to disk," says Peter Kastner, executive vice president and chief research officer with the market research and consulting firm, Aberdeen Group Inc., Boston, Mass. A possible performance advantage isn't the only factor driving 64-bit interest. The ong

## Rationale

The statement that running relational database workloads entirely in memory on 64-bit systems can be several times faster than relying on disk I/O accurately reflects how larger address spaces and RAM were used in early 64-bit Unix and Windows servers to grow buffer caches and reduce disk access for Oracle, DB2, and similar databases in the early 2000s. Over the subsequent decade, the same principle underpinned the rise of explicitly in-memory database systems and caches (for example SAP HANA and large in-memory OLTP/OLAP configurations), which consistently demonstrated multi‑x speedups over disk-bound architectures. The claim slightly over-implies how quickly typical enterprise databases would move to “all in memory” within a three-year horizon, but its core performance characterization proved directionally correct and enduring.

## Provenance

- **row_id**: 1159
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
