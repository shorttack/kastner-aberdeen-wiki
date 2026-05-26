#!/usr/bin/env python3
"""Surgical wiki propagation for the DEC longitudinal archival package."""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path("/home/user/workspace/kastner-aberdeen-wiki")
ARCHIVE_ROOT = Path("/home/user/workspace/aberdeen-group-archive")
STUDY_ID = "2026-kastner-dec-longitudinal-22d177"
ARCHIVE_COMMIT = "11670e8"

sys.path.insert(0, str(WIKI_ROOT / "scripts"))
from add_pass_a_v2_pages import build_entity_stub, build_full_study_page, build_tech_stub  # noqa: E402

csv.field_size_limit(sys.maxsize)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_text(path: Path, content: str) -> str:
    existed = path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "updated" if existed else "created"


def append_index_link() -> bool:
    index = WIKI_ROOT / "wiki" / "_index.md"
    text = index.read_text(encoding="utf-8")
    link = "- [[2026-kastner-dec-longitudinal-22d177|DEC longitudinal (1985–present)]]"
    if link in text:
        return False
    marker = "- [[2026-kastner-enterprise-ai-arc|Enterprise AI arc (1980–2024)]]"
    if marker in text:
        text = text.replace(marker, marker + "\n" + link)
    else:
        text += "\n## New longitudinal studies\n" + link + "\n"
    index.write_text(text, encoding="utf-8")
    return True


def update_manifest(stub_entities: int, stub_techs: int) -> None:
    path = WIKI_ROOT / "build_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["studies"] = 950
    manifest["entities"] = 3298
    manifest["technologies"] = 4388
    manifest["observations"] = 19773
    pass_a = manifest.setdefault("pass_a_v2", {})
    pass_a["applied_at"] = datetime.now(timezone.utc).isoformat()
    pass_a["source_archive_commit"] = ARCHIVE_COMMIT
    counts_after = pass_a.setdefault("data_layer", {}).setdefault("counts_after", {})
    counts_after.update({
        "studies": 950,
        "entities": 9510,
        "technologies": 7853,
        "observations": 19773,
        "known_entities": 3298,
        "known_technologies": 4388,
    })
    vault = pass_a.setdefault("vault_changes", {})
    studies = vault.setdefault("new_tier1_study_pages", [])
    if STUDY_ID not in studies:
        studies.append(STUDY_ID)
    vault["new_entity_stubs"] = int(vault.get("new_entity_stubs", 0)) + stub_entities
    vault["new_technology_stubs"] = int(vault.get("new_technology_stubs", 0)) + stub_techs
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    studies = load_csv(ARCHIVE_ROOT / "_master_studies.csv")
    known_entities = load_csv(ARCHIVE_ROOT / "_known_entities.csv")
    known_techs = load_csv(ARCHIVE_ROOT / "_known_technologies.csv")
    obs = load_csv(ARCHIVE_ROOT / "_master_observations.csv")
    master_entities = load_csv(ARCHIVE_ROOT / "_master_entities.csv")
    master_techs = load_csv(ARCHIVE_ROOT / "_master_technologies.csv")

    row = next((s for s in studies if s["study_id"] == STUDY_ID), None)
    if not row:
        raise SystemExit(f"{STUDY_ID} not found in master studies")

    ent_name_lookup = {e["entity_id"]: e.get("entity_name", e["entity_id"]) for e in known_entities}
    for e in master_entities:
        ent_name_lookup.setdefault(e["entity_id"], e.get("entity_name", e["entity_id"]))
    tech_name_lookup = {t["tech_id"]: t.get("tech_name", t["tech_id"]) for t in known_techs}
    for t in master_techs:
        tech_name_lookup.setdefault(t["tech_id"], t.get("tech_name", t["tech_id"]))
    name_ents = [{"entity_id": k, "entity_name": v} for k, v in ent_name_lookup.items()]
    name_techs = [{"tech_id": k, "tech_name": v} for k, v in tech_name_lookup.items()]

    page = build_full_study_page(row, obs, name_ents, name_techs)
    study_status = write_text(WIKI_ROOT / "wiki" / "studies" / f"{STUDY_ID}.md", page)

    dec_obs = [o for o in obs if o.get("study_id") == STUDY_ID]
    dec_entity_ids = sorted({o["entity_id"] for o in dec_obs if o.get("entity_id")})
    dec_tech_ids = sorted({o["tech_id"] for o in dec_obs if o.get("tech_id")})
    entity_by_id = {e["entity_id"]: e for e in known_entities}
    tech_by_id = {t["tech_id"]: t for t in known_techs}

    entity_stubs = 0
    for eid in dec_entity_ids:
        out = WIKI_ROOT / "wiki" / "entities" / f"{eid}.md"
        if out.exists():
            continue
        e = entity_by_id.get(eid) or next((x for x in master_entities if x["entity_id"] == eid), None)
        if not e:
            continue
        write_text(out, build_entity_stub(e, obs))
        entity_stubs += 1

    tech_stubs = 0
    for tid in dec_tech_ids:
        out = WIKI_ROOT / "wiki" / "technologies" / f"{tid}.md"
        if out.exists():
            continue
        t = tech_by_id.get(tid) or next((x for x in master_techs if x["tech_id"] == tid), None)
        if not t:
            continue
        write_text(out, build_tech_stub(t, obs))
        tech_stubs += 1

    index_changed = append_index_link()
    update_manifest(entity_stubs, tech_stubs)
    print({
        "study_page": study_status,
        "entity_stubs_created": entity_stubs,
        "technology_stubs_created": tech_stubs,
        "index_changed": index_changed,
    })


if __name__ == "__main__":
    main()
