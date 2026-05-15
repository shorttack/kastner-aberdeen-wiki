---
title: "Aberdeen Group Flash Report: High Availability Marketing Messages"
slug: 1998-hp-high-availability-and-metadata-7d1276
page_type: study
author: "Peter Kastner; Thomas Willmott; John Logan"
date: "1998-10-28"
study_type: advisory-report
subject_domain: "enterprise-computing;high-availability;marketing-strategy"
methodology: "qualitative-assessment;expert-panel;field-research"
importance: low
importance_rationale: "Captures a pivotal moment in enterprise HA strategy when the industry was transitioning from proprietary Unix dominance toward NT/Intel platforms. Documents the strategic thinking of a major vendor at a time when availability paradigms were being redefined. The advisory recommendations reflect real market dynamics confirmed by field research."
relevance: low
relevance_rationale: "Many concepts remain relevant: end-to-end availability thinking prefigured modern cloud-native resilience engineering; the tension between platform-specific and cross-platform HA persists in hybrid-cloud and multi-cloud contexts. The emphasis on services over box-level technology anticipated the shift to managed services and SRE practices."
prescience: low
prescience_rationale: "Several predictions proved accurate: the report correctly identified that NT/Windows availability would improve but remain behind Unix for years; it foresaw that end-to-end HA would become the dominant paradigm over box-level solutions; and the competitive assessments of Sun (single-box focus) and Compaq/Tandem (installed-base focus) accurately predicted their market trajectories. The recommendation to acquire Marathon Technologies was strategically sound even though HP did not act on it. The ad…"
license: CC-BY-4.0
tier: 2
entity_count: 17
tech_count: 11
obs_count: 35
tags: [type/study, importance/low, prescience/low, decade/1990s]
source_csv: master_studies.csv
---

# Aberdeen Group Flash Report: High Availability Marketing Messages

> Aberdeen Group advisory report from an October 1998 meeting with Hewlett-Packard personnel on high availability (HA) marketing strategy. Field research confirmed 40%+ of commercial server buyers considered availability an important buying attribute across NT and Unix markets. The report recommended HP differentiate via end-to-end HA (versus box-level), uptime contractual guarantees, and HAO remote monitoring. It advised transitioning away from the 'five nines' techie term, broadening HA application scope beyond Unix OLTP, and acquiring Marathon Technologies for NT fault tolerance. Competitive analysis covered IBM, Sun, and Compaq.

**Author:** Peter Kastner; Thomas Willmott; John Logan · **Date:** 1998-10-28 · **Type:** advisory-report
**Importance:** low — *Captures a pivotal moment in enterprise HA strategy when the industry was transitioning from proprietary Unix dominance toward NT/Intel platforms. Documents the strategic thinking of a major vendor at a time when availability paradigms were being redefined. The advisory recommendations reflect real…*
**Prescience:** low — *Several predictions proved accurate: the report correctly identified that NT/Windows availability would improve but remain behind Unix for years; it foresaw that end-to-end HA would become the dominant paradigm over box-level solutions; and the competitive assessments of Sun (single-box focus) and C…*

## Entities (17)

- [[ENT-001|Hewlett-Packard]]
- [[ENT-002|Aberdeen Group]]
- [[ENT-003|IBM]]
- [[ENT-004|Sun Microsystems]]
- [[ENT-005|Compaq]]
- [[ENT-006|Marathon Technologies]]
- [[ENT-007|Cisco]]
- [[ENT-008|EMC]]
- [[ENT-009|Microsoft]]
- [[ENT-010|DH Brown Associates]]
- [[ENT-011|Tandem Computers]]
- [[ENT-012|Digital Equipment Corporation]]
- [[ENT-013|Peter Kastner]]
- [[ENT-014|Thomas Willmott]]
- [[ENT-015|John Logan]]
- [[ENT-016|Jim Murphy]]
- [[ENT-017|Hewlett Packard Enterprise]]

## Technologies (11)

- [[TECH-001|MC/ServiceGuard]]
- [[TECH-002|Windows NT]]
- [[TECH-003|HP-UX]]
- [[TECH-004|High Availability Observatory]]
- [[TECH-005|Five Nines (99.999%)]]
- [[TECH-006|Server Clustering]]
- [[TECH-007|Fault Tolerance on NT]]
- [[TECH-008|End-to-End High Availability]]
- [[TECH-009|OLTP]]
- [[TECH-010|Intel Architecture (IA)]]
- [[TECH-011|Tandem NonStop]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1998-hp-high-availability-and-metadata-7d1276' ORDER BY year_observed;
```

