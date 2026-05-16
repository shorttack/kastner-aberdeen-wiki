---
title: "Top 100 Kastner Economic Calls (Ranked by Per-Study Share-of-Prescience Net Attributed Value)"
slug: kastner-top-100-economic-calls
page_type: theme
tier: 1
study_type: ranked-allocation-demonstration
audience: industry-analyst-peers
tags: [type/theme, type/methodology, theme/prescience-attribution, theme/ranked-list]
date_built: 2026-05-16
parent_study: kastner-prescience-market-rollup
allocation_method: equal-within-theme
universe_size: 360
ranked_count: 100
---

# Top 100 Kastner Economic Calls (Ranked by Per-Study Share-of-Prescience Net Attributed Value)

> **Framing note.** This is a companion ranking exercise to the [[kastner-prescience-market-rollup|prescience methodology demo]]. It applies the Phase 4 share-of-prescience attribution at study level rather than theme level, producing a defensible ranked list as an example of what archive users can do once the headline methodology is established. The list is **not** a final scoreboard — within-theme ties are by design under equal allocation, and the bottom of the §6 documents the refinement path that would break them.

---

## 1. What this ranking is and is not

**Is**: A defensible study-level allocation of Phase 4 net attributed value across the 360 high-prescience technology-tagged studies in the 15 headline themes. The top 100 (top 27.8%) is presented as a ranked table.

**Is not**: A claim that each study in a tie cluster is *equally* prescient. Equal-within-theme allocation is the floor — the minimum we can claim without doing a per-study scoring pass. The honest reading is "any of these N studies could occupy this rank slot."

**Why publish it anyway**: Because the floor is itself informative. The fact that *every* Mobile/Smartphone study in the archive carries at least $237.7B of allocated value tells you something real — that theme is so dominant in cumulative net-attributed value that even its smallest contributor punches above $200B. The ranking exists to make that visible at study granularity.

## 2. Method

```
per_study_value = theme_net_attributed_value / count(studies_in_theme)
```

