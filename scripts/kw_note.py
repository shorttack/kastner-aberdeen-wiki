#!/usr/bin/env python3
"""kw note — turn kw_ask answers (or anything) into permanent wiki notes.

This is how the corpus grows with Pete's interpretations. Notes live in
wiki/notes/ and carry page_type: note so kw_ask can include or exclude
them at query time via --no-notes / --only-notes.

Default mode is DRY-RUN: kw note prints the file it would write to stdout
and exits 0. Pass --commit to actually write the file. This matches the
forever-archive verify-then-write rule.

v3 changes (2026-05-28, post-matched-0-bug):
  * Slug index now reads from data/pages_manifest.parquet — the actual
    wiki page slugs (e.g. 'study-volume-1-ch06-dec-mainframes-last-...',
    'digital-equipment-corp'). v2 read from studies.parquet.study_id,
    entities.parquet.entity_id, technologies.parquet.tech_id, which are
    INTERNAL master IDs (e.g. 'STU-001234') that look nothing like wiki
    slugs. Net effect on v2: 'matched: 0' even when cited slugs were real
    wiki pages. v3 reads pages_manifest where slug IS the wiki filename
    stem and type ∈ {study, entity, technology, code}.
  * Falls back to data/{studies,entities,technologies,codes}.parquet
    only as a hard fallback if pages_manifest is missing. This shouldn't
    happen in practice — refresh_data_layer.py always writes it — but
    keeps the script robust.
  * Adds 'code' as a fourth match bucket (related_codes) since
    pages_manifest knows about 1293 methodology code pages.
  * CSV fallback removed: the master CSVs don't store the wiki slugs,
    only the internal IDs. There's no point in falling back to them.

v2 changes carried forward:
  * Parquet-first slug index — wiki repo is self-contained.

v1 changes carried forward:
  * --no-notes / --only-notes filter awareness via page_type: note.

Common usage:

  # Pipe an answer straight from kw ask
  kw ask "Why did DEC miss the PC transition?" \\
      --no-notes 2>/tmp/sources.txt \\
    | kw note --title "Why DEC missed the PC transition" \\
              --question "Why did DEC miss the PC transition?" \\
              --sources-from /tmp/sources.txt \\
              --commit

  # File a hand-written permanent note
  kw note --title "ATM vs Ethernet, retrospective" \\
          --body "ATM lost because…" --commit

  # Append to an existing note
  kw note --update note-atm-vs-ethernet-retrospective-2026-05-28 \\
          --append --body "Update 2026-06: new data from…" --commit

Frontmatter (page_type: note):
  title, slug, page_type=note, author, author_id, created, updated,
  question (optional), source_method, model, retrieval_k, tier=2,
  tags, related_studies, related_entities, related_technologies,
  related_codes
"""
from __future__ import annotations
import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "wiki"
NOTES_DIR = WIKI_ROOT / "notes"
DATA_DIR = ROOT / "data"

# Authors known to the corpus. Extend by passing --author <freeform string>.
AUTHORS = {
    "pete": ("Peter S. Kastner", "pete"),
    "bill": ("Bill Wallet", "bill"),
}

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")

# Citations in kw ask output look like [some-slug]
CITE_RE = re.compile(r"\[([a-z0-9][a-z0-9-]{2,})\]")

# Source line: "0.847  some-slug                              study"
SRC_LINE_RE = re.compile(
    r"^\s*(?P<score>[01]\.\d{3})\s+(?P<slug>[a-z0-9][a-z0-9-]+)\s+(?P<ptype>\S+)\s*$"
)

# Map pages_manifest.type -> classify_slugs bucket key (kept identical
# so frontmatter field names stay stable: related_studies etc.)
TYPE_BUCKETS = ("study", "entity", "technology", "code")


# ---------------------------------------------------------------------------
# Slug + title helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def build_slug(title: str, override: str | None) -> str:
    if override:
        if not SLUG_RE.match(override):
            sys.stderr.write(
                f"[kw note] invalid --slug '{override}'. "
                "Use lowercase, hyphens, digits only.\n"
            )
            sys.exit(2)
        return override
    base = slugify(title)
    today = date.today().isoformat()
    return f"note-{base}-{today}"


# ---------------------------------------------------------------------------
# Sources block parsing
# ---------------------------------------------------------------------------

