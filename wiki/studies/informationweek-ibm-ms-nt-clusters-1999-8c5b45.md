---
title: "IBM, Microsoft Team On NT Clusters"
slug: informationweek-ibm-ms-nt-clusters-1999-8c5b45
page_type: study
author: "InformationWeek staff"
date: "1999-05-21"
study_type: news-article
subject_domain: "windows-nt-clustering-enterprise-servers"
methodology: "news-reporting, expert-quote"
importance: medium
importance_rationale: "Documents the early-1999 push past two-node Microsoft Cluster Services limits — a key constraint that delayed Windows from credibly hosting tier-1 enterprise workloads."
relevance: low
relevance_rationale: "Cornhusker/Netfinity-era clustering is fully obsolete; modern Windows uses different high-availability architectures (Hyper-V failover, Azure Stack, S2D)."
prescience: medium
prescience_rationale: "Kastner correctly identified that enterprise demand for >2-node NT clusters was real and unmet, foreshadowing Windows 2000 Datacenter (4-node) and later Windows Server 2003 8-node clustering."
license: CC-BY-4.0
tier: 2
entity_count: 9
tech_count: 5
obs_count: 6
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# IBM, Microsoft Team On NT Clusters

> InformationWeek reports IBM's TechEd '99 demonstration of an eight-server Windows NT cluster code-named 'Cornhusker'. The IBM clustering technology is compatible with Microsoft Cluster Services and certified initially only on IBM Netfinity NT servers. Peter Kastner, research director and EVP at Aberdeen Group, observes that an increasing number of enterprise customers are embracing NT-based clustering and being constrained by two-node limits, predicting warm reception for Cornhusker among critical-application operators.

**Author:** InformationWeek staff · **Date:** 1999-05-21 · **Type:** news-article
**Importance:** medium — *Documents the early-1999 push past two-node Microsoft Cluster Services limits — a key constraint that delayed Windows from credibly hosting tier-1 enterprise workloads.*
**Prescience:** medium — *Kastner correctly identified that enterprise demand for >2-node NT clusters was real and unmet, foreshadowing Windows 2000 Datacenter (4-node) and later Windows Server 2003 8-node clustering.*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[answer-financial|Answer Financial Inc.]]
- [[ibm-corp|IBM Corporation]]
- [[ibm-netfinity|IBM Netfinity]]
- [[informationweek|InformationWeek]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sequent-computer-systems|Sequent Computer Systems Inc.]]
- [[tanveer-khan|Tanveer Khan]]

## Technologies (5)

- [[ibm-cornhusker|IBM Cornhusker (8-node NT cluster)]]
- [[microsoft-cluster-services|Microsoft Cluster Services (MSCS)]]
- [[microsoft-datacenter-server|Microsoft Datacenter Server]]
- [[windows-2000-advanced-server|Windows 2000 Advanced Server]]
- [[windows-nt-server|Windows NT Server 4.0 Enterprise Edition]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'informationweek-ibm-ms-nt-clusters-1999-8c5b45' ORDER BY year_observed;
```

