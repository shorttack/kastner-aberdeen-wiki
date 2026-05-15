---
title: "Power Macs 'won't hit 3GHz this year' – analysts"
slug: power-macs-won-t-hit-3ghz-this-year-anal-73ad0f
page_type: study
author: "Macworld UK staff (IDG)"
date: "2004-06-11"
study_type: news-article
subject_domain: "CPU-clock-speed-90nm-process"
methodology: "industry-analysis, analyst-commentary"
importance: medium
importance_rationale: "Captures Kastner's contemporaneous diagnosis of the industry-wide 90nm process wall that eventually forced both Intel (NetBurst cancellation) and Apple (Intel transition) to pivot."
relevance: low
relevance_rationale: "PowerPC G5 is discontinued; Apple moved to Intel 2005-2006 then Apple Silicon 2020. 90nm issues are a historical footnote."
prescience: high
prescience_rationale: "Kastner's 'another year' call was roughly right: Apple never shipped a 3GHz G5 from IBM and transitioned to Intel in 2005-2006; Intel's NetBurst-based clock race ended at 3.8GHz, with the subsequent pivot to Core architecture confirming the broader end of the GHz race."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 4
obs_count: 9
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Power Macs 'won't hit 3GHz this year' – analysts

> Macworld UK news piece (2004-06-11) reporting that Apple's self-imposed one-year 3GHz G5 target will miss its 11 June 2004 deadline, with analysts attributing the delay to industry-wide problems scaling the 90-nanometer manufacturing process. Peter Kastner, EVP and chief research officer at Aberdeen Research Group, quantifies the industry slowdown: Intel managed only 3.2→3.4GHz in the quarter while IBM got an 'A' for cranking the G5 from 2GHz to 2.5GHz — a 25% jump. Kastner predicts the industry will not reach 3GHz for another year.

**Author:** Macworld UK staff (IDG) · **Date:** 2004-06-11 · **Type:** news-article
**Importance:** medium — *Captures Kastner's contemporaneous diagnosis of the industry-wide 90nm process wall that eventually forced both Intel (NetBurst cancellation) and Apple (Intel transition) to pivot.*
**Prescience:** high — *Kastner's 'another year' call was roughly right: Apple never shipped a 3GHz G5 from IBM and transitioned to Intel in 2005-2006; Intel's NetBurst-based clock race ended at 3.8GHz, with the subsequent pivot to Core architecture confirming the broader end of the GHz race.*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[apple-computer|Apple Computer, Inc. / Apple Inc.]]
- [[ibm|International Business Machines Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[jupiterresearch|JupiterResearch]]
- [[macworld-uk|Macworld UK]]
- [[michael-gartenberg|Michael Gartenberg]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[tbr-research|Technology Business Research]]
- [[tim-deal|Tim Deal]]

## Technologies (4)

- [[90nm-process|90-nanometer semiconductor manufacturing process]]
- [[g5-cpu-3ghz-target|Apple 3GHz G5 one-year target]]
- [[ibm-powerpc-g5|IBM/Apple PowerPC G5 (PowerPC 970)]]
- [[intel-pentium-4|Intel Pentium 4 processor]]

## Key observations (top 25)

- **2004** — 90nm industry-wide clock issues: In switching to 90 nanometers, the industry has had more problems raising the clock speed than anyone anticipated a year ago.
- **2004** — Intel clock progress quarterly: Intel cranked up only a couple of hundred megahertz from 3.2GHz to 3.4GHz.
- **2004** — IBM G5 clock progress: IBM gets an 'A' for the second quarter for being able to crank the chip up from 2GHz to 2.5GHz — that's a 25 per cent increase.
- **2004** — Industry 3GHz target slips one year: Kastner doesn't expect the industry to reach the 3GHz target for another year.
- **2004** — Apple misses self-imposed G5 target: Apple missed its own 11 June 2004 deadline to ship a 3GHz G5; top speed as of article was 2.5GHz.
- **2004** — Apple analyst commentary: That's always the danger in making technology claims like that. You just have to hope that the laws of the universe can keep up with your claims.
- **2004** — IBM G5 supply concerns: I question IBM's ability to meet Apple's increased G5 processor demand moving forward given the company's availability challenges to date.
- **2005** — Apple abandons PowerPC: WWDC June 2005: Steve Jobs announces Apple's two-year transition from PowerPC to Intel x86; first Intel Macs shipped January 2006. G5 never reached 3GHz in shipping product.
- **2005** — Intel ends NetBurst clock race: Intel cancelled the 4GHz Pentium 4 roadmap and pivoted to the Core microarchitecture (Yonah 2006, Conroe 2006), confirming Kastner's diagnosis that the clock-speed race had hit a wall.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'power-macs-won-t-hit-3ghz-this-year-anal-73ad0f' ORDER BY year_observed;
```

