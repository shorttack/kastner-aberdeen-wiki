---
title: "Digital's ObjectBroker -- Advanced Integration of Distributed Resources"
slug: aberdeen-1995-digital-objectbroker
page_type: study
author: "Aberdeen Group"
date: "1995-08-01"
study_type: product-profile
subject_domain: "distributed-object-computing"
methodology: "industry-analysis,competitive-profiling,field-research"
importance: high
importance_rationale: "CORBA and ORB technology were the central distributed computing standard battle of the mid-1990s with 450+ industry supporters; Aberdeen's analysis of ObjectBroker informed Fortune 1000 integration architecture decisions worth billions."
relevance: medium
relevance_rationale: "CORBA itself is largely obsolete but the architectural patterns (distributed object invocation, IDL contracts, platform-neutral integration) directly prefigure gRPC, Protobuf, and microservices. The ORB as middleware concept transferred to ESB, API gateways, and service mesh."
prescience: low
prescience_rationale: "Core predictions failed: OLE-CORBA interop was abandoned by Microsoft, DEC/ObjectBroker was discontinued after Compaq acquisition in 1998, and CORBA was supplanted by SOAP/REST/microservices. Only short-term 2.6 feature roadmap was confirmed."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 19
obs_count: 55
tags: [type/study, importance/high, prescience/low, decade/1990s]
source_csv: master_studies.csv
---

# Digital's ObjectBroker -- Advanced Integration of Distributed Resources

> Profile evaluating Digital Equipment Corporation's ObjectBroker, a CORBA-compliant object request broker for integrating distributed heterogeneous resources. Examines ORB technology, legacy system encapsulation, OLE-COM integration, and 19-platform support.

**Author:** Aberdeen Group · **Date:** 1995-08-01 · **Type:** product-profile
**Importance:** high — *CORBA and ORB technology were the central distributed computing standard battle of the mid-1990s with 450+ industry supporters; Aberdeen's analysis of ObjectBroker informed Fortune 1000 integration architecture decisions worth billions.*
**Prescience:** low — *Core predictions failed: OLE-CORBA interop was abandoned by Microsoft, DEC/ObjectBroker was discontinued after Compaq acquisition in 1998, and CORBA was supplanted by SOAP/REST/microservices. Only short-term 2.6 feature roadmap was confirmed.*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[digital-equipment-corporation|Digital Equipment Corporation]]
- [[electronic-data-systems|Electronic Data Systems]]
- [[linkvest|Linkvest]]
- [[logica-north-america-inc|Logica North America Inc]]
- [[microsoft-corporation|Microsoft Corporation]]
- [[netlinks-technology|NetLinks Technology]]
- [[object-management-group|Object Management Group]]
- [[protosoft-inc|Protosoft Inc]]
- [[tandem-computers|Tandem Computers]]
- [[the-cushing-group|The Cushing Group]]

## Technologies (19)

- [[ACA_SERVICES|ACA Services]]
- [[GSS_API|GSS-API (Generic Security Services API)]]
- [[PARADIGM_PLUS|Paradigm Plus]]
- [[c-language-binding|C++ Language Binding]]
- [[com-component-object-model|COM (Component Object Model)]]
- [[corba-common-object-request-broker-architecture|CORBA (Common Object Request Broker Architecture)]]
- [[dce-distributed-computing-environment|DCE (Distributed Computing Environment)]]
- [[dde-dynamic-data-exchange|DDE (Dynamic Data Exchange)]]
- [[digital-objectbroker|Digital ObjectBroker]]
- [[implementation-mapping-language-iml|Implementation Mapping Language (IML)]]
- [[interface-definition-language-idl|Interface Definition Language (IDL)]]
- [[method-mapping-language-mml|Method Mapping Language (MML)]]
- [[nas-network-application-support|NAS (Network Application Support)]]
- [[object-request-broker-orb|Object Request Broker (ORB)]]
- [[objectplus|ObjectPlus]]
- [[ole-object-linking-and-embedding|OLE (Object Linking and Embedding)]]
- [[openvms|OpenVMS]]
- [[powerbuilder|PowerBuilder]]
- [[visual-basic|Visual Basic]]

## Key observations (top 25)

- **1995** — ObjectBroker runtime pricing: $149
- **1995** — ObjectBroker Unix development pricing: $5000
- **1995** — ObjectBroker NT development pricing: $980
- **1995** — ObjectBroker runtime pricing model: per-machine hardware-tiered with volume discounts
- **1995** — ObjectBroker version at publication: 2.5
- **1995** — Platform count: 19 platform combinations
- **1995** — CORBA compliance version: CORBA 1.2
- **1995** — CORBA 2.0 roadmap: Planned for ObjectBroker 2.6
- **1995** — IDL language bindings in v2.5: C binding, Visual Basic DLL binding
- **1995** — IDL C++ binding roadmap: Planned for ObjectBroker 2.6
- **1995** — ObjectBroker first release year: 1991
- **1995** — NAS inclusion: >50% of Digital installed base
- **1995** — Core component: ORB Core: ORB Core
- **1995** — Core component: Repositories: IDL, IML, MML Repositories
- **1995** — Core component: Registries: Configuration Registries
- **1995** — Core component: Context Objects: Context Objects
- **1995** — Graphical utilities: Systems Administrator, Network Tester, Context Object Editor, Repository Manager, Implementation Viewer, OLE Network Portal, DDE Listener
- **1995** — Skeleton Server: Wraps callable APIs with IDL interface
- **1995** — Script Server: Wraps command line interfaces
- **1995** — OLE Network Portal: OLE 2.0 interface to ObjectBroker registry
- **1995** — DDE Gateway: Legacy DDE message bridge
- **1995** — Legacy system encapsulation: CORBA wrapper for legacy/procedural code
- **1995** — Application Partitioning via IML/MML: IML: describe object implementations; MML: select among implementations
- **1995** — CORBA/OLE coexistence strategy: Dual-standard bridging architecture
- **1995** — ObjectBroker 2.6 announcement: GA expected early 1996

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-digital-objectbroker' ORDER BY year_observed;
```

