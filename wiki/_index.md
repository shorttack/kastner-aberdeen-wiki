---
title: Kastner Aberdeen Archive — Wiki Home
slug: _index
page_type: index
tags: [type/index]
---

# Kastner Aberdeen Archive — Wiki

A local-first Obsidian + DuckDB research environment derived from
[shorttack/aberdeen-group-archive](https://github.com/shorttack/aberdeen-group-archive).

## Start here
- [[volume-1-introduction-physics-of-the-machine|Volume 1 — Introduction]]
- [[kastner-technology-breadth-memoir-2026|Breadth memoir (2026)]]
- See `AGENTS.md` for the LLM primer
- See `chat-starter.md` for pre-warmed prompts

## Navigation
- [[_index-studies|All studies]]
- [[_index-entities|All entities]]
- [[_index-technologies|All technologies]]
- [[_index-volume-1|Volume 1 chapters]]
- [[_index-themes|Themes]]
- [[_index-decades|Decades]]

## High-prescience studies (Dataview)

```dataview
TABLE date, author, prescience_rationale
FROM "studies"
WHERE prescience = "high"
SORT date ASC
```