def parse_sources_file(path: Path) -> list[dict]:
    """Parse a kw ask stderr capture for the --- Sources --- block."""
    if not path.exists():
        sys.stderr.write(f"[kw note] sources file not found: {path}\n")
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    sources = []
    in_block = False
    for line in lines:
        if "--- Sources ---" in line:
            in_block = True
            continue
        if not in_block:
            continue
        if line.startswith("[kw ask] filter:"):
            break
        m = SRC_LINE_RE.match(line)
        if m:
            sources.append({
                "slug": m.group("slug"),
                "score": float(m.group("score")),
                "page_type": m.group("ptype"),
            })
    return sources


# ---------------------------------------------------------------------------
# Slug index — load from data/pages_manifest.parquet (canonical wiki slugs)
# ---------------------------------------------------------------------------

def _load_from_pages_manifest() -> dict[str, set[str]] | None:
    """Read wiki page slugs from data/pages_manifest.parquet.

    Schema verified 2026-05-28:
      (slug VARCHAR, tier BIGINT, type VARCHAR)
      type ∈ {study, entity, technology, code}
      slug values are the actual wiki filename stems used in [[wikilinks]]

    Returns dict keyed by classify bucket name, or None if unavailable.
    """
    try:
        import duckdb  # type: ignore
    except ImportError:
        sys.stderr.write(
            "[kw note] warn: duckdb not installed; cannot load slug index.\n"
        )
        return None
    pm = DATA_DIR / "pages_manifest.parquet"
    if not pm.exists():
        sys.stderr.write(
            f"[kw note] warn: {pm} not found; falling back to per-type "
            "parquets (legacy v2 behavior).\n"
        )
        return None
    out: dict[str, set[str]] = {k: set() for k in TYPE_BUCKETS}
    try:
        con = duckdb.connect(":memory:")
        rows = con.execute(
            f"SELECT slug, type FROM read_parquet('{pm.as_posix()}') "
            "WHERE slug IS NOT NULL AND type IS NOT NULL"
        ).fetchall()
        con.close()
        for slug, t in rows:
            if t in out:
                out[t].add(slug)
    except Exception as e:
        sys.stderr.write(f"[kw note] warn: pages_manifest load failed: {e}\n")
        return None
    sys.stderr.write(
        f"[kw note] loaded slug index from {pm.name}: "
        f"studies={len(out['study'])} "
        f"entities={len(out['entity'])} "
        f"technologies={len(out['technology'])} "
        f"codes={len(out['code'])}\n"
    )
    return out


# Legacy fallback (v2 behavior) — only triggers if pages_manifest is missing.
# Reads from per-type parquets using their ID columns. NOTE: these IDs are
# internal master IDs (STU-..., ENT-..., TEC-...), not the wiki slugs. This
# fallback will fail to match any wiki-style citation; it exists only so a
# truly broken data/ dir doesn't crash the script.
LEGACY_SPEC = {
    "study":      ("studies.parquet",      "study_id"),
    "entity":     ("entities.parquet",     "entity_id"),
    "technology": ("technologies.parquet", "tech_id"),
}


def _load_from_legacy_parquets() -> dict[str, set[str]] | None:
    try:
        import duckdb  # type: ignore
    except ImportError:
        return None
    out: dict[str, set[str]] = {k: set() for k in TYPE_BUCKETS}
    any_loaded = False
    try:
        con = duckdb.connect(":memory:")
        for kind, (fname, col) in LEGACY_SPEC.items():
            fp = DATA_DIR / fname
            if not fp.exists():
                continue
            rows = con.execute(
                f"SELECT DISTINCT {col} FROM read_parquet('{fp.as_posix()}') "
                f"WHERE {col} IS NOT NULL"
            ).fetchall()
            out[kind] = {r[0] for r in rows if r[0]}
            any_loaded = True
        con.close()
    except Exception as e:
        sys.stderr.write(f"[kw note] warn: legacy parquet load failed: {e}\n")
        return None
    if not any_loaded:
        return None
    sys.stderr.write(
        "[kw note] loaded legacy ID index (NOT wiki slugs): "
        f"studies={len(out['study'])} "
        f"entities={len(out['entity'])} "
        f"technologies={len(out['technology'])}\n"
    )
    return out


