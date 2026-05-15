---
title: "Chapter 2: The Physics of the Machine (1969–1972)"
slug: volume-1-ch02-physics-of-the-machine-1969-1972
page_type: chapter
author: "Peter S. Kastner"
date: "2026-05-14"
study_type: memoir
subject_domain: "memoir/volume-1"
methodology: "oral-history"
importance: high
importance_rationale: "Establishes Kastner's foundational programming education, the economic context that shaped 1960s–70s software culture, and early encounters with code generation and Y2K-class problems."
relevance: high
relevance_rationale: "Directly documents the IBM 360/65 service-bureau era, COBOL programming culture, early code generation, and the PHI–Wang Laboratories relationship—all central to the memoir's arc."
prescience: medium
prescience_rationale: "Kastner's 1969 fix of a two-digit-year bug at Marine Midland anticipated the global Y2K crisis by 30 years, and his observation that falling AI inference costs will reprise the cheap-compute dynamic shows consistent forward-thinking."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 17
obs_count: 77
tags: [type/chapter, importance/high, prescience/medium, decade/2020s]
source_csv: master_studies.csv
---

# Chapter 2: The Physics of the Machine (1969–1972)

> Kastner recounts his formative years (1969–1972) as a junior programmer at Philip Hankins Inc. (PHI), a service bureau in Arlington, Massachusetts where CPU time cost $360 per hour on an IBM 360/65. He describes the culture of rigorous efficiency shaped by those economics, key mentors including Robert Siegel, landmark early projects at Cumberland Farms and Marine Midland Bank (including an early Y2K fix), and the Cosmos code-generation system. The chapter ends with Wang Laboratories acquiring PHI and Kastner departing for Arthur D. Little Systems.

**Author:** Peter S. Kastner · **Date:** 2026-05-14 · **Type:** memoir
**Importance:** high — *Establishes Kastner's foundational programming education, the economic context that shaped 1960s–70s software culture, and early encounters with code generation and Y2K-class problems.*
**Prescience:** medium — *Kastner's 1969 fix of a two-digit-year bug at Marine Midland anticipated the global Y2K crisis by 30 years, and his observation that falling AI inference costs will reprise the cheap-compute dynamic shows consistent forward-thinking.*

## Entities (11)

- [[an-wang|An Wang]]
- [[arthur-d-little-systems|Arthur D. Little Systems]]
- [[cumberland-farms|Cumberland Farms]]
- [[dave-moros|David Moros]]
- [[marine-midland-bank|Marine Midland Bank]]
- [[murray-sherry|Murray Sherry]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[phi-computer-services|Philip Hankins Inc. (PHI)]]
- [[philip-hankins|Philip Hankins]]
- [[robert-siegel|Robert A. Siegel]]
- [[wang-laboratories|Wang Laboratories]]

## Technologies (17)

- [[apollo-navigation-software|Apollo Lunar Navigation Software]]
- [[bond-portfolio-system|Bond Portfolio System (Marine Midland)]]
- [[cobol|COBOL]]
- [[code-generation|Code Generation / Automated Code Generation]]
- [[core-dump|Core Dump / Hexadecimal Core Dump]]
- [[core-memory|Core Memory]]
- [[cosmos-application-package|Cosmos (Customer Accounting System / CAS)]]
- [[ibm-360|IBM System/360]]
- [[ibm-360-65|IBM System/360 Model 65]]
- [[ibm-360-reference-card|IBM System/360 Reference Card]]
- [[jcl|Job Control Language (JCL)]]
- [[punch-cards|Punch Cards / Card Decks]]
- [[retail-accounting-system|Retail Accounting System (Cumberland Farms)]]
- [[service-bureau-computing|Service Bureau Computing]]
- [[timesharing|Timesharing Systems]]
- [[wang-vs|Wang VS Operating System]]
- [[y2k-bug|Y2K / Year 2000 Two-Digit Year Bug]]

## Key observations (top 50)

