---
title: "Time Compression - Downtime Strategy: Formulas and Business Case"
slug: "study-13-hh-time-compression-downtime-strategy-4e50c9"
page_type: "study"
tags: ["type/study", "collection/case-analysis"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "13-hh-time-compression-downtime-strategy-4e50c9"
author: "David Hill (HH), Aberdeen Group"
date: "2003-01-01"
pub_year: 2003
type: "case-analysis"
subject_domain: "enterprise-storage"
methodology: "financial-modeling, tco-analysis, benchmark"
source_file: "13-HH-Time-Compression-Downtime-Strategy.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: 4.0
prescience_mean: 0.5
prescience_obs_count: 14
---

# Time Compression - Downtime Strategy: Formulas and Business Case

> Working document containing financial formulas and a detailed business case for demonstrating TCO savings from migrating from traditional tape-based nearline storage to a midline disk plus tape combination. Models downtime reduction for a large financial services company with 1 million customers by quantifying backup time savings and customer revenue impact. Provides specific dollar-per-GB pricing for online (HDS 9980V at $31.60/GB) midline ($9.30/GB) and nearline disk/tape systems.


_Published 2003, author **David Hill (HH), Aberdeen Group**, type **case-analysis**._


## Top observations

- Savings 1 (initial cost savings) + Savings 2 (backup time compression savings); includes opportunity cost savings at 0.6 multiplier `[ps=4]`
- CostO = cost(E GB online disk) + cost(G GB nearline tape) + cost(H GB offline tape) `[ps=3]`
- CostN = cost(E/2 online disk) + cost(E/2 midline disk) + cost(G/2 nearline disk) + cost(G/2 nearline tape) + cost(H offline tape); assumes online disk split in half and nearline tape split in half `[ps=0]`
- X = 800 GB/hr `[ps=0]`
- Y = 1600 GB/hr `[ps=0]`
- Medium/large financial services company; 1 million customers; 100K overseas business customers; 120 customers served/hour; $100/customer `[ps=0]`
- E = 3 TB critical data requiring backup `[ps=0]`
- 20TB nearline disk: $100K at $5/GB; 4-drive 100-slot tape library: $85K + $10K media = $95K; 40TB tape capacity at $2.50/GB; total combo: $195K `[ps=0]`
- $31.60/GB (HDS 9980V with 146GB disks) `[ps=0]`
- $13.30/GB (EMC CX600 with 146GB disks) `[ps=0]`
- $9.30/GB (70% of EMC midrange price) `[ps=0]`
- $10/hour ($100K salary * 1/10000 hours per year) `[ps=0]`
- Savings 2 = (customers served/hour * $/customer * backup time saved) + ($10 * backup time saved in hours) `[ps=0]`
- [UNVERIFIED] `[ps=0]`
- Opportunity cost savings = 0.6 * direct cost savings from New solution
- Old Way: A = M/X hours; New Way: B = M/(2X) hours (parallel backup); backup time saved = A - B = M/(2X)
- $130K for 8-drive 200-slot system; LTO-2 (400MB/cartridge at 40MB/sec 2:1 compression); $20K media (100/cartridge); total $150K; 80TB capacity; $1.90/GB
- Midline disk at 70% of midrange ($9.30/GB vs $13.30/GB) will enable measurable TCO savings in New Way architecture
