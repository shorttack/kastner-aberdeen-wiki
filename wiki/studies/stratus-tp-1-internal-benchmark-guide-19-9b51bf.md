---
title: "Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)"
slug: stratus-tp-1-internal-benchmark-guide-19-9b51bf
page_type: study
author: "Stratus Computer engineering (uncredited)"
date: "1983"
study_type: internal-engineering-document
subject_domain: "fault-tolerant-OLTP-benchmarks"
methodology: "Stratus internal performance-measurement document defining the TP-1 model (Requester/Server with COBOL/TPF requester and PL/1 server, transactions initiated by delay interval, no screen I/O, duplicated servers, varied file sizes/types). Reports 1.5-2.9 tps results across small/large relative and ind…"
importance: medium
importance_rationale: "Earliest Stratus internal benchmark document in the corpus; TP-1 model defines the Requester/Server pattern that underpins all later Stratus benchmark efforts."
relevance: medium
relevance_rationale: "TP-1 is the model PSK 1987-08 TopGun memo critiques relative to Tandem ET1 — bridges 1983 Stratus internal benchmark practice to the 1987 audited-benchmark era."
prescience: low
prescience_rationale: "TP-1 was a Stratus-internal model that did not survive the TPC standardization wave; its tps numbers are inputs to the later FTSN/EE-Times 'tps/CPU' industry frame but the model itself was superseded by ET1/TPC-A."
license: CC-BY-4.0
tier: 2
entity_count: 2
tech_count: 4
obs_count: 5
tags: [type/study, importance/medium, prescience/low, decade/1980s]
source_csv: master_studies.csv
---

# Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)

> Earliest Stratus internal performance document recovered in the corpus. Defines the TP-1 model and walks through small relative file (2.9 tps; 69% CPU; 18.0 disk I/O/sec), large relative file (2.3 tps; 94.7% CPU), and large indexed file configurations (1.5-1.8 tps depending on memory and server-queue topology). Key observations: cache utilization significantly impacts performance; performance is most affected by disk type/number/file size; multiple server copies greatly improve performance; server priority should exceed requester priority. The Stratus-vs-Tandem comparison section sits behind the TP-1 model definition. Predates the FTSN-32/FTSN-33 1985 Stratus 1.0-1.1 tps/CPU figures cited in Batch 25 — TP-1 is essentially Stratus's pre-ET1 internal predecessor benchmark.

**Author:** Stratus Computer engineering (uncredited) · **Date:** 1983 · **Type:** internal-engineering-document
**Importance:** medium — *Earliest Stratus internal benchmark document in the corpus; TP-1 model defines the Requester/Server pattern that underpins all later Stratus benchmark efforts.*
**Prescience:** low — *TP-1 was a Stratus-internal model that did not survive the TPC standardization wave; its tps numbers are inputs to the later FTSN/EE-Times 'tps/CPU' industry frame but the model itself was superseded by ET1/TPC-A.*

## Entities (2)

- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (4)

- [[debit-credit-benchmark|Debit-Credit benchmark (DC/ET1/TP1)]]
- [[fault-tolerant-architecture|Fault-tolerant systems architecture (general)]]
- [[stratus-vos|Stratus VOS (Virtual Operating System)]]
- [[tp1-benchmark|TP-1 performance model (Stratus internal)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-tp-1-internal-benchmark-guide-19-9b51bf' ORDER BY year_observed;
```

