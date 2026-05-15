---
title: "Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)"
slug: 07-pools-of-storage-functional-spec-597fa5
page_type: study
author: "Peter Kastner (executive sponsor); Jay Erikson (primary author)"
date: "2003-11-26"
study_type: employer-record
subject_domain: "midline-storage / ILM / software-development / Aberdeen-internal"
methodology: "document-review"
importance: high
importance_rationale: "Primary internal specification document for the most innovative deliverable in the Aberdeen-Maxtor engagement — the first Aberdeen research-delivery-by-simulation tool. Contains frank internal commentary not meant for the client including notes on content development cost control and future product roadmap for superimposing benchmark data. Represents Aberdeen's first attempt at a guided decision support tool for category marketing."
relevance: high
relevance_rationale: "The functional specification describes a decision support tool architecture (guided workflow + maturity grid + KPI analysis + Case for Action PDF output) that is recognizable in modern SaaS marketing tools assessment tools and maturity model platforms. The lead generation model (registration gating + rich user data to client) is still the standard model for gated B2B tools."
prescience: not-applicable
prescience_rationale: "The functional specification itself makes no market predictions — it is a software requirements document. The forward-looking innovation is the product concept itself (research-as-simulation). Prescience of the broader decision tool concept is addressed in File 6 (After-Action) observations."
license: CC-BY-4.0
tier: 1
entity_count: 11
tech_count: 6
obs_count: 20
tags: [type/study, importance/high, prescience/not-applicable, decade/2000s]
source_csv: master_studies.csv
---

# Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)

> Internal Aberdeen Group functional specification for the Pools of Storage Decision Tool — explicitly marked 'Do Not Share With Maxtor.' Version 1.0 dated November 25 2003 describing a guided decision support web application built in Microsoft ASP/SQL Server 2000 targeting Internet Explorer 5.5+ on Windows. The tool has four stages: Solution Workflow (recommend business process); Competitive Workflow (maturity grid positioning); Financial Framework (KPI analysis); and Case for Action (ROI/TCO calculation with PDF output). Planned development cost $23101.55 over 6 weeks with Aberdeen hosting 3 months.

**Author:** Peter Kastner (executive sponsor); Jay Erikson (primary author) · **Date:** 2003-11-26 · **Type:** employer-record
**Importance:** high — *Primary internal specification document for the most innovative deliverable in the Aberdeen-Maxtor engagement — the first Aberdeen research-delivery-by-simulation tool. Contains frank internal commentary not meant for the client including notes on content development cost control and future product…*
**Prescience:** not-applicable — *The functional specification itself makes no market predictions — it is a software requirements document. The forward-looking innovation is the product concept itself (research-as-simulation). Prescience of the broader decision tool concept is addressed in File 6 (After-Action) observations.*

## Entities (11)

- [[aberdeen-group|Aberdeen Group]]
- [[beth-conant|Beth Conant]]
- [[david-hill|David Hill]]
- [[jay-erikson|Jay Erikson]]
- [[john-boyne|John Boyne]]
- [[john-mclaughlin|John McLaughlin]]
- [[kerri-conrad|Kerri Conrad]]
- [[maxtor|Maxtor Corporation]]
- [[michael-beganny|Michael Beganny]]
- [[peter-kastner|Peter S. Kastner]]
- [[stan-elbaum|Stan Elbaum]]

## Technologies (6)

- [[aberdeen-maturity-grids|Aberdeen Maturity Grid Framework]]
- [[asp-microsoft|Microsoft Active Server Pages (ASP)]]
- [[internet-explorer|Internet Explorer 5.5+]]
- [[pos-decision-tool|Pools of Storage Decision Tool]]
- [[sql-server-2000|Microsoft SQL Server 2000]]
- [[windows-2000-server|Windows 2000 Server]]

## Key observations (top 25)

- **2003** — Tool confidentiality status: Aberdeen internal use only — under no circumstances to be shared with client Maxtor; separate sanitized version is the official public functional specification
- **2003** — Tool architecture — 4 stages: Stage 1: Solution Workflow (recommend business process); Stage 2: Competitive Workflow (maturity grid positioning); Stage 3: Financial Framework (KPI analysis); Stage 4: Case for Action (ROI/TCO output)
- **2003** — Tool development cost: $23101.55 planned development cost (strictly for development and review; excludes content development support and maintenance)
- **2003** — Tool development schedule: 6 weeks: Monday November 24 2003 to Friday January 16 2004
- **2003** — Technology stack choice: Microsoft ASP connecting to SQL Server 2000 on Windows 2000 Servers; IE 5.5+ on Windows; no plugins required
- **2003** — Lead generation purpose: Tool generates spreadsheet of registration data and user activity; business case printout/PDF for user's assumptions inputs and recommendations
- **2003** — Session architecture — no persistence: No user persistence; if user terminates before completing all stages user must start over; sequential navigation only
- **2003** — Hosting arrangement: Aberdeen provides 3 months hosting; Maxtor can assume hosting or initiate extended agreement with Aberdeen
- **2003** — Maturity grid content requirements: 18 maturity grids required for tool; developed by David Hill Beth Conant and contractor; due December 31 2003
- **2003** — KPI and business logic ownership: Stan Elbaum responsible for Solution Workflow questions (5 questions/5 pools of answers); KPI indicators and calculations; all due December 31 2003
- **2003** — Solution Workflow — 5 screening questions: What is your ecosystem? What is your role in that ecosystem? What is the asset base of your company? What is your geographical supply chain footprint? How customized are your solutions?
- **2003** — Financial Framework — KPI inputs: User enters two numbers (numerator and denominator of KPI ratio); system displays KPI boundaries for maturity positions; risk/return analysis with conservative/normal/aggressive options
- **2003** — Case for Action output content: Displays optimal financial results (operating profit + annual cash flow + one-time cash flow); desired to-be state; action items; Pools of Storage storage recommendations; generates PDF take-away
- **2003** — Future roadmap — benchmark data overlay: Future version of tool may superimpose benchmark data on Competitive Framework Diffusion chart if user chooses — design for this future now
- **2003** — Content updates as paid service: Content updates may be sold as an update service to Maxtor — no content management system; all content manually entered into database
- **2003** — Tool success criteria — 5 dimensions: Demonstrate PoS ROI/TCO best practices; reinforce Maxtor's PoS strategy and lexicon; perform at Aberdeen/Maxtor quality level; generate highly qualified information-rich leads from users; build credibility with Maxtor
- **2003** — Maturity grid position calculation: System calculates survey position by adding characteristic weightings for all answers then dividing by total possible points; position with highest percent is Survey Position
- **2003** — Document version control process: Living document; version changes tracked in Version Control table; document renamed by appending latest version number; original: PoS Functional Spec v1.0.doc dated 11/25/03
- **2003** — Performance target for hosting: Designed to run on 52Kbps dial-up; server holds X user threads; 15-minute session timeout per screen
- **2003** — Document feedback contact: Feedback to Jay Erikson at 970-232-7008 or Jay.Erikson@Aberdeen.com

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = '07-pools-of-storage-functional-spec-597fa5' ORDER BY year_observed;
```

