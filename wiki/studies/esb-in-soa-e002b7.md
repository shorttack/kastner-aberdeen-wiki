---
title: "The ESB in the Land of SOA"
slug: esb-in-soa-e002b7
page_type: study
author: "William Mougayar"
date: "2005-12-07"
study_type: employer-record
subject_domain: "ESB; SOA integration; enterprise middleware; vendor landscape"
methodology: "Aberdeen survey-based research note; survey of 286 companies 'How SOA is Changing IT'; vendor landscape analysis"
importance: high
importance_rationale: "Rich primary survey data from 286 companies with multiple adoption metrics; comprehensive ESB vendor landscape (20+ named vendors); Aberdeen's three-phase evolution framework; foundational SOA-era ESB analysis with quantified findings."
relevance: high
relevance_rationale: "Central to understanding SOA middleware adoption patterns; named-vendor landscape still historically significant; survey data benchmarks enterprise SOA technology adoption in 2005."
prescience: high
prescience_rationale: "ESB evolution framework was accurate; the convergence toward service/process bus proved correct; governance/registry integration became standard. However, many ESB vendors were absorbed or became legacy as cloud-native API management and microservices emerged. The 'SOA purist WS-* vs. proprietary wrapper' tension was real but resolved differently than implied."
license: CC-BY-4.0
tier: 1
entity_count: 29
tech_count: 17
obs_count: 16
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# The ESB in the Land of SOA

> Aberdeen research note (5 pages) on the emergence of ESB as de-facto technology standard for integrating SOA infrastructure. Based on survey of 286 companies ('How SOA is Changing IT'): 60% of large company respondents are using or planning shared messaging services within 12 months; 76% implementing Web Services calls to existing applications; 73% implementing applications-related services. Kastner's three-phase ESB evolution framework: Message Bus (messaging) → Service Bus (orchestration) → Process Bus (mediation). Four-segment vendor landscape: ESB pioneers/SOA-specific, traditional EAI/EII players, platform vendors, process-centric integrators. Aberdeen conclusions: evaluate ESB extensibility; existing ESBs need to go beyond messaging to orchestration and mediation; don't neglect services registry and governance.

**Author:** William Mougayar · **Date:** 2005-12-07 · **Type:** employer-record
**Importance:** high — *Rich primary survey data from 286 companies with multiple adoption metrics; comprehensive ESB vendor landscape (20+ named vendors); Aberdeen's three-phase evolution framework; foundational SOA-era ESB analysis with quantified findings.*
**Prescience:** high — *ESB evolution framework was accurate; the convergence toward service/process bus proved correct; governance/registry integration became standard. However, many ESB vendors were absorbed or became legacy as cloud-native API management and microservices emerged. The 'SOA purist WS-* vs. proprietary wr…*

## Entities (29)

- [[aberdeen-group|Aberdeen Group]]
- [[amberpoint|AmberPoint]]
- [[axway|Axway]]
- [[bea-systems|BEA Systems]]
- [[cape-clear|Cape Clear Software]]
- [[cordys|Cordys]]
- [[fiorano-software|Fiorano Software]]
- [[fusionware|FusionWare]]
- [[ibm|IBM]]
- [[informatica|Informatica]]
- [[iona-technologies|IONA Technologies (Artix)]]
- [[iway-software|iWay Software]]
- [[jboss|JBoss (Red Hat)]]
- [[magic-software|Magic Software Enterprises]]
- [[metastorm|Metastorm]]
- [[microsoft|Microsoft]]
- [[oracle|Oracle]]
- [[peter-kastner|Peter S. Kastner]]
- [[polarlake|PolarLake]]
- [[rick-saia|Rick Saia]]
- [[sap|SAP]]
- [[software-ag|Software AG]]
- [[sonic-software|Sonic Software]]
- [[sterling-commerce|Sterling Commerce]]
- [[sun-seebeyond|Sun Microsystems (SeeBeyond)]]
- [[tibco|TIBCO Software]]
- [[vitria-technology|Vitria Technology]]
- [[webmethods|webMethods]]
- [[william-mougayar|William Mougayar]]

## Technologies (17)

- [[bea-aqualogic-service-bus|BEA AquaLogic Service Bus]]
- [[business-process-management|Business Process Management (BPM) / Process Bus]]
- [[business-process-workflows|Business Process / Workflow Services]]
- [[composite-applications|Composite Applications]]
- [[enterprise-application-integration-eai|Enterprise Application Integration (EAI)]]
- [[enterprise-service-bus|Enterprise Service Bus (ESB)]]
- [[ibm-websphere-esb|IBM WebSphere ESB]]
- [[message-oriented-middleware|Message-Oriented Middleware (MOM) / Enterprise Messaging]]
- [[microsoft-biztalk|Microsoft BizTalk Server]]
- [[sap-netweaver|SAP NetWeaver]]
- [[service-oriented-architecture|Service-Oriented Architecture (SOA)]]
- [[services-orchestration|Services Orchestration]]
- [[soa-governance-management|SOA Governance / Management of Services]]
- [[soa-services-registry|SOA Services Registry / UDDI]]
- [[web-services|Web Services (XML/SOAP/WSDL/UDDI)]]
- [[ws-star-standards|WS-* Standards Stack]]
- [[xml-gateway-adapters|XML Gateways / Adapters]]

## Key observations (top 25)

- **2005** — Large company shared messaging adoption: 60% using or planning shared messaging services within 12 months
- **2005** — Web Services calls to existing apps — adoption: 76% have implemented or plan web services calls to existing applications within 12 months
- **2005** — Applications-related services adoption: 73% implementing or planning applications-related services within 12 months
- **2005** — Business process/workflow services adoption: 69% currently use or plan business process/workflow services within 12 months
- **2005** — XML gateways/adapters adoption: 65% currently use or plan XML gateways/adapters within 12 months
- **2005** — Shared messaging services (bus/registry) adoption: 60% implementing or planning shared messaging services (registry or bus) within 12 months
- **2005** — SOA governance/management of services adoption: 58% implementing or planning governance/management of services within 12 months
- **2005** — Composite applications adoption: 49% currently use or plan composite applications within 12 months
- **2005** — ESB market current phase: most of the market is in second wave (services orchestration phase)
- **2005** — ESB future evolution: ESB of the future will interact with/inherit Services Registry, exhibit policy/governance management, and interact with specialized data bus
- **2005** — ESB SOA methodology vs. product distinction: Adopting SOA is about choosing methodology rather than buying a product; traditional ESB was a finite-task product
- **2005** — SOA purist ESB definition: True ESB must religiously adhere to WS-* stack; proprietary middleware wrappers do not qualify
- **2005** — ESB vendor landscape segments: 4 segments: ESB pioneers/SOA-specific; traditional EAI/EII; application/integration platforms; process-centric
- **2005** — ESB selection guidance: Evaluate ESB extensibility; go beyond messaging to orchestration/mediation; include registry/governance; investigate at least one vendor per segment
- **2005** — ESB-services interdependence: As companies increase quantity of services, demand for more comprehensive ESBs increases commensurably
- **2005** — Process-centric ESB vendor limitations: Strong on BPM but does not offer granularity of services; weak on architectural scalability; marriage with SOA pioneers could be powerful

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'esb-in-soa-e002b7' ORDER BY year_observed;
```

