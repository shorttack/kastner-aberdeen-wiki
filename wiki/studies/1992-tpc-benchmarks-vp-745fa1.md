---
title: "Better Performance and Lower Prices Through TPC Benchmarks"
slug: 1992-tpc-benchmarks-vp-745fa1
page_type: study
author: "Aberdeen Group"
date: "1992-03-15"
study_type: viewpoint
subject_domain: "database-benchmarking"
methodology: "industry-analysis, benchmarking, competitive-profiling"
importance: high
importance_rationale: "First comprehensive independent analysis of TPC benchmarks' impact on buyer value; shaped enterprise procurement practices by establishing TPC-A as a mandatory RFP requirement"
relevance: medium
relevance_rationale: "Benchmarking methodology principles transfer directly to modern cloud/database benchmarking; TPC-C remains active today; specific hardware platforms are dated but competitive dynamics are instructive"
prescience: high
prescience_rationale: "Predicted TPC-C would become very important (correct — TPC-C became the dominant OLTP benchmark for decades); predicted continued price-performance improvements through 1993 (correct); predicted Unix/RDBMS contenders gaining against proprietary systems (correct — Unix/Linux ultimately won)"
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 16
obs_count: 40
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Better Performance and Lower Prices Through TPC Benchmarks

> First comprehensive independent analysis of TPC benchmarks' impact on buyer value. Aberdeen Group examines how Transaction Processing Council benchmarks TPC-A, TPC-B, and TPC-C transformed commercial performance measurement from unreliable vendor claims ('benchmarketing') into a rigorous standard. The study documents dramatic price-performance improvements (79% drop in K$/TPS-A since 1990), analyzes Digital Equipment's VAX benchmark realignment, and profiles Hewlett-Packard's gains. Includes predictions on TPC-C adoption and continued buyer benefits through 1993.

**Author:** Aberdeen Group · **Date:** 1992-03-15 · **Type:** viewpoint
**Importance:** high — *First comprehensive independent analysis of TPC benchmarks' impact on buyer value; shaped enterprise procurement practices by establishing TPC-A as a mandatory RFP requirement*
**Prescience:** high — *Predicted TPC-C would become very important (correct — TPC-C became the dominant OLTP benchmark for decades); predicted continued price-performance improvements through 1993 (correct); predicted Unix/RDBMS contenders gaining against proprietary systems (correct — Unix/Linux ultimately won)*

## Entities (11)

- [[ent-001|Transaction Processing Council (TPC)]]
- [[ent-002|Aberdeen Group]]
- [[ent-003|Digital Equipment Corporation (DEC)]]
- [[ent-004|Hewlett-Packard (HP)]]
- [[ent-005|IBM]]
- [[ent-006|Sequent Computer Systems]]
- [[ent-007|Bull (Groupe Bull)]]
- [[ent-008|Data General]]
- [[ent-009|Sun Microsystems]]
- [[ent-010|Compaq]]
- [[ent-011|Intel]]

## Technologies (16)

- [[tech-001|TPC-A benchmark]]
- [[tech-002|TPC-B benchmark]]
- [[tech-003|TPC-C benchmark]]
- [[tech-004|VAX (DEC VAX)]]
- [[tech-005|MicroVAX]]
- [[tech-006|VAX VMS (OpenVMS)]]
- [[tech-007|Rdb/VMS (Oracle Rdb)]]
- [[tech-008|PCI bus]]
- [[tech-009|Unix servers]]
- [[tech-010|RDBMS (relational databases)]]
- [[tech-011|AS/400]]
- [[tech-012|HP 3000]]
- [[tech-013|MPE/iX]]
- [[tech-014|HP-UX]]
- [[tech-015|ALLBASE RDBMS]]
- [[tech-016|Alpha RISC]]

## Key observations (top 25)

- **1990** — tpc_a_price_performance_kd_per_tps: 36.5 K$/TPS-A
- **1992** — tpc_a_price_performance_best_kd_per_tps: 7.7 K$/TPS-A
- **1992** — tpc_a_price_performance_percent_drop_since_1990: 79%
- **1992** — tpc_a_leadership_changes_q1_1992: 6 changes in 2.5 months
- **1992** — tpc_a_price_performance_improvement_2_years: 5x (fivefold)
- **1992** — tpc_a_price_performance_improvement_q1_1992: 35%
- **1992** — tpc_a_price_performance_approaching_floor: ~$7.5K/TPS-A
- **1994** — tpc_a_price_performance_expected_slowdown: ~$6.5K/TPS-A
- **1992** — tpc_a_best_performance_28tps_price: 28 TPS-A at $214K total
- **1992** — tpc_a_price_performance_leader_q1_1992: Led with DPX/2
- **1992** — tpc_a_price_performance_leader_q1_1992: Led with Sparcserver
- **1992** — tpc_a_price_performance_aviion_5225: Failed to crack $10K barrier
- **1992** — vax_6000_640_tpc_a_throughput: >200 TPS-A
- **1988** — vax_8830_debit_credit_throughput: 27 TPS
- **1992** — vax_throughput_improvement_1988_to_1992: 7x improvement
- **1992** — microvax_3100_80_price_performance: $7.69 K$/TPS-A
- **1992** — microvax_4000_300_price_performance: $10.71 K$/TPS-A
- **1992** — vax_6000_price_performance_range: $7.69 to $10.71 K$/TPS-A
- **1992** — vax_price_performance_flatness: Within 20% across product line
- **1992** — as400_price_performance_spread: 77% more expensive at high end
- **1992** — microvax_4000_300_improvement_20_months: 3x improvement from $31.90 to $10.71 K$/TPS-A
- **1992** — rdb_vms_performance_improvement_mechanism: Software efficiency gains equivalent to free hardware upgrade
- **1992** — microvax_4000_300_cost_reduction_factors: Disk -24%; memory -25%; 32MB less memory; 25% service discount; lower terminal prices
- **1992** — digital_vax_alpha_transition_strategy: VAX fire sale / Alpha transition
- **1992** — hp_3000_midrange_price_performance_improvement: 61% improvement since Jan 1990

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1992-tpc-benchmarks-vp-745fa1' ORDER BY year_observed;
```

