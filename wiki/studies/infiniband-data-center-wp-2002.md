---
title: "InfiniBand Architecture: Planning the Next-Generation Data Center"
slug: infiniband-data-center-wp-2002
page_type: study
author: "Peter S. Kastner"
date: "2002-05-01"
study_type: white-paper
subject_domain: "data-center-interconnect"
methodology: "industry-analysis,technology-assessment,expert-opinion"
importance: high
importance_rationale: "One of the earliest comprehensive enterprise analyst assessments of InfiniBand at the moment the IBTA standard was solidifying; shaped vendor and IT planner thinking about next-generation I/O architecture at a pivotal juncture."
relevance: medium
relevance_rationale: "IBA did become the dominant HPC interconnect fabric and RDMA concepts from IBA directly influenced RoCE and NVMe-oF, which remain central to modern AI/ML and storage networking; however specific PCI-X displacement predictions were only partially realized."
prescience: high
prescience_rationale: "Correctly predicted IBA adoption in HPC/storage clustering and blade server integration (7-8/10). Blade + IBA prediction proved accurate; TCP offload engine (TOE) prediction validated. IBA did not replace PCI-X in broad enterprise as envisioned — HPC and AI/ML training clusters became the primary domain. RDMA and switched-fabric concepts profoundly influenced RoCE and NVMe-oF, validating the core architectural thesis."
license: CC-BY-4.0
tier: 1
entity_count: 20
tech_count: 14
obs_count: 32
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# InfiniBand Architecture: Planning the Next-Generation Data Center

> An Aberdeen Group executive white paper published in May 2002 arguing that InfiniBand Architecture (IBA) would replace PCI-based I/O as the dominant data center interconnect within two to three years. The paper evaluates IBA's switched-fabric design against existing SCSI, Fibre Channel, and Ethernet protocols, and predicts adoption beginning in large enterprise and HPC data centers. It identifies blade server and server clustering as the primary early use cases and calls on IT planners to begin phased IBA deployments in 2003.

**Author:** Peter S. Kastner · **Date:** 2002-05-01 · **Type:** white-paper
**Importance:** high — *One of the earliest comprehensive enterprise analyst assessments of InfiniBand at the moment the IBTA standard was solidifying; shaped vendor and IT planner thinking about next-generation I/O architecture at a pivotal juncture.*
**Prescience:** high — *Correctly predicted IBA adoption in HPC/storage clustering and blade server integration (7-8/10). Blade + IBA prediction proved accurate; TCP offload engine (TOE) prediction validated. IBA did not replace PCI-X in broad enterprise as envisioned — HPC and AI/ML training clusters became the primary do…*

## Entities (20)

- [[aberdeen-group|Aberdeen Group]]
- [[adaptec|Adaptec]]
- [[agilent-technologies|Agilent Technologies]]
- [[cisco|Cisco Systems]]
- [[compaq|Compaq Computer Corporation]]
- [[dell|Dell Technologies]]
- [[emulex|Emulex Corporation]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[infiniband-trade-association|InfiniBand Trade Association (IBTA)]]
- [[infinicon|InfiniCon Systems]]
- [[infiniswitch|InfiniSwitch]]
- [[intel|Intel Corporation]]
- [[mellanox-technologies|Mellanox Technologies]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[qlogic|QLogic]]
- [[sun-microsystems|Sun Microsystems]]
- [[unisys|Unisys Corporation]]
- [[voltaire|Voltaire]]

## Technologies (14)

- [[3gio-pcie|3GIO / PCI Express (PCIe)]]
- [[blade-servers|Blade Server]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[hca|Host Channel Adapter (HCA)]]
- [[infiniband|InfiniBand Architecture (IBA)]]
- [[iscsi|iSCSI]]
- [[nas|Network Attached Storage (NAS)]]
- [[pci|Peripheral Component Interconnect (PCI)]]
- [[pci-x|PCI-X]]
- [[rdma|RDMA (Remote Direct Memory Access)]]
- [[san|Storage Area Network (SAN)]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[tca|Target Channel Adapter (TCA)]]
- [[tcp-ip|TCP/IP]]

## Key observations (top 25)

- **2002** — PCI bus bandwidth ceiling: 133 MB/s shared by all devices on bus
- **2002** — IBA link bandwidth range: 500 MB/s per link minimum scaling to 6 GB/s; 12-wire config reaches 30 Gb/s
- **2002** — IBTA member companies: 200+ technology sponsors
- **2002** — IBA production enterprise adoption timeline: Phased deployment beginning 2003; HCA silicon on system board by late 2003
- **2010** — IBA enterprise adoption — actual outcome: [UNVERIFIED]
- **2002** — Major computer suppliers offering IBA-enabled blades: All major suppliers offering IBA-enabled blades by 2003
- **2004** — IBA-enabled blade server market — actual outcome: Largely validated; HP/IBM/Dell shipped IBA-capable blade systems 2003-2004
- **2002** — IBA redundancy levels provided: Up to three levels of redundancy
- **2002** — IBA architecture components: Three: Host Channel Adapter (HCA) + Target Channel Adapter (TCA) + Switches/Routers
- **2002** — RDMA capability description: Offloads transport from host CPU via InfiniBand processor organizing I/O into packets
- **2020** — RDMA influence on modern networking — actual outcome: RDMA concepts from IBA directly influenced RoCE (RDMA over Converged Ethernet) and NVMe-oF; foundational to AI/ML training infrastructure
- **2002** — TCP/IP offload engine (TOE) benefit: Freeing server CPU from TCP/IP processing via IBA router; stretches per-processor software licenses
- **2006** — TCP offload engine commercialization — actual outcome: TOE cards became commercial products 2004-2008; IBA TOE validated for HPC but commodity NICs eventually handled offload via kernel bypass
- **2002** — Expected TCO reduction for database clusters: ~50% TCO reduction; ~70% lower I/O management costs
- **2002** — Blade server I/O problem description: Dozens of blades in rack create cabling rat's nest; server-to-server bandwidth and latency become performance limiters
- **2002** — Blades per rack in IBA reference design: 12 processing blades with redundant switched backplane and common power
- **2002** — PCI-X adequacy assessment: PCI-X and PCI-X 2.0 are inadequate and will not satisfy long-term data center connectivity needs
- **2006** — PCI-X displacement — actual outcome: PCI Express (PCIe) — not IBA — became the universal server I/O bus; IBA coexisted as an external fabric rather than replacing internal I/O
- **2002** — Fibre Channel positioning vs IBA: FC is an early network storage I/O protocol providing superior performance; IBA will route FC traffic and coexist initially
- **2002** — IBA first deployment environment: Large enterprise and research data centers where greatest need for expanded I/O bandwidth exists
- **2015** — IBA HPC market share — actual outcome: IBA >70% of TOP500 supercomputers by mid-2010s; dominant AI/ML training cluster fabric
- **2002** — Compaq merger with HP: Compaq acquired by HP in 2002 during paper publication period
- **2002** — IBA Quality of Service feature: Virtual Lanes allow QoS multiplexing on same physical link; every switch acts as QoS director
- **2002** — IBA distance capability: Decouples CPU from I/O controller; extends distance from inches to kilometers
- **2002** — iSCSI positioning vs IBA: iSCSI cited as example of storage-over-IP architecture trend aligned with IBA's fabric model

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'infiniband-data-center-wp-2002' ORDER BY year_observed;
```