Theme net values come from [Phase 4 attribution](kastner-prescience-market-rollup.md#34-share-of-prescience-attribution-phase-4). Study counts come from [Phase 1 classification](kastner-prescience-market-rollup.md#31-theme-classification-phase-1).

Per-theme allocations:

| Theme | Net $B | Studies | Per-study $B |
|---|---:|---:|---:|
| Mobile / Smartphone Computing | 2,852.5 | 12 | 237.7 |
| Digital Consumer Technology | 1,520.2 | 14 | 108.6 |
| OLTP / TPC | 924.6 | 16 | 57.8 |
| Cloud Computing & SaaS | 3,078.5 | 65 | 47.4 |
| Desktop PC / Windows Client | 617.6 | 19 | 32.5 |
| Enterprise Networking (IP/VoIP) | 606.2 | 22 | 27.6 |
| Enterprise Storage / ILM | 221.0 | 11 | 20.1 |
| Windows NT / Server OS | 198.2 | 11 | 18.0 |
| ERP | 194.6 | 19 | 10.2 |
| Fault-Tolerant Servers | 138.7 | 16 | 8.7 |
| Linux | 122.8 | 18 | 6.8 |
| RDBMS | 271.8 | 60 | 4.5 |
| Java / Web App Platforms | 74.2 | 18 | 4.1 |
| SOA / Web Services / API Mgmt | 59.9 | 16 | 3.7 |
| E-Commerce Platform Software | 38.1 | 23 | 1.7 |

(Note: study counts per theme reflect Phase 1 final classification incl. studies that exist in the archive but were not all loaded into the top-100 cut.)

## 3. Top 100 ranked table

The full ranked list lives in the companion archive study as `source/top100_full_ranking.csv` and `source/top100_full_ranking.md`. Sample of the top 20 below; the full ranking is reproduced in §5.

### 3.1 Top 10 by per-study allocated value

| # | $B Net | Date | Theme | Title |
|---|---:|---|---|---|
| 1 | $237.7 | 2002-03-25 | Mobile | Second-Generation PDAs: It's High Time for Wireless |
| 2 | $237.7 | 2002-04-01 | Mobile | WebEx: Taking Conferencing to the Business Communications Summit |
| 3 | $237.7 | 2006-10-27 | Mobile | The Outlook on AMD's Fusion Plans |
| 4 | $237.7 | 1998-05-01 | Mobile | Data Management: 1998 Practice Summary |
| 5 | $237.7 | 2001-09-17 | Mobile | Integrating HP and Compaq |
| 6 | $237.7 | 2002-11-01 | Mobile | DCT Segment Priorities Matrix (Home / Work / Mobile) |
| 7 | $237.7 | 2002-04-01 | Mobile | Personal Electronic Technology Vision — Sony Client |
| 8 | $237.7 | 2002-11-01 | Mobile | Digital Consumer Technology: The Revolution Has Started |
| 9 | $237.7 | 2002-06-25 | Mobile | Whatever Happened to Interactive TV? |
| 10 | $237.7 | 2004-05-24 | Mobile | Apple's Enterprise IT Battle Plan, Part Two |

### 3.2 Theme distribution in top 100

| Theme | Top-100 entries |
|---|---:|
| Mobile / Smartphone | 12 (ranks 1–12) |
| Digital Consumer Tech | 14 (ranks 13–26) |
| OLTP / TPC | 16 (ranks 27–42) |
| Cloud Computing & SaaS | 58 (ranks 43–100) |

The Cloud Computing tail is large because that theme has 65 studies and $47.4B is still above all other themes' per-study values — so it floods the long tail of the top 100.

## 4. What this surfaces for the archive

Five candidate "deep-dive" studies that the ranking surfaces as worth individual case-study treatment in future archive work:

1. **2002-03-25 "Second-Generation PDAs: It's High Time for Wireless"** — Mobile theme rank #1, predates iPhone by 5 years and named the PDA→smartphone convergence.
2. **2002-04-01 "WebEx: Taking Conferencing to the Business Communications Summit"** — flagged a $3.2B 2007 Cisco acquisition target 5 years early.
3. **2001-09-17 "Integrating HP and Compaq"** — written before the merger closed (May 2002); rare contemporary IT-channel prescience.
4. **2002-11-01 DCT keynote series** — appears multiple times in top 20 across Mobile and DCT themes; identifies the central thesis of the 2002 Kastner output.
5. **1988-01-01 "A Primer on Comparing Debit-Credit Tests"** (Kastner, DEC CSG) — origin document of the TPC-C benchmark prescience that anchors the OLTP theme's 50% attribution score.

## 5. Full ranked list (top 100)

See companion archive study `2026-kastner-top-100-economic-calls-2a98a7` for the full 100-row CSV with per-study prescience rationales. Open it via:

```sql
-- DuckDB query against the archive
SELECT * FROM read_csv_auto(
    '/home/user/workspace/aberdeen-group-archive/kastner-author/2026-kastner-top-100-economic-calls-2a98a7/source/top100_full_ranking.csv'
) ORDER BY rank;
```

Or fetch raw from GitHub: [`source/top100_full_ranking.csv`](https://github.com/shorttack/aberdeen-group-archive/blob/main/kastner-author/2026-kastner-top-100-economic-calls-2a98a7/source/top100_full_ranking.csv).

## 6. Limitations & refinement path

### 6.1 Within-theme ties are by design

Equal allocation cannot distinguish prescience between two studies that both fall under the same theme. A 1987 Computerworld fault-tolerant prediction and a 2003 SARS-supply-chain memo would both end up at the same per-study value if they shared a theme.

### 6.2 Theme-assignment artifacts

The Phase 1 priority-ordered classifier resolves overlap deterministically but not always optimally. Examples in the current top-100:

- **"Whatever Happened to Interactive TV?" (2002-06-25)** — currently in Mobile theme; arguably should be DCT or its own theme.
- **"WebEx: Taking Conferencing to the Business Communications Summit" (2002-04-01)** — currently in Mobile; the Mobile-wireless prediction was secondary to the WebEx-acquisition prediction.

A future re-tagging pass would correct these.

### 6.3 Refinement paths

| Path | Effort | Output |
|---|---|---|
| **A. Specificity heuristics** | ~20 min | Parse each `prescience_rationale` for named winners + dates + quantified numbers; re-score specificity 1–5 per study; break ties within themes |
| **B. Full per-study attribution** | ~2 hours | Hand-score lead × contrarian × specificity for each of the 360 studies; produce a no-ties top-100 list |
| **C. Cross-theme rebalancing** | ~4 hours | Re-tag the 360 studies allowing multi-theme membership with weights; re-allocate accordingly |

Path A is the recommended next step.

## 7. Replication

```python
import duckdb, json
con = duckdb.connect("db/kastner.duckdb", read_only=True)

# Get all high-prescience studies in headline themes
df = con.execute("""
  SELECT study_id, title, date FROM studies_with_high_prescience
""").df()

# Load Phase 1 + 4 outputs
with open("phase1_final.json") as f: p1 = json.load(f)
with open("phase4_attributed.json") as f: p4 = json.load(f)

# Equal allocation
ALIAS = {  # Phase 1 name → Phase 4 name
    "Windows NT / Server OS": "Windows NT / Server OS family",
    # ...etc (see top100_studies.py for full alias map)
}
net = {r["theme"]: r["net_attributed_b"] for r in p4["rows"]}
rows = []
for theme in p1["headline_themes"]:
    tname = ALIAS.get(theme["name"], theme["name"])
    per_study = net[tname] / len(theme["study_ids"])
    for sid in theme["study_ids"]:
        rows.append({"study_id": sid, "theme": tname, "value_b": per_study})

# Sort and take top 100
rows.sort(key=lambda r: r["value_b"], reverse=True)
top100 = rows[:100]
```

## 8. Provenance

| Field | Value |
|---|---|
| Build date | 2026-05-16 |
| Parent study | [[kastner-prescience-market-rollup]] |
| Companion archive study | `2026-kastner-top-100-economic-calls-2a98a7` |
| Allocation method | equal-within-theme |
| Total universe | 360 high-prescience tech-tagged studies |
| Top-100 cut | 27.8% of universe |
| Total allocated value (top 100) | sum across ranks 1-100 |
| Reviewer | Peter S. Kastner |
| Methodology version | v1.0 (equal-allocation baseline) |

---

## See also

- [[kastner-prescience-market-rollup]] — parent methodology study (Phase 4 attribution)
- [[kastner-technology-breadth-memoir-2026]] — narrative companion
- [[_index|Wiki index]] · [[_index-themes|All themes]]
