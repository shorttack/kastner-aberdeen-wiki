---
title: "InfoWorld — Dell sharpens blade attack: PowerEdge 1655MC server blades (Neel, 8-Apr-2002)"
slug: infoworld-dell-sharpens-blade-attack-nee-f9cb9c
page_type: study
author: "Dan Neel — InfoWorld Magazine"
date: "2002-04-08"
study_type: trade-press-feature
subject_domain: "server-blades-and-modular-computing"
methodology: "journalistic-reporting-with-analyst-quotes"
importance: medium
importance_rationale: "Documents Dell's late entry into the server-blade market — a key inflection point in commodity-server consolidation. Kastner quoted as 'chief research officer of Aberdeen Group in Boston' — title evolution from 'Vice President' (Studies 6-9) reflecting Aberdeen's organizational evolution. Companion to Batch 20 hostingtech-apple-xserve-asia-zieger-200-052af6 (Nov 2002) which also uses CRO title."
relevance: medium
relevance_rationale: "Direct primary-source Kastner quote (CRO era) on Dell blade strategy. Captures Aberdeen's 2002 view of Dell's commodity-server scaling and the blade vs. brick architecture debate. Provides title-evolution evidence (VP → CRO) at Aberdeen between 1999 (Study 9) and 2002. Co-references Compaq blade products (HP merger context per Batch 20 SIA-Compaq study)."
prescience: high
prescience_rationale: "The blade-then-brick roadmap anticipated modern hyperscale designs (Open Compute Project disaggregated racks, AWS Nitro/Graviton custom silicon, Microsoft Azure rack-scale). Dell's 'flexibility and agility' thesis (per Kastner) anticipated the hyperconverged-infrastructure (HCI) movement and ultimately cloud-native bare-metal-as-a-service. The InfiniBand+Microsoft partnership presaged the GPU-cluster networking that powers modern AI workloads."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 6
obs_count: 11
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# InfoWorld — Dell sharpens blade attack: PowerEdge 1655MC server blades (Neel, 8-Apr-2002)

> InfoWorld Magazine April 8, 2002 (circulation 225,047 weekly, San Mateo CA) feature by Dan Neel reporting on Dell's announcement at its spring analyst meeting in New York of the PowerEdge 1655MC server blades — Dell's first blade server entry, scheduled for third-quarter shipping. Article positions Dell as joining a 'groundswell' of competitors (HP, Compaq, others) capitalizing on IT executive interest in server blades. PowerEdge 1655MC hosts six dual-processor Intel Pentium III blades in a 5.25-inch rack — described as a precursor to Dell's future 'brick' servers (multiple servers per chassis, customer-assembled blocks of storage and memory). Quotes Peter Kastner, chief research officer of Aberdeen Group in Boston: 'Dell is trying to maintain a flexibility and an agility that is at the core of their business.' Notes 1655MC density limit (only 84 blades in standard rack vs. Compaq's hundreds), but Dell defends with VP Randy Groves saying competitors 'have focused on customers willing to sacrifice performance for space and power reasons. We don't see much of that.' Article notes Dell's parallel InfiniBand partnership with Microsoft. Dell hardware roadmap moves blade → modular brick → shared power/cooling decreasing data-center costs.

**Author:** Dan Neel — InfoWorld Magazine · **Date:** 2002-04-08 · **Type:** trade-press-feature
**Importance:** medium — *Documents Dell's late entry into the server-blade market — a key inflection point in commodity-server consolidation. Kastner quoted as 'chief research officer of Aberdeen Group in Boston' — title evolution from 'Vice President' (Studies 6-9) reflecting Aberdeen's organizational evolution. Companion…*
**Prescience:** high — *The blade-then-brick roadmap anticipated modern hyperscale designs (Open Compute Project disaggregated racks, AWS Nitro/Graviton custom silicon, Microsoft Azure rack-scale). Dell's 'flexibility and agility' thesis (per Kastner) anticipated the hyperconverged-infrastructure (HCI) movement and ultimat…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq-computer|Compaq Computer]]
- [[dan-neel|Dan Neel]]
- [[dell-inc|Dell Inc.]]
- [[hewlett-packard|Hewlett-Packard]]
- [[infoworld-magazine|InfoWorld Magazine]]
- [[intel-corporation|Intel Corporation]]
- [[microsoft-corporation|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[randy-groves|Randy Groves]]

## Technologies (6)

- [[dell-poweredge-1655mc|Dell PowerEdge 1655MC]]
- [[hp-bladeservers|HP/Compaq Server Blades]]
- [[infiniband|InfiniBand]]
- [[intel-pentium-iii|Intel Pentium III]]
- [[server-blades|Server Blades]]
- [[server-bricks|Server Bricks (Modular Computing)]]

## Key observations (top 25)

- **2002** — memorable_quote: Dell-trying-to-maintain-flexibility-and-agility-at-core-of-business
- **2002** — title: chief-research-officer-Aberdeen-Group
- **2002** — weekly_circulation: 225047
- **2002** — blades_per_5_25_rack: 6
- **2002** — blades_per_standard_rack_compaq: hundreds
- **2002** — blades_per_standard_rack: 84
- **2002** — processor_family: Intel-Pentium-III-dual
- **2002** — partnership: Dell-Microsoft-InfiniBand
- **2002** — roadmap: blades-to-bricks-to-shared-power-and-cooling
- **2002** — memorable_quote: competitors-focused-on-customers-willing-to-sacrifice-performance-for-space
- **2002** — drivers: consolidation-power-reduction-management-flexibility

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'infoworld-dell-sharpens-blade-attack-nee-f9cb9c' ORDER BY year_observed;
```

