---
title: "Network Storage: Obtaining the Payoff for Your Enterprise"
slug: 1997-network-storage--obtaining-the-payo-3bdc3d
page_type: study
author: "David Hill (Aberdeen Group)"
date: "1997"
study_type: Technology Viewpoint (Abstract Only)
subject_domain: "Network Storage / Enterprise Storage Architecture"
methodology: "Analyst viewpoint; strategic framework development"
importance: high
importance_rationale: "Historically important as an early industry analyst call for enterprise-wide network storage (NAS/SAN) adoption. David Hill was an influential storage analyst; this represents the beginning of the NAS/SAN market advocacy wave that drove enormous investment in the late 1990s and 2000s. The technology viewpoint format captures a pivotal inflection point in storage architecture thinking."
relevance: high
relevance_rationale: "Highly relevant to historians of enterprise storage, cloud computing origins, and IT infrastructure evolution. The 'storage as network' framing directly prefigures cloud object storage (S3, Azure Blob). The labor-intensive management of server-attached storage is a pain point that drove NetApp, EMC, and ultimately AWS S3 to massive adoption."
prescience: high
prescience_rationale: "Exceptionally prescient. Every major prediction in this abstract proved accurate: traditional storage architectures did become inadequate; enterprises that failed to adopt network storage did overpay and face management complexity; NAS and SAN became dominant; and the 'storage as a giant network' vision maps directly to modern cloud storage. The study was ahead of the mainstream enterprise adoption curve by approximately 3-5 years."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 5
obs_count: 12
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Network Storage: Obtaining the Payoff for Your Enterprise

> Aberdeen Group Technology Viewpoint by David Hill arguing that traditional server-centric Global 2000 enterprise storage architectures will become inadequate as high-data-volume applications emerge. Advocates for treating enterprise storage as a network — independent from servers — to achieve throughput, flexibility, and manageability. Provides a framework for adopting new network storage facilities. NOTE: Only the abstract (1,254 characters) is available; full report was behind Aberdeen paywall.

**Author:** David Hill (Aberdeen Group) · **Date:** 1997 · **Type:** Technology Viewpoint (Abstract Only)
**Importance:** high — *Historically important as an early industry analyst call for enterprise-wide network storage (NAS/SAN) adoption. David Hill was an influential storage analyst; this represents the beginning of the NAS/SAN market advocacy wave that drove enormous investment in the late 1990s and 2000s. The technology…*
**Prescience:** high — *Exceptionally prescient. Every major prediction in this abstract proved accurate: traditional storage architectures did become inadequate; enterprises that failed to adopt network storage did overpay and face management complexity; NAS and SAN became dominant; and the 'storage as a giant network' vi…*

## Entities (5)

- [[ENT-ABD-001|Aberdeen Group Inc.]]
- [[ENT-EMC-001|EMC Corporation]]
- [[ENT-G2000-001|Global 2000 Enterprises]]
- [[ENT-HILL-001|David Hill]]
- [[ENT-NETAPP-001|Network Appliance (NetApp)]]

## Technologies (5)

- [[TECH-DAS-001|Direct-Attached Storage (DAS)]]
- [[TECH-FIBRE-001|Fibre Channel]]
- [[TECH-NAS-001|Network-Attached Storage (NAS)]]
- [[TECH-NFS-001|Network File System (NFS)]]
- [[TECH-SAN-001|Storage Area Network (SAN)]]

## Key observations (top 25)

- **1997** — traditional_storage_adequacy: Traditional storage architectures will soon become inadequate for Global 2000 enterprises
- **2005** — traditional_storage_adequacy_outcome: Traditional DAS architectures were largely displaced by NAS/SAN in Global 2000 enterprises by 2005
- **1997** — network_storage_cost_advantage: Enterprises that fail to adopt network storage will overpay for storage
- **1997** — server_dependent_storage_management: Server-dependent storage leads to extreme labor-intensive management difficulties
- **2010** — nas_san_adoption_outcome: NAS and SAN became dominant enterprise storage; cloud storage extended the model to internet scale
- **1997** — network_storage_server_independence: New network storage facilities should have greater server independence than previous generations
- **1997** — network_storage_framework_factor_throughput: Throughput as key requirement for network storage architecture
- **1997** — network_storage_framework_factor_flexibility: Flexibility as key requirement for network storage architecture
- **1997** — network_storage_framework_factor_manageability: Manageability as key requirement for network storage architecture
- **1997** — legacy_storage_architecture_prevalence: Most Global 2000 enterprises using decades-old storage architectures as of 1997
- **1997** — high_volume_applications_trigger: New high-data-volume applications will trigger storage architecture failures
- **2006** — cloud_storage_model: AWS S3 launched 2006 extending network storage to cloud scale; validates server-independent storage model

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-network-storage--obtaining-the-payo-3bdc3d' ORDER BY year_observed;
```

