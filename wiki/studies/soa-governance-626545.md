---
title: "Management and Governance: Planning for an Optimized SOA Application Lifecycle"
slug: soa-governance-626545
page_type: study
author: "Aberdeen Group"
date: "2007-03"
study_type: employer-record
subject_domain: "SOA governance; SOA operations management; application lifecycle management"
methodology: "survey; benchmark; n=200+ companies; qualitative interviews; Nov 2006–Jan 2007"
importance: high
importance_rationale: "Provides quantitative benchmarks for SOA governance adoption; introduces three-way SOA strategy taxonomy (SOA Lite/Enterprise/ERP SOA) that became influential framing"
relevance: high
relevance_rationale: "Rich survey data on operational challenges, governance drivers by industry, lifecycle cost impact; spans 200+ company survey with financial and industry segmentation"
prescience: high
prescience_rationale: "Correctly predicted decades-long importance of SOA governance; design-time governance and service reuse principles now foundational to microservices/API management"
license: CC-BY-4.0
tier: 1
entity_count: 1
tech_count: 5
obs_count: 26
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Management and Governance: Planning for an Optimized SOA Application Lifecycle

> 24-page Aberdeen Group benchmark report examining effectiveness of IT investments in three SOA lifecycle areas: operations management, design/operations governance, and project/development/ALM tools. Survey of 200+ companies across geographies and industries. Between one-third and half of 950 companies surveyed in 2006 had serious deployment difficulties. Best-in-Class (top 20%) distinguish themselves through experience (33% with >2 years SOA), positive ROI (68%), design-time governance implementation, and automated management/governance solutions (>80%). Three SOA strategies identified: SOA Lite (50%), Enterprise SOA (30%), ERP SOA (20%).

**Author:** Aberdeen Group · **Date:** 2007-03 · **Type:** employer-record
**Importance:** high — *Provides quantitative benchmarks for SOA governance adoption; introduces three-way SOA strategy taxonomy (SOA Lite/Enterprise/ERP SOA) that became influential framing*
**Prescience:** high — *Correctly predicted decades-long importance of SOA governance; design-time governance and service reuse principles now foundational to microservices/API management*

## Entities (1)

- [[aberdeen-group|Aberdeen Group]]

## Technologies (5)

- [[alm-tools|Application Lifecycle Management Tools]]
- [[bpm-tools|Business Process Management (BPM) Tools]]
- [[soa-governance-tools|SOA Governance Software]]
- [[soa-middleware-esb|SOA Infrastructure Middleware / ESB]]
- [[soa-operations-management|SOA Operations Management]]

## Key observations (top 25)

- **2007** — soa_deployment_difficulties: Between 1/3 and 1/2 of 950 companies surveyed in 2006 had serious difficulties deploying SOA applications into stable production
- **2007** — bic_experience_two_years: 33% of Best-in-Class have more than 2 years experience with SOA technology
- **2007** — bic_positive_roi: 68% of Best-in-Class achieving positive ROI on SOA investments vs 23% overall (77% have yet to see payback)
- **2007** — bic_automated_governance: More than 80% of Best-in-Class have implemented automated solution for SOA operations and governance, typically third-party software
- **2007** — global_10000_soa_adoption: 90% of Global 10,000 organizations have embarked on SOA journeys
- **2007** — soa_strategy_distribution: SOA Lite: ~50% of companies; Enterprise SOA: ~30%; ERP SOA: ~20%
- **2007** — top_stumbling_block: 44% cite establishment of operational security, governance, and management as top SOA stumbling block
- **2007** — security_stumbling_block: 39% cite security issues as different from older IT as stumbling block
- **2007** — sla_scaling_stumbling_block: 38% cite SLAs/scaling to production volumes/reliability and availability as stumbling block
- **2007** — debugging_complexity_stumbling_block: 35% cite debugging problems with complex services and composites as stumbling block
- **2007** — data_management_stumbling_block: 34% cite data management of SOA services as problematic
- **2007** — design_time_governance_rate: About 25% of Global 10,000 organizations employing design-time governance
- **2007** — top_driver_new_capabilities: 45% of survey and 46% of supply chain organizations cite developing new business capabilities as top SOA governance driver
- **2007** — it_complexity_driver: 42% overall cite management of IT complexity as second driver; 44% of BIC (higher than average due to more experience)
- **2007** — bic_experience_12months: More than 50% of Best-in-Class have at least 12 months production experience with deployed SOA apps vs 30% of overall survey
- **2007** — bic_more_24months: 33% of Best-in-Class have more than 24 months SOA experience vs 12% of overall
- **2007** — bic_unhappy_dev_tools: 75% of Best-in-Class unhappy with application development tools and plan to supplement/replace within 6 months
- **2007** — bic_web_services_driver: Re-usage of applications via Web Services: BIC 47%, Average 43%, Laggard 36%
- **2007** — speed_it_driver: Speed of IT implementations: Laggard 43%, Average 30%, BIC 32%
- **2007** — code_reuse_cost_reduction: 50% code reuse under SOA governance cuts lines of maintained code in half permanently
- **2007** — it_budget_integration: 40% of IT budget dedicated to application integration; SOA positioned as solution
- **2007** — governance_banking_driver: Banking/brokerage/insurance most focused on compliance governance; manufacturing on operational complexity
- **2007** — recommendation_experience: Organizations dawdling with web services and no firm SOA plan are falling behind peers
- **2007** — recommendation_design_in: Design in SOA management and governance; manageability, reuse policies, security most economically designed in not bolted on
- **2007** — recommendation_lifecycle_costs: Without design-time governance, programmers will not reuse services and lifecycle costs will balloon

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'soa-governance-626545' ORDER BY year_observed;
```

