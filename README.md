# Kastner Aberdeen Wiki

A local-first research environment derived from the Kastner Aberdeen Archive:
- **933 unique studies** spanning 1979 – 2026
- **3299 entities** (48 tier-1 / 3251 stub)
- **4283 technologies** (33 tier-1 / 4250 stub)
- **19175 observations** indexed and queryable

## Quick start (Mac, Obsidian + DuckDB + Ollama)

```bash
# 1. Clone
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git
cd kastner-aberdeen-wiki

# 2. Open the vault in Obsidian: File → Open Folder → ./wiki

# 3. Query DuckDB (CLI)
brew install duckdb
duckdb db/kastner.duckdb
# > .tables
# > SELECT * FROM studies_with_high_prescience LIMIT 10;

# 4. Local LLM via Ollama (recommended models)
ollama pull qwen3:32b
ollama pull qwen3:30b-a3b
ollama pull nomic-embed-text-v2-moe   # then run scripts/reembed.py to get 768-dim vectors

# 5. Semantic search over the wiki
python scripts/semantic_search.py "What did Kastner predict about open source?"
```

## Repository layout

- `wiki/` — Obsidian vault (Markdown with `[[wikilinks]]`)
- `data/` — Parquet exports (DuckDB-native columnar)
- `db/kastner.duckdb` — pre-built DuckDB file with named views
- `db/queries/*.sql` — sample queries
- `scripts/` — utility scripts (semantic search, verification, rebuild)
- `AGENTS.md` — primer for any LLM working with this repo
- `chat-starter.md` — pre-warmed prompts (NL + SQL + Dataview)

## License
Content: CC-BY-4.0. Same as the source archive.

## Reproducibility
Built once from a snapshot of `shorttack/aberdeen-group-archive`. See
`build_manifest.json` for exact counts and timestamps.
