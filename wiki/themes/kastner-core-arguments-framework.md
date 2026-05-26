---
title: "Kastner's Core Arguments and Framework"
slug: kastner-core-arguments-framework
page_type: theme
tier: 1
study_type: framework-synthesis
audience: industry-analyst-peers
tags: [type/theme, type/framework, theme/core-arguments, theme/archive-as-protagonist, theme/wiki-driven-replication]
date_built: 2026-05-16
build_software: perplexity-computer
archive_study_id: 2026-kastner-core-arguments-framework-0b0c6b
total_arguments: 12
memoir_canonical: 7
derived: 5
total_supporting_observations: 1606
verified_plus_high_obs: 1385
partial_obs: 25
refuted_obs: 6
exemplar_studies_cited: 53
span_decades: "1960s-2020s"
companion_studies:
  - "[[kastner-prescience-methodology-demo]]"
  - "[[kastner-top-100-economic-calls]]"
  - "[[volume-1-ch10-the-long-view-1966-2026]]"
---

# Kastner's Core Arguments and Framework

## A Wiki-Driven Synthesis from the Aberdeen-Group-Archive

> **Note on framing.** This page is not a biography or a manifesto. It is a **queryable framework** — twelve recurring arguments running through Kastner's 1969–2026 career, each bound to a filter spec that returns the supporting observations from the archive's master tables. Every claim here is empirically self-defending: criticism must engage with specific rows, not assertions.

This is the second study in the archive built on the [[kastner-prescience-methodology-demo|archive-as-protagonist]] convention. The first established that the archive can be queried as a primary-source research instrument. This one extends the convention from methodology demonstration to **framework synthesis**.

---

## 1. The twelve arguments at a glance

Seven are memoir-canonical — they are Kastner's "Seven Patterns That Recur" articulated in [[volume-1-ch10-the-long-view-1966-2026|Chapter 10 of the 2026 memoir]]. Five are derived: supported by the archive but not explicitly named as patterns in Chapter 10.

| # | Argument | Pop | Verified+High | Refuted | Source |
|---:|---|---:|---:|---:|:---:|
| 1 | Economic winner displaces technical winner | 360 | 307 | 4 | memoir |
| 2 | Proprietary platforms fund their own displacement | 197 | 169 | 1 | memoir |
| 3 | Adoption timelines always longer than predicted | 26 | 25 | 0 | memoir |
| 4 | The integration problem is permanent | 148 | 125 | 0 | memoir |
| 5 | Data advantage compounds | 252 | 192 | 0 | memoir |
| 6 | Failure mode is almost never technical | 67 | 63 | 0 | memoir |
| 7 | The machine was never the hard part | 37 | 36 | 0 | memoir |
| 8 | Reliability is sold to buying committees, not engineers | 195 | 175 | 0 | derived |
| 9 | Categories must be created before they can be sold | 103 | 90 | 0 | derived |
| 10 | Analyst credibility is earned with named winners, dates, and numbers | 175 | 158 | 0 | derived |
| 11 | Free research is the marketing asset | 11 | 11 | 0 | derived |
| 12 | Compute scarcity has inverted; judgment is now the scarce resource | 35 | 34 | 0 | derived |
| **Total** | | **1,606** | **1,385** | **6** | |

Combined verified + high + partial: **1,410 (87.8%)**. Refuted: **6 (0.37%)**, all isolated to ARG-1 and ARG-2.

---

## 2. Argument scaffold

Every ARG carries seven fields. The structure makes the framework queryable and self-auditing.

| Field | Purpose |
|---|---|
| **Claim** | One sentence; the position being argued |
| **Mechanism** | Why it is true; how the argument derives from the archive |
| **Filter spec** | Python-style query against `_master_observations.csv` returning supporting rows |
| **Population** | Count of matching observations + confidence histogram + decade span |
| **Named exemplars** | Three to six specific `obs_id` citations as anchors |
| **Counter-evidence** | Observations that refute or strain the argument — preserved, not suppressed |
| **Wiki linkage** | Obsidian `[[wikilinks]]` to proof studies for deeper reading |

