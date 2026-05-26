---
title: "Kastner Memoir"
slug: "collection-Kastner-Memoir"
page_type: collection
tier: 1
study_count: 14
---


# Kastner Memoir


**14** studies, ~257 entity refs, ~237 tech refs, ~1242 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/Kastner Memoir")

SORT prescience_max DESC, pub_year DESC

```
