---
title: "Classification of Key Applications by Storage Category"
slug: "study-15-classification-key-applications-55b6be"
page_type: "study"
tags: ["type/study", "collection/case-analysis"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "15-classification-key-applications-55b6be"
author: "Aberdeen Group (David Hill)"
date: "2003-01-01"
pub_year: 2003
type: "case-analysis"
subject_domain: "enterprise-storage"
methodology: "industry-analysis"
source_file: "15-Classification-Key-Applications.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 2.1
prescience_obs_count: 10
---

# Classification of Key Applications by Storage Category

> A concise classification matrix mapping eight major enterprise application types to their data access characteristics (read/write patterns and data structures). The framework distinguishes Traditional OLTP, Contemporary OLTP, Business Intelligence, Web Applications, Personal Productivity, Interactive Design, Unique Large Files, and Large File Distribution. This taxonomy serves as the foundational analytical framework supporting Maxtor's midline storage category creation project.


_Published 2003, author **Aberdeen Group (David Hill)**, type **case-analysis**._


## Top observations

- Different application access patterns justify different storage tiers with distinct cost-performance profiles `[ps=5]`
- After creation content is fixed — ideally inalterable; read-only `[ps=4]`
- Application I/O analysis supports distinct midline storage tier between FC and desktop ATA `[ps=4]`
- Eight enterprise application categories mapped to storage access characteristics `[ps=3]`
- Update intensive — both reads and writes with focus on writes `[ps=3]`
- Web apps primarily read-biased which reduces need for high-write-performance premium storage `[ps=2]`
- Mix of writes and reads — updating for transactions plus random reads `[ps=0]`
- Query intensive — primarily sequential reads `[ps=0]`
- Primarily random reads with a little transaction processing `[ps=0]`
- Mix of reads and writes on large pieces of data `[ps=0]`
- Write once; read once to many times
- Read-only access of previously-created large bit-mapped files
- [UNVERIFIED]
- Sequential-read BI queries are over-provisioned on high-performance random-I/O SCSI storage
- Write-once read-few email pattern creates accumulating storage demand suited to lower-cost nearline
