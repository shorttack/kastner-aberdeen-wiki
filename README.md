# Kastner Aberdeen Wiki

A local-first research environment derived from the Kastner Aberdeen Archive:
- **933 unique studies** spanning 1979 – 2026
- **3299 entities** (48 tier-1 / 3251 stub)
- **4283 technologies** (33 tier-1 / 4250 stub)
- **19175 observations** indexed and queryable

## Quick start (Mac Mini M4)

```bash
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git
cd kastner-aberdeen-wiki
./setup.sh        # installs Homebrew, DuckDB, Python venv, Ollama, models
```

Then install [Obsidian](https://obsidian.md/download) and open `wiki/` as a vault.

Full walkthrough, troubleshooting, and the `kw` helper CLI reference: **[SETUP.md](SETUP.md)**.

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
