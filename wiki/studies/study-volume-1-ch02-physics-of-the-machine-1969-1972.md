---
title: "Chapter 2: The Physics of the Machine (1969–1972)"
slug: "study-volume-1-ch02-physics-of-the-machine-1969-1972"
page_type: "study"
tags: ["type/study", "collection/memoir"]
tier: 1
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
prescience_3y_enum: "medium"
prescience_5y_enum: "medium"
prescience_max: 5.0
prescience_mean: 1.47
prescience_obs_count: 77
---

# Chapter 2: The Physics of the Machine (1969–1972)


## Short-horizon prescience (3-year / 5-year)

- **3-year verdict:** medium — 3y Rule A: mean=3.44 over 73 usable obs (0 prefiltered, 4 pending) -> medium; 4 obs still pending (verdict may shift) [high>=3.5, medium>=2.0].
- **5-year verdict:** medium — 5y Rule A: mean=3.48 over 73 usable obs (0 prefiltered, 4 pending) -> medium; 4 obs still pending (verdict may shift) [high>=3.5, medium>=2.0].

> Kastner recounts his formative years (1969–1972) as a junior programmer at Philip Hankins Inc. (PHI), a service bureau in Arlington, Massachusetts where CPU time cost $360 per hour on an IBM 360/65. He describes the culture of rigorous efficiency shaped by those economics, key mentors including Robert Siegel, landmark early projects at Cumberland Farms and Marine Midland Bank (including an early Y2K fix), and the Cosmos code-generation system. The chapter ends with Wang Laboratories acquiring PHI and Kastner departing for Arthur D. Little Systems.


_Published 2026, author **Peter S. Kastner**, type **memoir**._


## Top observations

- JCL was notoriously cryptic; a single misplaced comma caused a job to fail and waste an expensive machine run. `[ps=5]`
- Good software anticipates the ways reality deviates from specification; models what the pump's gears actually did, not what the pump should have done. `[ps=5]`
- Gas pump counters roll over; bank systems use two-digit years. Good code anticipates the gap between specification and reality. Application users matter. `[ps=5]`
- PHI programmers' obsession with instruction counts was rational response to $360/hour, not personality. Change the economics, change the culture. `[ps=5]`
- Cosmos showed the right answer to Brooks's Law was tools that made each programmer more powerful, not more programmers. `[ps=5]`
- Software is a model of a much messier physical world; the Cumberland Farms and Marine Midland projects drove this lesson home. `[ps=5]`
- Systems with two-digit year fields stored year 2000 as '00', interpreted as 1900—a design choice consistent with 1960s storage economics. `[ps=5]`
- COBOL was the primary language for large application systems at commercial service bureaus in 1969; teams wrote it by hand one procedure at a time. `[ps=5]`
- By 2020s, compute is near-free and human talent is the scarce resource—the inverse of 1969. `[ps=4]`
- IBM instruction to set binary flag in register directly without touching memory; replaced 3 memory references with 1 instruction—transformative at scale. `[ps=4]`
- Timesharing (terminal-based interactive coding) existed at universities and research labs in 1969 but was not typical at commercial service bureaus. `[ps=4]`
- Every submission was a financial event; discipline of thinking through problems completely before submission was rigorous in ways instant-feedback IDEs don't replicate. `[ps=4]`
- Cosmos was an early form of low-code development, enabling PHI to deploy systems at scale and speed impossible with conventional programming teams. `[ps=4]`
- Cosmos allowed PHI to deploy systems at a scale and speed impossible with conventional programming teams; a force multiplier. `[ps=4]`
- 'The physics of the machine were now in my bones. It was time to learn the physics of organizations.' `[ps=4]`
- IBM System/360 family was the dominant platform at commercial service bureaus in late 1960s; reference card was primary programmer documentation. `[ps=4]`
- Efficiency culture at PHI was direct product of $360/hour economics: when machine time is scarce, programmer's job is to minimize consumption of it. `[ps=4]`
- Efficiency was not an engineering preference; it was economic survival at $360/hour. Unnecessary instructions were a small theft from the company budget. `[ps=3]`
- July 1969; while Apollo 11 transfixed the world, Kastner was fixing a Y2K-class two-digit-year bug in Marine Midland Bank's bond portfolio system. `[ps=3]`
- Two-digit year field: 30-year bond issued in 1970 maturing in 2000 would be recorded as '00', read as 1900. Kastner expanded field to fix it. `[ps=3]`
- Code generator sidesteps Brooks's Law coordination overhead; produces code faster than any team with perfect architectural consistency—a force multiplier. `[ps=3]`
- Working on Cosmos was 'genuinely exciting—the closest I had come so far to the automation dream'—building a machine that built other machines. `[ps=3]`
- Kastner had nothing against Wang Laboratories; called it 'a remarkable company'—and noted Moros provided key technical leadership for An Wang's computing initiatives. `[ps=3]`
- In 1969, most large apps were built by teams writing COBOL by hand one procedure at a time; Cosmos automated this with perfect architectural consistency. `[ps=3]`
- Frederick Brooks argued adding programmers to a late project makes it later; coordination cost grows faster than productivity added. Code generation sidesteps this. `[ps=3]`
