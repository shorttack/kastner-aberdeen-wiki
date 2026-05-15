---
title: "Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)"
slug: ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530
page_type: study
author: "Omri Serlin (FTSN newsletter)"
date: "1985-05-15"
study_type: industry-newsletter
subject_domain: "fault-tolerant-computing/transaction-processing-benchmarks"
methodology: "industry-newsletter-with-vendor-data"
importance: high
importance_rationale: "Omri Serlin's FTSN was the canonical cross-vendor neutral fault-tolerant industry newsletter of the era; this issue places Stratus, Tandem, and IBM TPF2 on the same ET1 yardstick — irreplaceable analytical context for the 1985-1986 Stratus benchmark corpus."
relevance: high
relevance_rationale: "Direct cross-reference between Tandem TXP (7.2-9.6 tps/CPU) and the Stratus result (1.0-1.1 tps/CPU per FTSN-32) clarifies Stratus's relative competitive position in 1985 and motivates Stratus's 1986 ET1 spec + benchmark corpus (study #7)."
prescience: medium
prescience_rationale: "Serlin's structured cost-per-tps + tps-per-CPU framing presaged the TPC-A/B/C standardized benchmarks (1988+) and remains the core measurement language of modern OLTP performance engineering."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 5
obs_count: 7
tags: [type/study, importance/high, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)

> Issue 33 of Omri Serlin's Fault-Tolerant Systems News (FTSN) newsletter, published May 15, 1985 by ITOM International (Los Altos, CA). Reports new Tandem ET1 benchmark data on a 4-processor TXP system, with TXP ranging 7.2-9.6 tps/CPU and (per Tandem) showing a significant cost-per-tps edge over IBM's TPF2. Three Guardian/Pathway/TMF software-stack configurations were tested ('V.2', 'V.5', 'V.6 new', 'V.6 old' with Guardian A06+DP1) producing 9.56 / 7.60 / 4.70 / 3.17 tps/processor and $33.7K / $39.2K / $58K / $80.6K cost-per-tps respectively. Database: 2M account records, 2,000 teller records, 200 branch records (1/5 the size of anon-et-al's Datamation specification). Tandem VP of Software Dennis McEvoy claims Tandem's V.2 and V.5 cost-per-tps is substantially lower than IBM TPF2 even though both are coded in COBOL (TPF2 mandates assembly), and that a 16-CPU TXP system can do 100 tps and a 10-system FOX network 1000 tps. The benchmark was run by Harald Sammer's 1000-tps group in Frankfurt. Notably, FTSN cross-references the Stratus result from FTSN-32 at 1.0-1.1 tps/CPU — making this newsletter a rare neutral cross-vendor 1985 ET1 data point that contextualizes Stratus's 1985-1986 TP1/ET1 claims (Batch 25 studies #5 and #7).

**Author:** Omri Serlin (FTSN newsletter) · **Date:** 1985-05-15 · **Type:** industry-newsletter
**Importance:** high — *Omri Serlin's FTSN was the canonical cross-vendor neutral fault-tolerant industry newsletter of the era; this issue places Stratus, Tandem, and IBM TPF2 on the same ET1 yardstick — irreplaceable analytical context for the 1985-1986 Stratus benchmark corpus.*
**Prescience:** medium — *Serlin's structured cost-per-tps + tps-per-CPU framing presaged the TPC-A/B/C standardized benchmarks (1988+) and remains the core measurement language of modern OLTP performance engineering.*

## Entities (9)

- [[datamation-magazine|Datamation magazine]]
- [[dennis-mcevoy-tandem|Dennis McEvoy]]
- [[ftsn-newsletter|Fault-Tolerant Systems News (FTSN)]]
- [[harald-sammer-tandem|Harald Sammer]]
- [[ibm|IBM Corporation]]
- [[itom-international|ITOM International Co.]]
- [[omri-serlin|Omri Serlin]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (5)

- [[et1-debit-credit|ET1 Debit-Credit Benchmark]]
- [[ibm-tpf2|IBM TPF2 (Transaction Processing Facility 2)]]
- [[tandem-fox-network|Tandem FOX Inter-System Network]]
- [[tandem-guardian-pathway-tmf|Tandem Guardian + Pathway + TMF Stack]]
- [[tandem-txp|Tandem TXP System]]

## Key observations (top 25)

- **1985** — TXP ET1 performance: 7.2-9.6 tps/CPU on 4-processor TXP; V.2 9.56 tps; V.5 7.60 tps; V.6 new 4.70 tps; V.6 old 3.17 tps
- **1985** — TXP cost per tps: $33.7K / $39.2K / $58K / $80.6K per tps for V.2 / V.5 / V.6 new / V.6 old
- **1985** — Stratus reported result: 1.0-1.1 tps/CPU (cross-reference from FTSN-32)
- **1985** — McEvoy 100-tps and 1000-tps thesis: 16-CPU TXP can do 100 tps; 10-system FOX network can do 'magic 1000 tps'
- **1985** — McEvoy IBM cost/TPS claim: Tandem V.2/V.5 cost/TPS substantially lower than IBM TPF2 in COBOL-vs-assembly comparison
- **1985** — Database scale: 2M account records, 2K teller records, 200 branch records (1/5 anon-et-al spec)
- **1985** — Sammer Tandem role: Harald Sammer led 1000-tps group in Frankfurt, W. Germany

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530' ORDER BY year_observed;
```

