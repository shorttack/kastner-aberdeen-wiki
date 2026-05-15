---
title: "Software Market Dynamics"
slug: software-market-safegu~1-ea7453
page_type: study
author: "Peter S. Kastner"
date: "1995"
study_type: white-paper
subject_domain: "software-market-analysis"
methodology: "industry-analysis, expert-opinion, trend-analysis"
importance: high
importance_rationale: "Provides a contemporaneous expert analysis of the mid-1990s software market at a pivotal transition point; captures Kastner's original framework (EISM) and predictions about NT, RDBMS, client-server, and OO development that proved remarkably accurate."
relevance: medium
relevance_rationale: "The EISM framework and the structural observations about software adoption velocity remain conceptually relevant to enterprise IT transitions; specific platform predictions are dated but historically instructive."
prescience: high
prescience_rationale: "Multiple predictions proved highly accurate: Windows 95 rapid acceptance, NT sweeping toward the enterprise, ODBMS remaining a niche, data warehousing reaching mainstream, and SAP-class ERP barriers to entry remaining high. OS/2 Warp's failure to recover was also correctly called., OCR quality is poor; obvious OCR errors corrected in abstract and observations (e.g., chawgiwg=changing, thhaw=than); raw text preserved as-is"
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 16
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Software Market Dynamics

> This presentation by Peter S. Kastner, Vice President at Aberdeen Group, surveys mid-1990s software market dynamics across five domains: operating systems, database management, client-server application development, client-server application solutions, and enterprise information systems management. Kastner argues that software is evolving faster than typical enterprises can absorb change, and identifies key market transitions and investment opportunities in areas such as RDBMS growth, Windows NT ascendancy, and EISM consolidation.

**Author:** Peter S. Kastner · **Date:** 1995 · **Type:** white-paper
**Importance:** high — *Provides a contemporaneous expert analysis of the mid-1990s software market at a pivotal transition point; captures Kastner's original framework (EISM) and predictions about NT, RDBMS, client-server, and OO development that proved remarkably accurate.*
**Prescience:** high — *Multiple predictions proved highly accurate: Windows 95 rapid acceptance, NT sweeping toward the enterprise, ODBMS remaining a niche, data warehousing reaching mainstream, and SAP-class ERP barriers to entry remaining high. OS/2 Warp's failure to recover was also correctly called., OCR quality is po…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[ibm|IBM]]
- [[microsoft|Microsoft]]
- [[novell|Novell]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sap|SAP]]

## Technologies (16)

- [[as400|IBM AS/400]]
- [[client-server|Client-Server Computing]]
- [[data-warehouse|Data Warehousing]]
- [[eism|Enterprise Information Systems Management (EISM)]]
- [[mvs|MVS]]
- [[object-cobol|Object COBOL]]
- [[odbc|ODBC]]
- [[odbms|Object-Oriented DBMS]]
- [[orb|Object Request Broker (ORB)]]
- [[os2-warp|IBM OS/2 Warp]]
- [[rdbms|Relational DBMS (generic)]]
- [[sap-r3|SAP R/3]]
- [[unix|UNIX (various)]]
- [[vms|VMS]]
- [[windows-95|Windows 95]]
- [[windows-nt|Windows NT Advanced Server]]

## Key observations (top 25)

- **1995** — Core thesis: software change velocity: Software is changing slower than hardware advances but faster than the typical company can assimilate change
- **1995** — Windows 95 market adoption: Windows 95 will gain rapid acceptance by 1996 after a rocky start
- **1996** — Windows 95 market adoption — outcome: Confirmed — Windows 95 achieved massive adoption; became dominant consumer/business OS
- **1995** — Windows NT enterprise ascendancy: NT Advanced Server sweeps up from workgroup toward enterprise; ISVs eyeing NT as next step
- **2000** — Windows NT enterprise ascendancy — outcome: Confirmed — Windows NT (evolved to 2000/XP/Server) swept enterprise market by early 2000s
- **1995** — OS/2 Warp recovery potential: IBM OS/2 Warp missed the window. Can never recover.
- **2001** — OS/2 Warp recovery — outcome: Not confirmed — OS/2 Warp never recovered; IBM discontinued OS/2 in 2001
- **1995** — UNIX market status: Mature market; variants capable of single enterprise-size applications
- **1995** — Legacy proprietary OS relevance: Old proprietary OS (MVS, VMS) do not matter for new platform decisions
- **1995** — RDBMS attach rate to Unix servers: 9 RDBMS licenses for every 10 multiuser Unix servers sold
- **1995** — RDBMS market temperature: Relational DBMS is hot-hot-hot; existing players get richer
- **1995** — Object-oriented DBMS market window: Pure ODBMS window has closed — relegated to a niche
- **2000** — ODBMS market — outcome: Confirmed — OODBMS remained niche; object-relational features absorbed into mainstream RDBMS (PostgreSQL, Oracle, DB2)
- **1995** — Data warehousing adoption status: Data warehousing is reaching mainstream
- **1995** — Data access strategy debate: Gateways to data sources vs. ODBC as competing approaches
- **1995** — Client-server evolution trajectory: Client-server will evolve to a distributed computing model by year 2000
- **2000** — Client-server → distributed computing — outcome: Confirmed — client-server evolved to n-tier, web, SOA, then cloud/microservices
- **1995** — Object-oriented development readiness: Next big market move is object-oriented development; products in place but ORB infrastructure missing
- **1995** — IS skills gap for OO development: OO development will be very hard for IS to learn
- **1995** — Barriers to entry in ERP market: Barriers to entry for Financials, HR, and high-end manufacturing (SAP) are huge
- **1995** — Client-server vertical app availability: 1995 sees mainstream availability of wide variety of C-S vertical apps
- **1995** — Windows NT as C-S solution platform: Windows NT is now a common option for C-S application solutions
- **1995** — Aberdeen EISM framework definition: EISM consolidates: network management, systems management, operations management, database management
- **1995** — Distributed systems management pain: Distributed systems are rapidly causing administrative chaos; huge interest in alleviating IS pain
- **1995** — Opportunity: software integration services: Software integration services compensate for IS inability to choose/implement

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'software-market-safegu~1-ea7453' ORDER BY year_observed;
```

