---
title: "Common Gateway Interface (CGI)"
slug: "cgi"
page_type: "technology"
tags: ["type/technology", "category/web technology", "era/mid-1990s"]
tier: 1
source_csv: "_master_technologies.csv"
tech_id: "cgi"
category: "web technology"
vendor: "NCSA/IETF standard"
era: "mid-1990s"
lifecycle_at_study: "emerging"
lifecycle_current: "{'lifecycle_current': 'legacy-supported', 'notes': 'CGI (Common Gateway Interface) is technically functional and still used on some legacy servers, but has largely been replaced by FastCGI, WSGI, and modern server-side frameworks. Still supported by Apache/Nginx but not recommended for new development.', 'source': 'https://blog.apolocloud.net/cgi-common-gateway-interface-the-power/'}"
occurrence_count: 6
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Common Gateway Interface (CGI)

> Aberdeen notes suppliers moving away from CGI toward web-server-to-application-server partitioning; confirmed by Apache/IIS app servers.


## Top observations

- CGI being replaced by ORBs and gateways — [[study-1996-electronic-commerce-25d31b]]
- moving_to_app_server_partitioning — [[study-aberdeen-1996-3com-reconciling-clientserver-development-internet]]
- CGI is standard mechanism for web servers to communicate with applications; used for on-the-fly HTML translation and report presentation — [[study-aberdeen-1996-iq-software-www-reporting]]
- CGI lacks robust transaction processing features necessary to scale without help — [[study-aberdeen-1996-progress-software-webspeed-internet]]
- CGI is a single-threaded bottleneck for communicating from web server to applications; must be replaced by multi-threaded alternatives for enterprise BI — [[study-aberdeen-1996-web-warehouses-dss-for-masses]]
- CGI single-threaded bottleneck must be replaced by multi-threaded alternative for enterprise-scale web BI — [[study-aberdeen-1996-web-warehouses-dss-for-masses]]
- SSL security became standard by 1997; CGI replaced by ISAPI/NSAPI and FastCGI by 1997-1998; DHTML/JavaScript addressed browser limitations; all major obstacles resolved within Aberdeen's 1-2 year timeline — [[study-aberdeen-1996-web-warehouses-dss-for-masses]]
- CGI positioned as current server-side scripting standard; implicitly foreshadows need for richer application servers. — [[study-ca-internet-app-dev-sales-training-1996-48db9c]]
- CGI was displaced by application servers (Java EE, PHP, Rails, Node, etc.) within a decade; Kastner's implicit pointer to limitations of raw CGI was correct. — [[study-ca-internet-app-dev-sales-training-1996-48db9c]]
