---
title: "A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988)"
slug: dec-primer-comparing-debit-credit-tests--c30cfa
page_type: study
author: "Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs"
date: "1988-01-01"
study_type: internal-competitive-marketing-paper
subject_domain: "OLTP-benchmark-vendor-comparison"
methodology: "competitive-analysis-paper"
importance: high
importance_rationale: "Kastner-authored DEC competitive-marketing primer — direct primary source from his DEC employer-era. Establishes his command of OLTP benchmark methodology and competitive analysis years before founding Aberdeen Group. Encodes the analytical voice and rigor that would later define his Aberdeen TPC-A audit and analyst practice."
relevance: high
relevance_rationale: "Concrete artifact of Kastner's DEC competitive-marketing role. References Style 1/2/3 framework which only makes sense in the context of the Kohler/Hsu engineering guidelines and Zahavi VAXcluster memo. Serves as Kastner's outward-facing competitive narrative built on the inward-facing engineering memos (Studies 1-3)."
prescience: high
prescience_rationale: "Kastner's per-vendor critique structure — citing each vendor's specific non-conformance points — directly anticipated TPC-A/TPC-C full-disclosure audit reports. His insistence on apples-to-apples comparison (Style 3 vs. competitors' equivalent setup) prefigures the standardized TPC executive summary format. The Stratus journaling-throttle critique (15-17 tps cap) presaged the broader industry recognition that fault-tolerance must be designed for journaled throughput, not just cache speed."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 10
obs_count: 11
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# A Primer on Comparing Debit Credit Tests (Kastner, DEC CSG, 1988)

> Internal Digital Equipment Corporation Corporate Systems Group competitive marketing paper authored by Peter S. Kastner (Competitive Marketing Programs, PDM1-2(E1), DTN 291-0364) circa 1988. Provides DEC sales and marketing teams with a primer on interpreting and comparing Debit-Credit benchmark results across vendors (IBM, Tandem, Stratus, System/3X). Defines DEC's three styles of Debit-Credit: Style 1 (fully qualified, all presentation services in SUT — DEC's most rigorous; not directly comparable to competitors), Style 2 (forms/character offloaded to front-end VAX, cost included in COO), and Style 3 (MicroVAX or intelligent controllers in branches — recommended for vendor comparison since no other vendor tests presentation-services costs). Critiques IBM (RAMP-C obscures comparison; OneKay 1000-tps benchmark unfairly extrapolated to 750 Debit-Credit tps under IMS Fastpath), Tandem (TopGun March 1987: 90%/2-sec instead of 95%/1-sec, only 1000 tellers per 100 tps instead of 10,000, partitioned files, NonStop SQL relative-record-key extension), and Stratus (ET-1 ≠ Debit-Credit; no journaling; single-threaded logging caps at 15-17 tps; aggressive caching of account file). Provides DEC-eye estimates: Stratus Model 120 ≈ less than 8.5 Style-1 Debit-Credit tps. Notes Tandem reports 2.5 tps/processor on CLX to 6.5 tps/processor on VLX using TopGun. States Style 1 presentation services consume 40% of VUPS on an 8700. Document signed Peter S. Kastner, CSG Competitive Marketing Progra…

**Author:** Peter S. Kastner — DEC Corporate Systems Group, Competitive Marketing Programs · **Date:** 1988-01-01 · **Type:** internal-competitive-marketing-paper
**Importance:** high — *Kastner-authored DEC competitive-marketing primer — direct primary source from his DEC employer-era. Establishes his command of OLTP benchmark methodology and competitive analysis years before founding Aberdeen Group. Encodes the analytical voice and rigor that would later define his Aberdeen TPC-A…*
**Prescience:** high — *Kastner's per-vendor critique structure — citing each vendor's specific non-conformance points — directly anticipated TPC-A/TPC-C full-disclosure audit reports. His insistence on apples-to-apples comparison (Style 3 vs. competitors' equivalent setup) prefigures the standardized TPC executive summary…*

## Entities (6)

- [[dec-corporate-systems-group|DEC Corporate Systems Group (CSG)]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[ibm|IBM Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (10)

- [[debit-credit-benchmark|Debit-Credit Benchmark]]
- [[ibm-onekay-benchmark|IBM OneKay 1000-tps Benchmark (1987)]]
- [[ibm-system-88|IBM System/88]]
- [[ims-fastpath|IMS Fastpath]]
- [[nonstop-sql|Tandem NonStop SQL]]
- [[ramp-c-benchmark|RAMP-C]]
- [[stratus-et1-benchmark|Stratus ET-1]]
- [[stratus-model-120|Stratus Model 120]]
- [[tandem-topgun-benchmark|Tandem TopGun (March 1987)]]
- [[vax-8700|VAX 8700]]

## Key observations (top 25)

- **1988** — definition: fully-qualified-all-presentation-services-in-SUT
- **1988** — recommendation: use-Style-3-for-vendor-comparison
- **1988** — presentation_services_pct_vups: 40
- **1987** — response_time_spec: 90pct-2sec
- **1987** — tellers_simulated: 1000-per-100-tps
- **1988** — kastner_estimate_tps: less-than-8.5
- **1988** — journaling_throughput_tps: 15-17
- **1987** — tps_per_processor_clx: 2.5
- **1987** — tps_per_processor_vlx: 6.5
- **1988** — test_constraint: 70-pct-cpu-utilization-in-house-rule
- **1988** — role: DEC-CSG-Competitive-Marketing-Programs

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dec-primer-comparing-debit-credit-tests--c30cfa' ORDER BY year_observed;
```

