---
title: "NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage"
slug: ncr-3000-cabinet-engineering-diagram-199-fa564f
page_type: study
author: "NCR Corporation (engineering documentation)"
date: "1992"
study_type: engineering-diagram
subject_domain: "server-hardware-architecture"
methodology: "vendor-engineering-documentation"
importance: medium
importance_rationale: "Concrete engineering documentation of the NCR 3000 family that underlies Aberdeen's 1991-1992 Open OLTP analyses; specifies the Intel486 50MHz / Micro Channel / hot-pluggable storage / X/Open platform that Kastner's white papers describe in the abstract."
relevance: medium
relevance_rationale: "Documents the NCR commercial multiprocessor platform that Aberdeen OLTP/MP studies and the WSJ ad refer to; provides hardware context for the contemporaneous Kastner Korean and Norway translations."
prescience: low
prescience_rationale: "Specific cabinet design did not predict any unique trend; however, the architectural choices (commodity x86 multiprocessing, hot-pluggable storage, modular SCSI, redundant power, X/Open Unix) anticipated the rack-mount commodity-x86 server pattern that dominated the 2000s data center."
license: CC-BY-4.0
tier: 2
entity_count: 3
tech_count: 7
obs_count: 6
tags: [type/study, importance/medium, prescience/low, decade/1990s]
source_csv: master_studies.csv
---

# NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage

> NCR Corporation engineering diagram from 1992 documenting the NCR 3000 server cabinet design: processor boards each carrying two 50MHz Intel486 microprocessors, memory boards, eight Primary Micro Channel slots (with eight Optional slots on the Optional Side), 6.75-inch hot-pluggable fans, hot-pluggable internal SCSI fixed disks (up to 14 full-height or 28 half-height), 4 full-height or 8 half-height removable devices on each side, standard 525MB QIC tape and 1.44MB flex disk, optional 600MB CD-ROM and 1.3GB Digital Audio Tape, power back-up system batteries, security lock, and a local peripheral board for VGA monitor / mouse / keyboard / diagnostic monitor / parallel printer. The artifact provides concrete platform context for the Aberdeen Open OLTP white-paper claims about low-cost commercial multiprocessor platforms, X/Open compliance, and downsizing-from-mainframe value propositions of 1991-1992. Companion to the Norway 1992 OLTP seminar deck which references the NCR Model 3550 (UNIX V.4 multiprocessor up to eight i486-50MHz, ~320 MIPS, supporting 1,000+ workstations).

**Author:** NCR Corporation (engineering documentation) · **Date:** 1992 · **Type:** engineering-diagram
**Importance:** medium — *Concrete engineering documentation of the NCR 3000 family that underlies Aberdeen's 1991-1992 Open OLTP analyses; specifies the Intel486 50MHz / Micro Channel / hot-pluggable storage / X/Open platform that Kastner's white papers describe in the abstract.*
**Prescience:** low — *Specific cabinet design did not predict any unique trend; however, the architectural choices (commodity x86 multiprocessing, hot-pluggable storage, modular SCSI, redundant power, X/Open Unix) anticipated the rack-mount commodity-x86 server pattern that dominated the 2000s data center.*

## Entities (3)

- [[att-corp|AT&T Corporation]]
- [[intel-corporation|Intel Corporation]]
- [[ncr-corporation|NCR Corporation]]

## Technologies (7)

- [[dat-tape-1-3gb|1.3GB Digital Audio Tape (DAT)]]
- [[hot-pluggable-storage|Hot-Pluggable Disk and Fan Subsystems]]
- [[intel-i486-50mhz|Intel i486 at 50MHz]]
- [[micro-channel-architecture|IBM Micro Channel Architecture (MCA)]]
- [[ncr-3000-family|NCR 3000 Server Family]]
- [[qic-tape-525mb|525MB Quarter-Inch Cartridge (QIC) Tape]]
- [[scsi-bus|Small Computer System Interface (SCSI)]]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'ncr-3000-cabinet-engineering-diagram-199-fa564f' ORDER BY year_observed;
```

