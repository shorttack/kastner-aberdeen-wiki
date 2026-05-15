---
title: "Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985)"
slug: stratus-internal-benchmark-tuning-guide--c53e3f
page_type: study
author: "Stratus Computer (internal engineering documentation)"
date: "1985"
study_type: internal-engineering-document
subject_domain: "transaction-processing/benchmark-tuning"
methodology: "internal-engineering-tuning-guide"
importance: high
importance_rationale: "Rare internal-use-only Stratus engineering document with verbatim 1985 TP-1 tuning results across three product lines. Provides the engineering ground truth for Stratus's pre-ET1 transaction-processing performance claims."
relevance: high
relevance_rationale: "Establishes the Stratus TP1 benchmark methodology (used widely in 1985-1986 marketing) and the production-system performance envelope that Kastner and other Stratus marketers were quoting from in trade-press appearances."
prescience: medium
prescience_rationale: "Stratus's 1985 internal TP1 design — PL/1 requester/server, parameterized loop counts to simulate workload, server-priority-above-requester tuning — anticipated the standardized TPC-A/B/C transaction benchmarks that emerged 1988-1992."
license: CC-BY-4.0
tier: 1
entity_count: 1
tech_count: 6
obs_count: 5
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985)

> Stratus Computer 1985 internal-use-only benchmark tuning guide documenting Stratus's internal TP-1 (transaction-processing) benchmark and the tuned performance results for three Stratus production systems: XA600 (5.0 tps with 2.1s avg / 3.3s 90th-percentile response, 80% CPU + 40% disk utilization, 3 duplexed D108 disks + 8 MB + 6 servers + 2 requesters with 80 tasks each); XA400 (3.4 tps, 1.8s avg / 2.7s 90th-percentile, 80% CPU + 25% disk, 8 MB + 3 Fuji disks + 4 servers + 2 requesters with 55 tasks); FT200 (1.7 tps, 2.1s avg / 3.5s 90th-percentile, 85% CPU + 18% disk, 8 MB + 2 Fuji disks + 1 requester with 55 tasks, server priority above requester). The guide describes TP1 as a PL/1 + COBOL requester/server simulation with parameterized indexed reads (5/tx), indexed rewrites (2/tx), sequential log writes (1/tx), 5,000-cycle requester CPU loop and 200-cycle server loop, 30-second sleep with +/-5s deviation, no screen I/O, no comms. Observations note task metering had no measurable effect, cache utilization significantly impacts performance, and multiple server copies improve performance. This document is the technical complement to the 1986 Stratus ET1 corpus (Batch 25 study #6+#7) — TP1 was the Stratus internal benchmark before ET1 became the industry standard.

**Author:** Stratus Computer (internal engineering documentation) · **Date:** 1985 · **Type:** internal-engineering-document
**Importance:** high — *Rare internal-use-only Stratus engineering document with verbatim 1985 TP-1 tuning results across three product lines. Provides the engineering ground truth for Stratus's pre-ET1 transaction-processing performance claims.*
**Prescience:** medium — *Stratus's 1985 internal TP1 design — PL/1 requester/server, parameterized loop counts to simulate workload, server-priority-above-requester tuning — anticipated the standardized TPC-A/B/C transaction benchmarks that emerged 1988-1992.*

## Entities (1)

- [[stratus-computer|Stratus Computer]]

## Technologies (6)

- [[fuji-disk-1985|Fuji Disk Drives (Stratus 1985)]]
- [[stratus-d108-disk|Stratus D108 Duplexed Disk]]
- [[stratus-ft200|Stratus FT200]]
- [[stratus-tp1-benchmark|Stratus TP-1 Internal Transaction Benchmark]]
- [[stratus-xa400|Stratus XA400]]
- [[stratus-xa600|Stratus XA600]]

## Key observations (top 25)

- **1985** — TP1 throughput: 5.0 tps; 2.1 sec avg / 3.3 sec 90th-percentile response; 80% CPU / 40% disk
- **1985** — TP1 throughput: 3.4 tps; 1.8 sec avg / 2.7 sec 90th-percentile; 80% CPU / 25% disk
- **1985** — TP1 throughput: 1.7 tps; 2.1 sec avg / 3.5 sec 90th-percentile; 85% CPU / 18% disk
- **1985** — Benchmark profile: 5 indexed reads + 2 indexed rewrites + 1 sequential log write per tx; 5000-cycle requester loop, 200-cycle server loop; 30s sleep +/- 5s; no screen I/O, no comms
- **1985** — Tuning observations: Task metering had no measurable effect; cache utilization significantly impacts performance; multiple server copies greatly improve performance

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-internal-benchmark-tuning-guide--c53e3f' ORDER BY year_observed;
```

