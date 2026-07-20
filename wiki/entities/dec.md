---
title: "DEC (Digital Equipment Corporation)"
slug: "dec"
page_type: "entity"
tags: ["type/entity", "entity-type/company"]
tier: 1
source_csv: "_master_entities.csv"
entity_id: "dec"
entity_type: "company"
sector: "minicomputers / enterprise computing"
status: "dissolved"
successor: "Compaq (1998) then HP (2002)"
years_active: "1957-1998"
occurrence_count: 13
prescience_max: 5.0
prescience_mean: 1.51
prescience_obs_count: 88
---

# DEC (Digital Equipment Corporation)

> Primary publisher and subject; headquartered in Maynard MA; Peter S. Kastner led Marketing and the DECtp product work documented in this journal


## Summary




## Top observations

- DECtp was right that OLTP wouldn't stay confined to special-purpose machines and that benchmarks would matter, but DEC fought a platform war just as platform economics shifted beneath it. `[ps=5]` — [[study-2026-kastner-fault-tolerant-wars]]
- "95% of these transactions must be completed in one second or less. Cost per transaction is calculated by a formula which divides the five-year cost of hardware, software, and maintenance exclusive of staff by the number of transactions per second." `[ps=5]` — [[study-dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836]]
- TPC-A represents limited class of applications; additional benchmarks representing broader range of commercial applications expected to be standardized by TPC in coming years `[ps=5]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Kastner at DEC and TPC founding observed VAX/Unix vs. mainframe battle and OLTP benchmark standardization, 1987-1990. `[ps=5]` — [[study-volume-1-appendix-career-timeline]]
- DEC, Data General, and a dozen other minicomputer vendors were all telling same story in different dialects; all correct short run, almost all wrong long run. `[ps=5]` — [[study-volume-1-ch04-prime-computer-1979-1981]]
- DEC told same correct-short-run, wrong-long-run minicomputer story; DEC’s VAX ecosystem ultimately also lost to x86/Unix economics. `[ps=5]` — [[study-volume-1-ch04-prime-computer-1979-1981]]
- "The best way to get valid performance measures is to use a widely recognized, easily understood, and easily duplicated benchmark in which time, cost, throughput, and recovery are clearly specified." `[ps=4]` — [[study-dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836]]
- Six components: application program, resource manager, transaction manager, communication manager, presentation manager, request manager `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Uses snapshot transactions for online backup; parallel transaction recovery; on-line backup, verification and repair utilities; AIJ (after-image journal) files for roll-forward `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- When a node fails, another node detects failure and rolls back lost transactions from failed node; database available as soon as recovery complete `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- ACMS concentrates security on back-end using VMS ACLs on tasks; SYSUAF-based login; execution controller with access-control-list checking per task; dynamic application changes without stopping work `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- User security profiles, terminal security profiles, and GEOG attribute provide geographic entitlement: certain functions accessible only from specific terminals (e.g., bank officer sensitive functions only at home office) `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- 90 percent of transactions must have response time less than 2 seconds; end-to-end response time (user at terminal); maximum qualified throughput (MQTh) is key metric `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Key requirements for 100-year mean time between failures: software-fault containment using processes and software-fault masking using process checkpointing and transactions `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- For short TP transactions (modify 1 record): commit processing represents 36 percent of total transaction duration; for batch transactions (modify 500 records): commit processing only 0.2 percent `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Many older TP systems centralized and tied to particular vendor; as expansion continues beyond geographic boundaries, centralized single-vendor TP systems less able to offer needed flexibility `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- DEC, Data General, Prime, and a dozen others were selling machines real businesses could operate without a priesthood of systems programmers. `[ps=4]` — [[study-volume-1-ch03-physics-of-consulting-1972-1979]]
- Against DEC’s VAX ecosystem, Prime’s argument was responsiveness: shorter application cycles, tighter integration, modest minicomputer footprint for mid-sized organizations. `[ps=4]` — [[study-volume-1-ch04-prime-computer-1979-1981]]
- Kastner recalls the Plaza Hotel launch, July 1988, was built around Debit-Credit benchmark evidence, because benchmark discipline was the only way to escape vendor specmanship. `[ps=3]` — [[study-2026-kastner-fault-tolerant-wars]]
- One Company One Strategy One Message — Leading the Way to Enterprise-Wide Computing `[ps=3]` — [[study-dec-mgmt-memo-v7n5-state-of-company-1988-6a9954]]
