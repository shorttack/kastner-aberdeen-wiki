---
title: "DCT Segment Priorities Matrix (Home / Work / Mobile)"
slug: dct-segment-priorities-matrix-2003
page_type: study
author: "Peter S. Kastner"
date: "2002-11-01"
study_type: dct
subject_domain: "dct/segment-prioritization"
methodology: "industry-analysis"
importance: medium
importance_rationale: "Internal prioritization framework used to drive Aberdeen Personal IT coverage decisions; anchors interpretation of subsequent topic/weekly output."
relevance: medium
relevance_rationale: "Matrix structure remains relevant to any multi-segment tech analyst practice; specific technology calls are dated."
prescience: high
prescience_rationale: "Kastner's 2.2→3.6 GHz desktop CPU call in 18 months was directionally correct (mainstream P4 reached 3.6 GHz by 2004); WiFi usability + Pentium 4 laptop inflection both materialized in 2003."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 16
obs_count: 21
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# DCT Segment Priorities Matrix (Home / Work / Mobile)

> Aberdeen Personal IT / DCT segment-priorities matrix cross-tabulating four technology categories (Computers & Peripherals, Networking, Productivity Apps & Services, Leisure & Entertainment) against three contexts (Home, Work, Mobile). Captures priority rankings with analyst notes — including desktop-CPU 2.2->3.6 GHz 18-month roadmap, Pentium 4 laptop impact, 2002 as a 'banner year for home networks' caveated on wireless usability, and 2003 PC/TV/stereo integration outlook.

**Author:** Peter S. Kastner · **Date:** 2002-11-01 · **Type:** dct
**Importance:** medium — *Internal prioritization framework used to drive Aberdeen Personal IT coverage decisions; anchors interpretation of subsequent topic/weekly output.*
**Prescience:** high — *Kastner's 2.2→3.6 GHz desktop CPU call in 18 months was directionally correct (mainstream P4 reached 3.6 GHz by 2004); WiFi usability + Pentium 4 laptop inflection both materialized in 2003.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[aol|America Online]]
- [[intel|Intel Corporation]]
- [[isaac-ro|Isaac Ro]]
- [[maged-shaker|Maged (Shaker)]]
- [[microsoft|Microsoft]]

## Technologies (16)

- [[cellular-data|Cellular data (2G/3G)]]
- [[desktop-pc|Desktop PC]]
- [[ethernet|Ethernet]]
- [[home-automation|Home automation]]
- [[ieee-802-11a|IEEE 802.11a WiFi]]
- [[intel-pentium-4|Intel Pentium 4]]
- [[location-services|Location-based services]]
- [[notebook-pc|Notebook / laptop PC]]
- [[pda|Personal Digital Assistant (PDA)]]
- [[personal-firewall|Personal firewall]]
- [[pim|Personal Information Management (PIM)]]
- [[pna|HomePNA phoneline networking]]
- [[powerline-networking|Powerline home networking]]
- [[pvr|Personal Video Recorder]]
- [[tablet-pc|Tablet PC]]
- [[wifi|WiFi (generic)]]

## Key observations (top 25)

- **2002** — Matrix structure: 4 technology categories x 3 contexts (Home/Work/Mobile)
- **2002** — Home — Computers: Desktop, laptop, tablet
- **2002** — Home — Computers note: Multiple PCs drives need for home networking
- **2003** — PC/TV/stereo integration outlook: In 2003, PCs integrate well with TV/stereo
- **2002** — System-bundle usability: Usability in system bundles an issue
- **2003** — Desktop CPU roadmap: Desktop MHz goes from 2.2 to 3.6 in 18 months
- **2003** — Notebook CPU inflection: Pentium 4 laptops are major performance improvement
- **2002** — Home — Networking: WiFi, PNA, Powerline, Ethernet, home automation
- **2002** — Home networking year: 2002 will be a banner year for home networks
- **2002** — Wireless usability: Usability a huge issue — wireless not the only choice
- **2002** — Work — Networking: WiFi 802.11a
- **2002** — Mobile — Networking: WiFi, cellular
- **2002** — Home — Productivity low-priority: Personal firewalls, security, OS, utilities, personal messaging, AOL/MSN services
- **2002** — Work — Productivity: Office
- **2002** — Mobile — Productivity: PIM
- **2002** — Home — Leisure: PVR, TV/stereo convergence, games, digital appliances
- **2002** — TV/stereo integration friction: In 2002, making a TV and stereo work with a PC is difficult
- **2003** — Relief on the way: Relief on the way in 2003 — what are the tradeoffs by buying now?
- **2002** — Mobile — Leisure: Location
- **2002** — Mobile — Computers: Laptop, PDA
- **2004** — Desktop CPU 3.6 GHz: Pentium 4 reached 3.6 GHz with the Prescott F-series / Pentium 4 560 launched June 21 2004 (3.6 GHz) — within the anticipated timeline; NetBurst hit its 3.8 GHz ceiling with P4 570J by November 2004 before thermal limits forced the architectural pivo…

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dct-segment-priorities-matrix-2003' ORDER BY year_observed;
```

