---
title: "DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988)"
slug: dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e
page_type: study
author: "Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI)"
date: "1988-03-04"
study_type: internal-engineering-memo
subject_domain: "VAXcluster-OLTP-architecture"
methodology: "engineering-analysis-memo"
importance: high
importance_rationale: "Captures DEC's frank engineering self-assessment of the VAXcluster's main OLTP weakness — distributed lock manager overhead under cross-branch Debit-Credit load — and the absence of 2PC for formal databases. This is the engineering reality behind the marketing claims and a key input into Aberdeen's later analyses of DEC's TP positioning."
relevance: high
relevance_rationale: "Zahavi was on the same Kohler/Hsu memo distribution as Kastner and worked in the same MR01-1/A65 facility. This memo is a key data point in the OLTP-performance discourse that shaped Kastner's subsequent Aberdeen TP analysis and TPC-A audit work. Direct evidence of the DEC DLM constraint that Aberdeen later flagged as a barrier to DEC's TP scaling."
prescience: medium
prescience_rationale: "Anticipates the broader industry shift to shared-nothing partitioned architectures (Tandem, Teradata, later cloud-native databases) for transaction workloads where shared-disk lock-coordination becomes a scaling cliff. Phil Bernstein's 2PC concerns directly anticipate the X/Open XA transaction model standardized 1991-1994."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 8
obs_count: 8
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988)

> Internal Digital Equipment Corporation interoffice memorandum dated 4-March-1988 by Bill Zahavi (TP Systems Performance Analysis, MR01-1/A65, DTN 297-7795, HYPER::BZAHAVI) addressed to @DC_VAXCLUSTER and @GROUP, on implementing the Debit-Credit benchmark on VAXclusters. Identifies the Distributed Lock Manager (DLM) as the major obstacle: only one cluster member owns locks for a given file, and the Debit-Credit specification's requirement that 15% of teller activity address other-branch accounts forces inter-node CI bus traffic. Distinguishes flat-file (RMS, Hash) from formal-database (DBMS, Rdb) implementations. Discusses partitioning strategies (cluster-member-A owns files-A, etc.) and the asymmetric statistics: 7.5% of cross-branch traffic lands on a different cluster member's locks for a 2-member cluster. Acknowledges that DECintact works only with flat files (RMS, Hash) while ACMS works best with DBMS and Rdb. Proposes that without 2-Phase Commit (2PC), only certain types of applications can be distributed using formal databases — explicitly referencing Phil Bernstein's prior memo. Closes by calling for cross-functional cooperation between TP, Databases, and VMS groups for both short and long-term solutions, and asks the document be treated as a 'living document.' Direct technical companion to the Kohler/Hsu guidelines (Study 1) and the broader DEC OLTP performance-engineering corpus.

**Author:** Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI) · **Date:** 1988-03-04 · **Type:** internal-engineering-memo
**Importance:** high — *Captures DEC's frank engineering self-assessment of the VAXcluster's main OLTP weakness — distributed lock manager overhead under cross-branch Debit-Credit load — and the absence of 2PC for formal databases. This is the engineering reality behind the marketing claims and a key input into Aberdeen's…*
**Prescience:** medium — *Anticipates the broader industry shift to shared-nothing partitioned architectures (Tandem, Teradata, later cloud-native databases) for transaction workloads where shared-disk lock-coordination becomes a scaling cliff. Phil Bernstein's 2PC concerns directly anticipate the X/Open XA transaction model…*

## Entities (4)

- [[bill-zahavi|Bill Zahavi]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[phil-bernstein|Philip A. Bernstein]]
- [[tandem-computers|Tandem Computers]]

## Technologies (8)

- [[acms|ACMS (Application Control Management System)]]
- [[ci-bus|CI Bus (Computer Interconnect)]]
- [[debit-credit-benchmark|Debit-Credit Benchmark]]
- [[decintact|DECintact]]
- [[distributed-lock-manager|VMS Distributed Lock Manager (DLM)]]
- [[rms|RMS (Record Management Services)]]
- [[two-phase-commit|Two-Phase Commit (2PC)]]
- [[vax-cluster|VAXcluster]]

## Key observations (top 25)

- **1988** — constraint_severity: major-obstacle-for-VAXcluster-Debit-Credit
- **1988** — cross_branch_traffic_pct: 15
- **1988** — cross_node_traffic_pct_2_member: 7.5
- **1988** — limitation: flat-files-only-RMS-Hash
- **1988** — availability: not-available-in-DEC-stack
- **1988** — router_overhead_treatment: excluded-from-Style-3
- **1988** — cross_group_coordination: TP-Databases-VMS
- **1988** — node_and_facility: HYPER-BZAHAVI-MRO1-1-A65

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e' ORDER BY year_observed;
```

