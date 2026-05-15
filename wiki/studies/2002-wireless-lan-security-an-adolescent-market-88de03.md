---
title: "Wireless LAN Security: An Adolescent Market"
slug: 2002-wireless-lan-security-an-adolescent-market-88de03
page_type: study
author: "Eric Hemmendinger"
date: "2002-10-01"
study_type: market-study
subject_domain: "network-security"
methodology: "industry-analysis, competitive-profiling, technology-assessment, expert-opinion"
importance: high
importance_rationale: "Published in October 2002 when WEP's fundamental security flaws were becoming publicly known, this InSight correctly identified the three-capability framework (VPN + personal firewall + seamless hand-off) that shaped enterprise WLAN security procurement for the following decade."
relevance: medium
relevance_rationale: "The three-capability framework (VPN, personal firewall, seamless handoff) maps directly to modern zero-trust network access architectures; while specific vendor names are dated, the problem framing and solution taxonomy remain relevant to enterprise Wi-Fi security design today."
prescience: medium
prescience_rationale: "The study correctly predicted that WLAN security would require dedicated solutions beyond WEP. The specific vendors it highlighted had mixed outcomes — AirDefense was acquired by Motorola (2008), Blue Socket by Adtran (2011), while others dissolved — reflecting the market consolidation the study anticipated."
license: CC-BY-4.0
tier: 1
entity_count: 16
tech_count: 8
obs_count: 18
tags: [type/study, importance/high, prescience/medium, decade/2000s]
source_csv: master_studies.csv
---

# Wireless LAN Security: An Adolescent Market

> This InSight addresses the challenge IT decision-makers face in securing wireless LAN environments and identifies three critical capabilities: VPNs, personal firewalls, and seamless WAP hand-off solutions. The study profiles the emerging WLAN security vendor landscape including AirDefense, Blue Socket, Cranite, Ecutel, Fortress Technologies, ReefEdge, and others, framing WLAN security as an adolescent market in need of maturation.

**Author:** Eric Hemmendinger · **Date:** 2002-10-01 · **Type:** market-study
**Importance:** high — *Published in October 2002 when WEP's fundamental security flaws were becoming publicly known, this InSight correctly identified the three-capability framework (VPN + personal firewall + seamless hand-off) that shaped enterprise WLAN security procurement for the following decade.*
**Prescience:** medium — *The study correctly predicted that WLAN security would require dedicated solutions beyond WEP. The specific vendors it highlighted had mixed outcomes — AirDefense was acquired by Motorola (2008), Blue Socket by Adtran (2011), while others dissolved — reflecting the market consolidation the study ant…*

## Entities (16)

- [[aberdeen-group|Aberdeen Group]]
- [[airdefense-inc|AirDefense Inc.]]
- [[blue-socket|Blue Socket Inc.]]
- [[check-point|Check Point Software Technologies]]
- [[cisco-systems|Cisco Systems Inc.]]
- [[cranite-systems|Cranite Systems]]
- [[ecutel-inc|Ecutel Inc.]]
- [[fortress-technologies|Fortress Technologies]]
- [[imperito-networks|Imperito Networks]]
- [[leap-point|Leap Point Inc.]]
- [[netmotion-wireless|NetMotion Wireless]]
- [[openreach-inc|OpenReach Inc.]]
- [[reefedge-inc|ReefEdge Inc.]]
- [[safenet-inc|SafeNet Inc.]]
- [[vernier-networks|Vernier Networks]]
- [[wavelink-corp|Wavelink Corporation]]

## Technologies (8)

- [[mac-filtering|MAC Address Filtering]]
- [[personal-firewall|Personal Firewall]]
- [[pki|Public Key Infrastructure (PKI)]]
- [[vpn|Virtual Private Network (VPN)]]
- [[wap-handoff|WAP Seamless Handoff]]
- [[wep|Wireless Encryption Protocol (WEP)]]
- [[wlan|Wireless LAN (WLAN)]]
- [[wpa|Wi-Fi Protected Access (WPA)]]

## Key observations (top 25)

- **2002** — WLAN security market maturity: Market described as adolescent — growing but lacking mature security solutions
- **2002** — WLAN adoption trajectory: As wireless LAN access increases so too do the problems of IT administrators
- **2002** — WLAN security capability 1: VPN: VPN is one of three essential capabilities for WLAN security
- **2002** — WLAN security capability 2: Personal firewall: Personal firewall is one of three essential capabilities for WLAN security
- **2002** — WLAN security capability 3: Seamless WAP handoff: Seamless hand-off between WAPs is one of three essential capabilities for WLAN security
- **2002** — WEP security adequacy: WEP insufficient for enterprise WLAN security; dedicated solutions required
- **2004** — WEP deprecated: Wi-Fi Alliance deprecated WEP in 2004; replaced by WPA/WPA2
- **2002** — AirDefense market position: WLAN security and monitoring vendor in emerging security segment
- **2008** — AirDefense acquisition: Acquired by Motorola in 2008; became Motorola AirDefense
- **2002** — Blue Socket market position: Wireless gateway and WLAN security vendor
- **2011** — Blue Socket acquisition: Acquired by Adtran in 2011; previously acquired Pingtel in direction change
- **2002** — ReefEdge competitive viability: Small WLAN security startup competing in adolescent market
- **2005** — ReefEdge dissolution: ReefEdge dissolved circa 2005; Blue Socket offered rebates to stranded customers
- **2002** — WLAN security market consolidation: Adolescent market expected to mature through vendor consolidation
- **2010** — WLAN security market consolidation outcome: Most specialist WLAN security startups dissolved or acquired by 2010; Cisco, Aruba, Motorola dominated
- **2002** — Cisco incumbent position: Major WLAN infrastructure vendor; potential to add security capabilities
- **2010** — Cisco WLAN security dominance: Cisco became dominant enterprise WLAN security vendor post-2005
- **2016** — Fortress Technologies acquisition: Acquired by Airbus Defence and Space in 2016; survived due to military-grade niche

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '2002-wireless-lan-security-an-adolescent-market-88de03' ORDER BY year_observed;
```

