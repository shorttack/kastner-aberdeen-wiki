---
title: "InfiniBand Architecture: Planning the Next-Generation Data Center"
slug: "study-infiniband-data-center-wp-2002"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
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
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 2.75
prescience_obs_count: 24
---

# InfiniBand Architecture: Planning the Next-Generation Data Center


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.72 over 32 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.84 over 32 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> An Aberdeen Group executive white paper published in May 2002 arguing that InfiniBand Architecture (IBA) would replace PCI-based I/O as the dominant data center interconnect within two to three years. The paper evaluates IBA's switched-fabric design against existing SCSI, Fibre Channel, and Ethernet protocols, and predicts adoption beginning in large enterprise and HPC data centers. It identifies blade server and server clustering as the primary early use cases and calls on IT planners to begin phased IBA deployments in 2003.


_Published 2002, author **Peter S. Kastner**, type **white-paper**._


## Top observations

- Offloads transport from host CPU via InfiniBand processor organizing I/O into packets `[ps=5]`
- RDMA concepts from IBA directly influenced RoCE (RDMA over Converged Ethernet) and NVMe-oF; foundational to AI/ML training infrastructure `[ps=5]`
- TOE cards became commercial products 2004-2008; IBA TOE validated for HPC but commodity NICs eventually handled offload via kernel bypass `[ps=5]`
- PCI-X and PCI-X 2.0 are inadequate and will not satisfy long-term data center connectivity needs `[ps=5]`
- PCI Express (PCIe) — not IBA — became the universal server I/O bus; IBA coexisted as an external fabric rather than replacing internal I/O `[ps=5]`
- Bandwidth scales as number of I/O ports increases; IBA overcomes shared bus bandwidth ceiling `[ps=5]`
- IBA/Mellanox critical for NVIDIA AI/ML training clusters; NVIDIA acquired Mellanox for $6.9B in 2019-2020 `[ps=5]`
- 500 MB/s per link minimum scaling to 6 GB/s; 12-wire config reaches 30 Gb/s `[ps=4]`
- Dozens of blades in rack create cabling rat's nest; server-to-server bandwidth and latency become performance limiters `[ps=4]`
- Virtual Lanes allow QoS multiplexing on same physical link; every switch acts as QoS director `[ps=4]`
- Large enterprise and research data centers where greatest need for expanded I/O bandwidth exists `[ps=3]`
- IBA >70% of TOP500 supercomputers by mid-2010s; dominant AI/ML training cluster fabric `[ps=3]`
- iSCSI cited as example of storage-over-IP architecture trend aligned with IBA's fabric model `[ps=3]`
- Multiple different cables in enterprise rack replaced with single common cable per server/storage unit `[ps=3]`
- Freeing server CPU from TCP/IP processing via IBA router; stretches per-processor software licenses `[ps=2]`
- ~50% TCO reduction; ~70% lower I/O management costs `[ps=2]`
- Leading manufacturers (Compaq/HP Dell IBM Unisys) to deliver servers with embedded HCA by 2003 `[ps=2]`
- All major suppliers offering IBA-enabled blades by 2003 `[ps=1]`
- 133 MB/s shared by all devices on bus `[ps=0]`
- 200+ technology sponsors `[ps=0]`
- [UNVERIFIED] `[ps=0]`
- Three: Host Channel Adapter (HCA) + Target Channel Adapter (TCA) + Switches/Routers `[ps=0]`
- 12 processing blades with redundant switched backplane and common power `[ps=0]`
- Compaq acquired by HP in 2002 during paper publication period `[ps=0]`
- Phased deployment beginning 2003; HCA silicon on system board by late 2003
