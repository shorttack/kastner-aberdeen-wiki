---
title: "Stratus 'The computer is down' ad reprints (Continuous Processing campaign, c.1984-1985)"
slug: stratus-computer-is-down-ad-reprints-c19-903ebf
page_type: study
author: "Stratus Computer marketing (Kastner-era; Kastner named in copy as direct contact)"
date: "1985-01-01"
study_type: advertising-collateral
subject_domain: "fault-tolerant-computing-marketing"
methodology: "advertising-content"
importance: high
importance_rationale: "Direct evidence of Kastner's role at Stratus: his name and direct phone number appear in a major national ad campaign. Captures the price/performance messaging that Stratus used to challenge IBM/DEC/HP and to differentiate from Tandem on hardware-vs-software fault tolerance. Foundational artifact for the Stratus chapter of Kastner's memoir."
relevance: medium
relevance_rationale: "The Continuous Processing concept (HW pair-and-spare) remains in production in modern Stratus systems. The competitive set (IBM 4381, HP 3000 68, DEC VAX) is obsolete but the price/performance benchmarking template is still industry-standard. The 'computer is down' concern translates to modern uptime SLAs (99.999%, 99.9999%)."
prescience: high
prescience_rationale: "The ad anticipates the criticality of always-on computing for commerce — the line 'when we become dependent on computers, we are at their mercy' preceded by decades the actual emergence of the always-on internet economy where minutes of downtime cost millions (e.g., Amazon ~$220K/minute, NYSE ~$1.4M/minute as of 2020s)."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 5
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Stratus 'The computer is down' ad reprints (Continuous Processing campaign, c.1984-1985)

> Compilation of Stratus 'The computer is down' magazine advertisements from the Continuous Processing campaign, circa 1984-1985 (cites Computerworld August 20, 1984 as source for relative price/performance index). The ads compare Stratus XA400 (relative performance 125, price $446,350, $/TPS $3,571) against IBM 4381 (perf 100, $707,897, $7,079), HP 3000 68 (perf 64, $437,754, $6,840), and DEC VAX-11/782 (perf 109, $656,889, $5,999). Targets brokers, bankers, manufacturers, and businessmen with the message that Stratus is designed not to fail vs. industry 98.5% reliability standard (which means failure once every two weeks). Lists Peter Kastner in Massachusetts at (617) 460-2192 (toll-free 1-800-752-4826) as the marketing contact — confirming Kastner's authorial role in the campaign during his Stratus employer era. Themes: 'Now that the world relies on computers it needs a computer it can rely on'; 'Continuous Processing'; positioning vs Tandem with hardware redundancy in chip technology.

**Author:** Stratus Computer marketing (Kastner-era; Kastner named in copy as direct contact) · **Date:** 1985-01-01 · **Type:** advertising-collateral
**Importance:** high — *Direct evidence of Kastner's role at Stratus: his name and direct phone number appear in a major national ad campaign. Captures the price/performance messaging that Stratus used to challenge IBM/DEC/HP and to differentiate from Tandem on hardware-vs-software fault tolerance. Foundational artifact fo…*
**Prescience:** high — *The ad anticipates the criticality of always-on computing for commerce — the line 'when we become dependent on computers, we are at their mercy' preceded by decades the actual emergence of the always-on internet economy where minutes of downtime cost millions (e.g., Amazon ~$220K/minute, NYSE ~$1.4M…*

## Entities (7)

- [[computerworld-magazine|Computerworld magazine]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (5)

- [[dec-vax-11-782|DEC VAX-11/782]]
- [[hp-3000-68|HP 3000 series 68]]
- [[ibm-4381|IBM 4381]]
- [[stratus-continuous-processing|Stratus Continuous Processing]]
- [[stratus-xa400|Stratus XA400]]

## Key observations (top 25)

- **1985** — Stratus XA400 list price: $446,350 — comparably configured (memory, disk, comm lines) plus fault tolerance INCLUDED
- **1985** — IBM 4381 list price: $707,897 — same comparable config; $/TPS $7,079 (highest in comparison)
- **1985** — HP 3000 series 68 list price: $437,754 — same comparable config; $/TPS $6,840
- **1985** — DEC VAX-11/782 list price: $656,889 — same comparable config; $/TPS $5,999
- **1985** — Stratus XA400 $/TPS: $3,571 per transaction-per-second — best in 4-vendor comparison; less than half of IBM/HP
- **1985** — Industry reliability standard critique: 98.5% reliability standard means computer goes down once every two weeks on statistical average — 'unthinkable for modern manufacturing'
- **1985** — Stratus reliability claim: 'Designed not to fail; not once every two weeks, or once every 200 weeks, or once every 2,000 weeks'
- **1985** — Direct named contact in national ad campaign: Ad copy reads: 'For information contact your local Stratus sales office, or call Peter Kastner in Massachusetts at (617) 460-2192 or toll-free at 1-800-752-4826'
- **1985** — Hardware redundancy cost approach: Stratus claim: hardware-based fault tolerance from chip-level redundancy adds 'a mere fraction to our cost, and absolutely nothing to your purchase price'
- **2025** — Continuous Processing longevity: Stratus's hardware fault-tolerant architecture shipped continuously from early 1980s into modern ftServer line and ztC Edge — among the longest-lived commercial fault-tolerant designs

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-computer-is-down-ad-reprints-c19-903ebf' ORDER BY year_observed;
```

