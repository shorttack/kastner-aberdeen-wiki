---
title: "Aberdeen Group SNR Architecture Slide Set: Critical Technology Planning Areas, Three-Tier Plus Topology, Client-Server Hype vs Implementation (1992)"
slug: aberdeen-snr-architecture-three-tier-sli-abaaa5
page_type: study
author: "Aberdeen Group / Peter S. Kastner (presenter)"
date: "1992"
study_type: aberdeen-presentation-slides
subject_domain: "enterprise-architecture/three-tier-client-server"
methodology: "aberdeen-analyst-presentation-deck"
importance: medium
importance_rationale: "Documents Aberdeen's 1992 enterprise-architecture planning framework and three-tier+ topology positioning during the early-1990s downsizing/distributed-systems wave; OCR is sparse but the planning categories are intact."
relevance: high
relevance_rationale: "Companion to Aberdeen's 1991-1993 distributed-systems / Open OLTP analytical track (Batches 22-24); demonstrates Aberdeen's 'three-tier plus' framing of enterprise topology before client-server had standardized definitions."
prescience: high
prescience_rationale: "1992 'three-tier plus' model — enterprise server + decision support + analytical system + replicated departmental systems + edge clients — anticipated the 2000s/2010s data-warehouse + operational-data-store + edge-client architecture and the modern data-mesh / lakehouse + replicated-microservice + mobile-and-PC-edge pattern."
license: CC-BY-4.0
tier: 1
entity_count: 2
tech_count: 5
obs_count: 5
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Aberdeen Group SNR Architecture Slide Set: Critical Technology Planning Areas, Three-Tier Plus Topology, Client-Server Hype vs Implementation (1992)

> 1992 Aberdeen Group 'SNR Architecture' slide deck (sparse OCR; original was a graphics-heavy presentation deck) outlining four 'Critical Technology Planning Areas' — Systems Software, Application Development, Acquisition, and Enterprise Topology — and presenting a 'Three-tier Plus' enterprise-topology model with 'state-of-the-art downsizing': enterprise server plus decision support; analytical system; replicated/departmental systems; PCs, Workstations, Macs, and Terminals at the edge. Also documents Aberdeen's 1992 stance that client-server has 'much hype but minimal application implementation' with at least six common definitions in use, and presents an 'enterprise spoke' interface set — Product Look-Up, Pricing Information, Order Entry, Master Database, and Current Inventory — bridging Production Systems to the enterprise edge. The deck is fragmentary in OCR but consistent with Aberdeen's 1991-1993 distributed-systems / Open OLTP analytical posture (Batches 22-24).

**Author:** Aberdeen Group / Peter S. Kastner (presenter) · **Date:** 1992 · **Type:** aberdeen-presentation-slides
**Importance:** medium — *Documents Aberdeen's 1992 enterprise-architecture planning framework and three-tier+ topology positioning during the early-1990s downsizing/distributed-systems wave; OCR is sparse but the planning categories are intact.*
**Prescience:** high — *1992 'three-tier plus' model — enterprise server + decision support + analytical system + replicated departmental systems + edge clients — anticipated the 2000s/2010s data-warehouse + operational-data-store + edge-client architecture and the modern data-mesh / lakehouse + replicated-microservice + m…*

## Entities (2)

- [[aberdeen-group|Aberdeen Group]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (5)

- [[aberdeen-critical-tech-planning|Aberdeen Critical Technology Planning Areas Framework]]
- [[aberdeen-three-tier-plus|Aberdeen 'Three-Tier Plus' Enterprise Topology Model]]
- [[client-server-1992|Client-Server (Aberdeen 1992 framing)]]
- [[enterprise-spoke-interface|Aberdeen Enterprise-Spoke Interface Set]]
- [[state-of-art-downsizing|State-of-the-Art Downsizing (Aberdeen 1992)]]

## Key observations (top 25)

- **1992** — Four critical planning areas: Systems Software; Application Development; Acquisition; Enterprise Topology
- **1992** — Three-tier-plus topology layers: Enterprise server + decision support; Analytical system; Replicated/departmental systems; PCs, Workstations, Macs, Terminals
- **1992** — Client-server 1992 stance: Much hype -- minimal application implementation; at least 6 common definitions
- **1992** — Enterprise spoke interfaces: Product Look-up, Pricing Information, Order Entry, Master Database, Current Inventory
- **1992** — Downsizing posture: State-of-the-art downsizing pattern characterizes 1992 enterprise transition

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'aberdeen-snr-architecture-three-tier-sli-abaaa5' ORDER BY year_observed;
```

