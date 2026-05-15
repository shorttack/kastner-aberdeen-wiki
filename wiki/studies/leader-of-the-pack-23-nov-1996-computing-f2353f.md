---
title: "Leader of the pack? [Wolfpack clustering coverage]"
slug: leader-of-the-pack-23-nov-1996-computing-f2353f
page_type: study
author: "Ian Ashbridge / Sarah Petrie (reporter); Peter Kastner (quoted source)"
date: "1996-11-23"
study_type: press-article
subject_domain: "windows-nt-clustering"
methodology: "press-coverage, expert-opinion, competitive-profiling"
importance: medium
importance_rationale: "Contemporaneous 1996 UK trade-press documentation of Microsoft Wolfpack's launch positioning and Kastner's skeptical-but-engaged analyst posture; captures Aberdeen's early NT-clustering market framing."
relevance: low
relevance_rationale: "Windows NT Wolfpack and its internal rivalries are settled history; the article is primarily of value as an archival record of late-1990s clustering hype cycles and analyst positioning."
prescience: high
prescience_rationale: "Kastner's 'wait two years' caveat and warning that no Wolfpack member had a complete toolkit proved broadly correct: Wolfpack (Microsoft Cluster Server) did not ship meaningful two-node support until 1997-1998 and four-node not until Windows 2000 Advanced Server in 2000."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 3
obs_count: 6
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Leader of the pack? [Wolfpack clustering coverage]

> Computing (UK) analysis of Microsoft's Wolfpack clustering initiative on Windows NT, featuring Peter Kastner of Aberdeen Group as a senior expert voice. Kastner warns that no single Wolfpack vendor has a complete clustering toolkit, that one in seven NT investments is aimed at clustering, and cautions enterprises against the 'siren song' of Microsoft-only Wolfpack deployments pending two years of maturation. Article maps the internal Wolfpack split between Tandem Servernet backers (Compaq, Dell, Tandem) and Microsoft-aligned vendors.

**Author:** Ian Ashbridge / Sarah Petrie (reporter); Peter Kastner (quoted source) · **Date:** 1996-11-23 · **Type:** press-article
**Importance:** medium — *Contemporaneous 1996 UK trade-press documentation of Microsoft Wolfpack's launch positioning and Kastner's skeptical-but-engaged analyst posture; captures Aberdeen's early NT-clustering market framing.*
**Prescience:** high — *Kastner's 'wait two years' caveat and warning that no Wolfpack member had a complete toolkit proved broadly correct: Wolfpack (Microsoft Cluster Server) did not ship meaningful two-node support until 1997-1998 and four-node not until Windows 2000 Advanced Server in 2000.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq-computer|Compaq Computer Corporation]]
- [[dell-computer|Dell Computer Corporation]]
- [[digital-equipment|Digital Equipment Corporation (DEC)]]
- [[ibm-corporation|IBM Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[peter-kastner|Peter S. Kastner]]
- [[tandem-computers|Tandem Computers]]

## Technologies (3)

- [[tandem-servernet|Tandem ServerNet]]
- [[windows-nt|Microsoft Windows NT]]
- [[wolfpack|Microsoft Wolfpack / MSCS]]

## Key observations (top 25)

- **1996** — Completeness of Wolfpack toolkit: No single Wolfpack vendor had the whole clustering toolkit at launch; 'all at the starting gate'
- **1996** — Share of NT buyers motivated by clustering: 1 in 7 (~14%) NT investments driven by clustering intent
- **1996** — Recommended wait before Microsoft-only deployment: Enterprises should wait ~2 years before betting on Microsoft-only Wolfpack
- **1996** — Wolfpack coalition split: Two factions: Servernet backers (Compaq, Dell, Tandem) vs Microsoft-centric
- **2000** — Wolfpack actual delivery timeline: Microsoft Cluster Server two-node shipped 1997; full 4-node capability only with Windows 2000 Advanced Server (2000)
- **1997** — Tandem acquisition: Compaq acquired Tandem in 1997 (closed June 1997)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'leader-of-the-pack-23-nov-1996-computing-f2353f' ORDER BY year_observed;
```

