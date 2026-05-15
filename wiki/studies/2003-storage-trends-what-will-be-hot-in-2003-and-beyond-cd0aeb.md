---
title: "Storage Trends: What Will Be Hot in 2003 — And Beyond"
slug: 2003-storage-trends-what-will-be-hot-in-2003-and-beyond-cd0aeb
page_type: study
author: "David Hill"
date: "2002-12-31"
study_type: market-study
subject_domain: "storage-infrastructure"
methodology: "industry-analysis|expert-opinion|competitive-profiling"
importance: high
importance_rationale: "Published at year-end 2002 as a comprehensive technology forecast, this study covered the emerging storage networking landscape at a defining moment when SAN, NAS, and iSCSI were converging and storage automation was nascent. Hill's framing of the 'IT utility' and 'storage utility' anticipated cloud storage by several years, making this an unusually forward-thinking Aberdeen InSight."
relevance: high
relevance_rationale: "Storage automation, resource pooling, policy-driven management, and the IT utility concept are now foundational to cloud and enterprise storage architectures. iSCSI, virtualization, and converged infrastructure all materialized as Hill predicted. The specific technology taxonomy remains valuable for understanding modern storage evolution."
prescience: high
prescience_rationale: "Hill's predictions were remarkably prescient: storage automation became central to enterprise IT, SAN and NAS both persisted and converged, iSCSI emerged as a cost-effective SAN alternative, the 'IT utility' model materialized as cloud storage (AWS S3 launched 2006), and tape automation remained relevant for backup/archive through the 2020s."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 9
obs_count: 15
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Storage Trends: What Will Be Hot in 2003 — And Beyond

> Aberdeen Group analyst David Hill forecasts the storage infrastructure landscape for 2003 and beyond, identifying a long-term transformation of the data center through storage automation, resource pooling, provisioning, and policy-driven management. In the short term, Hill predicts buyers will focus on storage staples (SAN, NAS, iSCSI, backup/restore, tape automation, disk arrays) even as attention turns to automation and virtualization. The study covers namespace management, global file systems, network storage technologies, and the emerging concept of the IT utility.

**Author:** David Hill · **Date:** 2002-12-31 · **Type:** market-study
**Importance:** high — *Published at year-end 2002 as a comprehensive technology forecast, this study covered the emerging storage networking landscape at a defining moment when SAN, NAS, and iSCSI were converging and storage automation was nascent. Hill's framing of the 'IT utility' and 'storage utility' anticipated cloud…*
**Prescience:** high — *Hill's predictions were remarkably prescient: storage automation became central to enterprise IT, SAN and NAS both persisted and converged, iSCSI emerged as a cost-effective SAN alternative, the 'IT utility' model materialized as cloud storage (AWS S3 launched 2006), and tape automation remained rel…*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[emc|EMC Corporation]]
- [[hitachi-hds|Hitachi Data Systems]]
- [[hp-storage|Hewlett-Packard (Storage)]]
- [[ibm-storage|IBM (Storage Division)]]
- [[network-appliance|Network Appliance (NetApp)]]
- [[storagetek|StorageTek]]

## Technologies (9)

- [[disk-array|Disk Array / RAID]]
- [[global-file-system|Global File System / Namespace]]
- [[iscsi|iSCSI (Internet Small Computer Systems Interface)]]
- [[it-utility|IT Utility / Storage Utility]]
- [[nas|Network Attached Storage (NAS)]]
- [[san|Storage Area Network (SAN)]]
- [[storage-automation|Storage Automation]]
- [[storage-virtualization|Storage Virtualization]]
- [[tape-automation|Tape Automation]]

## Key observations (top 25)

- **2003** — Long-term storage infrastructure transformation: Data center will be re-architected via storage automation for resource pooling and policy-driven management
- **2003** — SAN market short-term demand: Strong — buyers will focus on storage staples including SAN
- **2003** — NAS market short-term demand: Strong — NAS among storage staples buyers will continue buying
- **2003** — iSCSI market trajectory: Emerging — listed as key storage technology to watch in 2003+
- **2003** — Tape automation role: Continued relevance for backup/restore in near-term
- **2003** — Disk array market status: Mature staple — primary near-term storage buyer focus
- **2003** — Storage virtualization adoption trajectory: Will become key enabling technology for data center re-architecture
- **2003** — IT utility / storage utility emergence: Storage will evolve toward utility computing model
- **2003** — Global file system / namespace development: Single-image global file system will emerge as data center infrastructure
- **2003** — HP open SAN market share Q3 2003: 31.2% revenue share in open SAN market
- **2003** — Open SAN market growth rate Q3 2003: 15.7% year-over-year growth
- **2003** — EMC external storage market share 2003: 20.6% ($2.65B revenues)
- **2003** — Worldwide external controller-based disk storage market 2003: $12.89 billion total
- **2010** — Storage automation long-term adoption: Became foundational — virtualization enabled by 2010; 72% of orgs at least 25% virtual
- **2006** — IT utility / cloud storage emergence: AWS S3 launched March 2006 as first mass-market storage utility

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2003-storage-trends-what-will-be-hot-in-2003-and-beyond-cd0aeb' ORDER BY year_observed;
```

