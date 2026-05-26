---
title: "Project Examples"
slug: "collection-Project-Examples"
page_type: collection
tier: 1
study_count: 45
---


# Project Examples


**45** studies, ~428 entity refs, ~399 tech refs, ~1282 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/Project Examples")

SORT prescience_max DESC, pub_year DESC

```
