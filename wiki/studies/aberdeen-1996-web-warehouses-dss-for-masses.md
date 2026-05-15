---
title: "Web Warehouses: DSS For The Masses"
slug: aberdeen-1996-web-warehouses-dss-for-masses
page_type: study
author: "Aberdeen Group"
date: "1996-03-25"
study_type: market-study
subject_domain: "data-warehousing"
methodology: "industry-analysis, field-research, expert-opinion, competitive-profiling"
importance: high
importance_rationale: "Published in March 1996—more than a year before web-based BI tools became commercially mainstream—this study articulated the thin-client BI thesis that would drive the entire enterprise BI industry for the next decade; Aberdeen's $50 vs $1,000 cost comparison was one of the first rigorous economic arguments for web-delivered decision support."
relevance: high
relevance_rationale: "The web-browser as universal BI client became completely dominant (Tableau, Power BI, Looker all deliver via browser); the thin-client economics Aberdeen predicted materialized; the security and integration challenges Aberdeen identified remained active research areas through cloud BI era. The conceptual framework maps precisely to modern cloud data warehouses."
prescience: high
prescience_rationale: "Aberdeen's core predictions—browser-based BI democratizing decision support, Web removing cost barriers, parallel-scalable hardware becoming the warehouse standard, and security/CGI as short-term hurdles to be solved in 1-2 years—all proved correct. Modern cloud BI (AWS Redshift, Snowflake, Google BigQuery) is the exact architecture Aberdeen envisioned."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 8
obs_count: 25
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Web Warehouses: DSS For The Masses

> Aberdeen Group argues that the combination of the World Wide Web, Relational OLAP, and parallel-scalable hardware will 'democratize' enterprise data warehousing by dramatically reducing per-seat decision support costs (Web browser at ~$50/seat vs. $1,000/seat for traditional DSS software). The study analyzes Web-based decision support architecture, identifies hurdles to enterprise adoption (security, CGI bottlenecks, browser immaturity), and concludes that Web-enabled warehouses will transform enterprise competitive behavior.

**Author:** Aberdeen Group · **Date:** 1996-03-25 · **Type:** market-study
**Importance:** high — *Published in March 1996—more than a year before web-based BI tools became commercially mainstream—this study articulated the thin-client BI thesis that would drive the entire enterprise BI industry for the next decade; Aberdeen's $50 vs $1,000 cost comparison was one of the first rigorous economic a…*
**Prescience:** high — *Aberdeen's core predictions—browser-based BI democratizing decision support, Web removing cost barriers, parallel-scalable hardware becoming the warehouse standard, and security/CGI as short-term hurdles to be solved in 1-2 years—all proved correct. Modern cloud BI (AWS Redshift, Snowflake, Google B…*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[information-advantage|Information Advantage Inc.]]
- [[microsoft|Microsoft Corporation]]
- [[microstrategy|MicroStrategy Inc.]]
- [[ncr-corporation|NCR Corporation]]
- [[netscape|Netscape Communications]]
- [[oracle|Oracle Corporation]]
- [[red-brick-systems|Red Brick Systems]]
- [[spyglass|Spyglass Inc.]]

## Technologies (8)

- [[cgi|Common Gateway Interface (CGI)]]
- [[html|HTML (HyperText Markup Language)]]
- [[intranet|Enterprise Intranet]]
- [[parallel-scalable-hardware|Parallel-Scalable Server Hardware (SMP/MPP)]]
- [[rdbms|Relational Database Management System (RDBMS)]]
- [[relational-olap|Relational OLAP (ROLAP)]]
- [[teradata|NCR Teradata Database]]
- [[web-browser|Web Browser (Netscape Navigator / MSIE)]]

## Key observations (top 25)

