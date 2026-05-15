---
title: "A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983)"
slug: ieee-db-stratus-32-psk-1d4564
page_type: study
author: "Peter S. Kastner — Stratus Computer, Inc."
date: "1983-06-01"
study_type: technical-article
subject_domain: "fault-tolerant-computing-OLTP"
methodology: "industry-analysis,technical-architecture-description,document-review"
importance: high
importance_rationale: "Kastner-authored peer-reviewed IEEE Computer Society Technical Committee on Database Engineering article — primary technical-press source documenting the Stratus/32 fault-tolerant architecture (VOS, StrataLINK, TPF, two-phase commit) during Kastner's Stratus marketing tenure. Establishes his early authorial voice in the OLTP/transaction-processing technical community five years before his DEC Debit-Credit primer and the 1988 founding of TPC."
relevance: medium
relevance_rationale: "Continuous-Processing pair-and-spare hardware redundancy and two-phase commit with disk mirroring remain foundational concepts in modern always-on systems (financial markets, telecom, payments, cloud HA). Specific 68000-era hardware details are dated, but the architectural thesis still maps directly to today's resilient-system designs."
prescience: high
prescience_rationale: "Anticipated the now-universal architectural patterns of: (1) location-transparent distributed file systems (NFS, modern object stores), (2) two-phase commit for distributed transactions (still the textbook protocol in 2026), (3) call-home telemetry for predictive maintenance (modern AIOps), (4) self-checking commodity processors as a path to fault tolerance, and (5) hardware-detected failures with software-managed reconfiguration — the lineage that runs through HP NonStop, mainframe-class cloud,…"
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 14
obs_count: 28
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983)

> Peer-reviewed article by Peter S. Kastner of Stratus Computer, Inc., published in IEEE Computer Society Technical Committee on Database Engineering Bulletin (June 1983, Vol.6 No.2, pp.20-28). Describes the Stratus/32 multiprocessor fault-tolerant system architecture for commercial on-line transaction processing (OLTP). Each processing module contains paired self-checking logic (Motorola 68000 CPUs, memory, disk controllers), with up to 32 modules connected via the StrataLINK high-speed coaxial link. Stratus's Virtual Operating System (VOS) presents the federation as a single virtual computer, with transparent file/process distribution. Key software components covered: VOS file system, StrataNET networking, Transaction Processing Facility (TPF) with multi-tasking servers and START/COMMIT/ABORT primitives, two-phase commit protocol with 'Phase I Commit' flag, mirrored disks for write durability, and the Forms Management Facility. The article documents Stratus's continuous-processing thesis: hardware-detected failures with redundant pair-and-spare partners eliminate the need for checkpoint/restart programming at user or system level. This is Kastner's primary published technical exposition of Stratus architecture during his Stratus marketing tenure.

**Author:** Peter S. Kastner — Stratus Computer, Inc. · **Date:** 1983-06-01 · **Type:** technical-article
**Importance:** high — *Kastner-authored peer-reviewed IEEE Computer Society Technical Committee on Database Engineering article — primary technical-press source documenting the Stratus/32 fault-tolerant architecture (VOS, StrataLINK, TPF, two-phase commit) during Kastner's Stratus marketing tenure. Establishes his early a…*
**Prescience:** high — *Anticipated the now-universal architectural patterns of: (1) location-transparent distributed file systems (NFS, modern object stores), (2) two-phase commit for distributed transactions (still the textbook protocol in 2026), (3) call-home telemetry for predictive maintenance (modern AIOps), (4) self…*

## Entities (7)

- [[ieee-computer-society|IEEE Computer Society]]
- [[ieee-tcde|IEEE TC on Database Engineering]]
- [[motorola-inc|Motorola Corp.]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer, Inc.]]
- [[stratus-natick-ma|Stratus Computer Natick MA HQ]]
- [[tandem-computers|Tandem Computers]]

## Technologies (14)

- [[basic-language|BASIC]]
- [[cobol|COBOL]]
- [[disk-mirroring|Disk Mirroring (RAID-1 precursor)]]
- [[fortran|FORTRAN]]
- [[motorola-68000|Motorola 68000 CPU]]
- [[pascal|Pascal]]
- [[pl-1|PL/I]]
- [[stratus-32|Stratus/32]]
- [[stratus-fms|Forms Management Facility]]
- [[stratus-stralink|StrataLINK]]
- [[stratus-stranet|StrataNET]]
- [[stratus-tpf|Stratus Transaction Processing Facility (TPF)]]
- [[stratus-vos|Virtual Operating System (VOS)]]
- [[two-phase-commit|Two-Phase Commit Protocol]]

