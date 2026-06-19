---
title: Quote 1145 —  ()
type: quotation
slug: quote-1145
row_id: 1145
author: "Peter S. Kastner"
publication: ""
date: ""
headline: "Gartner's Smith concurred that the platform's basic security features are paramount. He rated the partitioning feature"
horizon: "SH-3y"
final_bucket: high
final_score: 4
final_confidence: 3
final_pipeline: P2
blog_scrape_contamination: false
scorer_version: quotations_corpus_v1
source_pass: quotations_corpus
tags: [quotation, prescience, kastner]
---

#  — 

**Headline**: Gartner's Smith concurred that the platform's basic security features are paramount. He rated the partitioning feature

**Verdict**: HIGH prescience — score=4, confidence=3, horizon=SH-3y, pipeline=P2

## Quote

> important bulwark against malware and denial-of-service attacks. As for .NET, Smith said those in the know already have it. "You didn't need to wait for Win2003 to deploy .NET. If you did, you didn't really understand the software." But Aberdeen's Kastner said that, nonetheless, integration of .NET with Win2003 is important because it makes .NET more reliable. "You have to realize Win2003 is a long-term project to bring underlying stabili

## Rationale

IIS 6.0 in Windows Server 2003 introduced worker process isolation and application pools, which materially improved containment of faults and reduced the kind of broad IIS-compromising worms seen with Code Red and Nimda, making it a meaningful, if not complete, bulwark against many web-facing malware and denial-of-service conditions. .NET Framework 1.0/1.1 was already deployable on Windows 2000 and XP, and early adopters did so, while Windows Server 2003’s tighter integration of the CLR and ASP.NET into IIS 6.0 became the standard, more reliable hosting environment for .NET applications by the mid-2000s. In practice Windows Server 2003 gained a strong reputation for stability and security and became the dominant Windows server platform through the second half of the 2000s, validating the idea that it was a long-term project to improve underlying system stability, even though Windows overall continued to face significant security challenges.

## Provenance

- **row_id**: 1145
- **Source master**: `_master_quotations_prescience.csv`
- **Scorer version**: quotations_corpus_v1
- **Author**: Peter S. Kastner