Anyone disputing a claim can re-run its filter and inspect the universe. Anyone extending the framework can add a new ARG with its own filter and watch its population evolve as the archive grows.

---

## 3. The arguments

### ARG-1 — Economic winner displaces technical winner

**Claim.** When two technologies compete and one is technically superior while the other has economic advantage (volume, price, distribution), the economic winner takes the durable category.

**Mechanism.** Distribution economics, network effects, and committee-driven procurement favor the lower-cost-per-unit option once the technical floor is acceptable. Engineers who pick the technical winner are overruled by procurement, finance, and committees who pick the economic winner.

**Filter spec.**
```
observation_type IN ('actual-outcome','viability-prediction')
AND text_contains('displace','succeed','outsell','market leadership',
                  'de facto','volume','consolidate')
```

**Population.** 360 rows; verified 118 / high 189 / partial 9 / medium 37 / low 2 / refuted 4. Span: 1960s–2020s (peaks 2000s n=134, 1990s n=85).

**Named exemplars.**
- `1996-sequent-38f0b1` → OBS-027 — NUMA in x86 (Opteron, Xeon adopt as standard) — verified
- `1997-ca-s-unicenter-tng-framework-pk-apr-50d15f` → OBS-017 — framework de facto standard — verified
- `1997-microsoft-nt-scalability-day--the-e-6460e2` → OBS-017 — NT enterprise outcome — verified
- `2001-aberdeen-group-recent-publications-psk-2be54d` → OBS-009 — Palm OS market leadership outcome — verified
- `2001-hp-cpq-merger-collection-edbca1` → OBS-027 — Itanium outcome — verified
- `2002-beyond-windows-8-way-servers-...-6828b2` → OBS-011 — server consolidation outcome — verified

**Counter-evidence.**
- `1999-uit15p-ca-unicenter-infrastructure-psk-d88ad8` → OBS-018 — vendor-backed architected infrastructure
- `dct-microsoft-homestation-notes-2002` → OBS-015 — Mira outcome
- `remarks-of-peter-kastner-to-the-massachu-96335b` → OBS-013 — Intel xScale divested

**Proof studies.** [[1996-sequent-38f0b1]], [[1997-microsoft-nt-scalability-day]], [[2001-hp-cpq-merger]], [[2002-beyond-windows-8-way-servers]], [[2010-x86-everywhere]]

---

### ARG-2 — Proprietary platforms fund their own displacement

**Claim.** The cash flow that funds proprietary platform dominance also underwrites the tooling, standards, and skills that enable the commodity replacement.

**Mechanism.** Proprietary platform revenues underwrite the broader ecosystem investment in tooling, standards, and skills that enable the commodity replacement. The cash flow that funds dominance also seeds the displacement.

**Filter spec.**
```
observation_type IN ('actual-outcome','viability-prediction','strategic-recommendation')
AND text_contains('open source','commodity','displace','migration',
                  'linux','wintel','x86')
```

**Population.** 197 rows; verified 98 / high 71 / partial 7 / medium 18 / refuted 1. Span: 1980s–2020s (peak 2000s n=85).

**Named exemplars.**
- `1996-sequent-38f0b1` → OBS-028 — ATM market outcome — verified
- `1997-ca-s-unicenter-tng-framework-pk-apr-50d15f` → OBS-017 — framework de facto standard — verified
- `1997-microsoft-nt-scalability-day--the-e-6460e2` → OBS-017 — NT enterprise outcome — verified
- `2001-aberdeen-group-recent-publications-psk-2be54d` → OBS-002 — Linux HPC market dominance — verified
- `2001-hp-cpq-merger-collection-edbca1` → OBS-009 — Linux leadership post-merger — verified
- `2002-undercutting-and-upselling-dell-...-3d70b1` → OBS-017 — PDA category disruption — verified