def _load_master_slugs() -> dict[str, set[str]]:
    """Return {'entity': {...}, 'technology': {...}, 'study': {...}, 'code': {...}}.

    Order of preference:
      1. data/pages_manifest.parquet (the canonical wiki slug list — what
         [[wikilinks]] actually point at)
      2. Legacy per-type parquets keyed by master ID (last-resort fallback;
         won't match wiki-style citations)
      3. Empty sets (everything UNRESOLVES; clear warning emitted)
    """
    result = _load_from_pages_manifest()
    if result is not None:
        return result
    result = _load_from_legacy_parquets()
    if result is not None:
        return result
    sys.stderr.write(
        "[kw note] warn: no slug index available; all citations will be "
        "marked UNRESOLVED. Run `kw rebuild-embeddings` or "
        "`scripts/refresh_data_layer.py` to regenerate "
        "data/pages_manifest.parquet.\n"
    )
    return {k: set() for k in TYPE_BUCKETS}


def rewrite_citations(body: str) -> tuple[str, list[str]]:
    """Convert [slug] citations into [[slug]] wikilinks.

    Skips already-bracketed [[slug]] and skips obvious non-slug tokens
    (e.g. numeric refs, page numbers).
    """
    found: list[str] = []

    def _sub(m: re.Match) -> str:
        slug = m.group(1)
        # Skip if it's actually part of a double-bracket [[slug]]
        start = m.start()
        if start > 0 and body[start - 1] == "[":
            return m.group(0)
        found.append(slug)
        return f"[[{slug}]]"

    new_body = CITE_RE.sub(_sub, body)
    # Dedupe found while preserving order
    seen = set()
    ordered = []
    for s in found:
        if s not in seen:
            seen.add(s)
            ordered.append(s)
    return new_body, ordered


def classify_slugs(slugs: list[str], masters: dict[str, set[str]]) -> dict[str, list[str]]:
    """Bucket cited slugs into related_studies/entities/technologies/codes."""
    out: dict[str, list[str]] = {k: [] for k in TYPE_BUCKETS}
    out["unknown"] = []
    for s in slugs:
        placed = False
        for bucket in TYPE_BUCKETS:
            if s in masters.get(bucket, set()):
                out[bucket].append(s)
                placed = True
                break
        if not placed:
            out["unknown"].append(s)
    return out


# ---------------------------------------------------------------------------
# Frontmatter + body assembly
# ---------------------------------------------------------------------------

def _yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(items) + "]"


def _yaml_str(v: str) -> str:
    # Quote anything with a colon, dash leader, or special yaml char.
    if v == "":
        return '""'
    if re.search(r'[:#\-\[\]{},&*!|>%@`"]', v) or v.startswith(" ") or v.endswith(" "):
        return '"' + v.replace('"', '\\"') + '"'
    return v


def build_frontmatter(
    *,
    title: str,
    slug: str,
    author_name: str,
    author_id: str,
    created: str,
    updated: str,
    question: str | None,
    source_method: str,
    model: str | None,
    retrieval_k: int | None,
    related: dict[str, list[str]],
    extra_tags: list[str],
) -> str:
    tags = [f"type/note", f"author/{author_id}"] + extra_tags
    lines = [
        "---",
        f"title: {_yaml_str(title)}",
        f"slug: {slug}",
        "page_type: note",
        f"author: {_yaml_str(author_name)}",
        f"author_id: {author_id}",
        f"created: {created}",
        f"updated: {updated}",
    ]
    if question:
        lines.append(f"question: {_yaml_str(question)}")
    lines.append(f"source_method: {source_method}")
    if model:
        lines.append(f"model: {_yaml_str(model)}")
    if retrieval_k is not None:
        lines.append(f"retrieval_k: {retrieval_k}")
    lines.append("tier: 2")
    lines.append(f"tags: {_yaml_list(tags)}")
    lines.append(f"related_studies: {_yaml_list(related.get('study', []))}")
    lines.append(f"related_entities: {_yaml_list(related.get('entity', []))}")
    lines.append(f"related_technologies: {_yaml_list(related.get('technology', []))}")
    lines.append(f"related_codes: {_yaml_list(related.get('code', []))}")
    lines.append("---")
    return "\n".join(lines)


