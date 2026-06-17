---
title: "DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988)"
slug: "study-dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e"
page_type: "study"
tags: ["type/study", "collection/internal-engineering-memo"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "dec-zahavi-debit-credit-vaxclusters-1988-1a9e2e"
author: "Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI)"
date: "1988-03-04"
pub_year: 1988
type: "internal-engineering-memo"
subject_domain: "VAXcluster-OLTP-architecture"
methodology: "engineering-analysis-memo"
source_file: "DECtp-on-VAXclusters-thoughts-1988-03-5.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_max: 0.0
prescience_mean: 0.0
prescience_obs_count: 7
---

# DEC Zahavi Memo: Debit-Credit Benchmark on VAXclusters (March 1988)

> Internal Digital Equipment Corporation interoffice memorandum dated 4-March-1988 by Bill Zahavi (TP Systems Performance Analysis, MR01-1/A65, DTN 297-7795, HYPER::BZAHAVI) addressed to @DC_VAXCLUSTER and @GROUP, on implementing the Debit-Credit benchmark on VAXclusters. Identifies the Distributed Lock Manager (DLM) as the major obstacle: only one cluster member owns locks for a given file, and the Debit-Credit specification's requirement that 15% of teller activity address other-branch accounts forces inter-node CI bus traffic. Distinguishes flat-file (RMS, Hash) from formal-database (DBMS, Rdb) implementations. Discusses partitioning strategies (cluster-member-A owns files-A, etc.) and the asymmetric statistics: 7.5% of cross-branch traffic lands on a different cluster member's locks for a 2-member cluster. Acknowledges that DECintact works only with flat files (RMS, Hash) while ACMS works best with DBMS and Rdb. Proposes that without 2-Phase Commit (2PC), only certain types of applications can be distributed using formal databases — explicitly referencing Phil Bernstein's prior memo. Closes by calling for cross-functional cooperation between TP, Databases, and VMS groups for both short and long-term solutions, and asks the document be treated as a 'living document.' Direct technical companion to the Kohler/Hsu guidelines (Study 1) and the broader DEC OLTP performance-engineering corpus.


_Published 1988, author **Bill Zahavi, DEC TP Systems Performance Analysis (HYPER::BZAHAVI)**, type **internal-engineering-memo**._


## Top observations

- major-obstacle-for-VAXcluster-Debit-Credit `[ps=0]`
- 15 `[ps=0]`
- 7.5 `[ps=0]`
- flat-files-only-RMS-Hash `[ps=0]`
- excluded-from-Style-3 `[ps=0]`
- TP-Databases-VMS `[ps=0]`
- HYPER-BZAHAVI-MRO1-1-A65 `[ps=0]`
- not-available-in-DEC-stack
