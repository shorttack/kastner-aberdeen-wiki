---
title: "Q&A: Achieving More Value from Enterprise Applications"
slug: q-a-achieving-more-value-from-enterprise-d1d7dd
page_type: study
author: "Peter S. Kastner (AberdeenGroup) — Enterprise Systems Journal"
date: "2006-05-23"
study_type: memoir
subject_domain: "enterprise-soa-applications"
methodology: "industry-analysis, expert-opinion, oral-history"
importance: high
importance_rationale: "Primary-source first-person Kastner authored piece; captures his 2006 framing of SOA strategy and the 'accidental architecture' warning at the peak of SOA hype."
relevance: medium
relevance_rationale: "Classical SOA/ESB stacks were supplanted by microservices/APIs post-2012, but Kastner's integration thesis and 'accidental architecture' warning translate directly to modern microservices sprawl and API-gateway decisions."
prescience: high
prescience_rationale: "Kastner was right: coupling SOA-enabled ERP with enterprise-wide SOA toolset did produce accidental architectures across many organizations. The microservices/API era 2015+ repeated the same pattern, vindicating Kastner's warning."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 5
obs_count: 8
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Q&A: Achieving More Value from Enterprise Applications

> Kastner-authored Q&A for Enterprise Systems Journal (2006-05-23) accompanying the AberdeenGroup Benchmark Report 'Achieving More Value from Enterprise Applications.' Kastner, then Research Vice President and co-founder of enterprise integration research at AberdeenGroup, diagnoses 'siloed applications connected with the software equivalent of chewing gum and baling wire,' reports that more than half of surveyed enterprises are unhappy with enterprise-application ROI and that over two-thirds view SOA technologies as the improvement path, warns against relying on SOA-enabled ERP as a general SOA toolset (the 'accidental architecture' trap), and recommends cross-platform, cross-process, cross-application capabilities when evaluating SOA infrastructure.

**Author:** Peter S. Kastner (AberdeenGroup) — Enterprise Systems Journal · **Date:** 2006-05-23 · **Type:** memoir
**Importance:** high — *Primary-source first-person Kastner authored piece; captures his 2006 framing of SOA strategy and the 'accidental architecture' warning at the peak of SOA hype.*
**Prescience:** high — *Kastner was right: coupling SOA-enabled ERP with enterprise-wide SOA toolset did produce accidental architectures across many organizations. The microservices/API era 2015+ repeated the same pattern, vindicating Kastner's warning.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[enterprise-strategies-publication|Enterprise Strategies (101 Communications co-publication)]]
- [[enterprise-systems-journal|Enterprise Systems Journal (ESJ) — 1105 Media]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (5)

- [[business-process-management|Business Process Management (BPM)]]
- [[enterprise-service-bus|Enterprise Service Bus (ESB)]]
- [[erp-application-platform|ERP Application Platform (generic)]]
- [[service-oriented-architecture|Service-Oriented Architecture (SOA)]]
- [[web-services|Web Services (SOAP/WSDL/UDDI)]]

## Key observations (top 25)

- **2006** — Siloed-applications diagnosis: One reason IT isn't as agile as it should be is due to the poor integration between applications. There are siloed applications connected with the software equivalent of chewing gum and baling wire.
- **2006** — ROI dissatisfaction survey: More than half of enterprises surveyed report they are unhappy with the ROI of the investment in enterprise applications.
- **2006** — SOA adoption survey: Over two-thirds of survey respondents see SOA technologies such as Web services and open middleware as the means of improving enterprise application integration.
- **2006** — Accidental architecture warning: SOA takes planning, lest IT fall into what we call an 'accidental architecture.' If IT takes a project-by-project approach to implementing SOA, they must pay particular attention to the SOA infrastructure and tools they pick.
- **2006** — Three SOA infrastructure criteria: Three key considerations for SOA infrastructure and tools: cross-platform, cross-process, cross-application capabilities.
- **2006** — SOA-enabled ERP as toolset warning: Some SOA buyers believe they can upgrade to the SOA versions of their ERP applications and then use the result as their SOA toolset. We warn against that approach in our report — it is dangerous.
- **2006** — BPM integration gap: Business process management isn't integrated well with the rest of IT; the silos were never designed for cross-application communications, and it is expensive to re-plumb the IT infrastructure.
- **2018** — Kastner's 'accidental architecture' replayed in microservices: Microservices era (2015-present) repeatedly produced accidental architectures at scale (microservices sprawl, distributed monoliths); teams adopted service meshes and platform engineering to contain, validating Kastner's 2006 warning.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'q-a-achieving-more-value-from-enterprise-d1d7dd' ORDER BY year_observed;
```

