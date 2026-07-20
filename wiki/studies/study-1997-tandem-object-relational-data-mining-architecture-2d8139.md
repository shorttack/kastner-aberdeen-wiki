---
title: "Tandem Object Relational Data Mining Architecture: Making The Data Mining Promise A Reality"
slug: "study-1997-tandem-object-relational-data-mining-architecture-2d8139"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "1997-tandem-object-relational-data-mining-architecture-2d8139"
author: "Aberdeen Group"
date: "1997-02-11"
pub_year: 1997
type: "white-paper"
subject_domain: "data-mining-architecture"
methodology: "industry-analysis, competitive-profiling, expert-opinion, field-research"
source_file: "1997 Tandem Object Relational Data Mining Architecture pr.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 2.86
prescience_obs_count: 21
---

# Tandem Object Relational Data Mining Architecture: Making The Data Mining Promise A Reality


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.67 over 21 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.81 over 21 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Group profiles Tandem Computers' Object Relational Data Mining architecture, which integrates data mining algorithms directly into the RDBMS to eliminate the need for separate flat-file extracts. The study evaluates Tandem's partnerships with five data mining vendors (Angoss, Data Distilleries, Magnify, NeoVista, Syllogic) and its Directional Consulting services, concluding that the architecture offers an enterprise-grade end-to-end solution particularly suited to large datasets in finance, retail, insurance, and telecommunications. Aberdeen assesses the initiative as potentially establishing a de facto standard SQL interface between data mining tools and relational databases.


_Published 1997, author **Aberdeen Group**, type **white-paper**._


## Top observations

- Determine what data will likely return best results — precedes algorithm execution `[ps=5]`
- Coding the data — formatting data to work best with selected algorithm `[ps=5]`
- Compaq acquired Tandem in 1997; ORDM architecture was deprioritized; de facto standard SQL data mining interface goal not achieved; Oracle/Microsoft/Informix did not adopt the standard `[ps=5]`
- ServerWare discontinued after Compaq acquisition; NT-based product line did not survive consolidation `[ps=5]`
- Tandem Computers acquired by Compaq for approximately $3B in 1997; became NonStop server division `[ps=5]`
- Data-manipulation functions integrated into RDBMS; enterprise executes against data directly in warehouse; no flat-file extract required `[ps=4]`
- Data scrubbing — removing data and field inconsistencies `[ps=4]`
- Algorithm execution and results review; re-tuning model and re-running algorithm iteratively `[ps=4]`
- Three initial solutions packages: credit card marketing; micromerchandising (market basket analysis); claims analysis `[ps=4]`
- In-database analytics became dominant approach in modern MPP systems (Teradata, Greenplum, Vertica, Snowflake, BigQuery); Tandem's architectural vision proven correct `[ps=4]`
- Directional Consulting designs and builds data mining environment within 90 days; charter is knowledge transfer not prolonged engagement; leaves software toolbox `[ps=3]`
- Parallel-scalable architecture; 5 integrated data mining partner algorithms; solutions packages with vertical templates; consulting services — end-to-end capability `[ps=3]`
- Create de facto standard SQL interface between data mining tools and RDBMS using SQL extensions `[ps=2]`
- Scales from SMP to MPP as data mining demands grow; runs on ServerWare/NT or Himalaya servers `[ps=2]`
- ORDM increases overall reliability of supplier code; saves data mining suppliers from writing redundant code; encourages more value-added development `[ps=2]`
- ORDM on ServerWare/NT will enable cost-sensitive scale from Windows NT to Himalaya in cost-sensitive increments `[ps=2]`
- Tandem's ORDM architecture will become an end-to-end enterprise weapon for competitive advantage; Aberdeen believes enterprises can look to it as the standard solution `[ps=1]`
- Five data mining partners integrated into ORDM: Angoss (KnowledgeSEEKER); Data Distilleries (Data Surveyor); Magnify (PATTERN:Detect/Profit); NeoVista (Decision Series); Syllogic (DM Tool/MP) `[ps=0]`
- Object Relational Data Mining architecture available Q3 1997 on ServerWare/NT and Himalaya; credit card/micromerchandising/claims packages available without SQL extensions immediately `[ps=0]`
- 98.8% scalability across 112 CPUs in TPC-C benchmark — cited from Aberdeen 1994 Product Viewpoint on Himalaya K10000 `[ps=0]`
- $360M+ annual software sales cited; key accounts in finance/insurance/retail/telecoms `[ps=0]`
