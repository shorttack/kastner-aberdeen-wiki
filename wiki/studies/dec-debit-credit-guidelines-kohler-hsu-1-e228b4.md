---
title: "DEC Proposed Debit-Credit Benchmark Guidelines (Kohler/Hsu, Dec 1987)"
slug: dec-debit-credit-guidelines-kohler-hsu-1-e228b4
page_type: study
author: "Walt Kohler & Yun-Ping Hsu, DEC HPS/OLTP Systems Performance Analysis Group"
date: "1987-12-21"
study_type: internal-engineering-memo
subject_domain: "OLTP-benchmark-methodology"
methodology: "engineering-guidelines-document"
importance: high
importance_rationale: "Insider engineering document showing DEC's approach to benchmark methodology 8 months before TPC was founded. Names 11 OLTP performance engineers including Peter Kastner, anchoring his presence in DEC's TP performance community during the formative period. Foundational artifact for understanding the pre-TPC era of vendor-defined benchmark interpretation."
relevance: high
relevance_rationale: "Direct evidence of Kastner's DEC-employer-era role in OLTP/TP performance work. Distribution list places him alongside the engineers (Bhandarkar, Hsu, Kohler, Zahavi) who shaped DEC's transaction-processing benchmark practice. Companion to the Kastner-authored 1988 Primer (Study 4)."
prescience: high
prescience_rationale: "The eleven-component decomposition (response time, database size, transaction mix verification, etc.) anticipates TPC-A's structure released August 1989. The concerns about ambiguous specs, partition tricks, and vendor interpretations directly motivated the formal TPC standardization effort."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 9
obs_count: 11
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# DEC Proposed Debit-Credit Benchmark Guidelines (Kohler/Hsu, Dec 1987)

> Internal Digital Equipment Corporation HPS/OLTP Systems Performance Analysis Group memorandum dated 21-Dec-1987 by Walt Kohler and Yun-Ping Hsu, addressed to a distribution list including Dileep Bhandarkar, Bhagyam Moses, Rudy Downs, Joe Marconis, Christopher Marshall, Jim Sasena, Fred Howell, Mike Dempsey, Peter Kastner (HPS::KASTNER), Bill Zahavi, and Linda Wright. Document marked COMPANY CONFIDENTIAL. Provides DEC-internal proposed guidelines for implementing and reporting the Debit-Credit benchmark. Summarizes the 1985 DATAMATION Anon Et Al specification, divides Debit-Credit into eleven components, and for each component lists Specification, Interpretations, Implementation Guidelines, and Compliance requirements. Components include: Application Implementation Language, Terminal Communications (X.25 block-mode vs. character-mode terminals with FEPs), database operations, response-time measurement (95th percentile/1 second), database size, transaction-mix and verification reporting. Includes ASCII diagrams of three implementation configurations: character-mode terminals without FEPs, character-mode with FEPs in machine room, and remote FEPs (e.g. MicroVAX per branch). Cites Trehan (1986), Serlin (1986), and Tandem (1987) prior memos. Establishes baseline DEC reporting standard before the public Transaction Processing Performance Council (TPC) was founded in August 1988.

**Author:** Walt Kohler & Yun-Ping Hsu, DEC HPS/OLTP Systems Performance Analysis Group · **Date:** 1987-12-21 · **Type:** internal-engineering-memo
**Importance:** high — *Insider engineering document showing DEC's approach to benchmark methodology 8 months before TPC was founded. Names 11 OLTP performance engineers including Peter Kastner, anchoring his presence in DEC's TP performance community during the formative period. Foundational artifact for understanding the…*
**Prescience:** high — *The eleven-component decomposition (response time, database size, transaction mix verification, etc.) anticipates TPC-A's structure released August 1989. The concerns about ambiguous specs, partition tricks, and vendor interpretations directly motivated the formal TPC standardization effort.*

## Entities (11)

- [[bill-zahavi|Bill Zahavi]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[dileep-bhandarkar|Dileep Bhandarkar]]
- [[ibm|IBM Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[rudy-downs|Rudy Downs]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]
- [[transaction-processing-performance-council|Transaction Processing Performance Council (TPC)]]
- [[walt-kohler|Walt Kohler]]
- [[yun-ping-hsu|Yun-Ping Hsu]]

## Technologies (9)

- [[acms|ACMS (Application Control Management System)]]
- [[debit-credit-benchmark|Debit-Credit Benchmark]]
- [[dec-dbms|VAX DBMS]]
- [[decintact|DECintact]]
- [[ibm-3270|IBM 3270 block-mode terminal family]]
- [[microvax|MicroVAX]]
- [[vax-cluster|VAXcluster]]
- [[vax-rdb|VAX Rdb/VMS]]
- [[x25-protocol|X.25 packet-switching protocol]]

## Key observations (top 25)

- **1987** — components_count: 11
- **1987** — response_time_pct1sec: 95th-percentile-1-second
- **1987** — memo_recipient_node: HPS::KASTNER
- **1987** — marking: COMPANY CONFIDENTIAL
- **1987** — role: co-author
- **1987** — role: co-author
- **1985** — specification_publication: DATAMATION-April-1985-Anon-et-al
- **1987** — tpc_founding_lead_time_months: 8
- **1987** — role: branch-office-FEP
- **1987** — constraint: distributed-lock-manager-cross-branch-traffic
- **1987** — use_case: formal-database-debit-credit

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dec-debit-credit-guidelines-kohler-hsu-1-e228b4' ORDER BY year_observed;
```

