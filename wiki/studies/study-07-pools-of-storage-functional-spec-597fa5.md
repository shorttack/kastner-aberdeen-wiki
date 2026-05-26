---
title: "Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)"
slug: "study-07-pools-of-storage-functional-spec-597fa5"
page_type: "study"
tags: ["type/study", "collection/employer-record"]
tier: 2
source_csv: "_master_studies.csv"
study_id: "07-pools-of-storage-functional-spec-597fa5"
author: "Peter Kastner (executive sponsor); Jay Erikson (primary author)"
date: "2003-11-26"
pub_year: 2003
type: "employer-record"
subject_domain: "midline-storage / ILM / software-development / Aberdeen-internal"
methodology: "document-review"
source_file: "07-Pools-of-Storage-Functional-Spec.txt"
license: "CC-BY-4.0"
importance: "high"
relevance: "high"
study_prescience_enum: "not-applicable"
prescience_max: null
prescience_mean: null
prescience_obs_count: 0
---

# Pools of Storage Decision Tool — Functional Specification (Aberdeen Internal)

> Internal Aberdeen Group functional specification for the Pools of Storage Decision Tool — explicitly marked 'Do Not Share With Maxtor.' Version 1.0 dated November 25 2003 describing a guided decision support web application built in Microsoft ASP/SQL Server 2000 targeting Internet Explorer 5.5+ on Windows. The tool has four stages: Solution Workflow (recommend business process); Competitive Workflow (maturity grid positioning); Financial Framework (KPI analysis); and Case for Action (ROI/TCO calculation with PDF output). Planned development cost $23101.55 over 6 weeks with Aberdeen hosting 3 months.


_Published 2003, author **Peter Kastner (executive sponsor); Jay Erikson (primary author)**, type **employer-record**._


## Top observations

- Aberdeen internal use only — under no circumstances to be shared with client Maxtor; separate sanitized version is the official public functional specification
- Stage 1: Solution Workflow (recommend business process); Stage 2: Competitive Workflow (maturity grid positioning); Stage 3: Financial Framework (KPI analysis); Stage 4: Case for Action (ROI/TCO output)
- $23101.55 planned development cost (strictly for development and review; excludes content development support and maintenance)
- 6 weeks: Monday November 24 2003 to Friday January 16 2004
- Microsoft ASP connecting to SQL Server 2000 on Windows 2000 Servers; IE 5.5+ on Windows; no plugins required
- Tool generates spreadsheet of registration data and user activity; business case printout/PDF for user's assumptions inputs and recommendations
- No user persistence; if user terminates before completing all stages user must start over; sequential navigation only
- Aberdeen provides 3 months hosting; Maxtor can assume hosting or initiate extended agreement with Aberdeen
- 18 maturity grids required for tool; developed by David Hill Beth Conant and contractor; due December 31 2003
- Stan Elbaum responsible for Solution Workflow questions (5 questions/5 pools of answers); KPI indicators and calculations; all due December 31 2003
- What is your ecosystem? What is your role in that ecosystem? What is the asset base of your company? What is your geographical supply chain footprint? How customized are your solutions?
- User enters two numbers (numerator and denominator of KPI ratio); system displays KPI boundaries for maturity positions; risk/return analysis with conservative/normal/aggressive options
- Displays optimal financial results (operating profit + annual cash flow + one-time cash flow); desired to-be state; action items; Pools of Storage storage recommendations; generates PDF take-away
- Future version of tool may superimpose benchmark data on Competitive Framework Diffusion chart if user chooses — design for this future now
- Content updates may be sold as an update service to Maxtor — no content management system; all content manually entered into database
- Demonstrate PoS ROI/TCO best practices; reinforce Maxtor's PoS strategy and lexicon; perform at Aberdeen/Maxtor quality level; generate highly qualified information-rich leads from users; build credibility with Maxtor
- System calculates survey position by adding characteristic weightings for all answers then dividing by total possible points; position with highest percent is Survey Position
- Living document; version changes tracked in Version Control table; document renamed by appending latest version number; original: PoS Functional Spec v1.0.doc dated 11/25/03
- Designed to run on 52Kbps dial-up; server holds X user threads; 15-minute session timeout per screen
- Feedback to Jay Erikson at 970-232-7008 or Jay.Erikson@Aberdeen.com
