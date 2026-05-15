---
title: "Tech Investor: Instant Messaging goes corporate"
slug: tech-investor-instant-messaging-goes-cor-1a14c2
page_type: study
author: "Eric Hellweg, CNN/Money"
date: "2002-11-08"
study_type: column-opinion
subject_domain: "enterprise-collaboration"
methodology: "analyst-commentary, vendor-commentary"
importance: medium
importance_rationale: "Primary CNN/Money coverage of the 2002 corporate-IM market transition — shortly before Microsoft's Live Communications Server (2003) and IBM Lotus Sametime expansion. Kastner's integration-with-calendar-email-web-conferencing thesis foreshadowed the exact UCaaS bundle that became Teams/Slack/Zoom."
relevance: high
relevance_rationale: "The 2002 enterprise-IM market Kastner described evolved directly into today's unified-communications-as-a-service market (Microsoft Teams, Slack, Zoom, Google Workspace) — a multi-hundred-billion-dollar category."
prescience: high
prescience_rationale: "Kastner's calendar+email+web-conferencing integration thesis proved exactly right: Microsoft rolled IM into Outlook/Exchange via Live Communications Server (2003), Office Communicator (2007), Lync (2010), Skype for Business (2015), and Teams (2017). WebEx was acquired by Cisco (2007) and later bundled with Cisco Jabber/Webex Teams. Slack (2013) and later Microsoft Teams (2017) realized the full vision Kastner sketched in 2002."
license: CC-BY-4.0
tier: 1
entity_count: 9
tech_count: 3
obs_count: 6
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# Tech Investor: Instant Messaging goes corporate

> CNN/Money Tech Investor column (Nov 8 2002) by Eric Hellweg on the corporate instant-messaging market opportunity. AOL launched Enterprise AIM Services this week; Yahoo! and Microsoft pushing competing corporate IM offerings. Peter Kastner, chief research officer for Aberdeen Research, frames the strategic prize as integration rather than IM itself: 'into the existing corporate communications infrastructure, which includes calendar and e-mail and will eventually include WebEx services.' Michael Gartenberg (Jupiter Research) warns that while AOL/Yahoo/Microsoft consumer-IM dominance is 'some validation for WebEx,' it should also be 'a cause for concern' if the big three decide to subsume the web-conferencing market.

**Author:** Eric Hellweg, CNN/Money · **Date:** 2002-11-08 · **Type:** column-opinion
**Importance:** medium — *Primary CNN/Money coverage of the 2002 corporate-IM market transition — shortly before Microsoft's Live Communications Server (2003) and IBM Lotus Sametime expansion. Kastner's integration-with-calendar-email-web-conferencing thesis foreshadowed the exact UCaaS bundle that became Teams/Slack/Zoom.*
**Prescience:** high — *Kastner's calendar+email+web-conferencing integration thesis proved exactly right: Microsoft rolled IM into Outlook/Exchange via Live Communications Server (2003), Office Communicator (2007), Lync (2010), Skype for Business (2015), and Teams (2017). WebEx was acquired by Cisco (2007) and later bundl…*

## Entities (9)

- [[aberdeen-group|Aberdeen Group]]
- [[aol-inc|America Online (AOL)]]
- [[cnn-money|CNN/Money (CNNMoney.com)]]
- [[eric-hellweg-journalist|Eric Hellweg]]
- [[michael-gartenberg-analyst|Michael Gartenberg]]
- [[microsoft|Microsoft Corporation]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[webex-inc|WebEx Communications, Inc.]]
- [[yahoo-inc|Yahoo! Inc.]]

## Technologies (3)

- [[enterprise-instant-messaging|Enterprise instant messaging]]
- [[unified-communications|Unified communications (UC / UCaaS)]]
- [[web-conferencing|Web conferencing / online meeting software]]

## Key observations (top 25)

- **2002** — Integration thesis: Corporate IM is about integration into the existing corporate communications infrastructure, which includes calendar and e-mail and will eventually include WebEx services.
- **2002** — Enterprise AIM Services launch: AOL launched Enterprise AIM Services Nov 2002 — a corporate version of AIM targeting the enterprise IM market alongside competing offerings from Yahoo! and Microsoft.
- **2002** — WebEx subsume risk: The major companies' push into corporate messaging offers some validation for WebEx, but it should be a cause for concern. If AOL, Yahoo, and Microsoft sense there's a market, they'll do everything they can to subsume them.
- **2017** — Teams realizes Kastner vision: Microsoft Teams (launched 2017) unified IM, calendar, email, web conferencing, and presence into a single UCaaS bundle — exactly the integration Kastner sketched in 2002 — and grew to 300M+ monthly active users by 2023.
- **2007** — Cisco acquires WebEx: Cisco Systems acquired WebEx Communications for $3.2 billion in March 2007; WebEx became central to Cisco's UC/collaboration portfolio (Cisco Jabber, Webex Teams, Webex Meetings).
- **2017** — AOL sunsets AIM: AOL sunset the AIM consumer service on Dec 15 2017; the Enterprise AIM Services discussed in this article were wound down earlier. AOL itself was acquired by Verizon 2015, then sold to Apollo 2021.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'tech-investor-instant-messaging-goes-cor-1a14c2' ORDER BY year_observed;
```

