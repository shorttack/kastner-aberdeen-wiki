---
title: "Don't Fall for the Siren-Song Price of Under-powered Desktop PCs (Aberdeen Impact)"
slug: aberdeen-impact-desktop-pc-sirens-1998-14b40c
page_type: study
author: "Peter S. Kastner"
date: "1998-09-10"
study_type: white-paper
subject_domain: "enterprise-pcs"
methodology: "industry-analysis, expert-opinion, buying-guide"
importance: high
importance_rationale: "Defining 1998 Kastner-authored Aberdeen 'Impact' on PC procurement strategy; called the corporate PC RAM/upgrade economics correctly at the transition from Windows 95 to Windows 2000."
relevance: medium
relevance_rationale: "'Welded Case' buy-up-the-stack framework remains applicable; specific 1998 PC specs are historical."
prescience: high
prescience_rationale: "Predicted that software upgrades would inevitably consume excess capacity, making 32MB PCs obsolete — verified as Windows 2000 required 64MB minimum and Office 2000 demanded real horsepower."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 14
obs_count: 16
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Don't Fall for the Siren-Song Price of Under-powered Desktop PCs (Aberdeen Impact)

> Aberdeen Group 'Impact' publication (Sept 10, 1998) in which Kastner warns IS executives against the 'siren song' of sub-$1,000 and Celeron-class corporate desktops. Argues that memory pressure from Windows 95/98/NT + Office 97 + Outlook 98 + IE4 + SNMP + anti-virus consumes 60MB virtual memory, making 32MB PCs obsolete. Recommends a 400 MHz Pentium II with 128 MB and a 17-inch monitor at $1,800-2,000 for a 3-year useful life, sized for Office 2000, IE 5, and Windows NT 5.0 (later Windows 2000). Introduces Aberdeen's 'Welded Case' model — buy extra PC power now to avoid labor-intensive upgrades.

**Author:** Peter S. Kastner · **Date:** 1998-09-10 · **Type:** white-paper
**Importance:** high — *Defining 1998 Kastner-authored Aberdeen 'Impact' on PC procurement strategy; called the corporate PC RAM/upgrade economics correctly at the transition from Windows 95 to Windows 2000.*
**Prescience:** high — *Predicted that software upgrades would inevitably consume excess capacity, making 32MB PCs obsolete — verified as Windows 2000 required 64MB minimum and Office 2000 demanded real horsepower.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[intel-corp|Intel Corporation]]
- [[microsoft|Microsoft]]
- [[peter-kastner|Peter S. Kastner]]

## Technologies (14)

- [[ie-4|Internet Explorer 4.0]]
- [[ie-5|Internet Explorer 5.0]]
- [[intel-celeron|Intel Celeron]]
- [[intel-pentium-4|Intel Pentium 4]]
- [[intel-pentium-ii|Intel Pentium II]]
- [[ms-office-2000|Microsoft Office 2000]]
- [[ms-office-97|Microsoft Office 97]]
- [[netbeui|NetBEUI]]
- [[outlook-98|Microsoft Outlook 98]]
- [[snmp|SNMP]]
- [[tcpip|TCP/IP]]
- [[windows-95|Windows 95 OSR2]]
- [[windows-98|Windows 98]]
- [[windows-nt5|Windows NT 5.0 / Windows 2000]]

## Key observations (top 25)

- **1998** — pii-speed: Pentium II up to 450 MHz
- **1995** — 3yr-ago-baseline: Typical new corp PC: 150 MHz, 32MB memory, $2,000+
- **1998** — pii-233-adequate: 233 MHz Pentium II with 32MB 'becoming just adequate'
- **1998** — typical-corp-desktop-stack: Windows 95 OSR2 or 98; TCP/IP+NetBEUI; Office 97; IE 4.0; Outlook 98; SNMP agent; antivirus; workflow apps
- **1998** — kastner-memory-usage: 'Virtual memory usage on my own PC is about 60MB'
- **1998** — mem-32-too-little: 32MB is now too little
- **1998** — welded-case-model: 'Welded Case' model — buy more PC power than needed; avoid labor-intensive upgrades
- **1998** — 3-5yr-asset-life: 3-5 year PC asset life planning
- **1999** — msft-intel-pc-spec: Microsoft-Intel 1999 PC Standard: min 300 MHz, 32 MB
- **1998** — recommended-pc: 400 MHz Pentium II, 128 MB memory, 17\" monitor at $1,800-$2,000
- **1999** — office-2000-horsepower: Recommended config will support Office 2000 and IE 5.0 in 1999
- **2000** — win-nt5-upgrade: Upgrade to Windows NT 5.0 in 2000
- **1998** — avoid-celeron: Avoid Celeron-class or 233 MHz Pentium II inventory close-outs
- **1998** — sub-1000-pc-trend: IS executives captivated by sub-$1,000 PCs; some buying home computers
- **1998** — background-services: Intranet/Internet/Extranet updates (push); e-mail tidal wave; shared workgroup access; systems mgmt SNMP
- **2000** — win2k-rel: Windows 2000 released Feb 2000 with 64MB min RAM requirement

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-impact-desktop-pc-sirens-1998-14b40c' ORDER BY year_observed;
```

