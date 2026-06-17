---
title: "Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities"
slug: "study-1997-digital-s-terabyte-hour-nonstop-vld-ce92ca"
page_type: "study"
tags: ["type/study", "collection/Viewpoint"]
tier: 1
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
prescience_max: 5.0
prescience_mean: 2.92
prescience_obs_count: 24
---

# Digital's Terabyte/Hour NonStop VLDB: Consider The Possibilities

> Aberdeen Group assessed Digital Equipment Corporation's NonStop VLDB backup/restore solution in May 1997, which delivered 400-750+ GB/hour rates — an order-of-magnitude improvement. Aberdeen predicted this technology would 'go strategic,' removing backup/restore as a database scaling barrier and enabling new architectures for data migration, disaster tolerance, and rolling VLDB operations.


_Published 1997, author **Aberdeen Group**, type **Viewpoint**._


## Top observations

- Backup/restore will go from commodity to strategic capability `[ps=5]`
- SAN snapshots, disk-based backup, and deduplication (EMC Data Domain, NetApp SnapVault) delivered order-of-magnitude improvements in backup/restore speed by 2005-2010, validating Aberdeen's prediction. `[ps=5]`
- Aberdeen's prediction that backup/restore would 'go strategic' was validated: continuous data protection (CDP), cloud backup (AWS Backup, Azure Backup), and cloud DR became multi-billion dollar markets by 2015-2020. `[ps=5]`
- Data warehouse refresh frequency improved dramatically. Modern data warehouses and data lakes support near-real-time or continuous loading by 2010-2020, validating Aberdeen's prediction. `[ps=5]`
- Parallelized online backup reduced but did not eliminate bottleneck `[ps=4]`
- 4 categories: administrative costs, availability reduction, downtime after crashes, database sclerosis `[ps=4]`
- 5 new applications: reconfiguration, rolling backup, data migration, disaster tolerance, security recovery `[ps=4]`
- Enterprise backup centers, data warehouses, rapidly-scaling new solutions (ERP, web servers) `[ps=4]`
- Night-long backup → 30 minutes; 2-day weekend backup → 3 hours `[ps=4]`
- First-mover; ½ to 1-year technology lead `[ps=4]`
- Technology is real; has arrived; delivers significant benefits; demands strategic rethinking `[ps=4]`
- Fast backup/restore enables dedicated migration server `[ps=4]`
- Compaq's acquisition of DEC in June 1998 effectively ended NonStop VLDB product development and marketing as predicted. `[ps=4]`
- SGI went bankrupt 2006/2009 and never became a backup/restore technology leader. The fast backup market was led by disk-based backup vendors (EMC, NetApp, Symantec), not traditional HPTC vendors. `[ps=4]`
- Upper limits to all databases removed; even 10TB can be backed up in one night `[ps=3]`
- Symantec acquired Open Vision Technologies' backup software in 1999; it became Symantec NetBackup, one of the dominant enterprise backup products for decades. `[ps=3]`
- SGI among first competitors in fast backup/restore market `[ps=2]`
- Periodic backup to remote tape bank viable alternative to expensive mirroring `[ps=2]`
- 3-16% in tests `[ps=0]`
- ~10 GB/hour `[ps=0]`
- 40-200 GB (depending on update frequency) `[ps=0]`
- AlphaServer 8400; 8 CPUs; 8 GB RAM; TLIOP with 4 PCI buses; 30 SCSI controllers; 16 tape drives `[ps=0]`
- Less than 10 terabytes (data warehouses with few updates) `[ps=0]`
- Under 20 minutes for databases under 100 GB `[ps=0]`
- 400–750 GB/hour
