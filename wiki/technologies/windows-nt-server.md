---
title: "Windows NT Server"
slug: windows-nt-server
page_type: technology
category: platform
vendor: "Microsoft"
era: "1993-2001"
lifecycle_at_study: "emerging"
lifecycle_current: "obsolete"
tier: 1
study_count: 12
obs_count: 43
aliases: ["Windows NT Server"]
tags: [type/technology, category/platform, vendor/microsoft]
source_csv: known_technologies.csv
---

# Windows NT Server

Windows NT Server is a platform from Microsoft (era 1993-2001). Current lifecycle: obsolete.

**Appears in 12 studies, 43 observations.**

## Studies citing this technology

- [[dssune~1-cbf6e3|Data Knowledge: 1998 Practice Summary]] (1998-07-01)
- [[mockup~1-ca8fde|Network Operating Systems: 1998 Practice Summary — Mockup/Template]] (1998-05-01)
- [[ncr-bringing-highly-available-nt-ecb055|NCR: Bringing Highly-Available NT to Transaction-Intensive Production Environments]] (1997-10-01)
- [[1997-ca-s-unicenter-tng-framework-pk-apr-50d15f|CA's Unicenter TNG Framework: Entry-Level for the Industry's Best Enterprise Management Software Solution]] (1997-07-14)
- [[aberdeen-1996-digital-debunks-ntsmp-scalability-myth|Digital Debunks the NT/SMP Scalability Myth]] (1996-11-22)
- [[aberdeen-1996-evaluating-system36-migration-strategies|Evaluating System/36 Migration Strategies]] (1996-09-01)
- [[aberdeen-1996-ncr-fail-safe-enterprise-nt|NCR: Finally a Fail-Safe Choice For Enterprise NT]] (1996-05-25)
- [[aberdeen-1996-sun-microsystems-decision-warehouse|Sun Microsystems Decision Warehouse]] (1996-03-01)
- [[aberdeen-1996-object-oriented-three-tier-plus-computing|Object-Oriented Three-Tier-Plus Computing: Client-Server for Adults]] (1996-02-01)
- [[rdbms-for-ibm-powera~1-7a44be|Power Academy RDBMS Sales Training]] (1996-01-23)

## Top observations

- **1997** — CA total annual revenue at time of announcement: $4+ billion annual revenue (Unicenter TNG at $1B run rate = ~25% of total) ([[1997-ca-s-unicenter-tng-framework-pk-apr-50d15f]])
- **1997** — CA total annual revenue at time of announcement: $4+ billion annual revenue (Unicenter TNG at $1B run rate = ~25% of total) ([[1997-ca-s-unicenter-tng-framework-pk-apr-50d15f]])
- **1995** — Compaq NT TPC-C benchmark baseline (Nov 1995): 2,400 tpmC at $242/tpmC (Compaq ProLiant Intel-based) ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — Server market sweet spot transaction range: 2,000 to 15,000 tpmC (midrange); below 2,500 tpmC (workgroup); above 15,000 tpmC (high-end/enterprise) ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — NT server market volume distribution by CPU count: Over 90% of all server systems sold are 4-way-or-less ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — Microsoft NT performance strategy: Three-pronged: (1) maximize 4-way performance via CPU tuning; (2) continue limited SMP beyond 4-way; (3) pursue high-end via performance clustering (Wolfpack) ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — Aberdeen explanation for NT SMP scalability gap: NT scalability limits beyond 4-way are not engineering-based but are a deliberate market economics decision by Microsoft ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — NT 32-bit architecture limitation assessment: NT 8-way+ systems will remain low-volume as long as NT is 32-bit; 64-bit NT needed for full high-end capability ([[aberdeen-1996-digital-debunks-ntsmp-scalability-myth]])
- **1996** — PC-LAN capital cost: 10-user system: Hardware: $24,125; Systems software: $9,690; Basic accounting package: ~$12,500 (additional) ([[aberdeen-1996-evaluating-system36-migration-strategies]])
- **1996** — PC-LAN capital cost: 20-user system: Hardware: $40,875; Systems software: $15,040; Basic accounting package: $22,500 ([[aberdeen-1996-evaluating-system36-migration-strategies]])
- **1996** — PC-LAN operational cost rule of thumb: $10,000 per year to manage, maintain, and upgrade a Windows NT Server + $1,000 per year for each attached PC ([[aberdeen-1996-evaluating-system36-migration-strategies]])
- **1996** — Aberdeen PC-LAN assessment for legacy migration: PC-LAN migration may be appropriate for those automating for the first time; it is not practical for System/36 owners who cannot afford to build new IT infrastructure from scratch ([[aberdeen-1996-evaluating-system36-migration-strategies]])
- **1996** — NCR NT enterprise strategy: RAS-augmentation: add enterprise-grade HA/clustering/TP-monitor on top of NT ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1995** — RAD schedule reduction: 20-25% reduction in OLTP application deployment time; some sites reported 50% ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1996** — SQL Server cost advantage vs alternatives: Microsoft SQL Server 6.5 on NT up to 90% less costly than Unix/OpenVMS/MVS RDBMS alternatives ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1996** — NT SMP scalability roadmap: NT/SQL Server to scale to 8 CPUs with NT Server 4.0 (fall 1996); 12-16 CPUs by mid-1997 ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1997** — NT SMP scalability achieved: Windows NT Server 4.0 Enterprise Edition (Sept 1997) supported 8-way SMP clustering; SQL Server 7.0 (1998) supported 8+ CPUs ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1996** — Aberdeen overall verdict on NCR NT: NCR is an 'experienced, fail-safe choice for NT-based OLTP application deployments' ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1994** — AT&T GIS enterprise NT commitment announcement: August 1994: AT&T GIS announced plan to bring NT into enterprise with scalability, manageability, reliability, serviceability features ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])
- **1996** — NT OLTP benefit factor 1: Time to market: IT decision makers primary motivation: NT enables faster competitive response than legacy mainframe ([[aberdeen-1996-ncr-fail-safe-enterprise-nt]])

## DuckDB query for full data

```sql
SELECT * FROM observations WHERE tech_id = 'windows-nt-server';
```

