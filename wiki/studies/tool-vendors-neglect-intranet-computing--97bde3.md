---
title: "Tool vendors neglect intranet needs (Kastner three-year IT predictions)"
slug: tool-vendors-neglect-intranet-computing--97bde3
page_type: study
author: "Douglas Hayward"
date: "1996-10-30"
study_type: news-article
subject_domain: "intranet-tools-browser-vs-Windows-client-1996"
methodology: "news-reporting, analyst-predictions, expert-interview"
importance: high
importance_rationale: "Rare documented three-year Kastner-Aberdeen prediction set from the peak-intranet era. Mixture of hits (browser-as-client dominance; Novell decline) and misses (Corel WordPerfect Java; OO dominance). The 1973 Y2K admission is a unique personal-biographical data point."
relevance: high
relevance_rationale: "Browser-as-primary-client prediction is now the dominant enterprise paradigm (SaaS, web apps); Novell decline analysis fully validated; Y2K anecdote ties Kastner directly to the legacy-code crisis discourse."
prescience: high
prescience_rationale: "Core prediction that tools vendors would have to 'treat browsers as just another client' was fully validated by SaaS and web-app dominance 1998-present. Novell analysis proved correct — Novell declined steadily, acquired by Attachmate 2011, then Micro Focus 2014, then OpenText 2023. OO-dominance prediction partially correct. Corel-WordPerfect-in-Java prediction failed."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 10
obs_count: 9
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Tool vendors neglect intranet needs (Kastner three-year IT predictions)

> Computing UK article by Douglas Hayward interviewing Peter Kastner (Aberdeen Group VP) in London during a BMC Software visit. Kastner delivers a set of three-year industry predictions: intranet-development delayed until tool vendors treat browsers as equal to Windows clients; Novell will struggle as intranet directory services obviate NDS; object-oriented and internet-based technology will temporarily raise then reduce IT ownership costs; network-computer vendors will bundle WordPerfect once Corel rewrites it in Java. Closes with Kastner's 1973 Chase Manhattan Y2K-noncompliant-code admission.

**Author:** Douglas Hayward · **Date:** 1996-10-30 · **Type:** news-article
**Importance:** high — *Rare documented three-year Kastner-Aberdeen prediction set from the peak-intranet era. Mixture of hits (browser-as-client dominance; Novell decline) and misses (Corel WordPerfect Java; OO dominance). The 1973 Y2K admission is a unique personal-biographical data point.*
**Prescience:** high — *Core prediction that tools vendors would have to 'treat browsers as just another client' was fully validated by SaaS and web-app dominance 1998-present. Novell analysis proved correct — Novell declined steadily, acquired by Attachmate 2011, then Micro Focus 2014, then OpenText 2023. OO-dominance pre…*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[bmc-software|BMC Software]]
- [[chase-manhattan-bank|Chase Manhattan Bank]]
- [[computing-uk|Computing (UK)]]
- [[corel-corp|Corel Corporation]]
- [[douglas-hayward-computing|Douglas Hayward]]
- [[microsoft|Microsoft Corporation]]
- [[novell-inc|Novell Inc.]]
- [[peter-s-kastner|Peter S. Kastner]]

## Technologies (10)

- [[corba|Object Request Broker Architecture (CORBA)]]
- [[intranet|Intranet (corporate web)]]
- [[java-platform|Java platform]]
- [[network-computer|Network Computer (NC)]]
- [[novell-nds|Novell Directory Services (NDS)]]
- [[web-browser-client|Web browser as client platform]]
- [[windows-client|Windows native client (Win32)]]
- [[windows-nt|Windows NT 4.0]]
- [[wordperfect|WordPerfect]]
- [[y2k-noncompliant-code|Y2K-noncompliant date code]]

## Key observations (top 25)

- **1996** — Kastner browser-client-equality prediction: 'Development of intranet environments will be delayed until tools vendors treat browsers as the equal of Windows clients. IT departments dont have enough resources to develop applications that people want, because they are having to develop them twic…
- **2000-2025** — Did browser become primary client: Yes — SaaS/web-app dominance from ~1999 onwards (Salesforce 1999, Gmail 2004, Microsoft 365 web 2010s), capped by Electron/Chromium desktop adoption. Browsers/Chromium now dominant enterprise-app delivery medium.
- **1996** — Kastner NDS-obsolescence prediction: 'You wont necessarily need Novells Directory Services if you have a corporate intranet with a white pages facility that lists all your users and their email addresses. I am distressed with Novells inability to see the threats to its position over the…
- **1996-2011** — Did Novell decline as Kastner predicted: Yes — Novell market share collapsed 1996-2003 as Windows NT/2000/Active Directory displaced NetWare/NDS in corporate directories. Novell acquired by Attachmate 2011, then Micro Focus 2014, then OpenText 2023. NDS rebranded eDirectory and exists in le…
- **1996** — Kastner no-ORB-dominance prediction: 'Object-oriented and Internet-based technology will help to bring down IT ownership costs in the short term, but costs will initially rise... No single request-broker architecture will dominate the industry.' — Kastner
- **1996** — Kastner NC-WordPerfect-Java bundle prediction: 'Network computer vendors will bundle WordPerfect with their devices after Corel rewrites the application in Java.' — Kastner
- **1996-2005** — Did Corel rewrite WordPerfect in Java for NCs: No — Corel's brief 1996-1997 Java-office initiative (Corel Office for Java) was abandoned. NC market itself collapsed by 2000. WordPerfect remained Win32 native.
- **1973** — Kastner 1973 Chase Manhattan Y2K admission: 'Kastner flew into London last week with a guilty secret. While working at Chase Manhattan Bank in 1973, he wrote a system which he knew would not be year 2000-compliant.' — Computing
- **1996** — Kastner IT-ownership-costs prediction: 'We are dealing with new technologies for which the industry doesnt yet have proper methodologies. That means costs will increase briefly as we go through the learning curve, but they will come down significantly over the longer term.' — Kastner

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'tool-vendors-neglect-intranet-computing--97bde3' ORDER BY year_observed;
```

