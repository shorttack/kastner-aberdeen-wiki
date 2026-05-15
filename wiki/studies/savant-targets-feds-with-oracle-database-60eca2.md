---
title: "Savant targets feds with Oracle database tool"
slug: savant-targets-feds-with-oracle-database-60eca2
page_type: study
author: "John Moore, Federal Computer Week (FCW)"
date: "1997-06-08"
study_type: news-article
subject_domain: "database-administration-tools"
methodology: "industry-analysis, analyst-commentary"
importance: low
importance_rationale: "Niche trade-press coverage of a small (now-defunct) Oracle DBA-tool vendor; Kastner's role is a single-sentence expert gloss. Provides a data point on mid-1990s federal DBMS adoption and the DBA-tools usability pressure point."
relevance: low
relevance_rationale: "Savant Corp. disappeared by mid-2000s; Q Diagnostic Center is discontinued. Oracle 7 is long obsolete. Federal GSA schedule mechanism persists, as does the broader DBA-tools-must-be-usable thesis (now addressed by observability platforms like Datadog and New Relic)."
prescience: medium
prescience_rationale: "Kastner's observation that database vendors faced pressure to make tools 'easier to use' proved accurate — the decade that followed (1998-2008) saw extensive DBA-tool GUI investment from Oracle (Enterprise Manager), IBM, Microsoft, Quest Software (Toad), and BMC. Modern cloud-database/observability platforms carry the usability thesis forward."
license: CC-BY-4.0
tier: 2
entity_count: 12
tech_count: 5
obs_count: 7
tags: [type/study, importance/low, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# Savant targets feds with Oracle database tool

> Federal Computer Week article (Jun 8 1997) on Savant Corp. (Bethesda MD) pushing its Q Diagnostic Center product into the US federal government Oracle-database market. Customers already include the Justice Department and the Pension Benefit Guaranty Corp.; Savant plans GSA-schedule sales. Savant strategist Alec Glorieux projects federal will become 10% of company sales by year-end 1997. The product — inspired by founder William Wynn's DBA role on Army Corps of Engineers Automation Plan — provides a graphical overview of Oracle 7 database health, translating operational statistics into animated pictorial displays (e.g., a funnel showing average transaction wait time), and uses comparative-analysis rather than threshold-based methodology. Peter Kastner, group VP at The Aberdeen Group, observes: 'The graphical interface makes sense at a time when database vendors are under a lot of pressure to make their database tools easier to use.' Pricing starts at $3,900/database; supports Oracle 7.2/7.3, Windows 3.1/95/NT, Q Viewer on Win95/NT. Planned expansion into network and OS monitoring by fall 1997.

**Author:** John Moore, Federal Computer Week (FCW) · **Date:** 1997-06-08 · **Type:** news-article
**Importance:** low — *Niche trade-press coverage of a small (now-defunct) Oracle DBA-tool vendor; Kastner's role is a single-sentence expert gloss. Provides a data point on mid-1990s federal DBMS adoption and the DBA-tools usability pressure point.*
**Prescience:** medium — *Kastner's observation that database vendors faced pressure to make tools 'easier to use' proved accurate — the decade that followed (1998-2008) saw extensive DBA-tool GUI investment from Oracle (Enterprise Manager), IBM, Microsoft, Quest Software (Toad), and BMC. Modern cloud-database/observability…*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[alec-glorieux|Alec Glorieux]]
- [[army-corps-engineers|US Army Corps of Engineers]]
- [[fcw-publication|Federal Computer Week (FCW)]]
- [[gsa|US General Services Administration]]
- [[microsoft|Microsoft Corporation]]
- [[oracle-corp|Oracle Corporation]]
- [[pbgc|Pension Benefit Guaranty Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[savant-corp|Savant Corporation]]
- [[us-doj|US Department of Justice]]
- [[william-wynn-savant|William Wynn]]

## Technologies (5)

- [[client-server|Client-Server Computing]]
- [[oracle-7|Oracle 7.2 / 7.3 database]]
- [[oracle-database|Oracle Database 7/8i/9i/10g/11g]]
- [[q-diagnostic-center|Savant Q Diagnostic Center for Oracle]]
- [[windows-3-1-95-nt|Microsoft Windows 3.1 / 95 / NT desktop clients]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'savant-targets-feds-with-oracle-database-60eca2' ORDER BY year_observed;
```

