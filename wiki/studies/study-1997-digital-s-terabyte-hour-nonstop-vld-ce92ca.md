---
title: "Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities"
slug: "study-1997-digital-s-terabyte-hour-nonstop-vld-ce92ca"
page_type: "study"
tags: ["type/study", "collection/Viewpoint"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "1997-digital-s-terabyte-hour-nonstop-vld-ce92ca"
author: "Aberdeen Group"
date: "1997-05-20"
pub_year: 1997
type: "Viewpoint"
subject_domain: "Database Storage / Very Large Database Management"
methodology: "Aberdeen benchmark analysis; vendor briefing; technical architecture assessment; market research"
source_file: "1997 Digital_s Terabyte_Hour NonStop VLDB pvp.pdf"
license: "CC-BY-4.0"
importance: "medium"
relevance: "medium"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities

> Aberdeen Group assessed Digital Equipment Corporation's NonStop VLDB backup/restore solution in May 1997, which delivered 400-750+ GB/hour rates — an order-of-magnitude improvement. Aberdeen predicted this technology would 'go strategic,' removing backup/restore as a database scaling barrier and enabling new architectures for data migration, disaster tolerance, and rolling VLDB operations.


_Published 1997, author **Aberdeen Group**, type **Viewpoint**._


## Top observations

- 400–750 GB/hour
- 3-16% in tests
- 1.5 TB/hour (with 1-2 additional TLIOP channels)
- ~10 GB/hour
- 40-200 GB (depending on update frequency)
- AlphaServer 8400; 8 CPUs; 8 GB RAM; TLIOP with 4 PCI buses; 30 SCSI controllers; 16 tape drives
- Oracle, Informix, Sybase, Microsoft SQL Server, SAP R/3
- High-end Unix or cost-effective Windows NT
- Parallelized online backup reduced but did not eliminate bottleneck
- Less than 10 terabytes (data warehouses with few updates)
- 4 categories: administrative costs, availability reduction, downtime after crashes, database sclerosis
- 5 new applications: reconfiguration, rolling backup, data migration, disaster tolerance, security recovery
- Enterprise backup centers, data warehouses, rapidly-scaling new solutions (ERP, web servers)
- Night-long backup → 30 minutes; 2-day weekend backup → 3 hours
- Under 20 minutes for databases under 100 GB
- First-mover; ½ to 1-year technology lead
- Well-regarded service arm for installation and maintenance
- Technology is real; has arrived; delivers significant benefits; demands strategic rethinking
- Backup/restore will go from commodity to strategic capability
- SGI among first competitors in fast backup/restore market
- Upper limits to all databases removed; even 10TB can be backed up in one night
- Fast backup/restore enables dedicated migration server
- Periodic backup to remote tape bank viable alternative to expensive mirroring
- Compaq's acquisition of DEC in June 1998 effectively ended NonStop VLDB product development and marketing as predicted.
- SAN snapshots, disk-based backup, and deduplication (EMC Data Domain, NetApp SnapVault) delivered order-of-magnitude improvements in backup/restore speed by 2005-2010, validating Aberdeen's prediction.
