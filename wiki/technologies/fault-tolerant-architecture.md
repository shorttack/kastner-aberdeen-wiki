---
title: "Dual-redundant fault-tolerant minicomputer architecture"
slug: "fault-tolerant-architecture"
page_type: "technology"
tags: ["type/technology", "category/computer-architecture", "era/1970s-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "fault-tolerant-architecture"
category: "computer-architecture"
vendor: "Stratus Computer"
era: "1970s-present"
lifecycle_at_study: "emerging"
lifecycle_current: "specialized-niche"
occurrence_count: 3
prescience_max: 5.0
prescience_mean: 2.33
prescience_obs_count: 9
---

# Dual-redundant fault-tolerant minicomputer architecture

> Four microprocessors arranged in two pairs with hardware comparator; failure handled without software awareness or lost clock cycles.


## Top observations

- Stratus relies on redundant hardware (dual CPU, dual memory, dual disks); Tandem achieves similar largely through software `[ps=5]` — [[study-boston-globe-stratus-xa2000-launch-1987--218ffd]]
- 'Red lights sell more than white papers.' You could argue against a benchmark. You could not argue against a machine still running after you just pulled a CPU board. `[ps=5]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Turned hardware redundancy into a maintenance model: 'the board that mails itself' — pull failed board while system runs, mail it back, no on-site engineer. `[ps=4]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- In mission-critical computing, downtime is not merely expensive. It is unacceptable. That is what Stratus proved, one pulled circuit board at a time. `[ps=4]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Five-nines uptime (99.999% — less than six minutes of downtime per year) was not a sales argument but an entry requirement for telecom contracts. `[ps=3]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Four physical microprocessors arranged in two pairs; hardware comparator checks results continuously; failed pair taken offline without losing a single clock cycle. `[ps=0]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Prospects invited to pull a CPU board from a running system during transaction processing; system kept running, red LED lit on failed component. `[ps=0]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- VP Hardware Gardner Hendrie could not reliably pull a board without crashing the system evening before public launch. `[ps=0]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Shiny Lexan plastic covers on circuit boards generated static electricity when pulled; carpet doused with water solved launch-day problem; ECO #1 replaced Lexan with cardboard. `[ps=0]` — [[study-volume-1-ch05-stratus-fault-tolerant-wars-1981-1987]]
- Fault-tolerant pair-of-Eclipses with hot standby for life-safety dispatch — [[study-adl-public-safety-911-cad-systems-1973-1979-b8a001]]
- ADLS pioneered municipal fault-tolerant CAD architecture in 1970s using paired-minicomputer redundancy — [[study-adl-public-safety-911-cad-systems-1973-1979-b8a001]]
