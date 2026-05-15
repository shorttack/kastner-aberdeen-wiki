---
title: "Aberdeen Group Semiconductor Research Practice Definition (2002)"
slug: topic-semiconductor-practice-definition-2002
page_type: study
author: "Peter S. Kastner"
date: "2002-03-01"
study_type: topic-analysis
subject_domain: "semiconductor,industry-structure,enabling-technology"
methodology: "industry-analysis,document-review"
importance: high
importance_rationale: "Defines the charter of a major Aberdeen practice; documents Kastner-era strategic framing of semiconductor industry structure at a key 2001-2002 inflection point."
relevance: high
relevance_rationale: "Concepts (fabless, foundries, DFT, SoC test, 300mm, sub-100nm, MEMS, photonics) remain directly relevant to semiconductor industry today."
prescience: high
prescience_rationale: "Correctly predicted (i) only TSMC/Intel/Samsung would fund leading-edge internally, (ii) growing fabless share, (iii) DFT mainstreaming, (iv) SOI adoption, (v) photonics/MEMS need for new test methods. Plastic Logic did not scale commercially."
license: CC-BY-4.0
tier: 1
entity_count: 39
tech_count: 21
obs_count: 23
tags: [type/study, importance/high, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Aberdeen Group Semiconductor Research Practice Definition (2002)

> Formal definition of Aberdeen Group's Semiconductor Research Practice: focus on enabling semiconductor technologies for emerging digital markets (MEMS, photonics, software-defined radios, NPUs, UWB), a taxonomy of semiconductor ecosystem trends (design, fabrication, test), and detailed target account lists spanning 36+ firms (Agere, AMD, ARM, ATI, Broadcom, IBM, Intel, Nvidia, Samsung, Sony, TSMC, etc.). Captures the 2001 semiconductor downturn context (-32% to $132B WW revenue) and a forward-looking view of fabless trends, design/NRE cost inflation ($10M+ per device), 300mm facility cost ($2.7B), verification engineering dominance (70% of cycle), DFT, SoC test, and molecular/Plastic-Logic disruption candidates.

**Author:** Peter S. Kastner · **Date:** 2002-03-01 · **Type:** topic-analysis
**Importance:** high — *Defines the charter of a major Aberdeen practice; documents Kastner-era strategic framing of semiconductor industry structure at a key 2001-2002 inflection point.*
**Prescience:** high — *Correctly predicted (i) only TSMC/Intel/Samsung would fund leading-edge internally, (ii) growing fabless share, (iii) DFT mainstreaming, (iv) SOI adoption, (v) photonics/MEMS need for new test methods. Plastic Logic did not scale commercially.*

## Entities (39)

- [[aberdeen-group|Aberdeen Group]]
- [[aberdeen-semi-practice|Aberdeen Group Semiconductor Research Practice]]
- [[agere|Agere Systems]]
- [[agilent-technologies|Agilent Technologies]]
- [[amd|AMD]]
- [[analog-devices|Analog Devices]]
- [[arm-holdings|ARM Holdings]]
- [[atheros|Atheros Communications]]
- [[ati|ATI Technologies]]
- [[bermai|Bermai]]
- [[broadcom|Broadcom]]
- [[cirrus-logic|Cirrus Logic]]
- [[cogency-semiconductor|Cogency Semiconductor]]
- [[conexant|Conexant Systems]]
- [[cypress-semiconductor|Cypress Semiconductor]]
- [[d-link|D-Link]]
- [[dsp-group|DSP Group]]
- [[eastman-kodak|Eastman Kodak]]
- [[ibm|IBM]]
- [[intel|Intel]]
- [[intellon|Intellon]]
- [[lincom-wireless|LinCom Wireless]]
- [[lsi-logic|LSI Logic]]
- [[micron-technology|Micron Technology]]
- [[motorola|Motorola]]
- [[national-semiconductor|National Semiconductor]]
- [[nec|NEC]]
- [[nvidia|Nvidia]]
- [[panasonic|Panasonic]]
- [[plastic-logic|Plastic Logic]]

## Technologies (21)

- [[300mm-wafer|300mm Wafer Process]]
- [[450mm-wafer|450mm Wafer Transition]]
- [[atpg|Automatic Test Pattern Generation (ATPG)]]
- [[bulk-cmos|Bulk CMOS]]
- [[design-for-test|Design For Test (DFT)]]
- [[fast-cycle-ram|Fast-cycle RAM]]
- [[gallium-arsenide|Gallium Arsenide (GaAs)]]
- [[ip-cores|Semiconductor IP Cores]]
- [[low-power-memory|Low-power memory devices]]
- [[mems|Microelectronic Machines (MEMS)]]
- [[molecular-circuits|Molecular Circuits]]
- [[network-processing-unit|Network Processing Unit (NPU)]]
- [[photonics|Photonics]]
- [[plastic-logic-inkjet|Plastic Logic conductive-ink circuits]]
- [[silicon-germanium|Germanium-doped Silicon (SiGe)]]
- [[silicon-on-insulator|Silicon on Insulator (SOI)]]
- [[software-defined-radio|Silicon/Software-Defined Radio]]
- [[sub-100nm-process|Sub-100 nanometer process]]
- [[system-on-chip|System-on-Chip (SoC)]]
- [[ultra-wideband|Ultra Wide Band (UWB)]]
- [[wifi|WiFi]]

## Key observations (top 25)

- **2001** — WW semiconductor revenue 2001: $132B (-32% YoY)
- **2005** — Leading-edge self-funders: Only Intel, Samsung, TSMC
- **2005** — Fabless growth: Number of fabless semi companies will increase
- **2002** — Memory segmentation: Specialized designs (low-power portable, fast-cycle graphics/router)
- **2002** — Intel SOI stance: Finally acknowledged future need
- **2002** — Wireless material battle: GaAs vs SiGe vs bulk CMOS continue to compete
- **2002** — Disruptive semiconductor tech: Fine jets writing circuits with conductive plastic inks
- **2002** — Molecular circuits: HP, IBM, universities demonstrated in labs
- **2001** — Design NRE cost: $10M+ per device
- **2002** — IP-firm consolidation: Many acquired or disappearing post-2001; more capable firms designing full subsystems
- **2002** — Design verification share: Over 70% of design cycle time; 2-3x more verification than design engineers
- **2001** — 300mm green-field facility cost: $2.7B+
- **2010** — 450mm transition forecast: Future transition beyond 300mm
- **2002** — DFT mainstreaming: Finally becoming mainstream + integrated in design tools
- **2005** — SoC multi-signal test: Single probe/socket for digital+analog+RF+mixed
- **2005** — Wafer probing photonics: No production-ready means exists
- **2005** — New test methods for MEMS/sensors: Need to be invented
- **2002** — Physical failure analysis: Difficult below 90nm; compounds yield ramp
- **2002** — Application segments: Communications, computers, consumer, telematics
- **2002** — Target device types: 8 (analog/DSP, imaging, embedded, networking, non-commodity memory, microprocessors, sensors, wireless)
- **2002** — Target company types: Fabless + Merchant IDMs
- **2002** — Target account count: 36 named firms
- **2002** — Inventory and capacity: Excess inventory finally disappearing; utilization improving for wireless+consumer

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'topic-semiconductor-practice-definition-2002' ORDER BY year_observed;
```

