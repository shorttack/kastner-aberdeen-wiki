---
title: "Who Cares If The Computer Breaks?"
slug: "study-ft-mitfor-1-a56a9d"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 2
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
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Who Cares If The Computer Breaks?

> A presentation delivered at the MIT Forum in October 1995 examining why computer failures are increasingly catastrophic as society's dependence on computing grows. Kastner surveys the causes of hardware, software, and network failure, then presents a spectrum of high-availability and fault-tolerance strategies ranging from RAID to fully redundant failover architectures. The talk concludes that future availability gains will depend on system software enabling application failover without prohibitive development costs.


_Published 1995, author **Peter S. Kastner**, type **white-paper**._


## Top observations

- 45% of U.S. workers now using PCs
- Commercial computers transitioned from book-keeping to money-making role; failures now catastrophic
- Unit reliability improves; system reliability declines due to more components
- Software fails due to complexity exceeding human capacity, poor design/testing, repeated rework
- Network availability is a key inhibitor to growth of distributed computing
- 99.9% uptime is a floor not the ceiling in today's business world
- 5,259.6 minutes per year
- 526.0 minutes per year
- 52.6 minutes per year
- 5.3 minutes per year
- 0.5 minutes per year
- RAID disk storage is a recommended hardware approach to minimize downtime
- Primary/secondary heartbeat failover: primary saves key data, sends heartbeat; secondary monitors and restarts
- Stratus exemplifies hardware self-checking failover architecture
- Tandem exemplifies N+1 failover architecture
- Digital Equipment exemplifies shared disk failover architecture
- RDBMS and OLTP software ensures data recoverability
- Most future availability improvements will depend on system software enabling application failover without dramatic cost/complexity increase
- Confirmed — systems management/monitoring became multi-billion-dollar market (Tivoli, BMC, CA, now Datadog, Splunk, Dynatrace)
- Buyers want highest availability but unwilling to pay much more than commodity prices
- Self-repairing networks identified as an emerging opportunity
- Systems management tools down to application-object level represent opportunity
- Disaster backup services for client-server applications identified as new business opportunity
- Confirmed — disaster recovery for distributed systems became standard practice; cloud DR services now mainstream
