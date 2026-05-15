---
title: "Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)"
slug: dtj-v03-01-tp-and-fault-tolerant-1991-cf078c
page_type: study
author: "Digital Equipment Corporation"
date: "1991-01-01"
study_type: employer-record
subject_domain: "transaction-processing"
methodology: "document-review, industry-analysis"
importance: high
importance_rationale: "Primary-source technical journal documenting the complete DECtp architecture at the moment of its 1988 announcement and 1991 maturation; first formal disclosure of DEC's TPC Benchmark A audited results and the DECdta distributed TP architecture."
relevance: high
relevance_rationale: "Transaction ACID properties, two-phase commit, client/server TP decomposition, fault-tolerant hardware design, and group commit optimization remain foundational concepts in modern distributed databases and cloud transaction systems."
prescience: high
prescience_rationale: "DECtp's open-standards alignment (X/Open DTP, OSI-TP, POSIX) and client/server model accurately anticipated the dominant paradigm; predicted convergence of ACMS and DECintact proved correct; VAXft fault-tolerant architecture foreshadowed modern high-availability designs., employer_id=DEC, kastner_role=Marketing (led the DECtp product work that resulted in these articles; specifically led the 1988 DECtp announcement), record_subtype=technical-journal, source_url=https://vmssoftware.com/docs/dtj-v…"
license: CC-BY-4.0
tier: 1
entity_count: 36
tech_count: 28
obs_count: 40
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)

> This issue of the Digital Technical Journal presents eight peer-reviewed technical papers documenting DEC's complete distributed transaction processing stack, including the DECdta architecture, ACMS and DECintact TP monitors, DECdtm kernel-level transaction management, TPC Benchmark A performance results, database availability strategies, optimized commit protocols, and VAXft 3000 fault-tolerant system verification. The papers collectively define DEC's strategy to lead the distributed TP market through an integrated, standards-aligned, client/server architecture. Formal TPC Benchmark A results are disclosed: 69.4 tpsA-Local on VAX 9000 Model 210 and 21.6 tpsA-Local on VAX 4000 Model 300.

**Author:** Digital Equipment Corporation · **Date:** 1991-01-01 · **Type:** employer-record
**Importance:** high — *Primary-source technical journal documenting the complete DECtp architecture at the moment of its 1988 announcement and 1991 maturation; first formal disclosure of DEC's TPC Benchmark A audited results and the DECdta distributed TP architecture.*
**Prescience:** high — *DECtp's open-standards alignment (X/Open DTP, OSI-TP, POSIX) and client/server model accurately anticipated the dominant paradigm; predicted convergence of ACMS and DECintact proved correct; VAXft fault-tolerant architecture foreshadowed modern high-availability designs., employer_id=DEC, kastner_ro…*

## Entities (36)

- [[DEC|Digital Equipment Corporation]]
- [[ananth-raghavan|Ananth Raghavan]]
- [[ashok-m-joshi|Ashok M. Joshi]]
- [[carlos-alonso|Carlos Alonso]]
- [[carlos-g-borgialli|Carlos G. Borgialli]]
- [[codasyl|Conference on Data Systems Languages (CODASYL)]]
- [[frances-a-habib|Frances A. Habib]]
- [[ibm|International Business Machines Corporation]]
- [[ieee|Institute of Electrical and Electronics Engineers]]
- [[iso|International Organization for Standardization]]
- [[james-e-johnson|James E. Johnson]]
- [[james-m-melvin|James M. Melvin]]
- [[jane-c-blake|Jane C. Blake]]
- [[kenneth-j-omahen|Kenneth J. Omahen]]
- [[mark-w-storm|Mark W. Storm]]
- [[national-semiconductor|National Semiconductor Corporation]]
- [[ncr|NCR Corporation]]
- [[peter-m-spiro|Peter M. Spiro]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[philip-a-bernstein|Philip A. Bernstein]]
- [[robert-v-landau|Robert V. Landau]]
- [[samuel-h-fuller|Samuel H. Fuller]]
- [[sperry-corporation|Sperry Corporation]]
- [[t-k-rengarajan|T. K. Rengarajan]]
- [[thomas-g-speer|Thomas G. Speer]]
- [[thomas-k-rogers|Thomas K. Rogers]]
- [[transaction-processing-performance-council|Transaction Processing Performance Council (TPC)]]
- [[vijay-trehan|Vijay Trehan]]
- [[wael-h-bahaa-el-din|Wael H. Bahaa-El-Din]]
- [[walter-h-kohler|Walter H. Kohler]]

## Technologies (28)

