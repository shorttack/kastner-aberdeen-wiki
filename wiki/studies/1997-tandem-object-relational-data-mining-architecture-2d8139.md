---
title: "Tandem Object Relational Data Mining Architecture: Making The Data Mining Promise A Reality"
slug: 1997-tandem-object-relational-data-mining-architecture-2d8139
page_type: study
author: "Aberdeen Group"
date: "1997-02-11"
study_type: white-paper
subject_domain: "data-mining-architecture"
methodology: "industry-analysis, competitive-profiling, expert-opinion, field-research"
importance: high
importance_rationale: "One of the earliest independent assessments of in-database analytics architecture; Tandem's push-down SQL approach to data mining anticipated by two decades what became standard practice in Hadoop and modern analytical databases. Published at the inflection point between data warehousing and data mining convergence."
relevance: high
relevance_rationale: "The core architectural concepts — in-database analytics, parallel query execution, SQL-based data mining interfaces, and iterative model refinement against full datasets — are central to modern data science platforms including Spark SQL, Snowflake, BigQuery, and virtually every MPP database. The framework and pain points documented remain directly applicable."
prescience: medium
prescience_rationale: "Aberdeen correctly predicted data mining would move from specialist tool to mainstream enterprise process and that architecture integrating algorithms with the database would win. The specific Tandem architecture failed when Compaq acquired Tandem in 1997 and deprioritized it, but the architectural vision proved prescient."
license: CC-BY-4.0
tier: 1
entity_count: 13
tech_count: 9
obs_count: 21
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Tandem Object Relational Data Mining Architecture: Making The Data Mining Promise A Reality

> Aberdeen Group profiles Tandem Computers' Object Relational Data Mining architecture, which integrates data mining algorithms directly into the RDBMS to eliminate the need for separate flat-file extracts. The study evaluates Tandem's partnerships with five data mining vendors (Angoss, Data Distilleries, Magnify, NeoVista, Syllogic) and its Directional Consulting services, concluding that the architecture offers an enterprise-grade end-to-end solution particularly suited to large datasets in finance, retail, insurance, and telecommunications. Aberdeen assesses the initiative as potentially establishing a de facto standard SQL interface between data mining tools and relational databases.

**Author:** Aberdeen Group · **Date:** 1997-02-11 · **Type:** white-paper
**Importance:** high — *One of the earliest independent assessments of in-database analytics architecture; Tandem's push-down SQL approach to data mining anticipated by two decades what became standard practice in Hadoop and modern analytical databases. Published at the inflection point between data warehousing and data mi…*
**Prescience:** medium — *Aberdeen correctly predicted data mining would move from specialist tool to mainstream enterprise process and that architecture integrating algorithms with the database would win. The specific Tandem architecture failed when Compaq acquired Tandem in 1997 and deprioritized it, but the architectural…*

## Entities (13)

- [[aberdeen-group|Aberdeen Group]]
- [[angoss-software|Angoss Software]]
- [[compaq|Compaq Computer]]
- [[data-distilleries|Data Distilleries]]
- [[hewlett-packard-enterprise|Hewlett Packard Enterprise]]
- [[informix|Informix Corporation]]
- [[magnify|Magnify Inc.]]
- [[microsoft|Microsoft Corporation]]
- [[mrj-technology-solutions|MRJ Technology Solutions]]
- [[neovista-solutions|NeoVista Solutions]]
- [[oracle|Oracle Corporation]]
- [[syllogic|Syllogic]]
- [[tandem-computers|Tandem Computers Incorporated]]

## Technologies (9)

- [[informix-illustra-datablade|Informix/Illustra DataBlade]]
- [[knowledgeseeker|Angoss KnowledgeSEEKER]]
- [[mpp|Massively Parallel Processing (MPP)]]
- [[smp|Symmetric Multiprocessing (SMP)]]
- [[tandem-himalaya|Tandem Himalaya]]
- [[tandem-nonstop-sql|Tandem NonStop SQL]]
- [[tandem-ordm-architecture|Tandem Object Relational Data Mining Architecture]]
- [[tandem-serverware|Tandem ServerWare]]
- [[windows-nt|Microsoft Windows NT Server]]

## Key observations (top 25)

- **1997** — ORDM architecture strategic goal: Create de facto standard SQL interface between data mining tools and RDBMS using SQL extensions
- **1997** — Partnership strategy: Five data mining partners integrated into ORDM: Angoss (KnowledgeSEEKER); Data Distilleries (Data Surveyor); Magnify (PATTERN:Detect/Profit); NeoVista (Decision Series); Syllogic (DM Tool/MP)
- **1997** — Core architectural innovation: Data-manipulation functions integrated into RDBMS; enterprise executes against data directly in warehouse; no flat-file extract required
- **1997** — Scalability architecture: Scales from SMP to MPP as data mining demands grow; runs on ServerWare/NT or Himalaya servers
- **1997** — Data mining life-cycle phase 1: Determine what data will likely return best results — precedes algorithm execution
- **1997** — Data mining life-cycle phase 2: Data scrubbing — removing data and field inconsistencies
- **1997** — Data mining life-cycle phase 3: Coding the data — formatting data to work best with selected algorithm
- **1997** — Data mining life-cycle phase 4: Algorithm execution and results review; re-tuning model and re-running algorithm iteratively
- **1997** — Target vertical markets: Three initial solutions packages: credit card marketing; micromerchandising (market basket analysis); claims analysis
- **1997** — ORDM availability date: Object Relational Data Mining architecture available Q3 1997 on ServerWare/NT and Himalaya; credit card/micromerchandising/claims packages available without SQL extensions immediately
- **1997** — ORDM as enterprise data mining standard: Tandem's ORDM architecture will become an end-to-end enterprise weapon for competitive advantage; Aberdeen believes enterprises can look to it as the standard solution
- **1998** — ORDM architecture fate post-acquisition: Compaq acquired Tandem in 1997; ORDM architecture was deprioritized; de facto standard SQL data mining interface goal not achieved; Oracle/Microsoft/Informix did not adopt the standard
- **2010** — In-database analytics vindication: In-database analytics became dominant approach in modern MPP systems (Teradata, Greenplum, Vertica, Snowflake, BigQuery); Tandem's architectural vision proven correct
- **1997** — Consulting model — knowledge transfer charter: Directional Consulting designs and builds data mining environment within 90 days; charter is knowledge transfer not prolonged engagement; leaves software toolbox
- **1994** — Tandem TPC-C scalability benchmark: 98.8% scalability across 112 CPUs in TPC-C benchmark — cited from Aberdeen 1994 Product Viewpoint on Himalaya K10000
- **1997** — Tandem competitive advantage factors: Parallel-scalable architecture; 5 integrated data mining partner algorithms; solutions packages with vertical templates; consulting services — end-to-end capability
- **1997** — Tandem annual software revenue: $360M+ annual software sales cited; key accounts in finance/insurance/retail/telecoms
- **1997** — Aberdeen assessment of ORDM value proposition: ORDM increases overall reliability of supplier code; saves data mining suppliers from writing redundant code; encourages more value-added development
- **1997** — ServerWare/NT platform viability: ORDM on ServerWare/NT will enable cost-sensitive scale from Windows NT to Himalaya in cost-sensitive increments
- **1999** — ServerWare fate: ServerWare discontinued after Compaq acquisition; NT-based product line did not survive consolidation
- **1997** — Tandem Computers acquisition: Tandem Computers acquired by Compaq for approximately $3B in 1997; became NonStop server division

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-tandem-object-relational-data-mining-architecture-2d8139' ORDER BY year_observed;
```

