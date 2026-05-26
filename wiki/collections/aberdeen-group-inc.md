---
title: "aberdeen-group-inc"
slug: "collection-aberdeen-group-inc"
page_type: collection
tier: 1
study_count: 29
---


# aberdeen-group-inc


**29** studies, ~626 entity refs, ~416 tech refs, ~673 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/aberdeen-group-inc")

SORT prescience_max DESC, pub_year DESC

```
