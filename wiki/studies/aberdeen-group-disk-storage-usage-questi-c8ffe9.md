---
title: "Aberdeen Group Disk Storage Usage Questionnaire (v1)"
slug: aberdeen-group-disk-storage-usage-questi-c8ffe9
page_type: study
author: "Peter S. Kastner; David Hill (Aberdeen Group)"
date: "2003-02-01"
study_type: market-study
subject_domain: "enterprise-storage / disk-tiering / ILM"
methodology: "ramp-survey-design, telephone-survey, quantitative-research"
importance: high
importance_rationale: "First telephone survey instrument purpose-built to quantify enterprise ATA midline storage receptivity at scale (targeting 70 respondents), establishing the market validation methodology for the MaXLine product launch and providing a baseline measurement of enterprise storage architecture composition in early 2003."
relevance: medium
relevance_rationale: "Survey's measurement of cold-data percentage, backup window pain, and architecture breakdowns remain valid research design patterns for enterprise storage market studies. Specific thresholds are dated but the measurement framework endures."
prescience: high
prescience_rationale: "Survey design captured the exact market readiness indicators — percentage of cold/inactive online data, backup window overflows, willingness to trade availability for cost — that proved decisive for ATA/SATA midline adoption. The architecture breakout (DAS/SAN/NAS percentages) directly predicted the SAN consolidation trend and subsequent NAS growth that dominated enterprise storage through 2015."
license: CC-BY-4.0
tier: 1
entity_count: 6
tech_count: 12
obs_count: 27
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Aberdeen Group Disk Storage Usage Questionnaire (v1)

> First version of the Aberdeen Group telephone survey questionnaire developed for the Maxtor RAMP project measuring enterprise disk storage usage patterns and receptivity to a midline ATA storage tier. The 28-question instrument covers total disk capacity, utilization, architecture breakdown (internal DAS / external DAS / SAN / NAS), OS platform distribution, redundancy schemes (RAID / mirroring / snapshot / remote copy / tape), cold data identification, technology willingness assessment, backup window issues, and terminology awareness. A demographic section captures company scope, job titles, revenues, IT budget, CIO reporting structure, and industry vertical. This v1 instrument was subsequently refined into Maxtor Survey v2.

**Author:** Peter S. Kastner; David Hill (Aberdeen Group) · **Date:** 2003-02-01 · **Type:** market-study
**Importance:** high — *First telephone survey instrument purpose-built to quantify enterprise ATA midline storage receptivity at scale (targeting 70 respondents), establishing the market validation methodology for the MaXLine product launch and providing a baseline measurement of enterprise storage architecture compositio…*
**Prescience:** high — *Survey design captured the exact market readiness indicators — percentage of cold/inactive online data, backup window overflows, willingness to trade availability for cost — that proved decisive for ATA/SATA midline adoption. The architecture breakout (DAS/SAN/NAS percentages) directly predicted the…*

## Entities (6)

- [[aberdeen-group|Aberdeen Group]]
- [[david-hill|David Hill]]
- [[ibm|IBM]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[microsoft|Microsoft]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (12)

- [[ata-disk|ATA Hard Disk Drive]]
- [[das-external|External Direct-Attached Storage (DAS)]]
- [[das-internal|Internal Direct-Attached Storage (DAS)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[nas|Network Attached Storage (NAS)]]
- [[point-in-time-copy|Point-in-Time Copy / Snapshot]]
- [[raid-1|RAID 1 (Local Mirroring)]]
- [[raid-5|RAID 5 (Parity RAID)]]
- [[remote-mirroring|Remote Mirroring]]
- [[san|Storage Area Network (SAN)]]
- [[scsi-disk|SCSI Hard Disk Drive]]
- [[tape-automation|Tape Automation]]

## Key observations (top 25)

- **2003** — Instrument type: Telephone survey questionnaire — version 1 of RAMP quantitative instrument
- **2003** — Total storage capacity measurement: Q1: Total disk available (GB or TB) — server-only; PC/workstations excluded
- **2003** — Storage utilization measurement: Q2: Actual used storage (GB/TB); Q3: Maximum desired utilization (%)
- **2003** — Storage architecture breakout design: Q4: Four-way split — internal DAS / external DAS / SAN / NAS — measured in GB/TB
- **2003** — Storage growth rate measurement: Q5: Expected storage growth in next 12 months (%)
- **2003** — OS platform storage distribution: Q6: Storage mapped to OS — mainframe / Unix / Windows / Other (GB/TB per OS)
- **2003** — Redundancy scheme inventory — full taxonomy: Q7: Seven redundancy methods probed — RAID 5 / RAID 1 / indexed snapshot / full-volume snapshot / remote mirroring / remote copy / tape generations
- **2003** — Snapshot count as a proxy for data value: Q8: Number of on-disk copies (excluding parity RAID) plus tape copies — directly measures copy proliferation
- **2003** — Cold data percentage hypothesis: Q9: What percentage of online data does not need highest-availability storage? (closed transactions / old e-mail)
- **2003** — Midline acceptability binary choice: Q10: Would you accept (a) higher-capacity/slightly-less-performance or (b) same-size/similar-performance for cold data migration?
- **2003** — Disk capacity-speed gap as adoption context: Q11: Despite capacity growing faster than speed, will you still move to larger capacity disks?
- **2003** — Array sharing policy: Q12: Do you allow multiple applications to share an array?
- **2003** — Disk technology installed base — three-way breakdown: Q13: SCSI / FC / ATA percentage breakout with drive sizes and rotational speeds
- **2003** — Performance bottleneck locus identification: Q14: Do you have performance bottlenecks? If yes: CPU / storage / network. If no: expect future bottleneck?
- **2003** — SLA formalization measurement: Q15-Q18: Formal SLA existence / informal criteria / consequences of unavailability and performance degradation
- **2003** — Backup window as structural pain point: Q19-Q20: Backup window length (or online backup); specific issues — running out of window, job failure rate
- **2003** — Terminology awareness battery — three terms: Q21: nearline storage / active archiving / mezzanine storage — tested for awareness
- **2003** — Respondent scope — geographic reach classification: Q22: Local / Regional / National / International / Global — five-level geographic scope
- **2003** — Respondent job title — 9-category classification: Q23: CIO / CTO / IS Director-Manager / Technical Specialist / Hardware Engineer / Software Engineer / Programmer / Systems Analyst / DBA / Other
- **2003** — Revenue size — nine-band classification: Q25: Revenue from <$10M to >$5B in 9 bands
- **2003** — IT budget — nine-band classification: Q26: IT budget from <$1M to >$500M in 9 bands
- **2003** — CIO reporting line: Q27: CIO reports to CFO / President-CEO / Other
- **2003** — Industry vertical — 25-category classification: Q28: 25 industry verticals from Aerospace to Wholesale Trade
- **2003** — SAN as primary future architecture: SAN listed before NAS in architecture breakout — implicit ordering by enterprise primacy
- **2003** — SAN vs. NAS growth trajectory outcome: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-group-disk-storage-usage-questi-c8ffe9' ORDER BY year_observed;
```

