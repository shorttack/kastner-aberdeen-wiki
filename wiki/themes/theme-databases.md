---
title: "Theme: Databases"
slug: theme-databases
page_type: theme
tier: 1
tags: [type/theme, theme/databases]
---
# Databases

One of fourteen thematic rollups from the [[kastner-technology-breadth-memoir-2026|breadth memoir]].

```dataview
TABLE study_count, obs_count
FROM "entities" OR "technologies"
WHERE contains(tags, "theme/databases")
SORT study_count DESC
LIMIT 30
```
