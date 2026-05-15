---
title: "PC Replacements: Lawyers, Auditors, and Common Sense Rules"
slug: dct-pc-replacement-insight1-2003-04
page_type: study
author: "Peter S. Kastner"
date: "2003-04-24"
study_type: dct
subject_domain: "enterprise-pc/lifecycle-management"
methodology: "industry-analysis, document-review"
importance: high
importance_rationale: "Framed the mid-2003 enterprise PC replacement cycle and contributed to Aberdeen's CIO guidance during the Windows 98/NT 4 end-of-support transition."
relevance: high
relevance_rationale: "Core framework (vendor support lifecycle + audit/legal exposure) remains directly applicable to enterprise OS migration planning today."
prescience: high
prescience_rationale: "Kastner predicted (all proved correct): Windows XP Pro SP1 stability, Pentium 4 Hyper-Threading mainstreaming in 2003, sub-5-lb Centrino notebook adoption, Springdale 800 MHz FSB mainstreaming, ~1/3 corporate purchases going mobile."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 11
obs_count: 21
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# PC Replacements: Lawyers, Auditors, and Common Sense Rules

> Aberdeen InSight arguing that the roughly 50 million Windows 98 / NT 4 corporate PCs still in service by mid-2003 should be accelerated off the desktop. Windows NT 4.x end-of-support (June 30, 2003) and Windows 98/SE (January 16, 2004) expose enterprises to unpatched security risk, auditor scrutiny, and potential negligence claims. Mid-2003 is framed as an auspicious PC replacement window anchored by Windows XP Pro SP1, Server 2003, Office 2003, Intel Springdale, Pentium 4 Hyper-Threading, and Centrino notebooks.

**Author:** Peter S. Kastner · **Date:** 2003-04-24 · **Type:** dct
**Importance:** high — *Framed the mid-2003 enterprise PC replacement cycle and contributed to Aberdeen's CIO guidance during the Windows 98/NT 4 end-of-support transition.*
**Prescience:** high — *Kastner predicted (all proved correct): Windows XP Pro SP1 stability, Pentium 4 Hyper-Threading mainstreaming in 2003, sub-5-lb Centrino notebook adoption, Springdale 800 MHz FSB mainstreaming, ~1/3 corporate purchases going mobile.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[ford-motor-company|Ford Motor Company]]
- [[intel|Intel Corporation]]
- [[microsoft|Microsoft]]
- [[symantec|Symantec]]

## Technologies (11)

- [[exchange-server-2003|Exchange Server 2003]]
- [[intel-centrino|Intel Centrino platform]]
- [[intel-pentium-4-ht|Intel Pentium 4 with Hyper-Threading]]
- [[intel-springdale|Intel Springdale 865/875 chipset]]
- [[office-2003|Office 2003]]
- [[sql-server-2000|SQL Server]]
- [[w95-tenrobot|W95.Tenrobot virus]]
- [[windows-98|Windows 98 / 98SE]]
- [[windows-nt-4|Windows NT 4.0 Workstation]]
- [[windows-server-2003|Windows Server 2003]]
- [[windows-xp-pro|Windows XP Professional]]

## Key observations (top 25)

- **2003** — Installed base of aging corporate PCs: 50,000,000+ Windows 98 / NT 4 PCs worldwide
- **2003** — Windows NT 4.x end of support: June 30, 2003
- **2003** — Windows 98/SE end of support: January 16, 2004
- **2003** — Microsoft support policy: Five-year support window after OS introduction
- **2003** — Virus example: W95.Tenrobot — memory-resident file appender on Win 95/98/Me
- **2003** — Auditability gap: Win 98/NT lack facilities to indicate machine has been hacked
- **2003** — Governance framing: Unpatched corporate desktops = unacceptable IT practice
- **2003** — Legal exposure: Negligence claim risk; reputational risk of 'laughing stock' outcomes
- **2003** — Client OS readiness: Windows XP Pro SP1 out and working well — no stability problems
- **2003** — Server-side readiness: Server 2003 + Exchange 2003 + SQL Server more efficient users of resources
- **2003** — Office 2003 near-term availability: Out in a few months; worth evaluating
- **2003** — Platform stability window: Springdale inaugurates 18-month platform/image stability period
- **2003** — Hyper-Threading mainstreaming: P4 HT now mainstream — better multi-tasking and thread-aware apps
- **2003** — Notebook mix: ~1/3 corporate PC purchases in 2003 will be notebooks; Centrino = long battery life + wireless productivity
- **2003** — Reference desktop price: $1,250-$1,400 including Windows XP Pro and Office XP Pro
- **2003** — Capital asset cost: ~$2/day over 3-4 years
- **2003** — Aberdeen internal precedent: Aberdeen itself upgraded its aging PC ecosystem the prior year
- **2003** — Prescriptive recommendation: SMBs lacking 24x7 IT should crank up planning for the recession-disrupted PC replacement cycle
- **2004** — Centrino adoption: Centrino achieved rapid mainstream adoption: launched March 12 2003; by end of 2003 Centrino-branded notebooks dominated business + premium consumer notebook segments; Intel reported Centrino as core of mobile PC growth through 2005 when Core Duo rep…
- **2006** — Windows XP corporate mainstream: Windows XP became the corporate mainstream desktop OS by mid-2004; Microsoft extended XP support multiple times due to Vista's slow corporate uptake (2007-2009); XP remained dominant enterprise desktop until Windows 7 displacement 2010-2013. Corporat…
- **2003** — Rhetorical parallel: Ford guarantees parts 5 years; Microsoft supports OS 5 years

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-pc-replacement-insight1-2003-04' ORDER BY year_observed;
```

