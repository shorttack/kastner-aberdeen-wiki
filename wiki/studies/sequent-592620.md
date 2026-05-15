---
title: "Sequent Servers and Data General Servers"
slug: sequent-592620
page_type: study
author: "Aberdeen Group"
date: "1994"
study_type: market-study
subject_domain: "midrange-server-market"
methodology: "competitive-profiling, document-review, industry-analysis"
importance: high
importance_rationale: "Rare surviving example of an Aberdeen Group IBM-confidential competitive intelligence brief from 1994; captures market-share dynamics, pricing structures, and benchmark data for Sequent and Data General at the peak of the Unix server wars."
relevance: low
relevance_rationale: "Both Sequent and Data General have ceased to exist as independent companies; document has historical value for understanding mid-1990s midrange server competition but no current operational relevance."
prescience: high
prescience_rationale: "The document correctly flagged Data General's Motorola 88K chipset as a strategic risk and noted DG's financial losses; DG was acquired by EMC in 1999. Sequent's financial fragility concern proved accurate; IBM acquired Sequent in 1999., confidentiality: ibm-confidential"
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 15
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Sequent Servers and Data General Servers

> This IBM-confidential competitive briefing prepared by Aberdeen Group profiles two midrange Unix server vendors — Sequent Computer Systems and Data General — for IBM sales force use circa 1994. The document covers product lines, pricing, TPS-A benchmark results, sales messages, and competitive strengths and concerns for each vendor, enabling IBM representatives to position against them in contested accounts.

**Author:** Aberdeen Group · **Date:** 1994 · **Type:** market-study
**Importance:** high — *Rare surviving example of an Aberdeen Group IBM-confidential competitive intelligence brief from 1994; captures market-share dynamics, pricing structures, and benchmark data for Sequent and Data General at the peak of the Unix server wars.*
**Prescience:** high — *The document correctly flagged Data General's Motorola 88K chipset as a strategic risk and noted DG's financial losses; DG was acquired by EMC in 1999. Sequent's financial fragility concern proved accurate; IBM acquired Sequent in 1999., confidentiality: ibm-confidential*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[ca-technologies|CA Technologies]]
- [[data-general|Data General]]
- [[ibm|IBM]]
- [[informix|Informix]]
- [[intel|Intel Corporation]]
- [[motorola|Motorola]]
- [[oracle|Oracle]]
- [[sequent-computer-systems|Sequent Computer Systems]]

## Technologies (15)

- [[decnet|DECnet]]
- [[dg-ux|DG/UX]]
- [[dynix-ptx|DYNIX/ptx]]
- [[fddi|FDDI]]
- [[informix-dsa|Informix DSA]]
- [[motorola-88k|Motorola 88K]]
- [[netware|NetWare]]
- [[oracle-parallel-server|Oracle Parallel Server]]
- [[raid|RAID]]
- [[scsi-2|SCSI-2]]
- [[sna|SNA]]
- [[token-ring|Token Ring]]
- [[unix-svr4|UNIX SVR4]]
- [[vmEbus|VMEbus]]
- [[windows-nt|Windows NT]]

## Key observations (top 25)

- **1994** — Max SMP processors — Sequent Symmetry: 30
- **1993** — Annual revenue — Sequent: $354 million (fiscal 1993)
- **1994** — TPS-A benchmark — Symmetry 2000/250: 183.34 tps-A
- **1994** — TPS-A benchmark — Symmetry 2000/750 (2-cluster): 1002.37 tps-A
- **1994** — Entry price — Symmetry 2000 midrange (290 model): $85,000
- **1994** — Entry price — Symmetry 5000 (SE20): $171,100
- **1994** — Entry price — Symmetry 5000 (SE60): $469,800
- **1994** — WinServer entry price range: $13,200 (WinServer 500) to $246,900 (WinServer 5000)
- **1994** — Key strength — SMP scalability: Best-in-class SMP parallelism up to 30 processors
- **1994** — Key customer concern — financial viability: Under-$500-million size; financial losses; lack of long-term profitability
- **1994** — Informix DSA parallelism exclusivity: 6-month exclusivity on Informix DSA parallelism
- **1994** — Windows NT strategy: Positioning NT on Intel for early adopters while maintaining UNIX leadership
- **1994** — DYNIX/ptx OS version upgrade: Just moved up to UNIX V.4
- **1994** — Sequent long-term financial viability: At risk — financial losses and sub-$500M revenue make survival uncertain
- **1999** — Sequent long-term financial viability — outcome: Confirmed risk — Sequent's financial fragility noted; acquired by IBM July 1999 for $810M due to inability to sustain independently
- **1994** — Max SMP processors — Data General Aviion: 16
- **1993** — Annual revenue — Data General: $1 billion (fiscal 1993)
- **1994** — TPS-A benchmark — Aviion 5500: 130.9 tps-A
- **1994** — TPS-A cost efficiency — Aviion 5500: $5,780 per tps-A
- **1994** — TPS-A benchmark — Aviion 9500: 523.64 tps-A
- **1994** — TPS-A cost efficiency — Aviion 9500: $5,357 per tps-A
- **1994** — Max external storage — Aviion 9500: 2 TB
- **1994** — Motorola 88K chipset — strategic risk: Motorola 88K chipset identified as approaching end of life
- **1994** — Data General platform longevity — chip risk: Motorola 88K EOL creates serious platform continuity risk for DG
- **1999** — Data General platform longevity — outcome: Confirmed — Motorola 88K officially EOL January 1998; Data General forced to transition to Intel; DG acquired by EMC 1999

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sequent-592620' ORDER BY year_observed;
```

