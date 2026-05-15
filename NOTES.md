# Build Notes

## Embedding model
Built with `sentence-transformers/all-MiniLM-L6-v2` (384-dim) for fast,
low-memory sandbox builds. Run `scripts/reembed.py --model nomic-ai/nomic-embed-text-v1.5`
locally to upgrade to 768-dim vectors with your preferred encoder.

## LLM enrichment (deferred)
Tier-1 pages were generated with templated rich content (top observations + structured sections),
not true LLM summarization. To upgrade specific pages, use a local Ollama model:

```bash
ollama run qwen3:32b < some-tier-1-page.md
```

Or batch-enrich tier-1 study pages via Perplexity from the desktop.

## Date anomalies
5 study `date` fields are in non-ISO form (e.g. "April 13, 2004", "~2023-2026") and bucket
into pseudo-decades in the `studies_by_decade` view. These are accurate to the source archive.
Fix upstream in `aberdeen-group-archive/_master_studies.csv` if desired.

## Volume 1 chapters
The 14 Volume 1 memoir chapters live in `wiki/volume-1/` (not `wiki/studies/`) and are
also listed in DuckDB view `volume_1_chapters`. They are tier-1 with rich content.

## Re-running the build
This wiki was built from a fixed snapshot. To rebuild against a newer snapshot of the archive:

```bash
python <path-to-kastner-wiki-builder>/scripts/build.py \
  --archive <path-to-aberdeen-group-archive> \
  --output . --skip-llm
python scripts/reembed.py --model nomic-ai/nomic-embed-text-v1.5
```
