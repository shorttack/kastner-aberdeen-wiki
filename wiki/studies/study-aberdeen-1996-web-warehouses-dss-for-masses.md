---
title: "Web Warehouses: DSS For The Masses"
slug: "study-aberdeen-1996-web-warehouses-dss-for-masses"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-web-warehouses-dss-for-masses"
author: "Aberdeen Group"
date: "1996-03-25"
pub_year: 1996
type: "market-study"
subject_domain: "data-warehousing"
methodology: "industry-analysis, field-research, expert-opinion, competitive-profiling"
source_file: "1996 Web Warehouses_ DSS For The Masses tvp.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Web Warehouses: DSS For The Masses

> Aberdeen Group argues that the combination of the World Wide Web, Relational OLAP, and parallel-scalable hardware will 'democratize' enterprise data warehousing by dramatically reducing per-seat decision support costs (Web browser at ~$50/seat vs. $1,000/seat for traditional DSS software). The study analyzes Web-based decision support architecture, identifies hurdles to enterprise adoption (security, CGI bottlenecks, browser immaturity), and concludes that Web-enabled warehouses will transform enterprise competitive behavior.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- Web browser: approximately $50/seat (quantity 1) vs. average $1,000/seat for traditional decision-support software
- NCR has approximately 12 years experience designing, managing and implementing data warehouses in virtually every industry
- Traditional warehouse cost barriers: warehouse design + desktop software + hardware + connectivity + dedicated lines to suppliers/offices + replication costs as system grows
- Browsers lack OLE, cut-and-paste ease, formatting inheritance compared to Windows front ends; power users will initially need coexistence of client-server and web ROLAP
- CGI is a single-threaded bottleneck for communicating from web server to applications; must be replaced by multi-threaded alternatives for enterprise BI
- Relational OLAP + HTML + Web server + cache-enhanced SQL = multidimensional analysis on the Web; MicroStrategy and Information Advantage leading implementations
- Web DSS demands: scalability (incremental CPUs/RAID), high availability (online backup/redundancy), RDBMS parallelization, systems/network management; same as traditional warehouse but at higher scale
- RDBMS is foundation for Relational OLAP and Web warehousing; parallel-scalable RDBMS required; proprietary multidimensional DBs incompatible with Web architecture
- Security beyond data encryption/browser authentication required before enterprise Web DSS deployment
- CGI single-threaded bottleneck must be replaced by multi-threaded alternative for enterprise-scale web BI
- Browsers must mature to accommodate dynamic portfolio analysis, not just static financial data
- HTML-based development tools need to add pop-up windows and radio bars to match GUI desktop capabilities
- Better integration with desktop applications (spreadsheets) required for power user adoption
- Natural information-gathering, no-update affinity between decision support and Web makes DSS the first high-impact Web candidate
- Aberdeen: as browsers mature, CEOs and high-level decision makers will mandate IS to build Web-enabled decision support
- Web reapportions warehouse costs: savings on desktop software/deployment redirected to server hardware, RDBMS, and data preparation — exactly where investment belongs
- Decision support is becoming so enterprise critical it is being placed in a reciprocal relationship with OLTP; IS must pay attention to OLTP-data download speed
- Aberdeen predicts Web browser will become the primary delivery mechanism for enterprise decision support, removing traditional DSS per-seat cost barrier
- Web browser became universal BI client by 2000-2005; Tableau (2003), Power BI, Looker all browser-based; Salesforce CRM entirely browser-based; per-seat BI costs dropped dramatically
- Aberdeen: most obstacles (security, CGI, browser maturity) will be swept away over next 1-2 years, driving new DSS/warehouse applications
- SSL security became standard by 1997; CGI replaced by ISAPI/NSAPI and FastCGI by 1997-1998; DHTML/JavaScript addressed browser limitations; all major obstacles resolved within Aberdeen's 1-2 year timeline
- NCR Worldmark servers cover SMP, Clusters, and MPP configurations; Teradata scales from data marts to multi-terabyte detailed warehouses
- NCR (infrastructure + consulting + industry templates) + MicroStrategy (ROLAP toolset) = 'warehouse-supplier synergy' model for enterprise Web DSS
- Enterprise Web warehouse strategy: start small SMP, scale within SMP range if appropriate, or grow to MPP — same architecture at different scale without recompilation
- Aberdeen: Internet will evolve into secure electronic backbone serving both intranet and business-to-business applications; decision support is the first high-impact candidate
