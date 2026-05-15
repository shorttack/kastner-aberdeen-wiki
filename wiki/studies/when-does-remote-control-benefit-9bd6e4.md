---
title: "When Does Remote Control Benefit Remote Node Architecture?"
slug: when-does-remote-control-benefit-9bd6e4
page_type: study
author: "Aberdeen Group (Virginia Brooks)"
date: "1997-06-01"
study_type: impact-study
subject_domain: "remote-access-technology"
methodology: "industry-analysis, expert-opinion, field-research"
importance: medium
importance_rationale: "A vendor-sponsored impact study for Traveling Software's LapLink; historically significant for documenting the remote node vs. remote control architectural debate at the 28.8kbps modem era peak. Aberdeen's five-criteria decision framework was practically useful but the study's scope and independence are limited by sponsorship."
relevance: low
relevance_rationale: "The specific architectural debate (remote node vs. remote control over dial-up) is entirely obsolete in the era of broadband VPN, cloud desktops, and zero-trust access. The conceptual tension between thin-client and thick-client remote access remains, but 28.8kbps dial-up specifics have no modern applicability."
prescience: medium
prescience_rationale: "Aberdeen predicted remote control adoption would rise as users grew frustrated with 28.8kbps data streaming; this proved directionally correct—remote desktop protocols (RDP, Citrix) did become dominant in many enterprise environments. However, the overall remote access landscape was transformed by broadband and VPN, not the specific remote control over remote node model Aberdeen advocated."
license: CC-BY-4.0
tier: 2
entity_count: 3
tech_count: 6
obs_count: 20
tags: [type/study, importance/medium, prescience/medium, decade/1990s]
source_csv: master_studies.csv
---

# When Does Remote Control Benefit Remote Node Architecture?

> This 1997 Aberdeen Group impact study examines the trade-offs between remote node and remote control architectures for corporate remote access, finding that hybrid deployments combining remote node with remote control software (specifically Traveling Software's LapLink) deliver superior performance. Aberdeen's end-user research identifies five specific deployment conditions where remote control over remote node is advantageous, including mobile user concentrations above 10%, large database access, and frequent software upgrade cycles.

**Author:** Aberdeen Group (Virginia Brooks) · **Date:** 1997-06-01 · **Type:** impact-study
**Importance:** medium — *A vendor-sponsored impact study for Traveling Software's LapLink; historically significant for documenting the remote node vs. remote control architectural debate at the 28.8kbps modem era peak. Aberdeen's five-criteria decision framework was practically useful but the study's scope and independence…*
**Prescience:** medium — *Aberdeen predicted remote control adoption would rise as users grew frustrated with 28.8kbps data streaming; this proved directionally correct—remote desktop protocols (RDP, Citrix) did become dominant in many enterprise environments. However, the overall remote access landscape was transformed by b…*

## Entities (3)

- [[aberdeen-group|Aberdeen Group]]
- [[traveling-software|Traveling Software Inc.]]
- [[virginia-brooks|Virginia Brooks]]

## Technologies (6)

- [[corporate-lan|Corporate LAN]]
- [[laplink|LapLink (remote control software)]]
- [[modem-28kbps|28.8 kbps Dial-Up Modem]]
- [[remote-control-arch|Remote Control Architecture]]
- [[remote-node-ras|Remote Node / RAS (Remote Access Server)]]
- [[vpn|Virtual Private Network (VPN)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'when-does-remote-control-benefit-9bd6e4' ORDER BY year_observed;
```

