---
title: "Planning for Emerging Industry-Standard Platforms (Executive White Paper)"
slug: "study-planningforemergingindustry-6-40decb"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "planningforemergingindustry-6-40decb"
author: "Aberdeen Group (Peter S. Kastner)"
date: "2003-08-01"
pub_year: 2003
type: "white-paper"
subject_domain: "industry-standard-servers/chipsets/memory/systems-management/I-O"
methodology: "industry-analysis, technology-assessment, roadmap-forecasting"
source_file: "PlanningForEmergingIndustry-6.pdf"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "high"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Planning for Emerging Industry-Standard Platforms (Executive White Paper)

> Aberdeen Executive White Paper sponsored by Intel surveying the 2004 generational transition in industry-standard (Intel Architecture) computing. Covers processors and enterprise chipsets (Xeon/Nocona, Itanium 2/Madison, E7501/E7205/E8870/Lindenhurst/Twin Castle, 875P Canterwood), memory evolution from DDR to DDR2 with mainframe-class memory mirroring/sparing/scrubbing, Intelligent Platform Management Initiative (IPMI 1.5) for heterogeneous datacenter management, and the major I/O transition from parallel PCI-X to serial PCI Express. Aberdeen predicts server consolidation, data-center utility computing, and continued IA market-share gain.


_Published 2003, author **Aberdeen Group (Peter S. Kastner)**, type **white-paper**._


## Top observations

- From mid-1990s, IA32-based servers assumed increasingly business-critical transaction processing, decision support, Web, and office workloads.
- Intel shipped more than 1 million enterprise chipsets since start of 2002 (E7501, E7505, E7205 for Xeon; E8870 for Itanium 2).
- Intel's chipsets undergo rigorous qualification and validation involving thousands of engineers and hundreds of millions of dollars — leading to high quality and predictable, stable operation.
- E7505 workstation chipset: fast AGP 8x, over 4 GB/s memory bandwidth; winning design/rendering benchmarks and share vs. RISC workstations.
- E7501 volume 2-way server chipset: up to 16GB real memory, 3 PCI-X I/O buses, dual Gigabit Ethernet.
- 2004 next-gen Xeon 'Nocona' with Lindenhurst chipset — industry's first chipset with PCI Express serial I/O and DDR2 memory.
- Intel Nocona (64-bit Xeon DP with EM64T) launched June 28, 2004, with Lindenhurst chipset platform released August 2, 2004. This was approximately on schedule with the prediction.
- 2H2004: new generation of 32-bit MP server CPUs 'Potomac' with 4-processor 'Twin Castle' chipset — Intel's first recent 4-way IA32 chipset since early 2002 server re-entry.
- Intel Potomac (Xeon MP, 90nm) and Twin Castle chipset platform were planned for 2004. Potomac (Cranford) shipped in 2005. The Twin Castle chipset for 4-way Potomac servers was also released in 2005, approximately on Intel's roadmap.
- Itanium 2 Madison released mid-2003; E8870 designed for 2-8-way Itanium 2 servers with extensive RAS; attractive for mission-critical databases, decision support, encryption; high memory bandwidth + EPIC for sci/tech.
- Itanium 2 performance winning benchmarks and picking up share vs high-end RISC/Unix and mainframe systems.
- DDR266: 2.1 GB/s per channel; DDR333: 2.6 GB/s; DDR400: 3.2 GB/s, often dual-channel for 6.4 GB/s peak. DDR has ~2x bandwidth of ordinary SDRAM.
- Aberdeen expects mainframe-class memory technologies (memory mirroring, spare memory, memory scrubbing) to migrate from high-end Itanium 2 down to multiprocessor and volume servers in 2004.
- Mainframe RAS features (memory mirroring, memory sparing, memory scrubbing) did migrate to industry-standard server platforms 2004-2006. Intel's Xeon MP platforms incorporated these features. HP's Superdome and IBM's x3950 added advanced RAS features to x86 servers by 2005-2006.
- DDR2-400 draws half the power of DDR400, 40% less than DDR333 — critical given 1U rack and blade form-factor trend. IT buyers can pick slow DDR266 or fast DDR2-400 at same power.
- Aberdeen research: about half the total cost of data center ownership is the labor of people who operate and administer the systems.
- IPMI v1.5 (released 2001): message-passing architecture and extensions for monitoring and reporting across data center LANs and remote serial ports — enabling comprehensive enterprise systems management.
- 150+ adopter companies as of 2003; IPMI, in use since 1998, is one of the tools used to build systems-management products lowering data center server-management costs.
- IPMI 1.5 benefits: release-level insulation between hardware and software changes; common user interfaces for LAN/WAN and dial-up; predictive failure alerts; self-healing; improved auto-provisioning; improved asset tracking; storage management/virtualization support.
- PCI: 64 bits parallel every 66MHz cycle = 532 MB/s aggregate bandwidth per bus.
- PCI-X doubles PCI to 1.06 GB/s at 133MHz. PCI-X 2.0 proposes 266MHz (2.1 GB/s peak) and 533MHz (4.2 GB/s peak). PCI-X 266 not in production before 2004; PCI-X 533 still in spec development.
- Aberdeen estimates PCI Express architecture will have a decade or more lifespan due to layered architecture allowing copper/optical/future cabling without affecting higher layer software.
- PCIe remains the dominant PC/server expansion bus standard as of 2025, now at PCIe 5.0 in production and PCIe 6.0 in servers. The prediction of long PCIe longevity was dramatically confirmed — PCIe 1.0 launched in 2003 and the architecture has dominated for 22+ years.
- PCI-E: each lane 2.5GHz = 'x1'; up to x16 aggregated = 4 GB/s bandwidth. Divisible into scalable widths (e.g., x4 for InfiniBand/10GbE).
- Key PCI-E attributes: (1) layered architecture; (2) RAS features — data integrity, advanced error logging via IPMI, hot-plug; (3) I/O consolidation/unification across buses; (4) advanced power/config management; (5) workstation graphics 2x AGP 8x; (6) virtual channels/isochrony/QoS for media I/O; (7) software compatible with PCI-X and PCI.
