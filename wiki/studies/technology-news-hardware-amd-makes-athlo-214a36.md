---
title: "AMD Makes Athlon 64 Thinner, Lighter"
slug: technology-news-hardware-amd-makes-athlo-214a36
page_type: study
author: "Jay Lyman, TechNewsWorld"
date: "2004-05-07"
study_type: news-article
subject_domain: "mobile-processors"
methodology: "product-analysis, analyst-commentary"
importance: medium
importance_rationale: "Documents AMD's mobile-processor pivot to 64-bit in mid-2004, capturing both the security-NX moment (XP SP2 / Sasser) and the emerging laptop-as-desktop-replacement thesis that Kastner articulates as the strategic driver."
relevance: medium
relevance_rationale: "The laptop-displaces-desktop thesis proved durably correct — notebooks passed desktops in US retail 2005 and worldwide 2008. The hardware security-bit pattern (NX/DEP 2004, Intel SGX 2015, pointer authentication 2018, CET 2020) continues to gate OS/browser security."
prescience: high
prescience_rationale: "Kastner's laptop-replacement framing was validated rapidly: US laptop retail unit sales surpassed desktops in 2005; worldwide PC shipments by form factor crossed over 2008. Hardware-security features (XP SP2 NX-bit enforcement) substantially reduced exploit success for code-injection malware — the specific Kastner/Reynolds worm-reduction prediction."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 6
obs_count: 6
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# AMD Makes Athlon 64 Thinner, Lighter

> TechNewsWorld article (May 7 2004, Jay Lyman) on AMD's launch of the Mobile Athlon 64 2800+ and 2700+ ($241/$209 in 1,000-unit quantities) for thin-and-light notebooks, with Enhanced Virus Protection (NX bit) security for the forthcoming Windows XP SP2. Acer's new Ferrari brand and Chinese OEM Amoi will be first to ship. Aberdeen chief research officer Peter Kastner endorses the mobile AMD64 push: 'As more consumers buy notebooks as desktop replacements, it makes sense for AMD to replace its mobility processors with 64-bit Athlons' — a lot of performance at a good value. Kastner identifies the rising laptop share of the total PC market as the key driver. Gartner's Martin Reynolds notes XP SP2 hardware security features will cut worms like the recent Sasser outbreak.

**Author:** Jay Lyman, TechNewsWorld · **Date:** 2004-05-07 · **Type:** news-article
**Importance:** medium — *Documents AMD's mobile-processor pivot to 64-bit in mid-2004, capturing both the security-NX moment (XP SP2 / Sasser) and the emerging laptop-as-desktop-replacement thesis that Kastner articulates as the strategic driver.*
**Prescience:** high — *Kastner's laptop-replacement framing was validated rapidly: US laptop retail unit sales surpassed desktops in 2005; worldwide PC shipments by form factor crossed over 2008. Hardware-security features (XP SP2 NX-bit enforcement) substantially reduced exploit success for code-injection malware — the s…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[acer-inc|Acer Inc.]]
- [[amd|Advanced Micro Devices, Inc.]]
- [[amoi-electronics|Amoi Electronics]]
- [[gartner-inc|Gartner, Inc.]]
- [[intel-corporation|Intel Corporation]]
- [[jay-lyman-journalist|Jay Lyman]]
- [[martin-reynolds-analyst|Martin Reynolds]]
- [[marty-seyer-amd|Marty Seyer]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[technewsworld|TechNewsWorld / ECT News Network]]

## Technologies (6)

- [[amd-athlon-64|AMD Athlon 64 processor]]
- [[amd64-architecture|AMD64 / x86-64 architecture (Opteron/Athlon 64)]]
- [[laptop-notebook-pc|Laptop / notebook PC]]
- [[nx-bit-dep|NX bit / Data Execution Prevention (DEP) / Enhanced Virus Protection]]
- [[windows-xp-64bit|Microsoft Windows XP 64-bit Edition / Windows XP Professional x64 Edition]]
- [[windows-xp-sp2|Microsoft Windows XP Service Pack 2]]

## Key observations (top 25)

- **2004** — Performance at a good value: The Athlon 64 has managed increased market traction because it is a lot of performance at a good value.
- **2004** — Notebooks as desktop replacements: As more consumers buy notebooks as desktop replacements, it makes sense for AMD to replace its mobility processors with 64-bit Athlons. The laptop share of the total PC market is rising steadily, prompting a response from chip and PC makers.
- **2004** — Mobile Athlon 64 2800+ pricing: AMD priced Mobile Athlon 64 2800+ at US$241 and 2700+ at $209 in 1,000-unit quantities, immediately available worldwide. Acer Ferrari and Chinese OEM Amoi Electronics named as first notebook launch partners.
- **2004** — NX/SP2 cuts worms: Gartner's Martin Reynolds: the enhanced security features with XP SP2 are likely to help cut down on the spread of worms such as the recent Sasser outbreak — across the board from both AMD and Intel.
- **2008** — Notebooks pass desktops worldwide: Worldwide PC shipments: notebooks passed desktops in unit volume in 2008 per IDC/Gartner — validating Kastner's rising-laptop-share thesis. US retail notebook sales crossed over desktops already in 2005.
- **2006** — NX/DEP becomes mandatory: NX bit / DEP hardware enforcement became a Windows baseline in Windows Vista (2006) and was later required for Windows 8 (2012). Code-injection worms of the Blaster/Sasser era largely disappeared; attackers shifted to return-oriented programming, JIT…

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'technology-news-hardware-amd-makes-athlo-214a36' ORDER BY year_observed;
```

