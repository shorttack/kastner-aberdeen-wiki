---
title: "Sirius – The Case For Web Enablement By Mainframe Upgrade"
slug: sirius-web-enablement-b81ea8
page_type: study
author: "Wayne Kernochan (Aberdeen Group)"
date: "1997-01-01"
study_type: market-study
subject_domain: "mainframe-web-enablement"
methodology: "industry-analysis,expert-opinion,competitive-profiling"
importance: medium
importance_rationale: "Published at the peak of Internet hype when mainframe obsolescence was widely predicted; Aberdeen's counter-narrative was commercially significant for mainframe ISVs and their enterprise customers."
relevance: medium
relevance_rationale: "The architectural trade-off between in-place modernization versus full rewrite remains a live debate in enterprise IT; the analytical framework applies directly to legacy system decisions today."
prescience: high
prescience_rationale: "Aberdeen predicted in-place web enablement would prove superior to migration/rewrite; this proved accurate — mainframe web-enabling tools proliferated and the mainframe survived the Internet era, with Sirius Software itself thriving until its 2012 acquisition by Rocket Software."
license: CC-BY-4.0
tier: 1
entity_count: 3
tech_count: 4
obs_count: 12
tags: [type/study, importance/medium, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Sirius – The Case For Web Enablement By Mainframe Upgrade

> Aberdeen Group argues that the advent of the Internet paradoxically strengthened the mainframe case: rather than forcing migration or rewrite of business-critical applications, enterprises could web-enable in place using tools like Sirius Software's Janus Web Server. Migration and rewriting were found to be riskier and less scalable than expected, while in-place web enablement offered a cost-effective path. The report recommends senior IS managers reconsider mainframe migration in favor of targeted upgrade strategies.

**Author:** Wayne Kernochan (Aberdeen Group) · **Date:** 1997-01-01 · **Type:** market-study
**Importance:** medium — *Published at the peak of Internet hype when mainframe obsolescence was widely predicted; Aberdeen's counter-narrative was commercially significant for mainframe ISVs and their enterprise customers.*
**Prescience:** high — *Aberdeen predicted in-place web enablement would prove superior to migration/rewrite; this proved accurate — mainframe web-enabling tools proliferated and the mainframe survived the Internet era, with Sirius Software itself thriving until its 2012 acquisition by Rocket Software.*

## Entities (3)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-corporation-of-america|Computer Corporation of America]]
- [[sirius-software-inc|Sirius Software Inc.]]

## Technologies (4)

- [[ibm-mainframe|IBM Mainframe (MVS/z/OS)]]
- [[janus-web-server|Janus Web Server]]
- [[model-204|Model 204]]
- [[www-http|World Wide Web / HTTP]]

## Key observations (top 25)

- **1997** — Mainframe web-enablement tool maturity: Tools arriving and improving; Janus Web Server cited as key example
- **1997** — Mainframe Internet strategy option 1: Rewrite — write application from scratch on Web server
- **1997** — Mainframe Internet strategy option 2: Migrate and upgrade — move mainframe app to web server then web-enable it
- **1997** — Mainframe Internet strategy option 3: Upgrade in place — web-enable mainframe application while keeping it on mainframe
- **1997** — Internet effect on mainframe: Paradoxically positive — made it easier to keep and web-enable mainframe apps rather than replace them
- **1997** — Scalability and robustness of rewritten apps: Migration or rewriting results in applications that are less scalable and robust than original mainframe apps
- **1997** — Janus Web Server market viability: Product expected to improve and gain adoption for mainframe web-enablement
- **2012** — Sirius Software Inc. corporate outcome: Acquired by Rocket Software in November 2012 for undisclosed sum; products continued under Rocket M204 brand
- **2026** — IBM mainframe survival post-Internet era: IBM mainframe (z/OS) remains in active production at major banks and government agencies nearly 30 years after study
- **1997** — Aberdeen recommendation for IS managers: Senior IS managers should reconsider rewriting or migrating mainframe apps; use new mainframe-software tools to web-enable in place
- **1997** — Cost-effectiveness of in-place web enablement: In-place web-enablement offers cost-effective Internet connectivity with minimal impact on production environment
- **2010** — Model 204 corporate outcome: Computer Corporation of America acquired by Rocket Software in March 2010; Model 204 rebranded as Rocket M204

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'sirius-web-enablement-b81ea8' ORDER BY year_observed;
```

