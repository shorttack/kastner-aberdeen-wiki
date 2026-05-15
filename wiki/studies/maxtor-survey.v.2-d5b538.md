---
title: "Maxtor RAMP Disk Storage Usage Questionnaire v2"
slug: maxtor-survey.v.2-d5b538
page_type: study
author: "Peter S. Kastner; David Hill (Aberdeen Group)"
date: "2003-03-01"
study_type: market-study
subject_domain: "enterprise-storage / disk-tiering / ILM"
methodology: "ramp-survey-design, telephone-survey, quantitative-research"
importance: high
importance_rationale: "Landmark market research instrument whose 1-7 Likert tradeoff scale (Q9) directly tested the fundamental positioning question for midline ATA storage: would enterprises accept lower availability for 50% cost reduction? The quantified willingness scores from this survey determined whether Maxtor could position MaXLine as a substitute or complement to FC/SCSI storage — a strategic inflection point for the entire midline storage category."
relevance: high
relevance_rationale: "The three Q9 tradeoff scenarios (high-capacity/less-availability at 50% cost reduction; current-size/less-availability at 30%; current-size/full-availability at 30%) map precisely to the modern cloud storage tier economics: Premium/Standard/Archive tiers with analogous cost-performance tradeoffs. The survey design framework anticipated tiered cloud storage by a decade."
prescience: high
prescience_rationale: "Q9's three-scenario willingness scale anticipated the exact tradeoff matrix that defined enterprise cloud storage tier adoption (2013-2023): hot storage (full performance/cost), cool storage (30% cheaper / slightly less available), and archive (50-80% cheaper / slower restore). The instrument also correctly framed the competitive question as complementary tier vs. substitute — proving prescient: midline SATA became a complementary tier, not a replacement for FC."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 10
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Maxtor RAMP Disk Storage Usage Questionnaire v2

> Refined second version of the Aberdeen Group telephone survey questionnaire for the Maxtor RAMP project. Streamlines the v1 instrument to 17 survey questions and a demographic section, with key enhancements: per-OS storage breakdowns (Q4.1-Q4.3) for mainframe / Windows / Unix separately, introduction of a 1-7 Likert willingness-to-tradeoff scale (Q9) testing three distinct cost-performance scenarios (50% cost reduction with lower availability; 30% with less availability; 30% with same availability), vendor engagement probing (Q10-Q11), restore frequency measurement (Q12), static data application identification (Q14), and a refined terminology awareness battery testing five terms. The instrument was used to collect data from approximately 70 enterprise IT decision-makers.

**Author:** Peter S. Kastner; David Hill (Aberdeen Group) · **Date:** 2003-03-01 · **Type:** market-study
**Importance:** high — *Landmark market research instrument whose 1-7 Likert tradeoff scale (Q9) directly tested the fundamental positioning question for midline ATA storage: would enterprises accept lower availability for 50% cost reduction? The quantified willingness scores from this survey determined whether Maxtor coul…*
**Prescience:** high — *Q9's three-scenario willingness scale anticipated the exact tradeoff matrix that defined enterprise cloud storage tier adoption (2013-2023): hot storage (full performance/cost), cool storage (30% cheaper / slightly less available), and archive (50-80% cheaper / slower restore). The instrument also c…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[ibm|IBM]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[microsoft|Microsoft]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (10)

