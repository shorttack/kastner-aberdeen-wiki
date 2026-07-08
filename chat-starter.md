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

## 4. Which studies were prescient at 3 years? (v1.6)

**SQL**
```sql
SELECT study_id, title, prescience_3y_enum
FROM v_studies_with_sh_verdicts
WHERE prescience_3y_enum = 'high'
ORDER BY title;
```

## 5. Which studies were prescient at 5 years? (v1.6)

```sql
SELECT study_id, title, prescience_5y_enum
FROM v_studies_with_sh_verdicts
WHERE prescience_5y_enum = 'high'
ORDER BY title;
```

## 6. Show the 3-year vs 5-year score distribution (v1.6)

```sql
SELECT '3y' AS horizon, prescience_3y AS score, n FROM v_sh_3y_distribution
UNION ALL
SELECT '5y', prescience_5y, n FROM v_sh_5y_distribution
ORDER BY horizon, score;
```

## 7-20

(See `AGENTS.md` for query recipes; remaining prompts grow with usage.)
