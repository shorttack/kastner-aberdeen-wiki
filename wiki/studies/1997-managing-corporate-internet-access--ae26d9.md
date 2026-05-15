---
title: "Managing Corporate Internet Access: A Business Priority"
slug: 1997-managing-corporate-internet-access--ae26d9
page_type: study
author: "Aberdeen Group"
date: "1997-04-01"
study_type: Executive White Paper
subject_domain: "Network Management / Bandwidth Management / Enterprise Internet Access"
methodology: "Analyst assessment; IT manager interviews; vendor briefings; market research"
importance: medium
importance_rationale: "Captures early enterprise bandwidth management challenge; Xedia validated by Lucent $246M acquisition in 1999"
relevance: medium
relevance_rationale: "Bandwidth management and QoS remain important; Frame Relay obsolete but SD-WAN and QoS concepts directly descend from this problem space"
prescience: high
prescience_rationale: "Aberdeen correctly predicted bandwidth management as critical enterprise priority; internet-centricity of business fully realized; Xedia acquisition validated assessment"
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 8
obs_count: 20
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Managing Corporate Internet Access: A Business Priority

> Aberdeen examines enterprise bandwidth management challenge and evaluates Xedia Corporation's Access Point broadband access management solution. Paper covers TCP/IP QoS limitations bandwidth allocation requirements and Xedia's Class Based Queuing and Intelligent Queuing approach at 50% below cost of competing solutions.

**Author:** Aberdeen Group · **Date:** 1997-04-01 · **Type:** Executive White Paper
**Importance:** medium — *Captures early enterprise bandwidth management challenge; Xedia validated by Lucent $246M acquisition in 1999*
**Prescience:** high — *Aberdeen correctly predicted bandwidth management as critical enterprise priority; internet-centricity of business fully realized; Xedia acquisition validated assessment*

## Entities (4)

- [[ENT-XED-001|Xedia Corporation]]
- [[ENT-XED-002|Lucent Technologies]]
- [[ENT-XED-003|Ascend Communications]]
- [[ENT-XED-004|Aberdeen Group]]

## Technologies (8)

- [[TECH-XED-001|Access Point (Xedia)]]
- [[TECH-XED-002|Class Based Queuing (CBQ)]]
- [[TECH-XED-003|Intelligent Queuing (IQ)]]
- [[TECH-XED-004|Frame Relay]]
- [[TECH-XED-005|TCP/IP]]
- [[TECH-XED-006|ATM (Asynchronous Transfer Mode)]]
- [[TECH-XED-007|MPLS (Multi-Protocol Label Switching)]]
- [[TECH-XED-008|SD-WAN (Software-Defined WAN)]]

## Key observations (top 25)

- **1997** — TCP/IP bandwidth limitation: TCP/IP cannot deliver controlled bandwidth distribution and has no ability to prioritize applications or ensure fair user access to remote resources
- **1997** — Enterprise internet access problem: IT managers face increasing pressure to guarantee users access bandwidth for business-critical applications and accurately assign bandwidth charges
- **1997** — Access Point price advantage: Xedia Access Point currently at 50% below cost of connectivity-only based solutions currently on the market
- **1997** — IQ software capabilities: Access Point's IQ software permits IT managers to establish traffic priorities and allocate bandwidth percentages; class defined by IP address range TCP/UDP ports
- **1997** — Access Point management capabilities: Web browser with Java presentation for management; ability to monitor usage of traffic classes and bandwidth; relevant as RMON probe equivalent for IT managers
- **1997** — Xedia Access Point market opportunity: Aberdeen strongly encourages IT administrators building internet into business strategy to seriously consider adding Xedia's Access Point
- **1999** — Xedia Access Point market outcome: Lucent Technologies acquired Xedia Corporation for $246 million in August 1999; strong validation of Aberdeen's positive assessment
- **1997** — Frame Relay adoption: Frame Relay cited as most widely used transmission uplink technology currently being selected by ISP customers
- **2005** — Frame Relay market decline: Frame Relay largely replaced by MPLS and broadband internet by mid-2000s; enterprise WAN market shifted to MPLS VPNs; Frame Relay revenues peaked around 2000
- **1997** — Internet-centric business strategy: Corporate access to internet must be subdivided among many users and applications and managed to ensure business efficiency and business success
- **2005** — Internet-centric business strategy: Fully validated: internet became foundation of business operations by 2000s; bandwidth management (QoS DSCP MPLS WFQ) became standard network engineering practice
- **1997** — QoS and bandwidth management tools: Network managers need hierarchical classification of flows priority and bandwidth allocation and in-depth buffering for managed internet access
- **2014** — QoS and bandwidth management tools: QoS became standard in enterprise networking through DSCP/DiffServ WFQ and MPLS QoS; SD-WAN (2014+) represents modern evolution of exactly the dynamic bandwidth allocation Aberdeen described
- **1997** — Xedia competitive strategy: Xedia uses RISC-based software architecture delivering flexibility and affordability at 50% below connectivity-only solutions with Frame Relay first then ATM support
- **2003** — ATM market outcome: ATM largely abandoned by enterprises by early 2000s as IP/Ethernet dominated; planned ATM support for Access Point became moot as ATM market collapsed
- **1997** — IT staffing vs. network complexity: Network managers frequently faced with reduced staff and budget while network grows in strategic importance
- **1997** — Access Point installation approach: Access Point can be configured at central site and shipped to enterprise site; supports OSPF2 and RIP2; compatible with installed hubs routers switches
- **1997** — Bandwidth throwing limitation: Throwing bandwidth at network problems is not always the complete solution; proper management of existing bandwidth is essential for maximum utilization
- **2016** — Lucent corporate outcome: Lucent Technologies merged with Alcatel in 2006; Nokia acquired Alcatel-Lucent in 2016; Xedia's Access Point technology was absorbed and eventually superseded by Cisco/Juniper QoS implementations
- **1997** — Aberdeen bandwidth management endorsement: Aberdeen views Class Based Queuing and Xedia's IQ approach as giant step forward in providing quality access and cost savings for internet-centric enterprise networks

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-managing-corporate-internet-access--ae26d9' ORDER BY year_observed;
```