- [[acms|VAX ACMS (Application Control and Management System)]]
- [[ansi-sql|ANSI/ISO SQL]]
- [[debit-credit|DebitCredit Benchmark]]
- [[decdta|DECdta (Digital Distributed Transaction Architecture)]]
- [[decdtm|DECdtm (Digital Distributed Transaction Manager)]]
- [[decforms|DECforms]]
- [[decintact|DECintact (Integrated Application Control)]]
- [[decnet|DECnet]]
- [[dectp|DECtp]]
- [[dna|Digital Network Architecture (DNA)]]
- [[ftss|Fault-tolerant System Services (FTSS)]]
- [[koda|KODA (database kernel)]]
- [[lat|LAT (Local Area Transport)]]
- [[osi-tp|OSI-TP (Open Systems Interconnection Transaction Processing)]]
- [[rdb-vms|VAX Rdb/VMS]]
- [[sna-lu62|IBM SNA LU6.2]]
- [[tpc-benchmark-a|TPC Benchmark A]]
- [[two-phase-commit|Two-Phase Commit Protocol (2PC)]]
- [[vax-4000-300|VAX 4000 Model 300]]
- [[vax-6000|VAX 6000 Series]]
- [[vax-6340|VAX 6340]]
- [[vax-9000|VAX 9000 Model 210]]
- [[vax-dbms|VAX DBMS]]
- [[vax-rms|VAX RMS (Record Management Services)]]
- [[vaxcluster|VAXcluster]]
- [[vaxft-3000|VAXft 3000]]
- [[vms|VMS (Virtual Memory System)]]
- [[x-open-dtp|X/Open Distributed Transaction Processing (DTP)]]

## Key observations (top 25)

- **1991** — DECtp strategic intent: Digital's strategy is to be a leader in transaction processing
- **1991** — DECdta component count: Six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager
- **1991** — Transaction ACID properties defined: Atomicity, Serializability, Durability — the three transaction properties
- **1991** — DECdtm embedding rationale: Embedding transaction semantics in VMS kernel provides consistency, interoperability, and flexibility across all applications not limited to traditional TP
- **1991** — Two-phase commit optimization for VAXcluster: DECdtm uses optimized variant of 2PC; VAXcluster capabilities greatly reduce potential for blocking versus traditional 2PC
- **1991** — ACMS introduction year: 1984
- **1991** — DECintact introduction year: 1988
- **1991** — ACMS vs DECintact distinguishing feature: ACMS uses 4GL task definition language (divide and conquer); DECintact uses 3GL library calls; persistent difference will be different application programming interfaces
- **1991** — DECforms standards compliance: DECforms is first implementation of ANSI/ISO Forms Interface Management Systems standard (CODASYL FIMS)
- **1991** — DECdta standards strategy: DECdta architecture supports X/Open TP Working Group standard APIs and IEEE POSIX; OSI-TP wire protocols for multi-vendor interoperability
- **1991** — DECdtm future standards conformance: Future DECdtm services designed to conform to de facto and international standards for transaction processing; ensures VMS application interoperability with other vendors
- **1991** — TPC Benchmark A — VAX 9000 Model 210 tpsA-Local: 69.4
- **1991** — TPC Benchmark A — VAX 4000 Model 300 tpsA-Local: 21.6
- **1991** — Analytical model accuracy vs measurement — VAX 9000: Model predicted 62-70 TPS (high end 70); actual audited result 69.4 TPS; within 1 percent of high-end prediction
- **1991** — Analytical model accuracy vs measurement — VAX 4000 Model 300: Model predicted 20.8 TPS; actual audited result 21.5 TPS; within 7 percent of model prediction
- **1991** — VAX 9000 CPU utilization at MQTh: >90 percent
- **1991** — KODA group commit: Commit-Lock Design throughput ceiling: 300 TPS
- **1991** — KODA group commit: Commit-Stall Design maximum throughput: 464 TPS
- **1991** — KODA group commit: Willing-to-Wait Design maximum throughput: 500 TPS
- **1991** — Group commit improvement potential: Up to 66 percent improvement in transaction throughput using more efficient grouping designs
- **1991** — VAXft 3000 dual-zone architecture: System comprises two duplicate zones (Zone A and Zone B); each zone is fully functional computer; connected by duplicate cross-link cables; dual-rail + single-rail design
- **1991** — VAXft 3000 fault coverage claim: Designed to recover from any single point of hardware failure; fault tolerance provided transparently for all VMS applications
- **1991** — VAXft 3000 four-phase verification strategy: Phase 1: hardware simulation with fault insertion; Phase 2: hardware verification with system exerciser and fault insertion; Phase 3: system software verification with fault insertion; Phase 4: application verification with fault insertion
- **1991** — VAX Rdb/VMS high-availability mechanisms: Uses snapshot transactions for online backup; parallel transaction recovery; on-line backup, verification and repair utilities; AIJ (after-image journal) files for roll-forward
- **1991** — KODA shared kernel strategy: Rdb/VMS and VAX DBMS share KODA kernel providing transaction capabilities and commit processing; data access independent of data model

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dtj-v03-01-tp-and-fault-tolerant-1991-cf078c' ORDER BY year_observed;
```

