---
title: "Oracle's Network Computing Architecture"
slug: aberdeen-1996-oracle-network-computing-architecture
page_type: study
author: "Aberdeen Group"
date: "1996-10-01"
study_type: market-study
subject_domain: "enterprise-software, distributed-computing, internet-architecture, RDBMS"
methodology: "industry-analysis, competitive-profiling, expert-opinion, document-review"
importance: high
importance_rationale: "Oracle's NCA represented a defining moment in enterprise middleware strategy as the industry transitioned from client-server to Internet architectures; Aberdeen's endorsement of NCA over competing approaches from Microsoft and others carried significant weight with enterprise IT buyers."
relevance: medium
relevance_rationale: "The cartridge/component model anticipated modern microservices and API-based architectures; Oracle's Universal Server became the foundation for Oracle Database which remains active, though NCA-specific cartridge mechanisms are long obsolete."
prescience: high
prescience_rationale: "Aberdeen correctly predicted Oracle would dominate enterprise internet database strategy and that component-based architecture would become the standard; Oracle remains a dominant enterprise database and application platform 30 years later."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 10
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Oracle's Network Computing Architecture

> Aberdeen Group evaluates Oracle's Network Computing Architecture (NCA), a comprehensive framework integrating multi-tier client-server, Internet, and distributed-object technologies through a 'cartridge' component model and Inter-Cartridge Exchange (ICX) middleware based on CORBA. The study concludes that NCA is not a 'marketecture' but a substantive extension of proven Oracle products providing a least-cost migration path to mission-critical 21st-century transaction processing, and recommends ISVs and enterprise IS factor it into their 1-2 year technology strategies.

**Author:** Aberdeen Group · **Date:** 1996-10-01 · **Type:** market-study
**Importance:** high — *Oracle's NCA represented a defining moment in enterprise middleware strategy as the industry transitioned from client-server to Internet architectures; Aberdeen's endorsement of NCA over competing approaches from Microsoft and others carried significant weight with enterprise IT buyers.*
**Prescience:** high — *Aberdeen correctly predicted Oracle would dominate enterprise internet database strategy and that component-based architecture would become the standard; Oracle remains a dominant enterprise database and application platform 30 years later.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[hp|Hewlett-Packard (HP)]]
- [[microsoft|Microsoft Corporation]]
- [[netscape-communications|Netscape Communications]]
- [[object-management-group|Object Management Group (OMG)]]
- [[oracle-corporation|Oracle Corporation]]

## Technologies (10)

- [[activex-com|ActiveX / COM (Microsoft)]]
- [[corba|CORBA (Common Object Request Broker Architecture)]]
- [[java|Java / JavaScript]]
- [[netsolutions|Oracle NetSolutions]]
- [[oracle-designer-2000|Oracle Designer/2000]]
- [[oracle-developer-2000|Oracle Developer/2000]]
- [[oracle-enterprise-manager|Oracle Enterprise Manager]]
- [[oracle-nca|Oracle Network Computing Architecture (NCA)]]
- [[oracle-universal-server|Oracle Universal Server (RDBMS)]]
- [[oracle-web-server|Oracle Web Server / Web Request Broker]]

## Key observations (top 25)

- **1996** — NCA architectural strategy: Integrate multi-tier client-server + Internet + distributed-object via unified cartridge model
- **1996** — NCA assessment: 'marketecture' test: Not a marketecture; straightforward extension of proven Oracle products
- **1996** — Oracle Universal Server RDBMS breadth: Unbeaten RDBMS breadth: parallel scalability, replication, multimedia data types
- **1996** — NCA component: Client Cartridges: Deploy on client platforms supporting Windows and Internet environments
- **1996** — NCA component: Application Server Cartridges: Enterprise-scale web-enabled application components; bypass CGI bottlenecks
- **1996** — NCA component: Database Server Cartridges: Database-level cartridges with direct access to Universal Server stored procedures and query optimizer
- **1996** — ICX / CORBA ORB role: Location-independent component invocation across platforms; bridges Oracle NCA to Microsoft COM
- **1996** — COM bridge in NCA: ICX provides bridges to Microsoft COM; supports both major ORB approaches
- **1996** — Java integration in NCA: Java integrated into CORBA; developers can use Java/JavaScript alongside C/C++, VB, PL/SQL
- **1996** — Developer/2000 web enablement: Legacy client-server apps written in Developer/2000 can be translated to Internet with little effort
- **1996** — Enterprise Manager SNMP integration: Integrates with HP OpenView for global systems administration
- **1996** — NCA adoption recommendation: Aberdeen recommends ISVs and IS not only prototype but factor NCA into strategies for next 1-2 years
- **1996** — NCA cartridge market prediction: Thriving market in vertical/functional cartridges expected within next year
- **1996** — Oracle roadmap: COM tighter integration: Aberdeen anticipates Oracle will integrate Microsoft COM more tightly over 1-2 years
- **1996** — Oracle roadmap: Developer/2000 cartridge tools: More advanced tools within Developer/2000 for creating and distributing cartridges expected
- **1996** — Oracle roadmap: vertical cartridges: Release of cartridges customized for business functions (finance) and vertical industries expected
- **2000** — NCA commercial outcome: NCA succeeded in establishing Oracle as enterprise internet platform; Oracle grew to dominant position
- **2005** — CORBA market outcome: CORBA declined rapidly by 2000s; superseded by XML web services and REST; Oracle shifted accordingly
- **2005** — COM/ActiveX fate: ActiveX declined in web context due to security issues; COM persisted in Windows desktop
- **2010** — Java in enterprise: Java became dominant enterprise language; Oracle acquired Sun Microsystems (Java) in 2010
- **2026** — Oracle RDBMS current status: Oracle Database remains leading enterprise RDBMS 30 years later; active and widely deployed
- **1996** — NCA risk profile: Relatively low risk: builds on proven Oracle products; wrapping legacy apps as cartridges
- **1996** — NCA target: Internet protocol support: Supports HTTP and Netscape IIOP for cross-platform communication
- **1996** — Enterprise Manager features: Job scheduling, event management, monitoring, diagnostics, replication management, network management
- **1996** — NetSolutions as NCA entry point: Includes web-enabled Developer/2000, Designer/2000, Cartridge Development Kit, Oracle Web Server

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-oracle-network-computing-architecture' ORDER BY year_observed;
```

