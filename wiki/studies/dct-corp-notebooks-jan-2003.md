---
title: "Corporate Notebook Lineup Snapshot, January 2003"
slug: dct-corp-notebooks-jan-2003
page_type: study
author: "Peter S. Kastner"
date: "2003-01-15"
study_type: dct
subject_domain: "dct"
methodology: "competitive-profiling"
importance: medium
importance_rationale: "Primary-source competitive snapshot at the moment HP finished absorbing Compaq and IBM ThinkPad was consolidating as the premium corporate alternative."
relevance: low
relevance_rationale: "Historical corporate notebook configuration data."
prescience: not-applicable
prescience_rationale: "Product snapshot; no predictions."
license: CC-BY-4.0
tier: 2
entity_count: 3
tech_count: 4
obs_count: 11
tags: [type/study, importance/medium, prescience/not-applicable, decade/2000s]
source_csv: master_studies.csv
---

# Corporate Notebook Lineup Snapshot, January 2003

> Two-sheet (Business and Consumer) snapshot of corporate notebook lineups as of January 2003, profiling HP Compaq Evo N800v / Evo 1000c / N610c / N410c, IBM ThinkPad T30 / X30, and parallel consumer configurations across three form-factor bands (Standard, Thin & Light, Value). Each entry captures manufacturer online price, street price (e.g., CDW), processor (Mobile Pentium 4-M or Pentium III-M), screen size, memory, HDD, optical drive, weight, warranty, OS (Windows XP Pro), Office XP Pro availability, and street-site source.

**Author:** Peter S. Kastner · **Date:** 2003-01-15 · **Type:** dct
**Importance:** medium — *Primary-source competitive snapshot at the moment HP finished absorbing Compaq and IBM ThinkPad was consolidating as the premium corporate alternative.*
**Prescience:** not-applicable — *Product snapshot; no predictions.*

## Entities (3)

- [[cdw|CDW Corp.]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]

## Technologies (4)

- [[intel-pentium-4-m|Mobile Intel Pentium 4 (M)]]
- [[intel-pentium-iii-m|Mobile Intel Pentium III (M)]]
- [[notebook-pc|Notebook PC form factor]]
- [[windows-xp|Microsoft Windows XP Pro]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-corp-notebooks-jan-2003' ORDER BY year_observed;
```

