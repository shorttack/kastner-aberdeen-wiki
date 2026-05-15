---
title: "Dun & Bradstreet Software SmartStream Distributed Enterprise: Putting It All Together To Better Spread It All Apart"
slug: aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better
page_type: study
author: "Aberdeen Group"
date: "1996-04-01"
study_type: product-profile
subject_domain: "enterprise resource planning / client-server applications"
methodology: "vendor analysis"
importance: high
importance_rationale: "This study documents D&B Software at a pivotal moment — generating $100M+ in SmartStream revenues with plans for divestiture by Dun & Bradstreet Corporation. The company was subsequently acquired by Geac Computer, which then abandoned the SmartStream manufacturing module. The fate represents a cautionary tale about single-RDBMS dependency limiting addressable market."
relevance: high
relevance_rationale: "Directly relevant to enterprise ERP market history, distributed application architecture evolution, and the consolidation dynamics that reduced dozens of ERP vendors to a handful (SAP, Oracle). The workflow-centric architecture anticipates modern BPM platforms."
prescience: medium
prescience_rationale: "Aberdeen's identification of the single-RDBMS limitation as a persistent competitive disadvantage proved prescient — D&B Software struggled to expand and was acquired by Geac, which abandoned SmartStream manufacturing in 1997. The prediction that SmartStream DE would gain leadership in distributed ERP was not fulfilled."
license: CC-BY-4.0
tier: 1
entity_count: 13
tech_count: 11
obs_count: 30
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Dun & Bradstreet Software SmartStream Distributed Enterprise: Putting It All Together To Better Spread It All Apart

> Aberdeen Group product profile of Dun & Bradstreet Software's SmartStream Distributed Enterprise (SmartStream DE) ERP suite. Examines the product's distributed client/server architecture, workflow capabilities, SQL Server/Sybase dependency, market positioning against Oracle Applications, PeopleSoft, SAP, and SSA, and D&B Software's strategic position as its parent Dun & Bradstreet Corporation prepares for divestiture. SmartStream DE revenues exceeded $100M in fiscal year 1995.

**Author:** Aberdeen Group · **Date:** 1996-04-01 · **Type:** product-profile
**Importance:** high — *This study documents D&B Software at a pivotal moment — generating $100M+ in SmartStream revenues with plans for divestiture by Dun & Bradstreet Corporation. The company was subsequently acquired by Geac Computer, which then abandoned the SmartStream manufacturing module. The fate represents a cauti…*
**Prescience:** medium — *Aberdeen's identification of the single-RDBMS limitation as a persistent competitive disadvantage proved prescient — D&B Software struggled to expand and was acquired by Geac, which abandoned SmartStream manufacturing in 1997. The prediction that SmartStream DE would gain leadership in distributed E…*

## Entities (13)

- [[ABERDEEN-GROUP|Aberdeen Group]]
- [[DB-SOFTWARE|Dun & Bradstreet Software (D&B Software)]]
- [[DOUG-MACINTYRE|Doug MacIntyre (CEO)]]
- [[DUN-BRADSTREET-CORP|The Dun & Bradstreet Corporation]]
- [[GEAC|Geac Computer Corporation]]
- [[MCCORMACK-DODGE|McCormack & Dodge]]
- [[MICROSOFT-SQL|Microsoft Corporation (SQL Server)]]
- [[MSA|Management Science America (MSA)]]
- [[ORACLE-APPS|Oracle Applications]]
- [[PEOPLESOFT|PeopleSoft Inc.]]
- [[SAP|SAP SE]]
- [[SSA|Systems Software Associates (SSA)]]
- [[SYBASE|Sybase Inc.]]

## Technologies (11)

- [[COGNOS-POWERPLAY|Cognos PowerPlay 4.1]]
- [[DISTRIBUTED-CSS|Distributed Client/Server Architecture]]
- [[ERP-CSS|Enterprise Resource Planning (ERP) / CSS]]
- [[MILLENNIUM-SERIES|D&B Software Millennium (M) Series]]
- [[MS-ACCESS|Microsoft Access 2.0]]
- [[MS-SQL-65|Microsoft SQL Server 6.5]]
- [[POWERBUILDER|PowerSoft PowerBuilder]]
- [[SMARTSTREAM-DE|SmartStream Distributed Enterprise v4.0]]
- [[SYBASE-REPSERVER|Sybase Replication Server]]
- [[SYBASE-SQL11|Sybase System 11.1]]
- [[WORKFLOW-TECH|Workflow Technology]]

## Key observations (top 25)

- **1996** — smartstream_revenue_fy95: 100m_plus
- **1996** — smartstream_customer_growth: 40_pct_new_customers_or_150_pct_over_1994
- **1996** — total_installed_base: 10000_plus_customer_sites
- **1996** — total_revenue_fy_nov95: 350m_plus_30pct_international
- **1996** — mainframe_maintenance_renewal: 80_pct_per_year
- **1996** — smartstream_first_deployment: 1992
- **1996** — architecture_type: cooperative_client_server_server_centric
- **1996** — replication_use: enterprise_security_and_business_tables
- **1996** — workflow_leadership: three_form_workflow_first_to_field
- **1996** — sap_workflow_status: still_developing_in_1996
- **1996** — oracle_workflow_status: still_developing_in_1996
- **1996** — rdbms_dependency: sybase_sql_server_only
- **1996** — rdbms_limitation_risk: single_rdbms_persistent_competitive_disadvantage
- **1996** — legacy_integration_gap: no_deliverable_solution_for_host_integration
- **1996** — parent_divestiture_plan: dun_bradstreet_corp_preparing_spinoff
- **1998** — acquisition_outcome: acquired_by_geac
- **1997** — smartstream_manufacturing_abandoned: geac_abandoned_smartstream_manufacturing
- **1996** — market_position_prediction: top_tier_css_application_supplier
- **1996** — leadership_position_prediction: will_take_leadership_in_distributed_erp
- **2004** — erp_leadership_outcome: not_fulfilled_acquired_and_product_abandoned
- **1996** — development_platform: powerbuilder_cpp_sybase_sql_stored_procs
- **1996** — version_at_study: smartstream_de_v4_0
- **1996** — distributed_architecture: data_and_processing_across_multiple_servers
- **1996** — isv_market_position: largest_sybase_sql_server_isv
- **1996** — marketing_strategy_1: mainframe_commitment_and_enhancement

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-app-dun-bradstreet-software-smartstrtogether-better' ORDER BY year_observed;
```

