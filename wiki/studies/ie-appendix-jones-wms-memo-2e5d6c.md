---
title: "Availability of Client/Server WMS in 1994"
slug: ie-appendix-jones-wms-memo-2e5d6c
page_type: study
author: "Dr. Katherine Jones"
date: "1999-06-07"
study_type: expert-report
subject_domain: "warehouse-management-systems"
methodology: "document-review, field-research"
importance: medium
importance_rationale: "Provides expert testimony establishing the state of WMS technology in 1994, relevant to the IE v. Andersen litigation timeline."
relevance: low
relevance_rationale: "WMS technology has evolved dramatically since 1994; the specific technology landscape described is purely historical."
prescience: high
prescience_rationale: "Correctly identified Manhattan Associates as a WMS pioneer and accurately characterized the pre-client/server state of warehouse management technology in 1994."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 6
obs_count: 15
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Availability of Client/Server WMS in 1994

> Aberdeen Group ERP Research memo examining the availability of client/server warehouse management software (WMS) packages in the US marketplace in mid-1994. Concludes that no commercially available WMS was truly client/server-based at that time, with the first instance being Manhattan Associates PkMS in 1995.

**Author:** Dr. Katherine Jones · **Date:** 1999-06-07 · **Type:** expert-report
**Importance:** medium — *Provides expert testimony establishing the state of WMS technology in 1994, relevant to the IE v. Andersen litigation timeline.*
**Prescience:** high — *Correctly identified Manhattan Associates as a WMS pioneer and accurately characterized the pre-client/server state of warehouse management technology in 1994.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[catalyst-international|Catalyst International]]
- [[computer-associates|Computer Associates]]
- [[digital-equipment-corp|Digital Equipment Corporation]]
- [[jba-international|JBA International]]
- [[katherine-jones|Dr. Katherine Jones]]
- [[manhattan-associates|Manhattan Associates]]

## Technologies (6)

- [[boss-wms|Computer Associates BOSS]]
- [[client-server-wms|Client/Server WMS]]
- [[ibm-as400|IBM AS/400]]
- [[pkms|Manhattan Associates PkMS]]
- [[rf-handhelds|Radio-Frequency Handhelds]]
- [[vt-terminals|DEC VT 100/200 Terminals]]

## Key observations (top 25)

- **1994** — client-server-wms-availability: No commercially available client/server WMS existed in the US marketplace in mid-1994
- **1994** — warehouse-communication-modes: Two primary modes: RF handhelds and DEC VT 100/200 terminals in emulation mode — neither is client/server
- **1994** — aberdeen-client-server-definition: Application cleaved such that user-facing portion runs locally and business logic runs on another computer
- **1995** — first-client-server-wms: Manhattan Associates PkMS was the first commercially released client/server WMS — shipped 1995
- **1993** — catalyst-rf-technology: Catalyst used Windows and Vermont Views on RF handhelds in 1993-94 but did not offer true client/server
- **1996** — catalyst-gui-desktop: Catalyst shipped GUI desktop program in 1996 — first true client/server replacement for VT 200s
- **1994** — as400-warehouse-environment: AS/400s were used in a host-dumb terminal environment in 1994 for warehouse management
- **1991** — manhattan-first-installations: Manhattan Associates first installations were in 1991 on both Unix and the AS/400
- **1994** — jba-wms-capability: JBA had a host-dumb terminal warehouse management system on the AS/400 in 1994
- **1994** — boss-wms-capability: Computer Associates had BOSS warehouse management system on the AS/400 in 1994
- **1994** — technology-availability-vs-products: Client/server technology was available in 1994 and before but no commercial WMS products used it
- **1994** — terminal-emulation-usage: DEC VT 100/200 terminals in emulation mode were a standard warehouse communication method
- **1995** — manhattan-associates-viability: Manhattan Associates positioned as pioneer in client/server WMS with strong first-mover advantage
- **2025** — manhattan-associates-outcome: Manhattan Associates is now a $6B+ market cap NASDAQ-listed supply chain solutions leader
- **2005** — catalyst-outcome: Catalyst International was acquired by RedPrairie (now Blue Yonder) — failed to maintain independent position

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ie-appendix-jones-wms-memo-2e5d6c' ORDER BY year_observed;
```

