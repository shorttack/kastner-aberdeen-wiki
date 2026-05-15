---
title: "AS/400 And NT Server — IBM and Microsoft Working Together To Comprehensively Meet Real User Requirements"
slug: aberdeen-1997-as400-nt-server-ibm-microsoft-working-together
page_type: study
author: "Aberdeen Group"
date: "1997-02-01"
study_type: white-paper
subject_domain: "AS400, NT-Server, IBM, Microsoft, enterprise-computing"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
importance: high
importance_rationale: "This Aberdeen Profile documented a landmark IBM-Microsoft agreement that settled a major mid-1990s platform war and directly shaped enterprise computing for thousands of AS/400 installations; published as the NT vs. AS/400 debate was at its peak, it provided the first independent analysis of the coexistence architecture."
relevance: medium
relevance_rationale: "The AS/400 platform survived and evolved into IBM i / IBM Power Systems — still active in 2025 — making this study's core prediction historically significant; the integration philosophy (coexistence over replacement) remains instructive for modern hybrid-cloud architects."
prescience: high
prescience_rationale: "Aberdeen's prediction that NT on AS/400 would benefit satellite offices and that AS/400 would retain production-application dominance proved correct; the platform survived multiple technology shifts and is still operational 28 years later as IBM i."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 11
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# AS/400 And NT Server — IBM and Microsoft Working Together To Comprehensively Meet Real User Requirements

> Aberdeen Group documents the IBM-Microsoft agreement of late 1996 to integrate NT Server 4.0 into the IBM AS/400 Integrated PC Server, scheduled for general availability in Q1 1998. The study explains the technical architecture (Intel Pentium Pro 200MHz board in AS/400 slot, sharing disk/tape with OS/400), identifies the integration points (ODBC, common user profiles, file system integration), and concludes that both IBM and its AS/400 customers benefit substantially from the arrangement, enabling enterprise users to run AS/400 production applications alongside NT-based desktop applications in a unified, cost-efficient infrastructure.

**Author:** Aberdeen Group · **Date:** 1997-02-01 · **Type:** white-paper
**Importance:** high — *This Aberdeen Profile documented a landmark IBM-Microsoft agreement that settled a major mid-1990s platform war and directly shaped enterprise computing for thousands of AS/400 installations; published as the NT vs. AS/400 debate was at its peak, it provided the first independent analysis of the coe…*
**Prescience:** high — *Aberdeen's prediction that NT on AS/400 would benefit satellite offices and that AS/400 would retain production-application dominance proved correct; the platform survived multiple technology shifts and is still operational 28 years later as IBM i.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[ibm|IBM Corporation]]
- [[lotus-development|Lotus Development Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[novell|Novell Inc.]]

## Technologies (11)

- [[backoffice-suite|Microsoft BackOffice Suite]]
- [[db2-400|DB2/400]]
- [[ibm-as400|IBM AS/400]]
- [[ibm-network-station|IBM Network Station]]
- [[integrated-pc-server|IBM Integrated PC Server (FSIOP)]]
- [[lan-server-400|IBM LAN Server/400]]
- [[lotus-domino|Lotus Domino 4.5]]
- [[novell-netware|Novell NetWare]]
- [[nt-server-40|Microsoft NT Server 4.0]]
- [[odbc|ODBC (Open Database Connectivity)]]
- [[os400|OS/400]]

## Key observations (top 25)

- **1996** — AS/400 vs. NT Server competitive result (1996): AS/400 won hands down vs. NT Server with BackOffice in reliability, scalability, supportability, total cost of acquisition and maintenance, MIS staff costs, ROI, and probable business disruption
- **1997** — NT Server 4.0 on Integrated PC Server availability timeline: NT Server 4.0 scheduled for general availability on AS/400 Integrated PC Server during Q1 1998
- **1998** — NT Server on AS/400 delivery outcome: NT Server 4.0 was delivered on the AS/400 Integrated PC Server as planned in early 1998; IBM fulfilled commitment
- **1997** — Integrated PC Server hardware specifications: Intel Pentium Pro 200MHz processor board with 512MB memory; fits AS/400 slot; disk/tape/I/O provided by AS/400; originally named FSIOP
- **1997** — Integrated PC Server performance impact on AS/400: Users report insignificant degradation in AS/400 production application performance when NOS runs on Integrated PC Server — surpasses expected negative result
- **1997** — NT Server integration limits vs. LAN Server/400 and NetWare: NT Server not as tightly integrated with OS/400 as LAN Server/400 and NetWare; requires own operator console; cannot use AS/400 console
- **1997** — Microsoft NT Server modification policy: Microsoft corporate policy: will not modify NT Server for any hardware manufacturer — NT must be NT regardless of platform
- **1997** — OS/400 and NT Server integration points: Three integration points: ODBC, common user profiles, OS/400 and NT file system integration; print integration in next OS/400 release
- **1997** — Lotus Domino 4.5 native AS/400 availability: Domino 4.5 available on Integrated PC Server May 1997; native mode on AS/400 expected year-end 1997
- **1997** — IBM AS/400 target market for NT integration: Primary target: satellite offices with small number of users; AS/400 for production applications, NT for file/print NOS; eliminates need for separate PC server
- **1997** — AS/400 superiority for transaction processing vs. NT BackOffice: AS/400 has more robust production qualities (reliability, serviceability, availability, security) required for transaction processing; BackOffice on NT not recommended for transaction workloads
- **1997** — Integrated PC Server architectural uniqueness: Unique in server mid-range: no other major supplier designed a system where separate processors handle enterprise production apps vs. file/print services in the same cabinet
- **1997** — AS/400 long-term platform viability: AS/400 will continue to be the production application platform of choice; NT will not replace it for business-critical workloads
- **2025** — AS/400 platform long-term viability outcome: AS/400 survived and evolved: renamed iSeries (2000), System i, then IBM i; still active as IBM Power Systems in 2025 with active installed base globally; Aberdeen's prediction confirmed
- **1997** — IBM Network Computing vision (AS/400 + NT + Network Stations): Combination of AS/400, NT, Office for NT/SmartSuite, and Network Stations will deliver real Network Computing benefits described by IBM senior executives
- **2002** — IBM Network Station outcome: IBM Network Station was discontinued by 2001 as thin-client market failed to materialize at predicted scale; Network Computing vision partially delivered but Network Stations themselves were market failures
- **1997** — AS/400 evolutionary history: AS/400 has 20+ year history; started as System/3; major architectural changes resulted in product name changes through progressively newer models
- **1997** — NOS options for AS/400 Integrated PC Server: Three NOS options: Novell NetWare, IBM LAN Server/400, and Microsoft NT Server; IBM proves ability to open AS/400 to customer requirements
- **1997** — IBM MIS cost reduction through AS/400+NT integration: MIS can manage relatively complex user environment (AS/400 + NT + intranet) at significantly lower cost than today's separate PC LAN and AS/400 operations
- **1997** — DB2/400 to NT application data transfer: Users can transfer data from DB2/400 to NT applications via ODBC; useful for mass mailings, customized presentations from customer databases

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1997-as400-nt-server-ibm-microsoft-working-together' ORDER BY year_observed;
```

