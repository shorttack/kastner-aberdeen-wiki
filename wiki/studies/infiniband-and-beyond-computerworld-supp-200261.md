---
title: "To InfiniBand and beyond, cry firms"
slug: infiniband-and-beyond-computerworld-supp-200261
page_type: study
author: "Carly Suppa"
date: "2002-08-13"
study_type: news-article
subject_domain: "data-center-interconnect-InfiniBand-2002"
methodology: "news-reporting, analyst-quote-aggregation"
importance: high
importance_rationale: "Captures peak-industry-optimism moment for InfiniBand when Aberdeen and the IBTA framed it as the successor to TCP/IP for server interconnect — a prediction that partially came true in HPC and now AI-training clusters."
relevance: high
relevance_rationale: "InfiniBand is the dominant fabric for GPU training clusters (NVIDIA Mellanox) and top-500 supercomputers in 2024-2026. Kastner's server-interconnect prediction substantively validated — though not via mass enterprise displacement of TCP/IP."
prescience: high
prescience_rationale: "Kastner's 'InfiniBand will replace TCP/IP as the high-speed server-to-server interconnect' and low-latency/blade-cluster framing accurately described the HPC and AI-cluster reality that emerged 15-20 years later. NVIDIA's 2019 Mellanox acquisition and the 2023-2026 AI-training boom made InfiniBand/NVLink central to the largest compute fabrics — precisely the multi-tiered, low-latency use case Kastner identified."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 7
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# To InfiniBand and beyond, cry firms

> Computerworld Australia feature on InfiniBand, a next-generation data-center interconnect operating at 2.5-10 Gbps (scaling to 30 Gbps) backed by 150+ firms in the InfiniBand Trade Association including IBM, Intel, Microsoft, Sun, and Dell. Draws on Aberdeen Group's 'InfiniBand Architecture: Planning the Next Generation Data Centre' white paper. Kastner (Aberdeen EVP/CRO) predicts InfiniBand 'will replace TCP/IP as the high-speed, server-to-server interconnect technology' with ISPs, ASPs and large web sites as initial targets.

**Author:** Carly Suppa · **Date:** 2002-08-13 · **Type:** news-article
**Importance:** high — *Captures peak-industry-optimism moment for InfiniBand when Aberdeen and the IBTA framed it as the successor to TCP/IP for server interconnect — a prediction that partially came true in HPC and now AI-training clusters.*
**Prescience:** high — *Kastner's 'InfiniBand will replace TCP/IP as the high-speed server-to-server interconnect' and low-latency/blade-cluster framing accurately described the HPC and AI-cluster reality that emerged 15-20 years later. NVIDIA's 2019 Mellanox acquisition and the 2023-2026 AI-training boom made InfiniBand/N…*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[carly-suppa-cw-au|Carly Suppa]]
- [[computerworld-australia|Computerworld Australia (IDG)]]
- [[dell|Dell Computer Corporation]]
- [[don-kerr-dell-canada|Don Kerr]]
- [[ibm-corp|IBM Corporation]]
- [[infiniband-trade-association|InfiniBand Trade Association (IBTA)]]
- [[intel-corp|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (7)

- [[blade-server|Blade server form factor]]
- [[ethernet|Ethernet (including 1/10 Gigabit)]]
- [[fibre-channel|Fibre Channel]]
- [[infiniband|InfiniBand architecture]]
- [[iscsi|iSCSI]]
- [[server-cluster|Server cluster (multi-node)]]
- [[tcp-ip|TCP/IP protocol stack]]

## Key observations (top 25)

- **2002** — InfiniBand speed range at time of article: 2.5 Gbps to 10 Gbps today; expected to reach up to 30 Gbps as it evolves
- **2002** — IBTA member count: More than 150 companies worldwide
- **2002** — Kastner TCP/IP-displacement prediction: 'In many instances, [InfiniBand] will replace TCP/IP as the high-speed, server-to-server interconnect technology.' — Kastner
- **2002** — Kastner on InfiniBand technical advantages: 'InfiniBand works at very high speeds with very low latency and is a very efficient and transparent protocol.' Plus: parallel connections with low CPU use, enabling huge I/O bandwidth; low-latency blade-to-blade messaging for clustering.
- **2002** — Initial-target-market prediction: ISPs, application service providers, and large web sites with multi-tiered architecture will be initial targets for InfiniBand's functionality
- **2002-2026** — Did InfiniBand displace TCP/IP in server interconnect: Mixed — did NOT broadly displace TCP/IP in enterprise server-to-server. Substantively validated in HPC (top-500 supercomputers majority-InfiniBand by 2010s) and AI-training clusters (NVIDIA acquired Mellanox 2019 for $6.9B; InfiniBand HDR/NDR the dom…
- **2002** — Aberdeen InfiniBand white paper: 'InfiniBand Architecture: Planning the Next Generation Data Centre' — published 2002
- **2002** — Dell Canada on InfiniBand importance: Kerr: InfiniBand one of the most exciting technologies Dell has seen; absolutely critical in enabling Dell to deliver more scalable systems with standardized interfaces

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'infiniband-and-beyond-computerworld-supp-200261' ORDER BY year_observed;
```

