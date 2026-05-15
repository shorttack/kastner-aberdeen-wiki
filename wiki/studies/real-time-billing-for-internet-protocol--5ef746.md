---
title: "Real-Time Billing for Internet Protocol (IP) Services"
slug: real-time-billing-for-internet-protocol--5ef746
page_type: study
author: "International Engineering Consortium (IEC) tutorial"
date: "1998-12-01"
study_type: white-paper
subject_domain: "isp-billing-cmb-systems"
methodology: "industry-analysis, technology-tutorial"
importance: medium
importance_rationale: "Captures pre-broadband Internet-era framing of real-time customer management/billing as strategic infrastructure — Kastner voiced a core thesis that would play out across SaaS metering and cloud pay-as-you-go for decades."
relevance: medium
relevance_rationale: "Real-time metering/billing is foundational to modern cloud and SaaS business models; Kastner's core insight about agility over 30-day cycles is directly relevant to today's consumption-based pricing."
prescience: high
prescience_rationale: "Kastner's 'turn on a dime' thesis anticipated SaaS metered billing, cloud pay-as-you-go (AWS 2006+), and modern telco convergent charging. Real-time CM&B became table stakes."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 4
obs_count: 7
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Real-Time Billing for Internet Protocol (IP) Services

> International Engineering Consortium online tutorial (authored ~1998 based on IDC/Forrester projections cited for 2002-2003) on the shift from back-office batch Customer Management and Billing (CM&B) systems to real-time front-office systems for Internet service providers. Peter Kastner, chief research officer of Aberdeen Group, is quoted arguing that traditional 30-45 day billing cycles don't work in the Internet's 'dog-eat-dog competitive world' — ISPs need infrastructure allowing customers to 'turn on a dime, try new services right away.' Supporting data: IDC's 1997 estimate of 68 million web users worldwide; Forrester projection of a $58B US business Internet services market by 2003.

**Author:** International Engineering Consortium (IEC) tutorial · **Date:** 1998-12-01 · **Type:** white-paper
**Importance:** medium — *Captures pre-broadband Internet-era framing of real-time customer management/billing as strategic infrastructure — Kastner voiced a core thesis that would play out across SaaS metering and cloud pay-as-you-go for decades.*
**Prescience:** high — *Kastner's 'turn on a dime' thesis anticipated SaaS metered billing, cloud pay-as-you-go (AWS 2006+), and modern telco convergent charging. Real-time CM&B became table stakes.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[forrester-research|Forrester Research, Inc.]]
- [[idc|International Data Corporation (IDC)]]
- [[iec-consortium|International Engineering Consortium (IEC)]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (4)

- [[cmb-system|Customer Management and Billing (CM&B) system]]
- [[internet|Internet / World Wide Web]]
- [[ip-real-time-billing|Real-Time IP Service Billing (CM&B)]]
- [[world-wide-web|World Wide Web (WWW)]]

## Key observations (top 25)

- **1998** — Real-time billing imperative: The Internet is truly a dog-eat-dog competitive world. We just can't use the technology that we used to in the past. Because of that, all of our traditional infrastructure things like billing, that used to work fine on a 30- or 45-day cycle, don't wo…
- **1998** — Customer agility thesis: We need to allow customers to turn on a dime, try new services right away.
- **1997** — Global web users: 68 million Web users worldwide at the end of 1997 (IDC estimate).
- **1997** — Web user growth forecast: 32% annual growth rate projected, resulting in 319 million Web users by end of 2002.
- **1998** — US business Internet services TAM: The U.S. business Internet services market — nearly $58 billion in 2003 — will rival business long-distance phone spending in size. Having grown from virtually nothing to $2.8 billion in just 3 years, the Internet services market will continue to pos…
- **2006** — AWS validates metered billing: Amazon Web Services launched March 2006 with per-hour EC2 and per-GB S3 metered billing, becoming the reference example of the real-time-billing thesis Kastner articulated 8 years earlier.
- **2020** — Convergent charging ubiquitous: By 2020, real-time convergent charging is standard in telco (Ericsson CC, Amdocs), SaaS (Stripe, Recurly), and cloud pay-as-you-go across all major hyperscalers — validating Kastner prediction.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'real-time-billing-for-internet-protocol--5ef746' ORDER BY year_observed;
```