## Key observations (top 25)

- **1983** — System scale: Up to 32 processing modules per Stratus system, connected via StrataLINK high-speed coax
- **1983** — Per-module hardware: Memory + 2 Motorola 68000 CPUs (software-visible) + ≥1 disk + peripheral controllers; CPU board contains 4 actual 68000 dies (2 self-checking pairs)
- **1983** — Module redundancy modes: Fully redundant / partially redundant / non-redundant; configurable per module; reconfiguration on-line without affecting running programs
- **1983** — Multi-module purpose: 'Multiple modules are used only to achieve greater system capacity; they never serve as backup for other modules.'
- **1983** — VOS distribution model: VOS runs in every module; all modules equal; transparent local networking makes the federation appear as a single virtual computer to programs, programmers and users
- **1983** — Uniform service interface: All VOS service requests have a uniform interface independent of which module performs the work (e.g., file open is identical regardless of disk location)
- **1983** — Bus architecture: Single 125 nsec cycle-time high-speed bus implemented as two parallel buses with independent data and control-logic paths
- **1983** — Self-checking board protocol: Each board runs two parallel sets of logic; on output, results are compared; mismatch lights red LED, raises bus interrupt, takes board off-line; redundant partner continues; no other component is aware
- **1983** — CPU board internals: Single CPU board = 4 Motorola 68000s organized as 2 software-visible CPUs; redundant virtual/physical address-translation maps; redundant partner CPU board for board-level fault tolerance
- **1983** — 68000 component price: Approximately $100 per Motorola 68000 in 1983
- **1983** — Memory subsystem: Redundant config: N MB program-visible memory implemented as 2N MB physical, split across 2 controllers; 64K RAMs on 2MB boards; 375 nsec read cycle; 4-way interleaved; redundancy can be turned on/off dynamically
- **1983** — Disk mirroring policy: Each disk can have a duplicate on a separate controller; writes go to both; reads come from the disk that is not busy or whose heads are best positioned; read errors retried from mirror
- **1983** — StrataLINK fault tolerance: Dual StrataLINKs run as parallel separate links; on failure of one, data are retransmitted over the survivor without affecting users
- **1983** — Phone-home maintenance call: On hard failure, maintenance software process automatically calls the Stratus national service center and transmits a data packet with site and failure info; 'Stratus service people know within a minute of customer failures'
- **1983** — Hot-swap field service: A failed board can be replaced in a running system by a non-technical person without special tools and without affecting any user's program; VOS dynamically reconfigures
- **1983** — TPF programming languages: Application programs may be written in COBOL, PL/I, BASIC, FORTRAN or Pascal; all language features usable, including I/O statements
- **1983** — TPF concurrency model: Multi-tasking, multiple transaction servers, large program address space; terminal-handling requesters and application servers can reside anywhere within a system or network of systems
- **1983** — TPF queue-based scaling: Single message queue can connect any number of servers with any number of requesters; queues redirect dynamically by changing the pathname to point to another module — applications scale without recompile
- **1983** — Two-phase commit implementation: Phase I writes all updated records to disk and sets 'Phase I Commit' flag in file header; original disk image preserved; all involved nodes must report Phase I success before VOS authorizes Phase II commit; restart-salvage detects Phase I Commit flag
- **1983** — Transaction primitives: START / COMMIT / ABORT primitives in TPF; ABORT restores all files to pre-START state regardless of whether data is on a single processing module or distributed
- **1983** — StrataNET security: System administrator can permit, permit-after-network-password, or deny incoming requests on each system node; access-control lists enforced across the network
- **1983** — File access-control lists: Every file has an access-control list of (user-id, rights ∈ {execute, read, read/write}); per-user or per-group; no embedded passwords in programs; enforced regardless of access program/command
- **1983** — Continuous-processing thesis: 'Stratus Computer uses hardware to detect failures before incorrect data can corrupt processing and databases. Redundant hardware allows the Stratus/32 to continue processing without performance loss in spite of a component failure.'
- **1983** — Synergy of HW fault-tolerance + system software: 'The synergy of hardware-based fault tolerance and high data integrity system software creates an efficient and friendly transaction processing environment.'
- **1983** — Location-transparent distributed FS adoption: Verified: location transparency (paths resolve to remote storage) became universal in NFS, AFS, DFS, modern object stores and global file systems

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ieee-db-stratus-32-psk-1d4564' ORDER BY year_observed;
```

