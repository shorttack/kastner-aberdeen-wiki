---
title: "InfiniBand Architecture: Planning the Next-Generation Data Center"
slug: "study-infiniband-data-center-wp-2002"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "infiniband-data-center-wp-2002"
author: "Peter S. Kastner"
date: "2002-05-01"
pub_year: 2002
type: "white-paper"
subject_domain: "data-center-interconnect"
methodology: "industry-analysis,technology-assessment,expert-opinion"
source_file: "intel-infiband-wp--edit-psk-5-22f-a2c551"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# InfiniBand Architecture: Planning the Next-Generation Data Center

> An Aberdeen Group executive white paper published in May 2002 arguing that InfiniBand Architecture (IBA) would replace PCI-based I/O as the dominant data center interconnect within two to three years. The paper evaluates IBA's switched-fabric design against existing SCSI, Fibre Channel, and Ethernet protocols, and predicts adoption beginning in large enterprise and HPC data centers. It identifies blade server and server clustering as the primary early use cases and calls on IT planners to begin phased IBA deployments in 2003.


_Published 2002, author **Peter S. Kastner**, type **white-paper**._


## Top observations

- 133 MB/s shared by all devices on bus
- 500 MB/s per link minimum scaling to 6 GB/s; 12-wire config reaches 30 Gb/s
- 200+ technology sponsors
- Phased deployment beginning 2003; HCA silicon on system board by late 2003
- [UNVERIFIED]
- All major suppliers offering IBA-enabled blades by 2003
- Largely validated; HP/IBM/Dell shipped IBA-capable blade systems 2003-2004
- Up to three levels of redundancy
- Three: Host Channel Adapter (HCA) + Target Channel Adapter (TCA) + Switches/Routers
- Offloads transport from host CPU via InfiniBand processor organizing I/O into packets
- RDMA concepts from IBA directly influenced RoCE (RDMA over Converged Ethernet) and NVMe-oF; foundational to AI/ML training infrastructure
- Freeing server CPU from TCP/IP processing via IBA router; stretches per-processor software licenses
- TOE cards became commercial products 2004-2008; IBA TOE validated for HPC but commodity NICs eventually handled offload via kernel bypass
- ~50% TCO reduction; ~70% lower I/O management costs
- Dozens of blades in rack create cabling rat's nest; server-to-server bandwidth and latency become performance limiters
- 12 processing blades with redundant switched backplane and common power
- PCI-X and PCI-X 2.0 are inadequate and will not satisfy long-term data center connectivity needs
- PCI Express (PCIe) — not IBA — became the universal server I/O bus; IBA coexisted as an external fabric rather than replacing internal I/O
- FC is an early network storage I/O protocol providing superior performance; IBA will route FC traffic and coexist initially
- Large enterprise and research data centers where greatest need for expanded I/O bandwidth exists
- IBA >70% of TOP500 supercomputers by mid-2010s; dominant AI/ML training cluster fabric
- Compaq acquired by HP in 2002 during paper publication period
- Virtual Lanes allow QoS multiplexing on same physical link; every switch acts as QoS director
- Decouples CPU from I/O controller; extends distance from inches to kilometers
- iSCSI cited as example of storage-over-IP architecture trend aligned with IBA's fabric model
