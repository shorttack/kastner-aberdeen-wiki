---
title: "IBM Network Computing: Enterprise Communications Family"
slug: 1997-ibm-s-enterprise-communications-fam-14559a
page_type: study
author: "Aberdeen Group"
date: "1997-06-01"
study_type: profile
subject_domain: "Enterprise Networking / Communications Software"
methodology: "vendor-briefing,product-evaluation,user-interviews"
importance: low
importance_rationale: "Represents a transitional moment in IBM's networking stack — the strategic pivot from SNA-centric to TCP/IP-aware multiprotocol architectures. Important as a primary source on the SNA deprecation trajectory and AnyNet/MPTN technology decisions."
relevance: low
relevance_rationale: "Directly relevant to the history of enterprise networking transitions from SNA to TCP/IP. Documents IBM's technical strategy at a critical juncture and provides benchmark context for evaluating communications middleware choices of the era."
prescience: medium
prescience_rationale: "Aberdeen accurately predicted that TCP/IP would displace SNA; that multiprotocol bridging would be a transitional strategy; that HPR dynamic routing features anticipate modern SDN concepts; and that ATM would not displace TCP/IP long-term. The call to place ECF 'high on lists to buy' was overstated — SNA was sunset by IBM within a decade."
license: CC-BY-4.0
tier: 2
entity_count: 5
tech_count: 8
obs_count: 18
tags: [type/study, importance/low, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# IBM Network Computing: Enterprise Communications Family

> Aberdeen Group evaluates IBM's Enterprise Communications Family, a suite of communications software for enterprise network computing. The study assesses IBM's advanced multiprotocol support (AnyNet/MPTN) and High Performance Routing (HPR) technologies, covering products including Communications Server (CS/2, CS/NT, CS/AIX, OS/400, CS/MVS) and Personal Communications. Aberdeen concludes that IBM's approach delivers scalability, flexibility, and ease of SNA-to-TCP/IP migration for enterprises transitioning to network computing architectures.

**Author:** Aberdeen Group · **Date:** 1997-06-01 · **Type:** profile
**Importance:** low — *Represents a transitional moment in IBM's networking stack — the strategic pivot from SNA-centric to TCP/IP-aware multiprotocol architectures. Important as a primary source on the SNA deprecation trajectory and AnyNet/MPTN technology decisions.*
**Prescience:** medium — *Aberdeen accurately predicted that TCP/IP would displace SNA; that multiprotocol bridging would be a transitional strategy; that HPR dynamic routing features anticipate modern SDN concepts; and that ATM would not displace TCP/IP long-term. The call to place ECF 'high on lists to buy' was overstated…*

## Entities (5)

- [[ENT-S1-001|IBM Corporation]]
- [[ENT-S1-002|IBM Communications Server]]
- [[ENT-S1-003|IBM Personal Communications]]
- [[ENT-S1-004|Novell NetWare for SAA]]
- [[ENT-S1-005|Aberdeen Group]]

## Technologies (8)

- [[TECH-S1-001|SNA (Systems Network Architecture)]]
- [[TECH-S1-002|TCP/IP]]
- [[TECH-S1-003|AnyNet / MPTN (Multiprotocol Transport Networking)]]
- [[TECH-S1-004|High Performance Routing (HPR)]]
- [[TECH-S1-005|ATM (Asynchronous Transfer Mode)]]
- [[TECH-S1-006|Frame Relay]]
- [[TECH-S1-007|TN3270E]]
- [[TECH-S1-008|APPN (Advanced Peer-to-Peer Networking)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-ibm-s-enterprise-communications-fam-14559a' ORDER BY year_observed;
```

