---
title: "Systems Management: Delayed Promise"
slug: systems-management-delayed-promise-1bc587
page_type: study
author: "Stuart J. Johnston with Monua Janah, InformationWeek #694"
date: "1998-08-03"
study_type: feature-article
subject_domain: "systems-management-zero-admin"
methodology: "industry-analysis, vendor-commentary, analyst-commentary"
importance: high
importance_rationale: "Primary contemporaneous IW coverage of Microsoft's Zero Administration initiative at a critical 1998 juncture; Kastner's 'evolutionary not revolutionary' prediction frames how the industry actually experienced the NT 5.0 / Windows 2000 rollout."
relevance: medium
relevance_rationale: "Zero Admin Windows as a branded initiative is long-dead, but its core goals (reduce PC TCO via centralized policy, software distribution, and remote management) persist in modern MDM/Intune/Jamf/Kandji and endpoint-management platforms. Kastner's homogeneity-gating observation recurs today with Azure AD join, co-management."
prescience: high
prescience_rationale: "Kastner's prediction that cost savings would happen 'very slowly, in an evolutionary fashion' gated on NT 5.0 adoption was precisely right. Windows 2000 shipped Feb 2000 (18+ months after this article); enterprise deployment lagged into 2003-2005; mixed-environment pain points persisted well into the Windows XP era. Group Policy, IntelliMirror, and SMS realized their potential only as NT 5.x homogeneity emerged."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 5
obs_count: 6
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Systems Management: Delayed Promise

> InformationWeek issue #694 feature (Aug 3 1998) by Stuart J. Johnston with Monua Janah analyzing the state of Microsoft's Zero Administration Windows (ZAW) initiative nearly two years after its announcement. Core thesis: the pieces are falling into place — Windows-based terminals (HP), Terminal Server edition of Windows NT 4.0, Systems Management Server 2.0 in final testing — but the plan still hinges on the delayed Windows NT 5.0 (later Windows 2000). Peter Kastner, Aberdeen Group analyst, provides the key skeptical quote: full benefits of Zero Administration accrue only to companies with homogeneous NT 5.0 environments, so cost savings 'will happen very slowly, in an evolutionary fashion' as companies upgrade. Additional reporting by Mary Hayes and Caryn Gillooly. Article captures the 1998 moment when NT 5.0's delays and the thin-client/terminal strategy dominated the IT systems-management conversation.

**Author:** Stuart J. Johnston with Monua Janah, InformationWeek #694 · **Date:** 1998-08-03 · **Type:** feature-article
**Importance:** high — *Primary contemporaneous IW coverage of Microsoft's Zero Administration initiative at a critical 1998 juncture; Kastner's 'evolutionary not revolutionary' prediction frames how the industry actually experienced the NT 5.0 / Windows 2000 rollout.*
**Prescience:** high — *Kastner's prediction that cost savings would happen 'very slowly, in an evolutionary fashion' gated on NT 5.0 adoption was precisely right. Windows 2000 shipped Feb 2000 (18+ months after this article); enterprise deployment lagged into 2003-2005; mixed-environment pain points persisted well into th…*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[informationweek|InformationWeek / TechWeb]]
- [[microsoft|Microsoft Corporation]]
- [[monua-janah-journalist|Monua Janah]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stuart-j-johnston-journalist|Stuart J. Johnston]]

## Technologies (5)

- [[systems-management-server|Microsoft Systems Management Server (SMS)]]
- [[windows-nt|Microsoft Windows NT]]
- [[windows-nt-5|Microsoft Windows NT 5.0 / Windows 2000]]
- [[windows-terminal-server|Windows NT 4.0 Terminal Server Edition]]
- [[zero-administration-windows|Microsoft Zero Administration initiative]]

## Key observations (top 25)

- **1998** — Slow evolutionary savings: Full benefits [of Zero Administration] accrue only to companies with homogeneous NT 5.0 environments. Cost savings Microsoft promises will happen very slowly, in an evolutionary fashion, as companies upgrade to NT 5.0.
- **1998** — Terminal Server released: Microsoft released Windows NT 4.0 Terminal Server Edition in June 1998, roughly one month before this article, extending Windows applications to users on Windows-based terminals without full PCs.
- **1998** — SMS 2.0 in final testing: Microsoft had begun final testing of Systems Management Server 2.0 as of Aug 1998 — a significant upgrade intended to deliver software distribution, inventory, and remote-control capabilities tied to the Zero Admin vision.
- **1998** — NT 5.0 delayed: Microsoft Windows NT 5.0 delays were the central risk to the Zero Administration initiative as of August 1998; the release was rebranded Windows 2000 and shipped Feb 17 2000 — roughly 18 months after this article, validating Kastner-era skepticism ab…
- **2003** — Evolutionary realization: Zero Admin Windows as a branded initiative dissolved, but its substance — Group Policy, IntelliMirror, SMS/SCCM, Remote Desktop — became mainstream only as NT 5.x homogeneity emerged in enterprise desktops 2003-2005, directly validating Kastner's evo…
- **2007** — SMS renamed SCCM: Microsoft Systems Management Server was renamed System Center Configuration Manager (SCCM) with the 2007 release; later co-evolved with Microsoft Intune cloud MDM; rebranded Microsoft Endpoint Configuration Manager (2019) and Microsoft Intune (2022)…

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'systems-management-delayed-promise-1bc587' ORDER BY year_observed;
```

