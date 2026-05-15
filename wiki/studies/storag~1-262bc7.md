---
title: "Storage & Storage Management: 1998 Practice Summary"
slug: storag~1-262bc7
page_type: study
author: "Aberdeen Group"
date: "1998-05-01"
study_type: other-research
subject_domain: "enterprise-storage"
methodology: "industry-analysis"
importance: medium
importance_rationale: "Institutional practice summary capturing the inflection point when enterprise storage transitioned from captive server-attached to networked architectures; valuable historical context for SAN/NAS adoption."
relevance: high
relevance_rationale: "Network storage architectures (SAN/NAS), storage management software, and the principle that storage must integrate with overall IT architecture remain foundational enterprise IT topics."
prescience: high
prescience_rationale: "Aberdeen correctly predicted that Fibre Channel SANs would not mainstream until 1999-2000 and that storage management software would become the key differentiator over raw hardware."
license: CC-BY-4.0
tier: 1
entity_count: 22
tech_count: 13
obs_count: 22
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Storage & Storage Management: 1998 Practice Summary

> Aberdeen Group's 1998 analysis of the enterprise storage market, arguing that storage must be treated as a system-level architectural decision — not a commodity — and introducing the concept of 'network storage' (any storage accessed over a network). The report covers SANs, NAS, Fibre Channel, RAID, tape technologies, and storage management software, forecasting that SANs would not become common until 1999 and that storage management software would be the critical differentiator. Supplier profiles cover 11 vendors including EMC, IBM, HP, VERITAS, Legato, and StorageTek.

**Author:** Aberdeen Group · **Date:** 1998-05-01 · **Type:** other-research
**Importance:** medium — *Institutional practice summary capturing the inflection point when enterprise storage transitioned from captive server-attached to networked architectures; valuable historical context for SAN/NAS adoption.*
**Prescience:** high — *Aberdeen correctly predicted that Fibre Channel SANs would not mainstream until 1999-2000 and that storage management software would become the key differentiator over raw hardware.*

## Entities (22)

- [[aberdeen-group|Aberdeen Group]]
- [[boole-and-babbage|Boole & Babbage Inc.]]
- [[brocade|Brocade Communications]]
- [[comdisco|Comdisco]]
- [[compaq|Compaq]]
- [[computer-associates|Computer Associates (CA)]]
- [[data-general|Data General Corporation]]
- [[emc|EMC Corporation]]
- [[exabyte|Exabyte]]
- [[gadzoox|Gadzoox Networks]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm|IBM]]
- [[intelliguard-software|Intelliguard Software]]
- [[legato|Legato Systems]]
- [[quantum-corporation|Quantum Corporation]]
- [[quinta-corporation|Quinta Corporation]]
- [[seagate-technology|Seagate Technology]]
- [[storagetek|Storage Technology Corporation (StorageTek)]]
- [[sun-microsystems|Sun Microsystems]]
- [[sungard|SunGard Data Systems]]
- [[veritas|VERITAS Software]]
- [[vixel|Vixel Corporation]]

## Technologies (13)

- [[escon|ESCON (Enterprise Systems Connection)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[hierarchical-storage|Hierarchical Storage Management (HSM)]]
- [[lto|Linear Tape-Open (LTO)]]
- [[nas|Network Attached Storage (NAS)]]
- [[network-storage|Network Storage Architecture]]
- [[raid|RAID (Redundant Array of Independent Disks)]]
- [[san|Storage Area Network (SAN)]]
- [[scsi|SCSI (Small Computer System Interface)]]
- [[ssa|Serial Storage Architecture (SSA)]]
- [[storage-mgmt-software|Storage Management Software]]
- [[super-dlt|Super DLTtape]]
- [[tape-backup|Tape Backup and Libraries]]

## Key observations (top 25)

- **1998** — Network storage complexity threshold: beyond 20 servers / 100 GB / multiple databases
- **1998** — RAID on LAN servers: now commonplace due to lower disk prices
- **1998** — SAN mainstream adoption timeline: 1998 is not the year of Fibre Channel or SANs; adoption common by 1999
- **1999** — SAN/Fibre Channel mainstream — actual outcome: Prediction proved accurate; Fibre Channel SAN began mainstream adoption 1999-2001.
- **1998** — Fibre Channel transmission speed: 100 MB per second
- **1998** — Tape backup strategic role: essential despite RAID; required for archiving disaster recovery non-hardware losses
- **1998** — Optically-assisted Winchester technology theoretical density: 250 Gbits/in2
- **1998** — Storage management software vs hardware importance: software will be key differentiator over hardware
- **1998** — Storage management software integration requirement: must integrate with HP OpenView / Tivoli / Unicenter TNG
- **1998** — Storage IS organizational status: storage is now equal to servers and architecture — Big 2 is Big 3
- **1998** — Next-gen tape technologies announced: Quantum Super DLTtape; HP/IBM/Seagate Linear Tape-Open (LTO)
- **1998** — Unix and NT disk storage market structure: mostly captive as part of server sale
- **1998** — NAS vs SAN positioning: both provide greater flexibility than server-dependent storage
- **1998** — EMC storage market position: leading enterprise storage hardware vendor
- **1998** — VERITAS storage software market position: leading storage management and backup software
- **1998** — Legato storage software market position: backup and recovery software via Networker
- **1998** — StorageTek market position: tape libraries and enterprise storage specialist
- **1998** — Storage administration labor cost challenge: finding sufficient storage management staff too difficult and too expensive
- **1998** — Cheap-storage myth: per-megabyte cost decline disguises true total cost; storage that cannot perform is expensive
- **1998** — HSM adoption status: non-mainframe HSM implementation cited as strategic question
- **1998** — Storage policy management evolution: software agents and predictive systems will enable preventative maintenance
- **1998** — Enterprise storage management philosophy shift: must treat storage as part of overall system — not commodity

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'storag~1-262bc7' ORDER BY year_observed;
```

