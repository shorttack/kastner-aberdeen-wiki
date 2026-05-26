---
title: "Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987)"
slug: volume-1-ch05-stratus-fault-tolerant-wars-1981-1987
page_type: chapter
author: "Peter S. Kastner"
date: "2026-05-14"
study_type: memoir
subject_domain: "memoir/volume-1"
methodology: "oral-history"
importance: high
importance_rationale: "Provides a rare insider account of Stratus Computer's early marketing strategy and the IBM OEM deal, capturing pivotal moments in fault-tolerant computing history from a senior participant."
relevance: high
relevance_rationale: "Directly covers the OLTP, fault-tolerant computing market, and ATM/financial-services IT segments with specific product, competitor, customer, and deal details relevant to 1980s technology industry analysis."
prescience: high
prescience_rationale: "Kastner's 1987 ghostwritten report predicted microprocessor-based OLTP price-performance explosion and mainframe displacement — a forecast confirmed by subsequent market history; his telecom pivot insight foreshadowed Stratus's long-term trajectory."
license: CC-BY-4.0
tier: 1
entity_count: 21
tech_count: 17
obs_count: 100
tags: [type/chapter, importance/high, prescience/high, decade/2020s]
source_csv: master_studies.csv
---

# Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987)

> Peter S. Kastner recounts his six years (1981–1987) as Manager of Marketing Development at Stratus Computer in Natick, MA, where he helped market a hardware-based fault-tolerant computing architecture competing primarily against Tandem Computers and IBM. The chapter traces key milestones including the IBM OEM deal (branding Stratus FT200 as the IBM System/88), the NORAD Cheyenne Mountain contract, and a telecom market breakthrough sparked by a hallway observation about Rolm PBX systems. Kastner distills enduring marketing lessons about quantifying downtime economics, physical demonstration as proof, and finding non-obvious market angles.

**Author:** Peter S. Kastner · **Date:** 2026-05-14 · **Type:** memoir
**Importance:** high — *Provides a rare insider account of Stratus Computer's early marketing strategy and the IBM OEM deal, capturing pivotal moments in fault-tolerant computing history from a senior participant.*
**Prescience:** high — *Kastner's 1987 ghostwritten report predicted microprocessor-based OLTP price-performance explosion and mainframe displacement — a forecast confirmed by subsequent market history; his telecom pivot insight foreshadowed Stratus's long-term trajectory.*

## Entities (21)

- [[ascend-communications|Ascend Communications]]
- [[cisco|Cisco Systems]]
- [[dec|Digital Equipment Corporation]]
- [[gardner-c-hendrie|Gardner Hendrie]]
- [[gte-sylvania|GTE Sylvania]]
- [[honeywell|Honeywell]]
- [[ibm|IBM]]
- [[jim-treybig|Jim Treybig]]
- [[john-logan|John Logan]]
- [[john-morgridge|John Morgridge]]
- [[kate-morgridge|Kate Morgridge]]
- [[mitre-corporation|Mitre Corporation]]
- [[norad|NORAD (North American Aerospace Defense Command)]]
- [[nortel-networks|Nortel]]
- [[peter-s-kastner|Peter S. Kastner]]
- [[prime-computer|Prime Computer]]
- [[rolm-corporation|Rolm Corporation]]
- [[stratus-computer|Stratus Computer]]
- [[systems-development-corporation|Systems Development Corporation]]
- [[tandem-computers|Tandem Computers]]
- [[yankee-group|Yankee Group]]

## Technologies (17)

