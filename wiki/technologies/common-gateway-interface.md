---
title: "Common Gateway Interface (CGI)"
slug: "common-gateway-interface"
page_type: "technology"
tags: ["type/technology", "category/protocol", "era/1993-2005"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "common-gateway-interface"
category: "protocol"
vendor: "NCSA/IETF"
era: "1993-2005"
lifecycle_at_study: "mature"
lifecycle_current: "legacy-supported"
occurrence_count: 1
prescience_max: 4.0
prescience_mean: 4.0
prescience_obs_count: 2
---

# Common Gateway Interface (CGI)

> CGI was the scalability bottleneck that NetDynamics bypassed; still technically available but obsolete


## Top observations

- CGI's single-threaded limitations prevent session optimization; browser/server paradigm becomes bottleneck as traffic increases `[ps=4]` — [[study-aberdeen-1996-spider-technologies-netdynamics]]
- CGI rendered obsolete for high-traffic applications by 2000; FastCGI, mod_perl, servlet containers all bypassed CGI model `[ps=4]` — [[study-aberdeen-1996-spider-technologies-netdynamics]]
- CGI single-threaded model will become increasingly inadequate as web traffic grows; bypass architectures required — [[study-aberdeen-1996-spider-technologies-netdynamics]]
