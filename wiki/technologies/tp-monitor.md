---
title: "TP Monitor (Transaction Processing Monitor)"
slug: "tp-monitor"
page_type: "technology"
tags: ["type/technology", "category/system-software", "era/1970s-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "tp-monitor"
category: "system-software"
vendor: "Multiple (Novell Tuxedo, IBM/Transarc Encina, IBM CICS)"
era: "1970s-present"
lifecycle_at_study: "mature"
lifecycle_current: "obsolete"
occurrence_count: 3
prescience_max: 5.0
prescience_mean: 3.6
prescience_obs_count: 5
---

# TP Monitor (Transaction Processing Monitor)

> BroadVision combines OO middleware with TP monitor technology to handle intense internet loads; key architectural differentiation.


## Top observations

- Interaction manager maintains persistent connections; caches user profiles, content, categories; amortizes database cost over multiple sessions `[ps=5]` — [[study-1997-broadvision-dynamic-web-application-5f10bb]]
- Eliminates CGI process start/stop overhead; multithreaded; load balances across multiple DB servers; query optimization on SQL construction `[ps=5]` — [[study-aberdeen-1996-spider-technologies-netdynamics]]
- Aberdeen urges: architecture must include TP-monitor-like middleware for scalable commercial web-database applications `[ps=4]` — [[study-aberdeen-1996-spider-technologies-netdynamics]]
- TP-monitor-as-web-middleware became the dominant enterprise architecture; J2EE application servers (WebLogic, WebSphere) codified this pattern; all major early app server companies acquired by 1998 `[ps=4]` — [[study-aberdeen-1996-spider-technologies-netdynamics]]
- Centura supports Novell Tuxedo TP monitor with Tuxedo Deployment Suite; middleware access to IBM CICS and Encina; 3-Tier Wizard for simplified TP programming `[ps=0]` — [[study-aberdeen-1996-moving-effectively-next-gen-client-server]]