- [[cobol|COBOL]]
- [[fault-tolerant-architecture|Lockstep Fault-Tolerant Architecture]]
- [[fault-tolerant-computing|Fault-Tolerant Computing]]
- [[fortran|FORTRAN]]
- [[ft-systems-1986-forecast|Fault-Tolerant Systems Market Forecast]]
- [[hardware-fault-tolerance|Hardware Fault Tolerance]]
- [[ibm-4300|IBM 4300 Series]]
- [[ibm-stratus-oem|IBM-Stratus OEM Agreement]]
- [[ibm-system-88|IBM System/88]]
- [[moore-law|Moore's Law]]
- [[motorola-68020|Motorola 68020]]
- [[nonstop-architecture|NonStop Architecture (Tandem)]]
- [[oltp|OLTP (Online Transaction Processing)]]
- [[oltp-45pct-growth-forecast|Future of Transaction Processing (1987 Report)]]
- [[ss7|SS7 (Signaling System No. 7)]]
- [[stratus-ft200|Stratus FT200]]
- [[stratus-xa2000|Stratus XA 2000]]

## Key observations (top 50)

- **1981** — Hire date and role at Stratus: Joined Stratus Computer on November 1, 1981 as Manager of Marketing Development, six weeks before product launch.
- **1981** — Product launch timing: First product announced December 1981, six weeks after Kastner joined.
- **1981** — Kastner's role description: Hired to translate radical engineering into a market-moving story before product was public; 'I landed running.'
- **1981** — Mainframe reliability problem: IBM 4300 would crash on component failure; recovery window of 30 minutes was unacceptable for ATM, airline reservations, stock trading.
- **1981** — Tandem NonStop architecture approach: Software-based fault tolerance using pairs of processors; programmers had to write explicit 'checkpointing' code for backup processor handoff.
- **1981** — Tandem cost assessment: Technically sound but expensive in the currency that mattered most: programmer time.
- **1974** — Tandem founding: Founded in 1974 in Cupertino, CA.
- **1981** — Stratus lockstep architecture design: Four physical microprocessors arranged in two pairs; hardware comparator checks results continuously; failed pair taken offline without losing a single clock cycle.
- **1981** — Hardware vs software fault tolerance distinction: Stratus hardware fault tolerance hides failures from software entirely; application runs without awareness of failure event.
- **1981** — Fault tolerance business case framework: Calculate cost of downtime per hour, compare to price premium for fault-tolerant hardware, determine when the math works.
- **1981** — Pull-the-plug demonstration concept: Prospects invited to pull a CPU board from a running system during transaction processing; system kept running, red LED lit on failed component.
- **1981** — Demo theater vs. white papers: 'Ten seconds of theater replaced fifty pages of white papers.'
- **1981** — Launch eve demo crisis: VP Hardware Gardner Hendrie could not reliably pull a board without crashing the system evening before public launch.
- **1981** — Lexan static electricity failure mode: Shiny Lexan plastic covers on circuit boards generated static electricity when pulled; carpet doused with water solved launch-day problem; ECO #1 replaced Lexan with cardboard.
- **1981** — First engineering change order: Engineering Change Order #1 replaced elegant Lexan plastic board covers with cardboard to eliminate static electricity risk.
- **1982** — Downtime cost marketing approach: Asked customers: 'What does one hour of downtime cost you?' — shifted IT managers from thinking about performance/capacity to quantifying availability.
- **1982** — ATM downtime revenue loss example: ATM network processing 10,000 transactions/hour at $40 average value: straightforward arithmetic for cost-per-hour of downtime.
- **1982** — Industry-specific downtime calculators: Created direct-mail pieces with cost-of-downtime calculators customized by industry; banking, brokerage, retail POS all covered.
- **1983** — Competitive displacement program against Tandem: Ran competitive displacement programs targeting Tandem users frustrated by NonStop programming complexity; message: 'Keep your programmers. Change your hardware.'
- **1986** — IBM OEM deal initiation: IBM came to Stratus after being nudged; IBM sales force watching enterprise customers evaluate fault-tolerant systems with nothing to offer them.
- **1986** — IBM System/88 branding: IBM agreed to rebrand the Stratus FT200 as the IBM System/88; Stratus marketing shifted to anchor: 'The Technology IBM Chose.'
- **1986** — IBM OEM deal vendor-risk neutralization: 'The Technology IBM Chose' neutralized every startup-risk objection; IBM brand eliminated uncertainty about Stratus viability.
- **1986** — IBM OEM deal significance — IBM side: IBM putting its name on a startup's product because it had no competitive alternative; validated Stratus without money buying such validation.
- **1986** — IBM-Stratus channel conflict challenge: IBM salesforce carried System/88 competing with conventional IBM mainframes in some use cases; Kastner developed 'battlecard' materials explaining swim lanes.
- **1986** — Battlecard as conflict-resolution document: Battlecards for IBM System/88 vs IBM 3090 were essentially conflict-resolution documents for a company simultaneously distributor and competitor.
- **1984** — Banking/financial services as fault-tolerant battleground: By mid-1980s principal battlefield was banking/financial services; ATM networks and POS authorization systems expanding rapidly; Tandem and Stratus competed for every significant deal.
- **1984** — Tandem competitive argument: Tandem claimed Stratus hardware approach was brute-force redundancy; Stratus countered that Tandem's architectural elegance was paid for by every developer writing recovery code.
- **1984** — Maintenance model innovation: Turned hardware redundancy into a maintenance model: 'the board that mails itself' — pull failed board while system runs, mail it back, no on-site engineer.
- **1984** — Zero-code advantage positioning: 'Zero-code advantage': on Stratus/System/88, standard COBOL or FORTRAN worked with fault tolerance as invisible infrastructure; no specialized NonStop programmers needed.
- **1984** — 5-year TCO comparison vs Tandem: Total cost of ownership over five years including programmer time, training, ongoing maintenance often reversed hardware price advantage in Stratus's favor.
- **1984** — Men's room market pivot: Made pivotal Stratus telecom market recommendation in a men's room; observed Rolm PBX systems needed exactly the reliability Stratus provided.
- **1984** — Telecom always-on requirement: Rolm digital PBX switching millions of calls was an always-on application; telecom had highest cost of downtime of any industry.
- **1985** — Stratus telecom market entry: Stratus became embedded infrastructure for SS7 signaling and emerging digital switching systems; five-nines uptime (99.999%, <6 min downtime/year) was entry requirement.
- **1985** — Five-nines uptime requirement: 99.999% uptime — less than six minutes of downtime per year — was entry requirement for telecom contracts, not a sales argument.
- **1987** — Stratus telecom trajectory: Telecom DNA built in those years would define Stratus's long-term trajectory, leading to acquisition by Ascend and eventual integration into Nortel.
- **1982** — Mitre Corporation cold call: Received cold call to present at Mitre Corporation in 1982; fifty silent engineers; declined to state requirements; Kastner had one hour.
- **1982** — Mitre presentation strategy: Kastner chose not to pitch fault tolerance alone; covered full architecture — communications controllers, modularity, data protocols, spares strategy — inferring complex defense integration need.
- **1982** — Mitre-to-NORAD chain: Mitre brought in GTE Sylvania and Systems Development Corporation; extended procurement process led to landmark NORAD contract.
- **1982** — GTE Sylvania role in NORAD deal: Brought in by Mitre as part of procurement chain for NORAD Cheyenne Mountain contract.
- **1982** — Systems Development Corporation role in NORAD deal: Brought in alongside GTE Sylvania by Mitre as part of NORAD procurement chain.
- **1987** — NORAD contract value — hardware: $10 million in systems hardware delivered to Cheyenne Mountain, Colorado by late 1980s.
- **1987** — NORAD contract value — spares: $40 million in spares delivered to Cheyenne Mountain, Colorado by late 1980s.
- **1987** — NORAD total contract value: $50 million total ($10M hardware + $40M spares) for granite-shielded Cheyenne Mountain nerve center monitoring skies for nuclear threats.
- **1985** — NORAD reference customer value: If the US Air Force trusted this machine inside a mountain during a nuclear threat, it could handle a department store's credit card authorizations.
- **1984** — John Morgridge background: VP of Sales and Marketing at Stratus; ex-Honeywell; direct, likable, very funny; later became Cisco's first non-founder CEO.
- **1984** — Cisco CEO trajectory: John Morgridge later became Cisco's first non-founder CEO and built that company into a generation-defining enterprise.
- **1984** — Kate Morgridge trade show assignment: John Morgridge arranged for daughter Kate to run trade shows for Kastner after Kastner spent 2.5 years running the program.
- **1984** — Kate Morgridge performance assessment: Turned out to be excellent — organized, energetic, genuinely good at the work.
- **1984** — T-shirt incident at trade show: At first show wore T-shirt reading 'Stratus Computers Never Go Down On You' to a union work-site; taught her about human nature in 1980s tech industry.
- **1987** — XA 2000 announcement role: Kastner led market and product team for XA 2000 announcement before departing; machines built on Motorola 68020 processors.

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'volume-1-ch05-stratus-fault-tolerant-wars-1981-1987' ORDER BY year_observed;
```

