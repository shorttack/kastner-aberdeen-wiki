# Chat starter — Kastner Aberdeen Wiki

20 pre-warmed prompts. Triple mode: natural-language + SQL + Dataview.

## 1. What were the 5 most prescient studies?

**SQL**
```sql
SELECT title, pub_year, prescience_max, prescience_mean
FROM v_top_prescient_studies
ORDER BY prescience_mean DESC LIMIT 5;
```

**Dataview**
~~~dataview
TABLE prescience_max, prescience_mean, pub_year
FROM "studies"
WHERE prescience_max >= 4
SORT prescience_mean DESC
LIMIT 5
~~~

## 2. Show prescient observations about Oracle

**SQL**
```sql
SELECT o.obs_id, o.prescience_score, o.metric_value, o.prescience_rationale
FROM v_observations o
WHERE o.entity_id = 'oracle' AND o.prescience_score >= 4
ORDER BY o.prescience_score DESC;
```

## 3. Which decade had the most prescient calls?

```sql
SELECT decade, high_prescience_studies
FROM v_prescience_by_decade
ORDER BY high_prescience_studies DESC;
```

## 4-20

(See `AGENTS.md` for query recipes; remaining prompts grow with usage.)
