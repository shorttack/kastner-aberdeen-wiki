---
title: "RAMP Interview: Kaiser Permanente (Maxtor Midline Storage Study)"
slug: kaiser-permanente-ramp-interview-for-max-8e4033
page_type: study
author: "Peter S. Kastner, David Hill"
date: "2003-04-01"
study_type: market-study
subject_domain: "enterprise-storage / healthcare-IT / midline-disk-evaluation / EHR-migration"
methodology: "ramp-interview, face-to-face, industry-analysis"
importance: high
importance_rationale: "Documents the healthcare IT storage landscape at the exact moment EHR migration was beginning; captures how HIPAA, regional fragmentation, and legacy mainframe dependencies were shaping storage purchasing — a direct antecedent to the Epic-driven healthcare IT transformation of the 2010s."
relevance: high
relevance_rationale: "Healthcare IT storage challenges documented here — EHR system fragmentation, compliance-driven retention, application-driven storage decisions, regional system incompatibility — all intensified over the following 20 years; Kaiser's eventual Epic adoption makes this a foundational baseline document."
prescience: high
prescience_rationale: "The prescience is exceptional: Sietsema correctly identified that applications (not storage strategy) would drive healthcare storage; Kaiser's eventual Epic migration (Epoch was an Epic precursor) took until the 2010s; HIPAA storage requirements exploded exactly as predicted; the 'storage utility' concept failed in healthcare exactly as Sietsema forecast; storage spending became opportunistic and application-triggered precisely as described."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 10
obs_count: 33
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# RAMP Interview: Kaiser Permanente (Maxtor Midline Storage Study)

> Face-to-face RAMP interview with Harvey Sietsema Jr., Applications Programming Manager at Kaiser Foundation Health Plan (Walnut Creek CA), capturing the healthcare IT perspective on storage purchasing for a primarily mainframe-centric organization. Kaiser's Management Data Repository (DB2/mainframe) served 2,200-3,000 users; the organization was mid-migration to the Epoch clinical system; HIPAA compliance was driving massive training; and regional fragmentation (northern vs. southern California operating separately) made enterprise storage planning infeasible. Sietsema's insight — 'applications are the tail that wags the storage dog' — captured how healthcare IT complexity would prevent systematic storage rationalization, making disk storage adoption opportunistic.

**Author:** Peter S. Kastner, David Hill · **Date:** 2003-04-01 · **Type:** market-study
**Importance:** high — *Documents the healthcare IT storage landscape at the exact moment EHR migration was beginning; captures how HIPAA, regional fragmentation, and legacy mainframe dependencies were shaping storage purchasing — a direct antecedent to the Epic-driven healthcare IT transformation of the 2010s.*
**Prescience:** high — *The prescience is exceptional: Sietsema correctly identified that applications (not storage strategy) would drive healthcare storage; Kaiser's eventual Epic migration (Epoch was an Epic precursor) took until the 2010s; HIPAA storage requirements exploded exactly as predicted; the 'storage utility' c…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill-aberdeen|David Hill]]
- [[epic-systems|Epic Systems Corporation]]
- [[epoch-epic|Epoch (Epic precursor / clinical information system)]]
- [[harvey-sietsema-jr|Harvey Sietsema Jr.]]
- [[ibm|IBM]]
- [[kaiser-foundation-health-plan|Kaiser Foundation Health Plan Inc.]]
- [[kaiser-permanente|Kaiser Permanente]]
- [[maxtor|Maxtor Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (10)

- [[ata-disk|ATA Disk (IDE/ATA-100)]]
- [[clinical-data-repository|Clinical Data Repository (CDR)]]
- [[document-scanning|Document / Image Scanning System]]
- [[epoch-ehr|Epoch Clinical Information System (EHR)]]
- [[hierarchical-database|Hierarchical Database]]
- [[hipaa-compliance-systems|HIPAA Compliance and Training Systems]]
- [[ibm-db2|IBM DB2]]
- [[ibm-mainframe|IBM Mainframe (System z / S/390)]]
- [[management-data-repository|Management Data Repository (MDR)]]
- [[sas-analytics|SAS (Statistical Analysis System)]]

## Key observations (top 25)

- **2003** — revenue: $22B
- **2003** — employee-count: 100000
- **2003** — primary-platform: IBM mainframe
- **2003** — mdr-description: Homegrown system; HR, patient, cost data; predates claims adjustment and outpatient
- **2003** — sas-users: 2200-3000 California users
- **2003** — mdr-geographic-coverage: Northern California only
- **2003** — physician-notes-method-north: scanned into system
- **2003** — physician-notes-method-south: hand-entered; higher error rate
- **2003** — ehr-migration-initiative: Automated Medical Record Initiative with Epoch
- **2003** — hipaa-impact: massive training for all contractors
- **2003** — roi-requirements-trend: much stricter; more comprehensive; business has more control
- **2003** — applications-drive-storage-thesis: Applications are the tail that wags the storage dog
- **2003** — storage-utility-concept-feasibility: Kaiser will not be able to move to an information utility because IT environment will be chaotic
- **2003** — midline-storage-adoption-model: opportunistic based upon application
- **2003** — it-governance-model: regional; each region has own IT organization
- **2003** — organizational-culture: collection of separate healthcare companies under Kaiser name
- **2003** — system-migration-challenge: Migration at more than one site is not just replacement of one system; requires replicating function across regions
- **2003** — healthcare-system-scope: Billing, patient records, clinical records — all must interface
- **2003** — roc-business-rules-initiative: Kaiser wants improved business rules in Regions Outside California
- **2003** — cio-reporting-structure: CIO reports to CIO who is also Chief Administrative Officer
- **2003** — cims-costing-system: huge costing database on mainframe hierarchical DB; some non-mainframe feeds
- **2003** — ata-midline-adoption-kaiser: not viable; IT too chaotic for strategic storage planning
- **2003** — hipaa-storage-growth-driver: HIPAA will drive increasing storage requirements and retention complexity
- **2003** — ehr-migration-timeline-estimate: Clinical Data Repository migration in 2-3 years
- **2015** — kaiser-epic-deployment-timeline: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'kaiser-permanente-ramp-interview-for-max-8e4033' ORDER BY year_observed;
```

