---
title: "Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos"
slug: "study-kastner-tandem-topgun-et1-analysis-1987-a3a09c"
page_type: "study"
tags: ["type/study", "collection/internal-engineering-memo"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "kastner-tandem-topgun-et1-analysis-1987--a3a09c"
author: "Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988)"
date: "1987-08-11/1988-01-13"
pub_year: 1987
type: "internal-engineering-memo"
subject_domain: "fault-tolerant-OLTP-benchmarks"
methodology: "Primary-source PSK-authored technical memos analyzing Tandem 32-VLX TopGun benchmark (208 tps) — first as Stratus marketing-support manager (Aug 1987 working document), then as DEC Corporate Systems Group (Jan 1988) re-applying the analysis to a Digital response."
source_file: "Tandem-TopGun-ET1-1987-08-PSK-DECtp.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_3y_enum: "medium"
prescience_5y_enum: "medium"
prescience_max: 2.0
prescience_mean: 0.12
prescience_obs_count: 8
---

# Tandem TopGun ET1 Benchmark Analysis — Kastner-authored Stratus + DEC memos


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** medium — 3y Rule A: mean=3.40 over 10 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].
- **5-year verdict:** medium — 5y Rule A: mean=3.30 over 10 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].

> Two PSK-authored memos covering the same Tandem TopGun ET1 benchmark across employer transitions: the August 1987 Stratus 'Working Document on the NonStop SQL Benchmark' (co-authored with Raphael Frommer and Clark Hodder, addressed to Bill Foster, Bob Freiburghouse and the Stratus engineering leadership) dissecting Tandem's 32-VLX 208-tps TopGun result; and the January 1988 DEC Corporate Systems Group memo applying the same analysis to plot Digital's response. PSK enumerates Tandem's 'go-fast tricks' (Pathway hacks, TMF buffering, file partitioning so all branch records sit on one ATB disk, mirrored disks worth ~5%, intelligent X.25 cluster controllers, relaxed 90%/2-sec response criterion vs the original 95%/1-sec, randomized arrival times) and concludes Tandem's 8-VLX baseline would deliver ~10-15 tps under conservative ET1 conditions — meaning Stratus and Digital are 'not nearly as bad as corporate mythology would have us believe.' The memo is a rare document of PSK actively analyzing competitive benchmarks across two employers in five months.


_Published 1987, author **Peter S. Kastner (with Raphael Frommer, Clark Hodder, Stratus, Aug 1987); Peter S. Kastner (DEC Corporate Systems Group, 13 January 1988)**, type **internal-engineering-memo**._


## Top observations

- Devising our own, new OLTP benchmark standard `[ps=2]`
- 208 `[ps=0]`
- 58 `[ps=0]`
- 10-15 `[ps=0]`
- 5 `[ps=0]`
- 6 options: do similar test; ignore; raise stakes; deemphasize ET-1; devise own standard; embrace RAMP-C `[ps=0]`
- Stratus Aug 1987 -> DEC Corporate Systems Group Jan 1988 `[ps=0]`
- Tandem is not as awesomely good as first appears. And Digital is not nearly as bad as corporate mythology would have us believe `[ps=-1]`
- 0.4 audit msgs/tx; 0.5 checkpoints/tx
- 8% (16-cpu); 10% (32-cpu)
