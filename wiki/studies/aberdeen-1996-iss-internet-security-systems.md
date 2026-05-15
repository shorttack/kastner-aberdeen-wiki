---
title: "ISS: The Foundation for Network Security"
slug: aberdeen-1996-iss-internet-security-systems
page_type: study
author: "Aberdeen Group"
date: "1996-10-01"
study_type: market-study
subject_domain: "network-security"
methodology: "industry-analysis, competitive-profiling, field-research"
importance: high
importance_rationale: "Published in 1996 at the critical juncture of commercial internet adoption, when enterprise network security was transitioning from physical perimeter defense to vulnerability assessment and continuous monitoring. Aberdeen's documentation of ISS SAFEsuite marked an important milestone in the formalization of network security assessment as an enterprise discipline."
relevance: high
relevance_rationale: "The core concepts Aberdeen identified—vulnerability scanning, prioritized risk analysis, continuous monitoring, intrusion detection—remain foundational to modern cybersecurity. ISS's approach directly influenced the entire vulnerability management and SIEM categories that dominate enterprise security spending today."
prescience: high
prescience_rationale: "Aberdeen's prediction that network security assessment would become critical enterprise infrastructure proved highly accurate. ISS was acquired by IBM for $1.93B in 2006, validating the platform's strategic value. Aberdeen's warning that electronic commerce without security assessment was reckless proved prescient given subsequent attack history."
license: CC-BY-4.0
tier: 1
entity_count: 8
tech_count: 7
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# ISS: The Foundation for Network Security

> Aberdeen Group profiles Internet Security Systems (ISS) and its SAFEsuite product family, which identifies, measures, analyzes, and prioritizes security risks in networked computing environments. The study covers ISS's scanning/analysis technology, products including Intranet Scanner, Firewall Scanner, Web Security Scanner, System Security Scanner, and RealSecure intrusion monitoring. Aberdeen recommends IS organizations building web-based e-commerce applications evaluate SAFEsuite as the foundation for a comprehensive enterprise security program.

**Author:** Aberdeen Group · **Date:** 1996-10-01 · **Type:** market-study
**Importance:** high — *Published in 1996 at the critical juncture of commercial internet adoption, when enterprise network security was transitioning from physical perimeter defense to vulnerability assessment and continuous monitoring. Aberdeen's documentation of ISS SAFEsuite marked an important milestone in the formali…*
**Prescience:** high — *Aberdeen's prediction that network security assessment would become critical enterprise infrastructure proved highly accurate. ISS was acquired by IBM for $1.93B in 2006, validating the platform's strategic value. Aberdeen's warning that electronic commerce without security assessment was reckless p…*

## Entities (8)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[bellcore|Bellcore (Bell Communications Research)]]
- [[ernst-young|Ernst & Young]]
- [[ibm|IBM Corporation]]
- [[internet-security-systems|Internet Security Systems (ISS)]]
- [[ncsa-national-computer-security|National Computer Security Association (NCSA)]]
- [[price-waterhouse|Price Waterhouse]]
- [[qualix-group|Qualix Group]]

## Technologies (7)

- [[firewall-technology|Firewall Technology]]
- [[realsecure|RealSecure]]
- [[safesuite|ISS SAFEsuite]]
- [[satan|SATAN (Security Administrators Tool for Analyzing Networks)]]
- [[tcp-ip|TCP/IP Protocol]]
- [[vpn|Virtual Private Networks (VPN)]]
- [[windows-nt-security|Windows NT Security Architecture]]

## Key observations (top 25)

- **1996** — ISS Market Strategy: Commercial packaged security scanner vs SATAN's free Unix-based approach; ready-to-install; no Unix expertise required
- **1996** — SAFEsuite Network Coverage: Covers all Unix platforms, Windows NT, AS/400, S/390, PC clients, routers, all firewalls, web servers, modems, printers, storage—any IP-connected device
- **1996** — NCSA Firewall Certification Role: NCSA uses ISS Firewall Scanner as core part of its firewall accreditation program certifying independently-developed firewall products
- **1996** — Cybersecurity Insurance Market Emergence: NCSA certification programs led insurance carriers to underwrite liability coverage for NCSA-certified web sites
- **1996** — ISS Distribution Network: More than 130 distributors worldwide; partnerships with Ernst & Young, Price Waterhouse, Raptor, Trusted Information Systems
- **1996** — SAFEsuite Operating Platform Support: Operates on Windows NT, HP-UX, IBM AIX, SunOS, Solaris, Intel Linux
- **1996** — Windows NT Network Security Gap: NT security policies are not enforced across the network; Microsoft removed security controls available in NT 3.50 from 3.51 and 4.0
- **1996** — Network Security Egg Metaphor: For experienced IS managers, networked application security appears like an egg—hard on the outside and soft on the inside; correctly configured externally but internally vulnerable
- **1996** — Firewall Limitation Recognition: Incorrectly configured routers, web servers, applications, operating environments, modems on internal sub-networks can shatter protective safeguards without warning
- **1996** — ISS Technology Leadership Position: ISS's technology appears to be leading the industry; continuously developing new capabilities; security is ongoing arms race
- **2006** — ISS Technology Leadership - Outcome: IBM acquired ISS for $1.93B in October 2006, confirming technology leadership and strategic value; ISS integrated into IBM Security Systems Division
- **1996** — Network Security Assessment as Enterprise Requirement: Aberdeen recommends IS organizations building web-based e-commerce applications evaluate SAFEsuite as foundation for comprehensive security program
- **2010** — Network Security Assessment as Enterprise Requirement - Outcome: Vulnerability management and security assessment became standard enterprise security practice; SIEM, vulnerability scanners, penetration testing became multi-billion dollar markets
- **1996** — SAFEsuite vs NetProbe vs PingWare Comparison: SAFEsuite comparable to competitors in ease of use/install/configure; outshines with more comprehensive vulnerability coverage, prioritized risk analysis, and update frequency
- **1996** — RealSecure Intrusion Detection Capability: Real-time intrusion monitoring; monitors packet flow; recognizes attack patterns; responds from email notification to connection termination
- **1996** — Internet-Time Security Vulnerability: Internet suppliers release products with 3-month cycles; quality suffers; security closely related to quality; Web-enabled applications are inherently vulnerable
- **1996** — ISS Enterprise Customer Base: Customers include AMP, Chevron, Department of Energy, First Union, Intel, IBM, JC Penney, Lockheed-Martin, MCI, Merck, Motorola, NASA, the Pentagon, Texas Instruments
- **1996** — ISS Corporate Structure: Privately held, venture-capital backed; does not release financial results at time of study
- **1996** — TCP/IP as Universal Security Attack Surface: TCP/IP has become the common alphabet of the modern information age; backbone for Internet, Intranet, remote access; also universal attack vector
- **1996** — Security Spending Without Assessment: Spending IS budget on security controls without understanding vulnerabilities or continuously monitoring is blindly throwing money away

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-iss-internet-security-systems' ORDER BY year_observed;
```

