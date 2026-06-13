#!/usr/bin/env python3
"""
kw_console_v1.py — Localhost web UI for annotating the Kastner wiki.

Purpose
-------
Browser-driven companion to `kw_note.py`. Eliminates command-typing for the
common case: find a study/entity/technology, write a freeform note or
rebuttal, save (+ optional commit).

Three entry modes:
  1. Paste-slug   — paste a slug or [[wikilink]] from Obsidian, resolve it
  2. Browse       — paginated list of studies / entities / technologies
  3. Search       — case-insensitive substring match across slug + title

Output: writes a markdown file to <WIKI_ROOT>/wiki/notes/<slug>.md, using
the same frontmatter shape as `kw_note.py` v4 (so Phase 5 embeddings and
`kw ask` retrieval keep working unchanged).

Run:
  python3 scripts/kw_console_v1.py            # binds 127.0.0.1:8765
  python3 scripts/kw_console_v1.py --port 9000

Or via launcher:
  kw console

Stack: FastAPI + uvicorn (single dep beyond stdlib), DuckDB read-only via
the canonical wiki at ~/Repos/kastner-aberdeen-wiki/db/kastner.duckdb.

Pete-only design rules satisfied:
  * Localhost only (no 0.0.0.0 bind, no auth needed)
  * Reuses kw_note v4 frontmatter/citation helpers; no duplication
  * page_type ∈ {note, rebuttal}; rebuttals carry extra fields
  * Pending-notes banner reads `git status wiki/notes/` on every browse
  * "Commit all now" runs `git add wiki/notes/ && git commit -m ... && git push`
  * "Dismiss until tomorrow" sets a session cookie that expires at midnight local

Version: v1.0  2026-06-13
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

# stdlib re-imports for kw_note helpers
import importlib.util

try:
    from fastapi import FastAPI, Form, HTTPException, Request
    from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
    from fastapi.staticfiles import StaticFiles
    import uvicorn
except ImportError as e:
    sys.stderr.write(
        f"[kw console] Missing dependency: {e}\n"
        "Install with: pip3 install fastapi uvicorn python-multipart\n"
    )
    sys.exit(2)

try:
    import duckdb
except ImportError:
    sys.stderr.write(
        "[kw console] Missing dependency: duckdb\n"
        "Install with: pip3 install duckdb\n"
        "(also required: python-multipart for form posts)\n"
    )
    sys.exit(2)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # wiki repo root
WIKI_ROOT = ROOT / "wiki"
NOTES_DIR = WIKI_ROOT / "notes"
DB_PATH = ROOT / "db" / "kastner.duckdb"
TEMPLATE_PATH = SCRIPT_DIR.parent / "templates" / "console.html"

# Import kw_note as a library
KW_NOTE_PATH = SCRIPT_DIR / "kw_note.py"
if not KW_NOTE_PATH.exists():
    sys.stderr.write(
        f"[kw console] Required sibling not found: {KW_NOTE_PATH}\n"
        "kw_console expects to live alongside kw_note.py under scripts/.\n"
    )
    sys.exit(2)

_spec = importlib.util.spec_from_file_location("kw_note", KW_NOTE_PATH)
kw_note = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kw_note)

# Reused functions from kw_note v4
slugify = kw_note.slugify
build_frontmatter = kw_note.build_frontmatter
_load_master_slugs_raw = kw_note._load_master_slugs

# Cache the slug index once per process — v1.0 reloaded the 10K-row parquet
# on every keystroke debounce (one /api/resolve per typed char). Phase 5
# auto-embeds new notes; new wiki pages only appear after a Phase 3 regen,
# and the user restarts kw console between sessions anyway, so a process-
# lifetime cache is safe.
_masters_cache: "dict[str, set[str]] | None" = None

def _load_master_slugs() -> "dict[str, set[str]]":
    global _masters_cache
    if _masters_cache is None:
        _masters_cache = _load_master_slugs_raw()
    return _masters_cache

_yaml_list = kw_note._yaml_list
_yaml_str = kw_note._yaml_str
AUTHORS = kw_note.AUTHORS

# ---------------------------------------------------------------------------
# Helpers — slug normalization, pending notes, git
# ---------------------------------------------------------------------------

WIKILINK_RE = re.compile(r"\[\[([^\[\]|]+?)(?:\|[^\[\]]*)?\]\]")
PATH_RE = re.compile(r"wiki/(?:studies|entities|technologies|codes|notes)/([^/]+?)\.md")


# Unicode dashes that macOS "Smart Dashes" and copy/paste from Word/Obsidian
# routinely substitute for plain ASCII hyphen-minus. Fold them ALL to '-'.
#   U+2010 hyphen, U+2011 non-breaking hyphen, U+2012 figure dash,
#   U+2013 en-dash, U+2014 em-dash, U+2015 horizontal bar, U+2212 minus sign
_DASH_FOLD = str.maketrans({
    "\u2010": "-", "\u2011": "-", "\u2012": "-",
    "\u2013": "-", "\u2014": "-", "\u2015": "-",
    "\u2212": "-",
})


def normalize_slug_input(raw: str) -> str:
    """Accept full slug, [[wikilink]], wiki/<type>/<slug>.md path; return bare slug.

    Also folds Unicode dashes → ASCII '-' (macOS Smart Dashes trap).
    """
    s = raw.strip()
    if not s:
        return ""
    # Fold Unicode dashes BEFORE regex matching
    s = s.translate(_DASH_FOLD)
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1).strip()
    m = PATH_RE.search(s)
    if m:
        s = m.group(1).strip()
    # If still has leading wiki/notes/ etc., strip
    s = s.replace("\\", "/")
    if "/" in s:
        s = s.rsplit("/", 1)[-1]
    if s.endswith(".md"):
        s = s[:-3]
    # Fold dashes again post-strip in case .md/path-stripping reintroduced them
    s = s.translate(_DASH_FOLD)
    return s.lower()


# Map bucket name → wiki-filename prefix used in pages_manifest.parquet.
# These prefixes are on the manifest slugs (e.g. "study-dec-mgmt-memo-...")
# but NOT on v_studies.study_id / v_entities.entity_id / v_technologies.tech_id.
# The DB stores the BASE form; we must return the base form so fetch_subject works.
_BUCKET_PREFIX = {
    "study": "study-",
    "entity": "entity-",
    "technology": "technology-",
    "code": "code-",
}


def _base_form(slug: str, bucket: str) -> str:
    """Strip the bucket prefix if present. 'study-foo' → 'foo'; 'foo' → 'foo'."""
    pfx = _BUCKET_PREFIX.get(bucket, "")
    if pfx and slug.startswith(pfx):
        return slug[len(pfx):]
    return slug


def _match_in_bucket(slug: str, bucket_slugs: set[str], bucket: str) -> Optional[str]:
    """Try both forms (with/without type prefix) against the manifest slug set.

    Returns the MATCHED manifest slug if found, else None.
    Caller is responsible for stripping the prefix before returning to fetch_subject.
    """
    if slug in bucket_slugs:
        return slug
    prefixed = _BUCKET_PREFIX.get(bucket, "") + slug
    if prefixed in bucket_slugs:
        return prefixed
    return None


def resolve_slug(slug: str, masters: dict[str, set[str]]) -> tuple[Optional[str], list[dict]]:
    """
    Return (resolved_type, candidates) where each candidate slug is the BASE
    form (no 'study-' / 'entity-' / etc. prefix), since that's what v_studies
    et al. key on.

    - If slug matches exactly in one bucket → ('study'|..., [single])
    - If slug is a unique prefix → as above
    - If ambiguous → (None, [list of {slug, type}])
    - If no match → (None, [])
    """
    if not slug:
        return None, []

    # exact match across all buckets, trying both base and type-prefixed forms
    exact = []
    for bucket, slugs in masters.items():
        hit = _match_in_bucket(slug, slugs, bucket)
        if hit:
            exact.append({"slug": _base_form(hit, bucket), "type": bucket})
    if len(exact) == 1:
        return exact[0]["type"], exact
    if len(exact) > 1:
        return None, exact

    # prefix match — try both forms of the query against the manifest slugs
    prefix_matches = []
    for bucket, slugs in masters.items():
        candidates_to_try = [slug, _BUCKET_PREFIX.get(bucket, "") + slug]
        for c in candidates_to_try:
            if not c:
                continue
            for s in slugs:
                if s.startswith(c):
                    prefix_matches.append({"slug": _base_form(s, bucket), "type": bucket})
    # de-dupe (a manifest slug can match both forms when type prefix is empty)
    seen = set()
    deduped = []
    for m in prefix_matches:
        key = (m["type"], m["slug"])
        if key not in seen:
            seen.add(key)
            deduped.append(m)
    prefix_matches = deduped
    if len(prefix_matches) == 1:
        return prefix_matches[0]["type"], prefix_matches
    if len(prefix_matches) > 1:
        return None, prefix_matches[:50]

    # substring fallback — catches partial-title pastes and middle-of-slug fragments.
    substring_matches = []
    for bucket, slugs in masters.items():
        for s in slugs:
            if slug in s:
                substring_matches.append({"slug": _base_form(s, bucket), "type": bucket})
                if len(substring_matches) > 50:
                    break
        if len(substring_matches) > 50:
            break
    # de-dupe substring matches too
    seen = set()
    deduped = []
    for m in substring_matches:
        key = (m["type"], m["slug"])
        if key not in seen:
            seen.add(key)
            deduped.append(m)
    substring_matches = deduped
    if len(substring_matches) == 1:
        return substring_matches[0]["type"], substring_matches
    if len(substring_matches) > 1:
        return None, substring_matches[:50]

    return None, []


def pending_notes() -> list[dict]:
    """git status --porcelain wiki/notes/ -> list of {path, status, mtime}."""
    if not (ROOT / ".git").exists():
        return []
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--porcelain", "wiki/notes/"],
            capture_output=True, text=True, timeout=5,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []
    if out.returncode != 0:
        return []
    notes = []
    for line in out.stdout.splitlines():
        if not line.strip():
            continue
        # porcelain: "XY filename"
        status = line[:2]
        path_part = line[3:].strip()
        if not path_part.endswith(".md"):
            continue
        full = ROOT / path_part
        try:
            mtime = dt.datetime.fromtimestamp(full.stat().st_mtime).strftime("%H:%M")
        except FileNotFoundError:
            mtime = "?"
        notes.append({
            "path": path_part,
            "name": Path(path_part).name,
            "status": status.strip(),
            "mtime": mtime,
        })
    return notes


def git_commit_notes(message: str) -> tuple[bool, str]:
    """git add wiki/notes/ && git commit -m ... && git push. Returns (ok, log)."""
    log_lines = []
    try:
        r = subprocess.run(
            ["git", "-C", str(ROOT), "add", "wiki/notes/"],
            capture_output=True, text=True, timeout=15,
        )
        log_lines.append(f"$ git add wiki/notes/\n{r.stdout}{r.stderr}")
        if r.returncode != 0:
            return False, "\n".join(log_lines)

        r = subprocess.run(
            ["git", "-C", str(ROOT), "commit", "-m", message],
            capture_output=True, text=True, timeout=15,
        )
        log_lines.append(f"$ git commit -m {message!r}\n{r.stdout}{r.stderr}")
        if r.returncode != 0:
            # nothing to commit is fine; surface message
            return False, "\n".join(log_lines)

        r = subprocess.run(
            ["git", "-C", str(ROOT), "push"],
            capture_output=True, text=True, timeout=60,
        )
        log_lines.append(f"$ git push\n{r.stdout}{r.stderr}")
        if r.returncode != 0:
            return False, "\n".join(log_lines)
    except subprocess.TimeoutExpired as e:
        log_lines.append(f"TIMEOUT: {e}")
        return False, "\n".join(log_lines)
    return True, "\n".join(log_lines)


# ---------------------------------------------------------------------------
# DuckDB read-only queries
# ---------------------------------------------------------------------------

def db_conn():
    if not DB_PATH.exists():
        raise HTTPException(503, f"DuckDB not found at {DB_PATH}. Run Phase 1+2.")
    return duckdb.connect(str(DB_PATH), read_only=True)


def list_studies(q: str | None, limit: int, offset: int) -> list[dict]:
    # v_studies columns (DESCRIBE 2026-06-13 on Pete's Mac): study_id, title,
    # author, date, type, subject_domain, methodology, source_file, abstract,
    # license, importance, importance_rationale, relevance, relevance_rationale,
    # study_prescience_enum, study_prescience_rationale, pub_year,
    # prescience_max, prescience_mean, prescience_obs_count.
    # No "collection_type" column — use "type" instead.
    sql = """
        SELECT study_id AS slug, title, pub_year, study_prescience_enum AS prescience,
               prescience_obs_count, type AS collection_type
        FROM v_studies
    """
    params: list = []
    if q:
        sql += " WHERE LOWER(study_id) LIKE ? OR LOWER(title) LIKE ?"
        like = f"%{q.lower()}%"
        params = [like, like]
    sql += " ORDER BY pub_year DESC NULLS LAST, study_id ASC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    with db_conn() as c:
        rows = c.execute(sql, params).fetchall()
        cols = [d[0] for d in c.description]
    return [dict(zip(cols, r)) for r in rows]


def list_entities(q: str | None, limit: int, offset: int) -> list[dict]:
    sql = """
        SELECT entity_id AS slug, entity_name AS title, entity_type AS category,
               occurrence_count AS obs_count
        FROM v_entities
    """
    params: list = []
    if q:
        sql += " WHERE LOWER(entity_id) LIKE ? OR LOWER(entity_name) LIKE ?"
        like = f"%{q.lower()}%"
        params = [like, like]
    sql += " ORDER BY occurrence_count DESC NULLS LAST, entity_id ASC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    with db_conn() as c:
        rows = c.execute(sql, params).fetchall()
        cols = [d[0] for d in c.description]
    return [dict(zip(cols, r)) for r in rows]


def list_technologies(q: str | None, limit: int, offset: int) -> list[dict]:
    sql = """
        SELECT tech_id AS slug, tech_name AS title, tech_type AS category,
               occurrence_count AS obs_count
        FROM v_technologies
    """
    params: list = []
    if q:
        sql += " WHERE LOWER(tech_id) LIKE ? OR LOWER(tech_name) LIKE ?"
        like = f"%{q.lower()}%"
        params = [like, like]
    sql += " ORDER BY occurrence_count DESC NULLS LAST, tech_id ASC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    with db_conn() as c:
        rows = c.execute(sql, params).fetchall()
        cols = [d[0] for d in c.description]
    return [dict(zip(cols, r)) for r in rows]


def fetch_subject(slug: str, kind: str) -> dict | None:
    """Pull a single subject row for the annotation form."""
    if kind == "study":
        sql = """
            SELECT study_id AS slug, title, author, pub_year, type AS collection_type,
                   subject_domain, study_prescience_enum AS prescience,
                   study_prescience_rationale AS prescience_rationale,
                   prescience_mean, prescience_obs_count
            FROM v_studies WHERE study_id = ?
        """
    elif kind == "entity":
        sql = """
            SELECT entity_id AS slug, entity_name AS title, entity_type AS category,
                   occurrence_count AS obs_count
            FROM v_entities WHERE entity_id = ?
        """
    elif kind == "technology":
        sql = """
            SELECT tech_id AS slug, tech_name AS title, tech_type AS category,
                   occurrence_count AS obs_count
            FROM v_technologies WHERE tech_id = ?
        """
    else:
        return None
    with db_conn() as c:
        rows = c.execute(sql, [slug]).fetchall()
        if not rows:
            return None
        cols = [d[0] for d in c.description]
    return dict(zip(cols, rows[0]))


# ---------------------------------------------------------------------------
# Save logic
# ---------------------------------------------------------------------------

def make_note_slug(subject_slug: str, page_type: str, date: str) -> str:
    """note-<subject>-<date>  or  rebuttal-<subject>-<date> ; truncate subject to 40."""
    prefix = "rebuttal" if page_type == "rebuttal" else "note"
    truncated = subject_slug[:40]
    base = f"{prefix}-{truncated}-{date}"
    # If exists, bump v2/v3/...
    target = NOTES_DIR / f"{base}.md"
    if not target.exists():
        return base
    for v in range(2, 100):
        candidate = f"{base}-v{v}"
        if not (NOTES_DIR / f"{candidate}.md").exists():
            return candidate
    raise RuntimeError(f"Cannot find an unused slug variant for {base}")


def render_body(
    *,
    title: str,
    page_type: str,
    subject: dict,
    subject_kind: str,
    body_md: str,
    scorer_baseline: str | None,
) -> str:
    parts = [f"# {title}", ""]
    parts.append(f"**Target:** [[{subject['slug']}]] ({subject_kind})  ")
    if "title" in subject and subject.get("title"):
        parts.append(f"**Subject title:** {subject['title']}  ")
    if page_type == "rebuttal" and scorer_baseline:
        parts.append(f"**Scorer baseline:** {scorer_baseline}  ")
    parts.append("")
    if page_type == "rebuttal":
        parts.append("## Player rebuttal")
    else:
        parts.append("## Annotation")
    parts.append("")
    parts.append(body_md.strip())
    parts.append("")
    parts.append("---")
    parts.append(f"*Generated by `kw console` v1 on "
                 f"{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}.*")
    return "\n".join(parts)


def write_note(
    *,
    subject_slug: str,
    subject_kind: str,
    title: str,
    body_md: str,
    page_type: str,
    author_key: str,
    scorer_baseline: str | None,
    commit: bool,
) -> dict:
    subject = fetch_subject(subject_slug, subject_kind)
    if not subject:
        raise HTTPException(404, f"Subject not found: {subject_slug} ({subject_kind})")

    author_name, author_id = AUTHORS.get(author_key, (author_key, slugify(author_key)))
    today = dt.date.today().isoformat()
    slug = make_note_slug(subject_slug, page_type, today)

    # Build related-* dict for frontmatter
    related = {"study": [], "entity": [], "technology": [], "code": []}
    related[subject_kind].append(subject_slug)

    # Frontmatter via kw_note helper — augment with rebuttal-specific fields
    fm = build_frontmatter(
        title=title,
        slug=slug,
        author_name=author_name,
        author_id=author_id,
        created=today,
        updated=today,
        question=None,
        source_method="kw_console_v1",
        model=None,
        retrieval_k=None,
        related=related,
        extra_tags=[
            f"page_type/{page_type}",
        ] + ([f"rebuts/{subject_slug}"] if page_type == "rebuttal" else []),
    )

    # Patch page_type line for rebuttals (frontmatter default is "note")
    if page_type == "rebuttal":
        fm = fm.replace("page_type: note", "page_type: rebuttal", 1)
        # Inject rebuts_study + scorer_baseline before closing ---
        injected = [f"rebuts_study: {subject_slug}"]
        if scorer_baseline:
            injected.append(f"scorer_baseline: {_yaml_str(scorer_baseline)}")
        fm_lines = fm.splitlines()
        # insert before the final ---
        for i in range(len(fm_lines) - 1, -1, -1):
            if fm_lines[i] == "---":
                fm_lines[i:i] = injected
                break
        fm = "\n".join(fm_lines)

    body = render_body(
        title=title,
        page_type=page_type,
        subject=subject,
        subject_kind=subject_kind,
        body_md=body_md,
        scorer_baseline=scorer_baseline,
    )

    content = fm + "\n\n" + body + "\n"

    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    target = NOTES_DIR / f"{slug}.md"
    if target.exists():
        raise HTTPException(409, f"Refusing to overwrite existing note: {target}")
    target.write_text(content, encoding="utf-8")

    result = {
        "ok": True,
        "slug": slug,
        "path": str(target.relative_to(ROOT)),
        "committed": False,
        "git_log": "",
    }

    if commit:
        msg = f"kw console: add {('rebuttal' if page_type == 'rebuttal' else 'note')} {slug}"
        ok, log = git_commit_notes(msg)
        result["committed"] = ok
        result["git_log"] = log

    return result


# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(title="KW Console", version="1.0")


def _template() -> str:
    if not TEMPLATE_PATH.exists():
        raise HTTPException(500, f"Template not found: {TEMPLATE_PATH}")
    return TEMPLATE_PATH.read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
def root():
    return _template()


@app.get("/api/pending")
def api_pending():
    return {"notes": pending_notes()}


@app.post("/api/commit-pending")
def api_commit_pending(message: str = Form(default="kw console: commit pending notes")):
    ok, log = git_commit_notes(message)
    return {"ok": ok, "log": log}


@app.get("/api/list")
def api_list(kind: str, q: Optional[str] = None,
             limit: int = 50, offset: int = 0):
    limit = max(1, min(limit, 200))
    if kind == "study":
        items = list_studies(q, limit, offset)
    elif kind == "entity":
        items = list_entities(q, limit, offset)
    elif kind == "technology":
        items = list_technologies(q, limit, offset)
    else:
        raise HTTPException(400, f"Unknown kind: {kind}")
    return {"kind": kind, "items": items, "limit": limit, "offset": offset}


@app.get("/api/resolve")
def api_resolve(raw: str):
    normalized = normalize_slug_input(raw)
    if not normalized:
        return {"ok": False, "error": "empty slug", "candidates": []}
    masters = _load_master_slugs()
    kind, candidates = resolve_slug(normalized, masters)
    if kind:
        # resolver now returns the BASE slug (no type prefix) in candidates,
        # which is what v_studies/v_entities/v_technologies use as their PK.
        resolved_slug = candidates[0]["slug"]
        subject = fetch_subject(resolved_slug, kind)
        return {"ok": True, "kind": kind, "slug": resolved_slug,
                "subject": subject, "candidates": candidates}
    return {"ok": False, "error": "ambiguous_or_missing",
            "normalized": normalized, "candidates": candidates}


@app.get("/api/subject")
def api_subject(kind: str, slug: str):
    subject = fetch_subject(slug, kind)
    if not subject:
        raise HTTPException(404, f"{kind} not found: {slug}")
    return {"ok": True, "kind": kind, "subject": subject}


@app.post("/api/save")
def api_save(
    subject_kind: str = Form(...),
    subject_slug: str = Form(...),
    title: str = Form(...),
    body_md: str = Form(...),
    page_type: str = Form("note"),
    author: str = Form("pete"),
    scorer_baseline: str = Form(""),
    commit: str = Form("no"),  # "yes" or "no"
):
    if page_type not in ("note", "rebuttal"):
        raise HTTPException(400, f"Bad page_type: {page_type}")
    if subject_kind not in ("study", "entity", "technology"):
        raise HTTPException(400, f"Bad subject_kind: {subject_kind}")
    if not title.strip():
        raise HTTPException(400, "Title is required")
    if not body_md.strip():
        raise HTTPException(400, "Body is required")
    try:
        result = write_note(
            subject_slug=subject_slug,
            subject_kind=subject_kind,
            title=title.strip(),
            body_md=body_md,
            page_type=page_type,
            author_key=author,
            scorer_baseline=scorer_baseline.strip() or None,
            commit=(commit.lower() == "yes"),
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"{type(e).__name__}: {e}")
    return result


@app.get("/api/health")
def api_health():
    return {
        "ok": True,
        "wiki_root": str(WIKI_ROOT),
        "notes_dir": str(NOTES_DIR),
        "db_path": str(DB_PATH),
        "db_exists": DB_PATH.exists(),
    }


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="KW Console v1 — annotation UI")
    p.add_argument("--host", default="127.0.0.1",
                   help="Bind host (default: 127.0.0.1 — localhost only)")
    p.add_argument("--port", type=int, default=8765,
                   help="Bind port (default: 8765)")
    p.add_argument("--reload", action="store_true",
                   help="Auto-reload on code change (dev only)")
    args = p.parse_args()

    if args.host not in ("127.0.0.1", "localhost", "::1"):
        sys.stderr.write(
            f"[kw console] Refusing to bind non-localhost host: {args.host}\n"
            "KW Console is single-user, no-auth, localhost-only by design.\n"
        )
        sys.exit(2)

    if not DB_PATH.exists():
        sys.stderr.write(
            f"[kw console] DuckDB not found at {DB_PATH}\n"
            "Run Phase 1+2 first.\n"
        )
        sys.exit(3)

    sys.stderr.write(
        f"[kw console] Starting on http://{args.host}:{args.port}\n"
        f"[kw console]   wiki_root = {WIKI_ROOT}\n"
        f"[kw console]   notes_dir = {NOTES_DIR}\n"
        f"[kw console]   db_path   = {DB_PATH}\n"
    )

    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload, log_level="info")


if __name__ == "__main__":
    main()
