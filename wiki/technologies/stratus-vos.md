---
title: "Stratus VOS (Virtual Operating System)"
slug: "stratus-vos"
page_type: "technology"
tags: ["type/technology", "category/operating-system", "era/1980s-present"]
tier: 2
source_csv: "_master_technologies.csv"
tech_id: "stratus-vos"
category: "operating-system"
vendor: "Stratus Computer"
era: "1980s-present"
lifecycle_at_study: "newly-launched-1982"
lifecycle_current: "active-as-stratus-vos"
occurrence_count: 2
prescience_max: 5.0
prescience_mean: 3.0
prescience_obs_count: 4
---

# Stratus VOS (Virtual Operating System)

> Distributed OS that makes a federation of processing modules appear as a single virtual computer to programs and users; transparent file/process distribution; uniform service-request interface.


## Top observations

- Verified: location transparency (paths resolve to remote storage) became universal in NFS, AFS, DFS, modern object stores and global file systems `[ps=5]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- All VOS service requests have a uniform interface independent of which module performs the work (e.g., file open is identical regardless of disk location) `[ps=4]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- VOS runs in every module; all modules equal; transparent local networking makes the federation appear as a single virtual computer to programs, programmers and users `[ps=3]` — [[study-ieee-db-stratus-32-psk-1d4564]]
- 16 MB total (4 MB VOS + 12 MB user) `[ps=0]` — [[study-mini-micro-stratus-32-arch-freiburghouse-6dc03e]]
- Every file has an access-control list of (user-id, rights ∈ {execute, read, read/write}); per-user or per-group; no embedded passwords in programs; enforced regardless of access program/command — [[study-ieee-db-stratus-32-psk-1d4564]]
