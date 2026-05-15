---
title: "Open Source and Linux: 2002 Poster Children for Security Problems"
slug: 2002-open-source-and-linux-2002-poster-children-for-sec-587674
page_type: study
author: "Jim Hurley, Eric Hemmendinger"
date: "2002-11-12"
study_type: market-study
subject_domain: "cybersecurity"
methodology: "industry-analysis"
importance: high
importance_rationale: "Contrarian and influential claim that directly challenged the prevailing narrative of open source software as inherently more secure than Windows; based on CERT advisory data which made it empirically grounded."
relevance: medium
relevance_rationale: "The open source vs. proprietary security debate remains active; the methodology of tracking vulnerability disclosure counts is still used. However the specific framing is now understood as incomplete — disclosure rate ≠ insecurity."
prescience: low
prescience_rationale: "The claim that open source was categorically less secure than Windows proved misleading. Modern security research shows Linux/open source generally has faster patch cycles and lower effective exploit rates despite higher disclosure counts. The framing conflated disclosure volume with actual risk."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 4
obs_count: 11
tags: [type/study, importance/high, prescience/low, decade/2000s]
source_csv: master_studies.csv
---

# Open Source and Linux: 2002 Poster Children for Security Problems

> Aberdeen Group analyzed CERT security advisories for the first 10 months of 2002 and found that open source and Linux software accounted for more than half of all advisories, surpassing Microsoft as the leading source of elevated security vulnerabilities. The study argues that the 'poster child' for security glitches had shifted from Microsoft to open source and Linux suppliers, reversing a common perception of that era.

**Author:** Jim Hurley, Eric Hemmendinger · **Date:** 2002-11-12 · **Type:** market-study
**Importance:** high — *Contrarian and influential claim that directly challenged the prevailing narrative of open source software as inherently more secure than Windows; based on CERT advisory data which made it empirically grounded.*
**Prescience:** low — *The claim that open source was categorically less secure than Windows proved misleading. Modern security research shows Linux/open source generally has faster patch cycles and lower effective exploit rates despite higher disclosure counts. The framing conflated disclosure volume with actual risk.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[cert-cc|CERT Coordination Center]]
- [[linux-kernel-community|Linux Kernel Community]]
- [[microsoft|Microsoft Corporation]]

## Technologies (4)

- [[linux-os|Linux Operating System]]
- [[open-source-software|Open Source Software (general)]]
- [[unix-os|Unix/Unix variants]]
- [[windows-os|Microsoft Windows]]

## Key observations (top 25)

- **2002** — CERT advisories covered period: January through October 2002
- **2002** — Open source and Linux share of CERT advisories: more than half (>50%)
- **2002** — Open source software security risk level: major source of elevated security vulnerabilities
- **2002** — Microsoft Windows security risk designation: no longer the primary security poster child
- **2002** — Linux security advisory prevalence: contributor to majority of CERT advisories
- **2002** — Shift of security vulnerability leadership: from Microsoft to open source/Linux
- **2002** — Open source security problem trajectory: open source will remain major security concern for IT buyers
- **2010** — Linux/open source security actual track record: Linux became dominant server OS with strong enterprise security reputation
- **2015** — Open source security framing outcome: CERT advisory count methodology widely criticized; active disclosure seen as sign of health not weakness
- **2002** — Data source methodology: CERT/CC security advisory count as vulnerability proxy
- **2002** — Open source CERT advisory count out of total 2002 advisories: 16 of total advisories (per The Register coverage)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2002-open-source-and-linux-2002-poster-children-for-sec-587674' ORDER BY year_observed;
```

