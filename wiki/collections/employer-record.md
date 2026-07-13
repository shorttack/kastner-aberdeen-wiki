---
title: "employer-record"
slug: "collection-employer-record"
page_type: collection
tier: 1
study_count: 1
---


# employer-record


**1** studies, ~9 entity refs, ~9 tech refs, ~12 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/employer-record")

SORT prescience_max DESC, pub_year DESC

```
