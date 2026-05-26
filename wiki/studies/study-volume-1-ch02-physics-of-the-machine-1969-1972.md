---
title: "Chapter 2: The Physics of the Machine (1969–1972)"
slug: "study-volume-1-ch02-physics-of-the-machine-1969-1972"
page_type: "study"
tags: ["type/study", "collection/memoir"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "volume-1-ch02-physics-of-the-machine-1969-1972"
author: "Peter S. Kastner"
date: "2026-05-14"
pub_year: 2026
type: "memoir"
subject_domain: "memoir/volume-1"
methodology: "oral-history"
source_file: "MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 2: The Physics of the Machine (1969-1972))"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "medium"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Chapter 2: The Physics of the Machine (1969–1972)

> Kastner recounts his formative years (1969–1972) as a junior programmer at Philip Hankins Inc. (PHI), a service bureau in Arlington, Massachusetts where CPU time cost $360 per hour on an IBM 360/65. He describes the culture of rigorous efficiency shaped by those economics, key mentors including Robert Siegel, landmark early projects at Cumberland Farms and Marine Midland Bank (including an early Y2K fix), and the Cosmos code-generation system. The chapter ends with Wang Laboratories acquiring PHI and Kastner departing for Arthur D. Little Systems.


_Published 2026, author **Peter S. Kastner**, type **memoir**._


## Top observations

- Kastner joined PHI in March 1969 as a 21-year-old junior programmer earning $7,200/year.
- $360 per hour on PHI's IBM System/360 Model 65 service bureau.
- 20 hours of machine time equaled one programmer's annual salary; machine was scarce, labor was cheap.
- By 2020s, compute is near-free and human talent is the scarce resource—the inverse of 1969.
- Converted funeral home in Arlington, Massachusetts; atmosphere half dormitory, half NASA mission control.
- Philip Hankins wrote navigation code for the Apollo lunar program before founding PHI.
- David Moros co-wrote navigation code for Apollo and served as PHI engineering lead; described as dapper, polite, and relentlessly precise.
- Robert A. Siegel later architected the Wang VS operating system after leaving PHI.
- An applications programmer manages physical machine resources: disk spin, core memory cycle, card reader click. Code is choreography of hardware.
- No Stack Overflow, no Google, no online docs; only the IBM System/360 Reference Card (placemat-sized fold-out) and yellow legal pads.
- Kastner learned to read hexadecimal core dumps to find the 'ghost in the machine'—debugging equivalent of reconstructing a car crash from skid marks.
- Kastner learned JCL—the 'dark arts'—to control IBM OS job execution; single misplaced comma could fail a job and waste expensive machine time.
- Catastrophic program failure generated hundreds of pages of raw hexadecimal numbers representing entire core memory contents.
- JCL was notoriously cryptic; a single misplaced comma caused a job to fail and waste an expensive machine run.
- IBM instruction to set binary flag in register directly without touching memory; replaced 3 memory references with 1 instruction—transformative at scale.
- Siegel confirmed the One-Instruction Switch optimization was achievable in COBOL, not just assembly.
- Efficiency was not an engineering preference; it was economic survival at $360/hour. Unnecessary instructions were a small theft from the company budget.
- Write code on coding form → keypunch to cards → submit to operations queue → wait hours → retrieve printout → iterate on error.
- Timesharing (terminal-based interactive coding) existed at universities and research labs in 1969 but was not typical at commercial service bureaus.
- Every submission was a financial event; discipline of thinking through problems completely before submission was rigorous in ways instant-feedback IDEs don't replicate.
- Pump counters physically rolled over to zero at 9,999 gallons; accounting code had to detect rollover and reconcile digital ledger against paper cash transmittal forms.
- Good software anticipates the ways reality deviates from specification; models what the pump's gears actually did, not what the pump should have done.
- July 1969; while Apollo 11 transfixed the world, Kastner was fixing a Y2K-class two-digit-year bug in Marine Midland Bank's bond portfolio system.
- Two-digit year field: 30-year bond issued in 1970 maturing in 2000 would be recorded as '00', read as 1900. Kastner expanded field to fix it.
- "No one wrote a press release about it. We were just doing the job." Fix came 30 years before the global Y2K panic.
