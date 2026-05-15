---
title: "Fault-Tolerant Systems Special Report — Information Systems News, 6 August 1984 (PSK at Stratus)"
slug: stratus-fault-tolerant-mkt-info-systems-1984-eb925f
page_type: study
author: "Omri Serlin; Paul E. Schindler Jr.; Jean S. Bozman (Information Systems News)"
date: "1984-08-06"
study_type: press-article
subject_domain: "fault-tolerant-computing-market-analysis"
methodology: "industry-analysis, expert-opinion, market-sizing"
importance: high
importance_rationale: "Major trade-press special report establishing the 1984 FT/OLTP market structure (Tandem vs Stratus duopoly, with Stratus as #2 at ~5.6% of a $712M segment) and capturing Kastner's authoritative articulation of the Stratus hardware-fault-tolerance philosophy during his Stratus marketing tenure."
relevance: medium
relevance_rationale: "Hardware-vs-software fault-tolerance debate has been largely settled by the cluster/software-HA approach in modern always-on systems, but the architectural taxonomy remains useful for understanding the lineage of today's resilient distributed systems."
prescience: high
prescience_rationale: "Serlin's framing that ~24 FT startups would mostly fail to reach production proved correct — by the early 1990s only Tandem, Stratus, and a handful of niche players remained. His observation that operator errors and communications-line failures were becoming larger downtime contributors than CPU/disk failures also anticipated the post-1990 shift in availability engineering toward people/process and network design."
license: CC-BY-4.0
tier: 1
entity_count: 15
tech_count: 6
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Fault-Tolerant Systems Special Report — Information Systems News, 6 August 1984 (PSK at Stratus)

> Multi-article fault-tolerant systems special report from Information Systems News, 6 August 1984, comprising three companion pieces by Omri Serlin (\"Nonstop Challenges in Fault-Tolerant Market\"), Paul E. Schindler Jr. (\"Fault-Tolerant Solutions Vary With Vendor\") and Jean S. Bozman (\"Users Find 'Fault Tolerance' a Relative Term\"). The report frames Tandem Computers and Stratus Computer as the only FT/OLTP suppliers to have successfully transitioned from development to full production by 1984, while ~24 startups stalled. Includes 1984 transaction-processing market projection charts ($22.5B total; IBM $17.5B / 77.8%; FT suppliers $712M / 3.2%; Tandem $585M / 82% of FT segment, Stratus $40M / 5.6%, Computer Consoles $67M / 9.4%, Synapse/Auragen/Tolerant/Sequoia $20M / 2.8%). Schindler's piece positions \"the philosophical leader of the hardware fault-tolerant camp\" as Stratus and quotes **Peter Kastner, manager of Stratus' corporate business development**, summing up the Stratus philosophy as \"hardware redundancy which is controlled by hardware, rather than by software\" — and arguing that the four-CPU checking design has \"definite advantages\" over software-based systems, with chips only 2 percent of system selling price. Bozman's user-experience piece reports a New York investment firm pulled boards at random from a Stratus system to test resilience: \"the only way we got it to stop was to pull out enough CPU boards to make it non-functional. However, the moment we replaced the CP…

**Author:** Omri Serlin; Paul E. Schindler Jr.; Jean S. Bozman (Information Systems News) · **Date:** 1984-08-06 · **Type:** press-article
**Importance:** high — *Major trade-press special report establishing the 1984 FT/OLTP market structure (Tandem vs Stratus duopoly, with Stratus as #2 at ~5.6% of a $712M segment) and capturing Kastner's authoritative articulation of the Stratus hardware-fault-tolerance philosophy during his Stratus marketing tenure.*
**Prescience:** high — *Serlin's framing that ~24 FT startups would mostly fail to reach production proved correct — by the early 1990s only Tandem, Stratus, and a handful of niche players remained. His observation that operator errors and communications-line failures were becoming larger downtime contributors than CPU/dis…*

## Entities (15)

- [[att-3b20d|AT&T 3B20D]]
- [[august-systems|August Systems Inc.]]
- [[auragen-systems-corp|Auragen Systems Corp.]]
- [[computer-consoles-inc|Computer Consoles Inc.]]
- [[dec-digital-equipment|Digital Equipment Corporation]]
- [[ibm|IBM]]
- [[itom-international|ITOM International Co.]]
- [[omri-serlin|Omri Serlin]]
- [[parallel-computers-inc|Parallel Computers Inc.]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sequoia-systems|Sequoia Systems]]
- [[stratus-computer|Stratus Computer]]
- [[synapse-computer-corp|Synapse Computer Corp.]]
- [[tandem-computers|Tandem Computers]]
- [[tolerant-systems|Tolerant Systems Inc.]]

## Technologies (6)

- [[hardware-fault-tolerance|Hardware fault tolerance]]
- [[motorola-68000|Motorola MC 68000]]
- [[oltp-online-transaction-processing|OLTP (online transaction processing)]]
- [[software-fault-tolerance|Software fault tolerance]]
- [[stratus-continuous-processing|Stratus Continuous Processing]]
- [[unix-rtr|Unix Real Time Reliable (Unix RTR)]]

## Key observations (top 25)

- **1984** — 1984 transaction-processing market size: $22.5B total: IBM $17.5B (77.8%); BUNCH/Amdahl/NAS $3B (13.3%); DEC/DG/HP/Prime/superminis $1B (4.4%); Fault-Tolerant suppliers $712M (3.2%)
- **1984** — 1984 FT/OLTP segment share: Tandem $585M/82%; Computer Consoles $67M/9.4%; Stratus $40M/5.6%; Synapse/Auragen/Tolerant/Sequoia et al $20M/2.8% — total $712M
- **1984** — Stratus philosophy on fault tolerance: Hardware redundancy controlled by hardware, rather than by software
- **1984** — Stratus chip-cost-fraction argument: Chips amount to only 2 percent of the selling price of a typical system; cost disadvantage of redundant hardware is overstated
- **1984** — Hardware-vs-software fault frequency: Hardware faults are far more infrequent than software faults
- **1984** — FT startup viability: Of ~24 FT/OLTP entrants 1980-1983, only Tandem and Stratus had completed transition from development to full production by 1984; many had product delays and capital-raising difficulties
- **1984** — Operator errors and comms lines as downtime cause: Mounting evidence that 'operator errors' and remote-communications-line problems are far more significant downtime factors than processor failures and disk crashes — neither problem effectively addressed in any current FT systems
- **1984** — User stress test of Stratus: New York investment firm tested by pulling printed-circuit boards at random; only way to stop the system was to pull enough CPU boards to make it non-functional, and once replaced it was off and running again

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-fault-tolerant-mkt-info-systems-1984-eb925f' ORDER BY year_observed;
```

