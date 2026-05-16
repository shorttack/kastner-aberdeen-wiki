# Mac Mini Setup — Kastner Aberdeen Wiki

End-to-end setup for the **48GB Mac Mini M4** to query the wiki locally with
Obsidian + DuckDB + Ollama + Perplexity hybrid. ~30 minutes the first time.

---

## TL;DR (one command)

```bash
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git
cd kastner-aberdeen-wiki
./setup.sh        # installs everything except Obsidian
```

Then open Obsidian → "Open folder as vault" → pick the `wiki/` subfolder.

---

## What gets installed

| Layer | Tool | Why |
|---|---|---|
| Package manager | Homebrew | Installs everything else |
| Editor / vault | Obsidian (manual download) | Browse the Markdown wiki with [[wikilinks]], graph view, Bases |
| Query engine | DuckDB (CLI + Python) | SQL over Parquet + the pre-built `kastner.duckdb` |
| Local LLM | Ollama + `qwen3:32b`, `qwen3:30b-a3b`, `nomic-embed-text-v2-moe` | Offline chat, embeddings, RAG |
| Python runtime | Python 3.11 + venv | `scripts/semantic_search.py`, `scripts/reembed.py`, `scripts/verify.py` |
| Glue | `kw` CLI (this repo) | One-line shortcuts for common workflows |
| Cloud LLM | Perplexity Desktop (manual) | Cross-archive synthesis + external fact-checking |

Disk footprint: ~50 GB (Ollama models are the bulk — `qwen3:32b` alone is ~20 GB).

---

## Step 1 — Prerequisites

You need:

1. **macOS 14+** on the Mac Mini M4 (Apple Silicon).
2. **Xcode Command Line Tools** — `xcode-select --install` if not already present.
3. **Git** — bundled with the command line tools above.
4. **GitHub access** to the private repo `shorttack/kastner-aberdeen-wiki`.
   - Easiest: `gh auth login` after installing the GitHub CLI.

---

## Step 2 — Clone the repo

```bash
mkdir -p ~/kastner && cd ~/kastner
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git
cd kastner-aberdeen-wiki
```

You should now have:

```
wiki/        # 8,549 Markdown pages — open this in Obsidian
data/        # Parquet exports
db/          # kastner.duckdb (pre-built, 10 named views)
scripts/     # semantic_search.py, reembed.py, verify.py, rebuild.py
AGENTS.md    # Read first if you point an LLM at this repo
chat-starter.md  # Pre-warmed prompts (NL + SQL + Dataview)
```

---

## Step 3 — Run the bootstrap script

```bash
./setup.sh
```

What it does, step by step (idempotent — safe to re-run):

1. **Homebrew** — installs if missing.
2. **DuckDB CLI** — `brew install duckdb` (only the binary; the file is already in `db/`).
3. **Python 3.11** — `brew install python@3.11`.
4. **Virtualenv** — creates `.venv/` and installs `requirements.txt`.
5. **Ollama** — `brew install ollama`, starts the service, then pulls:
   - `qwen3:32b` (~20 GB, primary chat model)
   - `qwen3:30b-a3b` (~18 GB, faster MoE alternative)
   - `nomic-embed-text-v2-moe` (~500 MB, 768-dim embeddings)
6. **Self-check** — `python scripts/verify.py` confirms every file is intact.
7. **(Optional) Re-embed** — prompts you whether to rebuild `data/embeddings.parquet`
   with the higher-quality 768-dim nomic vectors (~10 min on M4).

After this, `make verify` should pass all 13 checks.

---

## Step 4 — Install Obsidian (manual, one-time)

