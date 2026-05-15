---
title: "Sabre's Challenge"
slug: sabre-s-challenge-fb76f5
page_type: study
author: "John Foley (InformationWeek)"
date: "1997-08-18"
study_type: news-article
subject_domain: "airline-reservations-client-server-migration"
methodology: "industry-analysis, executive-interview"
importance: high
importance_rationale: "Kastner quoted in a cover-feature analysis of airline-reservations IT architecture at the inflection point when Travelocity and web-based reservations were emerging; captures the exact client-server surround strategy that dominated travel IT from 1997-2010."
relevance: medium
relevance_rationale: "Sabre continues operating; GDS (Global Distribution Systems) role persists but has been challenged by direct-connect APIs, NDC (New Distribution Capability), and OTAs (Expedia, Booking) since ~2015."
prescience: high
prescience_rationale: "Kastner's diagnosis of TPF as 'adding new applications is problematic' was validated by Sabre's eventual multi-decade migration path (never fully off TPF by the 2020s, with new business built on distributed systems around the core) and the broader industry shift toward SOA and cloud-native travel platforms."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 4
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Sabre's Challenge

> InformationWeek cover feature (August 18, 1997) on Sabre Group Holdings Inc. — spun off from AMR Corporation in late 1996 — and its challenge of expanding software offerings to attract new customers while modernizing a 25-year-old IBM TPF-based mainframe reservations system. System holds 4 TB of data on 400 airlines, 50 car-rental companies, and 35,000 hotels; at peak handles 5,200 messages/second; processed 350M reservations in 1996 at <2 second transaction time. Peter Kastner, Aberdeen Group analyst, explains the limitation: TPF is adept at handling reservations but 'adding new applications is problematic.' Sabre's answer is next-generation Sabre — a client-server surround strategy using Unix/Silicon Graphics servers and Oracle databases to extend the mainframe core. Travelocity (Sabre Interactive) is the flagship case. Thomas Cook (president, Sabre Technology Solutions) notes Sabre's goal of 15-25%/year non-airline revenue growth. Includes IBM 10-year Hong Kong airline deal (June 1997) among recent wins.

**Author:** John Foley (InformationWeek) · **Date:** 1997-08-18 · **Type:** news-article
**Importance:** high — *Kastner quoted in a cover-feature analysis of airline-reservations IT architecture at the inflection point when Travelocity and web-based reservations were emerging; captures the exact client-server surround strategy that dominated travel IT from 1997-2010.*
**Prescience:** high — *Kastner's diagnosis of TPF as 'adding new applications is problematic' was validated by Sabre's eventual multi-decade migration path (never fully off TPF by the 2020s, with new business built on distributed systems around the core) and the broader industry shift toward SOA and cloud-native travel pl…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[amr-corporation|AMR Corporation]]
- [[hong-kong-dragonair|Hong Kong airline GDS consortium]]
- [[ibm|International Business Machines Corporation]]
- [[informationweek|InformationWeek]]
- [[oracle-corp|Oracle Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[sabre-group|Sabre Group Holdings, Inc.]]
- [[silicon-graphics|Silicon Graphics, Inc.]]
- [[terrell-jones-sabre|Terrell B. Jones]]
- [[thomas-cook-sabre|Thomas Cook]]
- [[travelocity|Travelocity]]

## Technologies (4)

- [[client-server|Client-Server Computing]]
- [[ibm-tpf|IBM Transaction Processing Facility (TPF)]]
- [[sabre-reservation-system|Sabre airline reservation system]]
- [[unix-operating-system|Unix operating system]]

## Key observations (top 25)

- **1997** — TPF extensibility limits: TPF is adept at handling reservations, but adding new applications is problematic.
- **1997** — Sabre system scale: 4 terabytes of information; 400 airlines, 50 car rental companies, 35,000 hotels; peak 5,200 messages/second; 350 million reservations processed in 1996 at average <2 second transaction time.
- **1997** — Next-generation Sabre strategy: Next-generation Sabre involves surrounding the core transaction-processing engine with high-performance, special-purpose systems.
- **1997** — Non-airline revenue growth target: Non-airline revenue growth of 15% to 25% a year.
- **1997** — TPF migration desire: For a long time, we have wanted to migrate out of the TPF environment in order to reduce the time to market and cost of building products. We have not figured out a way to do that yet.
- **1997** — Travelocity backend: Travelocity runs on a Unix-based Silicon Graphics server and an Oracle database; 1 million users signed up.
- **1997** — IBM-Sabre Hong Kong deal: June 1997: Sabre and IBM announced a 10-year agreement to develop systems for Hong Kong airlines.
- **2024** — TPF persistence: Sabre continues to run core reservations on TPF (now z/TPF) into the 2020s, surrounded by distributed Java/cloud services — exactly the surround strategy described in 1997. Core TPF never fully retired.
- **2015** — Travelocity exit: Sabre sold Travelocity to Expedia in January 2015 for $280M; Travelocity rebranded as a meta-search frontend for Expedia inventory.
- **2014** — Sabre re-IPO: Sabre Corporation IPO April 2014 (NASDAQ: SABR) after private-equity ownership 2007-2014.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sabre-s-challenge-fb76f5' ORDER BY year_observed;
```