- **1996** — Web browser vs DSS software per-seat cost: Web browser: approximately $50/seat (quantity 1) vs. average $1,000/seat for traditional decision-support software
- **1996** — NCR warehouse experience: NCR has approximately 12 years experience designing, managing and implementing data warehouses in virtually every industry
- **1996** — Warehouse cost barrier composition: Traditional warehouse cost barriers: warehouse design + desktop software + hardware + connectivity + dedicated lines to suppliers/offices + replication costs as system grows
- **1996** — Browser vs Windows client for power users: Browsers lack OLE, cut-and-paste ease, formatting inheritance compared to Windows front ends; power users will initially need coexistence of client-server and web ROLAP
- **1996** — CGI bottleneck severity: CGI is a single-threaded bottleneck for communicating from web server to applications; must be replaced by multi-threaded alternatives for enterprise BI
- **1996** — ROLAP + Web architecture: Relational OLAP + HTML + Web server + cache-enhanced SQL = multidimensional analysis on the Web; MicroStrategy and Information Advantage leading implementations
- **1996** — Web warehouse hardware requirements: Web DSS demands: scalability (incremental CPUs/RAID), high availability (online backup/redundancy), RDBMS parallelization, systems/network management; same as traditional warehouse but at higher scale
- **1996** — RDBMS as Web warehouse foundation: RDBMS is foundation for Relational OLAP and Web warehousing; parallel-scalable RDBMS required; proprietary multidimensional DBs incompatible with Web architecture
- **1996** — Web DSS obstacle: security: Security beyond data encryption/browser authentication required before enterprise Web DSS deployment
- **1996** — Web DSS obstacle: CGI single-threading: CGI single-threaded bottleneck must be replaced by multi-threaded alternative for enterprise-scale web BI
- **1996** — Web DSS obstacle: browser immaturity: Browsers must mature to accommodate dynamic portfolio analysis, not just static financial data
- **1996** — Web DSS obstacle: limited app dev tools: HTML-based development tools need to add pop-up windows and radio bars to match GUI desktop capabilities
- **1996** — Web DSS obstacle: desktop integration: Better integration with desktop applications (spreadsheets) required for power user adoption
- **1996** — Intranet as first enterprise Web DSS opportunity: Natural information-gathering, no-update affinity between decision support and Web makes DSS the first high-impact Web candidate
- **1996** — CEO DSS mandate prediction: Aberdeen: as browsers mature, CEOs and high-level decision makers will mandate IS to build Web-enabled decision support
- **1996** — Web-driven warehouse expenditure reallocation: Web reapportions warehouse costs: savings on desktop software/deployment redirected to server hardware, RDBMS, and data preparation — exactly where investment belongs
- **1996** — Decision support as OLTP pressure point: Decision support is becoming so enterprise critical it is being placed in a reciprocal relationship with OLTP; IS must pay attention to OLTP-data download speed
- **1996** — Web browser as universal BI thin client: Aberdeen predicts Web browser will become the primary delivery mechanism for enterprise decision support, removing traditional DSS per-seat cost barrier
- **2005** — Web browser BI outcome: Web browser became universal BI client by 2000-2005; Tableau (2003), Power BI, Looker all browser-based; Salesforce CRM entirely browser-based; per-seat BI costs dropped dramatically
- **1996** — CGI/security obstacles cleared in 1-2 years: Aberdeen: most obstacles (security, CGI, browser maturity) will be swept away over next 1-2 years, driving new DSS/warehouse applications
- **1998** — Web DSS obstacle resolution outcome: SSL security became standard by 1997; CGI replaced by ISAPI/NSAPI and FastCGI by 1997-1998; DHTML/JavaScript addressed browser limitations; all major obstacles resolved within Aberdeen's 1-2 year timeline
- **1996** — NCR Teradata/Worldmark scalability range: NCR Worldmark servers cover SMP, Clusters, and MPP configurations; Teradata scales from data marts to multi-terabyte detailed warehouses
- **1996** — NCR/MicroStrategy partnership model: NCR (infrastructure + consulting + industry templates) + MicroStrategy (ROLAP toolset) = 'warehouse-supplier synergy' model for enterprise Web DSS
- **1996** — Web warehouse infrastructure strategy: Enterprise Web warehouse strategy: start small SMP, scale within SMP range if appropriate, or grow to MPP — same architecture at different scale without recompilation
- **1996** — Internet as enterprise data backbone: Aberdeen: Internet will evolve into secure electronic backbone serving both intranet and business-to-business applications; decision support is the first high-impact candidate

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-web-warehouses-dss-for-masses' ORDER BY year_observed;
```

