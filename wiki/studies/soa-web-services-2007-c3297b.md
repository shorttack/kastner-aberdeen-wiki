---
title: "SOA and Web Services Testing: How Different Can It Be?"
slug: soa-web-services-2007-c3297b
page_type: study
author: "Aberdeen Group"
date: "2007-08"
study_type: employer-record
subject_domain: "SOA testing; web services QA; software quality assurance"
methodology: "survey; benchmark; n=240 end-users; qualitative interviews"
importance: high
importance_rationale: "Captures 2007 state of SOA/web services testing practices with concrete survey data; documents transition from monolithic to composite application testing methodology"
relevance: high
relevance_rationale: "Directly addresses SOA QA maturity gap with quantitative benchmarks across three company tiers; useful for understanding adoption patterns"
prescience: high
prescience_rationale: "Correctly anticipated that business user involvement in QA and automated orchestration testing would become standard practice; shift toward continuous QA now universal in DevOps"
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 6
obs_count: 26
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# SOA and Web Services Testing: How Different Can It Be?

> 26-page Aberdeen Group benchmark report examining testing and quality assurance challenges for SOA and web services deployments. Unit and functional testing insufficient; integration, regression, business process, performance, and security testing all required. Survey of 240 end-users categorizes companies into Best-in-Class (top 20%), Industry Average (middle 50%), and Laggard (bottom 30%) using Aberdeen Competitive Framework and PACE model. Best-in-Class companies redesigned QA processes, use automated testing, involve business users throughout lifecycle, and track quality across entire project—not just at end.

**Author:** Aberdeen Group · **Date:** 2007-08 · **Type:** employer-record
**Importance:** high — *Captures 2007 state of SOA/web services testing practices with concrete survey data; documents transition from monolithic to composite application testing methodology*
**Prescience:** high — *Correctly anticipated that business user involvement in QA and automated orchestration testing would become standard practice; shift toward continuous QA now universal in DevOps*

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[isoft-group|iSOFT Group]]

## Technologies (6)

- [[automated-testing-tools|Automated Testing Tools (SOA)]]
- [[design-time-governance|Design-Time Governance]]
- [[production-monitoring|Production Monitoring and Reporting Tools]]
- [[requirements-tracking|Requirements Tracking Software]]
- [[soa-testing|SOA/Web Services Testing]]
- [[web-services-soa|Service Oriented Architecture / Web Services]]

## Key observations (top 25)

- **2007** — survey_sample_size: N=240 end-users
- **2007** — bic_quality_increase: 94% of Best-in-Class reported increase in software quality
- **2007** — bic_defect_reduction: 61% of Best-in-Class saw reduction in production defects
- **2007** — bic_repair_time_reduction: 57% of Best-in-Class reported decrease in mean time to repair defects
- **2007** — bic_code_test_coverage: 71% of Best-in-Class saw increase in code test coverage
- **2007** — bic_maintainability_improvement: 70% of Best-in-Class said maintainability improved
- **2007** — bic_automated_testing_adoption: 57% of Best-in-Class vs 35% of others use automated testing tools
- **2007** — quality_lifecycle_management: 81% of Best-in-Class manage quality throughout lifecycle vs 63% of others
- **2007** — business_user_involvement: 26% Best-in-Class vs 19% others involve business users in quality
- **2007** — top_driver_time_to_deliver: 55-56% of all companies cite reducing time to deliver as top QA driver
- **2007** — defect_reduction_driver: 60% Best-in-Class vs 52% others cite reducing defects as QA driver
- **2007** — risk_reduction_driver: 28% BIC vs 43% others cite risk reduction as QA driver
- **2007** — qa_redesign_rate: 20% Best-in-Class redesigned QA completely vs 7% others
- **2007** — testing_soa_differently: 62% Best-in-Class vs 54% others test SOA/web services differently from traditional software
- **2007** — requirements_tracking_adoption: 45% of Best-in-Class use requirements tracking tools vs 35% of Avg/Laggard
- **2007** — requirements_management_bic: 81% of BIC manage requirements throughout software lifecycle vs 72% Avg, 54% Laggard
- **2007** — automation_requirements_tracking: 38% BIC vs 28% Avg vs 21% Laggard use automation for requirements tracking
- **2007** — design_governance_adoption: 48% BIC use design-time governance to foster reusability vs 33% others
- **2007** — regression_testing_laggard: Only 39% of Laggard organizations conduct regression testing
- **2007** — qa_budget_ratio: Companies with formal QA often budget 2-3x development time for QA testing
- **2007** — isoft_qa_transformation: iSOFT rebuilt LORENZO product from scratch on SOA when older platform reached extendibility limits
- **2007** — requirements_based_testing_bic: Best-in-Class are twice as likely to use automated requirements-tracking tools vs Laggard
- **2007** — quality_measurement_bic: 70% of Best-in-Class measure quality throughout project lifecycle not just in testing
- **2007** — governance_reuse_bic: 47% of Best-in-Class use design-time governance to promote reuse vs 33% average
- **2007** — required_action_1: Expand quality focus: take end-to-end perspective and test interoperability across entire business process

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'soa-web-services-2007-c3297b' ORDER BY year_observed;
```

