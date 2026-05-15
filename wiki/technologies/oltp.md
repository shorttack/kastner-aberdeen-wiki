---
title: "Online Transaction Processing"
slug: oltp
page_type: technology
category: application
vendor: "Various"
era: "1992"
lifecycle_at_study: "current"
lifecycle_current: "current"
tier: 1
study_count: 18
obs_count: 43
aliases: ["Online Transaction Processing"]
tags: [type/technology, category/application, vendor/various]
source_csv: known_technologies.csv
---

# Online Transaction Processing

Online Transaction Processing is a application from Various (era 1992). Current lifecycle: current.

**Appears in 18 studies, 43 observations.**

## Studies citing this technology

- [[volume-1-appendix-career-timeline|Appendix: Career Timeline]] (2026-05-14)
- [[volume-1-ch05-stratus-fault-tolerant-wars-1981-1987|Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987)]] (2026-05-14)
- [[volume-1-ch06-dec-mainframes-last-stand-1987-1988|Chapter 6: Digital Equipment Corporation — The Mainframe's Last Stand (1987–1988)]] (2026-05-14)
- [[volume-1-ch10-the-long-view-1966-2026|Chapter 10: The Long View — What Fifty Years of Technology Markets Teach (1966-2026)]] (2026-05-14)
- [[psk-bio2004-939357|Biography of Peter S. Kastner, Chief Research Officer (2004)]] (2004)
- [[15-classification-key-applications-55b6be|Classification of Key Applications by Storage Category]] (2003-01-01)
- [[bio-webfocus-bef516|Peter Kastner - Aberdeen Group Biography (~2001)]] (2001)
- [[psk-niopubs-3d103b|Peter S. Kastner -- EVP/CRO Biography, Publications List, and Career History]] (1999-01-01)
- [[psk-ibmbio-fde139|Peter S. Kastner Biography for IBM Engagements (VP Era, c.1993-1995)]] (1993-1995)
- [[aberdeen-press-advisory-kastner-appointm-efd58c|Aberdeen Group Press Advisory and News Release: Aberdeen Group Picks Industry Veteran Peter S. Kastner to Head New Trans…]] (1988-12-05)

## Top observations

- **2003** — Traditional OLTP access pattern: Update intensive — both reads and writes with focus on writes ([[15-classification-key-applications-55b6be]])
- **1996** — enterprise superserver workload: New multi-tier architectures demand enterprise superservers for OLTP, DSS, and messaging workloads ([[1996-sequent-38f0b1]])
- **1996** — oltp_session_requirement: sessions_intrinsic_to_cs_not_browser ([[aberdeen-1996-3com-reconciling-clientserver-development-internet]])
- **1988** — Aberdeen Transaction Services thesis: Transaction processing is growing faster than enterprises can cope with it, particularly as they distribute computing throughout their organizations ([[aberdeen-press-advisory-kastner-appointm-efd58c]])
- **1988** — Aberdeen Transaction Services location: Located at Aberdeen corporate HQ in Boston ([[aberdeen-press-advisory-kastner-appointm-efd58c]])
- **** — :  ([[bio-webfocus-bef516]])
- **1988** — TP-market-size-1988: Transaction processing market approximately $26 billion; growing at 20-30% per year; expected to reach $60 billion by 1991 ([[dec-mgmt-memo-v7n5-state-of-company-1988-6a9954]])
- **1988** — TP-response-time-requirement: 90-95% of TP actions must complete in 1-2 seconds; systems are 'bet your business' applications requiring near-zero downtime ([[dec-mgmt-memo-v7n5-state-of-company-1988-6a9954]])
- **1988** — DATAMATION-survey-DEC-TP-intent: DATAMATION survey: customers report 1.3% of their TP systems currently from DEC; expect 10.4% from DEC by end of next year ([[dec-mgmt-memo-v7n5-state-of-company-1988-6a9954]])
- **1981** — Position: Manager Marketing Development, Stratus Computer, Inc.: Oct 1981-1987 (present at time of document) ([[dec-resume-performance-review-3-1f133b]])
- **1981** — Stratus Computer marketing growth: From zero to $200M sales level ([[dec-resume-performance-review-3-1f133b]])
- **1986** — Stratus Manager Marketing Development responsibilities: Competitive analysis, consultant relations, major opportunity sales planning, product introduction ([[dec-resume-performance-review-3-1f133b]])
- **1988** — DEC 1988 revenue: $11.5 billion ([[dectp-genspark-research2-4-a09a82]])
- **1988** — DEC TP market share pre-DECtp: ~5% ([[dectp-genspark-research2-4-a09a82]])
- **1988** — DECtp market share target by 1991: 10-15% ([[dectp-genspark-research2-4-a09a82]])
- **1988** — DECtp total throughput claim: Up to 9 million transactions per day ([[dectp-genspark-research2-4-a09a82]])
- **1992** — DEC first major annual loss: -$2.8 billion ([[dectp-genspark-research2-4-a09a82]])
- **1987** — Kastner Yankee Group OLTP study: Ghost-wrote 'The Future of OLTP'; completed late 1987; published early 1988 ([[dectp-genspark-research2-4-a09a82]])
- **1988** — Kastner Aberdeen Group co-founders: John R. Logan, Charles T. Casale (both former Prime), Thomas W. Willmott (formerly IDC) ([[dectp-genspark-research2-4-a09a82]])
- **1988** — DECtp SWOT: key weaknesses: 5% TP market share; engineering-centric culture; lack of enterprise SW partnerships; minimal TP experience ([[dectp-genspark-research2-4-a09a82]])

## DuckDB query for full data

```sql
SELECT * FROM observations WHERE tech_id = 'oltp';
```

