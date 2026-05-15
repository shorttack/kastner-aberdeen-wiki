---
title: "IBM AS/400 vs. HP 3000 Marketplace Analysis for Stanley-Vidmar"
slug: 1989-vidmar-as400-hp3000-and-metadata-a32d04
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1989-01-01"
study_type: consulting-report
subject_domain: "midrange-computing-platform-selection"
methodology: "benchmarking,competitive-analysis,user-interviews,expert-opinion"
importance: high
importance_rationale: "This is believed to be the first independent benchmark comparison of AS/400 vs. HP 3000 in a real manufacturing user context; Aberdeen's methodology of normalizing DebitCredit results across vendor benchmarks was cited as pioneering by the industry press."
relevance: medium
relevance_rationale: "The AS/400 vs. HP 3000 competitive analysis is historically significant; the recommendation framework for platform selection (risk, conversion cost, staff expertise, growth path) remains directly applicable to modern legacy migration decisions."
prescience: high
prescience_rationale: "Aberdeen correctly predicted the AS/400's performance shortcomings and maturity issues in 1989; HP 3000 indeed outlasted AS/400's original product line, running until 2010; Stanley-Vidmar remained part of The Stanley Works and is now Vidmar within Stanley Black & Decker."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 10
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# IBM AS/400 vs. HP 3000 Marketplace Analysis for Stanley-Vidmar

> This 1989 Aberdeen Group consulting report advises Stanley-Vidmar on the choice between upgrading to an HP Precision Architecture (HPPA) system versus converting to an IBM AS/400. Drawing on normalized DebitCredit benchmark data and analysis of Stanley-Vidmar's current HP 3000 Models 48 and 70, Aberdeen demonstrates that the AS/400 cannot provide adequate throughput growth while HPPA offers 2.5x capacity improvement with lower risk and conversion cost. The report recommends the HP 3000 Model 950 as the minimum entry point, upgradable to the 955 and 960.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1989-01-01 · **Type:** consulting-report
**Importance:** high — *This is believed to be the first independent benchmark comparison of AS/400 vs. HP 3000 in a real manufacturing user context; Aberdeen's methodology of normalizing DebitCredit results across vendor benchmarks was cited as pioneering by the industry press.*
**Prescience:** high — *Aberdeen correctly predicted the AS/400's performance shortcomings and maturity issues in 1989; HP 3000 indeed outlasted AS/400's original product line, running until 2010; Stanley-Vidmar remained part of The Stanley Works and is now Vidmar within Stanley Black & Decker.*

## Entities (10)

- [[e89-01|Stanley-Vidmar]]
- [[e89-02|Aberdeen Group]]
- [[e89-03|IBM]]
- [[e89-04|Hewlett-Packard]]
- [[e89-05|Arthur Andersen & Co.]]
- [[e89-06|Gartner Group]]
- [[e89-07|System Software Associates (SSA)]]
- [[e89-08|ADM Inc. (Cheshire CT)]]
- [[e89-09|IDC (International Data Corporation)]]
- [[e89-10|Forrester Research]]

## Technologies (10)

- [[t89-01|IBM AS/400 (OS/400)]]
- [[t89-02|HP 3000 (MPE/XL, TurboImage)]]
- [[t89-03|HP Precision Architecture (HPPA/PA-RISC)]]
- [[t89-04|DebitCredit Benchmark]]
- [[t89-05|IBM RAMP-C Benchmark]]
- [[t89-06|HP TurboImage (DBMS)]]
- [[t89-07|HP Allbase SQL]]
- [[t89-08|AS/400 SQL/400 and OS/400 Native File System]]
- [[t89-09|BPCS Manufacturing Package]]
- [[t89-10|MIPS (as performance metric)]]

## Key observations (top 25)

- **1989** — AS/400 product maturity: Not yet mature: no C compiler, 1MB program size limit, frequent OS patch tapes, OS/400 immature
- **1989** — HP HPPA Model 950 performance vs. HP 3000 Model 70: 2.5x the performance of Model 70; CPU-upgradable to 955 and 960
- **1989** — AS/400 B60 vs HP 3000 Model 70 DebitCredit performance: AS/400 B60 offers ~25% less performance than HP 3000 Model 70; B70 approximates Model 70
- **1989** — AS/400 conversion risk level for Stanley-Vidmar: High risk: MIS staff retraining, software conversion, new sales analysis system from scratch, cost escalation foreseeable
- **1989** — HPPA upgrade recommendation: Aberdeen recommends HP 950 as entry point; 955 if >25% growth per annum expected in 2 years
- **1989** — Arthur Andersen RAMP-C audit finding: Partner Richard Stuckey stated HP TurboImage was most impressive system in IBM's tests; AA subsequently OEM'd HP systems
- **1989** — AS/400 journaling performance impact: Journaling and Checksum recommended for production systems can reduce throughput by up to 60%
- **1989** — MIPS validity as comparative benchmark: MIPS invalid for AS/400 vs. HPPA comparison; AS/400 MIPS undisclosed by IBM; multiprocessor architecture makes definition unclear
- **1989** — Stanley-Vidmar HP expertise as intangible asset: MIS staff expertise in HP MPE OS is a significant intangible asset; existing low-priority programs run in MPE V emulation indefinitely
- **1989** — Aberdeen vs. Gartner Group competitive differentiation: Aberdeen: custom consulting from user interviews; Gartner: subscription research from supplier sources
- **1989** — HP Allbase SQL performance improvement projection: Aberdeen expects Allbase SQL performance to improve 50% during 1990
- **1989** — HP TurboImage performance improvement projection: Aberdeen expects TurboImage performance on HPPA to improve 20% in 1990
- **1989** — AS/400 long-term platform viability: AS/400 lacks growth path today; multiple-AS/400 clustering not a reasonable alternative
- **2026** — AS/400/IBM i longevity: AS/400 evolved through iSeries, System i to IBM i on Power Systems; still actively supported in 2026 with 100,000+ installations
- **2010** — HP 3000 end-of-life: HP ended support December 31, 2010; Stromasys emulator released 2012 for legacy sites
- **2024** — Stanley-Vidmar company outcome: Stanley Vidmar now Vidmar division of Stanley Black & Decker; still manufacturing heavy-duty storage cabinets in Allentown PA
- **2002** — Arthur Andersen dissolution: Arthur Andersen dissolved 2002 following Enron audit scandal; Accenture (formerly Andersen Consulting) spun off 2001
- **1989** — HP 935 vs. 950 cost/expandability trade-off: 935 70% capacity improvement over Model 70 but not expandable; 950 CPU-upgradable to 955/960 for higher initial cost
- **1989** — DebitCredit normalization methodology: Aberdeen normalized DebitCredit results across HP's and IBM's vendor-specific benchmark runs to enable cross-vendor comparison
- **1989** — AS/400 single-level storage crash recovery risk: AS/400 OS/400 single-level storage more likely to require lengthy restores after system failure than conventional midrange approach

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1989-vidmar-as400-hp3000-and-metadata-a32d04' ORDER BY year_observed;
```

