---
title: "Stratus Readies XA2000 Series to Take on Tandem High End — Computerworld, 2 February 1987 (PSK + Foster quoted)"
slug: stratus-xa2000-launch-cw-1987-11913f
page_type: study
author: "James Connolly (Computerworld)"
date: "1987-02-02"
study_type: press-article
subject_domain: "fault-tolerant-computing-product-launch"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
importance: high
importance_rationale: "Companion to the ABA Banking Journal launch ad (study #9). Captures Kastner under yet another title — 'manager of marketing support programs' — bringing his Stratus-titles tally to three (marketing-development, communications director, corporate business development, marketing support programs). Includes Foster's CEO-level OLTP-market thesis and Yankee Group's contemporaneous skepticism about Stratus' application depth."
relevance: medium
relevance_rationale: "OLTP/transaction-processing as the key driver of computing demand has been borne out by the cloud era. The Foster framing is a precursor to the modern digital-transformation narrative."
prescience: high
prescience_rationale: "Foster's prediction that 'most new applications tend to be on-line applications' and 'that is really what is driving the market' was exactly correct — the ensuing decades saw every major application class go online. Yankee Group's question about long-term IBM-Stratus compatibility was prescient: IBM dropped the System/88 by the early 1990s, exactly as the analyst worried."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 7
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Stratus Readies XA2000 Series to Take on Tandem High End — Computerworld, 2 February 1987 (PSK + Foster quoted)

> Computerworld feature on the Stratus XA2000 launch (the same family advertised in the ABA Banking Journal ad above). Article reports Stratus is launching a 'full-scale attack' on Tandem with the XA2000 family, pitting the high end against Tandem's 10-month-old NonStop VLX flagship; both vendors claim 50+ transactions/second peak. **William E. Foster, Stratus CEO**, quoted: 'We are selling into a market that has an insatiable appetite for transactions per second' and 'Most new applications for computers tend to be on-line applications. That is really what is driving the market. While people are looking at an on-line application, they have to ask themselves what happens if this thing goes down.' **Peter S. Kastner, manager of marketing support programs for Stratus**, explains the floating-point coprocessor (Motorola 68881) is designed for financial-modeling applications, not scientific/engineering markets. Article reports Stratus officials anticipate near-simultaneous IBM announcement adding XA2000 to **System/88 product line** (under Stratus-IBM OEM). Models 110/120/130/140 use single 40-slot chassis, Motorola 16-MHz 68020 + 68881 coprocessor, VOS Release 6.0 with 32-bit data path, 64MB memory, 64KB cache, 128MB virtual address, 46GB disk. Pricing: $260K-$500K Model 110; $770K-$1.1M Model 140. Yankee Group's Thomas Henkel comments this is Stratus' first move into VLX/IBM 3090 class but questions long-term IBM-Stratus compatibility and Stratus' application/database depth for hi…

**Author:** James Connolly (Computerworld) · **Date:** 1987-02-02 · **Type:** press-article
**Importance:** high — *Companion to the ABA Banking Journal launch ad (study #9). Captures Kastner under yet another title — 'manager of marketing support programs' — bringing his Stratus-titles tally to three (marketing-development, communications director, corporate business development, marketing support programs). Inc…*
**Prescience:** high — *Foster's prediction that 'most new applications tend to be on-line applications' and 'that is really what is driving the market' was exactly correct — the ensuing decades saw every major application class go online. Yankee Group's question about long-term IBM-Stratus compatibility was prescient: IBM…*

## Entities (8)

- [[ibm|IBM]]
- [[motorola|Motorola]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[thomas-henkel|Thomas Henkel]]
- [[william-e-foster|William E. Foster]]
- [[yankee-group|The Yankee Group]]

## Technologies (7)

- [[ibm-3090|IBM 3090]]
- [[ibm-system-88|IBM System/88]]
- [[motorola-68020|Motorola 68020]]
- [[motorola-68881|Motorola 68881 math coprocessor]]
- [[stratus-vos|Stratus VOS Release 6.0]]
- [[stratus-xa2000-family|Stratus XA2000 family]]
- [[tandem-nonstop-vlx|Tandem NonStop VLX]]

## Key observations (top 25)

- **1987** — OLTP market thesis: Most new applications for computers tend to be on-line applications. That is really what is driving the market. While people are looking at an on-line application, they have to ask themselves what happens if this thing goes down
- **1987** — TPS rates and growth: Both Stratus and Tandem claim 50+ TPS; Stratus designed XA2000 for 45% annual growth in OLTP market over 5 years to >50 TPS averages
- **1987** — XA2000 ET-1 ratings: Model 110 = 15 TPS; Model 120 = 27-29 TPS; Model 130 = 37-40 TPS; Model 140 = 47-53 TPS (ET-1 benchmark)
- **1987** — XA2000 architecture: Single 40-slot chassis Models 110-140; Motorola 68020 16-MHz + 68881 coprocessor; VOS 6.0 with 32-bit data path; 64MB memory, 64KB cache, 128MB virtual address, 46GB disk; Model 140 has four tightly-coupled duplicated CPUs
- **1987** — XA2000 pricing: $260,000-$500,000 Model 110; $770,000-$1.1M Model 140; transaction-per-second cost half of earlier Stratus products
- **1987** — Floating-point use case: 68881 designed to help users in existing on-line transaction processing markets perform tasks such as financial modeling; no plans to enter scientific/engineering markets
- **1987** — IBM-Stratus longevity question: Yankee Group Henkel questioned how long IBM will maintain its relationship with Stratus if Stratus' products continue to compete with 3090 mainframes
- **1987** — Stratus application depth gap: Henkel doubted Stratus had enough application and data base software to support high-performance transaction processing, particularly in growth areas such as manufacturing

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-xa2000-launch-cw-1987-11913f' ORDER BY year_observed;
```

