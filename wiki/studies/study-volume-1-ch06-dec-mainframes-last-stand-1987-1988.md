---
title: "Chapter 6: Digital Equipment Corporation — The Mainframe's Last Stand (1987–1988)"
slug: "study-volume-1-ch06-dec-mainframes-last-stand-1987-1988"
page_type: "study"
tags: ["type/study", "collection/memoir"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "volume-1-ch06-dec-mainframes-last-stand-1987-1988"
author: "Peter S. Kastner"
date: "2026-05-14"
pub_year: 2026
type: "memoir"
subject_domain: "memoir/volume-1"
methodology: "oral-history"
source_file: "MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 6: Digital Equipment Corporation — The Mainframe's Last Stand (1987-1988))"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Chapter 6: Digital Equipment Corporation — The Mainframe's Last Stand (1987–1988)

> Kastner recounts his 1987–1988 tenure at Digital Equipment Corporation as a Marketing Executive, where he orchestrated the DECtp (DEC Transaction Processing) launch and a covert benchmark of IBM's 3090 mainframe that exposed the 'SNA Tax' — massive hidden overhead in IBM's communications stack. He also describes his pivotal role in founding the Transaction Processing Performance Council (TPC), which established independent, audited, industry-standard OLTP benchmarks. The chapter closes with Kastner's observation that DEC, having beaten the mainframe on price-performance, was itself soon to be surpassed by x86 servers using the very same TPC benchmarks.


_Published 2026, author **Peter S. Kastner**, type **memoir**._


## Top observations

- Arrived at DEC in late 1987 carrying intimate technical knowledge from six years at Stratus and a freshly completed ghost-written Yankee Group report.
- Title was Marketing Executive — DEC's highest-level individual contributor in marketing.
- Assignment from Bill Steul's Corporate Systems group: 'look around DEC for things that needed to be done to improve the enterprise position.'
- Online Transaction Processing was 'still an IBM mainframe franchise' for banking, insurance, retail, and financial services as of 1987.
- DEC had the VAX architecture, a genuine relational database in Rdb, and a transaction monitor — but lacked a verifiable competitive story.
- 'The Future of Transaction Processing' published by Yankee Group in January 1987.
- Hired by John Logan at Yankee Group for $8,000 and a month of late evenings to ghostwrite 'The Future of Transaction Processing.'
- Former Prime Computer colleague who moved to Yankee Group; commissioned Kastner's ghost-written report on transaction processing.
- Moore's Law was meeting economics of departmental transaction processing; multiprocessor Intel 386 systems were appearing; mainframe cost-per-transaction advantage was evaporating.
- Mainframe displacement was 'not a matter of whether but when — and when was the early 1990s.'
- DECtp launch was eight months out when Kastner arrived at DEC; he became apparent Chair of the DECtp Task Force.
- Kastner networked furiously across ten DEC product groups to build the DECtp story; title of Task Force Chair never received in writing.
- DEC's hand was stronger than team realized: multiprocessor VAX 8200 + transaction-friendly Rdb + acquired OLTP transaction monitor.
- The SNA Tax: hidden overhead in IBM's mainframe architecture costing enterprise customers millions of dollars they couldn't see.
- DECtp marketing launch budget (excluding product R&D) totaled approximately $2 million — described as 'staggering' for a marketing program in 1988.
- Blind benchmark conducted through a CICS consulting firm in Westwood, Massachusetts using the Cullinet mainframe data center.
- John Cullinane, known to Kastner from PHI days, 'had built one of the first major commercial software companies.' The Route 128 world was always smaller than it appeared.
- Objective: measure IBM's highest possible throughput on a 3090 running DB2, then compare head-to-head against a DEC VAX under identical constraints.
- IBM's own systems analysts brought in under contract; told in writing IBM was to provide all reasonable services and tuning to maximize throughput; unaware DEC was the client.
- Simulates bank account transaction processing; measures TPS with 100 virtual terminals per claimed 1 TPS; requires 10,000 virtual users for 100 TPS claim; response time under one second.
- Called the 'four-minute mile' of enterprise computing; every serious OLTP vendor obsessed with it; single test score could define competitive position for years.
- Kastner had extensive debit-credit benchmark experience from Stratus vs. Tandem competitive engagements.
- IBM 3090-400 as System Under Test; IBM 3090-200 as load driver — two of IBM's largest mainframes in the same room, running tests at night and on weekends.
- More than one full 3090 CPU-second required to log in a single 3270 terminal via VTAM.
- 100 TPS benchmark required 10,000 virtual terminals × 1 CPU-second = 10,000 CPU-seconds of session overhead; over an hour of clock time on a 4-processor 3090-400 before a single transaction.
