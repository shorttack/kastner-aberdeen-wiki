---
title: "Windows 2000: High-End Ambitions"
slug: informationweek-windows-2000-high-end-am-4ccdae
page_type: study
author: "Stuart J. Johnston, Mary Hayes"
date: "1999-04-19"
study_type: news-feature
subject_domain: "windows-2000-datacenter-scalability"
methodology: "news-feature, expert-quote-aggregation, customer-survey"
importance: high
importance_rationale: "Primary-source Aberdeen data point and Kastner skepticism on Windows-2000 high-end scalability — important contextual setup for the next decade's Microsoft-vs-Unix scale wars."
relevance: medium
relevance_rationale: "Specific Datacenter Server SKU is obsolete, but Kastner's 'NT vs mainframe scaling' framing remains analytically relevant to today's Windows Server / Linux / hyperscaler comparisons."
prescience: high
prescience_rationale: "Kastner's 95%-boost-per-processor mainframe benchmark exposed real Windows NT scalability limits that took Microsoft another decade (Server 2008/2012, kernel rework) to overcome. 'Call me when it's ready' attitude reflected actual enterprise behavior — Windows 2000 Datacenter saw modest uptake while mainframes and high-end Unix continued dominating tier-one workloads."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 6
obs_count: 5
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Windows 2000: High-End Ambitions

> InformationWeek Issue 730 (April 19, 1999) reports on Microsoft's plans for Windows 2000 Datacenter Server — the high-end SKU promised as Microsoft's most scalable server OS, supporting up to 32 processors and 64 GB RAM. Aberdeen Group CRO Peter Kastner is skeptical, predicting IT response will be 'call me when it's ready,' and benchmarks NT scalability against IBM mainframe's 95% boost-per-processor. Datacenter Server hadn't begun beta testing and wasn't due until 3 months after the Windows 2000 base release, itself delayed. Aberdeen survey of 240 IT decision-makers evaluating Windows 2000 found 89% plan to use it for email, 84% intranet hosting, 84% generic servers.

**Author:** Stuart J. Johnston, Mary Hayes · **Date:** 1999-04-19 · **Type:** news-feature
**Importance:** high — *Primary-source Aberdeen data point and Kastner skepticism on Windows-2000 high-end scalability — important contextual setup for the next decade's Microsoft-vs-Unix scale wars.*
**Prescience:** high — *Kastner's 95%-boost-per-processor mainframe benchmark exposed real Windows NT scalability limits that took Microsoft another decade (Server 2008/2012, kernel rework) to overcome. 'Call me when it's ready' attitude reflected actual enterprise behavior — Windows 2000 Datacenter saw modest uptake while…*

## Entities (8)

- [[aberdeen-group|Aberdeen Group]]
- [[ibm-corp|IBM Corporation]]
- [[informationweek|InformationWeek]]
- [[mary-hayes-iw|Mary Hayes]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stuart-johnston-iw|Stuart J. Johnston]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (6)

- [[clustering-software|Server Clustering Software]]
- [[ibm-mainframe|IBM S/390 Mainframe]]
- [[windows-2000-advanced-server|Windows 2000 Advanced Server]]
- [[windows-2000-datacenter-server|Windows 2000 Datacenter Server]]
- [[windows-2000-server|Windows 2000 Server]]
- [[windows-nt|Microsoft Windows NT]]

## Key observations (top 25)

- **1999** — IT decision-maker call-me-when-ready stance: Datacenter Server will pique IT's interest; their response will be — Call me when it's ready
- **1999** — NT vs mainframe scaling benchmark: For all the tuning grief I go through, what gain am I going to see unless I get a huge performance boost? In the IBM mainframe environment, you're looking at a 95% boost per processor. NT has some ways to go to get into that range.
- **1999** — Aberdeen Windows 2000 IT-DM survey: Aberdeen Research survey of IT decision-makers in January 1999, of 240 evaluating Windows 2000: 89% plan to use Windows 2000 Server for email; 84% for Internet/intranet site hosting; 84% for generic servers
- **1999** — Datacenter pre-beta delay: Datacenter Server has not begun beta testing and isn't due until three months after Microsoft ships the initial Windows 2000 releases, which have been delayed
- **1999** — Sun 8-way clustering planned: Sun expects to ship eight-way clustering in the spring of 2000

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'informationweek-windows-2000-high-end-am-4ccdae' ORDER BY year_observed;
```

