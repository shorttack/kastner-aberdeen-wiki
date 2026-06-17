---
title: "The 64-bit Tipping Point: Optimizing Performance, Flexibility, and Value with Intel Itanium Architecture and Intel EM64T"
slug: "study-2004-09-intel-64bit-tipping-point-b21860"
page_type: "study"
tags: ["type/study", "collection/white-paper"]
tier: 1
source_csv: "_master_studies.csv"
study_id: "2004-09-intel-64bit-tipping-point-b21860"
author: "Intel Corporation"
date: "2004-09-01"
pub_year: 2004
type: "white-paper"
subject_domain: "processor-architecture"
methodology: "technology-analysis, vendor-positioning"
source_file: "The-64-bit-Tipping-Point-6.pdf"
license: "CC-BY-4.0"
importance: "medium"
relevance: "low"
study_prescience_enum: "high"
prescience_max: 5.0
prescience_mean: 3.14
prescience_obs_count: 14
---

# The 64-bit Tipping Point: Optimizing Performance, Flexibility, and Value with Intel Itanium Architecture and Intel EM64T

> Intel's September 2004 white paper positions two complementary 64-bit architectures—Itanium for high-end business-critical applications and Intel Xeon with EM64T for general-purpose computing—as the optimal 64-bit migration path. Citing IDC forecasts of Itanium server market growth from under $1 billion (2003) to $8 billion (2008), and Aberdeen Group's Peter Kastner on Itanium outperforming RISC, the paper argues that EM64T will trigger broad mainstream 64-bit migration while Itanium holds the data-tier niche. BEA WebLogic and SAS case studies illustrate platform selection tradeoffs.


_Published 2004, author **Intel Corporation**, type **white-paper**._


## Top observations

- Itanium-based server market less than $1 billion in 2003 `[ps=5]`
- Itanium server market did not reach $8 billion. By 2008, Itanium-based system revenue was approximately $4.4B annually (HP alone), declining to $3.5B by end-2009. x86-64 (EM64T/AMD64) dominated general workloads as predicted. Itanium was discontinued in 2021. `[ps=5]`
- IDC: New system shipments based on 32-bit x86 processors will be swept away over time by x86-64 designs `[ps=5]`
- 32-bit x86 server market was substantially displaced by x86-64 (EM64T/AMD64) by 2008-2010. By 2009, most new servers shipped with x86-64 processors. 32-bit-only server workloads became legacy by 2010. `[ps=5]`
- 64-bit processor can manipulate data in chunks twice as large (64-bit vs 32-bit); key for complex calculations requiring high precision `[ps=5]`
- EM64T/x86-64 will dominate general-purpose and mainstream enterprise applications; Itanium relegated to high-end business-critical niche `[ps=5]`
- Intel Xeon with EM64T triggers broad shift toward 64-bit computing; initially for applications constrained by 32-bit 4GB memory limit `[ps=4]`
- Rise of Web Services and Service Oriented Architecture (SOA) simplifying integration across businesses and supply chains; high-volume transactions in real-time; driving 64-bit demand `[ps=4]`
- Intel discontinued Itanium on July 29, 2021. Final orders accepted until January 30, 2020. This matched the predicted discontinuation. `[ps=3]`
- IDC forecasts Itanium-based server market to grow from less than $1 billion (2003) to more than $8 billion in 2008 `[ps=2]`
- Itanium architecture remains platform of choice for most demanding business-critical data tier applications: high-end database and business intelligence `[ps=1]`
- Omicronn Trax on BEA WebLogic + Itanium 2: 5 million messages/hour at only 50-60% utilization; outperformed RISC alternatives `[ps=0]`
- Itanium 2 processor supports up to 1 petabyte of physical memory; Xeon MP up to 1 terabyte; Xeon up to 64 gigabytes `[ps=0]`
- For some mid-tier enterprise applications, best platform choice not obvious; requires close look at software availability, business drivers, and workloads `[ps=0]`
- Intel Xeon with EM64T preferable for general-purpose applications: web, mail, digital content creation, mechanical CAD, EDA; mixed 32/64-bit environments
- Legacy mode (32-bit OS + apps), Compatibility mode (64-bit OS + 32-bit apps), 64-bit mode (full 64-bit OS + apps)
- Performance boost of up to 50% for existing 32-bit applications on EM64T platforms vs prior Xeon platforms
- Aberdeen Group (Peter Kastner, May 14 2004): Intel Itanium consistently outperforms 64-bit RISC-based servers; Intel-based platforms better performing per processor, more scalable, more cost-effective, and more flexible
- 94% of current Itanium-installed firms plan to buy more over next three years; 50% of non-buyers list it in future spend plans
- SpecjAppServer2002 leading benchmark results for absolute performance and price/performance all achieved using Intel architecture, majority on Itanium 2
- 64-bit processor transcends 4GB memory limit of 32-bit; can directly access virtually unlimited physical memory; dramatic performance for large memory-intensive applications
- RFID tags and point-of-sale devices causing quantum leap in processing and data requirements that may dwarf end-user workloads
- IDC: EM64T strategy provides excellent investment protection and additional headroom with few or no drawbacks; will initiate broad move toward 64-bit capable platforms
