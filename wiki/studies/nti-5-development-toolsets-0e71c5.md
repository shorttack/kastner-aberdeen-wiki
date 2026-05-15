---
title: "Selecting and Using Advanced Software Toolsets"
slug: nti-5-development-toolsets-0e71c5
page_type: study
author: "Peter S. Kastner, John Logan, Thomas Willmott"
date: "1993-04-01"
study_type: market-study
subject_domain: "software-development"
methodology: "industry-analysis, technology-assessment, vendor-profiling"
importance: high
importance_rationale: "Provides a comprehensive, practitioner-oriented taxonomy of the 1993 software toolset market at the inflection point from 3GL/4GL to client-server and GUI development, identifying specific vendors and architectural patterns that shaped enterprise application development for the decade."
relevance: medium
relevance_rationale: "The three-layer application architecture model and the principle of separating RDBMS from toolset selection remain architecturally relevant; specific product assessments are historical."
prescience: high
prescience_rationale: "Aberdeen's prediction that object-oriented technology would be mainstream by late 1990s and that enterprise-scale repositories would be a failed concept proved accurate; the positioning of C and C++ as dominant ISV languages also proved correct."
license: CC-BY-4.0
tier: 1
entity_count: 33
tech_count: 15
obs_count: 30
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Selecting and Using Advanced Software Toolsets

> This Aberdeen Group workbook surveys the rapidly changing software development toolset landscape in 1993, presenting key field research findings from CIO interviews and ISV briefings. It identifies best-in-class tools across 3GLs, 4GLs, RDBMS-integrated tools, GUI builders, and CASE, and defines the three-layer architecture — presentation, business logic, data access — of strategic applications. The study evaluates client-server development readiness, positions emerging GUI tools from Powersoft, Gupta, and others, and previews object-oriented technology as a late-1990s mainstream prospect.

**Author:** Peter S. Kastner, John Logan, Thomas Willmott · **Date:** 1993-04-01 · **Type:** market-study
**Importance:** high — *Provides a comprehensive, practitioner-oriented taxonomy of the 1993 software toolset market at the inflection point from 3GL/4GL to client-server and GUI development, identifying specific vendors and architectural patterns that shaped enterprise application development for the decade.*
**Prescience:** high — *Aberdeen's prediction that object-oriented technology would be mainstream by late 1990s and that enterprise-scale repositories would be a failed concept proved accurate; the positioning of C and C++ as dominant ISV languages also proved correct.*

## Entities (33)

- [[aberdeen-group|Aberdeen Group]]
- [[andersen-consulting|Andersen Consulting]]
- [[ask-computer|ASK Computer Systems]]
- [[blyth-software|Blyth Software]]
- [[cognos|Cognos]]
- [[cooperative-solutions|Cooperative Solutions]]
- [[digital-equipment-corporation|Digital Equipment Corporation]]
- [[forte-software|Forte Software]]
- [[gupta-technologies|Gupta Technologies]]
- [[hewlett-packard|Hewlett-Packard]]
- [[hyperdesk|Hyperdesk Corporation]]
- [[ibm|IBM]]
- [[informix|Informix]]
- [[ingres|Ingres]]
- [[intersolv|INTERSOLV]]
- [[john-logan|John Logan]]
- [[knowledgeware|KnowledgeWare]]
- [[ncr|NCR Corporation]]
- [[next-computer|Next Computer]]
- [[object-management-group|Object Management Group]]
- [[oracle|Oracle]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[powersoft|Powersoft Corporation]]
- [[progress-software|Progress Software]]
- [[software-ag|Software AG]]
- [[sun-microsystems|Sun Microsystems]]
- [[sybase|Sybase]]
- [[taligent|Taligent]]
- [[texas-instruments|Texas Instruments]]
- [[thomas-willmott|Thomas Willmott]]

## Technologies (15)

- [[4gl|Fourth Generation Languages (4GLs)]]
- [[ada|Ada]]
- [[c-language|C and C++]]
- [[case|Computer-Aided Software Engineering (CASE)]]
- [[client-server|Client-Server Application Framework]]
- [[cobol|COBOL]]
- [[corba|CORBA / OMG Object Standards]]
- [[fortran|Fortran]]
- [[gui-builders|GUI Application Builders]]
- [[microsoft-sql-server|Microsoft SQL Server (Sybase SQLServer)]]
- [[object-oriented|Object-Oriented Programming]]
- [[powerbuilder|PowerBuilder]]
- [[rdbms|Relational Database Management Systems]]
- [[sql|SQL (Structured Query Language)]]
- [[sql-windows|SQLWindows]]

## Key observations (top 25)

- **1993** — Software development as primary IS challenge: Development expertise constraining overall industry growth despite new tools
- **1993** — Enterprise repository concept outcome: Mega enterprise repository is failed concept
- **1993** — Object-oriented mainstream production timeline: 3-5 years out for production systems from 1993
- **1998** — OO production systems mainstream actual timing: [UNVERIFIED]
- **1993** — Object-oriented industry revolution timeline: Will revolutionize industry by end of 1990s
- **2000** — OO industry revolution actual occurrence: [UNVERIFIED]
- **1993** — Oracle RDBMS market position: Revenue leader; Oracle7 aggressive positioning
- **1993** — Sybase client-server positioning: Well-positioned as client-server advocate; SQLServer remarketed by Microsoft
- **1993** — Ingres market visibility post-ASK acquisition: Less visible in market since ASK Computer acquisition
- **1993** — Cognos Powerhouse market strength: Traditional strength in DEC and HP installed base
- **1993** — Progress Software revenue trajectory: Dramatic revenue growth last several quarters; excellent ISV platform reputation
- **1993** — Software AG Natural 4GL market coverage: Widely used IBM mainframe; recent thrust to HP 9000 and NCR System 3000
- **1993** — C language role in 1993 development strategy: Viable 3GL component; mostly-tools-some-C multi-component strategy emerging
- **1993** — COBOL status in 1993: Language of choice for large-scale mainframe; data centers in maintenance mode
- **1993** — IBM AD/Cycle strategy outcome: Disappointing; being reworked
- **1993** — Powersoft market position: Leading Windows GUI builder for PC development
- **1993** — Forte and Cooperative Solutions positioning: Full-blown integrated client-server for complex transaction processing
- **1993** — GUI support cost challenge for ISVs: Major GUI alternatives: Windows, Macintosh, Motif, OpenLook; ISVs struggling with multi-GUI expense
- **1993** — Legacy data access challenge: Core enterprise data still in hierarchical IMS files; SQL bridges required
- **1993** — Client-server toolset buyer confusion: MIS buyers confused by huge variety of client-server toolsets
- **1993** — Multi-platform client challenge: No universally satisfactory client; organizations dealing with Windows, OS/2, Mac, Unix
- **1993** — Optimal software development strategy: Enhance legacy systems + create strategic applications + continuous staff training
- **1993** — Toolset selection independence from RDBMS: Not always necessary to select RDBMS supplier's toolkit; can supplement or replace
- **1993** — OMG standardization scope: Standardizing types of service requests objects universally provide; object behavior in distributed systems
- **1993** — OO database technology landscape: European BKS Poet, Object Design, Objectivity, Ontos, Servio, Versant offer OODBMS

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'nti-5-development-toolsets-0e71c5' ORDER BY year_observed;
```

