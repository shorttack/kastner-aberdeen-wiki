---
title: "The Novell Predicament"
slug: aberdeen-1995-novell-predicament
page_type: study
author: "Aberdeen Group"
date: "1995-08-09"
study_type: market-viewpoint
subject_domain: "network operating systems and enterprise server market"
methodology: "user-interviews,vendor-briefing,analyst-assessment"
importance: high
importance_rationale: "This Market Viewpoint is a precise contemporaneous prediction of Novell's decline, issued August 1995. It documents the exact inflection point when enterprise IT shifted from NetWare to Windows NT, with supporting data from IT managers, hardware suppliers, and ISVs—a rare multi-source convergence."
relevance: high
relevance_rationale: "Novell's fate is a canonical case study in disruption by a platform transition. The specific mechanisms Aberdeen identified (ISV attrition, NDS vs. NT directory war, file/print commoditization) are directly relevant to understanding platform-era market shifts."
prescience: high
prescience_rationale: "Aberdeen's predictions were remarkably accurate: Windows NT did displace NetWare in enterprise file/print; Novell was acquired by Attachmate in 2011; NDS/eDirectory did not achieve broad cross-platform adoption; LDAP did become the dominant directory protocol over NDS."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 8
obs_count: 28
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# The Novell Predicament

> Aberdeen examines Novell's strategic crisis in August 1995, finding that IT managers are standardizing on Windows NT and that Novell has failed to execute its application server strategy. The report details Novell's three principal failure modes (tactical changes, technical execution failures, ISV attrition) and projects erosion of Novell's enterprise position. Aberdeen advises IT executives to carefully evaluate NetWare for medium and long term use while outlining prescriptions for Novell's survival.

**Author:** Aberdeen Group · **Date:** 1995-08-09 · **Type:** market-viewpoint
**Importance:** high — *This Market Viewpoint is a precise contemporaneous prediction of Novell's decline, issued August 1995. It documents the exact inflection point when enterprise IT shifted from NetWare to Windows NT, with supporting data from IT managers, hardware suppliers, and ISVs—a rare multi-source convergence.*
**Prescience:** high — *Aberdeen's predictions were remarkably accurate: Windows NT did displace NetWare in enterprise file/print; Novell was acquired by Attachmate in 2011; NDS/eDirectory did not achieve broad cross-platform adoption; LDAP did become the dominant directory protocol over NDS.*

## Entities (7)

- [[ENT-ATTACHMATE|Attachmate Group]]
- [[ENT-CA|Computer Associates (CA)]]
- [[ENT-IBM-OS2|IBM (OS/2 Warp Server)]]
- [[ENT-LOTUS|Lotus Development Corporation (IBM)]]
- [[ENT-MSFT-NT|Microsoft Corporation (Windows NT)]]
- [[ENT-NETSCAPE|Netscape Communications]]
- [[ENT-NOVELL|Novell Inc.]]

## Technologies (8)

- [[TECH-EXCHANGE|Microsoft Exchange Server]]
- [[TECH-GROUPWISE|Novell GroupWise]]
- [[TECH-LDAP|LDAP (Lightweight Directory Access Protocol)]]
- [[TECH-MANAGEWISE|Novell ManageWise]]
- [[TECH-NDS|Novell Directory Services (NDS)]]
- [[TECH-NETWARE|Novell NetWare]]
- [[TECH-OLE-DIR|Microsoft OLE Directory Services]]
- [[TECH-WINNT|Windows NT Server]]

## Key observations (top 25)

- **1995** — NetWare enterprise standard status: IT managers standardizing on Windows NT Workstation as desktop; expect NT Server to replace NetWare file/print
- **1995** — Novell failure modes: 3 principal failures: annual tactic changes, technical execution failures, ISV attrition
- **1995** — NDS value proposition: excellent cross-platform interoperability for Novell+NT+Unix; hierarchical management view
- **1995** — Windows NT market momentum: NT Server unit sales ramping; PC server suppliers reporting NetWare sales decline vs NT growth
- **1995** — Novell enterprise position trajectory: further erosion of Novell enterprise position projected
- **1995** — OLE Directory adoption prediction: Microsoft OLE Directory Services will succeed because OLE-enabled applications drag it into enterprise
- **1995** — LDAP as de-facto directory standard: LDAP will become de-facto directory services standard for Internet
- **1995** — NDS cross-platform acceptance: little evidence NDS will achieve widespread acceptance outside Novell installed base
- **2011** — Novell corporate fate: acquired by Attachmate Group for $2.2B in April 2011; 882 patents sold to Microsoft consortium for $450M
- **2000** — Windows NT server market outcome: Windows NT and successors (2000/2003) became dominant enterprise network OS; NetWare marginalized
- **2000** — LDAP actual outcome: LDAP became universal directory protocol; embedded in Active Directory, OpenLDAP, all major systems
- **2005** — GroupWise groupware market fate: GroupWise lost groupware war to Exchange/Notes; retained only legacy Novell-loyal customers
- **1995** — Green River (NetWare next release) expected features: SMP, distributed print, systems management, improved IP support
- **1995** — Novell strategic prescription (Aberdeen): Must make NDS best on NT bar none; open new markets to dominate; embrace NT not fight it
- **1995** — Novell historical failed initiatives: Portable NetWare, AppWare, Tuxedo acquisition, UnixWare, WordPerfect—all failed
- **1995** — Novell study publication date: Volume 9/Number 14, August 9, 1995
- **1995** — ISV porting to NetWare status: few ISVs actively porting applications to NetWare; ISVs look elsewhere
- **1995** — Groupware competitive landscape: Novell GroupWise vs IBM Notes vs HP OpenMail vs Microsoft Exchange vs Netscape CollabraShare
- **1995** — NDS multimedia/telecom positioning: NDS infrastructure services marketed to AT&T, Deutsche Telekom, NTT, Telstra, Unisource
- **1995** — Network management competitor landscape: ManageWise vs CA Unicenter vs HP OpenView as competing network management frameworks
- **1995** — Novell revenue trend: revenue declines confirmed; Aberdeen analysis confirms declining trend
- **1995** — NT-NDS integration prediction: Either Novell fully integrates NDS with NT or Microsoft delivers OLE Directory interoperating with NDS
- **2000** — Active Directory outcome: Active Directory shipped in Windows 2000; became dominant enterprise directory service
- **1995** — Lotus acquisition: IBM acquired Lotus Development Corporation for $3.5B in 1995
- **1995** — Aberdeen advisory stance: IT executives advised to carefully evaluate NetWare use for medium and long term

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1995-novell-predicament' ORDER BY year_observed;
```

