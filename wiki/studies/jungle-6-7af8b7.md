---
title: "Welcome to the RDBMS Jungle — Chapter 6"
slug: jungle-6-7af8b7
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1995"
study_type: consulting-report
subject_domain: "RDBMS vendor competitive analysis; technology ratings; IBM DB2 positioning"
methodology: "expert-analysis; competitive-intelligence; market-research"
importance: high
importance_rationale: "Deep competitive-intelligence supplement to JUNGLE-1-5; particularly valuable for IBM DB2 positioning and vendor weakness analysis from Informix sales perspective."
relevance: medium
relevance_rationale: "Historical primary-source competitive intelligence; IBM's 1994 Unix market share gain at HP's expense is a specific data point of archival significance."
prescience: high
prescience_rationale: "Correctly identified all major vendor weaknesses that materialized: Oracle's multimedia distraction; Sybase's architectural stagnation; IBM's perception problem; CA-Ingres's market decline. IBM gaining Unix share at HP's expense in 1994 proved a real trend. Microsoft's upward trajectory was underestimated."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 25
obs_count: 42
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Welcome to the RDBMS Jungle — Chapter 6

> Chapter 6 continuation of the RDBMS Jungle training deck. Reprises market size and supplier data from Chapters 1-5, then provides expanded competitive detail: vendor-by-vendor weakness analyses, RDBMS technology rating breakdowns (scalability, distributed data, open technology, development tools, other technologies, supplier solutions), ISV platform support data (IBM gaining Unix share at HP's expense in 1994), IBM RS/6000 + DB2 best-fit scenarios, and wrap-up on RDBMS market dynamics. 58-slide deck.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1995 · **Type:** consulting-report
**Importance:** high — *Deep competitive-intelligence supplement to JUNGLE-1-5; particularly valuable for IBM DB2 positioning and vendor weakness analysis from Informix sales perspective.*
**Prescience:** high — *Correctly identified all major vendor weaknesses that materialized: Oracle's multimedia distraction; Sybase's architectural stagnation; IBM's perception problem; CA-Ingres's market decline. IBM gaining Unix share at HP's expense in 1994 proved a real trend. Microsoft's upward trajectory was underest…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates (CA)]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm-corporation|International Business Machines Corporation]]
- [[ingres|Ingres]]
- [[microsoft-corporation|Microsoft Corporation]]
- [[oracle-corporation|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sequent-computer-systems|Sequent Computer Systems]]
- [[sun-microsystems|Sun Microsystems]]
- [[sybase|Sybase]]
- [[tandem-computers|Tandem Computers]]

## Technologies (25)

- [[aix|IBM AIX]]
- [[ca-ingres|CA-Ingres (OpenIngres)]]
- [[db2-aix|IBM DB2 for AIX]]
- [[decision-support|Decision Support / Business Intelligence]]
- [[hp-9000|HP 9000]]
- [[ibm-cics|IBM CICS TP Monitor]]
- [[ibm-db2|IBM DB2]]
- [[ibm-sp2|IBM SP2]]
- [[ibm-sp2|IBM SP2]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[oltp|Online Transaction Processing]]
- [[oracle-7|Oracle 7.x]]
- [[oracle-8|Oracle 8]]
- [[oracle-parallel-server|Oracle Parallel Server]]
- [[ordbms|Object-Relational DBMS (ORDBMS)]]
- [[rdbms|Relational Database (RDBMS)]]
- [[rs6000|IBM RS/6000]]
- [[rs6000-smp|IBM RS/6000 SMP]]
- [[sun-solaris|Sun Solaris]]
- [[sybase-iq|Sybase IQ Accelerator]]
- [[sybase-navigation-server|Sybase Navigation Server]]
- [[sybase-powerbuilder|Sybase PowerBuilder]]
- [[sybase-sql-server|Sybase SQL Server / System 11]]
- [[tpc-c|TPC-C Benchmark]]
- [[unix|UNIX (various)]]

## Key observations (top 25)

- **1995** — ww_database_market: ~$20 billion worldwide
- **1995** — rdbms_market_size: $5.5 billion (largest segment)
- **1995** — rdbms_submarket_growth: 50%+ per year
- **1995** — unix_vs_mainframe_dbms: Unix-server DBMS revenue now greater than mainframe revenues
- **1994** — sybase_revenue: $826 million total 1994 revenue; up 71% from 1993
- **1995** — sybase_market_rank: Second-largest RDBMS supplier
- **1994-1995** — sybase_past_growth: Past 60-80% growth rate
- **1994** — oracle_revenue: $2.4 billion; up 40% from 1993
- **1995** — oracle_market_cap: $18.7 billion; up 100% from 1994
- **1994-1995** — oracle_market_rank: Largest RDBMS supplier; on track for $3.6+ billion FY1996
- **1994** — informix_revenue: $469 million; up 33% from 1993; trailing 12mo $568M
- **1995** — informix_market_cap: $4.3 billion (up from $1.5B in 1994)
- **1994-1995** — informix_market_rank: Third-largest RDBMS supplier
- **1995** — ibm_scalability: Competitive but not leading on SMP; only compatible SMP and MPP story except AT&T
- **1995** — ingres_scalability: Modest scalability; no MPP
- **1995** — informix_scalability: Good scalability to 8 processors SMP; many TPC-Cs; soon on SP2 with version 8
- **1995** — msft_scalability: Modest scalability; no MPP; good on Alpha
- **1995** — oracle_scalability: Good story from desktop to SP2 & ES/9000; No TPC-C until July 1995
- **1995** — sybase_scalability: Poor beyond 4 processors; Navigation Server poor high-end MPP on AT&T 3600
- **1995** — ingres_distributed_rating: Best functionality in distributed/replication category
- **1995** — ibm_distributed_rating: Good async replication in Data Propagator; no peer-peer replication
- **1995** — informix_distributed_rating: Behind; better next year
- **1995** — oracle_distributed_rating: Good replication including peer-peer
- **1995** — sybase_open_tech_rating: Open Client & Open Server best gateway breadth; most flexible
- **1995** — ingres_dev_tools_rating: OpenROAD is most mature OO CADE (computer-aided development environment)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'jungle-6-7af8b7' ORDER BY year_observed;
```

