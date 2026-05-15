---
title: "Building Distributed Systems with Midrange Servers"
slug: nti-11-distributed-midrange-servers-1993-dedd19
page_type: study
author: "Peter S. Kastner, John Logan, Thomas Willmott"
date: "1993-08-01"
study_type: market-study
subject_domain: "distributed-computing-midrange"
methodology: "industry-analysis, technology-assessment, vendor-profiling"
importance: high
importance_rationale: "Definitive 1993 guide to the three-tier distributed architecture that became the dominant enterprise computing model; contains specific I/O benchmark comparisons (20-32 MB/sec midrange vs 9.5 MB/sec mainframe) that were influential in enterprise migration decisions."
relevance: medium
relevance_rationale: "The three-tier-plus architecture principles and the distributed systems design patterns described remain foundational; specific vendor products have changed but the architectural logic persists in modern cloud and microservices designs."
prescience: high
prescience_rationale: "Prediction that midrange servers would replace mainframes as production systems proved accurate; forecast of RDBMS as the software glue for distributed systems was borne out by the Oracle/SAP dominance of the late 1990s."
license: CC-BY-4.0
tier: 1
entity_count: 22
tech_count: 20
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Building Distributed Systems with Midrange Servers

> Aberdeen Group presents a comprehensive guide for IS executives on building enterprise distributed systems using midrange servers, covering enterprise requirements, server characteristics, operating systems, and distributed architectures. The study advocates the three-tier-plus topology and demonstrates how midrange servers surpass mainframes in I/O bandwidth, processor performance, and cost, delivering 50% IS cost reductions on average. Aberdeen profiles leading hardware suppliers (HP, NCR, Unisys, Compaq, DEC) and RDBMS vendors (Oracle, Sybase, Informix, Ingres, Software AG) as the foundation for distributed production systems.

**Author:** Peter S. Kastner, John Logan, Thomas Willmott · **Date:** 1993-08-01 · **Type:** market-study
**Importance:** high — *Definitive 1993 guide to the three-tier distributed architecture that became the dominant enterprise computing model; contains specific I/O benchmark comparisons (20-32 MB/sec midrange vs 9.5 MB/sec mainframe) that were influential in enterprise migration decisions.*
**Prescience:** high — *Prediction that midrange servers would replace mainframes as production systems proved accurate; forecast of RDBMS as the software glue for distributed systems was borne out by the Oracle/SAP dominance of the late 1990s.*

## Entities (22)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq|Compaq Computer Corporation]]
- [[digital-equipment-corporation|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[informix|Informix Corporation]]
- [[ingres|Ingres (ASK Group)]]
- [[john-logan|John Logan]]
- [[microsoft|Microsoft Corporation]]
- [[ncr|NCR Corporation]]
- [[novell|Novell, Inc.]]
- [[oracle|Oracle Corporation]]
- [[osf|Open Software Foundation (OSF)]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sco|The Santa Cruz Operation (SCO)]]
- [[software-ag|Software AG]]
- [[sun-microsystems|Sun Microsystems]]
- [[sybase|Sybase, Inc.]]
- [[thomas-willmott|Thomas Willmott]]
- [[transarc|Transarc Corporation]]
- [[unisys|Unisys Corporation]]
- [[usl|Unix System Laboratories (USL)]]

## Technologies (20)

- [[encina|Transarc Encina]]
- [[ethernet|Ethernet LAN]]
- [[fiber-optic|Fiber Optic Networking]]
- [[midrange-server|Midrange Server]]
- [[ncr-top-end|NCR Top End]]
- [[netware|Novell NetWare]]
- [[netware-nlm|Novell NetWare (NLMs)]]
- [[os400|IBM OS/400]]
- [[osf-dce|OSF DCE (Distributed Computing Environment)]]
- [[rdbms|Relational Database Management System (RDBMS)]]
- [[risc|RISC (Reduced Instruction Set Computing)]]
- [[sco-unix|SCO Unix]]
- [[smp|Symmetric Multiprocessing (SMP)]]
- [[sna|IBM SNA (Systems Network Architecture)]]
- [[sql|SQL (Structured Query Language)]]
- [[tcp-ip|TCP/IP]]
- [[tuxedo|USL Tuxedo]]
- [[unix|Unix]]
- [[vms|DEC VMS / OpenVMS]]
- [[windows-nt|Microsoft Windows NT Server]]

