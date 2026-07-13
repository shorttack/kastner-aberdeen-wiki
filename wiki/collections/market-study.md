---
title: "market-study"
slug: "collection-market-study"
page_type: collection
tier: 1
study_count: 4
---


# market-study


**4** studies, ~86 entity refs, ~65 tech refs, ~172 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/market-study")

SORT prescience_max DESC, pub_year DESC

```
