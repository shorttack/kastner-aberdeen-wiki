---
title: "Intel May Get Chip on Its Shoulder (USA Today on IBM-Intel Pentium FDIV battle)"
slug: usatoday-maney-pentium-fdiv-kastner-1994-13a035
page_type: study
author: "Kevin Maney (USA Today)"
date: "1994-12-13"
study_type: trade-press-feature
subject_domain: "semiconductor/Pentium-FDIV-bug/PC-industry-PR"
methodology: "press-feature-with-analyst-quotes"
importance: high
importance_rationale: "Marquee Pentium-FDIV crisis story with Kastner as primary analyst voice; documents the most significant Intel-IBM PC-industry confrontation of the early 1990s."
relevance: high
relevance_rationale: "Direct Kastner quote in major national newspaper at Aberdeen Group; illustrates Kastner's industry-stakes framing ('whole industry will get bloodied') and usage-realism counterpoint to IBM's spreadsheet scenario."
prescience: high
prescience_rationale: "Kastner's 'whole industry gets bloodied' / 'replacements for all customers' framing predicted the recall-economics playbook later applied to chip flaws (Pentium FDIV recall, and decades later Spectre/Meltdown disclosure economics); his usage-realism counterpoint anticipated the modern 'workload-realistic benchmarking' debate."
license: CC-BY-4.0
tier: 1
entity_count: 15
tech_count: 4
obs_count: 11
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Intel May Get Chip on Its Shoulder (USA Today on IBM-Intel Pentium FDIV battle)

> Kevin Maney's USA Today feature (13 December 1994) on IBM's decision to halt Pentium PC shipments after its labs concluded the FDIV bug could surface in spreadsheet recalculations as often as once every 24 days (vs Intel's once-every-27000-years claim). Quotes Aberdeen Group analyst Peter Kastner: 'The whole industry will get bloodied... It won't do much good for anybody's PC sales now through Christmas. IBM is a large, respected name. If it says there's a problem, people will believe it.' Kastner is also quoted on usage-pattern realism ('Most people with a Pentium computer and a spreadsheet don't do anything near 15 minutes of recalculations a day. It's more like seconds worth.'). Other voices: Intel CEO Andy Grove, IBM lab head Bill Pullyblank, IBM spokesman Rob Wilson, Microprocessor Report editor Michael Slater, PC Week editor in chief Daniel Lyons, Lynchburg College math professor Thomas Nicely.

**Author:** Kevin Maney (USA Today) · **Date:** 1994-12-13 · **Type:** trade-press-feature
**Importance:** high — *Marquee Pentium-FDIV crisis story with Kastner as primary analyst voice; documents the most significant Intel-IBM PC-industry confrontation of the early 1990s.*
**Prescience:** high — *Kastner's 'whole industry gets bloodied' / 'replacements for all customers' framing predicted the recall-economics playbook later applied to chip flaws (Pentium FDIV recall, and decades later Spectre/Meltdown disclosure economics); his usage-realism counterpoint anticipated the modern 'workload-real…*

## Entities (15)

- [[aberdeen-group|Aberdeen Group]]
- [[andy-grove|Andrew S. Grove]]
- [[bill-pullyblank-ibm|Bill Pullyblank]]
- [[daniel-lyons-pcweek|Daniel Lyons]]
- [[ibm|IBM Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[kevin-maney|Kevin Maney]]
- [[lynchburg-college|Lynchburg College]]
- [[michael-slater-mpr|Michael Slater]]
- [[microprocessor-report|Microprocessor Report]]
- [[pc-week|PC Week]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[rob-wilson-ibm|Rob Wilson]]
- [[thomas-nicely|Thomas Nicely]]
- [[usa-today|USA Today]]

## Technologies (4)

- [[pentium-fdiv-bug|Pentium FDIV Bug]]
- [[pentium-processor|Pentium Processor (P5/FDIV-affected)]]
- [[personal-computer|Personal Computer (Wintel)]]
- [[powerpc|PowerPC]]

## Key observations (top 25)

- **1994** — Whole industry impact framing: industry will get bloodied
- **1994** — PC sales impact through Christmas: negative
- **1994** — Usage realism counterpoint: seconds vs 15 minutes recalc daily
- **1994** — Intel error-rate claim: once every 27,000 years
- **1994** — IBM error-rate claim: once per 24 days
- **1994** — IBM lab error-rate per 100M calculations: 1 in 100 million
- **1994** — Intel stock movement: down 2% closing $60.625, 16M shares traded
- **1994** — Grove on contrived scenarios: you can always contrive situations
- **1994** — IBM halts Pentium PC shipments: halted 12-Dec-1994
- **1994** — Complexity of impact estimation: Intel minimizes, IBM maximizes
- **1994** — Replacement-cycle worry: could end up dealing with all customers

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'usatoday-maney-pentium-fdiv-kastner-1994-13a035' ORDER BY year_observed;
```

