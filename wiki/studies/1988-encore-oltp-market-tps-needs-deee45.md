---
title: "OLTP Market Transaction Processing Needs: A Vertical Market Analysis for Encore Computer"
slug: 1988-encore-oltp-market-tps-needs-deee45
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1988-01-01"
study_type: market-study
subject_domain: "OLTP-transaction-processing"
methodology: "industry-analysis,vertical-market-research,expert-opinion,benchmarking"
importance: high
importance_rationale: "First systematic sizing of high-end OLTP market by vertical segment with specific TPS thresholds; provided strategic market entry guidance for Encore's commercial mainframe alternative at a pivotal moment in the OLTP market's expansion."
relevance: medium
relevance_rationale: "TPS benchmarking methodology and vertical market classification remain analytically useful as historical baseline; specific hardware configurations and dollar market sizes are outdated, but the framework for segmenting OLTP demand by industry is still applied."
prescience: medium
prescience_rationale: "The study correctly identified communications, retail credit authorization, and transportation reservations as high-growth OLTP segments; however, Encore Computer failed commercially and the Series 90 never captured the predicted mainframe-alternative market."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 8
obs_count: 20
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# OLTP Market Transaction Processing Needs: A Vertical Market Analysis for Encore Computer

> This 1988 Aberdeen Group report prepared for Encore Computer Corporation analyzes online transaction processing (OLTP) market requirements across ten industry verticals—including banking, brokerage, retail, transportation, communications, and government. The study characterizes TPS throughput demands per application segment, sizes the high-end OLTP market at $1.4 billion (1989, >25 TPS) and $630M (>100 TPS), and identifies the top ten priority market/application areas for Encore's forthcoming commercial Series 90 system. Aberdeen concludes that multi-user people-to-computer OLTP and outstanding price/performance versus IBM 3090 mainframes are the most viable commercial strategies for the Series 90.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1988-01-01 · **Type:** market-study
**Importance:** high — *First systematic sizing of high-end OLTP market by vertical segment with specific TPS thresholds; provided strategic market entry guidance for Encore's commercial mainframe alternative at a pivotal moment in the OLTP market's expansion.*
**Prescience:** medium — *The study correctly identified communications, retail credit authorization, and transportation reservations as high-growth OLTP segments; however, Encore Computer failed commercially and the Series 90 never captured the predicted mainframe-alternative market.*

## Entities (12)

- [[enc-01|Encore Computer Corporation]]
- [[enc-02|Aberdeen Group]]
- [[enc-03|IBM]]
- [[enc-04|Hewlett-Packard]]
- [[enc-05|Digital Equipment Corporation]]
- [[enc-06|American Airlines (SABRE)]]
- [[enc-07|VISA / MasterCard]]
- [[enc-08|Dow Jones / Reuters / Telerate]]
- [[enc-09|Thinking Machines Corporation]]
- [[enc-10|Sears/IBM Prodigy]]
- [[enc-11|Federal Aviation Administration]]
- [[enc-12|Social Security Administration]]

## Technologies (8)

- [[t88-01|IBM 3090 Mainframe]]
- [[t88-02|Encore Series 90 (Commercial)]]
- [[t88-03|CICS]]
- [[t88-04|DB2]]
- [[t88-05|DebitCredit Benchmark (TPC-A precursor)]]
- [[t88-06|UNIX (System V)]]
- [[t88-07|IBM SABRE Reservation System]]
- [[t88-08|Object-Oriented Databases (OODB)]]

## Key observations (top 25)

- **1988** — Encore Series 90 primary OLTP positioning: Price/performance advantage over IBM 3090 mainframes; targets high-end commercial OLTP
- **1988** — Total high-end OLTP market size (>25 TPS, 1989): $1.4 billion
- **1988** — Total high-end OLTP market size (>100 TPS, 1990): $630 million
- **1988** — SABRE system peak TPS throughput: 2,000 TPS peak; 200 TPS per IBM 3090-200; growing at 15% per annum
- **1988** — Credit authorization peak TPS (VISA/MasterCard positive auth): 200 TPS
- **1988** — Government OLTP market priority ranking: #3 of 10 priority markets; estimated $200M high-end OLTP market
- **1988** — IBM 3090-180J OLTP throughput with CICS/DB2: ~40 TPS; $8M five-year lifecycle cost
- **1988** — Commercial Series 90 market viability as IBM mainframe alternative: Aberdeen believes commercial Series 90 can address wider database/data-communications commercial markets with outstanding price/performance in multiples of IBM mainframes
- **1999** — Encore Computer commercial market outcome: Encore failed commercially; Series 90 did not displace IBM mainframes; company liquidated January 1999
- **1988** — Communications OLTP priority #1 market size: $40M estimated; call switching 400 TPS growing to 600 TPS in 5 years
- **1988** — Manufacturing/distribution OLTP priority #6 market size: $50M estimated
- **1988** — Banking retail OLTP priority #8 market size: $65M estimated; 125 TPS mainframe norm in Europe
- **1988** — Social Security Administration OLTP volume estimate: 100 TPS aggregate over 10,000 terminals
- **1988** — Massively parallel computing for information retrieval: Thinking Machines installed at Dow Jones for full-text retrieval; early commercial deployment
- **1988** — Prodigy videotext service TPS projection: Sears/IBM Prodigy expects 100 TPS within three years
- **1988** — Object-oriented database adoption by insurance industry: Aberdeen believes insurance industry will increasingly embrace digital imaging and object-oriented databases
- **1988** — RDBMS performance for relationship banking: RDBMS performance has been poor until recently; cannot be price/performance justified for decision support with real-time query requirements
- **1988** — UNIX desirability for OLTP/government: UNIX is highly desirable for military COTS OLTP; intelligence analysis, logistics, and decision systems
- **1988** — DebitCredit benchmark as industry standard: DebitCredit evolving as de facto standard for measuring OLTP performance; TPS at 95th percentile <1 second response
- **1988** — OLTP market attractiveness rating criteria: Six factors: demonstrable high-end processing requirements; market barriers to entry; entrenched competition; financial attractiveness; time to market for new applications; market innovation or risk aversion tendencies

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1988-encore-oltp-market-tps-needs-deee45' ORDER BY year_observed;
```

