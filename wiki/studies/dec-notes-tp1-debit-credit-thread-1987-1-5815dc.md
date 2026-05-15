---
title: "DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987)"
slug: dec-notes-tp1-debit-credit-thread-1987-1-5815dc
page_type: study
author: "Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith)"
date: "1987-12-09"
study_type: internal-discussion-thread
subject_domain: "OLTP-benchmark-methodology-and-DBS-metrics"
methodology: "internal-engineering-NOTES-thread"
importance: medium
importance_rationale: "Captures the field-engineering and database-marketing debate over Debit-Credit interpretation at DEC in late 1987. Documents TP1 = Debit-Credit = Gray synonymy, naming conventions, and the explicit DEC concern about competitive benchmark abuse. Less foundational than the Kohler/Hsu guidelines memo (Study 1) but illustrates the broader cultural shift to formal metrics."
relevance: medium
relevance_rationale: "Kastner not named in this thread, but the discussion is the OLTP/DBS performance discourse he participated in as HPS::KASTNER. Provides voices from Database A/D (Kittell), DBS leadership (Smith), and field marketing (Saghagen, Rowlands, Mascall, Hammond) — the customer-facing context for the engineering work captured in the Kohler/Hsu guidelines."
prescience: medium
prescience_rationale: "Kittell's stereo-spec analogy ('unqualified TPS specs are worthless') exactly anticipates TPC's audit-and-disclosure requirement. The push for QUALIFIED metrics with explicit response-time, database size, and cost qualifiers anticipates TPC-A's full disclosure report."
license: CC-BY-4.0
tier: 2
entity_count: 12
tech_count: 4
obs_count: 11
tags: [type/study, importance/medium, prescience/medium, decade/1980s]
source_csv: master_studies.csv
---

# DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987)

> Internal DEC VAX Rdb/VMS NOTES file thread (Note 461) on the TP1 / Debit-Credit benchmark, captured December 1987. Thread initiated by Arild Saghagen (OSL09::ARILDS, Office & Infosystem Marketing) seeking RDB performance data for a finance-company sale where DEC and Wang were the final vendors and the customer asked about TP1 transaction rates against a 2x8550 cluster. Replies clarify TP1 = Debit-Credit = Gray benchmark (Rob Rowlands, BISTRO::ROWLANDS), point to internal Valbonne report TP_REPORT23.LN03 (HERON), warn that the spec leaves scope for 'artistic interpretation' (Tony Mascall, GYPSC::MASCALL). Charlie Hammond (SQM::HAMMOND, ZKO2-02) explains that TP1, Debit-Credit and Gray are all the same benchmark, lists ambiguities (95th/1-sec vs 2-sec, back-end vs terminal response, partitioning tricks). Richard Kittell (COOKIE::KITTELL, Database A/D) draws an analogy between unspecified TPS ratings and unspecified stereo frequency response — and forwards an April 1987 standardization draft by Kevin Smith (COOKIE::KSMITH) defining DBS Standard Metrics for FY87 and FY88: TPS (D/C, BATCH/END-TO-END, QUALIFIED/PEAK), $/TPS metrics (Host vs B/E System, Cost vs Price vs COO), database size metrics, and back-up rate metrics. Notes Rudy Downs hired as DBS Performance Manager. Document contemporaneous with the Kohler/Hsu Debit-Credit Guidelines memo and shows DEC's broader DBS group converging on standardized benchmark metrics — 8 months before TPC was founded.

**Author:** Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith) · **Date:** 1987-12-09 · **Type:** internal-discussion-thread
**Importance:** medium — *Captures the field-engineering and database-marketing debate over Debit-Credit interpretation at DEC in late 1987. Documents TP1 = Debit-Credit = Gray synonymy, naming conventions, and the explicit DEC concern about competitive benchmark abuse. Less foundational than the Kohler/Hsu guidelines memo (…*
**Prescience:** medium — *Kittell's stereo-spec analogy ('unqualified TPS specs are worthless') exactly anticipates TPC's audit-and-disclosure requirement. The push for QUALIFIED metrics with explicit response-time, database size, and cost qualifiers anticipates TPC-A's full disclosure report.*

## Entities (12)

- [[arild-saghagen|Arild Saghagen]]
- [[charlie-hammond|Charlie Hammond]]
- [[digital-equipment-corp|Digital Equipment Corporation (DEC)]]
- [[jim-gray|Jim Gray]]
- [[kevin-j-smith|Kevin J. Smith]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[richard-kittell|Richard S. Kittell]]
- [[rob-rowlands|Rob Rowlands]]
- [[rudy-downs|Rudy Downs]]
- [[tandem-computers|Tandem Computers]]
- [[tony-mascall|Tony Mascall]]
- [[wang-laboratories|Wang Laboratories]]

## Technologies (4)

- [[dbs-tps-metrics|DEC DBS TPS Metrics Standard]]
- [[debit-credit-benchmark|Debit-Credit Benchmark]]
- [[vax-8550|VAX 8550]]
- [[vax-rdb|VAX Rdb/VMS]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'dec-notes-tp1-debit-credit-thread-1987-1-5815dc' ORDER BY year_observed;
```

