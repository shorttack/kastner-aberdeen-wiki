---
title: "Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)"
slug: "study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c"
page_type: "study"
tags: ["type/study", "collection/employer-record"]
tier: 1
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
study_prescience_enum: "medium"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 2.02
prescience_obs_count: 40
---

# Digital Technical Journal — Transaction Processing, Databases, and Fault-tolerant Systems (Volume 3, Number 1, Winter 1991)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.80 over 40 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.65 over 40 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> This issue of the Digital Technical Journal presents eight peer-reviewed technical papers documenting DEC's complete distributed transaction processing stack, including the DECdta architecture, ACMS and DECintact TP monitors, DECdtm kernel-level transaction management, TPC Benchmark A performance results, database availability strategies, optimized commit protocols, and VAXft 3000 fault-tolerant system verification. The papers collectively define DEC's strategy to lead the distributed TP market through an integrated, standards-aligned, client/server architecture. Formal TPC Benchmark A results are disclosed: 69.4 tpsA-Local on VAX 9000 Model 210 and 21.6 tpsA-Local on VAX 4000 Model 300.


_Published 1991, author **Digital Equipment Corporation**, type **employer-record**._


## Top observations

- TPC-A represents limited class of applications; additional benchmarks representing broader range of commercial applications expected to be standardized by TPC in coming years `[ps=5]`
- DEC acquired by Compaq in 1998; did not achieve stated goal of TP market leadership; Oracle, IBM, and Tandem/HP dominated TP markets through 1990s; actual-outcome for OBS-033 `[ps=5]`
- Six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager `[ps=4]`
- Uses snapshot transactions for online backup; parallel transaction recovery; on-line backup, verification and repair utilities; AIJ (after-image journal) files for roll-forward `[ps=4]`
- When a node fails, another node detects failure and rolls back lost transactions from failed node; database available as soon as recovery complete `[ps=4]`
- ACMS concentrates security on back-end using VMS ACLs on tasks; SYSUAF-based login; execution controller with access-control-list checking per task; dynamic application changes without stopping work `[ps=4]`
- User security profiles, terminal security profiles, and GEOG attribute provide geographic entitlement: certain functions accessible only from specific terminals (e.g., bank officer sensitive functions only at home office) `[ps=4]`
- 90 percent of transactions must have response time less than 2 seconds; end-to-end response time (user at terminal); maximum qualified throughput (MQTh) is key metric `[ps=4]`
- Key requirements for 100-year mean time between failures: software-fault containment using processes and software-fault masking using process checkpointing and transactions `[ps=4]`
- For short TP transactions (modify 1 record): commit processing represents 36 percent of total transaction duration; for batch transactions (modify 500 records): commit processing only 0.2 percent `[ps=4]`
- Many older TP systems centralized and tied to particular vendor; as expansion continues beyond geographic boundaries, centralized single-vendor TP systems less able to offer needed flexibility `[ps=4]`
- Atomicity, Serializability, Durability — the three transaction properties `[ps=3]`
- DECdtm uses optimized variant of 2PC; VAXcluster capabilities greatly reduce potential for blocking versus traditional 2PC `[ps=3]`
- ACMS uses 4GL task definition language (divide and conquer); DECintact uses 3GL library calls; persistent difference will be different application programming interfaces `[ps=3]`
- DECdta architecture supports X/Open TP Working Group standard APIs and IEEE POSIX; OSI-TP wire protocols for multi-vendor interoperability `[ps=3]`
- Future DECdtm services designed to conform to de facto and international standards for transaction processing; ensures VMS application interoperability with other vendors `[ps=3]`
- System comprises two duplicate zones (Zone A and Zone B); each zone is fully functional computer; connected by duplicate cross-link cables; dual-rail + single-rail design `[ps=3]`
- Phase 1: hardware simulation with fault insertion; Phase 2: hardware verification with system exerciser and fault insertion; Phase 3: system software verification with fault insertion; Phase 4: application verification with fault insertion `[ps=3]`
- Communication managers separated from transaction managers; communication manager propagates 2PC messages to remote nodes; enables multiple commit protocols (IBM SNA LU6.2, OSI-TP) simultaneously `[ps=3]`
- DECintact used in banking: data entry clerks, verify/repair application, Fedwire Xmt queue sending to Federal Reserve; demonstrates exactly-once semantics for distributed queues `[ps=3]`
- Set of common features shared by both monitors growing with latest releases; external convergence fostered by internal convergence sharing underlying code; investment in either monitor protected `[ps=3]`
- Digital's strategy is to be a leader in transaction processing `[ps=2]`
- Embedding transaction semantics in VMS kernel provides consistency, interoperability, and flexibility across all applications not limited to traditional TP `[ps=2]`
- This combination of architecture, software, hardware technology, and support for emerging industry standards places Digital in excellent position to become industry leader for distributed portable transaction processing systems `[ps=1]`
- 1984 `[ps=0]`
