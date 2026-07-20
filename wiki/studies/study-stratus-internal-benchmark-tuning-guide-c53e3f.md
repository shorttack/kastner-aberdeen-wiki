---
title: "Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985)"
slug: "study-stratus-internal-benchmark-tuning-guide-c53e3f"
page_type: "study"
tags: ["type/study", "collection/internal-engineering-document"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "stratus-internal-benchmark-tuning-guide--c53e3f"
author: "Stratus Computer (internal engineering documentation)"
date: "1985"
pub_year: 1985
type: "internal-engineering-document"
subject_domain: "transaction-processing/benchmark-tuning"
methodology: "internal-engineering-tuning-guide"
source_file: "Stratus-1985-benchmark-tuning-guide-4.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "low"
prescience_3y_enum: "medium"
prescience_5y_enum: "medium"
prescience_max: 4.0
prescience_mean: 0.8
prescience_obs_count: 5
---

# Stratus Internal Benchmark Tuning Guide: TP-1 Results on XA600/XA400/FT200 (Stratus Internal Use Only, 1985)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** medium — 3y Rule A: mean=3.20 over 5 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].
- **5-year verdict:** medium — 5y Rule A: mean=3.00 over 5 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].

> Stratus Computer 1985 internal-use-only benchmark tuning guide documenting Stratus's internal TP-1 (transaction-processing) benchmark and the tuned performance results for three Stratus production systems: XA600 (5.0 tps with 2.1s avg / 3.3s 90th-percentile response, 80% CPU + 40% disk utilization, 3 duplexed D108 disks + 8 MB + 6 servers + 2 requesters with 80 tasks each); XA400 (3.4 tps, 1.8s avg / 2.7s 90th-percentile, 80% CPU + 25% disk, 8 MB + 3 Fuji disks + 4 servers + 2 requesters with 55 tasks); FT200 (1.7 tps, 2.1s avg / 3.5s 90th-percentile, 85% CPU + 18% disk, 8 MB + 2 Fuji disks + 1 requester with 55 tasks, server priority above requester). The guide describes TP1 as a PL/1 + COBOL requester/server simulation with parameterized indexed reads (5/tx), indexed rewrites (2/tx), sequential log writes (1/tx), 5,000-cycle requester CPU loop and 200-cycle server loop, 30-second sleep with +/-5s deviation, no screen I/O, no comms. Observations note task metering had no measurable effect, cache utilization significantly impacts performance, and multiple server copies improve performance. This document is the technical complement to the 1986 Stratus ET1 corpus (Batch 25 study #6+#7) — TP1 was the Stratus internal benchmark before ET1 became the industry standard.


_Published 1985, author **Stratus Computer (internal engineering documentation)**, type **internal-engineering-document**._


## Top observations

- Task metering had no measurable effect; cache utilization significantly impacts performance; multiple server copies greatly improve performance `[ps=4]`
- 5.0 tps; 2.1 sec avg / 3.3 sec 90th-percentile response; 80% CPU / 40% disk `[ps=0]`
- 3.4 tps; 1.8 sec avg / 2.7 sec 90th-percentile; 80% CPU / 25% disk `[ps=0]`
- 1.7 tps; 2.1 sec avg / 3.5 sec 90th-percentile; 85% CPU / 18% disk `[ps=0]`
- 5 indexed reads + 2 indexed rewrites + 1 sequential log write per tx; 5000-cycle requester loop, 200-cycle server loop; 30s sleep +/- 5s; no screen I/O, no comms `[ps=0]`
