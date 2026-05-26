---
title: "NC Server White Paper -- DRAFT"
slug: "study-netcompute-e6c378"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "netcompute-e6c378"
author: "Network Computer, Inc. (NCI) / Aberdeen Group"
date: "1997-01-01"
pub_year: 1997
type: "white-paper"
subject_domain: "network-computing"
methodology: "product-specification, industry-analysis"
source_file: "NetCompute.docx"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# NC Server White Paper -- DRAFT

> This draft white paper describes the NC Server from Network Computer, Inc. (NCI), a platform enabling network computing via a three-tier architecture of OS substrate, required system services, and NC applications. The document details NC components including initialization (BOOTP/DHCP), authentication (smart card), file system (NFS), print services, and applications (Oracle-based productivity tools, web server, mail, billing). The NC Server is positioned as a low-cost, centrally managed alternative to desktop PCs.


_Published 1997, author **Network Computer, Inc. (NCI) / Aberdeen Group**, type **white-paper**._


## Top observations

- Three-tier: NC OS Substrate + NC Required System Services + NC Applications
- DEC Unix, HP/UX 10, IBM AIX, Sun SPARC Solaris, Windows NT; plus low-cost NCI-branded substrate
- BOOTP-based; provides IP address and software images to NC Clients
- DHCP -- more flexible IP allocation; important scalability for large deployments
- Smart card (NC Card) + password/PIN; higher security than magnetic stripe; enables VPN
- Based on LDAP; models user/resource mappings; supports charging for resource access
- Based on Sun NFS; centralized file storage (NC clients have no local storage)
- Oracle Java-based suite 'Hatrick': word processor, spreadsheet, slide-show; integrates with Oracle InterOffice
- Value-added implementation of Oracle Web Server; supports NC Required Services and NC Childsafe
- Based on Oracle InterOffice; includes gateways to popular mail environments, POP3 support
- Key values: low cost of operation, security, scalability to accommodate several thousands of users
- NC Server will be backward compatible with NC Clients for maximum period of four years
- unknown
- Web-based management tools based on Oracle Enterprise Manager; single-transaction user provisioning
- Low-cost centrally administered alternative to traditional PC infrastructure; targets SOHO, Education, Community, Enterprise
- Integrates with Surfwatch web content filter; future: Oracle Context language processing for dynamic filtering
- Pay-per-use or license software via NC Application Manager; integrates with Oracle Enterprise Manager and NC Authorization
- Integrates with Oracle Financial Application Suite for complete business support solution
- Network computing is next step in evolution of computing; everything stored on network
- unknown
