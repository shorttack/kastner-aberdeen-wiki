---
title: "nVidia Personal Cinema 1.0 — Aberdeen Lab Report"
slug: nvidia-personal-cinema-lab-report-2002
page_type: study
author: "Peter S. Kastner"
date: "2002-01-17"
study_type: topic-analysis
subject_domain: "topic/personal-pcs"
methodology: "benchmarking, field-research, document-review"
importance: medium
importance_rationale: "Primary-source vendor-directed lab feedback documenting early-2002 state of consumer PC video/capture integration under Windows XP."
relevance: medium
relevance_rationale: "Useful historical reference for consumer DVR/HTPC integration usability — specifics dated but workflow observations remain instructive."
prescience: high
prescience_rationale: "Correctly predicted (a) that consumers would click-through PCfriendly install warnings (broadly true across DRM-tied video), and (b) that Movie Maker ease-of-use 'must be reckoned with' — MS Movie Maker did become the lowest-friction consumer editor of the era."
license: CC-BY-4.0
tier: 1
entity_count: 12
tech_count: 14
obs_count: 23
tags: [type/study, importance/medium, prescience/high, decade/2000s]
source_csv: master_studies.csv
---

# nVidia Personal Cinema 1.0 — Aberdeen Lab Report

> Aberdeen Group laboratory feedback report to nVidia management on 16 hours of hands-on testing of the Personal Cinema 1.0 kit (Compro GeForce2 MX 400 graphics card with VIVO breakout box) on a Dell 8100 running Windows XP. Evaluates graphics, TV tuner via WinDVR, DVD playback via WinDVD, Ulead Video Wave 4, and Microsoft Movie Maker workflows, and recommends packaging, cabling, and software-install improvements.

**Author:** Peter S. Kastner · **Date:** 2002-01-17 · **Type:** topic-analysis
**Importance:** medium — *Primary-source vendor-directed lab feedback documenting early-2002 state of consumer PC video/capture integration under Windows XP.*
**Prescience:** high — *Correctly predicted (a) that consumers would click-through PCfriendly install warnings (broadly true across DRM-tied video), and (b) that Movie Maker ease-of-use 'must be reckoned with' — MS Movie Maker did become the lowest-friction consumer editor of the era.*

## Entities (12)

- [[aberdeen-group|Aberdeen Group]]
- [[ati-technologies|ATI Technologies]]
- [[att-broadband|AT&T Broadband]]
- [[compro-technology|Compro Technology]]
- [[dell|Dell]]
- [[intervideo|InterVideo]]
- [[microsoft|Microsoft]]
- [[nvidia|NVIDIA Corporation]]
- [[philips|Royal Philips]]
- [[scientific-atlanta|Scientific Atlanta]]
- [[sony|Sony]]
- [[turtle-beach|Turtle Beach]]

## Technologies (14)

- [[agp-4x|AGP 4x]]
- [[ati-radeon-32-ddr|ATI Radeon 32 DDR]]
- [[intel-pentium-4|Intel Pentium 4]]
- [[microsoft-movie-maker|Microsoft Movie Maker]]
- [[nvidia-geforce2-mx-400|nVidia GeForce2 MX 400]]
- [[nvidia-personal-cinema|nVidia Personal Cinema 1.0]]
- [[pc-friendly|PCfriendly DVD software]]
- [[rdram|RDRAM]]
- [[s-video|S-Video]]
- [[ulead-videowave|Ulead Video Wave 4]]
- [[vivo-breakout-box|VIVO (Video-In/Video-Out) breakout box]]
- [[windows-xp|Windows XP]]
- [[windvd|InterVideo WinDVD]]
- [[windvr|InterVideo WinDVR]]

## Key observations (top 25)

- **2001** — Test duration: 16 hours over 3 days in December 2001
- **2001** — Lab PC configuration: Dell 8100 / P4 1.4 GHz / 384 MB RDRAM / current BIOS / Windows XP
- **2001** — Physical install: Easy; did not require metal bar used for ATI Radeon
- **2001** — VIVO cable labeling: Two different connectors poorly labeled; low-contrast tape easily missed
- **2001** — Recommendation — cabling: Use high-contrast or different-color tape; add 90-degree connector at card end
- **2001** — Software install: Required unexpected manual hard reboot before drivers installed correctly
- **2001** — Gaming performance: Comanche 4 and Ghost Recon — default and gamer settings — met ratings
- **2001** — TV-tuner CPU load: ~15% of Pentium 4 1.4 GHz
- **2001** — TV quality — windowed: Excellent analog quality in partial-screen
- **2001** — TV quality — fullscreen: Adequate at normal distance; not as satisfying as DVD playback
- **2001** — Stereo/mono defect: Television tab defaults to mono despite repeated stereo selection
- **2001** — DVD playback quality: Excellent full-screen video across tested DVDs
- **2001** — Interop defect: PCfriendly installs software that conflicts with WinDVD; causes dropped frames
- **2001** — User-click prediction: All consumers will click 'yes' on PCfriendly install — high nVidia support-call volume expected
- **2001** — Video Wave 4 onboarding: Documentation and video tours inadequate for new users
- **2001** — Movie Maker integration: Does not reliably/automatically set up with Personal Cinema; video-configure choices randomly missing
- **2001** — Movie Maker market weight: Ships with every Windows XP PC — nVidia wise to ensure seamless out-of-box Personal Cinema support
- **2001** — Audio hookup critique: Stereo-receiver configuration was overly ambitious; required hours of debugging and careful volume calibration
- **2001** — Install-sequence defect: WinDVD install failed because prior ATI WinDVD was not uninstalled first; blank Company field not accepted; '0'/'O' serial-number confusion
- **2001** — Teletext app defect: Restart prompt appeared before teletext install completed; 45-minute shutdown hang observed
- **2001** — Support-contact gap: No address or phone number for Compro on packaging — all calls presumed to go to nVidia
- **2001** — Overall verdict: High marks for hardware and packaging; software install integration needs improvement
- **2003** — Prediction outcome — PCfriendly: [UNVERIFIED]

## DuckDB query for full observation set

```sql
SELECT * FROM observations WHERE study_id = 'nvidia-personal-cinema-lab-report-2002' ORDER BY year_observed;
```

