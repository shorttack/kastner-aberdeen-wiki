---
title: "WSJ — Digital Challenges Tests by IBM Of Firms' Midrange Computers (Bulkeley, 17-Jun-1988)"
slug: wsj-digital-challenges-ibm-tests-bulkele-e2e227
page_type: study
author: "William M. Bulkeley — The Wall Street Journal"
date: "1988-06-17"
study_type: newspaper-feature
subject_domain: "vendor-benchmark-credibility-disputes"
methodology: "journalistic-reporting"
importance: high
importance_rationale: "WSJ business-page coverage marking the first national-press appearance of John R. Logan with an Aberdeen affiliation — 5+ months before Aberdeen's official December 1988 founding press advisory. Documents the public benchmark-credibility crisis that motivated TPC's creation in August 1988. Pairs with Kastner's DEC primer (Study 4) and Kohler/Hsu memo (Study 1) — the engineering-vs-marketing tension Kastner was navigating internally."
relevance: high
relevance_rationale: "Logan/Aberdeen quote validates Aberdeen's positioning as benchmark-credibility voice from inception. Kastner was still at DEC CSG when this appeared, navigating exactly the issues Logan critiqued. Within 6 months Kastner would leave DEC for Wang and ultimately join Aberdeen (Mar 1989 per press advisory). Direct documentary thread connecting DEC TP work, Aberdeen positioning, and Kastner's professional trajectory."
prescience: high
prescience_rationale: "Logan's verifiable-benchmark critique (RAMP-C not widely circulated, not audited) directly anticipated the TPC's auditor-disclosure regime adopted in TPC-A August 1989 — barely a year later. The 1% communication-line asymmetry critique anticipated TPC-A/C's mandated standard communications-environment disclosure."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 4
obs_count: 11
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# WSJ — Digital Challenges Tests by IBM Of Firms' Midrange Computers (Bulkeley, 17-Jun-1988)

> The Wall Street Journal Friday June 17, 1988 page 32 (Media and Marketing section) feature by William M. Bulkeley reporting on the public dispute between Digital Equipment Corporation and IBM over midrange-computer performance benchmarks. Article covers: (a) IBM's 1987 publication of RAMP-C tests showing IBM AS/400 surpassing DEC VAX; (b) Kenneth MacMorran (IBM midrange systems performance evaluation center manager) defending the tests; (c) DEC's H. Neal Houtz (director of competitive strategies) sending 'truth squads' to analysts and reporters in advance of IBM's expected Silverlake (AS/400) announcement; (d) DEC's specific complaint that IBM set up VAX with communications lines '1% as fast as IBM's lines' and used a network 10x slower than DEC's typical customer environment; (e) IBM's refusal to release RAMP-C source for independent audit. Includes Aberdeen Group consultant John Logan calling RAMP-C 'one of the cheapest tricks IBM could have pulled' because 'a benchmark should be something that is widely circulated and can be duplicated and verified.' George Weiss of Gartner Group adds: 'It indicates a degree of desperation in this marketplace.' Article notes IBM-Digital combined accounted for ~43% of $29.8B 1987 midrange sales. Also reports an unrelated J. Walter Thompson advertising win for the Del Taco Naugles fast-food chain. Article appears 5 months before Aberdeen Group's December 1988 founding press advisory naming Logan as co-founder/Chairman.

**Author:** William M. Bulkeley — The Wall Street Journal · **Date:** 1988-06-17 · **Type:** newspaper-feature
**Importance:** high — *WSJ business-page coverage marking the first national-press appearance of John R. Logan with an Aberdeen affiliation — 5+ months before Aberdeen's official December 1988 founding press advisory. Documents the public benchmark-credibility crisis that motivated TPC's creation in August 1988. Pairs wit…*
**Prescience:** high — *Logan's verifiable-benchmark critique (RAMP-C not widely circulated, not audited) directly anticipated the TPC's auditor-disclosure regime adopted in TPC-A August 1989 — barely a year later. The 1% communication-line asymmetry critique anticipated TPC-A/C's mandated standard communications-environme…*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[gartner-group|Gartner Group]]
- [[george-weiss|George Weiss]]
- [[h-neal-houtz|H. Neal Houtz]]
- [[ibm|IBM Corporation]]
- [[j-walter-thompson|J. Walter Thompson]]
- [[john-r-logan|John R. Logan]]
- [[kenneth-macmorran|Kenneth MacMorran]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[william-bulkeley|William M. Bulkeley]]

## Technologies (4)

- [[ibm-as400|IBM AS/400 (Silverlake)]]
- [[mips|MIPS (Millions of Instructions per Second)]]
- [[ramp-c-benchmark|RAMP-C]]
- [[vax-architecture|VAX architecture]]

## Key observations (top 25)

- **1988** — memorable_quote: one-of-the-cheapest-tricks-IBM-could-have-pulled
- **1988** — logan_principle: widely-circulated-and-duplicated-and-verified
- **1988** — first_wsj_appearance_with_logan: 1988-06-17
- **1987** — midrange_market_size_billion_usd: 29.8
- **1988** — tactic: competitive-truth-squads-to-analysts-and-reporters
- **1988** — test_environment_asymmetry_pct: 1
- **1988** — typical_customer_network_speedup: 10x
- **1988** — memorable_quote: indicates-degree-of-desperation-in-this-marketplace
- **1988** — behavior: refused-RAMP-C-source-and-independent-audit
- **1988** — credibility_signal: anonymous-analyst-said-questionable-aspects
- **1988** — tpc_lead_time_months: 2

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'wsj-digital-challenges-ibm-tests-bulkele-e2e227' ORDER BY year_observed;
```

