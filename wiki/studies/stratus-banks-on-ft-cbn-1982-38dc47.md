---
title: "Stratus Banks on Fault-Tolerant Systems' Success — Computer Business News, 7 June 1982 (PSK extensively quoted)"
slug: stratus-banks-on-ft-cbn-1982-38dc47
page_type: study
author: "Peter Bochner (Computer Business News)"
date: "1982-06-07"
study_type: press-article
subject_domain: "fault-tolerant-computing-strategy-and-channels"
methodology: "industry-analysis, expert-opinion, competitive-profiling"
importance: high
importance_rationale: "Most quote-rich Kastner press appearance in this batch — captures his strategic framing of the FT market, Stratus' channel strategy, the Olivetti OEM agreement (potential $40M by 1985), the architectural approach (Motorola-68000 paired-CPU, paired-board self-checking), the maintenance-pricing innovation (7% vs 10-12%), and explicit market predictions for 1983 and 1986. Also documents Kastner's pre-Stratus background at Arthur D. Little — a key biographical fact."
relevance: medium
relevance_rationale: "OEM channel strategy and software-house ecosystem patterns remain durable. Specific product/competitor details are historical."
prescience: high
prescience_rationale: "Kastner's June 1982 prediction that 'by 1986, all broad-based computer companies will have to offer fault-tolerant systems' was largely correct: by 1986-1988 IBM (System/88 via Stratus OEM 1986), DEC (DECtp), HP (3000-MPE high-availability), AT&T (3B20D), Unisys, and Bull all had FT/HA offerings. His 'half dozen or more shipping by end of 1983' came true (Tandem, Stratus, August, Synapse, Auragen, Sequoia, Tolerant, AT&T)."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 9
obs_count: 9
tags: [type/study, importance/high, prescience/high, decade/1980s]
source_csv: master_studies.csv
---

# Stratus Banks on Fault-Tolerant Systems' Success — Computer Business News, 7 June 1982 (PSK extensively quoted)

> Computer Business News feature article from CBN's 'CBN Visit' series in which staff writer Peter Bochner profiled Stratus Computer at its Natick MA headquarters with extensive in-person quotes from **Peter Kastner, manager of marketing development**. Article documents Stratus' channel strategy (Fortune 1000 direct + OEM + software-house agreements with discounts but no purchase requirement), the recently-signed Olivetti OEM agreement (England/France/Italy distribution; potentially $40M by 1985), early applications software (Tranpro transaction processor, Forms Management System, 3270 Terminal Support, 3270 Emulator, X.25 Networking, Fortran 77, Pascal) and competitive positioning. Kastner predicts: \"By 1986, all [broad-based] computer companies will have to offer fault-tolerant systems\" and \"at least a half dozen or more will be shipping by the end of 1983.\" He explains the four-Motorola-68000 paired-CPU architecture, Stratalink networking, the high-level language software approach (only several thousand lines of code; portable across CPU generations), 7%/year vs 10-12% industry-standard maintenance pricing thanks to remote diagnostics, and centralized-storage efficiencies that may partially reverse the decentralization trend. Kastner (introduced as 'a former analyst at Arthur D. Little') frames the FT market as 'blossoming from a niche market to a cross market' as more work goes online and the cost of downtime rises. Article also captures DG President Edson de Castro's comme…

**Author:** Peter Bochner (Computer Business News) · **Date:** 1982-06-07 · **Type:** press-article
**Importance:** high — *Most quote-rich Kastner press appearance in this batch — captures his strategic framing of the FT market, Stratus' channel strategy, the Olivetti OEM agreement (potential $40M by 1985), the architectural approach (Motorola-68000 paired-CPU, paired-board self-checking), the maintenance-pricing innova…*
**Prescience:** high — *Kastner's June 1982 prediction that 'by 1986, all broad-based computer companies will have to offer fault-tolerant systems' was largely correct: by 1986-1988 IBM (System/88 via Stratus OEM 1986), DEC (DECtp), HP (3000-MPE high-availability), AT&T (3B20D), Unisys, and Bull all had FT/HA offerings. Hi…*

## Entities (9)

- [[arthur-d-little|Arthur D. Little, Inc.]]
- [[data-general|Data General]]
- [[edson-de-castro|Edson de Castro]]
- [[ibm-4341|IBM 4341 Model 1]]
- [[olivetti|Ing. C. Olivetti & Co.]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[prime-computer|Prime Computer]]
- [[stratus-computer|Stratus Computer]]
- [[tandem-computers|Tandem Computers]]

## Technologies (9)

- [[forms-management-system-stratus|Stratus Forms Management System]]
- [[motorola-68000|Motorola 68000]]
- [[remote-diagnostics|Remote diagnostics (hardware + software)]]
- [[stratalink|Stratalink]]
- [[stratus-3270-emulator|Stratus 3270 Emulator]]
- [[stratus-3270-terminal-support|Stratus 3270 Terminal Support]]
- [[stratus-continuous-processing|Stratus Continuous Processing]]
- [[tranpro|Tranpro]]
- [[x25-networking|X.25 Networking (Stratus implementation)]]

## Key observations (top 25)

- **1982** — Stratus channel strategy: End-user, software-house, and two-year OEM contracts; software houses get fee per system sale and discount but no buy requirement; OEMs are 'first point of contact for customer whose computer has gone down'
- **1982** — Olivetti OEM agreement: Olivetti to distribute Stratus products in England/France/Italy; OEM-integration agreement; potential $40M by 1985
- **1982** — FT-market broad adoption by 1986: By 1986, all [broad-based] computer companies will have to offer fault-tolerant systems
- **1982** — FT shipments by end of 1983: At least a half dozen or more FT vendors will be shipping by the end of 1983
- **1982** — Stratus architecture: CPU boards use four 68000 chips paired off (OS + user); high-level language for OS keeps code small (several thousand lines) and CPU-portable via code-generator changes; pair-of-pair self-checking
- **1982** — Stratus maintenance pricing: 7% per year (vs industry standard of 10-12%) thanks to remote diagnostics + customer-replaceable boards delivered by cab
- **1982** — Stratus pricing positioning: Under-$200,000; positioned vs Prime 750, DEC VAX 11/750, and IBM 4341 Model 1 (against 32-bit minis on price); not directly going after Tandem on price/performance
- **1982** — FT market evolution: Fault-tolerant market is blossoming from a niche market to a cross market; as more work goes on-line, computers get closer to the heart of business operations and the cost of downtime goes up
- **1982** — Kastner pre-Stratus background: Kastner was a former analyst at Arthur D. Little prior to Stratus

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'stratus-banks-on-ft-cbn-1982-38dc47' ORDER BY year_observed;
```