## Key observations (top 25)

- **1993** — Midrange server vs mainframe capability: Midrange servers exceed IBM ES/9000 in technological capability and systems reliability
- **1993** — Midrange server user range: 1 to 1,000 active concurrent users; economical from single-employee brokerage to large datacenter
- **1992** — Midrange channel I/O bandwidth vs mainframe: Midrange: 20-32 MB/sec channel I/O; mainframe ESCOM: 9.5 MB/sec
- **1993** — Midrange vs mainframe IS cost reduction: 50% average cost reduction in acquisition, maintenance, and support; application development up to 80% less costly
- **1993** — RDBMS role in midrange servers: RDBMS is an integrable part of midrange server; provides speed of app dev, portability, customization, departmental customization
- **1993** — Midrange security/data integrity vs mainframe and PC LAN: Midrange servers provide greater functionality in security, data integrity, availability than either mainframes or PC LANs
- **1993** — Windows NT Server enterprise readiness: Falls short of enterprise production requirements in 1993; may change within 2-3 years
- **1993** — OSF DCE adoption timeline: Midrange servers will move from TCP/IP to OSF DCE within next several years
- **1998** — OSF DCE adoption — outcome: [UNVERIFIED]
- **1993** — HP position in midrange server market: Dominant revenue supplier of midrange servers for new enterprise applications
- **1993** — NCR position in midrange server market: Market leader for multiuser Intel/Unix midrange servers
- **1993** — Compaq midrange server revenue: $280 million per year in midrange servers based on SCO Unix
- **1993** — DEC VAX/VMS competitive position: Pioneer; standards to which others aspire; but unable to win major new accounts until Alpha/OpenVMS stabilizes
- **1993** — Encina transaction monitor role: New generation of transaction monitors for efficiently integrating OLTP apps, heterogeneous databases, and users
- **1993** — Tuxedo transaction monitor adoption: USL (now Novell division) introducing new generation of transaction monitors to tie islands of disparate databases
- **1993** — Three-tier-plus architecture: Three-tier-plus (client + distributed midrange + central production + analytical) is most successful distributed architecture
- **1993** — RDBMS-of-choice as architecture basis: Enterprises will implement client-server applications based on RDBMS-of-choice rather than any one manufacturer's midrange platform
- **1998** — RDBMS-centric architecture — outcome: [UNVERIFIED]
- **1993** — IBM suggestion to emulate Unisys strategy: If IBM emulated Unisys A-Series strategy it could extend useful life of ES/9000 mainframes
- **1993** — Remote operation control: Today's midrange servers can be remotely backed up, applications propagated, batch scheduled, and crashes recovered without on-site operators
- **1993** — Midrange many-to-everything interoperability: Users connected to midrange server hub have interoperable access to mainframes, PC users, databases worldwide including public data networks
- **1993** — Distributed production system hierarchy prediction: Three classes of midrange servers will be chief building blocks: datacenter application servers, gateway servers, distributed production servers
- **2000** — Distributed production system hierarchy — outcome: [UNVERIFIED]
- **1993** — Mainframe surround strategy benefits: Surround strategy: mainframe as data repository while new OLTP and decision support apps developed on midrange; preserves investment and retrains staff
- **1993** — Multiprocessor-based servers as standard: Advanced servers based upon multiple microprocessor architectures will become standard server platforms of mid-to-late 1990s

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'nti-11-distributed-midrange-servers-1993-dedd19' ORDER BY year_observed;
```

