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
prescience_max: 5.0
prescience_mean: 1.25
prescience_obs_count: 4
---

# Two-Phase Commit Protocol (2PC)

> Atomic commit protocol ensuring all-or-nothing transaction semantics across distributed resource managers; central protocol in DECdtm; DEC implemented optimized variant with VAXcluster-specific blocking reduction


## Top observations

- Verified: 2PC is the textbook distributed-commit protocol in 2026; XA standard, modern systems still implement Phase I/Phase II with prepare-flag durability `[ps=5]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- not-available-in-DEC-stack `[ps=0]` — [[study-dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e]]
- Phase I writes all updated records to disk and sets 'Phase I Commit' flag in file header; original disk image preserved; all involved nodes must report Phase I success before VOS authorizes Phase II commit; restart-salvage detects Phase I Commit flag `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- All major vendors implementing; no single implementation stands out `[ps=0]` — [[study-nti-6-rdbms-technology-48f4aa]]