**Counter-evidence.**
- `1999-uit15p-ca-unicenter-infrastructure-psk-d88ad8` → OBS-018 — vendor-backed architecture adoption

**Proof studies.** [[2001-aberdeen-group-recent-publications-psk]], [[2001-hp-cpq-merger-collection]], [[red-hat-ipo-1999]], [[linux-on-system-z-2002]]

---

### ARG-3 — Adoption timelines always longer than predicted

**Claim.** Technology adoption always takes longer than the forecasts say, by structural factors that do not change.

**Mechanism.** Technology curves are reported in years; org change happens at the pace of payroll, capex cycles, and replacement schedules. The gap between technical readiness and organizational absorption is structural and roughly constant across cycles.

**Filter spec.**
```
observation_type IN ('viability-prediction','actual-outcome','expert-opinion')
AND text_contains('adoption','timeline','years','decade',
                  'slower than','longer than','predicted')
```

**Population.** 26 rows; verified 5 / high 20 / medium 1. Span: 1990s–2020s (peak 2020s n=16). The argument is small in row count because it is meta-pattern: it gets stated explicitly in the memoir and epilogue, not in individual study predictions.

**Named exemplars.**
- `volume-1-ch08-aberdeen-go-go-years-1998-2006` → OBS-067 — Bedard management style — high
- `volume-1-ch10-the-long-view-1966-2026` → OBS-018 — **Pattern 3 named explicitly** — high
- `volume-1-epilogue-argument-with-reality` → OBS-005 — universal pattern of technology adoption — high

**Proof studies.** [[volume-1-ch10-the-long-view-1966-2026]], [[volume-1-epilogue-argument-with-reality]], [[aberdeen-go-go-years-1998-2006]]

---

### ARG-4 — The integration problem is permanent

**Claim.** Each generation of integration tooling solves the previous mismatch and creates a new one. The integration market does not converge.

**Mechanism.** Each generation of integration tooling (EAI, SOA, ESB, microservices, API gateways, MCP) solves the previous generation's mismatch by introducing a new layer that creates its own mismatch with what comes next.

**Filter spec.**
```
observation_type IN ('expert-opinion','actual-outcome','technology-assessment')
AND text_contains('integration','interoperability','accidental architecture',
                  'SOA','EAI','API','middleware','microservices')
```

**Population.** 148 rows; verified 25 / high 100 / partial 3 / medium 17 / low 3. Span: 1980s–2020s (peak 2000s n=83, 1990s n=37).

**Named exemplars.**
- `ca-interbiz-bizworks-profile-054f3c` → OBS-006 — interBiz division outcome — verified
- `lansa-composer-powerpoint-9f4257` → OBS-006 — SOA long-run trajectory — verified
- `q-a-achieving-more-value-from-enterprise-d1d7dd` → OBS-008 — accidental architecture replayed in microservices — verified
- `software-market-safegu~1-ea7453` → OBS-017 — client-server → distributed computing outcome — verified
- `1998-enterprise-application-integration-...-71496c` → OBS-014 — EAI market misunderstanding — high
- `aberdeen-productization-pricing-...-b7b001` → OBS-011 — MAS 14-topic coverage — high

**Proof studies.** [[1998-enterprise-application-integration-advanced-techno]], [[ca-interbiz-bizworks-profile]], [[aberdeen-ra-soa-management-governance-2007]], [[microservices-vs-soa-2018]]

---

### ARG-5 — Data advantage compounds

**Claim.** Once an entity captures the canonical data store for a category, switching costs grow nonlinearly with data accumulation.

**Mechanism.** Customer records, transaction logs, telemetry — every downstream feature anchors on the canonical store. The lock-in is not the schema; it is the observed behavior, the trained pipelines, and the operational scar tissue accumulated against the data.

