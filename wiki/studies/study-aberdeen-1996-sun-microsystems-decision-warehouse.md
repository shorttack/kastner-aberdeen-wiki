---
title: "Sun Microsystems Decision Warehouse"
slug: "study-aberdeen-1996-sun-microsystems-decision-warehouse"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-sun-microsystems-decision-warehouse"
author: "Aberdeen Group"
date: "1996-03-01"
pub_year: 1996
type: "market-study"
subject_domain: "data-warehousing-Unix-servers"
methodology: "industry-analysis, competitive-profiling, benchmarking, field-research"
source_file: "1996 dw Sun Microsystems Decision Warehouse pr.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 1.86
prescience_obs_count: 14
---

# Sun Microsystems Decision Warehouse

> This Aberdeen Group profile evaluates Sun Microsystems Computer Corporation's (SMCC) Decision Warehouse program, examining its UltraSPARC server architecture, SPARCstorage arrays, Solaris 2.5 SMP optimization, Database Engineering group, and partnerships with Oracle, Sybase, Informix, and other RDBMS vendors. Aberdeen concludes that SMCC has the requisite components to differentiate itself in the data warehousing market, projecting strong scalability for terabyte-class warehouses through the Enterprise Server Test Center and Competency Centers.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- Sun became a leading Unix data warehouse platform through the late 1990s-early 2000s; UltraSPARC/Solaris widely used for Oracle data warehouses. Sun's position weakened after 2003 as x86/Linux and commodity hardware eroded Unix server market; acquired by Oracle 2010. `[ps=5]`
- SPARCstorage arrays with fiber channels; hot-swap HA features; superior MTBF; mission-critical grade I/O; sequential access optimized for data warehouse workloads `[ps=4]`
- Comprehensive data warehouse infrastructure: UltraSPARC servers + Gigaplane bus + Solaris 2.5 + SPARCstorage + Database Engineering group + RDBMS partnerships + competency centers `[ps=3]`
- 2.6 GBps Gigaplane bus eliminates memory/disk bottleneck; multiple parallel CPU/I/O/network interconnections; exceeds anything available in comparable Unix systems `[ps=3]`
- Aberdeen: SMCC's Database Engineering group is its 'secret weapon' — dedicated to making major database products run as fast as possible; >$10M test center investment; Solaris 2.5 SMP improvements enabled by group testing `[ps=3]`
- 40-45% annual staff growth rate for past 3 years; expects to continue; Sun ranked top 3 in customer satisfaction North America, Europe, Asia `[ps=2]`
- NT Server scalability 'pales' vs Solaris; NT SMP overhead up to 30% vs Solaris 3-8%; Sun competes well against NT even for small warehouse/proof-of-concept `[ps=2]`
- Solaris 2.5 fine-tuned for multiprocessor; threaded I/O and networking; constant query response time as dataset and user count grow; 3-8% CPU overhead (vs up to 30% for NT) `[ps=2]`
- Bilateral engineering agreements with Oracle/Sybase/Informix; joint competency centers; bilateral optimization giving both SMCC and RDBMS supplier code improvements; classified as 'secret weapon' `[ps=2]`
- ~$7 billion FY1996 (ending June 30); commercial sales >$1.5B (at least one-third of revenue) `[ps=0]`
- Storage Products Group revenues estimated >$1 billion; independent P&L unit within SMCC `[ps=0]`
- SMCC invested >$10 million in Enterprise Server Test Center; tested data warehouses from 20GB pilots to 5.5TB Oracle demonstration `[ps=0]`
- 92-97% SMP scalability (depending on RDBMS) as CPUs added; only 3-8% overhead per added CPU vs 15-20% for typical Unix SMP and up to 30% for NT Server `[ps=0]`
- SMCC clusters support Oracle 7.3 distributed parallel query; pair of servers clustered using high-speed fiber channels; RDBMS contacts admitted product could not have been marketed without SMCC engineering involvement `[ps=0]`
- 2.6 GBps system bus; thin boards with dual CPUs + memory (up to 2GB/board) + high-speed I/O channels; parallel CPU/I/O/network interconnections approaching mainframe speeds
- Enterprise-level production data warehouses grow 3-5x in 18 months; majority >100GB now moving from pilot to full implementation; handful already over terabyte
- Aberdeen predicts warehouse sizes approaching terabyte with hundreds of attached users; production warehouses outpacing supplier capabilities except those (like SMCC) who solved scalability issues
- Prediction proved accurate: enterprise data warehouses grew to multi-terabyte scale by 2000-2005; petabyte-scale warehouses emerged by 2010 (Teradata, Netezza, then Hadoop). Scalability became the defining vendor differentiator as Aberdeen predicted.
- Aberdeen believes SMCC has requisite pieces to differentiate in data warehousing; expects Decision Warehouse customers to be 'spared the pain' of inadequate scalability
- Hot-swap disk modules, fans, power supplies; 4.2GB drives (3.5 inch backplane); industry-standard fiber channels; RAS Customer Action Team for storage issues; superior MTBF vs competitors
- UltraSPARC 64-bit delivers 2x power of prior SPARC; new high-speed servers shipping May 1996
