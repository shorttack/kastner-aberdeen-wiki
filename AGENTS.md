# AGENTS.md — Kastner Aberdeen Wiki

You are an LLM (Ollama, Perplexity, Claude, or other) working inside this repo.
Read this file first every session.

## What this repo is
A read-optimized snapshot of Peter S. Kastner's 50-year technology analysis archive,
shipped as three interlocking layers:

1. **Wiki (`wiki/`)** — Obsidian Markdown vault. 933 study pages, 3299 entity pages, 4283 tech pages, plus overview pages.
2. **Data (`data/`)** — Parquet files. Same content as the wiki, queryable as columnar tables.
3. **DB (`db/kastner.duckdb`)** — Pre-built DuckDB with ~10 named views over the Parquet.

## How to navigate
- Every page is keyed by a slug. Entity slugs match `entity_id`, tech slugs match `tech_id`, study slugs match `study_id`.
- Obsidian wikilinks: `[[ibm]]`, `[[ibm-360-65]]`, `[[volume-1-ch07-founding-aberdeen-1988-1997]]`.
- YAML frontmatter on every page exposes structured fields (tier, study_count, obs_count, tags, etc.).
- Tier-1 pages have rich summaries + observations. Tier-2 pages are stubs pointing at DuckDB.

## How to query DuckDB
```python
import duckdb
con = duckdb.connect("db/kastner.duckdb")
con.execute("SELECT * FROM studies_with_high_prescience LIMIT 10").fetchall()
```

Named views available: `studies_with_high_prescience`, `studies_by_decade`,
`entities_with_observation_count`, `technologies_with_observation_count`,
`prescience_summary`, `importance_summary`, `top_vendors_by_mentions`,
`volume_1_chapters`, `kastner_authored_studies`, `observations_by_year`.

## When to use Perplexity vs local
- **Local (Ollama, qwen3:32b or 30b-a3b)**: routine lookups, navigation, summarizing 1-3 pages.
- **Perplexity**: cross-archive synthesis, fact-checking against external sources, writing.

## Naming conventions
- Slugs: lowercase, hyphenated, ASCII only.
- Study slugs often end in a 6-char hash (legacy).
- Volume 1 chapters: `volume-1-chNN-{description}-{date-range}`.

## Common retrieval recipes
1. **"Find all studies citing entity X"**:
   `SELECT DISTINCT study_id FROM observations WHERE entity_id = 'X';`
2. **"All high-prescience studies in the 1990s"**:
   `SELECT * FROM studies_with_high_prescience WHERE date LIKE '199%';`
3. **"Entities co-appearing with X in >= 3 studies"**: query the `entity_cooccurrence` derivable from observations.

## Embeddings
`data/embeddings.parquet` has one 384-dim vector per wiki page, computed at build time with
`sentence-transformers/all-MiniLM-L6-v2` (chosen for fast, low-memory builds in any sandbox).
8549 rows, ~19 MB.

**To switch to nomic-embed-text-v2-moe (your preferred model) locally:**
```bash
ollama pull nomic-embed-text-v2-moe
python scripts/reembed.py --model nomic-ai/nomic-embed-text-v1.5
# or just call Ollama directly for 768-dim vectors
```

Use `scripts/semantic_search.py` for cosine-similarity retrieval against whatever model
`data/embeddings.parquet` currently holds.

## Build provenance
See `build_manifest.json` for exact build timestamp and source archive commit.
