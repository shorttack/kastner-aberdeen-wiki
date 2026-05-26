---
title: "DataPropagator (Relational and NonRelational)"
slug: "tech-iif-002"
page_type: "technology"
tags: ["type/technology", "category/Data Replication", "era/1994-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "tech-iif-002"
category: "Data Replication"
vendor: "IBM"
era: "1994-present"
lifecycle_at_study: "Growth"
lifecycle_current: "Evolved (renamed IBM Replication / DB2 DataPropagator integrated into DB2 replication services; CDC pattern lives on)"
occurrence_count: 1
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# DataPropagator (Relational and NonRelational)

> Log-based CDC replication tool. Absorbed into IBM DB2 replication capabilities; Change Data Capture pattern now dominant via Debezium, AWS DMS, etc.


## Top observations

- Log-based capture to staging area then apply to destination; minimizes production database impact — [[study-1997-ibm-information-integration-family--29351c]]
- DB2-to-Sybase, DB2-to-Oracle, Oracle-to-DB2, Oracle-to-Oracle confirmed customer deployments — [[study-1997-ibm-information-integration-family--29351c]]
- Will add further support for traditional RDBMS scalability technologies such as cursors and governors — [[study-1997-ibm-information-integration-family--29351c]]
- Absorbed into IBM DB2 Replication; log-based CDC pattern validated by entire industry — [[study-1997-ibm-information-integration-family--29351c]]
- Supports push from laptop or pull from central server for mobile/laptop replication — [[study-1997-ibm-information-integration-family--29351c]]