1. Download from [obsidian.md](https://obsidian.md/download) (free for personal use).
2. Open Obsidian → "Open folder as vault" → choose `~/kastner/kastner-aberdeen-wiki/wiki`.
3. Enable the core **Dataview** plugin and the new **Bases** core plugin:
   - Settings → Core plugins → toggle on **Bases**.
   - Settings → Community plugins → Browse → install **Dataview**.
4. The repo ships 5 pre-built Bases in `wiki/bases/` — they will appear in the file
   tree and render as filtered/sortable tables.

> **Novice tip:** Cmd-O opens the quick switcher. Cmd-G opens the graph. Click any
> `[[wikilink]]` to navigate. Cmd-click opens in a split pane.

---

## Step 5 — Install Perplexity Desktop (manual, one-time)

1. Download Perplexity Desktop for Mac from
   [perplexity.ai/desktop](https://www.perplexity.ai/desktop).
2. Sign in.
3. Workflow tip: use Perplexity for **cross-archive synthesis** and **external
   fact-checking** (anything that needs the live web). Use local Ollama for
   navigation, lookups, and summarizing 1–3 pages.

---

## Step 6 — Smoke test

After `setup.sh` finishes:

```bash
# DuckDB
make duckdb
# > .tables
# > SELECT * FROM studies_with_high_prescience LIMIT 5;
# > .quit

# Semantic search
source .venv/bin/activate
python scripts/semantic_search.py "category creation playbook"

# Ollama chat (one-shot)
ollama run qwen3:30b-a3b "Summarize this in 2 sentences." < AGENTS.md

# Full verification
make verify
```

If all four succeed, you're ready to work.

---

## Day-to-day commands

The `kw` helper (installed into `.venv/bin`) wraps the common workflows:

```bash
kw query "did Kastner predict the SaaS shift before 2005?"   # semantic + Ollama RAG
kw sql                                                       # opens DuckDB shell
kw page IBM                                                  # opens IBM entity page in Obsidian
kw verify                                                    # re-runs verify.py
kw reembed nomic                                             # rebuild embeddings to 768-dim
kw reembed minilm                                            # rebuild embeddings to 384-dim
```

Plain `make` targets also still work: `make duckdb`, `make verify`, `make semantic-search Q="..."`.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `setup.sh` fails on Homebrew | Run `brew doctor`, then re-run `setup.sh`. |
| `ollama pull` hangs | `ollama serve` in another terminal, then retry. |
| `scripts/semantic_search.py` says "Missing dependency" | `source .venv/bin/activate` first. |
| Embeddings dim mismatch warning | Run `kw reembed nomic` (or `minilm`) to align the vectors with the encoder you want. |
| Obsidian shows raw `[[wikilink]]` text | Switch the pane to Reading view (Cmd-E toggles). |
| Bases don't render | Settings → Core plugins → enable **Bases** (requires Obsidian ≥ 1.9). |
| `qwen3:32b` is too slow for chat | Use `qwen3:30b-a3b` instead — it's MoE and noticeably faster on M4. |

---

## Updating the wiki

When the source archive grows and you want to rebuild:

```bash
# In a clean working dir (NOT this repo)
git clone https://github.com/shorttack/aberdeen-group-archive.git
git clone https://github.com/shorttack/kastner-aberdeen-wiki.git wiki-rebuild
cd wiki-rebuild

# Re-run the build skill from Perplexity Computer, or directly:
python <path-to-kastner-wiki-builder-skill>/scripts/build.py \
  --archive ../aberdeen-group-archive \
  --output . \
  --skip-llm

# Re-embed locally with the better model
source .venv/bin/activate
python scripts/reembed.py --ollama nomic-embed-text-v2-moe

# Commit + push
git add . && git commit -m "Rebuild from archive snapshot $(date +%F)" && git push
```

---

## Storage and memory budget (48 GB M4)

| Resident process | RAM |
|---|---|
| Obsidian (vault loaded) | ~1.5 GB |
| DuckDB (idle) | ~50 MB |
| Ollama with `qwen3:30b-a3b` loaded | ~22 GB |
| Ollama with `qwen3:32b` loaded | ~24 GB |
| Python venv + semantic_search | ~1 GB |
| **Safe simultaneous load** | Obsidian + DuckDB + one Ollama model + Perplexity Desktop fits comfortably under 30 GB. |

Avoid running `qwen3:32b` and `qwen3:30b-a3b` simultaneously — Ollama will swap.

---

## What `setup.sh` does NOT do

- It does not install Obsidian (Mac App Store / drag-and-drop GUI app).
- It does not install Perplexity Desktop.
- It does not auth you to GitHub — do `gh auth login` once beforehand if you
  want to push wiki edits back.
- It does not modify `~/.zshrc` — the `kw` helper lives in the repo's venv,
  not on your global `$PATH`. Add `alias kw='~/kastner/kastner-aberdeen-wiki/.venv/bin/kw'`
  if you want it globally available.
