---
title: "Automating and Managing Internal Operations"
slug: 1997-automating-and-managing-internal-op-e69e64
page_type: study
author: "Aberdeen Group"
date: "1997-02-01"
study_type: white-paper
subject_domain: "IT-operations-management"
methodology: "field-research, industry-analysis, competitive-profiling"
importance: medium
importance_rationale: "Defined the 'Consolidated Operations Management' category and positioned help desk software as enterprise automation backbone; influential in framing ITSM market during Aberdeen's peak influence period."
relevance: medium
relevance_rationale: "The COM framework and its six success factors (adaptability, data access, UI, business rules, rapid modification, openness) remain conceptually applicable to modern ITSM and enterprise automation platforms, though specific product details are historical."
prescience: high
prescience_rationale: "Aberdeen's prediction that AR System would become a popular COM vehicle proved correct—Remedy grew to 7,000+ customers before acquisition by Peregrine/BMC; the ITSM platform consolidation trend Aberdeen described accurately forecast ServiceNow-era convergence."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 5
obs_count: 21
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Automating and Managing Internal Operations

> Aberdeen Group examines the trend toward 'Consolidated Operations Management' (COM) as enterprises automate internal processes—IT help desk, asset management, SLA tracking, procurement, and HR—using a common adaptable platform. The paper identifies six success factors for COM adoption and profiles Remedy Corporation's Action Request System (AR System) as the leading vehicle for this transition, citing its extensibility, 3,000-plus customer base, and use beyond traditional help desk functions.

**Author:** Aberdeen Group · **Date:** 1997-02-01 · **Type:** white-paper
**Importance:** medium — *Defined the 'Consolidated Operations Management' category and positioned help desk software as enterprise automation backbone; influential in framing ITSM market during Aberdeen's peak influence period.*
**Prescience:** high — *Aberdeen's prediction that AR System would become a popular COM vehicle proved correct—Remedy grew to 7,000+ customers before acquisition by Peregrine/BMC; the ITSM platform consolidation trend Aberdeen described accurately forecast ServiceNow-era convergence.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[oracle|Oracle Corporation]]
- [[remedy-corporation|Remedy Corporation]]
- [[sap|SAP AG]]

## Technologies (5)

- [[ar-system|Remedy Action Request System (AR System)]]
- [[ar-system-v3|AR System Version 3.0]]
- [[consolidated-operations-mgmt|Consolidated Operations Management (COM)]]
- [[help-desk-software|Internal IT Help Desk Software]]
- [[workflow-automation|Workflow Automation / Business Rules Engine]]

## Key observations (top 25)

- **1997** — Remedy customer count: 3,000+ customers by early 1997
- **1996** — AR System repeat customer sales rate: 53% of sales to existing customers (first 3 quarters 1996)
- **1997** — AR System core competency: Highly adaptable; call logging, tracking, escalation, notification, problem resolution, reporting
- **1997** — COM Success Factor 1: Highly and easily adaptable application
- **1997** — COM Success Factor 2: Wide data source and format access (multi-platform, multi-database)
- **1997** — COM Success Factor 3: Intuitive universal user interface
- **1997** — COM Success Factor 4: Ability to embed business rules and procedures
- **1997** — COM Success Factor 5: Rapid and continuous modification capability
- **1997** — COM Success Factor 6: Open system with exposed APIs for enterprise integration
- **1997** — Primary driver of AR System adoption beyond help desk: Ease of customization and high adaptability cited by all customers interviewed
- **1997** — AR System v3.0 improvement - UI: New screen widgets, view management, HTML User's Guide
- **1997** — AR System v3.0 improvement - Data access: Multi-table joins without SQL; Direct SQL for cross-enterprise database links
- **1997** — IT help desk as COM launchpad strategy: Help desk identified as natural starting point for internal operations automation
- **1997** — Internal operations targeted for COM automation: 9 categories: IT support, facilities, SLA tracking, asset management, inventory, procurement, defect tracking, personnel resource management, policy notification
- **1997** — AR System COM market leadership prediction: Remedy expected to become leading supplier of Consolidated Operations Management applications
- **2002** — AR System COM market leadership actual outcome: Remedy grew to 7,000+ customers; acquired by Peregrine for $1B (2001), then sold to BMC Software for $355M (2002); ITSM market converged as predicted but under ServiceNow leadership by 2010s
- **1997** — AR System deployment verticals: Automotive, computers, chemicals/pharma, energy/utilities, financial services, government, telecom, education
- **1997** — AR System extended use cases cited by customers: Inventory management, purchase order management, stock reordering, password/network address tracking, asset tracking, change management
- **1997** — Embedded workflow business rules capability: AR System v3.0 added pre-defined keywords to simplify embedding workflow processes and business rules
- **1997** — COM market growth prediction: Consolidated operations management will rapidly move up planning agenda of senior executives
- **2005** — COM market growth actual outcome: ITSM market grew substantially; Gartner ITSM predictions for $9.4B by 2000 were directionally correct; ServiceNow founded 2004 on same COM premise; market reached $14B+ by 2015

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-automating-and-managing-internal-op-e69e64' ORDER BY year_observed;
```

