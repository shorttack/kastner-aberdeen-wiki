---
title: "Moore's Law: True But Irrelevant"
slug: moore-s-law-true-but-irrelevant-internet-661e40
page_type: study
author: "David Haskin (InternetNews.com)"
date: "2003-05-16"
study_type: news-article
subject_domain: "enterprise-pc-strategy"
methodology: "industry-analysis, analyst-debate"
importance: high
importance_rationale: "Early influential articulation of the post-Moore's Law desktop-upgrade debate featuring the Gartner vs Aberdeen split; contributed to the analyst conversation that shaped corporate PC refresh cycles mid-decade."
relevance: medium
relevance_rationale: "The debate over desktop upgrade cadence still recurs; Kastner's multi-process argument prefigured today's background-workload reasoning on Copilot/AI PCs."
prescience: high
prescience_rationale: "Kastner's thesis that multi-threaded background workloads would drive desktop demand proved correct with the rise of antivirus, indexing, browsers with dozens of tabs, containers, and (from 2023) on-device AI."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 6
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Moore's Law: True But Irrelevant

> InternetNews.com piece pitting Gartner's Mark Margevicius ('no software coming anytime soon that needs more desktop performance') against Aberdeen Group's Peter Kastner, who disagrees. Kastner argues Windows 98/NT machines are obsolescent, corporate buyers should move to Office 2003 for collaboration productivity, and that the multi-process, multi-threaded workload of a modern PC ('40 processes going on when I'm checking email') will make CPU performance matter again on the desktop. He cautions IT managers that lengthening the desktop upgrade cycle is 'penny wise, pound foolish.'

**Author:** David Haskin (InternetNews.com) · **Date:** 2003-05-16 · **Type:** news-article
**Importance:** high — *Early influential articulation of the post-Moore's Law desktop-upgrade debate featuring the Gartner vs Aberdeen split; contributed to the analyst conversation that shaped corporate PC refresh cycles mid-decade.*
**Prescience:** high — *Kastner's thesis that multi-threaded background workloads would drive desktop demand proved correct with the rise of antivirus, indexing, browsers with dozens of tabs, containers, and (from 2023) on-device AI.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[andrew-gomez|Andrew Gomez]]
- [[david-haskin|David Haskin]]
- [[gartner-inc|Gartner, Inc.]]
- [[intel-corporation|Intel Corporation]]
- [[mark-margevicius|Mark Margevicius]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[roger-l-kay|Roger L. Kay]]

## Technologies (6)

- [[intel-pentium-4|Intel Pentium 4]]
- [[microsoft-office-2003|Microsoft Office 2003]]
- [[moores-law|Moore's Law]]
- [[multi-threading|Multi-threaded OS workload]]
- [[windows-98|Microsoft Windows 98]]
- [[windows-nt|Microsoft Windows NT]]

## Key observations (top 25)

- **2003** — Gartner: desktop performance enough: 'There isn't software coming out anytime soon that needs more performance on the desktop.'
- **2003** — Move to Office 2003: 'We recommend that corporate buyers look at Office 2003 because it has better collaboration capabilities that add to productivity.'
- **2003** — Windows 98/NT obsolescence: 'Windows 98 and NT machines are obsolescent. It's pretty provable that workers with those machines can't make use of the productivity improvements in the latest software.'
- **2003** — PC upgrade cycle caution: 'Over the long haul, that's penny wise and pound foolish' — warning to IT managers trying to save money by lengthening desktop-PC upgrade cycles.
- **2003** — Background workload drives demand: 'I turn my PC on in the morning and there's 40 processes going on, even if I'm only checking my e-mail. That's eventually going to be important for desktop PCs.'
- **2003** — Desktop performance will matter again: Kastner's argument implies background-workload demand will make CPU performance relevant again on desktop.
- **2016** — Moore's Law slowed materially: Single-thread CPU performance gains slowed meaningfully after ~2005; multi-core and heterogeneous (GPU/NPU) acceleration became primary drivers. Moore's Law as traditionally defined effectively ended c. 2016-2020.
- **2024** — Background workloads drove AI-PC era: Modern PCs routinely run dozens of background processes and, by 2024, on-device AI (Copilot+ PCs) — vindicating Kastner's 2003 prediction.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'moore-s-law-true-but-irrelevant-internet-661e40' ORDER BY year_observed;
```

