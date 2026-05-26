---
title: "other-authors"
slug: "collection-other-authors"
page_type: collection
tier: 1
study_count: 487
---


# other-authors


**487** studies, ~4205 entity refs, ~3212 tech refs, ~8114 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/other-authors")

SORT prescience_max DESC, pub_year DESC

```
