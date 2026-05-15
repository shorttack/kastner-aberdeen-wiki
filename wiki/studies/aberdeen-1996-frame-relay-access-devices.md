---
title: "Frame Relay Access Devices"
slug: aberdeen-1996-frame-relay-access-devices
page_type: study
author: "Aberdeen Group"
date: "1996-06-01"
study_type: market-study
subject_domain: "networking-WAN-frame-relay"
methodology: "industry-analysis, competitive-profiling, field-research"
importance: medium
importance_rationale: "Documented the FRAD vs. router decision at peak frame relay adoption; useful for understanding the SNA-to-IP transition period and WAN technology competitive dynamics of the mid-1990s."
relevance: low
relevance_rationale: "Frame relay and SNA are legacy protocols essentially replaced by MPLS, SD-WAN, and IP-native architectures; the study is primarily of historical interest for networking technology evolution."
prescience: high
prescience_rationale: "Aberdeen's prediction that frame relay would persist as an ATM edge network rather than being displaced proved accurate; ATM never displaced frame relay which coexisted until both were eventually superseded by MPLS/IP in the 2000s."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 6
obs_count: 18
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Frame Relay Access Devices

> This Aberdeen Group profile evaluates Netlink, Inc.'s family of Frame Relay Access Devices (FRADs) including TurboFRAD, OmniFRAD, NetFRAD, and the OmniLinx 8000 edge switch. The study examines the technical advantages of FRADs over routers for mixed SNA/LAN enterprise WAN environments, documents customer ROI through 20-25% leased-line cost savings, and predicts that frame relay will remain integral to the eventual ATM migration as an edge network.

**Author:** Aberdeen Group · **Date:** 1996-06-01 · **Type:** market-study
**Importance:** medium — *Documented the FRAD vs. router decision at peak frame relay adoption; useful for understanding the SNA-to-IP transition period and WAN technology competitive dynamics of the mid-1990s.*
**Prescience:** high — *Aberdeen's prediction that frame relay would persist as an ATM edge network rather than being displaced proved accurate; ATM never displaced frame relay which coexisted until both were eventually superseded by MPLS/IP in the 2000s.*

## Entities (6)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[anixter|Anixter International]]
- [[cabletron-systems|Cabletron Systems]]
- [[hp|Hewlett-Packard Company]]
- [[ibm|IBM]]
- [[netlink-inc|Netlink, Inc.]]

## Technologies (6)

- [[atm-networking|ATM (Asynchronous Transfer Mode)]]
- [[frad|Frame Relay Access Device (FRAD)]]
- [[frame-relay|Frame Relay]]
- [[intel-i960|Intel i960 RISC Microprocessor]]
- [[omnilinx-8000|OmniLinx 8000]]
- [[sna|IBM SNA (Systems Network Architecture)]]

## Key observations (top 25)

- **1996** — Product Strategy: Single consistent FRAD product line for enterprise data interconnect; TurboFRAD (branch), OmniFRAD (hub), NetFRAD (carrier); Matrix VC switching architecture
- **1996** — SNA Overhead: FRAD vs Router: RFC 1490 FRAD: 9 bytes/frame; TCP/IP SDLC encapsulation (router): 70 bytes; DLS (router): 50 bytes. Routers consume 50%+ of SNA frame at peak loading.
- **1996** — Customer ROI Timeline: Payback in 12-18 months; some customers in less than 12 months; driven by 20-25% reduction in leased-line costs plus MIS labor and network licensing savings
- **1996** — User Scalability Improvement: One customer moved from 'maybe 5 users' with prior FRAD to 10x increase using OmniFRAD RISC architecture
- **1996** — TurboFRAD Specifications: Standard 4 ports; max 8 ports; routes IP/IPX; RFC 1490; flash storage; 1 Ethernet or Token Ring LAN
- **1996** — OmniFRAD Specifications: Standard 4 ports; max 64 ports; routes IP/IPX; RFC 1490; hard drive storage; 2 Ethernet or Token Ring LAN; hub for star network
- **1996** — NetFRAD Specifications: Standard 2 T-1 or 4 serial; max 22 T-1 or 96 serial; carrier solution; 2 hard drives; 2 Ethernet and/or Token Ring
- **1996** — Frame Relay Market Growth: Rapidly growing service since 1991 offerings; IXCs dominate segment; RBOCs gaining foothold; frame relay eroding portion of leased-lines market
- **1996** — Frame Relay / ATM Migration Prediction: Aberdeen predicts ATM will appear first as backbone transmission fed by frame relay 'edge network'; frame relay will NOT be displaced by ATM
- **2005** — Frame Relay / ATM Migration Actual Outcome: ATM was deployed as backbone in telco networks while frame relay persisted as edge access through early 2000s; both eventually superseded by MPLS/IP, not one replacing the other as Aberdeen predicted
- **1996** — Netlink FRAD Market Viability: Aberdeen believes Netlink FRADs represent a sound investment decision with robust data services market continuing into next century; Matrix VC provides smooth transition to future capabilities
- **1996** — Netlink Actual Outcome: Netlink acquired by Cabletron Systems for ~$158-160M in stock in September 1996 — same month as this profile; Cabletron subsequently dissolved into 4 entities by 2001; frame relay products eventually discontinued
- **1996** — SafeLinx SNA Priority Management: Only FRADs using all available bandwidth of frame relay line; local SNA acknowledgment reduces WAN load; transparent backup reroutes around network failures
- **1996** — FRAD vs Router for SNA Environments: Enterprises with SNA traffic >40% or performance-sensitive SNA will benefit greatly from FRADs over routers; routers far less efficient at SNA traffic handling
- **1996** — Frame Relay vs X.25 Architecture: Frame relay evolved from X.25 digital packet switching; eliminated X.25 error correction/flow overhead in network layer; error correction delegated to end-user device (FRAD/router)
- **1996** — OmniLinx 8000 Edge Switch: Private/hybrid frame relay edge switch with backbone switch capabilities plus multiprotocol FRAD and routing functions; SNMP-managed via OmniView on HP OpenView
- **1996** — IBM Service Agreement with Netlink: IBM and Netlink have nationwide service agreement enabling quick response for SNA network customers; Anixter as global SI partner
- **1996** — ATM Competitive Position vs Frame Relay: Cell-relay ATM for high-throughput T3+ real-time apps being developed to integrate with frame relay base; ATM targets integrated voice/video/data

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-frame-relay-access-devices' ORDER BY year_observed;
```

