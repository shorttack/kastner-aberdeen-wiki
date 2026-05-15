---
title: "Timex RAMP Interview for Maxtor Project"
slug: timex-ramp-interview-for-maxtor-project-8c1b71
page_type: study
author: "Peter S. Kastner; David Hill"
date: "2003-04-16"
study_type: market-study
subject_domain: "enterprise-storage / consumer-manufacturing"
methodology: "face-to-face-interview, market-research, vendor-evaluation"
importance: high
importance_rationale: "Captures the 'management complexity veto' — the counter-intuitive finding that budget-constrained IT shops with the most inactive data are least likely to adopt storage tiering due to administrative overhead. The Timex interview is the canonical expression of this paradox in the RAMP dataset and directly shaped Kastner/Hill's market sizing and positioning recommendations for MaXLine."
relevance: high
relevance_rationale: "The administrative cost > hardware cost insight remains the central tension in enterprise storage: it drove the entire storage automation software market (ILM, HSM), converged infrastructure, hyperconverged (HCI), and cloud storage adoption. 'Transparency and significant cost savings would be the requirement to sell the Bobs of the world' is still the sales challenge for every storage tier vendor."
prescience: high
prescience_rationale: "Lutz's 2003 insight that disk costs are small compared to administrative costs was visionary: it predicted exactly why enterprise storage tiering adoption was slow until automation tools matured (2008-2015), why hyperconverged infrastructure (Nutanix, vSAN) succeeded by eliminating tier management, and why cloud object storage (S3) eventually absorbed inactive data without adding admin overhead."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 13
obs_count: 35
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Timex RAMP Interview for Maxtor Project

> Face-to-face RAMP interview with Robert (Bob) Lutz, Manager IT Operations at Timex (Middlebury CT), covering enterprise storage architecture, unwillingness to adopt additional storage tiers, and the critical insight that administrative costs dwarf hardware costs in storage decision-making. Timex had 6TB local / 10TB worldwide with 80% utilization and 80% inactive data, yet rated only 2/7 willingness to adopt low-cost disk. Lutz articulated that tight budgets and reduced headcount make adding a storage management tier more costly than the hardware savings — a foundational insight for the storage automation and hyperconverged infrastructure markets.

**Author:** Peter S. Kastner; David Hill · **Date:** 2003-04-16 · **Type:** market-study
**Importance:** high — *Captures the 'management complexity veto' — the counter-intuitive finding that budget-constrained IT shops with the most inactive data are least likely to adopt storage tiering due to administrative overhead. The Timex interview is the canonical expression of this paradox in the RAMP dataset and dir…*
**Prescience:** high — *Lutz's 2003 insight that disk costs are small compared to administrative costs was visionary: it predicted exactly why enterprise storage tiering adoption was slow until automation tools matured (2008-2015), why hyperconverged infrastructure (Nutanix, vSAN) succeeded by eliminating tier management,…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[compaq|Compaq]]
- [[david-hill|David Hill]]
- [[emc|EMC Corporation]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[maxtor-corporation|Maxtor Corporation]]
- [[microsoft|Microsoft]]
- [[oracle|Oracle]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[robert-lutz-timex|Robert Lutz (Bob Lutz)]]
- [[timex|Timex Group USA]]
- [[western-digital|Western Digital]]

## Technologies (13)

- [[active-project|Active Project (Imaging/Project Mgmt)]]
- [[ata-disk|ATA (IDE) Disk / Low-Cost Disk]]
- [[cad-cam|CAD/CAM Software / Imaging]]
- [[das|Direct-Attached Storage (DAS)]]
- [[fibre-channel|Fibre Channel (FC)]]
- [[hp-fc60|HP FC60 Disk Array]]
- [[hp-omniback|HP Omniback Backup Software]]
- [[microsoft-exchange|Microsoft Exchange]]
- [[oracle-financials|Oracle Financials (ERP)]]
- [[raid-5|RAID-5]]
- [[san|Storage Area Network (SAN)]]
- [[scsi-disk|SCSI Disk]]
- [[tape-library-robotic|HP Robotic Tape Library]]

## Key observations (top 25)

- **2003** — Company ownership and type: Privately held; consumer manufacturing (watches)
- **2003** — Total IT budget: $10M-$24M annual
- **2003** — CIO reporting line: Reports to CFO
- **2003** — Total storage — local (Middlebury): 6 TB
- **2003** — Total storage — worldwide: 10 TB
- **2003** — Storage utilization percentage: 80% in use
- **2003** — Expected storage growth (12 months) — Windows: 10% increase
- **2003** — Expected storage growth (12 months) — Unix: 10% increase
- **2003** — FC percentage of storage: 80% FC
- **2003** — SCSI percentage of storage: 20% SCSI
- **2003** — Percentage of inactive/seldom-written data (self-assessment): 80% inactive
- **2003** — Willingness: higher capacity + 50% cost reduction + slight availability reduction (7-point scale): 2 out of 7
- **2003** — Willingness: same capacity + 30% cost reduction + slight availability reduction (7-point scale): 2 out of 7
- **2003** — Likelihood to purchase low-cost disk in next 12 months (7-point scale): 2 out of 7 — unlikely
- **2003** — Primary barrier to low-cost disk adoption: Administrative management overhead exceeds disk cost savings
- **2003** — Relative cost: disk hardware vs. administration: Disk costs are small compared to administrative costs
- **2003** — Required conditions to sell tiered storage to 'the Bobs': Transparency and significant cost savings
- **2003** — Storage tiering adoption by SMB/cost-constrained shops without automation tools: Low without automation; management complexity will block adoption
- **2012** — Actual outcome: HCI/cloud as solution to tiering complexity: [UNVERIFIED]
- **2003** — IT staffing trend: Headcount being reduced; must reduce complexity
- **2003** — IT budget trend: Flat or declining; trying to reduce
- **2003** — Oracle Financials production database size: 1 TB
- **2003** — Oracle Financials storage architecture: HP FC60 DAS; array dedicated to application; FC interface
- **2003** — Microsoft Exchange email store size: ~1 TB
- **2003** — Email retention rationale: Cannot afford staff time to clean up; new disk cheaper than cleanup labor

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'timex-ramp-interview-for-maxtor-project-8c1b71' ORDER BY year_observed;
```

