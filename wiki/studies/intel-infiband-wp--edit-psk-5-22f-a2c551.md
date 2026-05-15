---
title: "InfiniBand Architecture: Planning the Next-Generation Data Center"
slug: intel-infiband-wp--edit-psk-5-22f-a2c551
page_type: study
author: "Peter S. Kastner"
date: "2002-05"
study_type: white-paper
subject_domain: "Enterprise IT Hardware / Networking / Data Center Architecture"
methodology: "expert-analysis; early-adopter field research"
importance: high
importance_rationale: "Foundational Aberdeen analysis of InfiniBand at the time of its emergence; combines architecture overview with enterprise planning guidance and early-adopter evidence."
relevance: high
relevance_rationale: "InfiniBand became the dominant HPC/data center fabric; this white paper captures the architectural rationale and transition planning logic at the critical early stage."
prescience: high
prescience_rationale: "Correctly predicted IBA adoption in HPC and large enterprise; blade server adoption with IBA; TCP offload engine uses; though IBA did not fully replace PCI-X in broad enterprise as envisioned — HPC became the primary domain."
license: CC-BY-4.0
tier: 1
entity_count: 20
tech_count: 16
obs_count: 22
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# InfiniBand Architecture: Planning the Next-Generation Data Center

> Aberdeen Executive White Paper providing a comprehensive overview of the emerging InfiniBand Architecture (IBA) for data center IT planners. Covers IBA components (HCA, TCA, switches/routers), comparison to PCI/PCI-X, IP over InfiniBand, storage over InfiniBand (SCSI, SAN, NAS), server scaling via clustering and blade servers, deployment transition planning, and early-adopter field research indicating 50% TCO reduction for database clusters. Recommends beginning evaluation in 2002 and phased deployment in 2003.

**Author:** Peter S. Kastner · **Date:** 2002-05 · **Type:** white-paper
**Importance:** high — *Foundational Aberdeen analysis of InfiniBand at the time of its emergence; combines architecture overview with enterprise planning guidance and early-adopter evidence.*
**Prescience:** high — *Correctly predicted IBA adoption in HPC and large enterprise; blade server adoption with IBA; TCP offload engine uses; though IBA did not fully replace PCI-X in broad enterprise as envisioned — HPC became the primary domain.*

## Entities (20)

- [[aberdeen-group|Aberdeen Group]]
- [[adaptec|Adaptec]]
- [[agilent-technologies|Agilent Technologies]]
- [[cisco|Cisco]]
- [[compaq|Compaq]]
- [[dell|Dell]]
- [[emulex|Emulex]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[infiniband-trade-association|InfiniBand Trade Association (IBTA)]]
- [[infinicon|InfiniCon Systems]]
- [[infiniswitch|InfiniSwitch]]
- [[intel|Intel Corporation]]
- [[mellanox-technologies|Mellanox Technologies]]
- [[microsoft|Microsoft]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[qlogic|QLogic]]
- [[sun-microsystems|Sun Microsystems]]
- [[unisys|Unisys]]
- [[voltaire|Voltaire]]

## Technologies (16)

- [[3gio-pci|3GIO (Third Generation I/O / PCI Express predecessor)]]
- [[agp|AGP (Accelerated Graphics Port)]]
- [[clustering|High-Availability / Performance Clustering]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[infiniband|InfiniBand Architecture (IBA)]]
- [[infiniband-hca|InfiniBand Host Channel Adapter (HCA)]]
- [[infiniband-switch|InfiniBand Switch/Router]]
- [[infiniband-tca|InfiniBand Target Channel Adapter (TCA)]]
- [[iscsi|iSCSI]]
- [[nas|Network Attached Storage (NAS)]]
- [[pci-x|PCI-X]]
- [[san|Storage Area Network (SAN)]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[server-blades|Server Blade Architecture]]
- [[tcp-ip|TCP/IP]]
- [[tcp-offload-engine|TCP Offload Engine (TOE)]]

## Key observations (top 25)

- **2002** — IBTA technology sponsors: more than 200
- **2002** — IBA bandwidth (12x): up to 30 Gbps
- **2002** — PCI bus bandwidth (aggregate): 532 MB/second (parallel PCI)
- **2002** — IBA per-link bandwidth: 500 MB/s minimum to 6 GB/s
- **2002** — IBA TCO reduction for database clusters: on the order of 50%
- **2002** — IBA I/O management cost savings: on the order of 70%
- **2002** — IBA clustering performance: near-linear scaling of transaction processing
- **2002** — TCP/IP processing freed by IBA router: significant CPU capacity freed
- **2003** — Major suppliers offering IBA-enabled blades: all major computer suppliers in 2003
- **2002** — IBA production deployment timeline: enterprise production beginning 2003
- **2023** — IBA production deployment timeline: [UNVERIFIED]
- **2002** — IBA vs PCI-X long-term: IBA will replace PCI-X as next-generation I/O interconnect
- **2023** — IBA vs PCI-X long-term: [UNVERIFIED]
- **2002** — Blade server drivers: dense computing and consolidation via IBA
- **2002** — HCA availability timeline: late 2002 or early 2003
- **2003** — HCA embedded in server systems: leading manufacturers 2003
- **2002** — SCSI ubiquity: primary server-storage protocol
- **2002** — FC-SAN limitation: high cost and complexity limits to large enterprise data centers
- **2004** — TOE expected uses: server-to-server, server-to-storage, TCP offload in 2004
- **2002** — 3GIO vs IBA: complementary: 3GIO replaces PCI; IBA handles I/O connectivity beyond motherboard
- **2002** — IBA evaluation timing: begin evaluating 2002; phased deployment 2003
- **2002** — IBA fabric adoption preference: emerged as preferred architecture for storage networking per Aberdeen research

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'intel-infiband-wp--edit-psk-5-22f-a2c551' ORDER BY year_observed;
```

