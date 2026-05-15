---
title: "Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters"
slug: 1997-marathon's-endurance-4000--imp-psk-f83368
page_type: study
author: "Peter S. Kastner"
date: "1997-02-07"
study_type: impact-brief
subject_domain: "server-high-availability"
methodology: "competitive-profiling, industry-analysis"
importance: high
importance_rationale: "First major analyst evaluation of hardware-based NT fault tolerance; Peter S. Kastner accurately identified the reliability gap in NT for mission-critical applications and positioned Marathon as a category-creating leader just as NT adoption was accelerating."
relevance: medium
relevance_rationale: "The architectural concepts (lock-step mirroring, hardware abstraction layer interception, campus-distance disaster recovery) are historically significant; modern high-availability architectures for VMs and containers evolved from these principles."
prescience: high
prescience_rationale: "Kastner correctly predicted the Endurance 4000 would become a 'breakaway leader' in fault-tolerant NT servers; Marathon survived, pivoted to software, and was acquired by Stratus Technologies in 2012 for its fault-tolerance IP. His critique of Wolfpack's 'minutes to recover' limitation proved accurate—MSCS v1 had serious reliability problems."
license: CC-BY-4.0
tier: 1
entity_count: 20
tech_count: 12
obs_count: 42
tags: [type/study, importance/high, prescience/high, decade/1990s]
source_csv: master_studies.csv
---

# Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters

> Peter S. Kastner of Aberdeen Group evaluates Marathon Technologies' Endurance 4000, a hardware-based fault-tolerant solution for Windows NT servers. With NT increasingly hosting mission-critical applications, the study examines why Microsoft's forthcoming Wolfpack clustering software provides only minutes-level failover—inadequate for true mission-critical needs—while Marathon's Endurance 4000 provides continuous, transparent fault tolerance at 99.99% uptime for ~$24,995. The study concludes the Endurance 4000 is a well-architected breakthrough that creates a new 'fault-tolerant NT servers' category.

**Author:** Peter S. Kastner · **Date:** 1997-02-07 · **Type:** impact-brief
**Importance:** high — *First major analyst evaluation of hardware-based NT fault tolerance; Peter S. Kastner accurately identified the reliability gap in NT for mission-critical applications and positioned Marathon as a category-creating leader just as NT adoption was accelerating.*
**Prescience:** high — *Kastner correctly predicted the Endurance 4000 would become a 'breakaway leader' in fault-tolerant NT servers; Marathon survived, pivoted to software, and was acquired by Stratus Technologies in 2012 for its fault-tolerance IP. His critique of Wolfpack's 'minutes to recover' limitation proved accura…*

## Entities (20)

- [[aberdeen-group|Aberdeen Group]]
- [[aberdeen-group|Aberdeen Group]]
- [[compaq|Compaq Computer Corporation]]
- [[compaq|Compaq Computer Corporation]]
- [[dec|Digital Equipment Corporation (DEC)]]
- [[dec|Digital Equipment Corporation (DEC)]]
- [[dell|Dell Computer Corporation]]
- [[dell|Dell Computer Corporation]]
- [[hewlett-packard|Hewlett-Packard]]
- [[hewlett-packard|Hewlett-Packard]]
- [[ibm|IBM]]
- [[ibm|IBM]]
- [[marathon-technologies|Marathon Technologies Corp.]]
- [[marathon-technologies|Marathon Technologies Corp.]]
- [[microsoft|Microsoft Corporation]]
- [[microsoft|Microsoft Corporation]]
- [[ncr|NCR Corporation]]
- [[ncr|NCR Corporation]]
- [[tandem-computers|Tandem Computers]]
- [[tandem-computers|Tandem Computers]]

## Technologies (12)

