---
title: "QACenter: Automated Software Quality From Start to Finish"
slug: qacenter-automated-software-quality-from-start-to--b7003b
page_type: study
author: "Aberdeen Group"
date: "1997-01-01"
study_type: market-study
subject_domain: "automated-software-testing"
methodology: "industry-analysis, competitive-profiling"
importance: high
importance_rationale: "Aberdeen Group's 1997 study was an early authoritative analyst endorsement of enterprise automated software testing at a time when the practice was not yet standard; it articulates the foundational rationale (cost reduction 50-75%, Y2K urgency, Internet testing) that drove adoption across the industry."
relevance: medium
relevance_rationale: "The study's core thesis — that automated testing reduces cost and improves quality — remains directly applicable; however specific platforms (CICS, VTAM, client-server toolsets) are dated; the broader framework for automated testing evaluation transfers strongly to modern CI/CD and DevOps contexts."
prescience: medium
prescience_rationale: "Aberdeen predicted Compuware QACenter would maintain leadership via tight Oracle Developer/2000 integration and a unified scripting language — Compuware was acquired by Thoma Bravo in 2014 and by BMC in 2020 where the products were absorbed; QACenter did not maintain independent market leadership but the automated testing market it helped define grew enormously."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 15
obs_count: 25
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# QACenter: Automated Software Quality From Start to Finish

> Aberdeen Group profiles Compuware's QACenter, a comprehensive automated software testing suite spanning client-server and mainframe platforms. The study documents QACenter's component tools (QARun, QAStress, QALoad, QADirector, QATrack, QAHiperstation, QAPlayback), evaluates its competitive position against Mercury Interactive and SQA/Segue, and presents Aberdeen's research showing that automated testing can reduce application testing cycles and costs by 50-75%. Aberdeen concludes that QACenter is a fully capable enterprise-level testing environment and that automated testing tools have become a necessity in the complex application development lifecycle.

**Author:** Aberdeen Group · **Date:** 1997-01-01 · **Type:** market-study
**Importance:** high — *Aberdeen Group's 1997 study was an early authoritative analyst endorsement of enterprise automated software testing at a time when the practice was not yet standard; it articulates the foundational rationale (cost reduction 50-75%, Y2K urgency, Internet testing) that drove adoption across the indust…*
**Prescience:** medium — *Aberdeen predicted Compuware QACenter would maintain leadership via tight Oracle Developer/2000 integration and a unified scripting language — Compuware was acquired by Thoma Bravo in 2014 and by BMC in 2020 where the products were absorbed; QACenter did not maintain independent market leadership bu…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[compuware|Compuware Corporation]]
- [[mercury-interactive|Mercury Interactive]]
- [[oracle|Oracle Corporation]]
- [[segue-software|Segue Software]]
- [[sqa-inc|SQA Inc.]]

## Technologies (15)

- [[ecotools|EcoTOOLS]]
- [[java|Java]]
- [[oracle-developer-2000|Oracle Developer/2000]]
- [[powerbuilder|PowerBuilder]]
- [[qacenter|Compuware QACenter]]
- [[qadirector|QADirector]]
- [[qahiperstation|QAHiperstation]]
- [[qaload|QALoad]]
- [[qaplayback|QAPlayback]]
- [[qarun|QARun]]
- [[qastress|QAStress]]
- [[qatrack|QATrack]]
- [[uniface|UNIFACE]]
- [[visual-basic|Microsoft Visual Basic]]
- [[windows-nt|Windows NT]]

## Key observations (top 25)

- **1996** — Compuware annual revenues: >$600 million for fiscal year 1996
- **1997** — Compuware Q2 FY1997 revenues: $184.3 million; +31.7% vs Q2 FY1996
- **1997** — Automated testing cost reduction vs manual testing: 50-75% reduction in testing cycle cost and time
- **1997** — Testing cost as share of development budget: Often 1/3 of overall development budget
- **1997** — Enterprise-level testing capability: Fully capable enterprise-level testing environment with integrated test asset management
- **1997** — ATE capability: centralized test process management: QADirector provides repository-based test orchestration
- **1997** — ATE capability: multi-platform coverage: Windows 95/NT/DOS/Unix; TCP/IP/NETBIOS/IPX/SPX; CICS/VTAM/IMS/TSO
- **1997** — ATE capability: dynamic test scripting: QARun auto-translates user actions into test scripts
- **1997** — ATE capability: load and stress testing: QALoad simulates hundreds/thousands of concurrent users; QAStress tests Windows apps
- **1997** — ATE capability: Internet/Web application testing: Supports HTTP/HTML/Java; works within Netscape and IE browsers
- **1997** — ATE capability: mainframe integration: QAHiperstation (VTAM/CICS); QAPlayback (CICS); SAP R/2 VTAM-level testing
- **1997** — ATE capability: defect tracking: QATrack for bug identification/assignment/resolution tracking
- **1997** — ATE capability: test asset reuse: QADirector repository stores/manages test scripts as reusable enterprise assets
- **1997** — Compuware competitive differentiation strategy: Full lifecycle support (create-execute-identify-correct) vs competitors' point-tool approach
- **1997** — Mercury Interactive competitive position: Primary competitor for cross-platform automated testing
- **1997** — SQA competitive position: Windows-specific testing — indirect competitor
- **1997** — Segue Software competitive position: Windows-specific testing — indirect competitor
- **1997** — Aberdeen adoption prediction — automated testing industry-wide: Aberdeen expects serious organizations will purchase automated testing tool in next 2 years (by 1999)
- **1997** — QACenter future requirements: Oracle Developer/2000 integration: Tight integration with Oracle Developer/2000 expected to be maintained and extended
- **1997** — QACenter future requirements: unified scripting language: Common scripting language encompassing all QACenter tools needed for product coherence
- **2014** — Compuware QACenter market position outcome: Compuware taken private by Thoma Bravo 2014 for $2.4B; QACenter did not achieve unified scripting; Mercury Interactive (HP) dominated market
- **1997** — Year 2000 (Y2K) testing applicability: QACenter and QAHiperstation positioned as critical tools for Y2K conversion testing
- **1997** — Compuware Y2K consulting offering: PRODUCTION 2000 consulting approach combining tools/processes/staff
- **1997** — Aberdeen assessment of Compuware financial stability: Consistent financially stable supplier; long-term commitment to development tools market matched by few suppliers
- **1997** — Compuware founding year: Founded 1973

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'qacenter-automated-software-quality-from-start-to--b7003b' ORDER BY year_observed;
```

