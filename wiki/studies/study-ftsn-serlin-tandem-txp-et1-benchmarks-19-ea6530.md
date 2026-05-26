---
title: "Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)"
slug: "study-ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530"
page_type: "study"
tags: ["type/study", "collection/industry-newsletter"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "ftsn-serlin-tandem-txp-et1-benchmarks-19-ea6530"
author: "Omri Serlin (FTSN newsletter)"
date: "1985-05-15"
pub_year: 1985
type: "industry-newsletter"
subject_domain: "fault-tolerant-computing/transaction-processing-benchmarks"
methodology: "industry-newsletter-with-vendor-data"
source_file: "Serlin-FTSN-5-15-1985.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Omri Serlin FTSN-33: Tandem Reports TXP ET1 Benchmarks 7.2-9.6 tps/CPU; Cites Stratus 1.0-1.1 tps/CPU (May 15, 1985)

> Issue 33 of Omri Serlin's Fault-Tolerant Systems News (FTSN) newsletter, published May 15, 1985 by ITOM International (Los Altos, CA). Reports new Tandem ET1 benchmark data on a 4-processor TXP system, with TXP ranging 7.2-9.6 tps/CPU and (per Tandem) showing a significant cost-per-tps edge over IBM's TPF2. Three Guardian/Pathway/TMF software-stack configurations were tested ('V.2', 'V.5', 'V.6 new', 'V.6 old' with Guardian A06+DP1) producing 9.56 / 7.60 / 4.70 / 3.17 tps/processor and $33.7K / $39.2K / $58K / $80.6K cost-per-tps respectively. Database: 2M account records, 2,000 teller records, 200 branch records (1/5 the size of anon-et-al's Datamation specification). Tandem VP of Software Dennis McEvoy claims Tandem's V.2 and V.5 cost-per-tps is substantially lower than IBM TPF2 even though both are coded in COBOL (TPF2 mandates assembly), and that a 16-CPU TXP system can do 100 tps and a 10-system FOX network 1000 tps. The benchmark was run by Harald Sammer's 1000-tps group in Frankfurt. Notably, FTSN cross-references the Stratus result from FTSN-32 at 1.0-1.1 tps/CPU — making this newsletter a rare neutral cross-vendor 1985 ET1 data point that contextualizes Stratus's 1985-1986 TP1/ET1 claims (Batch 25 studies #5 and #7).


_Published 1985, author **Omri Serlin (FTSN newsletter)**, type **industry-newsletter**._


## Top observations

- 7.2-9.6 tps/CPU on 4-processor TXP; V.2 9.56 tps; V.5 7.60 tps; V.6 new 4.70 tps; V.6 old 3.17 tps
- $33.7K / $39.2K / $58K / $80.6K per tps for V.2 / V.5 / V.6 new / V.6 old
- 1.0-1.1 tps/CPU (cross-reference from FTSN-32)
- 16-CPU TXP can do 100 tps; 10-system FOX network can do 'magic 1000 tps'
- Tandem V.2/V.5 cost/TPS substantially lower than IBM TPF2 in COBOL-vs-assembly comparison
- 2M account records, 2K teller records, 200 branch records (1/5 anon-et-al spec)
- Harald Sammer led 1000-tps group in Frankfurt, W. Germany
