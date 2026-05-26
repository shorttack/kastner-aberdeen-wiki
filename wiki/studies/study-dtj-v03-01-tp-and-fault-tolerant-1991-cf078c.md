---
title: "Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)"
slug: "study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c"
page_type: "study"
tags: ["type/study", "collection/employer-record"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "dtj-v03-01-tp-and-fault-tolerant-1991-cf078c"
author: "Digital Equipment Corporation"
date: "1991-01-01"
pub_year: 1991
type: "employer-record"
subject_domain: "transaction-processing"
methodology: "document-review, industry-analysis"
source_file: "dtj-v03-01-1991.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)

> This issue of the Digital Technical Journal presents eight peer-reviewed technical papers documenting DEC's complete distributed transaction processing stack, including the DECdta architecture, ACMS and DECintact TP monitors, DECdtm kernel-level transaction management, TPC Benchmark A performance results, database availability strategies, optimized commit protocols, and VAXft 3000 fault-tolerant system verification. The papers collectively define DEC's strategy to lead the distributed TP market through an integrated, standards-aligned, client/server architecture. Formal TPC Benchmark A results are disclosed: 69.4 tpsA-Local on VAX 9000 Model 210 and 21.6 tpsA-Local on VAX 4000 Model 300.


_Published 1991, author **Digital Equipment Corporation**, type **employer-record**._


## Top observations

- Digital's strategy is to be a leader in transaction processing
- Six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager
- Atomicity, Serializability, Durability — the three transaction properties
- Embedding transaction semantics in VMS kernel provides consistency, interoperability, and flexibility across all applications not limited to traditional TP
- DECdtm uses optimized variant of 2PC; VAXcluster capabilities greatly reduce potential for blocking versus traditional 2PC
- 1984
- 1988
- ACMS uses 4GL task definition language (divide and conquer); DECintact uses 3GL library calls; persistent difference will be different application programming interfaces
- DECforms is first implementation of ANSI/ISO Forms Interface Management Systems standard (CODASYL FIMS)
- DECdta architecture supports X/Open TP Working Group standard APIs and IEEE POSIX; OSI-TP wire protocols for multi-vendor interoperability
- Future DECdtm services designed to conform to de facto and international standards for transaction processing; ensures VMS application interoperability with other vendors
- 69.4
- 21.6
- Model predicted 62-70 TPS (high end 70); actual audited result 69.4 TPS; within 1 percent of high-end prediction
- Model predicted 20.8 TPS; actual audited result 21.5 TPS; within 7 percent of model prediction
- >90 percent
- 300 TPS
- 464 TPS
- 500 TPS
- Up to 66 percent improvement in transaction throughput using more efficient grouping designs
- System comprises two duplicate zones (Zone A and Zone B); each zone is fully functional computer; connected by duplicate cross-link cables; dual-rail + single-rail design
- Designed to recover from any single point of hardware failure; fault tolerance provided transparently for all VMS applications
- Phase 1: hardware simulation with fault insertion; Phase 2: hardware verification with system exerciser and fault insertion; Phase 3: system software verification with fault insertion; Phase 4: application verification with fault insertion
- Uses snapshot transactions for online backup; parallel transaction recovery; on-line backup, verification and repair utilities; AIJ (after-image journal) files for roll-forward
- Rdb/VMS and VAX DBMS share KODA kernel providing transaction capabilities and commit processing; data access independent of data model
