---
title: "TME 10 Security Management: Mainframe-class Security for Enterprise Network Computing"
slug: 1997-tme-10-security-management-8178c6
page_type: study
author: "Aberdeen Group"
date: "1997-02-01"
study_type: white-paper
subject_domain: "enterprise-security-management"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
importance: high
importance_rationale: "Among the first independent analyst assessments of centralized enterprise security management for heterogeneous networks; Tivoli was the dominant vendor in this space and this profile directly influenced enterprise purchasing decisions for network security infrastructure."
relevance: medium
relevance_rationale: "Role-based access control (RBAC), centralized policy enforcement, and cross-platform security management principles articulated in this study remain foundational to modern identity and access management (IAM) and zero-trust security frameworks, though specific products are obsolete."
prescience: high
prescience_rationale: "Aberdeen correctly predicted TME 10 SM would become a cornerstone enterprise security product; Tivoli was acquired by IBM for $743M in 1996 and TME 10 evolved into IBM Tivoli Identity Manager and subsequently IBM Security Verify, remaining active through 2020s under IBM's portfolio."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 10
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# TME 10 Security Management: Mainframe-class Security for Enterprise Network Computing

> Aberdeen Group profiles Tivoli's TME 10 Security Management product, positioning it as the first solution to bring mainframe-class security (RACF/ACF2-style) to distributed enterprise networks spanning Unix, Windows NT, Novell NetWare, and OS/390. The study documents IS executive frustrations with fragmented, platform-specific security tools and concludes that TME 10 SM fills a critical gap in Tivoli's product portfolio. Aberdeen recommends IS executives evaluate the product immediately as it resolves the longstanding challenge of consistent enterprise security policy enforcement across heterogeneous platforms.

**Author:** Aberdeen Group · **Date:** 1997-02-01 · **Type:** white-paper
**Importance:** high — *Among the first independent analyst assessments of centralized enterprise security management for heterogeneous networks; Tivoli was the dominant vendor in this space and this profile directly influenced enterprise purchasing decisions for network security infrastructure.*
**Prescience:** high — *Aberdeen correctly predicted TME 10 SM would become a cornerstone enterprise security product; Tivoli was acquired by IBM for $743M in 1996 and TME 10 evolved into IBM Tivoli Identity Manager and subsequently IBM Security Verify, remaining active through 2020s under IBM's portfolio.*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[axent|Axent Technologies]]
- [[checkpoint-software|Check Point Software Technologies]]
- [[cybersafe|CyberSafe Corporation]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[iss|Internet Security Systems]]
- [[microsoft|Microsoft Corporation]]
- [[novell|Novell Inc.]]
- [[sun-microsystems|Sun Microsystems]]
- [[tivoli-systems|Tivoli Systems Inc.]]
- [[trusted-information-systems|Trusted Information Systems]]

## Technologies (10)

- [[acf2|CA ACF2]]
- [[dce|Distributed Computing Environment (DCE)]]
- [[kerberos|Kerberos Authentication Protocol]]
- [[netware|Novell NetWare]]
- [[os390|IBM OS/390]]
- [[racf|IBM RACF (Resource Access Control Facility)]]
- [[tacf|Tivoli Access Control Facility (TACF)]]
- [[tme-10|Tivoli Management Environment (TME)]]
- [[tme-10-sm|TME 10 Security Management]]
- [[windows-nt|Windows NT Server]]

## Key observations (top 25)

- **1997** — Tivoli competitive position pre-TME 10 SM: Tivoli had competitive disadvantage because it could not deliver production-grade security services that competitors already provided
- **1997** — Portfolio gap filled by TME 10 SM: TME 10 SM fills a glaring void in Tivoli's product portfolio by adding enterprise-class security management
- **1997** — Platform coverage breadth: Supports HP-UX/RISC; IBM OS/390-RACF and AIX/RISC; Windows NT Server/Intel; Novell NetWare; SunOS and Solaris/RISC — via TME v3.1+
- **1997** — Security architecture approach: Role-based access control (RBAC) using system-independent security profile-records distributed over network; non-intrusive installation without taking servers down
- **1997** — IS security pain point 1: Solutions too complicated and brittle (DCE/Kerberos/Sesame) requiring expensive integration
- **1997** — IS security pain point 2: Solutions non-interoperable placing additional burden on IS budget and deployment schedules
- **1997** — IS security pain point 3: Solutions technology-focused instead of organizational and business-process focused
- **1997** — IS security pain point 4: Most solutions limited to protecting one operating environment (NetWare-only / Unix-only / NT-only / OS/390-only) requiring separate admin per platform
- **1997** — Authentication methods supported: Passwords (default); DCE and Kerberos for admin roles; time-of-day/day-of-week login restrictions; location-based login restrictions; password quality enforcement
- **1997** — RBAC architecture elements: Four-element RBAC: system-wide policies; group authorizations; role authorizations; IT resources — all managed centrally via security profile-records
- **1997** — Architecture scalability mechanism: Security profile-records pushed to subscribing nodes enabling local operation with central management; TACF for Unix partitions root account privileges to prevent compromise
- **1997** — Tivoli ISV partnership strategy: Partner Exchange (TPE) program with 12+ security ISV partners to integrate point solutions: Axent; Cybersafe; Checkpoint Software; Cygnus; Dynasoft; Haystack Labs; IBM; ICL; ISS; Mergent; Memco; Trusted Information Systems
- **1997** — Future platform expansion roadmap: Plans to add ACF2/TOP SECRET on mainframe; Oracle/Informix/Sybase databases; OS/2; DCE; web servers; smart card/public-key authentication; SSO; secure commerce
- **1997** — TME 10 SM strategic longevity: TME 10 SM will serve as cornerstone for integrating security components; IS decision makers can depend on it for managing security through IT transitions
- **2002** — TME 10 SM product evolution: IBM evolved TME 10 into IBM Tivoli Identity Manager (2001) and later IBM Security Identity Manager; Tivoli brand phased out 2013; technology survived as IBM Security Verify
- **1996** — Tivoli Systems IBM acquisition: Tivoli Systems acquired by IBM for $743M in 1996 before this study was published; study written under IBM ownership
- **1997** — RACF as gold standard for security: RACF described as proven mainframe security; enterprise desire is RACF-equivalent for distributed computing
- **1997** — Novell NetWare security limitations: NetWare security limited to NetWare-only platforms; incompatible with other enterprise systems
- **1997** — Aberdeen recommendation strength: Aberdeen recommends IS executives 'run — not walk — to evaluate the TME 10 Security Management solution'
- **1997** — DCE/Kerberos deployment complexity: DCE and Kerberos described as complicated and brittle security protocols requiring expensive lengthy in-house integration

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-tme-10-security-management-8178c6' ORDER BY year_observed;
```

