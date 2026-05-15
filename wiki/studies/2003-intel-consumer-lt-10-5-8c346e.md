---
title: "LaGrande Technology: A Proposal for Consumer Market Research"
slug: 2003-intel-consumer-lt-10-5-8c346e
page_type: study
author: "Peter S. Kastner"
date: "2003-10-05"
study_type: market-research-proposal
subject_domain: "hardware-security"
methodology: "qualitative-quantitative-mixed; focus-groups; IDIs; tracking-surveys; localized-quantitative-surveys"
importance: medium
importance_rationale: "Early proposal to expand hardware-based trusted computing to consumer markets at a pivotal moment in platform security history. Represents strategic thinking from a major analyst firm attempting to redirect Intel's product roadmap."
relevance: high
relevance_rationale: "Directly relevant to the evolution of hardware security in consumer computing, the Trusted Computing Group ecosystem, and the long arc from LaGrande Technology to Intel TXT to TPM 2.0 mandates in Windows 11."
prescience: high
prescience_rationale: "Aberdeen's core thesis -- that consumer PCs would require hardware-rooted trusted execution driven by identity theft, privacy, and online trust concerns -- proved visionary. While the specific LaGrande brand and the 2006 timeline did not materialize as forecast, the functional vision was fulfilled comprehensively: Intel embedded firmware TPM 2.0 (PTT) in every consumer Skylake+ processor from 2015; Microsoft mandated TPM 2.0 for all Windows 11 PCs in 2021; and Windows 11 enabled Virtualization-B…"
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 5
obs_count: 28
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# LaGrande Technology: A Proposal for Consumer Market Research

> A proposal from Aberdeen Group EVP Peter S. Kastner to Intel Corporation arguing that the consumer market for Intel's LaGrande Technology (LT) represents a significant untapped opportunity exceeding $150M in annual revenue. The proposal outlines a three-phase multinational research methodology spanning qualitative focus groups, tracking surveys, and localized quantitative surveys across 5-10 countries. Aberdeen contends that Intel's plan to focus LT exclusively on business markets overlooks consumer demand driven by identity theft fears, virus scares, online trust concerns, and intra-family privacy needs. The proposal estimates 10M+ consumer units by 2006 at $100 retail uplift per unit.

**Author:** Peter S. Kastner · **Date:** 2003-10-05 · **Type:** market-research-proposal
**Importance:** medium — *Early proposal to expand hardware-based trusted computing to consumer markets at a pivotal moment in platform security history. Represents strategic thinking from a major analyst firm attempting to redirect Intel's product roadmap.*
**Prescience:** high — *Aberdeen's core thesis -- that consumer PCs would require hardware-rooted trusted execution driven by identity theft, privacy, and online trust concerns -- proved visionary. While the specific LaGrande brand and the 2006 timeline did not materialize as forecast, the functional vision was fulfilled c…*

## Entities (8)

- [[ENT-001|Intel Corporation]]
- [[ENT-002|Aberdeen Group]]
- [[ENT-003|Peter S. Kastner]]
- [[ENT-004|Michael Ferron-Jones]]
- [[ENT-005|Jim Hurley]]
- [[ENT-006|Narendar Sahgal]]
- [[ENT-007|Microsoft]]
- [[ENT-008|Trusted Computing Group]]

## Technologies (5)

- [[TECH-001|Intel LaGrande Technology (LT)]]
- [[TECH-002|LT Platform]]
- [[TECH-003|Trusted Platform Module (TPM)]]
- [[TECH-004|Intel Trusted Execution Technology (TXT)]]
- [[TECH-005|NGSCB (Palladium)]]

## Key observations (top 25)

- **2003** — consumer_lt_annual_revenue_opportunity: $150M+
- **2006** — consumer_lt_unit_forecast: 10M+ units
- **2006** — consumer_lt_retail_uplift: $100 per PC
- **2003** — intel_lt_market_focus: business-only
- **2003** — aberdeen_recommended_focus: consumer-expansion
- **2003** — lt_platform_definition: LT + OS + applications
- **2003** — consumer_volume_rank_1: privacy-and-identity-protection
- **2003** — consumer_volume_rank_2: b2c-value-chains
- **2003** — consumer_volume_rank_3: b2b-value-chains
- **2003** — ubiquity_requirement: hardware and software must be ubiquitous
- **2003** — early_adopter_driver_1: identity-theft-fear
- **2003** — early_adopter_driver_2: virus-scares
- **2003** — early_adopter_driver_3: intra-family-privacy
- **2003** — early_adopter_driver_4: online-trust
- **2003** — cultural_privacy_variation: varies-by-country
- **2003** — consumer_computing_mix: secure-vs-ordinary
- **2003** — processor_id_concern: perceived-turn-off
- **2003** — research_scope_countries: US; Canada; Japan; Germany; UK; France; Italy; China; Brazil; Mexico
- **2003** — it_spending_coverage_pct: 74%
- **2003** — china_exclusion_rationale: political-special-case
- **2003** — attitude_evolution_thesis: evolving-with-experience
- **2006** — lt_renamed_to_txt: Intel TXT
- **2010** — txt_consumer_adoption: limited
- **2021** — tpm_windows11_mandate: mandatory
- **2003** — business_drives_consumer: business-adoption-spillover

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2003-intel-consumer-lt-10-5-8c346e' ORDER BY year_observed;
```

