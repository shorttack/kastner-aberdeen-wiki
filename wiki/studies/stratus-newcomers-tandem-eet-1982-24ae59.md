---
title: "Newcomers Invade Fault-Tolerant Field, But Tandem Has Big Lead — Electronic Engineering Times, 24 May 1982 (PSK quoted)"
slug: stratus-newcomers-tandem-eet-1982-24ae59
page_type: study
author: "Electronic Engineering Times staff"
date: "1982-05-24"
study_type: press-article
subject_domain: "fault-tolerant-computing-market-entry"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
importance: high
importance_rationale: "Earliest documented Kastner press appearance (May 1982) — within months of Stratus' first product shipments — quoting him on Stratus' competitive position vs Tandem, design philosophy, and customer wins. Foundational artifact for Kastner's Stratus chapter and for understanding the FT-market entry dynamics of 1982."
relevance: medium
relevance_rationale: "Specific competitive dynamics are historical; the broader pattern of incumbent-vs-startup disruption in regulated/high-availability segments remains an evergreen template."
prescience: medium
prescience_rationale: "Kastner's claim that Stratus' superior design features would make it a heavyweight proved partially correct — Stratus did become the durable #2 FT vendor for two decades, but Tandem retained leadership and Stratus never overtook it. Larry Roberts' prediction that Tandem would ship 32-bit within 18 months proved approximately correct (NonStop II/TXP came mid-decade)."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 6
obs_count: 10
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Newcomers Invade Fault-Tolerant Field, But Tandem Has Big Lead — Electronic Engineering Times, 24 May 1982 (PSK quoted)

> Electronic Engineering Times feature article examining new entrants challenging Tandem Computers' overwhelming dominance of the fault-tolerant computer-systems market. Newcomers profiled: **Stratus Computers (Natick, MA)**, **August Systems (Tigard, OR)**, and **Synapse Computers (Milpitas, CA)**. Stratus is identified as the biggest threat to Tandem, having begun shipments in February 1982. **Peter Kastner, manager of marketing development at Stratus**, claims the company has already \"taken away some orders from Tandem\" — selling to a dairy company and a shoe-store chain. Stratus output of four systems per month is below Tandem's pace, but Kastner argues Stratus will become a heavyweight based on design features superior to the leader's, and on price (minimum-configuration Stratus ~$110,000 below the $260,000 equivalent Tandem package). Kastner contrasts Stratus' hardware-based 32-bit architecture with Tandem's software-based 'Guardian' approach (parallel processors with periodic review and Encompass transaction tracking). Article also includes 32-bit-architecture debate (Tandem's Jerry Peterson argues 16-vs-32 bits is irrelevant for transaction throughput; Larry Roberts of Hambrecht & Quist predicts Tandem will ship 32-bit within 18 months). Strategic Business Services projects $2.6B FT hardware/peripherals annual market by 1988; Dataquest forecasts $5B annual including software by 1985. SIAC's John McGee describes the established-vendor switching cost barrier facing newcom…

**Author:** Electronic Engineering Times staff · **Date:** 1982-05-24 · **Type:** press-article
**Importance:** high — *Earliest documented Kastner press appearance (May 1982) — within months of Stratus' first product shipments — quoting him on Stratus' competitive position vs Tandem, design philosophy, and customer wins. Foundational artifact for Kastner's Stratus chapter and for understanding the FT-market entry dy…*
**Prescience:** medium — *Kastner's claim that Stratus' superior design features would make it a heavyweight proved partially correct — Stratus did become the durable #2 FT vendor for two decades, but Tandem retained leadership and Stratus never overtook it. Larry Roberts' prediction that Tandem would ship 32-bit within 18 m…*

## Entities (11)

- [[august-systems|August Systems Inc.]]
- [[dataquest|Dataquest]]
- [[gartner-group|Gartner Group]]
- [[hambrecht-quist|Hambrecht & Quist]]
- [[intel-iapx-432|Intel iAPX 432]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[siac-securities-industry-automation|Securities Industry Automation Corporation (SIAC)]]
- [[strategic-business-services|Strategic Business Services]]
- [[stratus-computer|Stratus Computer]]
- [[synapse-computer-corp|Synapse Computer Corp.]]
- [[tandem-computers|Tandem Computers]]

## Technologies (6)

- [[32-bit-architecture|32-bit architecture]]
- [[intermarket-trading-system|Intermarket Trading System (ITS)]]
- [[stratalink|Stratalink]]
- [[stratus-continuous-processing|Stratus Continuous Processing]]
- [[tandem-encompass-tps|Tandem Encompass TPS]]
- [[tandem-guardian-os|Tandem Guardian OS]]

## Key observations (top 25)

- **1981** — FT market 1981 size: ~$100M industry sales (CPU hardware + peripherals specifically packaged with FT systems) per Strategic Business Services Nov 1981 survey 'Survivable Systems: Pitfalls and Opportunities'
- **1981** — Tandem 1981 sales: $208M; ~total domination of fault-tolerant market
- **1981** — Tandem growth rate: ~106% revenue growth annually for past three years; targets $1B by 1985 (~20% market share)
- **1988** — FT hardware/peripherals 1988 forecast: $2.6B annual sales by 1988 per Strategic Business Services
- **1985** — Total FT market 1985 forecast: $5B annual volume by 1985 (including software) per Dataquest
- **1982** — Stratus competitive wins: Stratus has already taken away some orders from Tandem — sold to a dairy company and a shoe-store chain
- **1982** — Stratus output: Four systems per month — below Tandem's pace, but Kastner argues design features and price will make Stratus a heavyweight
- **1982** — Stratus vs Tandem price: Minimum-configuration Stratus is ~$110,000 below the $260,000 equivalent Tandem package
- **1982** — Stratus hardware-checking advantage: Every component is self-checking during each operating cycle; absolutely no user-software is involved in making existing applications fault-tolerant
- **1982** — Stratus 32-bit advantage: Stratus has faster computational ability and bigger memory system thanks to 32-bit capability vs Tandem's 16-bit internal data paths

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-newcomers-tandem-eet-1982-24ae59' ORDER BY year_observed;
```

