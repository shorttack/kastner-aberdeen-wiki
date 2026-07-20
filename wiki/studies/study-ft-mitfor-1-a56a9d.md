---
title: "Who Cares If The Computer Breaks?"
slug: "study-ft-mitfor-1-a56a9d"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "ft-mitfor~1-a56a9d"
author: "Peter S. Kastner"
date: "1995-10-01"
pub_year: 1995
type: "white-paper"
subject_domain: "fault-tolerance, high-availability"
methodology: "industry-analysis, expert-opinion"
source_file: "FT MITFOR~1.pdf"
license: "CC-BY-4.0"
importance: "medium"
relevance: "high"
study_prescience_enum: "medium"
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 3.12
prescience_obs_count: 24
---

# Who Cares If The Computer Breaks?


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=4.04 over 24 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.29 over 24 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> A presentation delivered at the MIT Forum in October 1995 examining why computer failures are increasingly catastrophic as society's dependence on computing grows. Kastner surveys the causes of hardware, software, and network failure, then presents a spectrum of high-availability and fault-tolerance strategies ranging from RAID to fully redundant failover architectures. The talk concludes that future availability gains will depend on system software enabling application failover without prohibitive development costs.


_Published 1995, author **Peter S. Kastner**, type **white-paper**._


## Top observations

- Commercial computers transitioned from book-keeping to money-making role; failures now catastrophic `[ps=5]`
- RAID disk storage is a recommended hardware approach to minimize downtime `[ps=5]`
- Stratus exemplifies hardware self-checking failover architecture `[ps=5]`
- Confirmed — systems management/monitoring became multi-billion-dollar market (Tivoli, BMC, CA, now Datadog, Splunk, Dynatrace) `[ps=5]`
- Systems management tools down to application-object level represent opportunity `[ps=5]`
- Software fails due to complexity exceeding human capacity, poor design/testing, repeated rework `[ps=4]`
- Network availability is a key inhibitor to growth of distributed computing `[ps=4]`
- 99.9% uptime is a floor not the ceiling in today's business world `[ps=4]`
- Primary/secondary heartbeat failover: primary saves key data, sends heartbeat; secondary monitors and restarts `[ps=4]`
- Tandem exemplifies N+1 failover architecture `[ps=4]`
- Digital Equipment exemplifies shared disk failover architecture `[ps=4]`
- Most future availability improvements will depend on system software enabling application failover without dramatic cost/complexity increase `[ps=4]`
- Buyers want highest availability but unwilling to pay much more than commodity prices `[ps=4]`
- Self-repairing networks identified as an emerging opportunity `[ps=4]`
- Disaster backup services for client-server applications identified as new business opportunity `[ps=4]`
- Confirmed — disaster recovery for distributed systems became standard practice; cloud DR services now mainstream `[ps=4]`
- Unit reliability improves; system reliability declines due to more components `[ps=3]`
- RDBMS and OLTP software ensures data recoverability `[ps=3]`
- 45% of U.S. workers now using PCs `[ps=0]`
- 5,259.6 minutes per year `[ps=0]`
- 526.0 minutes per year `[ps=0]`
- 52.6 minutes per year `[ps=0]`
- 5.3 minutes per year `[ps=0]`
- 0.5 minutes per year `[ps=0]`
