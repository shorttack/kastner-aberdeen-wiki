---
title: "Open Online Transaction Processing: An Enterprise Manager's Guide — Korean (Hangul) Translation, c. 1991/1992"
slug: aberdeen-open-oltp-enterprise-managers-k-3fc536
page_type: study
author: "Peter S. Kastner (Aberdeen Group); Korean translation by NCR Korea (publisher)"
date: "1991"
study_type: translated-white-paper
subject_domain: "open-OLTP/enterprise-IS-strategy/Korean-localization"
methodology: "translation-reconciliation-of-Aberdeen-white-paper"
importance: high
importance_rationale: "Direct evidence that the Aberdeen / Kastner Open OLTP white paper was translated and distributed in Korean by NCR for the Korean enterprise IS audience; pairs with the English-fragment study from Batch 22 to give the archive a complete bilingual record of the seminal 1991-1992 Aberdeen Open OLTP corpus."
relevance: high
relevance_rationale: "Foundational Kastner-authored Aberdeen study in Korean translation; pairs with the English fragments archive from Batch 22 and the Norway 1992 seminar (Batch 23) that delivers the same content in Norwegian/English to a European audience. Together these three artifacts document the international rollout of Kastner's Open OLTP thesis through NCR's 1991-1992 sponsored channel."
prescience: high
prescience_rationale: "Anticipates the global adoption of open-standards transaction processing (XA, X/Open DTP) that became universal by the late 1990s; predicts that distributed networked computing with heterogeneous RDBMS interoperability (today's microservices + polyglot persistence pattern) would replace proprietary CICS/IMS stacks; the 'most OLTP apps need ≤12 TPS' insight reframed system sizing for the commodity-x86 era and cloud-native era. Also anticipates the international consumption of analyst research as…"
license: CC-BY-4.0
tier: 1
entity_count: 16
tech_count: 12
obs_count: 13
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Open Online Transaction Processing: An Enterprise Manager's Guide — Korean (Hangul) Translation, c. 1991/1992

> Korean-language (Hangul) translation of the Aberdeen Group white paper 'Open Online Transaction Processing: An Enterprise Manager's Guide' authored by Peter S. Kastner (and developed/funded by Aberdeen and its sponsor company, per the bilingual title-page note). This is the international localization companion to the English-language Aberdeen Open OLTP study archived in Batch 22 (slug aberdeen-open-online-transaction-process). Four source files were reconciled per user instruction ('reconcile translations... pick the best or merge to fix artifacts'): (1) NCR-Open-OLTP-1991-Hangul-Korean-8.docx — primary Korean original (89,020 bytes); (2) NCR-Open-OLTP-Korea-1991-9.docx — duplicate of the same Hangul original (89,437 bytes; trivial differences); (3) NCR-Korea-1991-Google-Translate-3.docx — clean Korean→English Google Translate rendering used as the primary English text in this archive; (4) NCR-Korea-1991-poor-translation-4.docx — older/poor translation with severe character-encoding artifacts ('0=11', '0？611 01.7？'), retained for completeness but not authoritative. The cleanest English text (file #3) preserves the full Aberdeen argument: Open OLTP definition (computer mechanism that changes the state of a business in real time while using industry standards), six standards bodies (ISO/X-Open/POSIX/SQL-Access/OSF DCE/Unix International), ACID test components, six executive checklist items, fifteen-stage life-cycle model, and the Aberdeen claim that >90% of OLTP applications ne…

**Author:** Peter S. Kastner (Aberdeen Group); Korean translation by NCR Korea (publisher) · **Date:** 1991 · **Type:** translated-white-paper
**Importance:** high — *Direct evidence that the Aberdeen / Kastner Open OLTP white paper was translated and distributed in Korean by NCR for the Korean enterprise IS audience; pairs with the English-fragment study from Batch 22 to give the archive a complete bilingual record of the seminal 1991-1992 Aberdeen Open OLTP cor…*
**Prescience:** high — *Anticipates the global adoption of open-standards transaction processing (XA, X/Open DTP) that became universal by the late 1990s; predicts that distributed networked computing with heterogeneous RDBMS interoperability (today's microservices + polyglot persistence pattern) would replace proprietary…*

## Entities (16)

- [[aberdeen-group|Aberdeen Group]]
- [[apple-computer|Apple Computer]]
- [[att-corp|AT&T Corporation]]
- [[ibm|IBM Corporation]]
- [[informix-software|Informix Software]]
- [[intel-corporation|Intel Corporation]]
- [[iso-org|International Organization for Standardization (ISO)]]
- [[ncr-corporation|NCR Corporation]]
- [[ncr-korea|NCR Korea]]
- [[open-software-foundation|Open Software Foundation (OSF)]]
- [[oracle-corporation|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sybase-inc|Sybase, Inc.]]
- [[tpc-org|Transaction Processing Performance Council (TPC)]]
- [[unix-international|Unix International]]
- [[x-open-company|X/Open Company Ltd.]]

## Technologies (12)

- [[acid-properties|ACID Properties (Atomicity, Consistency, Isolation, Durability)]]
- [[client-server-computing|Client-Server Computing]]
- [[downsizing|Downsizing/Rightsizing]]
- [[oltp-traditional|Traditional OLTP (proprietary)]]
- [[open-oltp|Open Online Transaction Processing (Open OLTP)]]
- [[osf-dce|OSF Distributed Computing Environment (DCE)]]
- [[posix-1003|POSIX (IEEE 1003)]]
- [[relational-database|Relational Database Management Systems (RDBMS)]]
- [[sql-standard|SQL (Structured Query Language) Standard]]
- [[tp-monitor|Transaction Processing Monitor]]
- [[unix-intl-atlas|Unix International ATLAS Architecture]]
- [[x-open-dtp|X/Open Distributed Transaction Processing (DTP)]]

## Key observations (top 25)

- **1991** — Open OLTP definition: computer mechanism that changes the state of a business in real time while using industry standards that support interoperability across diverse computing systems
- **1991** — Application TPS distribution: >90% of OLTP applications need <=12 transactions per second
- **1991** — RDBMS price-performance vs mainframe: up to 5x cheaper per transaction
- **1991** — ACID test components: Atomicity / Consistency / Isolation / Durability
- **1991** — Six standards bodies for Open OLTP: ISO / X-Open / POSIX / SQL Access Group / OSF DCE / Unix International
- **1991** — Executive checklist: leadership / qualified technical staff / productive tools / external experts / realistic funded plan / goal-oriented evaluation
- **1991** — Buyer key considerations: openness / reliability / compatibility / functionality / supplier-relationships
- **1991** — Maturity assessment: Open OLTP technically mature enough for serious business consideration
- **1991** — Open OLTP three pillars: client-server / distributed databases / desktop utilization / heterogeneous interoperability
- **1991** — NCR Korea sponsorship: Hangul translation distributed by NCR Korea
- **1991** — Author identification: Peter S. Kastner, Aberdeen Group, Inc.
- **1992** — Translation reconciliation: Google Translate (clean) chosen as primary English text; older translation retained but unreliable
- **1991** — Universality claim: no business too big or too small to benefit from Open OLTP

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-open-oltp-enterprise-managers-k-3fc536' ORDER BY year_observed;
```

