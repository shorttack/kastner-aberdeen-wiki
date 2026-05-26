---
title: "A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983)"
slug: "study-ieee-db-stratus-32-psk-1d4564"
page_type: "study"
tags: ["type/study", "collection/technical-article"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "ieee-db-stratus-32-psk-1d4564"
author: "Peter S. Kastner — Stratus Computer, Inc."
date: "1983-06-01"
pub_year: 1983
type: "technical-article"
subject_domain: "fault-tolerant-computing-OLTP"
methodology: "industry-analysis,technical-architecture-description,document-review"
source_file: "IEEE-DB-Stratus-32-PSK.md"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# A Fault-Tolerant Transaction Processing Environment (Stratus/32, IEEE Database Engineering, June 1983)

> Peer-reviewed article by Peter S. Kastner of Stratus Computer, Inc., published in IEEE Computer Society Technical Committee on Database Engineering Bulletin (June 1983, Vol.6 No.2, pp.20-28). Describes the Stratus/32 multiprocessor fault-tolerant system architecture for commercial on-line transaction processing (OLTP). Each processing module contains paired self-checking logic (Motorola 68000 CPUs, memory, disk controllers), with up to 32 modules connected via the StrataLINK high-speed coaxial link. Stratus's Virtual Operating System (VOS) presents the federation as a single virtual computer, with transparent file/process distribution. Key software components covered: VOS file system, StrataNET networking, Transaction Processing Facility (TPF) with multi-tasking servers and START/COMMIT/ABORT primitives, two-phase commit protocol with 'Phase I Commit' flag, mirrored disks for write durability, and the Forms Management Facility. The article documents Stratus's continuous-processing thesis: hardware-detected failures with redundant pair-and-spare partners eliminate the need for checkpoint/restart programming at user or system level. This is Kastner's primary published technical exposition of Stratus architecture during his Stratus marketing tenure.


_Published 1983, author **Peter S. Kastner — Stratus Computer, Inc.**, type **technical-article**._


## Top observations

- Up to 32 processing modules per Stratus system, connected via StrataLINK high-speed coax
- Memory + 2 Motorola 68000 CPUs (software-visible) + ≥1 disk + peripheral controllers; CPU board contains 4 actual 68000 dies (2 self-checking pairs)
- Fully redundant / partially redundant / non-redundant; configurable per module; reconfiguration on-line without affecting running programs
- 'Multiple modules are used only to achieve greater system capacity; they never serve as backup for other modules.'
- VOS runs in every module; all modules equal; transparent local networking makes the federation appear as a single virtual computer to programs, programmers and users
- All VOS service requests have a uniform interface independent of which module performs the work (e.g., file open is identical regardless of disk location)
- Single 125 nsec cycle-time high-speed bus implemented as two parallel buses with independent data and control-logic paths
- Each board runs two parallel sets of logic; on output, results are compared; mismatch lights red LED, raises bus interrupt, takes board off-line; redundant partner continues; no other component is aware
- Single CPU board = 4 Motorola 68000s organized as 2 software-visible CPUs; redundant virtual/physical address-translation maps; redundant partner CPU board for board-level fault tolerance
- Approximately $100 per Motorola 68000 in 1983
- Redundant config: N MB program-visible memory implemented as 2N MB physical, split across 2 controllers; 64K RAMs on 2MB boards; 375 nsec read cycle; 4-way interleaved; redundancy can be turned on/off dynamically
- Each disk can have a duplicate on a separate controller; writes go to both; reads come from the disk that is not busy or whose heads are best positioned; read errors retried from mirror
- Dual StrataLINKs run as parallel separate links; on failure of one, data are retransmitted over the survivor without affecting users
- On hard failure, maintenance software process automatically calls the Stratus national service center and transmits a data packet with site and failure info; 'Stratus service people know within a minute of customer failures'
- A failed board can be replaced in a running system by a non-technical person without special tools and without affecting any user's program; VOS dynamically reconfigures
- Application programs may be written in COBOL, PL/I, BASIC, FORTRAN or Pascal; all language features usable, including I/O statements
- Multi-tasking, multiple transaction servers, large program address space; terminal-handling requesters and application servers can reside anywhere within a system or network of systems
- Single message queue can connect any number of servers with any number of requesters; queues redirect dynamically by changing the pathname to point to another module — applications scale without recompile
- Phase I writes all updated records to disk and sets 'Phase I Commit' flag in file header; original disk image preserved; all involved nodes must report Phase I success before VOS authorizes Phase II commit; restart-salvage detects Phase I Commit flag
- START / COMMIT / ABORT primitives in TPF; ABORT restores all files to pre-START state regardless of whether data is on a single processing module or distributed
- System administrator can permit, permit-after-network-password, or deny incoming requests on each system node; access-control lists enforced across the network
- Every file has an access-control list of (user-id, rights ∈ {execute, read, read/write}); per-user or per-group; no embedded passwords in programs; enforced regardless of access program/command
- 'Stratus Computer uses hardware to detect failures before incorrect data can corrupt processing and databases. Redundant hardware allows the Stratus/32 to continue processing without performance loss in spite of a component failure.'
- 'The synergy of hardware-based fault tolerance and high data integrity system software creates an efficient and friendly transaction processing environment.'
- Verified: location transparency (paths resolve to remote storage) became universal in NFS, AFS, DFS, modern object stores and global file systems
