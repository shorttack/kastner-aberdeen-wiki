---
title: "Internet Architecture: Prescription For Success"
slug: aberdeen-1996-computer-telephony-integration
page_type: study
author: "Aberdeen Group"
date: "1996-04-17"
study_type: white-paper
subject_domain: "internet-intranet-architecture"
methodology: "industry-analysis, competitive-profiling, document-review"
importance: high
importance_rationale: "Published at the apex of the first Internet boom, this Viewpoint articulated the Intranet-first strategy at a moment of maximum enterprise confusion about Internet vs. Intranet priorities; Aberdeen's architectural framework influenced thousands of IS decisions in 1996-1997."
relevance: high
relevance_rationale: "The core architectural principles—TP-monitor-like middleware for scalability, separation of web presentation from data tiers, metadata repositories—are directly ancestral to modern microservices, API gateways, and cloud-native architectures still in use today."
prescience: high
prescience_rationale: "Aberdeen's prediction that Java would be limited near-term as a '3GL without 4GL extensions' proved accurate for 1996-1998; the Intranet-first thesis proved correct as enterprises deployed intranets before public e-commerce matured; middleware and RDBMS scalability predictions all materialized."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 8
obs_count: 23
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Internet Architecture: Prescription For Success

> Aberdeen Group prescribes an enterprise Internet/Intranet architecture for 1996, arguing that long-term value lies in the Intranet rather than public Internet. The study recommends a scalable architecture combining TP-monitor-like middleware, 64-bit VLM server hardware, parallel-scalable RDBMSs, and second-generation CADEs. Aberdeen dismisses Java as immature and warns that enterprises without proper architectural foundations will find that short-term Internet success blocks long-term success.

**Author:** Aberdeen Group · **Date:** 1996-04-17 · **Type:** white-paper
**Importance:** high — *Published at the apex of the first Internet boom, this Viewpoint articulated the Intranet-first strategy at a moment of maximum enterprise confusion about Internet vs. Intranet priorities; Aberdeen's architectural framework influenced thousands of IS decisions in 1996-1997.*
**Prescience:** high — *Aberdeen's prediction that Java would be limited near-term as a '3GL without 4GL extensions' proved accurate for 1996-1998; the Intranet-first thesis proved correct as enterprises deployed intranets before public e-commerce matured; middleware and RDBMS scalability predictions all materialized.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates International]]
- [[informix|Informix Software]]
- [[oracle-corporation|Oracle Corporation]]
- [[sequent-computer|Sequent Computer Systems]]
- [[spider-technologies|Spider Technologies]]
- [[sybase|Sybase Inc.]]

## Technologies (8)

- [[cade|CADE (Client-Server Application Development Environment)]]
- [[electronic-commerce|Internet Electronic Commerce]]
- [[fusion-numa-technology|Fusion/NUMA Technology]]
- [[java|Java]]
- [[object-relational-rdbms|Object-Relational RDBMS]]
- [[tp-monitor-middleware|TP Monitor / Internet Middleware]]
- [[vlm-technology|VLM (Very Large Memory) Technology]]
- [[web-browser-server|Web Browser / Web Server]]

## Key observations (top 25)

- **1996** — Aberdeen Internet strategy recommendation: Intranet-first: real Internet value lies in internal use of Internet protocols; build architectural foundation before external deployment
- **1996** — Internet challenge 1: Content: Most enterprise data in plain-vanilla format; must define web-presentable data elements and user-friendly interface
- **1996** — Internet challenge 2: Scalability: Web browser/server become bottlenecks as demand grows; must use TP-monitor-like middleware to bypass
- **1996** — Internet challenge 3: Flexibility: No vendor has shrink-wrapped solution for all enterprise Internet needs; require Internet-enabled CADEs for customization
- **1996** — Internet challenge 4: Robustness: Internet web servers lag enterprise systems in security, availability, and administration tools
- **1996** — Internet challenge 5: Electronic Commerce: Wide array of e-commerce solutions emerging; IS must move aggressively to integrate into architecture
- **1996** — VLM server hardware for Internet: 64-bit VLM (>4GB RAM) enables higher performance for data warehousing and mixed OLTP/DSS Internet applications
- **1996** — Fusion/NUMA technology for Internet scaling: NUMA extends SMP with clustering and MPP features; allows scaling beyond SMP limits without application changes
- **1996** — Informix Illustra object-relational merger timeline: Informix + Illustra DataBlades object-relational solution to be merged by 1997
- **1997** — Informix Illustra merger outcome: Informix Universal Server (1996) integrated Illustra DataBlades; prediction accurate; Informix acquired by IBM 2001
- **1996** — Heterogeneous RDBMS replication by end of 1996: Aberdeen anticipates most RDBMS vendors will support heterogeneous replication by end of 1996
- **1996** — Oracle WebSystem internet middleware: Oracle WebSystem: replacement web browser/server with load balancing and RDBMS integration; best when Oracle already in architecture
- **1996** — Java capability assessment 1996: Java is overhyped; lacks 4GL/VPE extensions; applets too large for 28.8K baud; 'C++ for the Internet' near-term
- **1996** — Java medium-term role prediction: Most toolset suppliers will provide Java support by end of 1996; once CADEs add Java, they offer best-of-all-worlds
- **1999** — Java enterprise adoption outcome: Java became dominant enterprise application language by 1999-2001 (J2EE); CADE+Java prediction partially correct but applets also declined as Aberdeen predicted
- **1996** — E-commerce long-term value prediction: Internet electronic commerce promises dramatic decreases in selling costs and new opportunities for customer interaction
- **2005** — E-commerce transformation outcome: E-commerce transformed retail, financial services, and B2B transactions globally; selling cost reductions materialized as predicted
- **1996** — Telecom bandwidth constraint prediction: Big telecom companies will not deliver major end-user bandwidth increases in near future; 2-way cable not ready
- **2000** — Bandwidth expansion outcome: Broadband (DSL, cable) rollout accelerated 1998-2002; Aberdeen's near-term constraint proved partially correct but underestimated speed of cable/DSL
- **1996** — CA-Unicenter ICE for internet systems management: CA-Unicenter Internet Commerce Enabled (ICE) exemplifies trend toward enterprise-class systems management of internet computing
- **1996** — Middleware as most critical internet architecture component: Of all Internet architectural components, middleware is the most critical to scalability
- **1996** — Second-generation CADE Java support timeline: Many second-generation CADEs will allow highly scalable Internet application development by mid-1996
- **1998** — CADE Java support outcome: CADEs (PowerBuilder, Delphi, Forte etc.) added Java support by 1997-1998; CADEs largely displaced by Java IDE tools (Eclipse, NetBeans) by 2000

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-1996-computer-telephony-integration' ORDER BY year_observed;
```

