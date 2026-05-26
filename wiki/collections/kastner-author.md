---
title: "kastner-author"
slug: "collection-kastner-author"
page_type: collection
tier: 1
study_count: 369
---


# kastner-author


**369** studies, ~3926 entity refs, ~3453 tech refs, ~8356 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/kastner-author")

SORT prescience_max DESC, pub_year DESC

```
