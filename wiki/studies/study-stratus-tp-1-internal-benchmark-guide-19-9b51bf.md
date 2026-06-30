---
title: "Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)"
slug: "study-stratus-tp-1-internal-benchmark-guide-19-9b51bf"
page_type: "study"
tags: ["type/study", "collection/internal-engineering-document"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "stratus-tp-1-internal-benchmark-guide-19-9b51bf"
author: "Stratus Computer engineering (uncredited)"
date: "1983"
pub_year: 1983
type: "internal-engineering-document"
subject_domain: "fault-tolerant-OLTP-benchmarks"
methodology: "Stratus internal performance-measurement document defining the TP-1 model (Requester/Server with COBOL/TPF requester and PL/1 server, transactions initiated by delay interval, no screen I/O, duplicated servers, varied file sizes/types). Reports 1.5-2.9 tps results across small/large relative and indexed file configurations on non-duplexed Stratus systems, then closes with Stratus-vs-Tandem observations."
source_file: "TP-1-benchmark-guide-Stratus-1983-2.pdf"
license: "CC-BY-4.0"
importance: "medium"
relevance: "medium"
study_prescience_enum: "low"
prescience_3y_enum: "medium"
prescience_5y_enum: "medium"
prescience_max: 4.0
prescience_mean: 1.33
prescience_obs_count: 3
---

# Stratus 'TP-1 Performance Model' internal benchmark guide (1983, Stratus internal)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** medium — 3y Rule A: mean=3.20 over 5 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].
- **5-year verdict:** medium — 5y Rule A: mean=3.20 over 5 usable obs (0 prefiltered, 0 pending) -> medium [high>=3.5, medium>=2.0].

> Earliest Stratus internal performance document recovered in the corpus. Defines the TP-1 model and walks through small relative file (2.9 tps; 69% CPU; 18.0 disk I/O/sec), large relative file (2.3 tps; 94.7% CPU), and large indexed file configurations (1.5-1.8 tps depending on memory and server-queue topology). Key observations: cache utilization significantly impacts performance; performance is most affected by disk type/number/file size; multiple server copies greatly improve performance; server priority should exceed requester priority. The Stratus-vs-Tandem comparison section sits behind the TP-1 model definition. Predates the FTSN-32/FTSN-33 1985 Stratus 1.0-1.1 tps/CPU figures cited in Batch 25 — TP-1 is essentially Stratus's pre-ET1 internal predecessor benchmark.


_Published 1983, author **Stratus Computer engineering (uncredited)**, type **internal-engineering-document**._


## Top observations

- Requester (COBOL/TPF) + Server (PL/1) pattern; transactions on delay interval; no screen/comm I/O; duplicated servers; varied file types/sizes `[ps=4]`
- 2.9 `[ps=0]`
- 1.8 `[ps=0]`
- 2.3
- Cache utilization significant; disk type/count/file-size dominant; multiple server copies help; server priority > requester priority
