---
title: "Web Warehouses: DSS For The Masses"
slug: "study-aberdeen-1996-web-warehouses-dss-for-masses"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
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
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 3.78
prescience_obs_count: 18
---

# Web Warehouses: DSS For The Masses


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=4.00 over 25 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.44 over 25 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Group argues that the combination of the World Wide Web, Relational OLAP, and parallel-scalable hardware will 'democratize' enterprise data warehousing by dramatically reducing per-seat decision support costs (Web browser at ~$50/seat vs. $1,000/seat for traditional DSS software). The study analyzes Web-based decision support architecture, identifies hurdles to enterprise adoption (security, CGI bottlenecks, browser immaturity), and concludes that Web-enabled warehouses will transform enterprise competitive behavior.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- Web browser: approximately $50/seat (quantity 1) vs. average $1,000/seat for traditional decision-support software `[ps=5]`
- Web DSS demands: scalability (incremental CPUs/RAID), high availability (online backup/redundancy), RDBMS parallelization, systems/network management; same as traditional warehouse but at higher scale `[ps=5]`
- Browsers must mature to accommodate dynamic portfolio analysis, not just static financial data `[ps=5]`
- Better integration with desktop applications (spreadsheets) required for power user adoption `[ps=5]`
- Web browser became universal BI client by 2000-2005; Tableau (2003), Power BI, Looker all browser-based; Salesforce CRM entirely browser-based; per-seat BI costs dropped dramatically `[ps=5]`
- NCR Worldmark servers cover SMP, Clusters, and MPP configurations; Teradata scales from data marts to multi-terabyte detailed warehouses `[ps=5]`
- Browsers lack OLE, cut-and-paste ease, formatting inheritance compared to Windows front ends; power users will initially need coexistence of client-server and web ROLAP `[ps=4]`
- Aberdeen: as browsers mature, CEOs and high-level decision makers will mandate IS to build Web-enabled decision support `[ps=4]`
- Web reapportions warehouse costs: savings on desktop software/deployment redirected to server hardware, RDBMS, and data preparation — exactly where investment belongs `[ps=4]`
- Decision support is becoming so enterprise critical it is being placed in a reciprocal relationship with OLTP; IS must pay attention to OLTP-data download speed `[ps=4]`
- Aberdeen predicts Web browser will become the primary delivery mechanism for enterprise decision support, removing traditional DSS per-seat cost barrier `[ps=4]`
- Aberdeen: most obstacles (security, CGI, browser maturity) will be swept away over next 1-2 years, driving new DSS/warehouse applications `[ps=4]`
- Relational OLAP + HTML + Web server + cache-enhanced SQL = multidimensional analysis on the Web; MicroStrategy and Information Advantage leading implementations `[ps=3]`
- RDBMS is foundation for Relational OLAP and Web warehousing; parallel-scalable RDBMS required; proprietary multidimensional DBs incompatible with Web architecture `[ps=3]`
- Natural information-gathering, no-update affinity between decision support and Web makes DSS the first high-impact Web candidate `[ps=3]`
- NCR (infrastructure + consulting + industry templates) + MicroStrategy (ROLAP toolset) = 'warehouse-supplier synergy' model for enterprise Web DSS `[ps=3]`
- HTML-based development tools need to add pop-up windows and radio bars to match GUI desktop capabilities `[ps=2]`
- NCR has approximately 12 years experience designing, managing and implementing data warehouses in virtually every industry `[ps=0]`
- Traditional warehouse cost barriers: warehouse design + desktop software + hardware + connectivity + dedicated lines to suppliers/offices + replication costs as system grows
- CGI is a single-threaded bottleneck for communicating from web server to applications; must be replaced by multi-threaded alternatives for enterprise BI
- Security beyond data encryption/browser authentication required before enterprise Web DSS deployment
- CGI single-threaded bottleneck must be replaced by multi-threaded alternative for enterprise-scale web BI
- SSL security became standard by 1997; CGI replaced by ISAPI/NSAPI and FastCGI by 1997-1998; DHTML/JavaScript addressed browser limitations; all major obstacles resolved within Aberdeen's 1-2 year timeline
- Enterprise Web warehouse strategy: start small SMP, scale within SMP range if appropriate, or grow to MPP — same architecture at different scale without recompilation
- Aberdeen: Internet will evolve into secure electronic backbone serving both intranet and business-to-business applications; decision support is the first high-impact candidate
