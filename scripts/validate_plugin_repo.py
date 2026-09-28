#!/usr/bin/env python3
"""Validate the Naris Premium marketplace and plugin using only the Python stdlib."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN = ROOT / "plugins" / "naris-premium"
PORTABLE_MANIFEST = PLUGIN / "plugin.json"
COMPAT_MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_asset_path(value: object, field: str, errors: list[str]) -> None:
    if not isinstance(value, str):
        errors.append(f"Compatibility manifest field {field} must be a string")
        return
    require(value.startswith("./"), f"{field} must start with ./", errors)
    target = (PLUGIN / value).resolve()
    require(PLUGIN.resolve() in target.parents, f"{field} escapes plugin root: {value}", errors)
    require(target.is_file(), f"Referenced asset does not exist: {value}", errors)


def validate_skills(errors: list[str]) -> None:
    skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    require(bool(skill_files), "Plugin must include at least one skill", errors)
    for path in skill_files:
        text = path.read_text(encoding="utf-8-sig")
        require("[TODO:" not in text, f"TODO placeholder remains in {path.relative_to(ROOT)}", errors)
        require(text.startswith("---\n") or text.startswith("---\r\n"), f"Missing YAML frontmatter: {path.relative_to(ROOT)}", errors)
        match = re.search(r"(?m)^name:\s*[\"']?([^\"'\r\n]+)", text)
        require(bool(match), f"Missing skill name: {path.relative_to(ROOT)}", errors)
        if match:
            name = match.group(1).strip()
            require(bool(SKILL_NAME.fullmatch(name)), f"Invalid skill name '{name}' in {path.relative_to(ROOT)}", errors)
            require(path.parent.name == name, f"Skill folder and name differ: {path.parent.name} != {name}", errors)
        require(bool(re.search(r"(?m)^description:\s*.+", text)), f"Missing skill description: {path.relative_to(ROOT)}", errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-version", help="Require manifests to match a release version")
    args = parser.parse_args()
    errors: list[str] = []

    marketplace = load_json(MARKETPLACE, errors)
    portable = load_json(PORTABLE_MANIFEST, errors)
    compat = load_json(COMPAT_MANIFEST, errors)

    require(marketplace.get("name") == "naris-premium-marketplace", "Unexpected marketplace name", errors)
    entries = marketplace.get("plugins", [])
    require(isinstance(entries, list) and len(entries) == 1, "Marketplace must contain exactly one plugin", errors)
    if isinstance(entries, list) and entries:
        entry = entries[0]
        require(entry.get("name") == "naris-premium", "Marketplace plugin name must be naris-premium", errors)
        source = entry.get("source", {})
        require(source.get("source") == "local", "Marketplace plugin source must be local", errors)
        require(source.get("path") == "./plugins/naris-premium", "Marketplace plugin path is incorrect", errors)
        policy = entry.get("policy", {})
        require(policy.get("installation") in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}, "Invalid installation policy", errors)
        require(policy.get("authentication") in {"ON_INSTALL", "ON_USE"}, "Invalid authentication policy", errors)
        require(isinstance(entry.get("category"), str) and bool(entry.get("category")), "Marketplace category is required", errors)

    for label, manifest in (("portable", portable), ("compatibility", compat)):
        require(manifest.get("name") == "naris-premium", f"{label} manifest name must be naris-premium", errors)
        version = manifest.get("version")
        require(isinstance(version, str) and bool(SEMVER.fullmatch(version)), f"{label} manifest version must be valid semver", errors)
        require(isinstance(manifest.get("description"), str) and bool(manifest.get("description")), f"{label} manifest description is required", errors)

    require(portable.get("version") == compat.get("version"), "Portable and compatibility manifest versions differ", errors)
    if args.expected_version:
        require(portable.get("version") == args.expected_version, f"Tag version {args.expected_version} does not match plugin version {portable.get('version')}", errors)

    interface = compat.get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(isinstance(interface.get(field), str) and bool(interface.get(field)), f"Compatibility interface.{field} is required", errors)
    for field in ("composerIcon", "logo", "logoDark"):
        if field in interface:
            validate_asset_path(interface[field], field, errors)
    screenshots = interface.get("screenshots", [])
    require(isinstance(screenshots, list), "interface.screenshots must be an array", errors)
    if isinstance(screenshots, list):
        for index, value in enumerate(screenshots):
            validate_asset_path(value, f"screenshots[{index}]", errors)
            if isinstance(value, str):
                require(value.lower().endswith(".png"), f"Screenshot must be PNG: {value}", errors)

    validate_skills(errors)

    if errors:
        print("Plugin validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Plugin validation passed: naris-premium {portable.get('version')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

