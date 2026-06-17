---
title: "Solaris 2.5"
slug: "solaris-25"
page_type: "technology"
tags: ["type/technology", "category/platform", "era/1995-1998"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "solaris-25"
category: "platform"
vendor: "Sun Microsystems"
era: "1995-1998"
lifecycle_at_study: "mature"
lifecycle_current: "obsolete"
occurrence_count: 1
prescience_max: 2.0
prescience_mean: 1.0
prescience_obs_count: 2
---

# Solaris 2.5

> Fine-tuned SMP: 3-8% CPU overhead vs 15-30% for NT; threaded I/O and networking; SMP scalability 92-97% efficiency; succeeded by Solaris 2.6, 7, 8...


## Top observations

- Solaris 2.5 fine-tuned for multiprocessor; threaded I/O and networking; constant query response time as dataset and user count grow; 3-8% CPU overhead (vs up to 30% for NT) `[ps=2]` — [[study-aberdeen-1996-sun-microsystems-decision-warehouse]]
- 92-97% SMP scalability (depending on RDBMS) as CPUs added; only 3-8% overhead per added CPU vs 15-20% for typical Unix SMP and up to 30% for NT Server `[ps=0]` — [[study-aberdeen-1996-sun-microsystems-decision-warehouse]]
