---
title: "The Outlook on AMD's Fusion Plans"
slug: amd-fusion-outlook-newsfactor-garrett-5859d3
page_type: study
author: "David Garrett, NewsFactor"
date: "2006-10-27"
study_type: news-article
subject_domain: "cpu-gpu-integration"
methodology: "product-analysis, analyst-commentary"
importance: medium
importance_rationale: "Documents analyst consensus at the AMD-ATI-acquisition closing moment (Oct 2006). Kastner's prediction that CPU+GPU integration would drive lower-cost PCs was the emerging thesis that became APU / Intel iGPU mainstream reality."
relevance: medium
relevance_rationale: "AMD Fusion products (APUs) shipped 2011 (Llano) and became the industry mainstream — Intel integrated graphics, Apple M-series SoCs, AMD Ryzen APUs, and mobile SoCs all fulfill Kastner's one-chip-computer prediction at scale. Still actively relevant to current SoC discussions."
prescience: high
prescience_rationale: "Kastner's one-chip-computer framing directly predicted the APU era: AMD Llano (2011), Intel Sandy Bridge with iGPU (2011), Apple A-series (iPhone SoCs), Apple M1 (2020), and mobile Snapdragon/Exynos all integrate CPU+GPU on one die. The 'fewer chips on the motherboard' cost argument became the dominant logic of PC motherboard design from 2011 onward. Kastner's $200-PC caveat was also correct — AMD Fusion enabled lower-cost PCs but not a dramatic bottom floor; sub-$200 x86 PCs remained niche."
license: CC-BY-4.0
tier: 1
entity_count: 10
tech_count: 4
obs_count: 7
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# The Outlook on AMD's Fusion Plans

> NewsFactor article (Oct 27 2006, David Garrett) on AMD's Fusion program announced the week AMD closed its $5.4B ATI acquisition. Fusion would combine AMD CPUs with ATI GPUs in a single unified processor, targeted for late 2007 / early 2008. Peter Kastner, VP and research director for information technology at Aberdeen Group, frames Fusion as enabling 'a one-chip computer that contains the functions that in the past have been in the chipset and the processor,' allowing 'a much less expensive PC to be made, because you'd have fewer chips to put on the motherboard.' Kastner caveats: 'I don't see this as moving to $200 PCs.' Samir Bhavnani of Current Analysis emphasizes the power-efficiency angle and Windows Vista Aero implications. Ad-sidebar date stamps indicate this 2006 article was captured in June 2009 during the CloudAve/Palm Pre era.

**Author:** David Garrett, NewsFactor · **Date:** 2006-10-27 · **Type:** news-article
**Importance:** medium — *Documents analyst consensus at the AMD-ATI-acquisition closing moment (Oct 2006). Kastner's prediction that CPU+GPU integration would drive lower-cost PCs was the emerging thesis that became APU / Intel iGPU mainstream reality.*
**Prescience:** high — *Kastner's one-chip-computer framing directly predicted the APU era: AMD Llano (2011), Intel Sandy Bridge with iGPU (2011), Apple A-series (iPhone SoCs), Apple M1 (2020), and mobile Snapdragon/Exynos all integrate CPU+GPU on one die. The 'fewer chips on the motherboard' cost argument became the domin…*

## Entities (10)

- [[aberdeen-group|Aberdeen Group]]
- [[amd|Advanced Micro Devices]]
- [[ati-technologies|ATI Technologies Inc.]]
- [[current-analysis|Current Analysis]]
- [[david-garrett-newsfactor|David Garrett]]
- [[intel-corp|Intel Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[newsfactor-network|NewsFactor Network]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[samir-bhavnani-current|Samir Bhavnani]]

## Technologies (4)

- [[amd-cpu|AMD x86 CPU]]
- [[amd-fusion-apu|AMD Fusion (later AMD APU)]]
- [[ati-radeon-gpu|ATI Radeon GPU]]
- [[windows-vista|Microsoft Windows Vista (with Aero)]]

## Key observations (top 25)

- **2006** — Kastner one-chip-computer framing: 'AMD with ATI can create a one-chip computer that contains the functions that in the past have been in the chipset and the processor. That would allow a much less expensive PC to be made, because you'd have fewer chips to put on the motherboard.' — P…
- **2006** — Kastner $200 PC caveat: 'I don't see this as moving to $200 PCs' — Kastner tempering expectations that Fusion would radically collapse PC prices
- **2006** — Bhavnani power-efficiency framing: 'One of the biggest benefits to combining the CPU and GPU on a single chip is not only better overall system performance, but, importantly, more energy efficiency' — Samir Bhavnani, Current Analysis
- **2006** — AMD-ATI acquisition closes: AMD completed $5.4B acquisition of ATI Technologies in the week prior to article (Oct 24 2006 close); Fusion program announced immediately post-close
- **2006** — Fusion debut timeline: Fusion products expected to debut in late 2007 or early 2008 according to AMD
- **2011** — AMD Llano ships as first APU: AMD Llano (A-series) shipped June 2011 as the first AMD Fusion APU product, integrating Phenom II K10 CPU cores with Radeon HD 6000-series GPU on the same die — approximately 3 years after AMD's original late-2007/early-2008 target
- **2020** — One-chip-computer becomes industry default: By 2020 the one-chip-computer model (CPU+GPU on one die) was industry-default: Apple M1 SoC (2020), Intel Tiger Lake iGPU, AMD Ryzen APUs, and every smartphone SoC. Kastner's 2006 prediction was fully validated and became the dominant PC architecture…

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'amd-fusion-outlook-newsfactor-garrett-5859d3' ORDER BY year_observed;
```

