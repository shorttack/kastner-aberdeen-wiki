---
title: "Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993)"
slug: aberdeen-dops-distributed-open-prod-syst-cbae77
page_type: study
author: "Peter S. Kastner — Vice-President, Aberdeen Group, Inc."
date: "1993-06-01"
study_type: conference-presentation
subject_domain: "distributed-systems-architecture"
methodology: "Aberdeen-Group-presentation-deck"
importance: high
importance_rationale: "Foundational Aberdeen DOPS framework — the core thesis Aberdeen would build the early-90s consulting practice around. Multi-vendor distributed-transaction diagram is the canonical 1993 visualization of what production distributed systems could become. Direct continuation of Spoke-Node-Ring (Study 6) into specific multi-vendor architecture."
relevance: high
relevance_rationale: "Documents Kastner/Aberdeen's role positioning DCE/Encina as the production-distributed-system enabler. The Stratus-IBM-RS6000-HP-Pyramid diagram is precisely the heterogeneous multi-vendor world Aberdeen advised Fortune 1000 IT leaders on. Reinforces Aberdeen's neutral-broker positioning across all major Unix and proprietary platforms."
prescience: high
prescience_rationale: "DCE-on-Encina vision didn't fully materialize commercially, but the concept of distributed transaction coordination across heterogeneous data stores directly anticipated modern distributed-saga patterns, X/Open XA, and ultimately microservices' transactional complexity. SQL Access Group's interoperability anticipated ODBC and JDBC. The 'hide the complexities of comm network, data location, how/where things get done' definition of Intelligent Applications is prescient of serverless and Kubernetes…"
license: CC-BY-4.0
tier: 1
entity_count: 13
tech_count: 10
obs_count: 12
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993)

> Aberdeen Group conference presentation deck delivered by Peter S. Kastner (Vice-President, Aberdeen Group) circa 1993 titled 'Distributed Open Production Systems: The Next Generation Begins.' Boston office at 92 State Street, (617) 723-7890. Defines Downsizing as migrating computer-based functions from central mainframe to dispersed computing systems and operationally as moving MIS function down the organization. Presents the Spoke-Node-Ring Planning Model based on three buyer demands: Distributed Systems, Open Systems, Production-Quality Applications. Centerpiece is a complex multi-vendor distributed-application diagram showing: a Stratus Encina/DCE/Sybase/VOS Order Processing node coordinating with IBM S/390 CICS/DCE/DB2/DRDA/MVS/ESA Credit Admin; RS/6000 Encina/DCE/Informix Warehouse Distribution; HP 9000 Encina/DCE/Allbase/HP-UX Resource Planning (MRP); Pyramid Ui-AHas Ingres/Unix 5.4 MP Order Processing — all linked via Encina/DCE distributed transactions. Defines Intelligent Applications as those that 'use more system services and hide the complexities' (comm network, data location, how/where things get done). Six Technology Combinations: standalone Unix; single-source database; production distributed databases; communications to open & proprietary; mainframes treating world as peers; distributed data integrity. Future enablers: SQL Access Group's database interoperability, OSF's Distributed Computing Environment (DCE), IBM's endorsement of DCE, new products for distrib…

**Author:** Peter S. Kastner — Vice-President, Aberdeen Group, Inc. · **Date:** 1993-06-01 · **Type:** conference-presentation
**Importance:** high — *Foundational Aberdeen DOPS framework — the core thesis Aberdeen would build the early-90s consulting practice around. Multi-vendor distributed-transaction diagram is the canonical 1993 visualization of what production distributed systems could become. Direct continuation of Spoke-Node-Ring (Study 6)…*
**Prescience:** high — *DCE-on-Encina vision didn't fully materialize commercially, but the concept of distributed transaction coordination across heterogeneous data stores directly anticipated modern distributed-saga patterns, X/Open XA, and ultimately microservices' transactional complexity. SQL Access Group's interopera…*

## Entities (13)

- [[aberdeen-group|Aberdeen Group]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM Corporation]]
- [[ibm-rs6000|IBM RS/6000]]
- [[informix-software|Informix Software]]
- [[ingres-corporation|Ingres Corporation]]
- [[osf-open-software-foundation|Open Software Foundation (OSF)]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[pyramid-technology|Pyramid Technology]]
- [[sql-access-group|SQL Access Group (SAG)]]
- [[stratus-computer|Stratus Computer]]
- [[sybase-inc|Sybase Inc.]]
- [[transarc-corporation|Transarc Corporation]]

## Technologies (10)

- [[dops-distributed-open-prod|Distributed Open Production Systems (DOPS)]]
- [[downsizing-it-strategy|IT Downsizing]]
- [[encina-tp-monitor|Transarc Encina TP Monitor]]
- [[hp-allbase|HP Allbase/SQL]]
- [[ibm-cics|IBM CICS]]
- [[ibm-drda|IBM DRDA (Distributed Relational Database Architecture)]]
- [[intelligent-applications|Intelligent Applications]]
- [[osf-dce|OSF Distributed Computing Environment (DCE)]]
- [[spoke-node-ring|Spoke-Node-Ring (S-N-R) Planning Model]]
- [[two-phase-commit|Two-Phase Commit (2PC)]]

## Key observations (top 25)

- **1993** — definition: Distributed-Open-Production-Quality-systems
- **1993** — platforms_in_diagram: Stratus-IBM-S390-RS6000-HP9000-Pyramid
- **1993** — characteristics: use-more-system-services-hide-complexities
- **1993** — tech_combination_count: 6
- **1993** — key_enabler: IBM-endorsement-of-DCE
- **1993** — promise: database-interoperability-standard
- **1993** — diagram_role: Stratus-Encina-DCE-Sybase-VOS-Order-Processing
- **1993** — diagram_role: S-390-CICS-DCE-DB2-DRDA-MVS-ESA-Credit-Admin
- **1993** — diagram_role: HP-9000-Encina-DCE-Allbase-HP-UX-MRP
- **1993** — title: Vice-President-Aberdeen-Group
- **1993** — framework_iteration: 1993-Next-Generation-Begins
- **1993** — diagram_role: RS6000-Encina-DCE-Informix-Warehouse-Distribution

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-dops-distributed-open-prod-syst-cbae77' ORDER BY year_observed;
```

