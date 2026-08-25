"""Docs and manifest consistency checks, verified on every PR, push, and release.

What this locks in:
- Claude and Codex marketplaces list exactly the plugin directories on disk;
- marketplace sources point to the matching plugin directories;
- newest released CHANGELOG version matches every provider manifest;
- README and marketplace aggregate counts match disk;
- plugin README section counts match disk when declared;
- every plugin README documents the supported multi-LLM usage paths;
- every /plugin:command reference in a plugin README resolves to a real command file.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"


def plugin_dirs():
    return sorted(
        p
        for p in ROOT.iterdir()
        if p.is_dir() and (p / ".claude-plugin" / "plugin.json").is_file()
    )


def skill_count(plugin: Path) -> int:
    skills = plugin / "skills"
    if not skills.is_dir():
        return 0
    return sum(1 for s in skills.iterdir() if s.is_dir())


def command_count(plugin: Path) -> int:
    cmds = plugin / "commands"
    if not cmds.is_dir():
        return 0
    return len(list(cmds.glob("*.md")))


def marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def codex_marketplace() -> dict:
    return json.loads(CODEX_MARKETPLACE.read_text(encoding="utf-8"))


def latest_changelog_version() -> str:
    for line in CHANGELOG.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## v(\d+\.\d+\.\d+)\b", line)
        if m:
            return m.group(1)
    raise AssertionError("no ## vX.Y.Z heading found in CHANGELOG.md")


class TestMarketplaceList(unittest.TestCase):
    def test_marketplace_lists_exactly_the_plugins_on_disk(self):
        listed = {p["name"] for p in marketplace()["plugins"]}
        on_disk = {p.name for p in plugin_dirs()}
        self.assertEqual(
            listed,
            on_disk,
            f"marketplace.json vs disk: only listed={sorted(listed - on_disk)}, "
            f"only on disk={sorted(on_disk - listed)}",
        )

    def test_sources_point_at_matching_directories(self):
        for p in marketplace()["plugins"]:
            source = p["source"]
            if isinstance(source, str):
                self.assertEqual(source, f"./{p['name']}")
                continue

            self.assertIsInstance(source, dict, f"unsupported source shape for {p['name']}")
            self.assertEqual(source.get("source"), "git-subdir")
            self.assertEqual(source.get("path"), p["name"])
            self.assertTrue(source.get("url"), f"missing git-subdir url for {p['name']}")
            self.assertTrue(source.get("ref"), f"missing git-subdir ref for {p['name']}")


class TestCodexMarketplace(unittest.TestCase):
    def test_codex_marketplace_lists_exactly_the_plugins_on_disk(self):
        listed = {p["name"] for p in codex_marketplace()["plugins"]}
        on_disk = {p.name for p in plugin_dirs()}
        self.assertEqual(
            listed,
            on_disk,
            f"Codex marketplace vs disk: only listed={sorted(listed - on_disk)}, "
            f"only on disk={sorted(on_disk - listed)}",
        )

    def test_codex_sources_point_at_matching_directories(self):
        for p in codex_marketplace()["plugins"]:
            source = p.get("source", {})
            self.assertEqual(source.get("source"), "local", p["name"])
            self.assertEqual(source.get("path"), f"./{p['name']}", p["name"])

    def test_every_plugin_has_codex_manifest(self):
        for p in plugin_dirs():
            manifest = p / ".codex-plugin" / "plugin.json"
            self.assertTrue(manifest.is_file(), f"missing Codex manifest: {manifest.relative_to(ROOT)}")
            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(data.get("name"), p.name, p.name)
            self.assertEqual(data.get("skills"), "./skills/", p.name)
            self.assertTrue(data.get("interface", {}).get("displayName"), p.name)


class TestVersionSync(unittest.TestCase):
    def test_all_versions_identical_and_match_changelog(self):
        want = latest_changelog_version()
        mismatches = []
        mp_version = marketplace()["version"]
        if mp_version != want:
            mismatches.append(f"marketplace.json={mp_version}")
        for p in plugin_dirs():
            claude_manifest = p / ".claude-plugin" / "plugin.json"
            claude_v = json.loads(claude_manifest.read_text(encoding="utf-8"))["version"]
            if claude_v != want:
                mismatches.append(f"{p.name}/claude={claude_v}")

            codex_manifest = p / ".codex-plugin" / "plugin.json"
            codex_v = json.loads(codex_manifest.read_text(encoding="utf-8"))["version"]
            if codex_v != want:
                mismatches.append(f"{p.name}/codex={codex_v}")
        self.assertEqual(mismatches, [], f"CHANGELOG says v{want}; out of sync: {mismatches}")


class TestChangelogFormat(unittest.TestCase):
    def test_headings_well_formed_dated_unique_descending(self):
        text = CHANGELOG.read_text(encoding="utf-8")
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        self.assertTrue(headings, "CHANGELOG.md has no ## headings")

        versions = []
        for heading in headings:
            if heading.strip() == "## Unreleased":
                continue
            m = re.match(r"^## v(\d+\.\d+\.\d+) — \d{4}-\d{2}-\d{2}$", heading)
            self.assertIsNotNone(
                m,
                f"malformed CHANGELOG heading {heading!r}: expected '## vX.Y.Z — YYYY-MM-DD'",
            )
            versions.append(tuple(int(x) for x in m.group(1).split(".")))

        self.assertEqual(len(versions), len(set(versions)), "duplicate version headings")
        self.assertEqual(versions, sorted(versions, reverse=True), "version headings are not newest-first")


class TestReadmeCounts(unittest.TestCase):
    def _totals(self):
        plugins = plugin_dirs()
        return (
            sum(map(skill_count, plugins)),
            sum(map(command_count, plugins)),
            len(plugins),
        )

    def test_root_readme_headline_counts(self):
        skills, commands, plugins = self._totals()
        text = README.read_text(encoding="utf-8")
        m = re.search(r"(\d+) PM skills and (\d+) chained workflows across (\d+) plugins", text)
        self.assertIsNotNone(m, "headline count sentence not found in README.md")
        self.assertEqual(
            (int(m.group(1)), int(m.group(2)), int(m.group(3))),
            (skills, commands, plugins),
            "README.md headline counts don't match disk",
        )

    def test_marketplace_description_counts(self):
        skills, commands, plugins = self._totals()
        desc = marketplace()["description"]
        m = re.search(
            r"(\d+) domain-specific skills and (\d+) chained workflows across (\d+) PM plugins",
            desc,
        )
        self.assertIsNotNone(m, "count sentence not found in marketplace.json description")
        self.assertEqual(
            (int(m.group(1)), int(m.group(2)), int(m.group(3))),
            (skills, commands, plugins),
            "marketplace.json description counts don't match disk",
        )

    def test_plugin_readme_section_counts(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            m = re.search(r"^## Skills \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(int(m.group(1)), skill_count(p), f"{p.name} skill count")
            m = re.search(r"^## Commands \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(int(m.group(1)), command_count(p), f"{p.name} command count")


class TestMultiLlmOnboarding(unittest.TestCase):
    REQUIRED_SECTIONS = (
        "## Install and use",
        "### Claude Code / Cowork",
        "### Codex",
        "### ChatGPT",
        "### Other LLMs",
    )

    def test_every_plugin_readme_has_multi_llm_onboarding(self):
        failures = []
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                failures.append(f"{p.name}: README.md missing")
                continue
            text = readme.read_text(encoding="utf-8")
            for section in self.REQUIRED_SECTIONS:
                if section not in text:
                    failures.append(f"{p.name}: missing {section}")
            if "docs/USING_WITH_LLMS.md" not in text:
                failures.append(f"{p.name}: missing shared LLM usage guide link")
        self.assertEqual(failures, [], "\n".join(failures))

    def test_root_readme_documents_core_surfaces(self):
        text = README.read_text(encoding="utf-8")
        for phrase in (
            "Claude Cowork / Desktop",
            "Claude Code CLI",
            "Codex CLI / Codex app",
            "### ChatGPT",
            "Any other LLM",
            "docs/USING_WITH_LLMS.md",
        ):
            self.assertIn(phrase, text)


class TestCommandReferences(unittest.TestCase):
    def test_plugin_readme_command_refs_exist(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            for m in re.finditer(rf"/{re.escape(p.name)}:([\w-]+)", text):
                cmd = p / "commands" / f"{m.group(1)}.md"
                self.assertTrue(
                    cmd.is_file(),
                    f"{p.name}/README.md references /{p.name}:{m.group(1)} but commands/{m.group(1)}.md is missing",
                )


if __name__ == "__main__":
    unittest.main()
