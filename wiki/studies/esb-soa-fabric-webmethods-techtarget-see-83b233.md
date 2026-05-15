---
title: "The traditional ESB gets weaved into an SOA fabric"
slug: esb-soa-fabric-webmethods-techtarget-see-83b233
page_type: study
author: "Rich Seeley, SearchWebServices / TechTarget"
date: "2006-12-21"
study_type: news-article
subject_domain: "soa-esb-middleware"
methodology: "product-analysis, analyst-commentary, industry-trend-analysis"
importance: high
importance_rationale: "Documents a pivotal moment in SOA/ESB/BPM convergence — the 2006 year when 'fabric' replaced 'bus' as the organizing metaphor for integration infrastructure. Kastner's 50% Global 5000 BPM adoption statistic is a landmark data point in SOA-era IT statistics, widely cited in subsequent trade-press and analyst reports. Also noteworthy for Kastner's public acknowledgment that his prior EAI-death prediction was wrong — a rare analyst-self-correction moment."
relevance: medium
relevance_rationale: "ESB/SOA terminology largely displaced by microservices + API gateway + service mesh by 2020. BPM evolved into workflow-automation / iBPMS / low-code-automation. However, the underlying enterprise-integration problem (composite apps, legacy-system connectivity, governance) remains central, and Kastner's 'most customers don't abandon investments' lesson applies directly to current monolith-to-microservices migrations."
prescience: high
prescience_rationale: "Kastner's 50% Global 5000 BPM engagement statistic was validated by subsequent Gartner/Forrester surveys and directly foreshadowed the 2010s iBPMS / workflow-automation boom (Pegasystems, Appian). His EAI-persistence finding (customers don't abandon legacy integration investments) is an enduring architectural pattern — the same dynamic plays out in monolith-to-microservices and mainframe-to-cloud migrations today. Fabric-over-bus terminology evolved into service-mesh / API-mesh."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 7
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# The traditional ESB gets weaved into an SOA fabric

> SearchWebServices / TechTarget article (Dec 21 2006, Rich Seeley) on the evolution of the enterprise service bus (ESB) category, triggered by the launch of webMethods Fabric 7.0. Peter S. Kastner, VP Enterprise Integration at Aberdeen Group, is a central voice. His key findings: (1) EAI is not dead — 'We found almost nobody who is willing to abandon their investments in EAI just to buy an ESB'; (2) 'My hypothesis going into the year was that the EAI companies would take it on the chin. The reality is the vast majority of their customers are fairly easily connecting SOA via adapters to their EAI fabric or infrastructure' — Kastner publicly updates his prior prediction; (3) BPM-ESB convergence is widespread: 'We're seeing at this point that roughly 50 percent of the Global 5000 are actively engaged in business process management development.' AMR Research's Bill Swanton and webMethods CTO Marc Breissinger round out the SOA-BPM-ESB convergence narrative. Burton Group's 'middleware fabric' terminology is cited.

**Author:** Rich Seeley, SearchWebServices / TechTarget · **Date:** 2006-12-21 · **Type:** news-article
**Importance:** high — *Documents a pivotal moment in SOA/ESB/BPM convergence — the 2006 year when 'fabric' replaced 'bus' as the organizing metaphor for integration infrastructure. Kastner's 50% Global 5000 BPM adoption statistic is a landmark data point in SOA-era IT statistics, widely cited in subsequent trade-press and…*
**Prescience:** high — *Kastner's 50% Global 5000 BPM engagement statistic was validated by subsequent Gartner/Forrester surveys and directly foreshadowed the 2010s iBPMS / workflow-automation boom (Pegasystems, Appian). His EAI-persistence finding (customers don't abandon legacy integration investments) is an enduring arc…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[amr-research|AMR Research]]
- [[bill-swanton-amr|Bill Swanton]]
- [[burton-group|Burton Group]]
- [[fiorano-software|Fiorano Software]]
- [[marc-breissinger-webmethods|Marc Breissinger]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[rich-seeley-techtarget|Rich Seeley]]
- [[software-ag|Software AG]]
- [[techtarget|TechTarget Inc.]]
- [[tibco-software|TIBCO Software Inc.]]
- [[webmethods|webMethods, Inc.]]

## Technologies (7)

- [[bam|Business Activity Monitoring (BAM)]]
- [[bpm|Business Process Management (BPM)]]
- [[eai|Enterprise Application Integration (EAI)]]
- [[esb|Enterprise Service Bus (ESB)]]
- [[middleware-fabric|Middleware fabric / Web services fabric]]
- [[soa|Service-Oriented Architecture (SOA)]]
- [[webmethods-fabric-7|webMethods Fabric 7.0]]

## Key observations (top 25)

- **2006** — Kastner EAI-persistence finding: 'We found almost nobody who is willing to abandon their investments in EAI just to buy an ESB to say that they own one.' — Peter S. Kastner, Aberdeen Group
- **2006** — Kastner self-correction on EAI death: 'My hypothesis going into the year was that the EAI companies would take it on the chin. The reality is the vast majority of their customers are fairly easily connecting SOA via adapters to their EAI fabric or infrastructure.' — Kastner publicly upda…
- **2006** — Kastner 50% Global 5000 BPM-engagement statistic: 'We're seeing at this point that roughly 50 percent of the Global 5000 are actively engaged in business process management development.' — Peter S. Kastner, VP Enterprise Integration, Aberdeen Group
- **2006** — Kastner on TIBCO and Fiorano BPM investment: 'Tibco has invested heavily in BPM over the last several years. Fiorano also beefed up their ESB product significantly in the BPM space in the last six months.' — Kastner
- **2006** — Swanton on webMethods Fabric 7.0 integration: 'The thing that we see in webMethods Fabric 7.0 is a really straightforward development environment for building composite applications in an SOA fashion.' — Bill Swanton, AMR Research
- **2006** — webMethods Fabric 7.0 launch: webMethods announced Fabric 7.0 this week combining EAI, ESB, BPM, BAM, registry/repository, governance
- **2006** — Breissinger fabric-terminology framing: 'Integration backbones -> service buses -> fabric' progression; 'fabric is the same concept taken one step further to include the business process management and the analytics and the composite application development capabilities' — Marc Breissinger…
- **2007** — Software AG acquires webMethods: Software AG acquired webMethods in June 2007 for approximately $546M, folding Fabric 7.0 into its integration portfolio
- **2015** — ESB terminology displaced by microservices + API gateway: By 2015 ESB-centric integration architectures had been largely displaced by microservices with API gateway and later service mesh (Istio 2017). Kastner's fabric-terminology moment was a waypoint in that evolution.
- **2015** — BPM matures into iBPMS / workflow automation: By 2015 BPM had evolved into iBPMS (intelligent BPMS, per Gartner) and low-code workflow automation platforms (Pegasystems, Appian, ServiceNow workflows), validating Kastner's 50% Global 5000 adoption trajectory

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'esb-soa-fabric-webmethods-techtarget-see-83b233' ORDER BY year_observed;
```