- **1969** — Career start: PHI join date and salary: Kastner joined PHI in March 1969 as a 21-year-old junior programmer earning $7,200/year.
- **1969** — CPU time cost per hour: $360 per hour on PHI's IBM System/360 Model 65 service bureau.
- **1969** — Compute cost vs. labor cost equation (1969): 20 hours of machine time equaled one programmer's annual salary; machine was scarce, labor was cheap.
- **1969** — Inversion of compute vs. labor scarcity: By 2020s, compute is near-free and human talent is the scarce resource—the inverse of 1969.
- **1969** — PHI headquarters description: Converted funeral home in Arlington, Massachusetts; atmosphere half dormitory, half NASA mission control.
- **1969** — Founder background: Apollo navigation code: Philip Hankins wrote navigation code for the Apollo lunar program before founding PHI.
- **1969** — Engineering lead background: Apollo navigation code: David Moros co-wrote navigation code for Apollo and served as PHI engineering lead; described as dapper, polite, and relentlessly precise.
- **1969** — Siegel's later career: Wang VS architect: Robert A. Siegel later architected the Wang VS operating system after leaving PHI.
- **1969** — Siegel's teaching philosophy: programmer manages physical resources: An applications programmer manages physical machine resources: disk spin, core memory cycle, card reader click. Code is choreography of hardware.
- **1969** — Learning tools available: reference card and legal pads: No Stack Overflow, no Google, no online docs; only the IBM System/360 Reference Card (placemat-sized fold-out) and yellow legal pads.
- **1969** — Learning hexadecimal core dump reading: Kastner learned to read hexadecimal core dumps to find the 'ghost in the machine'—debugging equivalent of reconstructing a car crash from skid marks.
- **1969** — Learning JCL (Job Control Language): Kastner learned JCL—the 'dark arts'—to control IBM OS job execution; single misplaced comma could fail a job and waste expensive machine time.
- **1969** — Core dump scale: Catastrophic program failure generated hundreds of pages of raw hexadecimal numbers representing entire core memory contents.
- **1969** — JCL characteristics: cryptic and unforgiving: JCL was notoriously cryptic; a single misplaced comma caused a job to fail and waste an expensive machine run.
- **1969** — Siegel's One-Instruction Switch technique: IBM instruction to set binary flag in register directly without touching memory; replaced 3 memory references with 1 instruction—transformative at scale.
- **1969** — One-Instruction Switch achievable in COBOL: Siegel confirmed the One-Instruction Switch optimization was achievable in COBOL, not just assembly.
- **1969** — Economics of 1969 programming culture: Efficiency was not an engineering preference; it was economic survival at $360/hour. Unnecessary instructions were a small theft from the company budget.
- **1969** — Service bureau batch submission workflow: Write code on coding form → keypunch to cards → submit to operations queue → wait hours → retrieve printout → iterate on error.
- **1969** — Timesharing availability: universities vs. commercial bureaus: Timesharing (terminal-based interactive coding) existed at universities and research labs in 1969 but was not typical at commercial service bureaus.
- **1969** — Batch submission imposed rigorous pre-coding discipline: Every submission was a financial event; discipline of thinking through problems completely before submission was rigorous in ways instant-feedback IDEs don't replicate.
- **1969** — Cumberland Farms pump counter rollover problem: Pump counters physically rolled over to zero at 9,999 gallons; accounting code had to detect rollover and reconcile digital ledger against paper cash transmittal forms.
- **1969** — Lesson: software models physical reality, not ideal specifications: Good software anticipates the ways reality deviates from specification; models what the pump's gears actually did, not what the pump should have done.
- **1969** — Marine Midland bond portfolio Y2K fix date: July 1969; while Apollo 11 transfixed the world, Kastner was fixing a Y2K-class two-digit-year bug in Marine Midland Bank's bond portfolio system.
- **1969** — Y2K bug discovered 30 years early: Two-digit year field: 30-year bond issued in 1970 maturing in 2000 would be recorded as '00', read as 1900. Kastner expanded field to fix it.
- **1969** — Y2K fix made quietly, no press release: \"No one wrote a press release about it. We were just doing the job.\" Fix came 30 years before the global Y2K panic.
- **1969** — Cosmos system description and naming: Originally called Customer Accounting System (CAS), renamed Cosmos; Creedence Clearwater Revival 'Cosmos Factory' album cover framed on main room wall.
- **1969** — Cosmos capability: code generation at scale: Cosmos generated millions of lines of architecturally sound COBOL code according to specifications—a generator, not a conventional application.
- **1969** — Code generation as answer to Brooks's Law: Code generator sidesteps Brooks's Law coordination overhead; produces code faster than any team with perfect architectural consistency—a force multiplier.
- **1969** — Code generation as early low-code development: Cosmos was an early form of low-code development, enabling PHI to deploy systems at scale and speed impossible with conventional programming teams.
- **1970** — Cosmos productivity: bank checking account system build time: Team of four built an entire bank checking account system using Cosmos in one year.
- **1969** — Personal excitement working on Cosmos: Working on Cosmos was 'genuinely exciting—the closest I had come so far to the automation dream'—building a machine that built other machines.
- **1972** — Wang acquires PHI and relocates staff: Wang Laboratories acquired PHI; professional staff ordered to relocate to Wang's facility in Tewksbury, Massachusetts (~25 miles north of Boston).
- **1972** — Reason for leaving PHI: commute, not dissatisfaction: Kastner's wife worked in Quincy (South Shore); Tewksbury (North Shore) commute through Boston was 'Commute of Death'—impractical daily commitment.
- **1972** — Wang described as remarkable company: Kastner had nothing against Wang Laboratories; called it 'a remarkable company'—and noted Moros provided key technical leadership for An Wang's computing initiatives.
- **1972** — Moros role at Wang post-acquisition: David Moros provided key technical leadership for Dr. An Wang's computing initiatives after PHI's acquisition by Wang Laboratories.
- **1972** — PHI diaspora: Murray Sherry leads group to Arthur D. Little Systems: Kastner followed Murray Sherry and others from PHI to Arthur D. Little Systems in Cambridge; described as 'a small, seasoned rescue squad.'
- **1972** — PHI alumni group joined Arthur D. Little Systems: Several PHI alumni arrived together at Arthur D. Little Systems, Cambridge—described as 'arriving as a small, seasoned rescue squad' rather than joining a consultancy.
- **1972** — Lesson 1: software models physical reality: Gas pump counters roll over; bank systems use two-digit years. Good code anticipates the gap between specification and reality. Application users matter.
- **1972** — Lesson 2: economics shape engineering culture more than aesthetics: PHI programmers' obsession with instruction counts was rational response to $360/hour, not personality. Change the economics, change the culture.
- **1972** — Lesson 3: automation multiplied by systems beats automation multiplied by people: Cosmos showed the right answer to Brooks's Law was tools that made each programmer more powerful, not more programmers.
- **2024** — AI inference cost trajectory analogy to 1969 compute costs: Falling AI inference costs in late 2020s will re-invert the economics again—echoing the 1969 dynamic in reverse. Worth remembering.
- **1969** — Kastner's starting age and compensation: Age 21, salary $7,200/year—described as higher than what many bank vice presidents earned at the time.
- **1969** — CPU cost relative to annual salary: 20 hours of IBM 360/65 CPU time at $360/hour = $7,200 = one programmer's annual salary in 1969.
- **1969** — PHI staff composition: Collection of whiz kids and productive eccentrics spread across a ramshackle group of old houses and a repurposed funeral home in Arlington, MA.
- **1969** — PHI sloppy code culture: At PHI, sloppy code was not merely an error—it was a moral failing. Apollo-derived DNA ran through everything they built.
- **1969** — Siegel character description: Brilliant, abrasive mentor. Did not teach syntax; taught physics of the machine—physical resources of disk, memory, card reader.
- **1969** — Moros character description: Described as 'dapper, polite, and relentlessly precise'; presided over PHI's engineering team.
- **1969** — Core dump debugging analogy: Reading a core dump was like reconstructing a car crash from skid marks—hundreds of pages of raw hex to locate program crash cause and data state.
- **1969** — Cumberland Farms project type: Retail accounting system for New England gas station and convenience store chain; one of Kastner's first PHI assignments.
- **1969** — Software is not mathematics: Software is a model of a much messier physical world; the Cumberland Farms and Marine Midland projects drove this lesson home.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'volume-1-ch02-physics-of-the-machine-1969-1972' ORDER BY year_observed;
```

