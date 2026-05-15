---
title: "Respiratory Illness Could Restrict I.T. Supply Lines"
slug: respiratory-illness-could-restrict-i.t.--c3c523
page_type: study
author: "Gregg Keizer, Techweb News, with Eric Chabrow and Marianne Kolbasuk McGee (InformationWeek)"
date: "2003-04-07"
study_type: news-article
subject_domain: "IT-supply-chain-pandemic-risk"
methodology: "industry-analysis, analyst-commentary"
importance: high
importance_rationale: "First-order Kastner framing of SARS as an IT supply-chain event — the single earliest widely-cited industry-analyst warning that a Guangdong pandemic could cascade through global IT procurement. Became the template for post-COVID supply-chain analyses 17 years later."
relevance: high
relevance_rationale: "Supply-chain-concentration risk (Guangdong / single-region sourcing, especially for power supplies and semiconductors) remains a live concern through 2020-2026 (COVID-19, US-China decoupling, CHIPS Act)."
prescience: high
prescience_rationale: "Kastner's warning proved directly prescient in the COVID-19 pandemic (2020-2022), when Chinese factory shutdowns caused exactly the kind of power-supply, semiconductor, and finished-PC shortages he described — affecting Dell, HP, Apple, and the broader industry."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 2
obs_count: 6
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Respiratory Illness Could Restrict I.T. Supply Lines

> InformationWeek news story (2003-04-07 issue) on the potential impact of SARS (severe acute respiratory syndrome) on IT hardware supply chains. Peter Kastner, an Aberdeen Group analyst, warns in a recent report that 'worst case, it could result in major supply-chain disruptions and another downdraft for an already challenged industry' — because much of the world's electronics manufacturing (including most AC-to-DC power supplies) is concentrated in Guangdong province, China, which is also where SARS broke out. IT consultant Joe Wetz (K-Lag Technology) reports that his team is already building hardware-delay buffers into project timelines, with longer delays requiring alternate sourcing.

**Author:** Gregg Keizer, Techweb News, with Eric Chabrow and Marianne Kolbasuk McGee (InformationWeek) · **Date:** 2003-04-07 · **Type:** news-article
**Importance:** high — *First-order Kastner framing of SARS as an IT supply-chain event — the single earliest widely-cited industry-analyst warning that a Guangdong pandemic could cascade through global IT procurement. Became the template for post-COVID supply-chain analyses 17 years later.*
**Prescience:** high — *Kastner's warning proved directly prescient in the COVID-19 pandemic (2020-2022), when Chinese factory shutdowns caused exactly the kind of power-supply, semiconductor, and finished-PC shortages he described — affecting Dell, HP, Apple, and the broader industry.*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[apple-computer|Apple Computer, Inc. / Apple Inc.]]
- [[compaq|Compaq Computer Corporation]]
- [[dell-computer|Dell Computer / Dell Inc.]]
- [[guangdong-province|Guangdong Province, China]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[informationweek|InformationWeek / TechWeb]]
- [[joe-wetz|Joe Wetz]]
- [[k-lag-technology|K-Lag Technology]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[who-world-health-organization|World Health Organization]]

## Technologies (2)

- [[ac-dc-power-supplies|AC-to-DC switching power supplies]]
- [[global-it-supply-chain|Globalized IT manufacturing supply chain]]

## Key observations (top 25)

- **2003** — SARS supply-chain risk: If infection rates go unchecked, the IT manufacturing supply chain may be broken. Worst case, it could result in major supply-chain disruptions and another downdraft for an already challenged industry.
- **2003** — Guangdong power-supply concentration: Guangdong province is home to much of China electronics and IT hardware industry and the source for most of the world AC-to-DC power supplies.
- **2003** — K-Lag delay buffering: We are anticipating delays, and we are building that into project time frames. Many projects can withstand hardware delays of a few weeks, but if the problem lingers, we might have to find other sources.
- **2003** — SARS 2003 outcome: SARS caused limited but measurable IT supply-chain disruption in Q2 2003 (component delays of 2-6 weeks for some products), partially offsetting post-dot-com IT spending recovery.
- **2020** — COVID-19 realization of supply-chain risk: COVID-19 pandemic (2020-2022) caused far greater IT supply-chain disruption than SARS: Guangdong factory shutdowns, semiconductor shortage, power-supply shortages, finished-PC shortages affecting Dell, HP, Apple, and the industry — directly validatin…
- **2022** — US-China decoupling / CHIPS Act: US Congress passed the $52B CHIPS Act in 2022 explicitly to diversify semiconductor manufacturing away from Asian concentration; ongoing US-China trade tensions and factory reshoring confirm supply-chain-concentration as a durable strategic risk.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'respiratory-illness-could-restrict-i.t.--c3c523' ORDER BY year_observed;
```