- [[endurance-4000|Marathon Endurance 4000]]
- [[endurance-4000|Marathon Endurance 4000]]
- [[everrun|Marathon everRun (software fault tolerance)]]
- [[everrun|Marathon everRun (software fault tolerance)]]
- [[nt-hal|NT Hardware Abstraction Layer (HAL)]]
- [[nt-hal|NT Hardware Abstraction Layer (HAL)]]
- [[nt-server|Microsoft Windows NT Server]]
- [[nt-server|Microsoft Windows NT Server]]
- [[pentium-pro|Intel Pentium Pro]]
- [[pentium-pro|Intel Pentium Pro]]
- [[wolfpack-mscs|Microsoft Wolfpack / Microsoft Cluster Server (MSCS)]]
- [[wolfpack-mscs|Microsoft Wolfpack / Microsoft Cluster Server (MSCS)]]

## Key observations (top 25)

- **1997** — Availability rating: 99.99% application uptime — approximately two orders of magnitude improvement over standard NT server
- **1997** — Availability rating: 99.99% application uptime — approximately two orders of magnitude improvement over standard NT server
- **1997** — Product price: $24,995
- **1997** — Product price: $24,995
- **1997** — Architecture configuration: 4 servers: 2 lock-stepped Computing Elements (CE) + 2 I/O Processors (IOP); all Pentium Pro class
- **1997** — Architecture configuration: 4 servers: 2 lock-stepped Computing Elements (CE) + 2 I/O Processors (IOP); all Pentium Pro class
- **1997** — Disaster recovery distance: Each half connected by optical fiber up to 1.5 kilometers (1 mile) apart — building/campus-scale disaster recovery
- **1997** — Disaster recovery distance: Each half connected by optical fiber up to 1.5 kilometers (1 mile) apart — building/campus-scale disaster recovery
- **1997** — Application compatibility: NT OS and all shrink-wrapped applications unaware of Endurance 4000; no special application versions required
- **1997** — Application compatibility: NT OS and all shrink-wrapped applications unaware of Endurance 4000; no special application versions required
- **1997** — Wolfpack failover time: Recovery measured in minutes; requires reboot
- **1997** — Wolfpack failover time: Recovery measured in minutes; requires reboot
- **1997** — Wolfpack delivery timing: Expected to ship later in 1997
- **1997** — Wolfpack delivery timing: Expected to ship later in 1997
- **1997** — Wolfpack actual ship date and reception: Shipped September 1997 with Windows NT Server 4.0 Enterprise Edition; had significant reliability problems in v1; only 2-node clusters; improved substantially in Windows 2000
- **1997** — Wolfpack actual ship date and reception: Shipped September 1997 with Windows NT Server 4.0 Enterprise Edition; had significant reliability problems in v1; only 2-node clusters; improved substantially in Windows 2000
- **1997** — NT Server adoption trend: Ever-increasing trend toward NT Server for enterprise applications including transaction processing, email, groupware, internet/intranet, network management
- **1997** — NT Server adoption trend: Ever-increasing trend toward NT Server for enterprise applications including transaction processing, email, groupware, internet/intranet, network management
- **1997** — NT reliability assessment: NT Server was never designed to run mission-critical applications without failing; no general purpose OS makes that claim
- **1997** — NT reliability assessment: NT Server was never designed to run mission-critical applications without failing; no general purpose OS makes that claim
- **1997** — NT deployment risk warning: As more enterprise application 'jewels' hosted on NT servers, risk of significant business disruption rises exponentially as servers 'deployed like popcorn'
- **1997** — NT deployment risk warning: As more enterprise application 'jewels' hosted on NT servers, risk of significant business disruption rises exponentially as servers 'deployed like popcorn'
- **1997** — Wolfpack compatibility: Wolfpack or other cluster software can run on Endurance-hardened servers
- **1997** — Wolfpack compatibility: Wolfpack or other cluster software can run on Endurance-hardened servers
- **1997** — Memory synchronization: CEs synchronized by memory copy; IOPs synchronized by automatic disk copy when failed component replaced; true continuous processing

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '1997-marathon's-endurance-4000--imp-psk-f83368' ORDER BY year_observed;
```