**Filter spec.**
```
observation_type IN ('expert-opinion','viability-prediction','actual-outcome','strategic-recommendation')
AND text_contains('data','database','customer information','transaction',
                  'warehouse','RDBMS','installed base','feedback loop')
```

**Population.** 252 rows; verified 35 / high 157 / partial 5 / medium 53 / low 1. Span: 1990s–2020s (peak 1990s n=162).

**Named exemplars.**
- `rdbms-for-ibm-powera~1-7a44be` → OBS-026 — Sybase momentum outcome — verified
- `software-market-safegu~1-ea7453` → OBS-013 — ODBMS market outcome — verified
- `technology-themes-2003-04` → OBS-010 — real-time consumer tracking actual outcome — verified
- `1990-bull-rdbms-1990-and-2024-metadata-fe61bf` → OBS-009 — Salomon Brothers RDBMS decision — high
- `1998as400-1-146289` → OBS-030 — application strategy shift — high
- `aberdeen-1995-universal-servers-rdbms-technology-next-decade` → OBS-009 — Universal Server timeline — high

**Proof studies.** [[1990-bull-rdbms-1990-and-2024]], [[1995-universal-servers-rdbms-technology-next-decade]], [[oracle-data-strategy-2008]], [[snowflake-data-cloud-2024]]

---

### ARG-6 — Failure mode is almost never technical

**Claim.** Across actual-outcome rows where a technology failed to deliver promised value, the proximate cause is governance, funding, political compromise, or operational mismatch — not the technology itself.

**Mechanism.** The machine works; the institution does not. Across hundreds of post-mortems in the archive, the root-cause analysis lands on humans, not silicon.

**Filter spec.**
```
observation_type IN ('actual-outcome','risk-assessment','analytical-finding','expert-opinion','strategic-recommendation')
AND text_contains('governance','organizational','political','funding',
                  'culture','adoption failure','strategy','operational',
                  'litigation','liability')
```

**Population.** 67 rows; verified 3 / high 60 / medium 3 / low 1. Span: 1960s–2020s.

**Named exemplars.**
- `aberdeen-ra-soa-management-governance-20-ff6a2c` → OBS-008 — operational governance economic mechanism — high
- `computerworld-ilm-waiting-2004` → OBS-012 — offline tape litigation liability — high
- `dct-memoir-ramp-vs-dct-prescience-2026` → OBS-024 — common failure mode across refutations — high
- `hp-mercury-soa-2006-pdf-80785e` → OBS-010 — IT governance as SOA requirement — high
- `intel-consumer-lt-10-5-03-580af7` → OBS-018 — consumer LT research questions — high
- `the-business-value-in-it-outsourcing-7d5f23` → OBS-001 — IT outsourcing drivers ranked — high

**Proof studies.** [[aberdeen-ra-soa-management-governance-2007]], [[the-business-value-in-it-outsourcing]], [[computerworld-ilm-waiting-2004]]

---

### ARG-7 — The machine was never the hard part

**Claim.** Across every career chapter (PHI 1969, Prime 1979, Aberdeen 1997, Adoptex 2026), the binding constraint has been organizational physics — not the underlying technology.

**Mechanism.** Communication, incentives, decision-rights, culture — these are the actual variables. The machine is the dependent.

**Filter spec.**
```
observation_type IN ('expert-opinion','topic-insight','personal-recollection','framework-definition')
AND text_contains('organization','culture','institutional','beyond code',
                  'physics of organiz','workflow','people','politics')
```

**Population.** 37 rows; verified 1 / high 35 / low 1. Span: 1960s–2020s (peak 2020s n=18 — argument crystallizes in memoir).

**Named exemplars.**
- `informix-dsa-presentation-2-8d5fa3` → OBS-020 — irrelevant channel factors — high
- `volume-1-ch01-waiting-for-automation-1960-1969` → OBS-071 — system definition beyond code — high
- `volume-1-ch02-physics-of-the-machine-1969-1972` → OBS-061 — transition from physics of machine to physics of organization — high
- `volume-1-ch04-prime-computer-1979-1981` → OBS-016 — Prime argument against DEC VAX — high
- `volume-1-ch07-founding-aberdeen-1988-1997` → OBS-059 — arguments against VC: culture and control — high
- `volume-1-ch08-aberdeen-go-go-years-1998-2006` → OBS-070 — institutional professionalism vs early-stage culture — high

