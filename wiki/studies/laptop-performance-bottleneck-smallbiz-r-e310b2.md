---
title: "News Factor: The Laptop Performance Bottleneck (Smallbiztechnology.com excerpt)"
slug: laptop-performance-bottleneck-smallbiz-r-e310b2
page_type: study
author: "Ramon Ray (Smallbiztechnology.com blog), quoting NewsFactor (Peter Kastner, Aberdeen Group)"
date: "2002-11-18"
study_type: blog-reblog
subject_domain: "mobile-computing-hard-drives"
methodology: "excerpt-reblog, expert-opinion"
importance: low
importance_rationale: "Short reblog excerpt, not original reporting. Preserves a minor Kastner quote on mobile hard-drive performance but adds no independent analytical content. Valuable only as the archival record of an otherwise lost NewsFactor article."
relevance: medium
relevance_rationale: "Kastner's hard-drive-as-bottleneck observation was prescient: SSDs replaced HDDs as the primary laptop storage between 2012-2018 precisely because drive I/O remained the dominant responsiveness bottleneck even as CPUs and RAM scaled. The Ramon Ray 'ditch your desktop' prediction was vindicated by laptops overtaking desktops in US unit shipments in 2008."
prescience: high
prescience_rationale: "Ray's 'ditch your desktop' prediction (2002) came true ~2008 for US consumer shipments. Kastner's HDD-bottleneck point directly underpinned the 2012+ SSD transition."
license: CC-BY-4.0
tier: 1
entity_count: 5
tech_count: 3
obs_count: 6
tags: [type/study, importance/low, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# News Factor: The Laptop Performance Bottleneck (Smallbiztechnology.com excerpt)

> Smallbiztechnology.com (Ramon Ray) blog post (Nov 18, 2002) reblogging a NewsFactor article on laptop performance bottlenecks. The excerpt preserves a Peter Kastner quote — 'Hard drive speed counts for an awful lot of overall computing responsiveness' — attributed to Peter Kastner, executive vice president and chief research officer at Aberdeen Group. Ray's editorial note ('My spin: Get a good laptop, docking station, external monitor and a few more things... and then ditch your desktop') anticipates the laptop-as-primary-device trend by roughly 5-6 years. The Kastner quote is the surviving record of the underlying NewsFactor piece in this archive.

**Author:** Ramon Ray (Smallbiztechnology.com blog), quoting NewsFactor (Peter Kastner, Aberdeen Group) · **Date:** 2002-11-18 · **Type:** blog-reblog
**Importance:** low — *Short reblog excerpt, not original reporting. Preserves a minor Kastner quote on mobile hard-drive performance but adds no independent analytical content. Valuable only as the archival record of an otherwise lost NewsFactor article.*
**Prescience:** high — *Ray's 'ditch your desktop' prediction (2002) came true ~2008 for US consumer shipments. Kastner's HDD-bottleneck point directly underpinned the 2012+ SSD transition.*

## Entities (5)

- [[aberdeen-group|Aberdeen Group]]
- [[newsfactor-network|NewsFactor Network]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[ramon-ray-blogger|Ramon Ray]]
- [[smallbiztechnology-com|Smallbiztechnology.com]]

## Technologies (3)

- [[laptop-docking-station|Laptop docking station]]
- [[laptop-hdd|2.5-inch mobile hard disk drive]]
- [[laptop-pc|Laptop computer (notebook PC)]]

## Key observations (top 25)

- **2002** — Kastner HDD-as-bottleneck observation: 'Hard drive speed counts for an awful lot of overall computing responsiveness' — Peter Kastner, EVP and Chief Research Officer, Aberdeen Group, to NewsFactor
- **2002** — Ray laptop-replaces-desktop prediction: 'Get a good laptop, docking station, external monitor and a few more things... and then ditch your desktop'
- **2002** — Mobile disk drive design constraints: Designers of mobile disk drives face unique constraints: less space, less power, more shock-resistant than desktop HDDs; disk drives are the most noticeable lagging mobile component
- **2002** — Laptop as desktop replacement: Ray predicts users can ditch desktops once laptops + docking + external displays reach parity
- **2008** — US laptops overtake desktops in unit shipments: Q2 2008: US consumer notebook shipments exceeded desktop shipments for the first time (Gartner/IDC data). Laptop-as-primary-device pattern became mainstream ~5-6 years after Ray's prediction.
- **2015** — SSDs displace HDDs in laptops: By 2015 majority of new consumer laptops shipped with SSDs; by 2018 SSDs were the default. The shift was driven by exactly the I/O-bottleneck reasoning Kastner articulated in 2002.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'laptop-performance-bottleneck-smallbiz-r-e310b2' ORDER BY year_observed;
```

