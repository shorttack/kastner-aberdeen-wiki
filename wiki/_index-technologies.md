---
title: All Technologies
slug: _index-technologies
page_type: index
tags: [type/index]
---
# All Technologies (tier 1)

```dataview
TABLE vendor, category, study_count, obs_count
FROM "technologies"
WHERE tier = 1
SORT study_count DESC
```
