---
title: "Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance"
slug: "study-aberdeen-1996-hp-enterprise-parallel-server-scalable-performance"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-hp-enterprise-parallel-server-scalable-performance"
author: "Aberdeen Group"
date: "1996-07-01"
pub_year: 1996
type: "market-study"
subject_domain: "high-end-Unix-servers-HPC"
methodology: "industry-analysis, competitive-profiling, benchmarking, field-research"
source_file: "1996 Hewlett-Packard_s Enterprise Parallel S...tion to Scalable, High-End Performance pr.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "low"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Hewlett-Packard's Enterprise Parallel Servers: A Graceful Transition to Scalable, High-End Performance

> This Aberdeen Group profile evaluates Hewlett-Packard's Enterprise Parallel Server (EPS) architecture, specifically the EPS21 and EPS30 introduced May 15, 1996. The study examines EPS's combination of SMP nodes connected via a fibre channel switch for high-end OLTP and data warehousing, compares it against IBM RS/6000 SP and other competitors, documents a TPC-C benchmark of 17,826 tpmC at $396/tpmC for the EPS30, and reports positive feedback from early adopters.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- HPP (Highly Parallel Processing): SMP nodes connected via fibre channel switch; evolutionary extension of SMP/clustering; gradual upgrade path for existing K/T-Class systems
- 17,826 tpmC at $396/tpmC (48 processors, T-Class SMP nodes, Oracle 7.3); second highest published result as of July 1996
- 16 ports; 266 Mbit/s per port; 532 Mbit/s full duplex; hub architecture; nodes up to 2 km from switch; target: 32 ports at 1 Gbit/s by 3Q97
- H2 1998: support for 768 processors (64 SMP nodes x 12 processors); interconnect target 10 km by 3Q97
- Highest TPC-C performance ratings on record as of July 1996
- Best TPC-D price/performance on record as of July 1996
- Highest absolute TPC-D performance rating on record as of July 1996
- Aberdeen predicts EPS will become datacenter system-of-choice for very large application requirements as HP builds aggressive EPS sales/marketing campaign
- HP EPS/PA-RISC platform did not become dominant datacenter standard; HP shifted to Itanium (Integrity servers) around 2001-2002; x86/Linux ultimately dominated high-end commercial computing; HP-UX market share declined steadily
- Aberdeen predicts HP Tachyon fibre channel adapter has very high probability of becoming an open-systems industry standard; 50+ storage suppliers adopting it
- Fibre Channel became an industry standard for storage connectivity (FC-AL, FCAL SAN), though standardization occurred through ANSI/IEEE rather than Tachyon-specifically; HP Tachyon was a key enabler of FC storage area network adoption in late 1990s
- Aberdeen anticipates significant performance increase in 3Q96 as next-gen HP 9000 64-bit PA-8000 SMP nodes become available
- HP PA-8000 processor introduced as planned; HP EPS with PA-8000 nodes improved TPC-C results significantly in 1997; prediction proved accurate
- Single-processor nodes; PSSP/HACMP split management environment; geographically constrained to one site; IBM execs described SP as 'not-yet-ready-for-production' at conferences
- Aberdeen: most IS decision makers interviewed do not know EPS exists; HP needs more aggressive sales/marketing campaign urgently
- EPS customers exceeded expectations for 'headroom' problems; smooth migration from HP SMP/cluster; workload balancing described as 'a real joy'; investment protection major business benefit
- EPS inherent hardware redundancy + HP MC/ServiceGuard: users can achieve same or higher availability than state-of-art clustering while maintaining high performance
- Each K-Class or T-Class SMP node: multi-processor, high-performance compute unit; T-Class supports up to 14-way SMP
- Hub architecture allows direct node-to-node messaging without intermediate hops; key differentiator from pure MPP interconnects
- MC/System Environment tools: single-system view, single-point management, systems admin, config, performance monitoring, load balancing bundled with EPS clusters
