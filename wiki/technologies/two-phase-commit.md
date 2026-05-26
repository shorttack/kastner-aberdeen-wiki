---
title: "Two-Phase Commit Protocol (2PC)"
slug: "two-phase-commit"
page_type: "technology"
tags: ["type/technology", "category/distributed-transaction-protocol", "era/1978-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "two-phase-commit"
category: "distributed-transaction-protocol"
vendor: "Industry / X-Open"
era: "1978-present"
lifecycle_at_study: "industry-standard-X-Open-XA-since-1991"
lifecycle_current: "industry-standard-X-Open-XA-since-1991"
occurrence_count: 3
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Two-Phase Commit Protocol (2PC)

> Atomic commit protocol ensuring all-or-nothing transaction semantics across distributed resource managers; central protocol in DECdtm; DEC implemented optimized variant with VAXcluster-specific blocking reduction


## Top observations

- not-available-in-DEC-stack — [[study-dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e]]
- Phase I writes all updated records to disk and sets 'Phase I Commit' flag in file header; original disk image preserved; all involved nodes must report Phase I success before VOS authorizes Phase II commit; restart-salvage detects Phase I Commit flag — [[study-ieee-db-stratus-32-psk-1d4564]]
- Verified: 2PC is the textbook distributed-commit protocol in 2026; XA standard, modern systems still implement Phase I/Phase II with prepare-flag durability — [[study-ieee-db-stratus-32-psk-1d4564]]
- All major vendors implementing; no single implementation stands out — [[study-nti-6-rdbms-technology-48f4aa]]
