---
title: "NC Server White Paper -- DRAFT"
slug: netcompute-e6c378
page_type: study
author: "Network Computer, Inc. (NCI) / Aberdeen Group"
date: "1997-01-01"
study_type: white-paper
subject_domain: "network-computing"
methodology: "product-specification, industry-analysis"
importance: high
importance_rationale: "Captures the thin-client/network computing wave of the late 1990s; documents NCI's Oracle-backed NC Server architecture that competed against Microsoft and Intel's dominance."
relevance: medium
relevance_rationale: "The network computing paradigm re-emerged as cloud computing and Chromebooks; the architectural concepts (server-side processing, thin clients) are foundational to current cloud computing."
prescience: medium
prescience_rationale: "NCI's NC Server concept correctly anticipated the direction of cloud/SaaS but failed in the late-1990s market; the thin-client model ultimately succeeded through different vectors (smartphones, Chromebooks, cloud)."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 17
obs_count: 20
tags: [type/study, importance/high, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# NC Server White Paper -- DRAFT

> This draft white paper describes the NC Server from Network Computer, Inc. (NCI), a platform enabling network computing via a three-tier architecture of OS substrate, required system services, and NC applications. The document details NC components including initialization (BOOTP/DHCP), authentication (smart card), file system (NFS), print services, and applications (Oracle-based productivity tools, web server, mail, billing). The NC Server is positioned as a low-cost, centrally managed alternative to desktop PCs.

**Author:** Network Computer, Inc. (NCI) / Aberdeen Group · **Date:** 1997-01-01 · **Type:** white-paper
**Importance:** high — *Captures the thin-client/network computing wave of the late 1990s; documents NCI's Oracle-backed NC Server architecture that competed against Microsoft and Intel's dominance.*
**Prescience:** medium — *NCI's NC Server concept correctly anticipated the direction of cloud/SaaS but failed in the late-1990s market; the thin-client model ultimately succeeded through different vectors (smartphones, Chromebooks, cloud).*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[network-computer-inc|Network Computer, Inc. (NCI)]]
- [[open-group|The Open Group]]
- [[oracle|Oracle Corporation]]
- [[sun-microsystems|Sun Microsystems]]

## Technologies (17)

- [[bootp|BOOTP (Boot Protocol)]]
- [[dhcp|DHCP (Dynamic Host Configuration Protocol)]]
- [[ldap|LDAP (Lightweight Directory Access Protocol)]]
- [[microsoft-windows-nt|Microsoft Windows NT]]
- [[nc-card|NC Card (Smart Card)]]
- [[nc-server|NC Server]]
- [[nfs|NFS (Network File System)]]
- [[oracle-context|Oracle Context (Language Processing Engine)]]
- [[oracle-enterprise-manager|Oracle Enterprise Manager]]
- [[oracle-financial-apps|Oracle Financial Application Suite]]
- [[oracle-interoffice|Oracle InterOffice]]
- [[oracle-java-hatrick|Oracle Java Productivity Suite (Hatrick)]]
- [[oracle-web-server|Oracle Web Server]]
- [[sun-solaris|Sun Solaris]]
- [[surfwatch|Surfwatch Web Filter]]
- [[unix|UNIX (various)]]
- [[vpn|Virtual Private Networks (VPN)]]

## Key observations (top 25)

- **1997** — NC Server architecture tiers: Three-tier: NC OS Substrate + NC Required System Services + NC Applications
- **1997** — NC Server OS Substrate options: DEC Unix, HP/UX 10, IBM AIX, Sun SPARC Solaris, Windows NT; plus low-cost NCI-branded substrate
- **1997** — NC Initialization protocol (initial): BOOTP-based; provides IP address and software images to NC Clients
- **1997** — NC Initialization protocol (future): DHCP -- more flexible IP allocation; important scalability for large deployments
- **1997** — NC Authentication mechanism: Smart card (NC Card) + password/PIN; higher security than magnetic stripe; enables VPN
- **1997** — NC Authorization standard: Based on LDAP; models user/resource mappings; supports charging for resource access
- **1997** — NC File System implementation: Based on Sun NFS; centralized file storage (NC clients have no local storage)
- **1997** — NC Productivity Applications: Oracle Java-based suite 'Hatrick': word processor, spreadsheet, slide-show; integrates with Oracle InterOffice
- **1997** — NC Web Server basis: Value-added implementation of Oracle Web Server; supports NC Required Services and NC Childsafe
- **1997** — NC Mail system: Based on Oracle InterOffice; includes gateways to popular mail environments, POP3 support
- **1997** — NC Server scalability claim: Key values: low cost of operation, security, scalability to accommodate several thousands of users
- **1997** — NC Server backward compatibility: NC Server will be backward compatible with NC Clients for maximum period of four years
- **2001** — NC Server/NCI survival: unknown
- **1997** — NC Server Manager basis: Web-based management tools based on Oracle Enterprise Manager; single-transaction user provisioning
- **1997** — NC Server market positioning: Low-cost centrally administered alternative to traditional PC infrastructure; targets SOHO, Education, Community, Enterprise
- **1997** — NC Childsafe initial implementation: Integrates with Surfwatch web content filter; future: Oracle Context language processing for dynamic filtering
- **1997** — NC Application Manager licensing model: Pay-per-use or license software via NC Application Manager; integrates with Oracle Enterprise Manager and NC Authorization
- **1997** — NC Billing and Accounting integration: Integrates with Oracle Financial Application Suite for complete business support solution
- **1997** — Network computing paradigm adoption: Network computing is next step in evolution of computing; everything stored on network
- **2005** — Network computing thin-client adoption actual: unknown

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'netcompute-e6c378' ORDER BY year_observed;
```

