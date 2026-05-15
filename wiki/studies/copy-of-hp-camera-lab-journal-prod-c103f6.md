---
title: "Caveat Emptor: HP's Consumer IT Leadership Needs New Focus on Consumers"
slug: copy-of-hp-camera-lab-journal-prod-c103f6
page_type: study
author: "Peter S. Kastner"
date: "2001-12-05"
study_type: case-analysis
subject_domain: "Consumer Electronics / Digital Cameras / Customer Support"
methodology: "First-person lab evaluation; real-product consumer experience testing with HP C315 digital camera"
importance: medium
importance_rationale: "Documents a real consumer product failure and Windows XP compatibility crisis; illustrative of the broader challenge for IT companies entering the consumer market in the early 2000s."
relevance: high
relevance_rationale: "Directly authored by Kastner under Aberdeen Lab Journal branding; primary source on HP consumer IT strategy evaluation."
prescience: high
prescience_rationale: "Warned HP would lose consumer market share without improved support and documentation; HP ultimately exited the consumer digital camera market, and consumer IT complexity remained a systemic industry challenge."
license: CC-BY-4.0
tier: 1
entity_count: 3
tech_count: 6
obs_count: 16
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Caveat Emptor: HP's Consumer IT Leadership Needs New Focus on Consumers

> Aberdeen Lab Journal dated December 5, 2001. Kastner recounts a first-person experience evaluating HP's C315 digital camera through installation under Windows ME and then Windows XP. The report identifies a critical undocumented incompatibility: the HP photo transfer software shipped with the camera interferes with Windows XP's native camera support, causing photo transfer failures. HP's support web site does not document the workaround (not installing the bundled software), and the support technician was unaware of the issue. Aberdeen concludes HP's consumer IT leadership strategy requires improved process, simpler documentation, and better support to prevent costly support calls and consumer defection.

**Author:** Peter S. Kastner · **Date:** 2001-12-05 · **Type:** case-analysis
**Importance:** medium — *Documents a real consumer product failure and Windows XP compatibility crisis; illustrative of the broader challenge for IT companies entering the consumer market in the early 2000s.*
**Prescience:** high — *Warned HP would lose consumer market share without improved support and documentation; HP ultimately exited the consumer digital camera market, and consumer IT complexity remained a systemic industry challenge.*

## Entities (3)

- [[aberdeen-group|Aberdeen Group / Aberdeen Laboratories]]
- [[hewlett-packard|Hewlett-Packard (HP)]]
- [[microsoft|Microsoft Corporation]]

## Technologies (6)

- [[acd-see-software|ACD See Image Display Software]]
- [[hp-c315-camera|HP C315 Digital Camera]]
- [[hp-photo-transfer-software|HP Photo Transfer Software (C315 Bundle)]]
- [[usb-camera-interface|USB Camera Interface / Windows XP Native Camera Support]]
- [[windows-me|Microsoft Windows ME]]
- [[windows-xp|Microsoft Windows XP]]

## Key observations (top 25)

- **2001** — HP Consumer IT Leadership Strategy: HP avowed strategy: lead market in consumer IT including access PCs, imaging, and new CE products
- **2001** — C315 Photo Quality: Consistently high quality photographs over 6 months of use
- **2001** — ACD See Missing DLL Under Windows ME: ACD See image display software had a missing .dll; unusable as primary image-handler
- **2001** — HP Photo Transfer Software XP Incompatibility: HP bundled photo transfer software interferes with Windows XP native camera support; causes photo transfer failure
- **2001** — In-Place Upgrade vs. Clean Install Caveat: HP web site claims XP native support but only works with clean install, not in-place upgrade
- **2001** — Support Call Cost vs. Camera Retail Price: A single tech support call costs HP more than the retail price of the camera
- **2001** — Support Call Duration: 45 minutes to resolve immediate problem; native XP support still not functioning afterward
- **2001** — Undocumented Workaround: Workaround (do not install bundled HP photo transfer software) not documented on HP support site
- **2001** — Consumer Defection Prediction: Dissatisfied consumers will go elsewhere for high-tech appliances; HP will lose consumer market share
- **2005** — HP Consumer Camera Market Exit: [UNVERIFIED]
- **2001** — HP Internal Process Fix: Fix internal process that facilitated lack-of-instructions fiasco
- **2001** — Consumer-Appropriate Documentation: Keep instructions simple and predictable; consumer pain tolerance lower than IT professionals
- **2001** — Simplify the Complex: Simplify the complex — easy to say, hard to do
- **2001** — Consumer Support Economics Law: Economic law of consumer electronics: cannot afford many support calls and still profit on mass-market products
- **2001** — HP Photography Web Site Quality: HP photography web site offers free photo publishing but is hard to find
- **2001** — Windows XP Compatibility Lesson for Consumers: Programs and devices working with prior Windows may not work under XP; always check support site for XP-specific updates

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'copy-of-hp-camera-lab-journal-prod-c103f6' ORDER BY year_observed;
```

