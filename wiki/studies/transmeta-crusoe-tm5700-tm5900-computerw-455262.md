---
title: "Transmeta unveils smaller microprocessors (Crusoe TM5700/TM5900 launch)"
slug: transmeta-crusoe-tm5700-tm5900-computerw-455262
page_type: study
author: "Gillian Law"
date: "2004-01-05"
study_type: news-article
subject_domain: "low-power-x86-Transmeta-Crusoe-embedded-2004"
methodology: "news-reporting, product-launch-coverage"
importance: medium
importance_rationale: "Captures Transmeta's strategic pivot toward embedded/size-constrained markets after desktop/notebook failure, and Kastner's prescient performance critique that presaged Transmeta's 2009 dissolution."
relevance: medium
relevance_rationale: "Historical record of an important low-power-x86 pioneer; some design concepts (code-morphing, low-TDP x86) foreshadowed Intel Atom and ARM-based laptops."
prescience: high
prescience_rationale: "Kastner's 'not good enough for many of today's applications' assessment and 'customer concerns over performance' framing accurately predicted Transmeta's market trajectory — company exited processor business 2005, sold IP and ceased operating by 2009. The performance-deficit thesis fully validated."
license: CC-BY-4.0
tier: 1
entity_count: 7
tech_count: 10
obs_count: 8
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Transmeta unveils smaller microprocessors (Crusoe TM5700/TM5900 launch)

> IDG News Service report (via Computerworld) on Transmeta's launch of the Crusoe TM5700 and TM5900 x86-compatible processors at 1 GHz in a 21mm-by-21mm package — half the size of the TM5800 — targeting set-top boxes, thin clients, blade servers, portable consumer products. 512KB (TM5900) or 256KB (TM5700) L2 cache, 64-bit DDR SDRAM controller, 32-bit PCI controller, integrated Northbridge. Kastner (Aberdeen EVP/CRO) flags ongoing TM5800 performance complaints (HP TC100 tablet example): 'not been good enough for many of today's applications.'

**Author:** Gillian Law · **Date:** 2004-01-05 · **Type:** news-article
**Importance:** medium — *Captures Transmeta's strategic pivot toward embedded/size-constrained markets after desktop/notebook failure, and Kastner's prescient performance critique that presaged Transmeta's 2009 dissolution.*
**Prescience:** high — *Kastner's 'not good enough for many of today's applications' assessment and 'customer concerns over performance' framing accurately predicted Transmeta's market trajectory — company exited processor business 2005, sold IP and ceased operating by 2009. The performance-deficit thesis fully validated.*

## Entities (7)

- [[aberdeen-group|Aberdeen Group]]
- [[computerworld|Computerworld (US)]]
- [[gillian-law-idg|Gillian Law]]
- [[hewlett-packard|Hewlett-Packard]]
- [[idg-news-service|IDG News Service]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[transmeta-corp|Transmeta Corporation]]

## Technologies (10)

- [[blade-server-2004|Blade server (2004-era)]]
- [[code-morphing-software|Transmeta Code Morphing Software]]
- [[ddr-sdram-64bit|64-bit DDR SDRAM memory controller]]
- [[pci-bus-32bit|32-bit PCI controller]]
- [[set-top-box-embedded|Set-top box / embedded computing]]
- [[thin-client-computing|Thin client computing]]
- [[transmeta-crusoe-tm5700|Transmeta Crusoe TM5700]]
- [[transmeta-crusoe-tm5800|Transmeta Crusoe TM5800]]
- [[transmeta-crusoe-tm5900|Transmeta Crusoe TM5900]]
- [[x86-compatible-low-power|x86-compatible low-power processor category]]

## Key observations (top 25)

- **2004** — TM5900 package dimensions: 21mm x 21mm (0.8-inch square); 50% smaller than TM5800
- **2004** — TM5700 clock speed: Up to 1 GHz x86-compatible performance
- **2004** — TM5900 cache configuration: 512KB L2 write-back cache (TM5900); 256KB (TM5700); 64KB I-cache + 64KB D-cache; integrated Northbridge; 64-bit DDR SDRAM controller; 32-bit PCI controller
- **2004** — Kastner on TM5800 performance complaints: 'Transmeta has run into customer concerns over performance with the TM5800, for example in Hewlett-Packards TC100 tablet. Users expect more performance than Transmeta has been able to deliver.' — Kastner
- **2004** — Kastner on Crusoe processor adequacy: Kastner had not been briefed about the new, embedded version of the Crusoe processor but said the power of the processors to date has 'not been good enough for many of todays applications.' — Kastner
- **2004** — Motherboard reference platform Q1 2004: Reference platform based on TM5900 available in Q1 2004 with schematics, design guides, processor specifications, device drivers
- **2004-2009** — Did Transmeta survive Kastner's performance critique: No — Transmeta exited processor business 2005 (focused on IP licensing after Efficeon losses), sold IP assets to Novafora 2008, ceased operating 2009. Performance and design-win shortfalls validated Kastner's 'not good enough' thesis.
- **2004** — HP TC100 tablet as TM5800 customer example: HP TC100 tablet used TM5800; cited by Kastner as performance-complaint venue

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'transmeta-crusoe-tm5700-tm5900-computerw-455262' ORDER BY year_observed;
```

