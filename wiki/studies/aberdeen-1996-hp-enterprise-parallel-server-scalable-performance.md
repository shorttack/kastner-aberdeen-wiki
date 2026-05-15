---
title: "Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance"
slug: aberdeen-1996-hp-enterprise-parallel-server-scalable-performance
page_type: study
author: "Aberdeen Group"
date: "1996-07-01"
study_type: market-study
subject_domain: "high-end-Unix-servers-HPC"
methodology: "industry-analysis, competitive-profiling, benchmarking, field-research"
importance: high
importance_rationale: "First detailed independent assessment of HP's EPS architecture at launch, documenting its TPC-C benchmark results and positioning against IBM RS/6000 SP at a decisive moment in Unix datacenter competition; directly informed enterprise procurement decisions."
relevance: low
relevance_rationale: "HP's EPS platform and PA-RISC architecture are long discontinued; HP-UX servers have declined significantly since the rise of x86/Linux; methodology for evaluating parallel server architectures retains some value for historical comparison."
prescience: medium
prescience_rationale: "Aberdeen correctly predicted HP's PA-8000 upgrade would improve performance and that fibre channel would become an industry standard (Tachyon). The prediction that EPS would become a 'datacenter system of choice' was overstated; HP servers lost significant ground to x86/Linux in subsequent years."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 8
obs_count: 20
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance

> This Aberdeen Group profile evaluates Hewlett-Packard's Enterprise Parallel Server (EPS) architecture, specifically the EPS21 and EPS30 introduced May 15, 1996. The study examines EPS's combination of SMP nodes connected via a fibre channel switch for high-end OLTP and data warehousing, compares it against IBM RS/6000 SP and other competitors, documents a TPC-C benchmark of 17,826 tpmC at $396/tpmC for the EPS30, and reports positive feedback from early adopters.

**Author:** Aberdeen Group · **Date:** 1996-07-01 · **Type:** market-study
**Importance:** high — *First detailed independent assessment of HP's EPS architecture at launch, documenting its TPC-C benchmark results and positioning against IBM RS/6000 SP at a decisive moment in Unix datacenter competition; directly informed enterprise procurement decisions.*
**Prescience:** medium — *Aberdeen correctly predicted HP's PA-8000 upgrade would improve performance and that fibre channel would become an industry standard (Tachyon). The prediction that EPS would become a 'datacenter system of choice' was overstated; HP servers lost significant ground to x86/Linux in subsequent years.*

## Entities (10)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[digital-equipment|Digital Equipment Corporation (DEC)]]
- [[emc-corporation|EMC Corporation]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[ibm|IBM]]
- [[informix|Informix Software]]
- [[ncr-corporation|NCR Corporation]]
- [[oracle|Oracle Corporation]]
- [[sap|SAP AG]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (8)

- [[hp-enterprise-switch|HP Enterprise Switch (Fibre Channel)]]
- [[hp-eps|HP Enterprise Parallel Server (EPS)]]
- [[hp-pa8000|HP PA-8000 RISC Processor]]
- [[hp-ux|HP-UX]]
- [[ibm-rs6000-sp|IBM RS/6000 SP]]
- [[oracle-parallel-server|Oracle Parallel Server]]
- [[tachyon-fc|HP Tachyon Fibre Channel Adapter]]
- [[tpc-c-benchmark|TPC-C Benchmark]]

## Key observations (top 25)

- **1996** — EPS Architecture Strategy: HPP (Highly Parallel Processing): SMP nodes connected via fibre channel switch; evolutionary extension of SMP/clustering; gradual upgrade path for existing K/T-Class systems
- **1996** — TPC-C OLTP Benchmark (EPS30): 17,826 tpmC at $396/tpmC (48 processors, T-Class SMP nodes, Oracle 7.3); second highest published result as of July 1996
- **1996** — HP Enterprise Switch Specifications: 16 ports; 266 Mbit/s per port; 532 Mbit/s full duplex; hub architecture; nodes up to 2 km from switch; target: 32 ports at 1 Gbit/s by 3Q97
- **1996** — EPS Scalability Roadmap: H2 1998: support for 768 processors (64 SMP nodes x 12 processors); interconnect target 10 km by 3Q97
- **1996** — DEC TruCluster TPC-C Performance: Highest TPC-C performance ratings on record as of July 1996
- **1996** — Sun Ultra Enterprise 6000 TPC-D Performance: Best TPC-D price/performance on record as of July 1996
- **1996** — NCR 5100M TPC-D Performance: Highest absolute TPC-D performance rating on record as of July 1996
- **1996** — EPS Datacenter Standard Prediction: Aberdeen predicts EPS will become datacenter system-of-choice for very large application requirements as HP builds aggressive EPS sales/marketing campaign
- **2002** — EPS Datacenter Actual Outcome: HP EPS/PA-RISC platform did not become dominant datacenter standard; HP shifted to Itanium (Integrity servers) around 2001-2002; x86/Linux ultimately dominated high-end commercial computing; HP-UX market share declined steadily
- **1996** — Tachyon FC Standard Prediction: Aberdeen predicts HP Tachyon fibre channel adapter has very high probability of becoming an open-systems industry standard; 50+ storage suppliers adopting it
- **2000** — Tachyon FC Standard Actual Outcome: Fibre Channel became an industry standard for storage connectivity (FC-AL, FCAL SAN), though standardization occurred through ANSI/IEEE rather than Tachyon-specifically; HP Tachyon was a key enabler of FC storage area network adoption in late 1990s
- **1996** — PA-8000 Performance Improvement Prediction: Aberdeen anticipates significant performance increase in 3Q96 as next-gen HP 9000 64-bit PA-8000 SMP nodes become available
- **1997** — PA-8000 Performance Improvement Actual Outcome: HP PA-8000 processor introduced as planned; HP EPS with PA-8000 nodes improved TPC-C results significantly in 1997; prediction proved accurate
- **1996** — IBM RS/6000 SP Limitations vs HP EPS: Single-processor nodes; PSSP/HACMP split management environment; geographically constrained to one site; IBM execs described SP as 'not-yet-ready-for-production' at conferences
- **1996** — IS Decision-Maker Awareness Gap: Aberdeen: most IS decision makers interviewed do not know EPS exists; HP needs more aggressive sales/marketing campaign urgently
- **1996** — Early User Satisfaction: EPS customers exceeded expectations for 'headroom' problems; smooth migration from HP SMP/cluster; workload balancing described as 'a real joy'; investment protection major business benefit
- **1996** — High Availability + High Performance Capability: EPS inherent hardware redundancy + HP MC/ServiceGuard: users can achieve same or higher availability than state-of-art clustering while maintaining high performance
- **1996** — HPP Architecture Factor: SMP Node: Each K-Class or T-Class SMP node: multi-processor, high-performance compute unit; T-Class supports up to 14-way SMP
- **1996** — HPP Architecture Factor: Fibre Channel Switch: Hub architecture allows direct node-to-node messaging without intermediate hops; key differentiator from pure MPP interconnects
- **1996** — HPP Architecture Factor: MCSE Management: MC/System Environment tools: single-system view, single-point management, systems admin, config, performance monitoring, load balancing bundled with EPS clusters

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-hp-enterprise-parallel-server-scalable-performance' ORDER BY year_observed;
```

