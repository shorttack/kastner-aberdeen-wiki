---
title: "Directory to the Network"
slug: 1997-novell-directory-to-the-network-str-048b05
page_type: study
author: "Aberdeen Group"
date: "1997-06-01"
study_type: Strategic Profile
subject_domain: "Network Infrastructure / Directory Services"
methodology: "Analyst interviews with IS and LOB executives; product evaluation; competitive analysis"
importance: medium
importance_rationale: "Captures a critical inflection point in enterprise networking: the battle between NDS and Microsoft's future Active Directory for directory-services dominance. NDS was technically superior but ultimately lost to Active Directory bundled with Windows 2000 — an outcome that reshaped enterprise IT for decades."
relevance: medium
relevance_rationale: "Directly relevant to modern identity and access management (IAM), LDAP, and directory-services architecture. The NDS vs. Active Directory contest prefigures today's debates about directory consolidation, hybrid identity, and Zero Trust."
prescience: medium
prescience_rationale: "Aberdeen's prediction that NDS would become the de facto enterprise directory standard proved incorrect — Microsoft's Active Directory, shipped with Windows 2000 in 2000, ultimately dominated. However, Aberdeen's insistence on a single hierarchical LDAP-based enterprise directory proved highly prescient, as did warnings about the IS/LOB gap, the necessity of LDAP standards, and the strategic importance of directory services to e-commerce and VPN deployments."
license: CC-BY-4.0
tier: 2
entity_count: 12
tech_count: 12
obs_count: 20
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Directory to the Network

> Examines Novell's strategy for Novell Directory Services (NDS) as the company seeks to position NDS as the de facto enterprise meta-directory standard. Reviews NDS's extensibility, scalability, portability, and availability attributes; its cross-platform porting to NT and Unix; Java strategy; and related products IntranetWare, ManageWise, and GroupWise. Aberdeen concludes NDS best meets enterprise directory criteria and is ahead of Microsoft's forthcoming Active Directory.

**Author:** Aberdeen Group · **Date:** 1997-06-01 · **Type:** Strategic Profile
**Importance:** medium — *Captures a critical inflection point in enterprise networking: the battle between NDS and Microsoft's future Active Directory for directory-services dominance. NDS was technically superior but ultimately lost to Active Directory bundled with Windows 2000 — an outcome that reshaped enterprise IT for…*
**Prescience:** medium — *Aberdeen's prediction that NDS would become the de facto enterprise directory standard proved incorrect — Microsoft's Active Directory, shipped with Windows 2000 in 2000, ultimately dominated. However, Aberdeen's insistence on a single hierarchical LDAP-based enterprise directory proved highly presc…*

## Entities (12)

- [[ENT-NOV-001|Novell Inc.]]
- [[ENT-NOV-002|Microsoft Corporation]]
- [[ENT-NOV-003|Banyan Systems]]
- [[ENT-NOV-004|IBM]]
- [[ENT-NOV-005|Computer Associates (CA)]]
- [[ENT-NOV-006|Oracle Corporation]]
- [[ENT-NOV-007|SunSoft (Sun Microsystems)]]
- [[ENT-NOV-008|Caldera]]
- [[ENT-NOV-009|Hewlett-Packard]]
- [[ENT-NOV-010|AT&T]]
- [[ENT-NOV-011|Deutsche Telekom]]
- [[ENT-NOV-012|NTT]]

## Technologies (12)

- [[TECH-NOV-001|Novell Directory Services (NDS)]]
- [[TECH-NOV-002|Active Directory]]
- [[TECH-NOV-003|LDAP (Lightweight Directory Access Protocol)]]
- [[TECH-NOV-004|X.500]]
- [[TECH-NOV-005|IntranetWare]]
- [[TECH-NOV-006|NetWare]]
- [[TECH-NOV-007|GroupWise]]
- [[TECH-NOV-008|ManageWise]]
- [[TECH-NOV-009|Unicenter TNG]]
- [[TECH-NOV-010|Virtual Private Network (VPN)]]
- [[TECH-NOV-011|Novell Application Launcher]]
- [[TECH-NOV-012|StreetTalk]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-novell-directory-to-the-network-str-048b05' ORDER BY year_observed;
```

