---
title: "The Outlook on Intel's Quad-Core Chips"
slug: intel-quad-core-outlook-newsfactor-garre-c32252
page_type: study
author: "David Garrett, NewsFactor"
date: "2006-11-15"
study_type: news-article
subject_domain: "cpu-multicore"
methodology: "product-analysis, analyst-commentary"
importance: medium
importance_rationale: "Documents Intel's quad-core/tick-tock cadence reset moment and the server-virtualization-consolidation trend that drove enterprise CPU adoption 2006-2010. Kastner's Q2 2007 mainstream prediction was essentially correct."
relevance: medium
relevance_rationale: "Core-count scaling and virtualization-driven consolidation remain foundational to modern server economics. The 2006 quad-core era is historically dated, but the framework (more cores + consolidation) still dominates 2020s 64-core/128-core enterprise CPU discussion."
prescience: high
prescience_rationale: "Kastner's Q2 2007 mainstream-adoption prediction proved essentially correct — Core 2 Quad desktop volume ramped Q1-Q2 2007. Server virtualization-driven consolidation did become the dominant enterprise-server purchasing rationale 2007-2012. Kastner's 'awesome Christmas dream' gaming/multimedia framing also aligned with strong Q4 2006 and 2007 Core 2 Extreme desktop sales."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 4
obs_count: 9
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# The Outlook on Intel's Quad-Core Chips

> NewsFactor article (Nov 15 2006, David Garrett) on Intel's quad-core processor release: the Xeon 5300 server series (up to 50% faster than dual-core Xeon 5100) and the Core 2 Extreme desktop series (up to 80% faster for threaded apps). Peter Kastner, VP and research director for enterprise technology at Aberdeen Group, predicts 'rapid adoption reaching mainstream in Q2 of next year [2007],' driven by aggressive Intel pricing. He flags server virtualization-driven consolidation as the killer app: 'Quad-core becomes really exciting for the many IT organizations that are looking at server consolidation through virtualization.' For consumers, Kastner calls quad-core gaming/multimedia performance 'awesome' and 'your Christmas dream.' The article captures Intel's attempt to regain enterprise momentum lost to AMD Opteron (esp. Dell's 2006 Opteron server capitulation).

**Author:** David Garrett, NewsFactor · **Date:** 2006-11-15 · **Type:** news-article
**Importance:** medium — *Documents Intel's quad-core/tick-tock cadence reset moment and the server-virtualization-consolidation trend that drove enterprise CPU adoption 2006-2010. Kastner's Q2 2007 mainstream prediction was essentially correct.*
**Prescience:** high — *Kastner's Q2 2007 mainstream-adoption prediction proved essentially correct — Core 2 Quad desktop volume ramped Q1-Q2 2007. Server virtualization-driven consolidation did become the dominant enterprise-server purchasing rationale 2007-2012. Kastner's 'awesome Christmas dream' gaming/multimedia frami…*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[amd|Advanced Micro Devices]]
- [[david-garrett-newsfactor|David Garrett]]
- [[dell|Dell Inc.]]
- [[financial-times|Financial Times]]
- [[hewlett-packard|Hewlett-Packard]]
- [[intel-corp|Intel Corporation]]
- [[newsfactor-network|NewsFactor Network]]
- [[pat-gelsinger-intel|Pat Gelsinger]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (4)

- [[amd-opteron|AMD Opteron]]
- [[intel-core-2-extreme-quad|Intel Core 2 Extreme QX6700 (Kentsfield, quad-core desktop)]]
- [[intel-xeon-5300|Intel Xeon 5300 series (Clovertown, quad-core server)]]
- [[server-virtualization|Server virtualization (VMware ESX, etc.)]]

## Key observations (top 25)

- **2006** — Kastner Q2 2007 mainstream prediction: 'I see a rapid adoption reaching mainstream in Q2 of next year. These should ramp up very rapidly because Intel has priced them to drive market acceptance.' — Peter Kastner, Aberdeen Group
- **2006** — Kastner virtualization-consolidation framing: 'Quad-core becomes really exciting for the many IT organizations that are looking at server consolidation through virtualization' — Kastner on enterprise server driver
- **2006** — Kastner server-market adoption framing: 'On a server, which can use multiple cores, almost by nature this should be very attractive for a huge percentage of volume server shipments' — Kastner on quad-core server TAM
- **2006** — Kastner consumer gaming/multimedia framing: Kastner described quad-core performance in gaming, multimedia, and high-end consumer apps as 'awesome.' 'All the reviews I've read have said this is your Christmas dream'
- **2006** — Intel quad-core performance specs: Xeon 5300 up to 50% faster than dual-core Xeon 5100; Core 2 Extreme up to 80% faster for highly threaded apps
- **2006** — Gelsinger four-fold-performance framing: 'In one year, we've achieved a four-fold increase in performance. That is stunning.' — Pat Gelsinger, Intel (via Financial Times)
- **2006** — Dell Opteron-server launch: Dell finally launched Opteron-based servers in 2006 despite years of Intel-exclusivity — triggering Intel's quad-core urgency
- **2007** — Q2 2007 mainstream quad-core adoption: Core 2 Quad Q6600 launched Jan 2007 at $851, dropped to $266 by July 2007, driving mainstream quad-core adoption in Q2-Q3 2007 exactly as Kastner predicted
- **2012** — Virtualization-driven consolidation dominant: By 2012 server virtualization had become the dominant enterprise-server architecture (VMware + Hyper-V + KVM), exactly as Kastner framed it as quad-core's killer app in 2006

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'intel-quad-core-outlook-newsfactor-garre-c32252' ORDER BY year_observed;
```

