---
title: "topic-analysis"
slug: "collection-topic-analysis"
page_type: collection
tier: 1
study_count: 1
---


# topic-analysis


**1** studies, ~11 entity refs, ~19 tech refs, ~22 observations.


```dataview

TABLE prescience_max, prescience_mean, pub_year, author

FROM "studies"

WHERE contains(string(file.frontmatter.tags), "collection/topic-analysis")

SORT prescience_max DESC, pub_year DESC

```
