---
title: "Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters"
slug: "study-1997-marathon-s-endurance-4000-imp-psk-f83368"
page_type: "study"
tags: ["type/study", "collection/impact-brief"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "1997-marathon's-endurance-4000--imp-psk-f83368"
author: "Peter S. Kastner"
date: "1997-02-07"
pub_year: 1997
type: "impact-brief"
subject_domain: "server-high-availability"
methodology: "competitive-profiling, industry-analysis"
source_file: "1997 Marathon's Endurance™ 4000_ imp PSK.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "medium"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 2.61
prescience_obs_count: 18
---

# Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters

> Peter S. Kastner of Aberdeen Group evaluates Marathon Technologies' Endurance 4000, a hardware-based fault-tolerant solution for Windows NT servers. With NT increasingly hosting mission-critical applications, the study examines why Microsoft's forthcoming Wolfpack clustering software provides only minutes-level failover—inadequate for true mission-critical needs—while Marathon's Endurance 4000 provides continuous, transparent fault tolerance at 99.99% uptime for ~$24,995. The study concludes the Endurance 4000 is a well-architected breakthrough that creates a new 'fault-tolerant NT servers' category.


_Published 1997, author **Peter S. Kastner**, type **impact-brief**._


## Top observations

- Expected to ship later in 1997 `[ps=5]`
- Shipped September 1997 with Windows NT Server 4.0 Enterprise Edition; had significant reliability problems in v1; only 2-node clusters; improved substantially in Windows 2000 `[ps=5]`
- Pivoted to software-only product (everRun) in 2004; acquired by Stratus Technologies September 24, 2012; technology continued as Stratus everRun MX product line `[ps=5]`
- OLTP, system management, firewall applications in critical category; also many e-mail, file serving, groupware applications `[ps=5]`
- Recovery measured in minutes; requires reboot `[ps=4]`
- Ever-increasing trend toward NT Server for enterprise applications including transaction processing, email, groupware, internet/intranet, network management `[ps=4]`
- NT Server was never designed to run mission-critical applications without failing; no general purpose OS makes that claim `[ps=4]`
- As more enterprise application 'jewels' hosted on NT servers, risk of significant business disruption rises exponentially as servers 'deployed like popcorn' `[ps=4]`
- 99.99% application uptime — approximately two orders of magnitude improvement over standard NT server `[ps=3]`
- CEs synchronized by memory copy; IOPs synchronized by automatic disk copy when failed component replaced; true continuous processing `[ps=3]`
- 'Well-architected, affordable, hardware-based solution' that adds value 'as if by magic' to shrink-wrapped applications on standard Intel hardware `[ps=3]`
- If Endurance 4000 passes hardware compatibility tests, it will be 'breakaway leader' in the new 'fault-tolerant NT servers and clusters' category `[ps=2]`
- 4 servers: 2 lock-stepped Computing Elements (CE) + 2 I/O Processors (IOP); all Pentium Pro class `[ps=0]`
- NT OS and all shrink-wrapped applications unaware of Endurance 4000; no special application versions required `[ps=0]`
- Wolfpack or other cluster software can run on Endurance-hardened servers `[ps=0]`
- Compaq, Dell, HP, IBM, Micron — major Pentium Pro server platforms tested `[ps=0]`
- No true fault-tolerant solution existed in NT cluster market at time of study; only Wolfpack (not yet shipped) or cluster middleware requiring special app versions `[ps=0]`
- Endurance 4000 includes port to alert external alarm system upon failure `[ps=0]`
- $24,995
- Each half connected by optical fiber up to 1.5 kilometers (1 mile) apart — building/campus-scale disaster recovery
- Marathon Technologies succeeded; HP announced reseller agreement for Endurance 6200 (successor) in 2000; First Options of Chicago used Marathon for trading apps; Aberdeen analyst Joe Clabby confirmed '5 nines of availability in NT industry'