**Proof studies.** [[volume-1-ch01-waiting-for-automation-1960-1969]], [[volume-1-ch02-physics-of-the-machine-1969-1972]], [[volume-1-ch04-prime-computer-1979-1981]], [[volume-1-ch07-founding-aberdeen-1988-1997]]

---

### ARG-8 — Reliability is sold to buying committees, not engineers (derived)

**Claim.** Fault-tolerant and high-availability sales cycles are won at committee level. Engineering benchmarks influence shortlists, not selection.

**Mechanism.** Loss-event narratives (downtime cost, litigation exposure, regulatory consequence) dominate procurement conversations once CIO + CFO + auditor + ops are in the room. Engineering scoring is upstream of that conversation.

**Filter spec.**
```
observation_type IN ('market-data','expert-opinion','strategic-recommendation','actual-outcome')
AND (entity_name IN ('Stratus Computer','Tandem Computers','Marathon Technologies')
     OR text_contains('fault-tolerant','high availability','five 9s',
                      '99.999','uptime','committee','procurement','RFP'))
```

**Population.** 195 rows; verified 19 / high 156 / partial 1 / medium 17. Span: 1960s–2020s (peak 1990s n=102, 1980s n=41).

**Named exemplars.**
- `1991-encore-and-metadata-47f414` → OBS-028 — Tandem outcome — verified
- `1997-marathon's-endurance-4000` → OBS-008 — Wolfpack ship date — verified
- `stratus-computer-is-down-ad-reprints-c19-903ebf` → OBS-001 — Stratus XA400 list price — verified
- `stratus-corporate-overview-1982-11-a7e367` → OBS-001 — founding date and purpose — verified
- `stratus-foster-acm-speech-pr-1982-16a134` → OBS-001 — Foster ACM keynote thesis — verified
- `1990-bull-rdbms-1990-and-2024-metadata-fe61bf` → OBS-001 — Ingres vs Sybase user satisfaction — high

**Proof studies.** [[stratus-corporate-overview-1982-11]], [[stratus-foster-acm-speech-pr-1982]], [[1991-encore-and-metadata]], [[1997-marathon-endurance-4000]]

---

### ARG-9 — Categories must be created before they can be sold (derived)

**Claim.** The category language a vendor uses to sell is almost always invented first by an analyst. The category precedes the budget line.

**Mechanism.** Buying committees need a named bucket on the procurement form before money can flow. Analysts create the bucket. Across Kastner's career (CA Unicenter, Stratus FT, Encore, Marathon, DCT), the engagement pattern is the same: vendor pays for the category, analyst names it, the named category becomes the budget line.

**Filter spec.**
```
observation_type IN ('framework-definition','strategic-recommendation','market-data','topic-insight')
AND text_contains('category','positioning','market creation','first-mover',
                  'define the market','total available market','TAM',
                  'create the category')
```

**Population.** 103 rows; verified ~25 / high ~65. Span: 1980s–2000s (peak Aberdeen era).

**Named exemplars.** (drawn from cluster)
- Aberdeen Productization Program (2000) — MAS coverage list and budget-line creation
- DCT service-line founding documents (2002)
- CA Unicenter TNG framework positioning (1997)
- Stratus continuous-processing category (1980s)
- Encore parallel-processing category (1988)
- Marathon split-site continuous-processing (1997)

**Proof studies.** [[aberdeen-productization-pricing-and-survey-research-program-2000]], [[1997-ca-s-unicenter-tng-framework-pk-apr]], [[stratus-foster-acm-speech-pr-1982]], [[dct-launch-2002]]

---

