---
title: "Planning for Emerging Industry-Standard Platforms (Executive White Paper)"
slug: "study-planningforemergingindustry-6-40decb"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
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
prescience_3y_enum: "high"
prescience_5y_enum: "high"
prescience_max: 5.0
prescience_mean: 3.66
prescience_obs_count: 32
---

# Planning for Emerging Industry-Standard Platforms (Executive White Paper)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** high — 3y Rule A: mean=4.25 over 32 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].
- **5-year verdict:** high — 5y Rule A: mean=4.22 over 32 usable obs (0 prefiltered, 0 pending) -> high [high>=3.5, medium>=2.0].

> Aberdeen Executive White Paper sponsored by Intel surveying the 2004 generational transition in industry-standard (Intel Architecture) computing. Covers processors and enterprise chipsets (Xeon/Nocona, Itanium 2/Madison, E7501/E7205/E8870/Lindenhurst/Twin Castle, 875P Canterwood), memory evolution from DDR to DDR2 with mainframe-class memory mirroring/sparing/scrubbing, Intelligent Platform Management Initiative (IPMI 1.5) for heterogeneous datacenter management, and the major I/O transition from parallel PCI-X to serial PCI Express. Aberdeen predicts server consolidation, data-center utility computing, and continued IA market-share gain.


_Published 2003, author **Aberdeen Group (Peter S. Kastner)**, type **white-paper**._


## Top observations

- From mid-1990s, IA32-based servers assumed increasingly business-critical transaction processing, decision support, Web, and office workloads. `[ps=5]`
- Intel Nocona (64-bit Xeon DP with EM64T) launched June 28, 2004, with Lindenhurst chipset platform released August 2, 2004. This was approximately on schedule with the prediction. `[ps=5]`
- Intel Potomac (Xeon MP, 90nm) and Twin Castle chipset platform were planned for 2004. Potomac (Cranford) shipped in 2005. The Twin Castle chipset for 4-way Potomac servers was also released in 2005, approximately on Intel's roadmap. `[ps=5]`
- DDR266: 2.1 GB/s per channel; DDR333: 2.6 GB/s; DDR400: 3.2 GB/s, often dual-channel for 6.4 GB/s peak. DDR has ~2x bandwidth of ordinary SDRAM. `[ps=5]`
- Mainframe RAS features (memory mirroring, memory sparing, memory scrubbing) did migrate to industry-standard server platforms 2004-2006. Intel's Xeon MP platforms incorporated these features. HP's Superdome and IBM's x3950 added advanced RAS features to x86 servers by 2005-2006. `[ps=5]`
- 150+ adopter companies as of 2003; IPMI, in use since 1998, is one of the tools used to build systems-management products lowering data center server-management costs. `[ps=5]`
- Aberdeen estimates PCI Express architecture will have a decade or more lifespan due to layered architecture allowing copper/optical/future cabling without affecting higher layer software. `[ps=5]`
- PCIe remains the dominant PC/server expansion bus standard as of 2025, now at PCIe 5.0 in production and PCIe 6.0 in servers. The prediction of long PCIe longevity was dramatically confirmed — PCIe 1.0 launched in 2003 and the architecture has dominated for 22+ years. `[ps=5]`
- 2004 PCI-E capabilities expected: serial graphics replacing AGP (4 GB/s over PCI-E, 2x AGP 8x); x8 links ~2x PCI-X 266; serial disk connections proliferating (SATA + SCSI); 10GbE served by PCI-E x8; InfiniBand at 4x freed from PCI-X bottleneck. `[ps=5]`
- PCIe adoption in 2004-2005 was rapid. Intel introduced PCIe in all chipsets in 2004 per roadmap. Dell launched Precision Workstation 470/670 and PowerEdge servers with PCIe in mid-2004. By 2005 PCIe was standard on new server and workstation platforms. `[ps=5]`
- Aberdeen's nod in PCI-E vs PCI-X 266 matchup goes to PCI Express for more theoretical bandwidth and long-life architecture, while still using tried-and-true PCI-based systems software. 2004 platforms expected to include both PCI/PCI-X slots and PCI-E slots. `[ps=5]`
- Aberdeen expects industry-standard servers to continue gaining market segment share — a sign IT buyers are pleased with value received. `[ps=5]`
- Intel's chipsets undergo rigorous qualification and validation involving thousands of engineers and hundreds of millions of dollars — leading to high quality and predictable, stable operation. `[ps=4]`
- E7505 workstation chipset: fast AGP 8x, over 4 GB/s memory bandwidth; winning design/rendering benchmarks and share vs. RISC workstations. `[ps=4]`
- 2004 next-gen Xeon 'Nocona' with Lindenhurst chipset — industry's first chipset with PCI Express serial I/O and DDR2 memory. `[ps=4]`
- 2H2004: new generation of 32-bit MP server CPUs 'Potomac' with 4-processor 'Twin Castle' chipset — Intel's first recent 4-way IA32 chipset since early 2002 server re-entry. `[ps=4]`
- Aberdeen expects mainframe-class memory technologies (memory mirroring, spare memory, memory scrubbing) to migrate from high-end Itanium 2 down to multiprocessor and volume servers in 2004. `[ps=4]`
- Aberdeen research: about half the total cost of data center ownership is the labor of people who operate and administer the systems. `[ps=4]`
- PCI-X doubles PCI to 1.06 GB/s at 133MHz. PCI-X 2.0 proposes 266MHz (2.1 GB/s peak) and 533MHz (4.2 GB/s peak). PCI-X 266 not in production before 2004; PCI-X 533 still in spec development. `[ps=4]`
- PCI-E: each lane 2.5GHz = 'x1'; up to x16 aggregated = 4 GB/s bandwidth. Divisible into scalable widths (e.g., x4 for InfiniBand/10GbE). `[ps=4]`
- Key PCI-E attributes: (1) layered architecture; (2) RAS features — data integrity, advanced error logging via IPMI, hot-plug; (3) I/O consolidation/unification across buses; (4) advanced power/config management; (5) workstation graphics 2x AGP 8x; (6) virtual channels/isochrony/QoS for media I/O; (7) software compatible with PCI-X and PCI. `[ps=4]`
- Building 4-way Xeon MP in 2004 extends Intel's own validated products to cover ~95% of 32-bit server and workstation market segment. Industry partners handle the high-end, low-volume IA32 systems. `[ps=4]`
- Aberdeen predicts industry-standard technology improvements (DDR2, IPMI, PCI-E) will drive server consolidation initiatives at many enterprises. `[ps=4]`
- DDR2-400 draws half the power of DDR400, 40% less than DDR333 — critical given 1U rack and blade form-factor trend. IT buyers can pick slow DDR266 or fast DDR2-400 at same power. `[ps=3]`
- IPMI v1.5 (released 2001): message-passing architecture and extensions for monitoring and reporting across data center LANs and remote serial ports — enabling comprehensive enterprise systems management. `[ps=3]`
