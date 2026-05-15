---
title: "The EC Company: Not Your Father's EDI"
slug: 1997-the-ec-company-not-your-father-s-edi-c1ebff
page_type: study
author: "Aberdeen Group"
date: "1997-05-01"
study_type: market-study
subject_domain: "EDI-electronic-commerce-supply-chain"
methodology: "competitive-profiling, industry-analysis, field-research"
importance: high
importance_rationale: "The study identified a genuine market gap — mid-market EDI adoption at only 2% vs. 95% Fortune 1000 penetration — and profiled an innovative solution architecture and pricing model that presaged the internet-driven disruption of VAN-based EDI."
relevance: high
relevance_rationale: "The dynamics of disrupting expensive incumbent networks with internet-native, low-cost alternatives remain highly relevant to B2B integration, APIs, and supply chain digitization debates in 2024; the specific pricing and architecture detail provides rich historical context."
prescience: medium
prescience_rationale: "Aberdeen correctly identified internet-based EDI as the future and the hub model as architecturally sound; however, The EC Company itself did not survive — EDI disruption came through Sterling Commerce, GXS, and eventually AS2/API-based B2B, not through this specific startup."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 9
obs_count: 22
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# The EC Company: Not Your Father's EDI

> Aberdeen Group profiles The EC Company, a 1994-founded Palo Alto start-up offering a dramatically lower-cost EDI enablement solution for mid-market supply chain organizations. The study details the company's unique hub-centric network architecture, aggressive low-price strategy (EC Exchange for $130, transactions approaching postage-stamp cost), and indirect channel distribution through Arthur Andersen, Huntington Bank, and Thompson Financial. Aberdeen concludes the company may break the mold of traditional VAN-based EDI if it can sustain transaction volume growth to achieve profitability within 18–24 months.

**Author:** Aberdeen Group · **Date:** 1997-05-01 · **Type:** market-study
**Importance:** high — *The study identified a genuine market gap — mid-market EDI adoption at only 2% vs. 95% Fortune 1000 penetration — and profiled an innovative solution architecture and pricing model that presaged the internet-driven disruption of VAN-based EDI.*
**Prescience:** medium — *Aberdeen correctly identified internet-based EDI as the future and the hub model as architecturally sound; however, The EC Company itself did not survive — EDI disruption came through Sterling Commerce, GXS, and eventually AS2/API-based B2B, not through this specific startup.*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[arthur-andersen|Arthur Andersen LLC]]
- [[general-electric-information-services|General Electric Information Services (GEIS)]]
- [[harbinger|Harbinger Corporation]]
- [[huntington-bank|Huntington National Bank]]
- [[peoplesoft|PeopleSoft]]
- [[platinum-software|Platinum Software]]
- [[premenos|Premenos Corporation]]
- [[sterling-commerce|Sterling Commerce]]
- [[the-ec-company|The EC Company]]
- [[thompson-financial|Thompson Financial Publishing]]
- [[uunet|UUNET Technologies]]

## Technologies (9)

- [[as2-edi|AS2 Internet EDI]]
- [[ec-central|EC Central]]
- [[ec-exchange|EC Exchange]]
- [[ec-start|EC Start]]
- [[edi-van|EDI Value-Added Network (VAN)]]
- [[ms-sql-server|Microsoft SQL Server 6.5]]
- [[public-key-encryption|Public Key/Private Key Encryption]]
- [[uunet-network|UUNET Internet Backbone]]
- [[windows-nt|Windows NT Server]]

## Key observations (top 25)

- **1997** — Fortune 1000 EDI adoption: 95%
- **1997** — Small-business EDI adoption: 2% of businesses with 5+ employees
- **1997** — Traditional EDI VAN transaction fee range: $1.00 to $5.00 per transaction
- **1997** — EC Exchange license fee: $130
- **1997** — EC Network monthly service fee (25 tx): $30/month including first 25 transactions at $0.45 each additional
- **1997** — Total venture capital raised: $11.1 million through three rounds
- **1997** — Distribution strategy: Indirect channel via VAR and OEM partners (Arthur Andersen, Huntington Bank, Thompson Financial, Platinum Software, PeopleSoft)
- **1997** — Founding history: Founded 1994 as Buena Vista Software, Inc.; rebranded to The EC Company
- **1997** — Software maturity: Well-engineered for ease of use; 16-bit; lacks automated scheduling; not yet enterprise messaging server-class
- **1997** — Network architecture: Private extranet on outsourced UUNET infrastructure; hub-centric translation; 270 US points of presence
- **1997** — Security model: Public Key/Private Key session encryption; symmetric session keys discarded after use
- **1997** — Path to profitability: Company estimates 18-24 months to profitable equilibrium on transaction volume model
- **1997** — Market disruption potential: May break the mold of traditional EDI VAN suppliers if transaction volume achieved
- **1997** — Incumbent response strategy: Web-forms via Internet extended from EDI server; Internet-enabled EDI server software at partner sites
- **1997** — Investment type: First venture investment by Arthur Andersen audit partnership in firm history
- **2002** — Company survival: The EC Company did not achieve market breakthrough; likely dissolved or quietly acquired during EDI market consolidation 1998-2002
- **2005** — AS2 internet EDI standard adoption: RFC 4130 AS2 standard adopted 2005; fulfilled EC Company's internet-native EDI vision
- **2011** — Sterling Commerce acquisition chain: Sterling Commerce acquired by AT&T (2000), then Oracle (2011) for $1.4B; became Oracle B2B Commerce
- **2002** — Arthur Andersen dissolution: Arthur Andersen dissolved 2002 following Enron accounting scandal
- **1997** — Mid-market barrier: technical expertise: EDI requires EDI standards knowledge, database mapping, per-partner translation — too complex for mid-market IT staff
- **1997** — Mid-market barrier: VAN transaction costs: $1-$5 per transaction creates ROI barrier for low-volume mid-market companies
- **1997** — Mid-market barrier: initial implementation cost: High initial EDI software/hardware investment deters mid-market adoption

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-the-ec-company-not-your-father-s-edi-c1ebff' ORDER BY year_observed;
```