### ARG-10 — Analyst credibility is earned with named winners, dates, and numbers (derived)

**Claim.** The rows that travel furthest cite a named entity, a specific year, and a number. Hedged or unspecified rows are not memorable and not citable.

**Mechanism.** Specificity is what makes a prediction falsifiable. Falsifiable predictions, once they survive, accumulate citation traffic and become the analyst's brand. This is why Kastner's methodology starts with "name the company, give the year, attach a number."

**Filter spec.**
```
observation_type IN ('market-data','viability-prediction','actual-outcome')
AND metric_value matches NAMED_ENTITY
AND year_observed IS NOT NULL
```

**Population.** 175 rows. Span: 1980s–2020s.

**Named exemplars.** Operationalized at full scale in [[kastner-top-100-economic-calls]] — that study identifies 100 specific calls that satisfy this filter and ranks them by citation lift. ARG-10 is therefore the **methodological precondition** for the top-100 list, not a separate empirical claim.

**Proof studies.** [[kastner-top-100-economic-calls]], [[kastner-prescience-methodology-demo]]

---

### ARG-11 — Free research is the marketing asset (derived)

**Claim.** Free research distributed in volume outperforms paid subscriptions as a sales-funnel asset. The product is the relationship; the research is the lure.

**Mechanism.** From the 1990s Aberdeen subscription pivot to the 2000s DCT free-research engine to current AI-era thought-leadership content, the funnel arithmetic favors give-it-away. Subscription revenue is small relative to the consulting / sponsored-research revenue the free distribution generates.

**Filter spec.**
```
observation_type IN ('strategic-recommendation','framework-definition','market-data')
AND text_contains('free research','marketing','sponsored research','asset',
                  'outbound','lead generation','distribution')
```

**Population.** 11 rows. Small because it appears as a recommendation pattern in a handful of high-leverage strategy documents rather than across many studies.

**Named exemplars.** Aberdeen Productization Program (2000); DCT free-research service-line launch (2002); aberdeen-outbound-marketing memos (2003-2005).

**Proof studies.** [[aberdeen-productization-pricing-and-survey-research-program-2000]], [[dct-launch-2002]], [[aberdeen-outbound-marketing-2003]]

---

### ARG-12 — Compute scarcity has inverted; judgment is now the scarce resource (derived)

**Claim.** From 1968 (compute scarce, judgment ubiquitous) to 2026 (frontier compute metered and commoditized, qualified judgment over messy enterprise data is the binding constraint), the scarce resource has fully inverted.

**Mechanism.** Frontier-model compute is now a metered commodity available on contract. The bottleneck has moved to whoever can interpret messy enterprise context, name the right questions, and ratify the model's outputs against business reality. AI-readiness work formalizes this inversion.

**Filter spec.**
```
observation_type IN ('expert-opinion','topic-insight','viability-prediction','analytical-finding')
AND text_contains('judgment','LLM','AI','generative','assistant','agent',
                  'reasoning','expertise','interpretation','synthesis')
```

**Population.** 35 rows; verified 1 / high 34. Span: 1960s–2020s (concentrated in 2020s).

**Named exemplars.** Memoir Chapter 10 and Epilogue articulations; Adoptex AI readiness framework documents; AI-exchange rows where Kastner queries a model and ratifies the output.

**Proof studies.** [[adoptex-ai-readiness-framework-2025]], [[volume-1-ch10-the-long-view-1966-2026]], [[volume-1-epilogue-argument-with-reality]]

---

## 4. How to use this framework

The framework is the navigation hub. There are four use modes:

| Mode | Steps |
|---|---|
| **Audit a claim** | Pick an ARG. Take its filter spec. Run it against `_master_observations.csv` in DuckDB. Compare your population count to the one published here. Inspect the disagreement. |
| **Find proof** | Pick an ARG. Read the named exemplars. Click through to the proof studies linked at the bottom of each section. |
| **Extend the framework** | Add a new ARG (ARG-13...). Define its claim, mechanism, filter spec. Run the filter. Publish the population and exemplars. The framework grows. |
| **Refute the framework** | Find a row that should be counter-evidence to an ARG and is not yet listed. Open a PR adding it to the counter-evidence list. The framework strengthens through honest counter-evidence, not its suppression. |

