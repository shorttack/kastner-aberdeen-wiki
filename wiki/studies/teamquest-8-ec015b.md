---
title: "Using TeamQuest Performance Software to Align IT with Business Priorities"
slug: teamquest-8-ec015b
page_type: study
author: "TeamQuest Corporation"
date: "2004-01-01"
study_type: vendor-whitepaper
subject_domain: "IT-performance-management"
methodology: "vendor-whitepaper, analyst-quote"
importance: medium
importance_rationale: "TeamQuest whitepaper represents vendor-use of Kastner/Aberdeen credentialing during the server-consolidation peak (2003-2006); documents how Aberdeen chief-research-officer commentary was packaged to support the business case for capacity-planning tools."
relevance: medium
relevance_rationale: "Server consolidation as a discrete 2000s category has largely been absorbed into virtualization (VMware), then cloud migration, then cloud FinOps. Capacity planning as a discipline is alive and well in modern SRE, FinOps, and AIOps practice. TeamQuest itself was acquired by Helpsystems 2018."
prescience: medium
prescience_rationale: "Kastner's millions-of-dollars-in-savings thesis for server recentralization was directionally correct and proved over the ensuing decade — VMware-driven consolidation drove 5-10x physical-server reduction in typical data centers by 2012. The specific 'recentralization' framing later shifted to 'cloud migration' (AWS, Azure, GCP 2010s) but the underlying consolidation-savings logic transferred intact."
license: CC-BY-4.0
tier: 2
entity_count: 4
tech_count: 4
obs_count: 5
tags: [type/study, importance/medium, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Using TeamQuest Performance Software to Align IT with Business Priorities

> TeamQuest Corporation whitepaper (2004, 7 pages) positioning TeamQuest performance-management software (TeamQuest Analyzer, TeamQuest Reporter, TeamQuest Model, TeamQuest View) as a vehicle for aligning IT operations with business priorities. The paper walks through capacity planning methods (benchmarking, trending, modeling — both simulation and analytic), workload characterization, service-level management, and server-consolidation use cases. Peter Kastner, chief research officer at Aberdeen Group Inc., is quoted in support of the server-consolidation thesis: 'For a large corporation, it's fairly easy to get to millions of dollars in savings through recentralization of servers and expensive IT support.' Document targets enterprise IT operations managers pursuing consolidation and capacity planning; published date 2004, copyright © 2004 TeamQuest Corporation; pre-dates the 2018 TeamQuest acquisition by Helpsystems (now Fortra).

**Author:** TeamQuest Corporation · **Date:** 2004-01-01 · **Type:** vendor-whitepaper
**Importance:** medium — *TeamQuest whitepaper represents vendor-use of Kastner/Aberdeen credentialing during the server-consolidation peak (2003-2006); documents how Aberdeen chief-research-officer commentary was packaged to support the business case for capacity-planning tools.*
**Prescience:** medium — *Kastner's millions-of-dollars-in-savings thesis for server recentralization was directionally correct and proved over the ensuing decade — VMware-driven consolidation drove 5-10x physical-server reduction in typical data centers by 2012. The specific 'recentralization' framing later shifted to 'clou…*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[helpsystems-fortra|Helpsystems / Fortra]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[teamquest-corp|TeamQuest Corporation]]

## Technologies (4)

- [[it-business-alignment|IT / business alignment]]
- [[it-capacity-planning|IT capacity planning / performance modeling]]
- [[server-consolidation|Server consolidation / data-center consolidation]]
- [[teamquest-performance-software|TeamQuest performance-management software suite]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'teamquest-8-ec015b' ORDER BY year_observed;
```

