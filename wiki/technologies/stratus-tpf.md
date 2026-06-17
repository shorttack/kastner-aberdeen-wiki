---
title: "Stratus TPF (Transaction Processing Facility)"
slug: "stratus-tpf"
page_type: "technology"
tags: ["type/technology", "category/transaction-processing-monitor", "era/1980s-1990s"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "stratus-tpf"
category: "transaction-processing-monitor"
vendor: "Stratus Computer"
era: "1980s-1990s"
lifecycle_at_study: "current-1986"
lifecycle_current: "obsolete"
occurrence_count: 1
prescience_max: 5.0
prescience_mean: 3.25
prescience_obs_count: 4
---

# Stratus TPF (Transaction Processing Facility)

> Multi-tasking transaction-server framework; START / COMMIT / ABORT primitives; per-application message queues that can be dynamically redirected; two-phase commit across modules.


## Top observations

- Single message queue can connect any number of servers with any number of requesters; queues redirect dynamically by changing the pathname to point to another module — applications scale without recompile `[ps=5]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Multi-tasking, multiple transaction servers, large program address space; terminal-handling requesters and application servers can reside anywhere within a system or network of systems `[ps=4]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- START / COMMIT / ABORT primitives in TPF; ABORT restores all files to pre-START state regardless of whether data is on a single processing module or distributed `[ps=4]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- Application programs may be written in COBOL, PL/I, BASIC, FORTRAN or Pascal; all language features usable, including I/O statements `[ps=0]` — [[study-ieee-db-stratus-32-psk-1d4564]]
