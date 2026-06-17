---
title: "Stratus ET1 Implementation (May 1, 1986)"
slug: "stratus-et1-implementation"
page_type: "technology"
tags: ["type/technology", "category/transaction-processing-implementation", "era/1986-late-1980s"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "stratus-et1-implementation"
category: "transaction-processing-implementation"
vendor: "Stratus"
era: "1986-late-1980s"
lifecycle_at_study: "newly-defined-1986"
lifecycle_current: "obsolete"
occurrence_count: 1
prescience_max: 3.0
prescience_mean: 2.0
prescience_obs_count: 3
---

# Stratus ET1 Implementation (May 1, 1986)

> Stratus's official ET1 implementation per May 1, 1986 functional spec


## Top observations

- Read X.25 + Read/Rewrite Account/Teller/Branch + Write History sequential + Write X.25 ack `[ps=3]` — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
- 2M accounts (200 MB), 2K tellers, 200 branches (per module); access patterns: Account indexed, Teller relative random, Branch relative random `[ps=3]` — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
- 85% transactions hit current process branch; remaining 15% dispatched to other modules `[ps=0]` — [[study-stratus-et1-functional-spec-and-benchmar-0c3172]]
