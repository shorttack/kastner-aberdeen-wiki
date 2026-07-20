---
title: "DECdtm (Digital Distributed Transaction Manager)"
slug: "decdtm"
page_type: "technology"
tags: ["type/technology", "category/transaction-processing", "era/1980s-1990s"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "decdtm"
category: "transaction-processing"
vendor: "Digital Equipment Corporation"
era: "1980s-1990s"
lifecycle_at_study: "emerging distributed transaction manager"
lifecycle_current: "legacy-discontinued"
occurrence_count: 2
prescience_max: 4.0
prescience_mean: 2.0
prescience_obs_count: 6
---

# DECdtm (Digital Distributed Transaction Manager)

> Embedded in VMS OS kernel; implements optimized two-phase commit protocol; supports distributed atomic transactions across multiple resource managers and nodes; VAXcluster-optimized blocking reduction


## Top observations

- Key requirements for 100-year mean time between failures: software-fault containment using processes and software-fault masking using process checkpointing and transactions `[ps=4]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- DECdtm uses optimized variant of 2PC; VAXcluster capabilities greatly reduce potential for blocking versus traditional 2PC `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Future DECdtm services designed to conform to de facto and international standards for transaction processing; ensures VMS application interoperability with other vendors `[ps=3]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- Embedding transaction semantics in VMS kernel provides consistency, interoperability, and flexibility across all applications not limited to traditional TP `[ps=2]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
- historical `[ps=0]` — [[study-2026-kastner-dec-longitudinal-22d177]]
- $START_TRANSW, $END_TRANSW, $ADD_BRANCHW, $START_BRANCHW, $READY_TO_COMMITW, $DECLARE_RMW, $JOIN_RMW, $FINISH_RMOPW system service calls `[ps=0]` — [[study-dtj-v03-01-tp-and-fault-tolerant-1991-cf078c]]
