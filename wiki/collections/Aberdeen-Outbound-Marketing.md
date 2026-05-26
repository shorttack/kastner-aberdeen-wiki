---
title: "Aberdeen Outbound Marketing"
slug: "collection-Aberdeen-Outbound-Marketing"
page_type: collection
tier: 1
study_count: 3
---


# Aberdeen Outbound Marketing


**3** studies, ~16 entity refs, ~12 tech refs, ~40 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/Aberdeen Outbound Marketing")

SORT prescience_max DESC, pub_year DESC

```
