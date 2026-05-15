---
title: "An Overview of Internet Application Development (CA Sales Training June 1996)"
slug: ca-internet-app-dev-sales-training-1996-48db9c
page_type: study
author: "Peter S. Kastner"
date: "1996-06-01"
study_type: employer-record
subject_domain: "employer/aberdeen-group"
methodology: "industry-analysis, executive-presentation, sales-force-education"
importance: high
importance_rationale: "Early (June 1996) analyst framing of Internet application development for a major enterprise-software sales force, delivered at the inflection point between client-server and Web architectures."
relevance: medium
relevance_rationale: "Content is foundational-education material; architectural contrasts remain interesting as a period piece."
prescience: high
prescience_rationale: "Kastner's 1996 framing of Web apps ('runs on a server(s); presentation by client browser; no session') turned out to be the dominant enterprise-application architecture within five years; his 'no concept of a session' framing foreshadowed the later shift to stateless REST."
license: CC-BY-4.0
tier: 1
entity_count: 4
tech_count: 6
obs_count: 10
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# An Overview of Internet Application Development (CA Sales Training June 1996)

> 'An Overview of Internet Application Development' — Peter S. Kastner presentation to Computer Associates Sales Training, June 1996. Introduces the Internet/intranet stack (thin-client browser, TCP/IP, HTTP, CGI, firewall, RDBMS) and contrasts Internet applications with traditional client-server. Early canonical analyst framing of the Web as an application-delivery platform delivered to a CA sales audience in the Netscape-dominant pre-IE3 era.

**Author:** Peter S. Kastner · **Date:** 1996-06-01 · **Type:** employer-record
**Importance:** high — *Early (June 1996) analyst framing of Internet application development for a major enterprise-software sales force, delivered at the inflection point between client-server and Web architectures.*
**Prescience:** high — *Kastner's 1996 framing of Web apps ('runs on a server(s); presentation by client browser; no session') turned out to be the dominant enterprise-application architecture within five years; his 'no concept of a session' framing foreshadowed the later shift to stateless REST.*

## Entities (4)

- [[aberdeen-group|Aberdeen Group]]
- [[computer-associates|Computer Associates International, Inc.]]
- [[netscape|Netscape Communications]]
- [[peter-kastner|Peter S. Kastner]]

## Technologies (6)

- [[cgi|Common Gateway Interface (CGI)]]
- [[client-server|Client-Server Architecture]]
- [[firewall|Enterprise Firewall]]
- [[http|HTTP (HyperText Transport Protocol)]]
- [[tcp-ip|TCP/IP]]
- [[web-browser|Web Browser (thin client)]]

## Key observations (top 25)

- **1996** — Internet/intranet component stack: Thin-client Web browser (e.g., Netscape); WAN/LAN using TCP/IP; HTTP server; CGI scripts; firewall for enterprise-network privacy; application RDBMS.
- **1996** — Client-server vs Internet apps: Client-server: app runs on desktop; data brought from server to desktop; session-oriented (OLTP). Internet: app runs on server(s); presentation by client browser; no concept of a session.
- **1996** — Thin-client dominance over time: Thin-client Web browser as presentation layer enables application architecture that runs on servers and presents via browser — foundational framing for the next decade of enterprise apps.
- **1996** — CGI as interim scripting: CGI positioned as current server-side scripting standard; implicitly foreshadows need for richer application servers.
- **2026** — Web-app architecture outcome: Web application architecture (server-side app + browser presentation) became the dominant enterprise-app architecture by ~2001 and remains so. Kastner prediction verified.
- **2026** — CGI outcome: CGI was displaced by application servers (Java EE, PHP, Rails, Node, etc.) within a decade; Kastner's implicit pointer to limitations of raw CGI was correct.
- **2026** — Client-server decline: Client-server architecture was largely displaced by Web/web-services architecture across enterprise app development by 2005. Kastner's 1996 contrast framing was prescient.
- **1996** — Netscape as canonical browser: Netscape referenced as the default example browser in a June-1996 CA sales deck — accurate market position at time of writing.
- **1996** — Kastner role 1996: Signed as 'Vice President', Aberdeen Group.
- **1996** — Kastner delivering sales training for CA: June 1996 Internet app-dev training for CA sales — concrete evidence of the sales-force-education service line named in the 1999 retainer proposal.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ca-internet-app-dev-sales-training-1996-48db9c' ORDER BY year_observed;
```

