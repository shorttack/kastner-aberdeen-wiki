---
title: "Choosing The Right Markets and the Right Partners for Informix"
slug: informix-dsa-presentation-2-8d5fa3
page_type: study
author: "Peter S. Kastner / Aberdeen Group"
date: "1995-1996"
study_type: consulting-report
subject_domain: "market segmentation; channel strategy; client-server solutions; RDBMS vertical markets"
methodology: "expert-analysis; market segmentation; channel strategy"
importance: high
importance_rationale: "Richest market-and-channel strategy document in the set; provides pricing data, vertical market ratings, and channel selection frameworks for Informix sales training."
relevance: medium
relevance_rationale: "Framework for RDBMS market segmentation and channel strategy still instructive; specific pricing and competitive landscape now historical."
prescience: high
prescience_rationale: "Correctly forecast NT Server growth at workgroup/department level; predicted SAP dominance in enterprise CSS; foresaw ISV shift to Windows 32-bit; channel strategy advice on VAR loyalty and ISV leverage proved accurate."
license: CC-BY-4.0
tier: 1
entity_count: 13
tech_count: 10
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Choosing The Right Markets and the Right Partners for Informix

> Aberdeen Group analysis of the optimal markets and channel partners for Informix. Covers industry trends (open systems, RAD, distributed computing, client-server), customer decision-making dynamics, CSS market characteristics with pricing tiers ($500-$150k/module by company size), and detailed channel partner assessments (VARs, ISVs, OEMs, SIs, Big 6). Includes vertical market ratings for telecomm, retail, banking, manufacturing, and state/local government. 67-slide deck used in Informix sales training.

**Author:** Peter S. Kastner / Aberdeen Group · **Date:** 1995-1996 · **Type:** consulting-report
**Importance:** high — *Richest market-and-channel strategy document in the set; provides pricing data, vertical market ratings, and channel selection frameworks for Informix sales training.*
**Prescience:** high — *Correctly forecast NT Server growth at workgroup/department level; predicted SAP dominance in enterprise CSS; foresaw ISV shift to Windows 32-bit; channel strategy advice on VAR loyalty and ISV leverage proved accurate.*

## Entities (13)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq-computer|Compaq Computer Corporation]]
- [[computer-associates|Computer Associates (CA)]]
- [[digital-equipment-corporation|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[ibm-corporation|International Business Machines Corporation]]
- [[microsoft-corporation|Microsoft Corporation]]
- [[novell-inc|Novell, Inc.]]
- [[oracle-corporation|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sap-ag|SAP AG]]
- [[sun-microsystems|Sun Microsystems]]
- [[tandem-computer|Tandem Computer Corporation]]

## Technologies (10)

- [[as400|IBM AS/400]]
- [[client-server|Client-Server Architecture]]
- [[decision-support|Decision Support / Business Intelligence]]
- [[microsoft-sql-server|Microsoft SQL Server]]
- [[novell-netware|Novell NetWare]]
- [[ordbms|Object-Relational DBMS (ORDBMS)]]
- [[rdbms|Relational Database (RDBMS)]]
- [[sap-r3|SAP R/3]]
- [[sybase-powerbuilder|Sybase PowerBuilder]]
- [[unix-server|Unix Enterprise Servers]]

## Key observations (top 25)

- **1995-1996** — unix_tier1_growth_rate: 20%+ per year
- **1995-1996** — nt_server_adoption: Steadily picking up steam at workgroup/department level
- **1995-1996** — mpp_market_share: <2% of server market
- **1995-1996** — nt_clustering_timeline: NT Server clustering will emerge in 1996, thrive in 1997 (Compaq+Tandem; DEC)
- **1997** — nt_clustering_timeline: unknown
- **1995** — css_module_price_small_co: $500 to $5,000 per module (companies <$25M revenue)
- **1995** — css_module_price_midmarket: $10,000 to $75,000 per module (companies <$250M revenue)
- **1995** — css_module_price_enterprise: $50,000 to $150,000 per module (companies >$251M revenue)
- **1995** — css_enterprise_leader: SAP AG is enterprise CSS market leader
- **1995** — css_market_structure: Solution set (integrated vs best-of-breed); architecture (app-centric vs DB-centric); toolsets; channel; midrange OS
- **1995** — css_impl_fortune500_mfg: Manufacturing & Distribution: 12 to 36 months (Fortune 500)
- **1995** — css_impl_fortune1000_hr: Human Resources: 1 to 3 months (Fortune 1000)
- **1994-1995** — new_impl_client_server_vs_mf: Client-Server implementations surging vs mainframe; 449 vs 210 planned
- **1995** — telecomm_market_rating: Highly attractive — time to market beats price; many channel partners
- **1995** — retail_market_rating: Good with 50% chance rain — price always important; low margins
- **1995** — banking_market_rating: Good over time; fair in 1996 — Informix not broadly known
- **1995** — manufacturing_market_rating: Good short and long term — solutions-oriented; VARs and ISVs critical
- **1995** — state_local_govt_rating: Fair — long selling cycle; bidding regulations; competition among partners
- **1995** — channel_partner_crit_success: Leads; programs; tiered coop marketing funding; senior account management; tech support access
- **1995** — irrelevant_channel_factors: Price; switch incentives; best technology du jour; moral superiority
- **1995** — it_top_issue_1995: Aligning IT and corporate goals (#1 issue for IT executives in 1995)
- **1995** — sap_isvs_leverage: SAP R/3 to Informix: large leverage factor for ISV partners
- **1995** — it_industry_growth: IT industry in most rapid growth stage ever; rate of change accelerating
- **1995** — unix_commercial_maturity: Only in 1990s has Unix emerged as practical and reliable for commercial applications
- **1995** — informix_strategic_markets: Workgroup; C-S apps; customer-interaction; end-user; custom/enterprise; imaging/workflow; Internet; data warehousing

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'informix-dsa-presentation-2-8d5fa3' ORDER BY year_observed;
```

