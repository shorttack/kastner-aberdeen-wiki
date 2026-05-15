---
title: "Tiger Responds to Security Warnings"
slug: tiger-responds-security-warnings-eweek-b-95c721
page_type: study
author: "Ian Betteridge"
date: "2005-04-29"
study_type: news-article
subject_domain: "Mac-OS-X-Tiger-security-posture-2005"
methodology: "news-reporting, analyst-quote-aggregation"
importance: medium
importance_rationale: "Landmark Mac OS X Tiger launch coverage with rare quantitative Apple/Symantec vulnerability data and Kastner's predictive framework for Apple-platform attacks."
relevance: medium
relevance_rationale: "Baseline for long-running debate over Mac-OS-versus-Windows attack surface; Kastner's severity-vs-count framing remains useful for modern macOS risk analysis."
prescience: high
prescience_rationale: "Kastner predicted 'Apple's growing success will bring more attacks, but so far Apple has been able to keep up with — if not a step ahead of — the bad guys.' Both halves validated: macOS attacks did grow with market share (Trojans, 2012 Flashback, 2016 KeRanger, 2020s XCSSET) but enterprise-severity comparisons with Windows remain one-sided in Apple's favor."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 7
obs_count: 8
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Tiger Responds to Security Warnings

> eWEEK article reporting Mac OS X 10.4 'Tiger' launch features (Kerberos VPN, stealth-mode firewall, Safe Downloads, secure virtual memory) in the context of analyst warnings that Apple's rising market share will attract more attackers. Kastner (Vericours Inc. director) cites the Symantec Internet Security Threat Report figure of 37/1,403 new vulnerabilities involving Apple in H2 2004 and argues severity and organizational impact remain much lower than Microsoft's.

**Author:** Ian Betteridge · **Date:** 2005-04-29 · **Type:** news-article
**Importance:** medium — *Landmark Mac OS X Tiger launch coverage with rare quantitative Apple/Symantec vulnerability data and Kastner's predictive framework for Apple-platform attacks.*
**Prescience:** high — *Kastner predicted 'Apple's growing success will bring more attacks, but so far Apple has been able to keep up with — if not a step ahead of — the bad guys.' Both halves validated: macOS attacks did grow with market share (Trojans, 2012 Flashback, 2016 KeRanger, 2020s XCSSET) but enterprise-severity…*

## Entities (11)

- [[apple-inc|Apple Inc.]]
- [[eweek|eWEEK]]
- [[frost-sullivan|Frost & Sullivan]]
- [[ian-betteridge-eweek|Ian Betteridge]]
- [[microsoft|Microsoft Corporation]]
- [[morgan-stanley|Morgan Stanley]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[rufus-connell-frost|Rufus Connell]]
- [[sophos-plc|Sophos Plc.]]
- [[symantec-corp|Symantec Corporation]]
- [[vericours|Vericours Inc.]]

## Technologies (7)

- [[kerberos|Kerberos authentication protocol]]
- [[mac-os-x-firewall-stealth|Mac OS X Stealth-mode firewall]]
- [[mac-os-x-secure-vm|Mac OS X Secure Virtual Memory]]
- [[mac-os-x-tiger|Mac OS X 10.4 (Tiger)]]
- [[opener-renepo|Opener / Renepo malware]]
- [[safe-downloads|Safe Downloads (Mac OS X Tiger)]]
- [[windows-os-family|Microsoft Windows OS family]]

## Key observations (top 25)

- **2004** — Apple vulnerabilities H2 2004 (Symantec ISTR): 37 of 1,403 new vulnerabilities involving Apple for six months ended Dec 31 2004
- **2005** — Kastner on Apple vulnerability severity: 'While the ratio of new Apple vulnerabilities to total new vulnerabilities approximates Apples market share, the severity and impact on organizations can only be categorized as much lower than with Microsoft operating systems.'
- **2005** — Kastner Apple-attack-growth prediction: 'I agree with Symantec that Apples growing success will bring more attacks, but so far Apple has been able to keep up with — if not a step ahead of — the bad guys.' — Kastner
- **2005-2025** — Did macOS attacks grow with market share: Yes — 2012 Flashback Trojan (~600K Macs), 2016 KeRanger ransomware, 2020s XCSSET, Silver Sparrow, ongoing enterprise-credential theft campaigns. Apple-enterprise severity per incident generally remained lower than Windows ransomware events.
- **2005** — Connell on Microsoft attack surface: 'Microsoft, with nearly 97 percent of the market, is a much more appealing target' — Connell
- **2005** — Morgan Stanley Apple market-share-doubling projection: Morgan Stanley predicted Apple could see its market share double by end of 2005
- **2005** — Tiger security feature set: Kerberos VPN, stealth-mode firewall, Safe Downloads, secure virtual memory
- **2004** — First Mac OS X malware: Opener / Renepo discovered by Sophos — script to harvest passwords, copied itself to mounted volumes but lacked effective propagation

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'tiger-responds-security-warnings-eweek-b-95c721' ORDER BY year_observed;
```

