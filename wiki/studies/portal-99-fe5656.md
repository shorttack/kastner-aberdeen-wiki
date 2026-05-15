---
title: "Portal's Infranet -- Real-Time Customer Management and Billing Pays Dividends to ISPs, Internet-Based Businesses"
slug: portal-99-fe5656
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1999-10-01"
study_type: white-paper
subject_domain: "ISP-billing-software"
methodology: "competitive-profiling, industry-analysis, product-evaluation"
importance: high
importance_rationale: "Captures the ISP billing software market at a critical juncture (1999); documents the architecture and market positioning of Portal Software before its IPO, providing a benchmark for real-time billing evolution."
relevance: medium
relevance_rationale: "Real-time billing and customer management remain critical for telecom and SaaS businesses; Portal Software's approach foreshadowed modern subscription billing platforms (Zuora, Salesforce Billing)."
prescience: high
prescience_rationale: "Aberdeen correctly predicted Portal's real-time architecture would become the industry benchmark; Portal was acquired by Oracle in 2006 for $220M, validating its market position."
license: CC-BY-4.0
tier: 1
entity_count: 19
tech_count: 10
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Portal's Infranet -- Real-Time Customer Management and Billing Pays Dividends to ISPs, Internet-Based Businesses

> Aberdeen Group profiles Portal Software's Infranet 6.0, a real-time customer management and billing platform designed for ISPs and internet-based businesses. The report evaluates Infranet's N-tier object-oriented architecture, real-time billing capabilities, and partnerships with HP, Sun, Compaq, Cisco, Microsoft, and Oracle. Aberdeen concludes Infranet is the stand-out product for real-time customer billing and service, with market-leading capabilities versus competitors Solect and Kenan/Arbor.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1999-10-01 · **Type:** white-paper
**Importance:** high — *Captures the ISP billing software market at a critical juncture (1999); documents the architecture and market positioning of Portal Software before its IPO, providing a benchmark for real-time billing evolution.*
**Prescience:** high — *Aberdeen correctly predicted Portal's real-time architecture would become the industry benchmark; Portal was acquired by Oracle in 2006 for $220M, validating its market position.*

## Entities (19)

- [[aberdeen-group|Aberdeen Group]]
- [[andersen-consulting|Andersen Consulting (Accenture)]]
- [[cisco|Cisco Systems]]
- [[compaq|Compaq]]
- [[compuserve|CompuServe]]
- [[france-telecom|France Telecom Interactive]]
- [[hewlett-packard|Hewlett-Packard]]
- [[john-little|John Little]]
- [[juno-online|Juno Online Services]]
- [[kenan-systems|Kenan Systems (EC/Arbor)]]
- [[microsoft|Microsoft]]
- [[oracle|Oracle]]
- [[portal-software|Portal Software, Inc.]]
- [[pricewaterhousecoopers|PriceWaterhouseCoopers]]
- [[solect|Solect]]
- [[sprint|Sprint]]
- [[sun-microsystems|Sun Microsystems]]
- [[verisign|VeriSign]]
- [[vocaltec|VocalTec]]

## Technologies (10)

- [[cisco-netflow|Cisco Netflow]]
- [[html|HTML]]
- [[infranet|Portal Infranet 6.0]]
- [[infranet-architecture|Infranet N-tier Architecture]]
- [[itm-b-benchmark|ITM-B Internet Performance Benchmark]]
- [[mcis|Microsoft Commercial Internet System (MCIS)]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[oracle-rdb|Oracle Rdb]]
- [[sql|SQL (Structured Query Language)]]
- [[xml|XML (Extensible Markup Language)]]

## Key observations (top 25)

- **1999** — Portal founding and background: Founded 1985; ran ISP operation for 10 years; released first Infranet in May 1996; IPO May 6 1999 NASDAQ: PRSF; 400+ employees worldwide
- **1999** — Infranet core capabilities: Registration, authentication/authorization, activity tracking, event rating/pricing, billing, customer management, business reporting
- **1999** — Infranet architecture design: N-tier application servers; object-oriented; load balancing; 4-level firewall; backup servers at each tier; complete API set
- **1999** — Infranet 6.0 enhancements: Enhanced rating process architecture; real-time volume/tier model; unlimited branded service customers; Web-based brand interfaces; panel-based flexible design
- **1999** — Infranet pricing model: Pay-by-the-subscriber; 25,000-subscriber entry point; fixed cost increments as business grows; no per-server license penalty
- **1999** — Infranet market position: Second-generation Internet business billing leader; ISP market 25,000+ subscribers
- **1999** — Portal vs Solect (low end): Solect targeted smaller ISPs (up to 30K subscribers); single server limitation; few extensibility features; shrink-wrapped
- **1999** — Portal vs Kenan/Arbor (high end): Kenan has telephony billing experience; acquired by Lucent; moving into Energy/Utilities; 2/3 of revenue from services; Portal argues real-time event handling superiority
- **1999** — HP partnership with Portal: HP joint marketing; demonstrated Infranet scalability on Unix platforms via ITM-B benchmark
- **1999** — Microsoft-Portal integration: Tight integration with NT Server, SQL Server 7, MCIS; Microsoft worked extensively with Portal
- **1999** — Oracle-Portal partnership: Portal is Oracle Business Alliance Partner; Oracle actively co-markets with Portal
- **1999** — Cisco-Portal metered billing partnership: Portal-Cisco development of metered billing applications using Cisco Netflow technology; plus IP telephony gateway support (VocalTec, Skywave)
- **1999** — CompuServe as Infranet customer: CompuServe uses Infranet for customer management and billing
- **1999** — Sprint Internet Passport uses Infranet: Sprint's Internet Passport service uses Portal Infranet
- **1999** — Infranet as standard-bearer for real-time billing: Under no circumstances should IT consider replicating Infranet's functionality themselves; Infranet is Aberdeen's first choice for traditional and new-breed ISPs
- **2006** — Portal Software fate: unknown
- **1999** — ISP market evolution prediction: ISP data access services becoming commodity; ISPs must expand to value-added services beyond data access
- **1999** — Internet market dynamic forecast: Brand-name driven shake-out; big get bigger; small specialize; highly dynamic environment
- **1999** — Infranet multi-database support: Multi-database support including Oracle Rdb and SQL Server 7; multi-threaded invoicing (HTML, XML, DOC1 formats)
- **1999** — Portal target market segment: Medium-to-large ISPs with 25,000+ subscribers; online/internet-based services; IP telephony providers; gaming companies; content providers; billing service bureaus

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'portal-99-fe5656' ORDER BY year_observed;
```