---

## 5. Replication

```bash
git clone https://github.com/shorttack/aberdeen-group-archive
cd aberdeen-group-archive
duckdb kastner.duckdb <<SQL
  CREATE TABLE obs AS SELECT * FROM '_master_observations.csv';
  -- Example: ARG-1 filter
  SELECT COUNT(*) FROM obs
  WHERE observation_type IN ('actual-outcome','viability-prediction')
    AND (metric_name ILIKE '%displace%' OR metric_name ILIKE '%market leadership%'
         OR metric_name ILIKE '%de facto%' OR metric_value ILIKE '%volume%');
SQL
```

The reference Python implementation lives at `build_argument_clusters.py` in the workspace root of the assembly run. All twelve filter specs match published populations within ±5% tolerance (slack accounts for bag-of-words ambiguity).

---

## 6. Live queries (Bases)

These Bases files re-execute the argument filters against the wiki's live data:

- `wiki/bases/arg-1-economic-winner.base` — _to be added_
- `wiki/bases/arg-7-the-machine-was-never-the-hard-part.base` — _to be added_
- `wiki/bases/arg-12-compute-judgment-inversion.base` — _to be added_

The base files are deferred to a follow-up commit so the framework page can land first.

---

## 7. Cross-references

- [[kastner-prescience-methodology-demo]] — first archive-as-protagonist study; establishes the replication convention
- [[kastner-top-100-economic-calls]] — operationalizes ARG-10 (named winners + dates + numbers) at scale
- [[volume-1-ch10-the-long-view-1966-2026]] — memoir source for ARG-1 through ARG-7 (Seven Patterns)
- [[volume-1-epilogue-argument-with-reality]] — memoir epilogue supports universal-pattern framing
- [[kastner-prescience-market-rollup]] — cross-archive market sizing for proof-study attribution weights
- [[aberdeen-productization-pricing-and-survey-research-program-2000]] — ARG-11 free-research-as-marketing primary source
- [[2026-kastner-ibm-longitudinal|IBM longitudinal]] — single-entity stress test for ARG-1, ARG-2, ARG-5
- [[2026-kastner-oracle-longitudinal|Oracle longitudinal]] — single-entity stress test for ARG-3, ARG-4, ARG-10
- [[2026-kastner-enterprise-ai-arc|Enterprise AI arc]] — cross-entity AI thread synthesis
- [[pass-a-v2-verification-pipeline|Pass A v2]] — structural verification supporting ARG-10 (named winners with verified outcomes)

---

## 8. Citation

Kastner, P. S. (2026). _Kastner's Core Arguments and Framework: A Wiki-Driven Synthesis from the Aberdeen-Group-Archive._ Aberdeen Group Archive, study `2026-kastner-core-arguments-framework-0b0c6b`. CC-BY-4.0. Companion wiki page: `kastner-core-arguments-framework`.

---

## 9. Limitations

1. **Argument count fixed at 12 may overfit.** Treat the framework as living; new ARGs can be added with their own filter and population claim.
2. **Filter spec uses bag-of-words text matching** — both over-includes and under-includes vs hand-curation. Exemplar lists are the anchored ground truth.
3. **Memoir-canonical vs derived split is judgment** — some derived ARGs (ARG-8, ARG-9) appear in Chapter 10 prose without being named as patterns. Treat the 7/5 split as expository, not definitive.
4. **Six refuted observations preserved as counter-evidence.** Aggregate framework holds; specific cases warrant inspection.
5. **Archive itself not yet peer-reviewed.** Each cited proof study has its own confidence rating; downstream consumers should propagate uncertainty.
