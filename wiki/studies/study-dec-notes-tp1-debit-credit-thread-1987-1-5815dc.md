---
title: "DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987)"
slug: "study-dec-notes-tp1-debit-credit-thread-1987-1-5815dc"
page_type: "study"
tags: ["type/study", "collection/internal-discussion-thread"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "dec-notes-tp1-debit-credit-thread-1987-1-5815dc"
author: "Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith)"
date: "1987-12-09"
pub_year: 1987
type: "internal-discussion-thread"
subject_domain: "OLTP-benchmark-methodology-and-DBS-metrics"
methodology: "internal-engineering-NOTES-thread"
source_file: "DECtp-debit-credit-thoughts-1987-RDB-4.pdf"
license: "CC-BY-4.0"
importance: "medium"
relevance: "medium"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# DEC RDB NOTES File Thread: TP1/Debit-Credit Benchmark Discussion (Dec 1987)

> Internal DEC VAX Rdb/VMS NOTES file thread (Note 461) on the TP1 / Debit-Credit benchmark, captured December 1987. Thread initiated by Arild Saghagen (OSL09::ARILDS, Office & Infosystem Marketing) seeking RDB performance data for a finance-company sale where DEC and Wang were the final vendors and the customer asked about TP1 transaction rates against a 2x8550 cluster. Replies clarify TP1 = Debit-Credit = Gray benchmark (Rob Rowlands, BISTRO::ROWLANDS), point to internal Valbonne report TP_REPORT23.LN03 (HERON), warn that the spec leaves scope for 'artistic interpretation' (Tony Mascall, GYPSC::MASCALL). Charlie Hammond (SQM::HAMMOND, ZKO2-02) explains that TP1, Debit-Credit and Gray are all the same benchmark, lists ambiguities (95th/1-sec vs 2-sec, back-end vs terminal response, partitioning tricks). Richard Kittell (COOKIE::KITTELL, Database A/D) draws an analogy between unspecified TPS ratings and unspecified stereo frequency response — and forwards an April 1987 standardization draft by Kevin Smith (COOKIE::KSMITH) defining DBS Standard Metrics for FY87 and FY88: TPS (D/C, BATCH/END-TO-END, QUALIFIED/PEAK), $/TPS metrics (Host vs B/E System, Cost vs Price vs COO), database size metrics, and back-up rate metrics. Notes Rudy Downs hired as DBS Performance Manager. Document contemporaneous with the Kohler/Hsu Debit-Credit Guidelines memo and shows DEC's broader DBS group converging on standardized benchmark metrics — 8 months before TPC was founded.


_Published 1987, author **Multiple DEC engineers (Saghagen, Rowlands, Mascall, Hammond, Kittell, Smith)**, type **internal-discussion-thread**._


## Top observations

- TP1=Debit-Credit=Gray
- scope-for-artistic-interpretation
- TPS-D-C-end-to-end-qualified-and-peak
- TPS-MIP
- DBS-Performance-Manager
- finalist-vs-DEC-in-finance-sale
- anonymous-benchmark-author
- stating-TPS-without-percentile-and-time-is-like-stereo-without-frequency-response
- TPS-(benchmark-environment-characterization)
- offline-backup-gross-MB-per-sec
- physical-IOs-per-transaction