def build_body(
    *,
    title: str,
    question: str | None,
    created: str,
    answer: str,
    sources: list[dict],
    unknown_slugs: list[str],
) -> str:
    out = [f"# {title}", ""]
    if question:
        out.append(f"> **Question ({created}):** {question}")
        out.append("")
    out.append("## Answer")
    out.append("")
    out.append(answer.strip())
    out.append("")
    if sources:
        out.append("## Sources")
        out.append("")
        for s in sources:
            out.append(
                f"- [[{s['slug']}]] (score: {s['score']:.3f}, "
                f"page_type: {s['page_type']})"
            )
        out.append("")
    if unknown_slugs:
        out.append("## Unresolved citations")
        out.append("")
        out.append(
            "The following slugs were cited in the answer but were not found "
            "in `data/pages_manifest.parquet`. They may be stale, "
            "mis-spelled, or refer to pages outside the canonical archive:"
        )
        out.append("")
        for s in unknown_slugs:
            out.append(f"- `{s}`")
        out.append("")
    out.append("## Notes")
    out.append("")
    out.append("<!-- Add your annotations here. This section is yours. -->")
    out.append("")
    out.append("---")
    out.append(f"*Generated by `kw note` v3 on {created}. "
               "Edit freely — this is a permanent note.*")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# IO
# ---------------------------------------------------------------------------

def read_input(args) -> str:
    if args.body:
        return args.body
    if args.from_file:
        return Path(args.from_file).read_text(encoding="utf-8")
    if args.from_stdin or not sys.stdin.isatty():
        return sys.stdin.read()
    sys.stderr.write(
        "[kw note] no input. Pass --body TEXT, --from-file PATH, "
        "or pipe stdin.\n"
    )
    sys.exit(2)


def write_or_print(target: Path, content: str, commit: bool) -> None:
    if commit:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            sys.stderr.write(f"[kw note] refuse to overwrite {target}. "
                             "Use --update to append.\n")
            sys.exit(3)
        target.write_text(content, encoding="utf-8")
        sys.stderr.write(f"[kw note] wrote {target}\n")
        sys.stderr.write(
            "[kw note] hint: re-embed to make this note searchable:\n"
            "          kw rebuild-embeddings   (or scripts/reembed.py --ollama bge-m3)\n"
        )
    else:
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")
        sys.stderr.write(
            f"[kw note] DRY-RUN — would write {target.relative_to(ROOT)} "
            f"({len(content)} bytes). Re-run with --commit to save.\n"
        )


