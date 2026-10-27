#!/usr/bin/env python3
"""Validate profile/README.md against labs-registry.json (Galhoom Labs)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "labs-registry.json"
README_PATH = ROOT / "profile" / "README.md"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not REGISTRY_PATH.is_file():
        fail(f"missing registry: {REGISTRY_PATH}")
    if not README_PATH.is_file():
        fail(f"missing README: {README_PATH}")

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    readme = README_PATH.read_text(encoding="utf-8")
    lowered = readme.lower()

    if registry.get("organization") != "galhoom-labs":
        fail("registry.organization must be galhoom-labs")

    categories = registry["categories"]
    repos = registry.get("repos") or []

    # 1) Category IDs contiguous 1..N
    cat_ids = [c["id"] for c in categories]
    if cat_ids != list(range(1, len(categories) + 1)):
        fail(f"categories must be contiguous 1..N, got {cat_ids}")

    # 2) Promise language
    if "real product" not in lowered and "real products" not in lowered:
        fail("README must state Labs is about real product(s)")
    if "galhoom-path" not in lowered:
        fail("README must link/cross-reference galhoom-path")
    if "practice" not in lowered and "learn" not in lowered:
        fail("README must contrast with learning/practice (Path)")

    # 3) Category labels from registry must appear (diagram / copy)
    for c in categories:
        for key in ("diagram_label", "item_label", "name"):
            label = c.get(key)
            if not label:
                continue
            # name alone may be too short; require diagram_label always
            if key == "diagram_label" and label not in readme:
                fail(f"README missing category diagram label: {label!r}")
            if key == "item_label" and label not in readme:
                fail(f"README missing category item label: {label!r}")

    # 4) Mermaid style intact
    if "flowchart TB" not in readme:
        fail("README Mermaid must use flowchart TB")
    if "classDef org" not in readme or "classDef track" not in readme:
        fail("README Mermaid must keep classDef org/track style")
    if 'LABS["🧪 galhoom-labs"]' not in readme:
        fail("README Mermaid must keep Labs root node")

    # 5) Banned category expansion while out_for_now
    out = [x.lower() for x in registry.get("scope", {}).get("out_for_now", [])]
    if any("libraries" in x for x in out):
        # diagram must not resurrect Libraries / Templates tracks
        if re.search(r"📦\s*Libraries|Libraries\s*&\s*packages", readme):
            fail("README must not list Libraries while scope.out_for_now includes them")
        if re.search(r"📋\s*Templates|Generic starters", readme):
            fail("README must not list Templates while scope.out_for_now includes them")

    # 6) Every registered product ID must appear once repos exist
    for repo in repos:
        rid = repo["id"]
        pattern = rf"(?<![0-9.]){re.escape(rid)}(?![0-9])"
        if not re.search(pattern, readme):
            fail(f"README missing product ID {rid} ({repo.get('name')})")

    # 7) Within each category, IDs ascending in README when present
    by_cat: dict[int, list[dict]] = {}
    for repo in repos:
        by_cat.setdefault(repo["category"], []).append(repo)

    for cat_id, cat_repos in sorted(by_cat.items()):

        def minor(r: dict) -> tuple[int, str]:
            _major, _, rest = r["id"].partition(".")
            m = re.match(r"^(\d+)", rest)
            return (int(m.group(1)) if m else 0, rest)

        ordered = sorted(cat_repos, key=minor)
        positions = []
        for r in ordered:
            m = re.search(rf"(?<![0-9.]){re.escape(r['id'])}(?![0-9])", readme)
            if not m:
                fail(f"could not locate ID {r['id']} for order check")
            positions.append((r["id"], m.start()))
        for (a_id, a_pos), (b_id, b_pos) in zip(positions, positions[1:]):
            if a_pos >= b_pos:
                fail(
                    f"Category {cat_id} product order broken: "
                    f"{a_id} must appear before {b_id}"
                )

    print("OK: labs-registry.json <-> profile/README.md checks passed.")
    print(f"  categories: {len(categories)} | products: {len(repos)}")


if __name__ == "__main__":
    main()
