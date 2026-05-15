---
title: "Middleware Technology: 1998 Practice Summary"
slug: middle~1-a64fa0
page_type: study
author: "Aberdeen Group"
date: "1998-05-01"
study_type: other-research
subject_domain: "middleware"
methodology: "industry-analysis, market-overview"
importance: medium
importance_rationale: "Captures the middleware landscape at a pivotal moment when the market was transitioning from point products to integrated EAI solutions and Internet-centric architectures; profiles vendors who would become major players (BEA acquired by Oracle; TIBCO IPO)."
relevance: high
relevance_rationale: "Middleware categories like messaging, application servers, and EAI are foundational to modern enterprise architecture; the CORBA vs. DCOM debate resolved in favor of neither (REST/HTTP won), but the underlying integration challenges remain highly relevant."
prescience: high
prescience_rationale: "Aberdeen correctly predicted market consolidation, the rise of EAI as a strategic priority, the importance of integrated middleware over point products, and BEA/TIBCO viability — most of these proved accurate over the following five years."
license: CC-BY-4.0
tier: 1
entity_count: 17
tech_count: 14
obs_count: 23
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Middleware Technology: 1998 Practice Summary

> Aberdeen Group's 1998 practice summary covering the middleware technology market, analyzing gateways, TP monitors, RPCs, messaging, ORBs, data access tools, EAI solutions, and application servers as distinct middleware categories. The report sizes the middleware market at approximately $6 billion by 2000, identifies the CORBA vs. DCOM standards battle as a critical industry question, and provides supplier abstracts for thirteen vendors including BEA Systems, IBM, Microsoft, TIBCO, and CrossWorlds. Key findings include that no vendor had yet delivered a fully integrated middleware solution and that market consolidation was underway.

**Author:** Aberdeen Group · **Date:** 1998-05-01 · **Type:** other-research
**Importance:** medium — *Captures the middleware landscape at a pivotal moment when the market was transitioning from point products to integrated EAI solutions and Internet-centric architectures; profiles vendors who would become major players (BEA acquired by Oracle; TIBCO IPO).*
**Prescience:** high — *Aberdeen correctly predicted market consolidation, the rise of EAI as a strategic priority, the importance of integrated middleware over point products, and BEA/TIBCO viability — most of these proved accurate over the following five years.*

## Entities (17)

- [[aberdeen-group|Aberdeen Group]]
- [[active-software|Active Software]]
- [[bea-systems|BEA Systems Inc.]]
- [[borland-international|Borland International Inc. (soon to be Inprise)]]
- [[crossworlds-software|CrossWorlds Software]]
- [[expersoft|EXPERSOFT Corporation]]
- [[ibm|IBM Corporation]]
- [[insession|Insession Inc.]]
- [[iona-technologies|IONA Technologies]]
- [[microsoft|Microsoft Corporation]]
- [[neon-networks|New Era of Networks Inc. (NEON)]]
- [[oracle|Oracle Corporation]]
- [[reliant-data-systems|RELIANT Data Systems]]
- [[smartdb|SmartDB Corporation]]
- [[sybase|Sybase Inc.]]
- [[tibco-software|TIBCO Software Inc.]]
- [[visigenic|Visigenic Software]]

## Technologies (14)

- [[cgi|CGI (Common Gateway Interface)]]
- [[component-broker|IBM Component Broker (CB)]]
- [[corba|CORBA (Common Object Request Broker Architecture)]]
- [[dcom|DCOM (Distributed Component Object Model)]]
- [[iis-asp|IIS/Active Server Pages (ASP)]]
- [[microsoft-transaction-server|Microsoft Transaction Server (MTS)]]
- [[mq-series|IBM MQSeries]]
- [[msmq|Microsoft Message Queue (MSMQ)]]
- [[rpc|Remote Procedure Calls (RPC)]]
- [[sap-r3|SAP R/3]]
- [[tib-active-enterprise|TIB/ActiveEnterprise]]
- [[tp-monitors|Transaction Processing (TP) Monitors]]
- [[tuxedo|TUXEDO TP Monitor]]
- [[visiBroker|VisiBroker ORB]]

## Key observations (top 25)

- **1997** — middleware_market_share_of_app_integration: About 50% of $1.3B application and data integration market
- **1997** — app_data_integration_market_size: $1.3 billion
- **2001** — app_data_integration_market_forecast: $8 billion by 2001
- **2000** — middleware_market_forecast: ~$6 billion by year 2000
- **1997** — middleware_market_consolidation: Consolidation underway: BEA/Digital; Visigenic/Borland acquisitions in 1997
- **1998** — integrated_middleware_availability: No single supplier has developed a completely integrated middleware solution
- **1998** — middleware_buying_decision_level: Mid-level IS managers typically make middleware buying decision
- **1998** — tp_monitor_concurrent_user_scale: Hundreds to thousands of concurrent users
- **1998** — rpc_market_trajectory: Small and diminishing category; functionality built into OS
- **1998** — orb_interoperability_status: Major ORBs do not communicate with each other; CORBA and DCOM cannot interoperate
- **1999** — eai_sap_integration_criticality: EAI middleware will be crucial to effective use of SAP R/3 within 1-1.5 years
- **2000** — integrated_middleware_requirement: Middleware suppliers must offer complete integrated solution or alliances for long-term viability
- **1998** — cgi_performance_bottleneck: CGI web middleware slowing server performance and complicating development
- **1998** — mqseries_admin_tool_gap: MQSeries implementations lack adequate administrative and development tools
- **1998** — ibm_middleware_position: Relatively strong position via MQSeries popularity and NCF introduction
- **1998** — microsoft_middleware_position: Strong position for enterprise entry; needs proof of implementation for IS buyers
- **1998** — bea_market_position: Market dominant position in TUXEDO TP monitor; aggressive acquisition strategy
- **1998** — tibco_positioning: Pioneered publish-subscribe technology; Wall Street de facto standard; expanding to EAI
- **1998** — crossworlds_market_position: Led EAI market awareness; largest war chest; SAP-to-PeopleSoft integration opportunity
- **1998** — aberdeen_buyer_recommendation: Demand integrated architecture roadmap; prototype within 6 months; enterprise-wide rollout in year 2
- **1998** — eai_project_types: Application integration increasingly involves mission-critical business processes + data warehousing + Y2K conversions
- **1998** — enterprise_app_services_concept: Aberdeen defines higher-level middleware as Enterprise Application Services (EAS)
- **1998** — neon_financial_vertical_challenge: NEON must expand beyond financial vertical where custom apps dominate

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'middle~1-a64fa0' ORDER BY year_observed;
```

