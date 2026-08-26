#!/usr/bin/env python3
"""Shared utilities for the PM Skills behavioral benchmark.

Standard-library only. These functions validate benchmark definitions and create
stable case fingerprints. They do not call or grade an LLM by themselves.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


class BenchmarkDefinitionError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BenchmarkDefinitionError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise BenchmarkDefinitionError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise BenchmarkDefinitionError(f"expected JSON object: {path}")
    return data


def canonical_case_stimulus(case: dict[str, Any]) -> dict[str, Any]:
    """Return only the frozen model-visible stimulus and routing identity."""
    return {
        "id": case.get("id"),
        "workflow": case.get("workflow"),
        "prompt": case.get("prompt"),
        "context": case.get("context"),
    }


def case_fingerprint(case: dict[str, Any]) -> str:
    """Bind a run to the complete case definition, not only its prompt."""
    payload = json.dumps(
        case,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def suite_fingerprint(suite: dict[str, Any]) -> str:
    """Bind a run to the rubric and every case in the frozen suite."""
    payload = json.dumps(
        suite,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def subject_fingerprint(repo_root: Path, paths: list[str]) -> str:
    """Hash the exact workflow files supplied for a benchmark observation."""
    digest = hashlib.sha256()
    for value in sorted(paths):
        path = (repo_root / value).resolve()
        try:
            path.relative_to(repo_root.resolve())
        except ValueError as exc:
            raise BenchmarkDefinitionError(f"subject path escapes repository: {value}") from exc
        if not path.is_file():
            raise BenchmarkDefinitionError(f"subject path does not exist: {value}")
        digest.update(value.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def get_case(suite: dict[str, Any], case_id: str) -> dict[str, Any]:
    for case in suite.get("cases", []):
        if isinstance(case, dict) and case.get("id") == case_id:
            return case
    raise KeyError(f"unknown case_id: {case_id}")


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_regexes(patterns: Any, where: str, errors: list[str]) -> None:
    if not isinstance(patterns, list):
        errors.append(f"{where}: must be an array")
        return
    for index, pattern in enumerate(patterns):
        if not _nonempty_string(pattern):
            errors.append(f"{where}[{index}]: must be a non-empty string")
            continue
        try:
            re.compile(pattern)
        except re.error as exc:
            errors.append(f"{where}[{index}]: invalid regex: {exc}")


def validate_suite(
    suite: dict[str, Any],
    *,
    required_families: list[str] | None = None,
    require_variants: bool = False,
    require_fixtures: bool = False,
    minimum_cases: int = 1,
) -> list[str]:
    errors: list[str] = []

    rubric = suite.get("rubric")
    if not isinstance(rubric, dict) or not rubric:
        errors.append("suite.rubric: non-empty object required")
    else:
        total = 0
        for name, spec in rubric.items():
            if not isinstance(spec, dict):
                errors.append(f"suite.rubric.{name}: must be an object")
                continue
            weight = spec.get("weight")
            if not isinstance(weight, (int, float)) or weight <= 0:
                errors.append(f"suite.rubric.{name}.weight: positive number required")
            else:
                total += weight
            if not _nonempty_string(spec.get("description")):
                errors.append(f"suite.rubric.{name}.description: required")
        if total != 100:
            errors.append(f"suite.rubric: weights total {total}, expected 100")

    threshold = suite.get("default_pass_threshold")
    if not isinstance(threshold, (int, float)) or not 0 <= threshold <= 100:
        errors.append("suite.default_pass_threshold: must be 0..100")

    cases = suite.get("cases")
    if not isinstance(cases, list):
        errors.append("suite.cases: array required")
        return errors
    if len(cases) < minimum_cases:
        errors.append(f"suite.cases: expected at least {minimum_cases}, found {len(cases)}")

    ids: set[str] = set()
    by_id: dict[str, dict[str, Any]] = {}
    family_variants: dict[str, set[str]] = {}

    for index, case in enumerate(cases):
        where = f"suite.cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{where}: must be an object")
            continue

        case_id = case.get("id")
        if not _nonempty_string(case_id):
            errors.append(f"{where}.id: required")
            continue
        if case_id in ids:
            errors.append(f"{where}.id: duplicate {case_id!r}")
        ids.add(case_id)
        by_id[case_id] = case

        for field in ("workflow", "failure_family", "prompt", "context"):
            if not _nonempty_string(case.get(field)):
                errors.append(f"{where}.{field}: non-empty string required")

        expected = case.get("expected_behaviors")
        if not isinstance(expected, list) or len(expected) < 3:
            errors.append(f"{where}.expected_behaviors: at least 3 behaviors required")
        elif not all(_nonempty_string(item) for item in expected):
            errors.append(f"{where}.expected_behaviors: all entries must be non-empty strings")

        hard = case.get("hard_gates")
        if not isinstance(hard, dict):
            errors.append(f"{where}.hard_gates: object required")
        else:
            _validate_regexes(hard.get("required_patterns", []), f"{where}.hard_gates.required_patterns", errors)
            _validate_regexes(hard.get("forbidden_patterns", []), f"{where}.hard_gates.forbidden_patterns", errors)
            if not hard.get("required_patterns") and not hard.get("forbidden_patterns"):
                errors.append(f"{where}.hard_gates: at least one deterministic gate required")

        fixtures = case.get("hard_gate_fixtures")
        if require_fixtures and not isinstance(fixtures, dict):
            errors.append(f"{where}.hard_gate_fixtures: object required")
        elif isinstance(fixtures, dict):
            for outcome in ("pass", "fail"):
                samples = fixtures.get(outcome)
                if not isinstance(samples, list) or len(samples) < 2:
                    errors.append(
                        f"{where}.hard_gate_fixtures.{outcome}: at least 2 strings required"
                    )
                elif not all(_nonempty_string(item) for item in samples):
                    errors.append(
                        f"{where}.hard_gate_fixtures.{outcome}: all entries must be non-empty strings"
                    )

        case_threshold = case.get("pass_threshold")
        if case_threshold is not None and (
            not isinstance(case_threshold, (int, float)) or not 0 <= case_threshold <= 100
        ):
            errors.append(f"{where}.pass_threshold: must be 0..100")

        family = case.get("family")
        variant = case.get("variant")
        if require_variants:
            if not _nonempty_string(family):
                errors.append(f"{where}.family: required in representative suite")
            if variant not in {"BASE", "MUTATION"}:
                errors.append(f"{where}.variant: must be BASE or MUTATION")
            if _nonempty_string(family) and variant in {"BASE", "MUTATION"}:
                family_variants.setdefault(family, set()).add(variant)

            parent = case.get("parent_case_id")
            if variant == "BASE" and parent is not None:
                errors.append(f"{where}.parent_case_id: BASE must be null")
            if variant == "MUTATION" and not _nonempty_string(parent):
                errors.append(f"{where}.parent_case_id: MUTATION requires parent case")

    if require_variants:
        for case_id, case in by_id.items():
            if case.get("variant") != "MUTATION":
                continue
            parent_id = case.get("parent_case_id")
            parent = by_id.get(parent_id)
            if not parent:
                errors.append(f"case {case_id}: parent_case_id {parent_id!r} not found")
                continue
            if parent.get("variant") != "BASE":
                errors.append(f"case {case_id}: parent must be BASE")
            if parent.get("family") != case.get("family"):
                errors.append(f"case {case_id}: parent must be in same family")

    if required_families:
        families = set(family_variants)
        missing = set(required_families) - families
        if missing:
            errors.append(f"suite: missing required families {sorted(missing)}")
        for family in required_families:
            variants = family_variants.get(family, set())
            if not {"BASE", "MUTATION"}.issubset(variants):
                errors.append(f"suite family {family!r}: requires BASE and MUTATION")

    return errors


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("benchmark_id", "primary_suite", "minimum_runs_per_case", "required_families"):
        if key not in manifest:
            errors.append(f"manifest: missing {key}")

    if not _nonempty_string(manifest.get("benchmark_id")):
        errors.append("manifest.benchmark_id: required")
    if not _nonempty_string(manifest.get("primary_suite")):
        errors.append("manifest.primary_suite: required")
    minimum = manifest.get("minimum_runs_per_case")
    if not isinstance(minimum, int) or minimum < 1:
        errors.append("manifest.minimum_runs_per_case: integer >= 1 required")
    families = manifest.get("required_families")
    if not isinstance(families, list) or not families or not all(_nonempty_string(x) for x in families):
        errors.append("manifest.required_families: non-empty string array required")

    subjects = manifest.get("workflow_subjects")
    if not isinstance(subjects, dict) or not subjects:
        errors.append("manifest.workflow_subjects: non-empty object required")
    else:
        for workflow, paths in subjects.items():
            if not _nonempty_string(workflow):
                errors.append("manifest.workflow_subjects: workflow keys must be non-empty")
            if not isinstance(paths, list) or not paths or not all(_nonempty_string(x) for x in paths):
                errors.append(
                    f"manifest.workflow_subjects.{workflow}: non-empty string array required"
                )

    gate = manifest.get("release_gate", {})
    if not isinstance(gate, dict):
        errors.append("manifest.release_gate: object required")
    else:
        hard = gate.get("maximum_hard_gate_failure_rate")
        pass_rate = gate.get("minimum_case_pass_rate")
        mean = gate.get("minimum_mean_weighted_score")
        family = gate.get("minimum_family_pass_rate")
        unstable = gate.get("maximum_unstable_cases")
        if not isinstance(hard, (int, float)) or not 0 <= hard <= 1:
            errors.append("manifest.release_gate.maximum_hard_gate_failure_rate: 0..1 required")
        if not isinstance(pass_rate, (int, float)) or not 0 <= pass_rate <= 1:
            errors.append("manifest.release_gate.minimum_case_pass_rate: 0..1 required")
        if not isinstance(mean, (int, float)) or not 0 <= mean <= 100:
            errors.append("manifest.release_gate.minimum_mean_weighted_score: 0..100 required")
        if not isinstance(family, (int, float)) or not 0 <= family <= 1:
            errors.append("manifest.release_gate.minimum_family_pass_rate: 0..1 required")
        if not isinstance(unstable, int) or unstable < 0:
            errors.append("manifest.release_gate.maximum_unstable_cases: integer >= 0 required")

    mutation_policy = manifest.get("mutation_policy")
    if mutation_policy not in {"controlled_pairs", "unpaired_family_challenges"}:
        errors.append(
            "manifest.mutation_policy: controlled_pairs or unpaired_family_challenges required"
        )

    return errors
