---
title: "Stratus Press Release — William Foster ACM Annual Conference Speech, 27 October 1982 (Kastner as media contact)"
slug: stratus-foster-acm-speech-pr-1982-16a134
page_type: study
author: "Stratus Computer (corporate communications — Kastner-era)"
date: "1982-10-18"
study_type: press-release
subject_domain: "fault-tolerant-computing-thought-leadership"
methodology: "corporate-document, expert-opinion"
importance: high
importance_rationale: "Primary-source Stratus PR document with Kastner explicitly listed as the press-contact for the company's CEO thought-leadership program. Combined with the Olivetti article ('communications director'), the CBN article ('manager of marketing development'), the 1984 InfoSystems quote ('manager of corporate business development'), and the 1987 CW article ('manager of marketing support programs'), this assembles a four-title evolution of Kastner's roles at Stratus 1981-1987. Foster's ACM keynote is a…"
relevance: high
relevance_rationale: "Foster's 'parallel processing as the building block' thesis perfectly anticipated the multi-core / GPU / massively-parallel-cloud era. The ACM keynote is one of the earliest formal industry articulations of the parallel-processing-as-the-future argument from a commercial-systems vendor."
prescience: high
prescience_rationale: "Foster's 1982 thesis — that the central processor would 'vanish' as parallel chips became the building block of high-performance computers, and that parallel processing would drive 10x-100x reliability improvements — was extraordinarily prescient. Multi-core CPUs, massively-parallel GPUs, distributed-systems-as-default cloud architectures, and cluster-based HA all validate the thesis."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 3
obs_count: 4
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Stratus Press Release — William Foster ACM Annual Conference Speech, 27 October 1982 (Kastner as media contact)

> Stratus Computer corporate press release dated 18 October 1982 announcing that Stratus President **William E. Foster** would address the **Association of Computing Machinery (ACM) Annual Conference in Dallas, Texas on October 27** as one of two featured speakers in the General Session. Foster's topic: **'New Computer Architectures: The Vanishing Central Processor.'** Conference theme: 'The Computer Industry: Solving or Creating Today's Problems' — ~40 technical sessions, ~2,000 attendees per ACM. Press release includes a substantial Foster speech excerpt: \"By using multiple 16 or 32 bit processor chips executing in parallel, major advances in price, performance, and reliability have been achieved. Older products rely on a single, custom CENTRAL processor which must share its time among many users and tasks. The only way to improve performance is to replace the central processor with a more powerful one. By contrast, systems using the latest high performance microprocessor chips can distribute work over many processor chips, and system performance can be easily enhanced by adding more chips.\" Foster concludes: \"like the vacuum tube, the transistor, and the gate array, the processor chip has become a high level building block in the most advanced high performance computers. In addition, parallel processing has allowed us to increase the reliability of on-line systems by 10 to 100 times, a level of reliability which is mandatory as society increases its dependence on computers.\"…

**Author:** Stratus Computer (corporate communications — Kastner-era) · **Date:** 1982-10-18 · **Type:** press-release
**Importance:** high — *Primary-source Stratus PR document with Kastner explicitly listed as the press-contact for the company's CEO thought-leadership program. Combined with the Olivetti article ('communications director'), the CBN article ('manager of marketing development'), the 1984 InfoSystems quote ('manager of corpo…*
**Prescience:** high — *Foster's 1982 thesis — that the central processor would 'vanish' as parallel chips became the building block of high-performance computers, and that parallel processing would drive 10x-100x reliability improvements — was extraordinarily prescient. Multi-core CPUs, massively-parallel GPUs, distribute…*

## Entities (7)

- [[acm|Association of Computing Machinery (ACM)]]
- [[data-general|Data General]]
- [[hewlett-packard|Hewlett-Packard]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[university-of-santa-clara|University of Santa Clara (now Santa Clara University)]]
- [[william-e-foster|William E. Foster]]

## Technologies (3)

- [[parallel-processing|Parallel processing (multi-chip)]]
- [[stratus-32|Stratus/32 Continuous Processing]]
- [[vanishing-central-processor|Vanishing central processor (Foster thesis)]]

## Key observations (top 25)

- **1982** — Foster ACM keynote thesis: By using multiple 16 or 32 bit processor chips executing in parallel, major advances in price, performance, and reliability have been achieved... systems using the latest high performance microprocessor chips can distribute work over many processor c…
- **1982** — Reliability via parallelism: Parallel processing has allowed us to increase the reliability of on-line systems by 10 to 100 times, a level of reliability which is mandatory as society increases its dependence on computers
- **1982** — Processor chip as building block: Like the vacuum tube, the transistor, and the gate array, the processor chip has become a high level building block in the most advanced high performance computers
- **1982** — Kastner press-contact role: Peter Kastner served as Stratus' named press contact for executive thought-leadership announcements (per this PR document)

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-foster-acm-speech-pr-1982-16a134' ORDER BY year_observed;
```