def append_to_existing(slug: str, addition: str, commit: bool) -> None:
    target = NOTES_DIR / f"{slug}.md"
    if not target.exists():
        sys.stderr.write(f"[kw note] no such note: {target.relative_to(ROOT)}\n")
        sys.exit(3)
    existing = target.read_text(encoding="utf-8")
    today = date.today().isoformat()
    # Bump `updated:` in frontmatter
    new_existing = re.sub(
        r"^updated:\s*.*$",
        f"updated: {today}",
        existing,
        count=1,
        flags=re.MULTILINE,
    )
    addition_block = (
        f"\n\n## Update ({today})\n\n{addition.strip()}\n"
    )
    final = new_existing.rstrip() + addition_block
    if commit:
        target.write_text(final, encoding="utf-8")
        sys.stderr.write(f"[kw note] appended to {target.relative_to(ROOT)}\n")
    else:
        sys.stdout.write(final)
        sys.stderr.write(
            f"[kw note] DRY-RUN append — re-run with --commit to save.\n"
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_author(arg: str) -> tuple[str, str]:
    if arg in AUTHORS:
        return AUTHORS[arg]
    # Freeform: derive id from first word
    short = re.sub(r"[^a-z0-9]+", "", arg.lower().split()[0])[:16] or "anon"
    return arg, short


def main():
    p = argparse.ArgumentParser(
        prog="kw note",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--title", help="Note title (required for new notes)")
    p.add_argument("--slug", help="Override slug (default: derived from title)")
    p.add_argument("--tags", default="",
                   help="Comma-separated extra tags (no 'type/note' prefix)")
    src = p.add_mutually_exclusive_group()
    src.add_argument("--from-file", help="Read answer body from file")
    src.add_argument("--from-stdin", action="store_true",
                     help="Read answer body from stdin (default if piped)")
    src.add_argument("--body", help="Inline answer body")
    p.add_argument("--author", default="pete",
                   help="pete|bill|<freeform name> (default: pete)")
    p.add_argument("--update",
                   help="Slug of existing note to append/replace")
    upd = p.add_mutually_exclusive_group()
    upd.add_argument("--append", action="store_true",
                     help="With --update: append as new Update section")
    upd.add_argument("--replace", action="store_true",
                     help="With --update: overwrite body (frontmatter kept)")
    p.add_argument("--question",
                   help="Original kw ask question, preserved in frontmatter")
    p.add_argument("--sources-from",
                   help="Path to a kw ask stderr capture; parses Sources block")
    p.add_argument("--model",
                   help="LLM model used (recorded in frontmatter)")
    p.add_argument("--retrieval-k", type=int,
                   help="k value used in kw ask (recorded in frontmatter)")
    p.add_argument("--commit", action="store_true",
                   help="Actually write the file (default is dry-run)")
    args = p.parse_args()

    # Update path
    if args.update:
        if not (args.append or args.replace):
            sys.stderr.write(
                "[kw note] --update requires either --append or --replace.\n"
            )
            sys.exit(2)
        addition = read_input(args)
        if args.replace:
            # Treat replace as: write a new body section, keep frontmatter.
            target = NOTES_DIR / f"{args.update}.md"
            if not target.exists():
                sys.stderr.write(
                    f"[kw note] no such note: {target.relative_to(ROOT)}\n"
                )
                sys.exit(3)
            existing = target.read_text(encoding="utf-8")
            m = re.match(r"^(---\n.*?\n---\n)", existing, re.DOTALL)
            if not m:
                sys.stderr.write(
                    "[kw note] could not find frontmatter in existing note.\n"
                )
                sys.exit(3)
            front = m.group(1)
            today = date.today().isoformat()
            front = re.sub(
                r"^updated:\s*.*$",
                f"updated: {today}",
                front,
                count=1,
                flags=re.MULTILINE,
            )
            new = front + "\n" + addition.strip() + "\n"
            if args.commit:
                target.write_text(new, encoding="utf-8")
                sys.stderr.write(
                    f"[kw note] replaced body of {target.relative_to(ROOT)}\n"
                )
            else:
                sys.stdout.write(new)
                sys.stderr.write(
                    "[kw note] DRY-RUN replace — re-run with --commit.\n"
                )
            return
        # default: append
        append_to_existing(args.update, addition, args.commit)
        return

    # New-note path
    if not args.title:
        sys.stderr.write("[kw note] --title is required for new notes.\n")
        sys.exit(2)

    raw_answer = read_input(args)

    # Wikilink proposal pass: rewrite [slug] -> [[slug]]
    body_with_links, cited_slugs = rewrite_citations(raw_answer)

    masters = _load_master_slugs()
    classified = classify_slugs(cited_slugs, masters)

    # Sources block (optional)
    sources: list[dict] = []
    if args.sources_from:
        sources = parse_sources_file(Path(args.sources_from))

    # Author
    author_name, author_id = resolve_author(args.author)

    # Slug + paths
    slug = build_slug(args.title, args.slug)
    target = NOTES_DIR / f"{slug}.md"

    # Tags
    extra_tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    # Source method inference
    source_method = "manual"
    if args.question or args.sources_from:
        source_method = "kw-ask"

    today = date.today().isoformat()

    front = build_frontmatter(
        title=args.title,
        slug=slug,
        author_name=author_name,
        author_id=author_id,
        created=today,
        updated=today,
        question=args.question,
        source_method=source_method,
        model=args.model,
        retrieval_k=args.retrieval_k,
        related=classified,
        extra_tags=extra_tags,
    )

    body = build_body(
        title=args.title,
        question=args.question,
        created=today,
        answer=body_with_links,
        sources=sources,
        unknown_slugs=classified["unknown"],
    )

    content = front + "\n\n" + body + "\n"

    # Proposal summary on stderr (always shown)
    sys.stderr.write(
        f"[kw note] slug: {slug}\n"
        f"[kw note] author: {author_name} ({author_id})\n"
        f"[kw note] wikilink rewrites: {len(cited_slugs)} citations\n"
        f"[kw note]   matched studies:      {len(classified['study'])}\n"
        f"[kw note]   matched entities:     {len(classified['entity'])}\n"
        f"[kw note]   matched technologies: {len(classified['technology'])}\n"
        f"[kw note]   matched codes:        {len(classified['code'])}\n"
        f"[kw note]   UNRESOLVED:           {len(classified['unknown'])}\n"
    )
    if classified["unknown"]:
        sys.stderr.write(
            f"[kw note]   (unresolved listed in the note body for review)\n"
        )

    write_or_print(target, content, args.commit)


if __name__ == "__main__":
    main()
