---
title: "Microsoft's Move To Mothball Old Code Raises Concerns"
slug: microsoft-s-move-to-mothball-old-code-ra-724d34
page_type: study
author: "Sharon Gaudin (Datamation / itmanagement.earthweb.com)"
date: "2002-06-17"
study_type: news-article
subject_domain: "software-security"
methodology: "industry-analysis, expert-interview"
importance: medium
importance_rationale: "Early security-focused lifecycle-management framing that anchored Microsoft's Trustworthy Computing initiative (launched January 2002)."
relevance: medium
relevance_rationale: "Old-code-mothballing is a perennial software-engineering policy topic; approach remains a reference for platform-vendor lifecycle decisions."
prescience: high
prescience_rationale: "Kastner's prediction that retiring 16-bit/9x legacy was necessary and correct was borne out — Microsoft's subsequent security posture substantially improved, and dropping 9x support was a significant contributor."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 5
obs_count: 7
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Microsoft's Move To Mothball Old Code Raises Concerns

> Datamation/EarthWeb article on Microsoft's announcement that it will retire pre-Windows NT 32-bit legacy code (Windows 9x / Windows 95) rather than continue patching vulnerabilities. Peter Kastner (Aberdeen Group CRO) endorses the decision — Microsoft has to make this call to stay true to its 'fix security-prone code' mantra — while noting the collateral pain for the tens of millions still on Windows 9x/95. IDC's Dan Kusnetzky offers contrasting nuance.

**Author:** Sharon Gaudin (Datamation / itmanagement.earthweb.com) · **Date:** 2002-06-17 · **Type:** news-article
**Importance:** medium — *Early security-focused lifecycle-management framing that anchored Microsoft's Trustworthy Computing initiative (launched January 2002).*
**Prescience:** high — *Kastner's prediction that retiring 16-bit/9x legacy was necessary and correct was borne out — Microsoft's subsequent security posture substantially improved, and dropping 9x support was a significant contributor.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[dan-kusnetzky|Dan Kusnetzky]]
- [[idc|International Data Corporation (IDC)]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sharon-gaudin|Sharon Gaudin]]

## Technologies (5)

- [[trustworthy-computing|Microsoft Trustworthy Computing Initiative]]
- [[windows-95|Microsoft Windows 95]]
- [[windows-98|Microsoft Windows 98]]
- [[windows-9x|Microsoft Windows 9x]]
- [[windows-nt|Microsoft Windows NT]]

## Key observations (top 25)

- **2002** — Old-code retirement is the only answer: 'I think it's the only answer they could give and still be true to the mantra of: if we find security-prone problems in our code, we will fix it.' Code otherwise working is being ripped out because it has fundamental security flaws.
- **2002** — Windows 9x installed base: Tens of millions still using Windows 9x, including millions still on Windows 95.
- **2002** — Move enterprise to Windows NT: Microsoft will say they've been advising enterprise customers for years to move to Windows NT - based on newer 32-bit code.
- **2002** — Old-code retirement policy: Microsoft announced policy of ripping out legacy pre-NT code rather than patching individual vulnerabilities.
- **2002** — Kusnetzky measured counterpoint: 'What will have trouble and what won't depends on what Microsoft finds and what replaces the legacy code. If the new code operates the same…'
- **2002** — Trustworthy Computing success: Kastner and the article imply the old-code retirement is necessary for Microsoft to earn credibility on security.
- **2007** — Microsoft security posture improved: Microsoft Trustworthy Computing produced measurable security improvements: Windows XP SP2 (2004), Vista UAC, defender, certification; 9x formally retired 2006.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'microsoft-s-move-to-mothball-old-code-ra-724d34' ORDER BY year_observed;
```

