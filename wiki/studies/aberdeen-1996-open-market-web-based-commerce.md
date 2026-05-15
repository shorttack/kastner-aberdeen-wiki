---
title: "Open Market: Delivering the Infrastructure For Truly Open Web-based Commerce"
slug: aberdeen-1996-open-market-web-based-commerce
page_type: study
author: "Aberdeen Group"
date: "1996-10-01"
study_type: market-study
subject_domain: "web-commerce, e-commerce-infrastructure, payment-systems"
methodology: "industry-analysis, competitive-profiling, field-research, expert-opinion"
importance: high
importance_rationale: "Open Market was among the first enterprise-grade web commerce platforms at a pivotal moment in e-commerce infrastructure formation (1996); Aberdeen's endorsement to AT&T, BT, MCI, and major banks made this a significant industry signal."
relevance: medium
relevance_rationale: "The many-to-many transaction architecture and CSP model anticipated API-based commerce ecosystems; specific OM-Transact/OM-Axcess products are obsolete, but the conceptual framework for distributed commerce middleware remains instructive."
prescience: medium
prescience_rationale: "Aberdeen correctly predicted that enterprise web commerce would require comprehensive back-office integration beyond simple HTTP servers; however Open Market was acquired by Divine (2001) then went bankrupt (2003), not achieving the sustained market leadership Aberdeen projected."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 7
obs_count: 28
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Open Market: Delivering the Infrastructure For Truly Open Web-based Commerce

> Aberdeen Group profiles Open Market, Inc. (Cambridge, MA), a pioneer in enterprise-grade web commerce infrastructure. The study examines Open Market's product suite—OM-Transact, OM-Axcess, and OM-SecureLink—designed to support many-to-many web-based transactions across multiple content servers and back-office systems. Aberdeen strongly recommends Open Market's platform as the most comprehensive and production-ready solution for enterprises building next-generation electronic commerce infrastructure, and contrasts it favorably against IBM and point-to-point proprietary competitors.

**Author:** Aberdeen Group · **Date:** 1996-10-01 · **Type:** market-study
**Importance:** high — *Open Market was among the first enterprise-grade web commerce platforms at a pivotal moment in e-commerce infrastructure formation (1996); Aberdeen's endorsement to AT&T, BT, MCI, and major banks made this a significant industry signal.*
**Prescience:** medium — *Aberdeen correctly predicted that enterprise web commerce would require comprehensive back-office integration beyond simple HTTP servers; however Open Market was acquired by Divine (2001) then went bankrupt (2003), not achieving the sustained market leadership Aberdeen projected.*

## Entities (10)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[att|AT&T]]
- [[british-telecom|British Telecommunications (BT)]]
- [[ibm|IBM]]
- [[mci|MCI Communications]]
- [[microsoft|Microsoft Corporation]]
- [[netscape-communications|Netscape Communications]]
- [[onewave-inc|OneWave, Inc.]]
- [[open-market-inc|Open Market, Inc.]]
- [[trilogy-development-group|Trilogy Development Group]]

## Technologies (7)

- [[http|HTTP (HyperText Transfer Protocol)]]
- [[om-axcess|OM-Axcess]]
- [[om-securelink|OM-SecureLink]]
- [[om-transact|OM-Transact]]
- [[oracle-rdbms|Oracle RDBMS]]
- [[ssl|SSL (Secure Sockets Layer)]]
- [[sybase-rdbms|Sybase RDBMS]]

## Key observations (top 25)

- **1996** — Business strategy: Many-to-many web commerce infrastructure for Commerce Service Providers (CSPs)
- **1996** — OM-Transact architecture: Modular plug-in, database-centric, geographically dispersed; Oracle or Sybase backend
- **1996** — OM-SecureLink security: MD5 hash + SSL + ticketing; HTTP-standard compliant
- **1996** — IPO fundraising: Over $80 million raised in IPO
- **1996** — Annual expense rate: $50 million
- **1996** — Annualized revenue run rate (last quarter): $27 million
- **1996** — IBM web commerce strategy: Cyber-mall approach: all transaction applications hosted on one central site
- **1996** — IBM e-commerce product maturity vs Open Market: IBM products lack advanced functionality; focus on IBM CSP services, not enterprise B2B
- **1996** — Netscape web strategy: Commodity HTTP server focus; not a comprehensive e-commerce infrastructure
- **1996** — Microsoft web strategy: Commodity HTTP server (IIS); not addressing enterprise back-office commerce
- **1996** — Open Market revenue growth: Revenue growth rate may increase significantly given CSP customer endorsements
- **1996** — Open Market long-term market position: Should be leading infrastructure for enterprise web commerce if mindshare achieved
- **1996** — AT&T adoption of OM-Transact: AT&T named as industry-leading CSP using Open Market products
- **1996** — CSP model: internal IT departments: Corporations using Open Market to provide Web capabilities for multiple divisions
- **1996** — CSP model: external service providers: Banks, telcos, internet access providers extending offerings via Open Market
- **1996** — OM-Transact key functions: Authentication, payment processing, order management, shipping/tax calculation, digital goods fulfillment
- **1996** — ISV partner count: 13 ISV partners for front-office web development (including Informix, Powersoft, SoftQuad)
- **1996** — Trilogy alliance purpose: Sales force automation integration with Open Market back-office
- **1996** — Aberdeen recommendation: Enterprise IS executives would be highly remiss not to fully evaluate Open Market
- **2001** — Open Market acquisition: Acquired by Divine Inc. for approximately $59 million in 2001
- **2003** — Divine Inc bankruptcy: Divine filed for bankruptcy early 2003; Open Market assets split between Soverain and FatWire
- **2003** — Revenue growth outcome: Did not sustain leadership; acquired below IPO valuation and acquirer went bankrupt
- **1996** — OM-Axcess access management: Central access management across HTTP layer and individual database layer
- **1996** — Competitive landscape size: Literally hundreds of suppliers claiming to offer web-based transaction tools
- **1996** — Aberdeen market framing: In-house custom programming is Open Market's chief competitor

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-open-market-web-based-commerce' ORDER BY year_observed;
```

