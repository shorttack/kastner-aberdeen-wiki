# Chat-Starter — Pre-Warmed Prompts

Each prompt is shown in three modes:
- **Natural language** — drop into an LLM
- **DuckDB SQL** — paste into `duckdb db/kastner.duckdb`
- **Dataview** — drop into an Obsidian note

## 1. What were Kastner's most prescient predictions?
- **NL**: "List the 15 studies rated prescience=high, chronologically, with their rationales."
- **SQL**: `SELECT date, title, prescience_rationale FROM studies_with_high_prescience;`
- **Dataview**:
```dataview
TABLE date, prescience_rationale FROM "studies" WHERE prescience = "high" SORT date ASC
```

## 2. Show me Kastner's writing about Stratus Computer
- **NL**: "Find all studies and observations referencing Stratus Computer."
- **SQL**: `SELECT s.* FROM studies s JOIN observations o USING (study_id) WHERE o.entity_id = 'stratus-computer';`
- **Dataview**:
```dataview
LIST FROM [[stratus-computer]]
```

## 3. Top 20 technologies by archive coverage
- **NL**: "Which technologies appear in the most studies?"
- **SQL**: `SELECT * FROM technologies_with_observation_count LIMIT 20;`
- **Dataview**:
```dataview
TABLE study_count, vendor FROM "technologies" WHERE tier = 1 SORT study_count DESC LIMIT 20
```

## 4. Volume 1 chapter map
- **NL**: "Summarize Volume 1 of the memoir in two sentences per chapter."
- **SQL**: `SELECT study_id, title, date FROM volume_1_chapters;`
- **Dataview**:
```dataview
TABLE date, obs_count FROM "volume-1" SORT file.name ASC
```

## 5. Press partnerships
- **NL**: "Where in the archive is Bill Bulkeley (WSJ) or Hiawatha Bray (Boston Globe) mentioned?"
- **SQL**: `SELECT * FROM observations WHERE LOWER(metric_value) LIKE '%bulkeley%' OR LOWER(metric_value) LIKE '%hiawatha%';`

## 6. 1990s open-source thesis
- **NL**: "Show me how Kastner's open-source thinking evolved 1995-2010."
- **SQL**: `SELECT s.date, s.title, o.metric_name, o.metric_value FROM studies s JOIN observations o USING (study_id) WHERE s.date BETWEEN '1995' AND '2010' AND LOWER(o.metric_value) LIKE '%open source%' ORDER BY s.date;`

## 7. Memoir cross-reference: Volume 1 ↔ breadth memoir
- **NL**: "Which entities appear in both Volume 1 Chapter 8 and the breadth memoir?"
- **SQL**: `SELECT DISTINCT a.entity_id FROM entities a JOIN entities b USING (entity_id) WHERE a.study_id = 'volume-1-ch08-aberdeen-go-go-years-1998-2006' AND b.study_id = 'kastner-technology-breadth-memoir-2026';`

## 8. Prescience-vs-importance scatter
- **SQL**:
```sql
SELECT importance, prescience, COUNT(*) FROM studies
GROUP BY importance, prescience ORDER BY 1,2;
```

## 9. The IE v. Andersen story
- **NL**: "Reconstruct the IE v. Andersen narrative from the archive."
- Open `[[ie-andersen-expert-report]]` and follow its links; or:
- **SQL**: `SELECT * FROM observations WHERE study_id LIKE '%ie-andersen%' ORDER BY year_observed;`

## 10. Career arc query
- **NL**: "What was Kastner doing in 1985 vs 1995 vs 2005?"
- **SQL**:
```sql
SELECT date, title, type FROM kastner_authored_studies
WHERE date LIKE '1985%' OR date LIKE '1995%' OR date LIKE '2005%'
ORDER BY date;
```

## 11. Decade overview
- **NL**: "What was the dominant technology focus of the 1990s in Kastner's archive?"
- See `[[decade-1990s]]`

## 12. Vendor leaderboard
- **SQL**: `SELECT * FROM top_vendors_by_mentions;`

## 13. Find the unverified predictions
- **SQL**: `SELECT * FROM observations WHERE observation_type = 'viability-prediction' AND confidence = '[DEFERRED]';`

## 14. Aberdeen co-founders
- **NL**: "Who co-founded Aberdeen Group with Kastner?"
- Open `[[volume-1-ch07-founding-aberdeen-1988-1997]]`

## 15. Semantic search starter
```bash
python scripts/semantic_search.py "What did Kastner predict about consumerization of IT?"
```

## 16. Methodologies inventory
- **SQL**: `SELECT methodology, COUNT(*) FROM studies GROUP BY methodology ORDER BY 2 DESC LIMIT 20;`

## 17. Find every TPC reference
- **SQL**: `SELECT * FROM observations WHERE LOWER(metric_value) LIKE '%tpc%';`

## 18. Studies that named ARM
- **SQL**: `SELECT s.title, s.date FROM studies s JOIN technologies t USING (study_id) WHERE LOWER(t.tech_name) LIKE '%arm%';`

## 19. Compare two entities
- **NL**: "Compare what the archive says about IBM and DEC in the 1980s."
- Open `[[ibm]]` and `[[dec]]` side by side; cross-reference Studies sections.

## 20. The big picture
- **NL**: "Read AGENTS.md, then summarize what this archive is for in one paragraph."