- [[ata-disk|ATA Hard Disk Drive]]
- [[das-external|External Direct-Attached Storage (DAS)]]
- [[das-internal|Internal Direct-Attached Storage (DAS)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[nas|Network Attached Storage (NAS)]]
- [[point-in-time-copy|Point-in-Time Copy / Snapshot]]
- [[san|Storage Area Network (SAN)]]
- [[scsi-disk|SCSI Hard Disk Drive]]
- [[serial-ata|Serial ATA (SATA)]]
- [[tape-automation|Tape Automation]]

## Key observations (top 25)

- **2003** — Instrument type: Telephone survey questionnaire — version 2; refined and streamlined from v1
- **2003** — OS platform — direct responsibility probe: Q1: Which OSes does your organization use AND which are you directly responsible for? (Mainframe / Windows / Unix-Linux)
- **2003** — Per-OS storage architecture breakout — v2 design: Q4.1-Q4.3: Per-OS capacity share / DAS-SAN-NAS mix / 12-month growth / max fill rate — separately for mainframe / Windows / Unix
- **2003** — Windows and Unix/Linux treated as equivalents for open-systems storage: Q4.2 and Q4.3 use identical structure; both excluded from mainframe category
- **2003** — Online disk vs. tape copy count: Q5: Online disk copies (excluding original) / tape copies (each generation = one copy)
- **2003** — Read-only / seldom-written data identification — refined framing: Q6: Data that is effectively read-only or seldom written — closed transaction logs / old e-mail — but cannot yet be archived to tape
- **2003** — Cold data application identification: Q7: What applications fall under the read-only/seldom-written category? (Open-ended)
- **2003** — Cold data percentage quantification: Q8: What percent of total storage is the read-only/seldom-written data?
- **2003** — Willingness-to-tradeoff — 1-7 Likert scale design: Q9: Rate willingness to trade off on 3 scenarios (1=unwilling to tradeoff; 7=sign me up today)
- **2003** — Willingness scenario A — highest value proposition: Q9(a): Higher capacity + slightly less performance + slightly less availability + ~50% cost reduction
- **2003** — Willingness scenario B — availability-reduced conservative case: Q9(b): Current disk sizes + current performance + slightly less availability + ~30% cost reduction
- **2003** — Willingness scenario C — no tradeoff required: Q9(c): Current disk size + current performance + current availability + ~30% cost reduction
- **2003** — Vendor engagement measurement: Q10: Has your current storage supplier discussed low-cost disk options with you? (Supplier name?)
- **2003** — Purchase intent — 1-7 scale: Q11: If yes [vendor discussed low-cost options] — plans to purchase in next 12 months (1=Not at all; 7=Already have)
- **2003** — Restore frequency as reliability proxy: Q12: How often do you restore one or more volumes from storage failure — weekly / monthly / quarterly / semi-annually / annually / less than annually
- **2003** — Static data application identification — specific examples: Q14: Single applications with very large non-volatile/static data — video data / images / data warehouse detailed / old e-mails
- **2003** — Open-systems disk technology breakout — three types: Q15: SCSI / FC / ATA percentage + drive sizes + rotational speeds — open-systems disk arrays only
- **2003** — Backup/restore issues — five-symptom multi-select: Q16: Five specific backup failure modes — offline window / job failure rate / cannot guarantee restore / management burden / restore time too long
- **2003** — Terminology awareness — five-term battery: Q17: Active archiving / online archiving / mezzanine storage / nearline storage / low-cost storage — all five tested
- **2003** — Midline storage as complementary vs. substitute tier: Q9's three scenarios implicitly test whether midline is a substitute (Scenario C) or complement (Scenarios A/B) for existing storage
- **2003** — Midline as complement vs. substitute — outcome: [UNVERIFIED]
- **2003** — 50% cost reduction target for maximum-tradeoff scenario: Q9(a) states cost reduction \"\"on the order of 50%\"\" for higher-capacity / less-available option
- **2003** — Unix / Linux / open-systems grouped as single category: Q1 and Q4.3 treat Unix, Linux, and 'open systems' as a single category
- **2003** — Question numbering gap — Q13 absent: Survey jumps from Q12 to Q14 — Q13 missing or removed in v2 revision
- **2003** — Vendor name capture in Q10: Q10 asks for supplier name when vendor has discussed low-cost disk — competitive intelligence design

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'maxtor-survey.v.2-d5b538' ORDER BY year_observed;
```

