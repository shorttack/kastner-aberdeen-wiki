---
title: "True Enterprise Data Knowledge Through Integrated Data Marts"
slug: "study-aberdeen-1996-enterprise-data-knowledge-integrated-data-marts"
page_type: "study"
tags: ["type/study", "collection/market-study"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "aberdeen-1996-enterprise-data-knowledge-integrated-data-marts"
author: "Aberdeen Group"
date: "1996-09-23"
pub_year: 1996
type: "market-study"
subject_domain: "data-warehousing"
methodology: "industry-analysis, field-research, expert-opinion, document-review"
source_file: "1996 True Enterprise Data Knowledge Through Integrated Data Marts mvp.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 4.32
prescience_obs_count: 25
---

# True Enterprise Data Knowledge Through Integrated Data Marts


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=3.88 over 25 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.20 over 25 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Group argues that the proliferation of standalone departmental data marts—while individually successful—creates enterprise fragmentation, contradictory business rules, and ROI erosion. The study presents an iterative 'integrated data marts' architecture: building subject-specific data marts that feed a common RDBMS-based enterprise warehouse, using high-level industry templates and synchronization methodologies to deliver both business-unit autonomy and enterprise data integrity.


_Published 1996, author **Aberdeen Group**, type **market-study**._


## Top observations

- Aberdeen field experience: enterprises that build uncontrolled standalone data marts end up with contradictory business rules and enterprise-crippling data requests `[ps=5]`
- Most enterprises have one or more inconsistent definitions for basic enterprise expression 'revenue' across systems `[ps=5]`
- Managing synchronization across data marts is critical; requires disciplined ETL and common data stewardship `[ps=5]`
- Aberdeen advocates RDBMS-based architecture over proprietary multidimensional databases for enterprise data marts; RDBMS provides flexibility and integration path `[ps=5]`
- Standalone data marts: frequently commandeered by business units; adequately answer short-term objectives but prove shortsighted; risk of contradictory business rules `[ps=5]`
- RDBMS-driven technology is the preferred foundation; parallel-scalable hardware and RDBMS combine to create enterprise-capable warehouse platform `[ps=5]`
- Aberdeen identifies distinct data mart themes: sales/marketing, financial, manufacturing, supply chain — each requiring subject-specific modeling with common enterprise metrics `[ps=5]`
- Data transformation specialists (Prism Solutions et al.) provide critical ETL capabilities; short-term consulting engagements with suppliers a viable jump-start strategy `[ps=5]`
- Proprietary multidimensional database technologies optimize for domain-specific queries but create proprietary lock-in; RDBMS preferred for enterprise integration `[ps=5]`
- Begin with one data mart addressing a single subject area that links into an RDBMS-driven enterprise whole `[ps=4]`
- Enterprise must work from high-level model and common business metrics before building individual data marts `[ps=4]`
- Use iterative method of building a road map for the enterprise to follow; each data mart funds the next `[ps=4]`
- Involve end users throughout design; data marts must reflect business drivers embedded in end-user behavior `[ps=4]`
- Use Rapid Application Deployment to maintain business momentum; demonstrate ROI early to secure continued funding `[ps=4]`
- Early attempts at monolithic enterprise-wide warehouses failed due to rapidly changing business dynamics toppling top-down models `[ps=4]`
- Enterprise policy of encouraged fragmentation could be disastrous for the business; competitive disadvantage from incompatible data marts `[ps=4]`
- Enterprises that followed integrated model begin generating ROI that underwrites subsequent data mart efforts; project-by-project experience creates compounding value `[ps=4]`
- IS executives must build data access systems that reflect business drivers embedded in end-user behavior; IT-driven warehouses miss this requirement `[ps=4]`
- Aberdeen predicts integrated data mart approach (subject-by-subject building toward enterprise warehouse) will prove superior to standalone or top-down approaches `[ps=4]`
- Hub-and-spoke data warehouse architecture (matching Aberdeen's integrated model) became the dominant enterprise BI pattern through 2000s; standalone data marts caused exactly the fragmentation Aberdeen warned about `[ps=4]`
- Aberdeen: enterprises moving away from integrated spirit will squander ROI and be ill-prepared for competitive battles `[ps=4]`
- 'Data swamp' problem became widespread by 2013-2015 as unmanaged data lakes replicated exactly the fragmentation Aberdeen warned about; data governance and data catalog tools emerged to address this `[ps=4]`
- 'Factory ready' data infrastructure requires: parallel-scalable hardware, RDBMS, ETL tools, and data quality/transformation capabilities before data mart build `[ps=4]`
- Global trading, global risk assessment, and competitive intelligence needs cited as primary business drivers accelerating data mart adoption in 1996 `[ps=4]`
- NCR, Tandem, and Prism Solutions positioned as providers of industry-specific data warehouse templates and short-term consulting engagements `[ps=3]`
