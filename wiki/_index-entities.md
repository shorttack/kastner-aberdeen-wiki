---
title: All Entities
slug: _index-entities
page_type: index
tags: [type/index]
---
# All Entities (tier 1)

```dataview
TABLE sector, study_count, obs_count
FROM "entities"
WHERE tier = 1
SORT study_count DESC
```
