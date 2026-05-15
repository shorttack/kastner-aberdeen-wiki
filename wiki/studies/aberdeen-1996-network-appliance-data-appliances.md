---
title: "Network Appliance: Data Appliances for Commercial Network Computing"
slug: aberdeen-1996-network-appliance-data-appliances
page_type: study
author: "Aberdeen Group"
date: "1996-11-01"
study_type: market-study
subject_domain: "network-attached-storage"
methodology: "industry-analysis, competitive-profiling, field-research"
importance: high
importance_rationale: "Aberdeen identified NetApp at the precise moment the NAS market was emerging as a distinct category; the study's framing of 'data appliance' as a product concept helped define the NAS segment and NetApp grew to become a $6B+ annual revenue company by 2024."
relevance: high
relevance_rationale: "NetApp remains a leading data infrastructure company (NASDAQ: NTAP, ~$6.3B revenue FY2024); the architectural principles of dedicated NAS vs. general-purpose servers underpin modern cloud storage and object storage design decisions."
prescience: high
prescience_rationale: "Aberdeen predicted NetApp would approach $100M revenue in FY1997 (actual FY1997 was ~$166M), and foresaw CIFS and HTTP multiprotocol support as the key differentiator—both proved foundational to NetApp's long-term dominance of enterprise NAS."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 7
obs_count: 22
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Network Appliance: Data Appliances for Commercial Network Computing

> Aberdeen Group profiles Network Appliance (NetApp) as a pioneer in network-attached storage (NAS) for commercial computing environments. The study examines NetApp's filer hardware (F220, F330, F540), Data ONTAP software with WAFL file system, and multiprotocol support (NFS, CIFS, HTTP). Aberdeen concludes NetApp is well-positioned to capitalize on the shift from application-server-based storage to dedicated network-attached data servers, citing revenue growth from $2M (1994) to $47M (FY1996) approaching $100M.

**Author:** Aberdeen Group · **Date:** 1996-11-01 · **Type:** market-study
**Importance:** high — *Aberdeen identified NetApp at the precise moment the NAS market was emerging as a distinct category; the study's framing of 'data appliance' as a product concept helped define the NAS segment and NetApp grew to become a $6B+ annual revenue company by 2024.*
**Prescience:** high — *Aberdeen predicted NetApp would approach $100M revenue in FY1997 (actual FY1997 was ~$166M), and foresaw CIFS and HTTP multiprotocol support as the key differentiator—both proved foundational to NetApp's long-term dominance of enterprise NAS.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[auspex-systems|Auspex Systems]]
- [[hewlett-packard|Hewlett-Packard]]
- [[legato-systems|Legato Systems]]
- [[network-appliance|Network Appliance, Inc. (NetApp)]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (7)

- [[cifs|CIFS (Common Internet File System)]]
- [[data-ontap|Data ONTAP]]
- [[ndmp|NDMP (Network Data Management Protocol)]]
- [[netapp-filers|NetApp Filer Hardware (F220/F330/F540)]]
- [[nfs|NFS (Network File System)]]
- [[raid-4|RAID 4]]
- [[wafl|WAFL (Write Anywhere File Layout)]]

## Key observations (top 25)

- **1996** — NetApp product strategy: Dedicated single-purpose NAS appliance: no user applications on data server; multiprotocol NFS/CIFS/HTTP
- **1994** — NetApp revenue FY1994: $2 million
- **1995** — NetApp revenue FY1995: $14.5 million
- **1996** — NetApp revenue FY1996: $47 million
- **1996** — NetApp FY1997 revenue forecast: FY1997 run-rate indicates fast approach to $100 million revenue mark
- **1997** — NetApp FY1997 revenue actual: NetApp actual FY1997 revenue approximately $166 million; exceeded $100M target
- **1996** — Data ONTAP WAFL performance claim: WAFL provides faster reads and writes over network than local storage attached to general-purpose servers
- **1996** — Data ONTAP availability rating: Data availability in excess of 99.99% via integrated RAID 4 and hot-spare drive reconstruction
- **1996** — Snapshot capability: Up to 20 simultaneous on-line read-only snapshots; enables online backup while applications are active
- **1996** — CIFS/multiprotocol differentiation: Only vendor providing seamless access to NFS, CIFS, and HTTP simultaneously on one filer
- **1996** — NDMP standard adoption prediction: NetApp leading NDMP standardization effort will result in greater centralized control and interoperable NAS backup ecosystem
- **2000** — NDMP standard adoption actual: NDMP became established industry standard for NAS backup; widely supported by backup vendors including Veritas, Legato, IBM
- **1996** — NetApp market mix commercial/technical: Revenue approximately evenly split between commercial and technical (CAD/CASE) application environments by 1996
- **1996** — Auspex competitive position: Single-function NAS competitor lacking CIFS/HTTP multiprotocol support
- **2001** — Auspex Systems fate: Auspex Systems ceased operations ~2000-2001; failed to compete with NetApp's multiprotocol approach
- **1996** — NetApp long-term NAS market leadership: NetApp's focus on advanced OS software features (vs. hardware) will keep it in the lead against competitors
- **2024** — NetApp long-term market position actual: NetApp became leading NAS/hybrid cloud storage vendor; NASDAQ: NTAP; $6.27B FY2024 revenue; industry leader for 30 years
- **1996** — NAS cyclical problem factor 1: performance degradation: Application response time degrades as more users share networked data; IS forced to upgrade application servers repeatedly
- **1996** — NAS cyclical problem factor 2: distributed data management: Data scattered across workstations and servers; expensive to maintain availability and backup
- **1996** — Aberdeen overall verdict on NetApp: IS decision makers responsible for networked computing 'ought to look at and closely evaluate NetApp — for an already proven solution'
- **1996** — HTML/Java management interface: NetApp plans HTML/Java-based administrative front-end across multiple workstations for lower operational costs
- **1999** — HTML/Java management interface delivery: NetApp delivered web-based management interfaces for ONTAP by late 1990s; became standard feature of NAS management

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-network-appliance-data-appliances' ORDER BY year_observed;
```

