---
title: "The Role of the Mainframe"
slug: nti-9-mainframe-role-1993-77fc40
page_type: study
author: "Peter S. Kastner, John Logan, Thomas Willmott"
date: "1993-05-01"
study_type: market-study
subject_domain: "mainframe-computing"
methodology: "industry-analysis, technology-assessment, vendor-profiling"
importance: high
importance_rationale: "Provides a contemporaneous, data-rich analysis of the pivotal mainframe-to-client-server transition from a leading IT research firm at the exact inflection point in 1993; cited specific financial metrics (Amdahl margins, IBM market cap) that illuminate the era."
relevance: medium
relevance_rationale: "The mainframe transition playbook (surround, rehost, green-field) remains relevant to modern legacy modernization; the specific IBM/Unisys competitive dynamics are historical."
prescience: high
prescience_rationale: "The prediction that IBM ES/9000 mainframes would fade from enterprises proved largely accurate; the green-field approach Aberdeen described became the dominant modernization strategy over the following decade."
license: CC-BY-4.0
tier: 1
entity_count: 19
tech_count: 14
obs_count: 29
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# The Role of the Mainframe

> Aberdeen Group objectively evaluates the declining role of the IBM ES/9000 mainframe in enterprise computing, contrasting it with Unisys A-Series growth. The study analyzes the paradox of increasing mainframe MIPS adoption alongside financial losses, software economics failures, and the blending of mainframe and midrange hardware capabilities. Aberdeen concludes that IBM mainframes will gradually be phased out and recommends either evolutionary (surround, rehost, rewrite) or green-field replacement strategies for IS executives.

**Author:** Peter S. Kastner, John Logan, Thomas Willmott · **Date:** 1993-05-01 · **Type:** market-study
**Importance:** high — *Provides a contemporaneous, data-rich analysis of the pivotal mainframe-to-client-server transition from a leading IT research firm at the exact inflection point in 1993; cited specific financial metrics (Amdahl margins, IBM market cap) that illuminate the era.*
**Prescience:** high — *The prediction that IBM ES/9000 mainframes would fade from enterprises proved largely accurate; the green-field approach Aberdeen described became the dominant modernization strategy over the following decade.*

## Entities (19)

- [[aberdeen-group|Aberdeen Group]]
- [[amdahl|Amdahl Corporation]]
- [[bull|Groupe Bull]]
- [[computer-associates|Computer Associates International]]
- [[fujitsu|Fujitsu]]
- [[hewlett-packard|Hewlett-Packard]]
- [[hitachi|Hitachi]]
- [[ibm|IBM]]
- [[ingres|Ingres (ASK Group)]]
- [[intel|Intel Corporation]]
- [[john-logan|John Logan]]
- [[microsoft|Microsoft Corporation]]
- [[ncr|NCR Corporation]]
- [[oracle|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[software-ag|Software AG]]
- [[sybase|Sybase, Inc.]]
- [[thomas-willmott|Thomas Willmott]]
- [[unisys|Unisys Corporation]]

## Technologies (14)

- [[cobol|COBOL]]
- [[db2|IBM DB2]]
- [[es9000|IBM ES/9000 (Enterprise System 9000)]]
- [[ibm-3270|IBM 3270 Terminals]]
- [[ibm-ad-cycle|IBM AD/Cycle]]
- [[ibm-rs6000|IBM RS/6000]]
- [[ibm-saa|IBM SAA (Systems Application Architecture)]]
- [[mvs|IBM MVS]]
- [[natural-4gl|Natural (4GL)]]
- [[pc-lan|PC LAN (Local Area Network)]]
- [[raid|RAID (Redundant Array of Inexpensive Disks)]]
- [[risc|RISC (Reduced Instruction Set Computing)]]
- [[tcm|TCM (Thermal Conduction Module) Processor Technology]]
- [[unisys-a-series|Unisys A-Series]]

## Key observations (top 25)

- **1992** — IBM mainframe MIPS shipped: More MIPS shipped in 1992 than any prior year — but least profitable year
- **1993** — IBM mainframe installed base decline rate: Declining 7% per year as datacenters consolidate
- **1993** — Amdahl gross margins: 30% vs 45% for PC-clone manufacturers
- **1993** — IBM market capitalization vs peers: IBM $30B; Microsoft $25B; Intel $25B; HP $20B
- **1993** — Application backlog on mainframe: 18-36 months for major new applications; 6-9 months for trivial report changes
- **1993** — IS spending as share of capital spending: Approximately 50% of all capital spending in many enterprises
- **1993** — ES/9000 technology advancement assessment: IBM did not advance ES/9000 as it could or should; MVS closed; TCM fell behind RISC; DB2 trails by several generations; no RAID upgrade
- **1992** — Unisys A-Series installation growth: 12% increase in installations for 1992
- **1993** — RISC vs mainframe TCM processor comparison: High-end RISC now has power of largest mainframe TCM processors; next-gen RISC will handily outperform
- **1993** — Midrange I/O bandwidth vs mainframe: HP and NCR midrange: 20+ MB/sec per channel; IBM ESCOM mainframe: 9.5 MB/sec
- **1990** — AD/Cycle outcome: Became a fiasco; IBM could not deliver promised services; killed mainframe ISV tools market
- **1993** — DB2 vs midrange RDBMS functionality: DB2 does not have functionality of Oracle, Ingres, Sybase midrange competitors
- **1987** — SAA client-server path: No clear client-server path despite 1987 promises; did not fulfill vision
- **1993** — Mainframe software license economics: Annual fees increasing with no corresponding productivity gain; installed base declining creates destructive cycle
- **1993** — Mainframe software harvesting trend: Computer Associates pricing models exemplify trend to harvest mainframe business
- **1993** — Mainframe IT staff transition barriers: Majority of data center professionals are IBM-mainframe trained; 12-18 months to retrain even best staff
- **1993** — Percentage of mainframe applications that are irrelevant: IS managers report up to 80% of mainframe applications are now irrelevant to how enterprises do business
- **1993** — PC vs mainframe spending: More money spent on PCs than on mainframe computers
- **1993** — Mainframe MIPS capacity growth despite decline: Cheap mainframe CPUs allow datacenters to add 20-30% capacity per year for existing back-office apps
- **1993** — Unisys A-Series openness features: SCAMP microprocessor, CCE software, rack-mount with industry-standard interfaces; Oracle, Unix server, PC LAN compatible
- **1993** — IBM mainframe phase-out timeline: IBM mainframes will be gradually phased out over next decade; probably irrelevant within 2-4 years
- **2003** — IBM mainframe phase-out — outcome: [UNVERIFIED]
- **1993** — Mainframe evolution strategies: Three evolutionary paths: Surround (mainframe as data repository), Rehost/Convert, Rewrite
- **1993** — Green-field strategy key barrier: Availability of qualified internal personnel is typically the gating factor; nearly all require outside professional services
- **1993** — Aberdeen conclusion on IBM mainframe role: Traditional IBM-defined mainframe role is merely maintenance in short term and irrelevant in long term

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'nti-9-mainframe-role-1993-77fc40' ORDER BY year_observed;
```

