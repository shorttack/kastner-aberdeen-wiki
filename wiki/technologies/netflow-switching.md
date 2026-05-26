---
title: "NetFlow Switching"
slug: "netflow-switching"
page_type: "technology"
tags: ["type/technology", "category/protocol", "era/1996-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "netflow-switching"
category: "protocol"
vendor: "Cisco Systems"
era: "1996-present"
lifecycle_at_study: "emerging"
lifecycle_current: "active"
occurrence_count: 1
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# NetFlow Switching

> Cisco's per-flow packet forwarding and statistics technology; implemented in IOS 11 (1996); establishes flow cache to speed packet processing; exports per-conversation statistics; provides QoS and accounting capabilities; Aberdeen notes 10% processing overhead tradeoff; NetFlow v9 became basis for IETF IPFIX standard (RFC 7011, 2013); still widely used for network monitoring as of 2026.


## Top observations

- Implemented in 7000/7500 series routers; per-port enabling; flow cache expires inactive flows; 10% overhead on router processing — [[study-1997-cisco-s-core-products-business-inte-bd8697]]
- Establishes flow between source/destination on first packet; subsequent packets switched not routed; exports per-conversation statistics; enables per-flow QoS and security — [[study-1997-cisco-s-core-products-business-inte-bd8697]]
- NetFlow v5 became widely deployed standard for network flow monitoring; NetFlow v9 (Flexible NetFlow) became basis for IETF IPFIX standard (RFC 7011, 2013); still fundamental to network monitoring and security analytics as of 2026 — [[study-1997-cisco-s-core-products-business-inte-bd8697]]
