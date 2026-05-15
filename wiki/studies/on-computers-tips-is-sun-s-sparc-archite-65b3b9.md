---
title: "Is Sun's SPARC Architecture on Life Support?"
slug: on-computers-tips-is-sun-s-sparc-archite-65b3b9
page_type: study
author: "Peter S. Kastner"
date: "2009-06-17"
study_type: memoir
subject_domain: "memoir"
methodology: "oral-history"
importance: high
importance_rationale: "Correctly calls the SPARC endgame at the moment of the Oracle-Sun merger; positions Oracle integrated-stack thesis later realized through Exadata/Exalogic etc."
relevance: high
relevance_rationale: "SPARC did wind down; Oracle did pursue integrated-stack strategy — this memoir is a primary-source prediction that proved accurate."
prescience: high
prescience_rationale: "Rock was cancelled post-merger (2009); Solaris on x86 won commodity share; SPARC business cut by Oracle 2017; Oracle did pursue full-stack strategy with Exadata, Exalogic, SaaS."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 6
obs_count: 7
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Is Sun's SPARC Architecture on Life Support?

> Kastner blog post on OnComputersTips observing Sun's long-hyped Rock chip is apparently dead and that — with the pending Oracle-Sun merger and Solaris already on X64 commodity servers — the case for SPARC is gone. Kastner muses that Oracle has the opportunity to create a one-stop IT shop with the full hardware-to-application stack, unmatched since IBM exited the application software business 40 years earlier.

**Author:** Peter S. Kastner · **Date:** 2009-06-17 · **Type:** memoir
**Importance:** high — *Correctly calls the SPARC endgame at the moment of the Oracle-Sun merger; positions Oracle integrated-stack thesis later realized through Exadata/Exalogic etc.*
**Prescience:** high — *Rock was cancelled post-merger (2009); Solaris on x86 won commodity share; SPARC business cut by Oracle 2017; Oracle did pursue full-stack strategy with Exadata, Exalogic, SaaS.*

## Entities (6)

- [[amd|Advanced Micro Devices]]
- [[ibm|International Business Machines Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[oracle-corp|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (6)

- [[oracle-exadata|Oracle Exadata Database Machine]]
- [[solaris-os|Solaris Operating System]]
- [[sparc-architecture|SPARC processor architecture]]
- [[sun-niagara-t1|Sun UltraSPARC T1 (Niagara)]]
- [[sun-rock-chip|Sun Rock UltraSPARC processor]]
- [[x64-commodity-server|x86-64 commodity server]]

## Key observations (top 25)

- **2009** — Rock chip dead: Sun's long-hyped Rock chip is apparently dead. Well, that's one less project for Oracle to cancel when the merger goes through.
- **2009** — SPARC case gone: With Sun's high-end future SPARC platform DOA, the future of SPARC machines gets riskier for enterprise IT strategists. With Solaris available on X64 commodity servers, there's no longer a huge case for SPARC.
- **2009** — Oracle full-stack opportunity: Oracle has the opportunity to create the one-stop shop for IT — entire stack from base server hardware to Layer 7 applications — that has not existed since IBM got out of the application software business 40 years ago this month.
- **2009** — Open question: What will Oracle do with that opportunity?
- **2009** — Rock cancelled: Sun Rock chip was officially cancelled shortly after Oracle-Sun merger closed in 2010; the high-end SPARC roadmap was reset around T-series.
- **2017** — Full-stack realized: Oracle did build the integrated stack: Exadata database machines, Exalogic, Oracle Cloud Infrastructure, SaaS apps — realizing Kastner's prediction.
- **2017** — SPARC Solaris team layoff: Oracle laid off most of the Solaris and SPARC engineering staff in September 2017; SPARC M8 was the last new CPU; T-series entered long-term sustaining mode.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'on-computers-tips-is-sun-s-sparc-archite-65b3b9' ORDER BY year_observed;
```

