---
title: "Hewlett-Packard's Praesidium: A Family of Products To make Business on the Net A Reality"
slug: aberdeen-1996-hp-praesidium-family
page_type: study
author: "Aberdeen Group"
date: "1996-09-09"
study_type: market-study
subject_domain: "Internet-security-electronic-commerce"
methodology: "industry-analysis, competitive-profiling, document-review"
importance: high
importance_rationale: "One of the earliest detailed assessments of a comprehensive enterprise Internet security framework at the dawn of commercial e-commerce; addressed foundational security architecture problems that defined the next decade of IT security practice."
relevance: medium
relevance_rationale: "The security framework concepts (authentication, authorization separation, trusted gateway, role-based access) remain foundational to modern security architecture; specific HP products are obsolete but the threat model and architectural patterns transfer directly to Zero Trust and IAM frameworks."
prescience: high
prescience_rationale: "Aberdeen's predictions that enterprise security would require integrated frameworks rather than point solutions, and that role-based authorization would displace access control lists, proved highly accurate — both are now standard security architecture principles."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 8
obs_count: 20
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Hewlett-Packard's Praesidium: A Family of Products To make Business on the Net A Reality

> This Aberdeen Group profile, dated September 9, 1996, evaluates Hewlett-Packard's Praesidium security framework for enterprise Internet and Intranet transaction security. The study examines HP's VirtualVault trusted gateway, Praesidium Authorization Server, ImagineCard smart card authentication, and the International Cryptography Framework (ICF), positioning them as a comprehensive solution for moving enterprises from pilot electronic commerce projects to production-grade deployments.

**Author:** Aberdeen Group · **Date:** 1996-09-09 · **Type:** market-study
**Importance:** high — *One of the earliest detailed assessments of a comprehensive enterprise Internet security framework at the dawn of commercial e-commerce; addressed foundational security architecture problems that defined the next decade of IT security practice.*
**Prescience:** high — *Aberdeen's predictions that enterprise security would require integrated frameworks rather than point solutions, and that role-based authorization would displace access control lists, proved highly accurate — both are now standard security architecture principles.*

## Entities (10)

- [[aberdeen-group|Aberdeen Group, Inc.]]
- [[axent-technologies|Axent Technologies]]
- [[checkpoint-software|Check Point Software Technologies]]
- [[gemplus|Gemplus International]]
- [[hewlett-packard|Hewlett-Packard Company]]
- [[informix|Informix Software]]
- [[netscape|Netscape Communications]]
- [[nortel|Nortel Networks]]
- [[oracle|Oracle Corporation]]
- [[verifone|VeriFone Systems]]

## Technologies (8)

- [[authorization-server|HP Praesidium Authorization Server]]
- [[hp-openview|HP OpenView]]
- [[hp-praesidium|HP Praesidium Security Framework]]
- [[imaginecard|ImagineCard Smart Card]]
- [[international-cryptography-framework|International Cryptography Framework (ICF)]]
- [[set-protocol|Secure Electronic Transfer (SET)]]
- [[virtualvault|HP Praesidium VirtualVault]]
- [[x509-certificates|X.509 Digital Certificates]]

## Key observations (top 25)

- **1996** — Praesidium Framework Strategy: Modular yet integrated security framework: VirtualVault (trusted gateway) + Authorization Server (business-logic) + ICF (crypto framework) + ImagineCard (authentication); business-logic-driven vs mechanical ACL approach
- **1996** — VirtualVault Trust Model: B1 class SecureWare; protected reference monitor isolates web-server from Intranet resources; roles-based admin eliminating superuser; real-time audit log monitoring; already deployed by Federal banks for Internet banking
- **1996** — Authorization Server Architecture: Role-and-rules-based authorization separating identity/authorization from back-end; authorized access by app/app-server/location/time-of-day/day-of-week/roles; secured replication for HA
- **1996** — ICF Purpose and Design: Designed to resolve national encryption export control impasse; enables enterprises to use politically-approved crypto per political boundary; HP-proposed open standard
- **1996** — E-Commerce Enterprise Status: IS executives testing small-scale pilot projects between trading partners; point-solutions found inadequate; internal-commerce-networks physically disconnected from corporate network for security
- **1996** — Integrated Security Framework vs Point Solutions: Aberdeen concludes point-solutions will not work for production-grade enterprise e-commerce; integrated framework required; Praesidium approach will prevail
- **2005** — Integrated Security Framework vs Point Solutions Outcome: Prediction verified: enterprise security market consolidated around integrated frameworks; HP Praesidium products were discontinued but the framework concept prevailed — IAM platforms (RSA, IBM Tivoli, Microsoft IAM) and unified security suites becam…
- **1996** — Role-Based Access Control (RBAC) vs ACL Prediction: Aberdeen predicts role-and-rules-based authorization will replace mechanical ACL-based security controls; transforming mechanical controls into business-logic
- **2004** — RBAC vs ACL Adoption Actual Outcome: RBAC became the dominant enterprise authorization model; NIST RBAC standard published 2004; RBAC is now the industry standard for enterprise IAM, supplanting traditional ACLs as Aberdeen predicted
- **1996** — SET Protocol Adoption: Praesidium plans to integrate with SET for credit card transactions; SET and X.509 cited as key authentication standards to support
- **2001** — SET Protocol Actual Outcome: SET protocol was abandoned by 2001; SSL/TLS became the universal payment security standard instead; 3D Secure replaced SET. Aberdeen's implicit preference for flexible crypto frameworks was correct but SET itself failed.
- **1996** — ImagineCard Universal Authentication Prediction: ImagineCard may provide features needed for universal adoption as a multi-credential smart card for enterprise and consumer authentication
- **2000** — ImagineCard Actual Outcome: ImagineCard did not achieve universal adoption; smart card adoption in enterprise remained limited until PKI/FIDO standards era; consumer smart card payments (EMV chip) achieved mainstream adoption but through Visa/Mastercard not HP framework
- **1996** — Certificate Authority Cost Reduction: Praesidium could reduce or eliminate $300,000 up-front cost to establish account with third-party CA; enterprises with large transaction volumes can run own secured back-end operations
- **1996** — Aberdeen Security Framework Verdict: HP Praesidium could do for commercial cyber-transactions what vaults did for banks; provides tools for IS executives to secure Intranet and conduct Internet commerce
- **1996** — Praesidium as OpenView Security Analog: Praesidium framework intentionally modeled on HP OpenView's successful network management framework approach; ISV partner recruitment strategy parallels OpenView ecosystem development
- **1996** — Security Factor: Authentication (Front-End): Credentials: passwords, smart cards, X.509 certificates, biometrics; ImagineCard for multi-credential; HP integrating diverse credential types including SET and public-key systems
- **1996** — Security Factor: Cryptography/Transport (ICF): ICF resolves national encryption export control impasse; enables per-country crypto policy; protects credentials and message traffic in transit over wire and wireless networks
- **1996** — Security Factor: Trusted Gateway (VirtualVault): B1-class trusted gateway isolating web apps from Intranet; roles-based admin; real-time audit; goes beyond firewall protection; shields against internal threats and external
- **1996** — Security Factor: Authorization (Business-Logic): Role-and-rules authorization separating identity from back-end; access by app/server/location/time/roles; HA replication; transforms mechanical ACLs into flexible business-logic

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-hp-praesidium-family' ORDER BY year_observed;
```

