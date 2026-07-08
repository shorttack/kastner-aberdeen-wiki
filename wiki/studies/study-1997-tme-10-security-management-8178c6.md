---
title: "TME 10 Security Management: Mainframe-class Security for Enterprise Network Computing"
slug: "study-1997-tme-10-security-management-8178c6"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "1997-tme-10-security-management-8178c6"
author: "Aberdeen Group"
date: "1997-02-01"
pub_year: 1997
type: "white-paper"
subject_domain: "enterprise-security-management"
methodology: "industry-analysis, competitive-profiling, expert-opinion"
source_file: "1997 TME 10 Security Management pr.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 4.0
prescience_mean: 2.4
prescience_obs_count: 15
---

# TME 10 Security Management: Mainframe-class Security for Enterprise Network Computing


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.70 over 20 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=3.65 over 20 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Group profiles Tivoli's TME 10 Security Management product, positioning it as the first solution to bring mainframe-class security (RACF/ACF2-style) to distributed enterprise networks spanning Unix, Windows NT, Novell NetWare, and OS/390. The study documents IS executive frustrations with fragmented, platform-specific security tools and concludes that TME 10 SM fills a critical gap in Tivoli's product portfolio. Aberdeen recommends IS executives evaluate the product immediately as it resolves the longstanding challenge of consistent enterprise security policy enforcement across heterogeneous platforms.


_Published 1997, author **Aberdeen Group**, type **white-paper**._


## Top observations

- Role-based access control (RBAC) using system-independent security profile-records distributed over network; non-intrusive installation without taking servers down `[ps=4]`
- Four-element RBAC: system-wide policies; group authorizations; role authorizations; IT resources — all managed centrally via security profile-records `[ps=4]`
- Plans to add ACF2/TOP SECRET on mainframe; Oracle/Informix/Sybase databases; OS/2; DCE; web servers; smart card/public-key authentication; SSO; secure commerce `[ps=4]`
- IBM evolved TME 10 into IBM Tivoli Identity Manager (2001) and later IBM Security Identity Manager; Tivoli brand phased out 2013; technology survived as IBM Security Verify `[ps=4]`
- RACF described as proven mainframe security; enterprise desire is RACF-equivalent for distributed computing `[ps=4]`
- TME 10 SM fills a glaring void in Tivoli's product portfolio by adding enterprise-class security management `[ps=3]`
- Solutions too complicated and brittle (DCE/Kerberos/Sesame) requiring expensive integration `[ps=3]`
- NetWare security limited to NetWare-only platforms; incompatible with other enterprise systems `[ps=3]`
- DCE and Kerberos described as complicated and brittle security protocols requiring expensive lengthy in-house integration `[ps=3]`
- Tivoli had competitive disadvantage because it could not deliver production-grade security services that competitors already provided `[ps=2]`
- TME 10 SM will serve as cornerstone for integrating security components; IS decision makers can depend on it for managing security through IT transitions `[ps=2]`
- Supports HP-UX/RISC; IBM OS/390-RACF and AIX/RISC; Windows NT Server/Intel; Novell NetWare; SunOS and Solaris/RISC — via TME v3.1+ `[ps=0]`
- Most solutions limited to protecting one operating environment (NetWare-only / Unix-only / NT-only / OS/390-only) requiring separate admin per platform `[ps=0]`
- Partner Exchange (TPE) program with 12+ security ISV partners to integrate point solutions: Axent; Cybersafe; Checkpoint Software; Cygnus; Dynasoft; Haystack Labs; IBM; ICL; ISS; Mergent; Memco; Trusted Information Systems `[ps=0]`
- Tivoli Systems acquired by IBM for $743M in 1996 before this study was published; study written under IBM ownership `[ps=0]`
- Solutions non-interoperable placing additional burden on IS budget and deployment schedules
- Solutions technology-focused instead of organizational and business-process focused
- Passwords (default); DCE and Kerberos for admin roles; time-of-day/day-of-week login restrictions; location-based login restrictions; password quality enforcement
- Security profile-records pushed to subscribing nodes enabling local operation with central management; TACF for Unix partitions root account privileges to prevent compromise
- Aberdeen recommends IS executives 'run — not walk — to evaluate the TME 10 Security Management solution'
