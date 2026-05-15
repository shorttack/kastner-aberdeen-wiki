---
title: "Classification of Key Applications by Storage Category"
slug: 15-classification-key-applications-55b6be
page_type: study
author: "Aberdeen Group (David Hill)"
date: "2003-01-01"
study_type: case-analysis
subject_domain: "enterprise-storage"
methodology: "industry-analysis"
importance: high
importance_rationale: "First structured application-to-storage-access mapping produced as part of Aberdeen/Maxtor's midline storage category creation effort; directly shaped the commercial rationale for differentiated storage tiers."
relevance: high
relevance_rationale: "Application I/O pattern taxonomy remains foundational to storage tiering and ILM architectures; the categories and their read/write descriptions are still used in modern storage design."
prescience: high
prescience_rationale: "Predicted that different workloads require differentiated storage tiers (performance vs. nearline vs. archive); this tiered ILM model became industry standard and is the basis of modern cloud storage classes (hot/warm/cold)."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 10
obs_count: 15
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Classification of Key Applications by Storage Category

> A concise classification matrix mapping eight major enterprise application types to their data access characteristics (read/write patterns and data structures). The framework distinguishes Traditional OLTP, Contemporary OLTP, Business Intelligence, Web Applications, Personal Productivity, Interactive Design, Unique Large Files, and Large File Distribution. This taxonomy serves as the foundational analytical framework supporting Maxtor's midline storage category creation project.

**Author:** Aberdeen Group (David Hill) · **Date:** 2003-01-01 · **Type:** case-analysis
**Importance:** high — *First structured application-to-storage-access mapping produced as part of Aberdeen/Maxtor's midline storage category creation effort; directly shaped the commercial rationale for differentiated storage tiers.*
**Prescience:** high — *Predicted that different workloads require differentiated storage tiers (performance vs. nearline vs. archive); this tiered ILM model became industry standard and is the basis of modern cloud storage classes (hot/warm/cold).*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[maxtor|Maxtor Corporation]]
- [[sap|SAP]]

## Technologies (10)

- [[business-intelligence|Business Intelligence / Data Warehousing]]
- [[cad-cam|CAD/CAM and Post-Production Editing]]
- [[email-storage|Personal Productivity / Email Storage]]
- [[ilm|Information Lifecycle Management (ILM)]]
- [[large-file-distribution|Large File Distribution (MP3 / Video)]]
- [[large-file-storage|Unique Large Files (X-ray / MRI)]]
- [[midline-storage|Midline Storage]]
- [[oltp|Online Transaction Processing]]
- [[oltp-contemporary|Contemporary OLTP]]
- [[web-application|Web Application Storage]]

## Key observations (top 25)

- **2003** — Storage classification framework scope: Eight enterprise application categories mapped to storage access characteristics
- **2003** — Traditional OLTP access pattern: Update intensive — both reads and writes with focus on writes
- **2003** — Contemporary OLTP access pattern: Mix of writes and reads — updating for transactions plus random reads
- **2003** — Business Intelligence access pattern: Query intensive — primarily sequential reads
- **2003** — Web application access pattern: Primarily random reads with a little transaction processing
- **2003** — Personal productivity / email access pattern: Write once; read once to many times
- **2003** — Interactive design access pattern: Mix of reads and writes on large pieces of data
- **2003** — Unique large files access pattern: After creation content is fixed — ideally inalterable; read-only
- **2003** — Large file distribution access pattern: Read-only access of previously-created large bit-mapped files
- **2003** — Midline storage tier market viability: Application I/O analysis supports distinct midline storage tier between FC and desktop ATA
- **2023** — Midline/nearline storage tier adoption: [UNVERIFIED]
- **2003** — ILM storage tier rationale: Different application access patterns justify different storage tiers with distinct cost-performance profiles
- **2003** — BI workload storage mismatch risk: Sequential-read BI queries are over-provisioned on high-performance random-I/O SCSI storage
- **2003** — Email storage growth trajectory: Write-once read-few email pattern creates accumulating storage demand suited to lower-cost nearline
- **2003** — Web application read dominance: Web apps primarily read-biased which reduces need for high-write-performance premium storage

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '15-classification-key-applications-55b6be' ORDER BY year_observed;
```

