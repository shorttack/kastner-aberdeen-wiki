---
title: "IBM AS/400 vs. HP 3000 Marketplace Analysis for Stanley-Vidmar"
slug: "study-1989-vidmar-as400-hp3000-and-metadata-a32d04"
page_type: "study"
tags: ["type/study", "collection/consulting-report"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "1989-vidmar-as400-hp3000-and-metadata-a32d04"
author: "Peter S. Kastner / Aberdeen Group"
date: "1989-01-01"
pub_year: 1989
type: "consulting-report"
subject_domain: "midrange-computing-platform-selection"
methodology: "benchmarking,competitive-analysis,user-interviews,expert-opinion"
source_file: "1989 Vidmar AS400 HP3000 and metadata.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "low"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 1.45
prescience_obs_count: 20
---

# IBM AS/400 vs. HP 3000 Marketplace Analysis for Stanley-Vidmar


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.61 over 18 usable obs (0 prefiltered, 2 pending) -> high; 2 obs still pending (verdict may shift) [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.72 over 18 usable obs (0 prefiltered, 2 pending) -> high; 2 obs still pending (verdict may shift) [high>=3.5, medium>=2.0].

> This 1989 Aberdeen Group consulting report advises Stanley-Vidmar on the choice between upgrading to an HP Precision Architecture (HPPA) system versus converting to an IBM AS/400. Drawing on normalized DebitCredit benchmark data and analysis of Stanley-Vidmar's current HP 3000 Models 48 and 70, Aberdeen demonstrates that the AS/400 cannot provide adequate throughput growth while HPPA offers 2.5x capacity improvement with lower risk and conversion cost. The report recommends the HP 3000 Model 950 as the minimum entry point, upgradable to the 955 and 960.


_Published 1989, author **Peter S. Kastner / Aberdeen Group**, type **consulting-report**._


## Top observations

- MIPS invalid for AS/400 vs. HPPA comparison; AS/400 MIPS undisclosed by IBM; multiprocessor architecture makes definition unclear `[ps=5]`
- AS/400 evolved through iSeries, System i to IBM i on Power Systems; still actively supported in 2026 with 100,000+ installations `[ps=5]`
- Stanley Vidmar now Vidmar division of Stanley Black & Decker; still manufacturing heavy-duty storage cabinets in Allentown PA `[ps=5]`
- MIS staff expertise in HP MPE OS is a significant intangible asset; existing low-priority programs run in MPE V emulation indefinitely `[ps=4]`
- Journaling and Checksum recommended for production systems can reduce throughput by up to 60% `[ps=3]`
- Aberdeen: custom consulting from user interviews; Gartner: subscription research from supplier sources `[ps=3]`
- Not yet mature: no C compiler, 1MB program size limit, frequent OS patch tapes, OS/400 immature `[ps=2]`
- AS/400 lacks growth path today; multiple-AS/400 clustering not a reasonable alternative `[ps=1]`
- AS/400 OS/400 single-level storage more likely to require lengthy restores after system failure than conventional midrange approach `[ps=1]`
- 2.5x the performance of Model 70; CPU-upgradable to 955 and 960 `[ps=0]`
- AS/400 B60 offers ~25% less performance than HP 3000 Model 70; B70 approximates Model 70 `[ps=0]`
- High risk: MIS staff retraining, software conversion, new sales analysis system from scratch, cost escalation foreseeable `[ps=0]`
- Aberdeen recommends HP 950 as entry point; 955 if >25% growth per annum expected in 2 years `[ps=0]`
- Partner Richard Stuckey stated HP TurboImage was most impressive system in IBM's tests; AA subsequently OEM'd HP systems `[ps=0]`
- Aberdeen expects Allbase SQL performance to improve 50% during 1990 `[ps=0]`
- Aberdeen expects TurboImage performance on HPPA to improve 20% in 1990 `[ps=0]`
- HP ended support December 31, 2010; Stromasys emulator released 2012 for legacy sites `[ps=0]`
- Arthur Andersen dissolved 2002 following Enron audit scandal; Accenture (formerly Andersen Consulting) spun off 2001 `[ps=0]`
- 935 70% capacity improvement over Model 70 but not expandable; 950 CPU-upgradable to 955/960 for higher initial cost `[ps=0]`
- Aberdeen normalized DebitCredit results across HP's and IBM's vendor-specific benchmark runs to enable cross-vendor comparison `[ps=0]`
