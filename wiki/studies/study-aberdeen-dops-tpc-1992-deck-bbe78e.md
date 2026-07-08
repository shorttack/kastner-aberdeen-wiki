---
title: "Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck)"
slug: "study-aberdeen-dops-tpc-1992-deck-bbe78e"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "aberdeen-dops-tpc-1992-deck-bbe78e"
author: "Peter S. Kastner (Aberdeen Group)"
date: "1992-02-01"
pub_year: 1992
type: "market-study"
subject_domain: "transaction-processing-benchmarks-distributed-computing"
methodology: "benchmark-analysis, market-tracking, competitive-profiling"
source_file: "1992-DOPS-TPC-3.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 4.0
prescience_mean: 0.73
prescience_obs_count: 11
---

# Aberdeen Group — DOPS and TPC-A/TPC-B benchmark results (1992 deck)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.71 over 17 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.65 over 17 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Group slide deck from February 1992 (dated '2/92' in footer) presenting TPC-A and TPC-B benchmark results and introducing Aberdeen's DOPS (Distributed Online Processing Systems) framework. Highlights an 85% price decline for equivalent transaction-processing capacity from the DEC VAX 8830 (1988 best-performance, $1,800K 5-year cost for 27 tps) to the VAX 3100-80 (1992 entry-level, $280K). Compares TPC-A at 40 tps-A across Bull DPX/2, DEC VAX 4000-300, HP 9000 957LX, IBM AS/400 D70, and IBM RS/6000 530H (costs $450K-$920K). TPC-B results at 39.7-46 tps-B across Compaq 486/50L, DECsystem 5500, HP 9000 807S, Data General AViiON 4600, MIPS 3330, RS/6000 320H, and Sun SPARC Server 2 (cluster ~$100K). Introduces the DOPS environment (multiple databases, networks, hetero-geneous hardware, mixed OLTP/OLDS) with performance issues including 'Production/Snapshot/Test/Runamuck' database categories.


_Published 1992, author **Peter S. Kastner (Aberdeen Group)**, type **market-study**._


## Top observations

- VAX 8830 (1988 best) $1,800K vs VAX 3100-80 (1992 entry) $280K — 85% decline in 3.5 years for 27 tps with relational database (TPC-A-like) `[ps=4]`
- Distributed heterogeneous environments require new multi-dimensional metrics beyond single-system TPC benchmarks `[ps=4]`
- IBM AS/400 D70 ~$920K 5-year cost for 40 tps-A — highest in the set `[ps=0]`
- IBM RS/6000 530H ~$620K 5-year cost for 40 tps-A `[ps=0]`
- HP 9000 957LX ~$680K 5-year cost (49 tps, starred) `[ps=0]`
- DEC VAX 4000-300 ~$620K 5-year cost for 40 tps-A `[ps=0]`
- DECsystem 5500: ~$160K — outlier high-cost `[ps=0]`
- Data General AViiON 4600: ~$102K at 39.7-46 tps-B `[ps=0]`
- MIPS 3330: ~$110K at 39.7-46 tps-B `[ps=0]`
- IBM RS/6000 320H: ~$107K at 39.7-46 tps-B `[ps=0]`
- Sun SPARC Server 2: ~$102K at 39.7-46 tps-B `[ps=0]`
- End-to-End Response Time; Multiple Databases; Multiple Networks; Heterogeneous Hardware; Mixed OLTP & OLDS
- Bull DPX/2 at ~$450K 5-year lifecycle cost — lowest in comparison
- Compaq 486/50L: ~$110K 5-year cost at 39.7-46 tps-B
- HP 9000 807S: ~$105K at 39.7-46 tps-B
- Transactions vs Queries; Production/Snapshot/Test/Runamuck DBs; What does the client do? What does the front end do? No textbook answers
- DOPS must handle mixed OLTP and Online Decision Support workloads — precursor to HTAP (Hybrid Transactional/Analytical Processing)
