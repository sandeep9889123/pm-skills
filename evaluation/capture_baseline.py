#!/usr/bin/env python3
"""Capture predeclared fresh-session Wave 7 outputs from supported model APIs.

The runner sends only the mapped workflow files plus the frozen case prompt and
context. It writes the exact request, full provider response, raw text output,
and a run record before moving to the next slot. It never retries or supplies a
corrective follow-up after a provider has returned a response.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlsplit

try:  # direct: python evaluation/capture_baseline.py
    from benchmark_utils import get_case, load_json, suite_fingerprint
except ModuleNotFoundError:  # imported from repository-root tests/tools
    from evaluation.benchmark_utils import get_case, load_json, suite_fingerprint

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
DEFAULT_MANIFEST = EVAL_DIR / "benchmark_manifest.json"

ADAPTERS = {
    "openai-responses": {
        "provider": "OpenAI",
        "endpoint": "https://api.openai.com/v1/responses",
        "api_key_env": "OPENAI_API_KEY",
    },
    "anthropic-messages": {
        "provider": "Anthropic",
        "endpoint": "https://api.anthropic.com/v1/messages",
        "api_key_env": "ANTHROPIC_API_KEY",
    },
}


class CaptureError(RuntimeError):
    """Raised when a run cannot be captured without weakening the protocol."""


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Never forward benchmark credentials across an HTTP redirect."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise CaptureError(f"capture artifacts must live inside the repository: {path}") from exc


def slug(value: str) -> str:
    result = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-")
    return result or "capture"


def repository_commit() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise CaptureError(f"cannot resolve repository commit: {exc}") from exc


def validate_endpoint(value: str) -> str:
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise CaptureError("model endpoint must be an absolute https URL")
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise CaptureError("model endpoint cannot contain credentials, query parameters, or fragments")
    return value


def build_prompt_bundle(
    case: dict[str, Any], subject_paths: list[str]
) -> dict[str, Any]:
    subjects = []
    rendered_subjects = []
    for value in subject_paths:
        path = (REPO_ROOT / value).resolve()
        try:
            path.relative_to(REPO_ROOT.resolve())
        except ValueError as exc:
            raise CaptureError(f"workflow subject escapes repository: {value}") from exc
        if not path.is_file():
            raise CaptureError(f"workflow subject is missing: {value}")
        content = path.read_text(encoding="utf-8")
        subjects.append(
            {
                "path": value,
                "sha256": sha256_bytes(content.encode("utf-8")),
                "content": content,
            }
        )
        rendered_subjects.append(f"--- BEGIN {value} ---\n{content}\n--- END {value} ---")

    system = (
        "Execute the workflow identified below. Treat the supplied workflow material "
        "as the governing instructions for this response.\n\n"
        f"Workflow: {case['workflow']}\n\n"
        + "\n\n".join(rendered_subjects)
    )
    user = (
        f"Task:\n{case['prompt']}\n\n"
        f"Context supplied for this task:\n{case['context']}"
    )
    return {
        "schema_version": "1.0",
        "case_id": case["id"],
        "workflow": case["workflow"],
        "subjects": subjects,
        "model_visible": {"system": system, "user": user},
    }


def request_parameters(
    adapter: str,
    model: str,
    max_output_tokens: int,
    temperature: float | None,
    reasoning_effort: str | None,
) -> dict[str, Any]:
    parameters: dict[str, Any] = {
        "adapter": adapter,
        "model": model,
        "max_output_tokens": max_output_tokens,
        "temperature": temperature,
        "reasoning_effort": reasoning_effort,
        "tools": [],
    }
    return parameters


def build_request(
    adapter: str,
    model: str,
    prompt_bundle: dict[str, Any],
    max_output_tokens: int,
    temperature: float | None = None,
    reasoning_effort: str | None = None,
) -> dict[str, Any]:
    visible = prompt_bundle["model_visible"]
    if adapter == "openai-responses":
        body: dict[str, Any] = {
            "model": model,
            "instructions": visible["system"],
            "input": visible["user"],
            "max_output_tokens": max_output_tokens,
            "store": False,
        }
        if temperature is not None:
            body["temperature"] = temperature
        if reasoning_effort is not None:
            body["reasoning"] = {"effort": reasoning_effort}
        return body
    if adapter == "anthropic-messages":
        if reasoning_effort is not None:
            raise CaptureError("--reasoning-effort is only supported by openai-responses")
        body = {
            "model": model,
            "system": visible["system"],
            "messages": [{"role": "user", "content": visible["user"]}],
            "max_tokens": max_output_tokens,
        }
        if temperature is not None:
            body["temperature"] = temperature
        return body
    raise CaptureError(f"unsupported adapter: {adapter}")


def request_headers(adapter: str, api_key: str) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if adapter == "openai-responses":
        headers["Authorization"] = f"Bearer {api_key}"
    elif adapter == "anthropic-messages":
        headers["x-api-key"] = api_key
        headers["anthropic-version"] = "2023-06-01"
    else:
        raise CaptureError(f"unsupported adapter: {adapter}")
    return headers


def call_json(
    endpoint: str,
    headers: dict[str, str],
    body: dict[str, Any],
    timeout_seconds: int,
) -> dict[str, Any]:
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        opener = urllib.request.build_opener(NoRedirectHandler)
        with opener.open(request, timeout=timeout_seconds) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read(4096).decode("utf-8", errors="replace")
        raise CaptureError(f"provider HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise CaptureError(f"provider request failed without retry: {exc}") from exc
    if not isinstance(payload, dict):
        raise CaptureError("provider returned a non-object JSON response")
    return payload


def extract_response(adapter: str, payload: dict[str, Any]) -> tuple[str, str, str]:
    request_id = payload.get("id")
    response_model = payload.get("model")
    if not isinstance(request_id, str) or not request_id:
        raise CaptureError("provider response is missing id")
    if not isinstance(response_model, str) or not response_model:
        raise CaptureError("provider response is missing model")

    chunks: list[str] = []
    if adapter == "openai-responses":
        for item in payload.get("output", []):
            if isinstance(item, dict) and item.get("type") == "message":
                for block in item.get("content", []):
                    if isinstance(block, dict) and block.get("type") == "output_text":
                        text = block.get("text")
                        if isinstance(text, str) and text:
                            chunks.append(text)
                    elif isinstance(block, dict) and block.get("type") == "refusal":
                        refusal = block.get("refusal")
                        if isinstance(refusal, str) and refusal:
                            chunks.append(refusal)
    elif adapter == "anthropic-messages":
        for block in payload.get("content", []):
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text")
                if isinstance(text, str) and text:
                    chunks.append(text)
    else:
        raise CaptureError(f"unsupported adapter: {adapter}")

    # The complete provider response preserves block boundaries. The raw text
    # file concatenates text fields without trimming or adding model-authored
    # characters. Empty assistant text remains an observed hard-gate failure.
    return "".join(chunks), request_id, response_model


def plan_identity(plan: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in plan.items() if key != "created_at"}


def prepare_plan(path: Path, plan: dict[str, Any], resume: bool) -> None:
    if path.exists():
        observed = load_json(path)
        if plan_identity(observed) != plan_identity(plan):
            raise CaptureError("existing run plan differs; use a new output cell")
        if not resume:
            raise CaptureError("run plan already exists; use --resume to continue exact missing slots")
        return
    write_json(path, plan)


def record_capture(
    *,
    case: dict[str, Any],
    run_index: int,
    planned_runs: int,
    adapter: str,
    endpoint: str,
    model: str,
    parameters: dict[str, Any],
    prompt_bundle: dict[str, Any],
    request_body: dict[str, Any],
    provider_response: dict[str, Any],
    output: str,
    request_id: str,
    response_model: str,
    case_dir: Path,
) -> Path:
    stem = f"run-{run_index}"
    prompt_path = case_dir / f"{stem}.prompt.json"
    request_path = case_dir / f"{stem}.request.json"
    response_path = case_dir / f"{stem}.provider.json"
    output_path = case_dir / f"{stem}.md"
    record_path = case_dir / f"{stem}.run.json"
    for path in (prompt_path, request_path, response_path, output_path, record_path):
        if path.exists():
            raise CaptureError(f"refusing to overwrite pre-existing slot artifact: {path}")

    write_json(prompt_path, prompt_bundle)
    write_json(request_path, request_body)
    write_json(response_path, provider_response)
    output_path.write_text(output, encoding="utf-8")

    configuration = canonical_json(
        {
            "adapter": adapter,
            "max_output_tokens": parameters["max_output_tokens"],
            "temperature": parameters["temperature"],
            "reasoning_effort": parameters["reasoning_effort"],
            "tools": [],
        }
    )
    command = [
        sys.executable,
        str(EVAL_DIR / "record_run.py"),
        "--case",
        case["id"],
        "--output",
        str(output_path),
        "--provider",
        ADAPTERS[adapter]["provider"],
        "--model",
        model,
        "--version",
        response_model,
        "--configuration",
        configuration,
        "--run-index",
        str(run_index),
        "--planned-runs",
        str(planned_runs),
        "--fresh-session",
        "--tools-enabled",
        "false",
        "--tool-profile",
        "no-external-tools-api",
        "--tool-notes",
        "Fresh stateless API request; no provider or client tools supplied.",
        "--workflow-invoked",
        case["workflow"],
        "--record",
        str(record_path),
        "--notes",
        "Automated API capture; weighted judgement pending.",
    ]
    completed = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
    if completed.returncode != 0:
        raise CaptureError(f"record_run.py rejected captured slot: {completed.stderr}{completed.stdout}")

    record = load_json(record_path)
    record["capture"] = {
        "mode": "automated_api",
        "adapter": adapter,
        "endpoint": endpoint,
        "prompt_bundle_path": repo_relative(prompt_path),
        "prompt_bundle_sha256": sha256_file(prompt_path),
        "request_path": repo_relative(request_path),
        "request_sha256": sha256_file(request_path),
        "provider_response_path": repo_relative(response_path),
        "provider_response_sha256": sha256_file(response_path),
        "provider_request_id": request_id,
        "response_model": response_model,
        "request_parameters": parameters,
    }
    write_json(record_path, record)
    return record_path


def run_capture(
    args: argparse.Namespace,
    transport: Callable[[str, dict[str, str], dict[str, Any], int], dict[str, Any]] = call_json,
) -> Path:
    manifest = load_json(args.manifest)
    suite = load_json(REPO_ROOT / manifest["primary_suite"])
    all_case_ids = [case["id"] for case in suite["cases"]]
    if args.case_ids == "all":
        if not args.allow_all:
            raise CaptureError("full-suite capture requires --allow-all")
        case_ids = all_case_ids
    else:
        requested = [value.strip() for value in args.case_ids.split(",") if value.strip()]
        if not requested or len(requested) != len(set(requested)):
            raise CaptureError("--case-ids must contain unique comma-separated case IDs")
        unknown = sorted(set(requested) - set(all_case_ids))
        if unknown:
            raise CaptureError(f"unknown case IDs: {unknown}")
        case_ids = [value for value in all_case_ids if value in set(requested)]

    minimum_runs = int(manifest["minimum_runs_per_case"])
    if args.planned_runs < minimum_runs:
        raise CaptureError(f"--planned-runs must be at least {minimum_runs}")
    endpoint = validate_endpoint(args.endpoint or ADAPTERS[args.adapter]["endpoint"])
    parameters = request_parameters(
        args.adapter,
        args.model,
        args.max_output_tokens,
        args.temperature,
        args.reasoning_effort,
    )
    configuration_digest = sha256_bytes(canonical_json(parameters).encode("utf-8"))[:12]
    cell_name = slug(f"{ADAPTERS[args.adapter]['provider']}-{args.model}-{configuration_digest}")
    cell_dir = args.output_root / cell_name
    repo_relative(cell_dir)

    plan = {
        "schema_version": "1.0",
        "benchmark_id": manifest["benchmark_id"],
        "suite_fingerprint": suite_fingerprint(suite),
        "repository_commit": repository_commit(),
        "adapter": args.adapter,
        "provider": ADAPTERS[args.adapter]["provider"],
        "endpoint": endpoint,
        "parameters": parameters,
        "case_ids": case_ids,
        "planned_runs": args.planned_runs,
        "execution_order": "run-index-then-suite-order",
        "retry_policy": "no automatic retries",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    plan_path = cell_dir / "run-plan.json"
    prepare_plan(plan_path, plan, args.resume)

    if args.dry_run:
        for case_id in case_ids:
            case = get_case(suite, case_id)
            bundle = build_prompt_bundle(
                case, manifest["workflow_subjects"][case["workflow"]]
            )
            write_json(cell_dir / case_id / "dry-run.prompt.json", bundle)
        return cell_dir

    key_env = args.api_key_env or ADAPTERS[args.adapter]["api_key_env"]
    api_key = os.environ.get(key_env, "").strip()
    if not api_key:
        raise CaptureError(f"required API credential is not set: {key_env}")
    headers = request_headers(args.adapter, api_key)

    for run_index in range(1, args.planned_runs + 1):
        for case_id in case_ids:
            case = get_case(suite, case_id)
            case_dir = cell_dir / case_id
            record_path = case_dir / f"run-{run_index}.run.json"
            stem = f"run-{run_index}"
            slot_paths = [
                case_dir / f"{stem}.prompt.json",
                case_dir / f"{stem}.request.json",
                case_dir / f"{stem}.provider.json",
                case_dir / f"{stem}.md",
                record_path,
            ]
            existing = [path for path in slot_paths if path.exists()]
            if existing:
                if args.resume and len(existing) == len(slot_paths):
                    print(f"Skipping existing slot {case_id}:run-{run_index}")
                    continue
                raise CaptureError(
                    f"partial or unapproved slot exists for {case_id}:run-{run_index}; "
                    "use a new output cell rather than overwriting evidence"
                )
            prompt_bundle = build_prompt_bundle(
                case, manifest["workflow_subjects"][case["workflow"]]
            )
            request_body = build_request(
                args.adapter,
                args.model,
                prompt_bundle,
                args.max_output_tokens,
                args.temperature,
                args.reasoning_effort,
            )
            print(f"Capturing {case_id}:run-{run_index}", flush=True)
            provider_response = transport(
                endpoint, headers, request_body, args.timeout_seconds
            )
            output, request_id, response_model = extract_response(
                args.adapter, provider_response
            )
            record_capture(
                case=case,
                run_index=run_index,
                planned_runs=args.planned_runs,
                adapter=args.adapter,
                endpoint=endpoint,
                model=args.model,
                parameters=parameters,
                prompt_bundle=prompt_bundle,
                request_body=request_body,
                provider_response=provider_response,
                output=output,
                request_id=request_id,
                response_model=response_model,
                case_dir=case_dir,
            )
    return cell_dir


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adapter", choices=sorted(ADAPTERS), required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--endpoint")
    parser.add_argument("--api-key-env")
    parser.add_argument("--case-ids", required=True, help="Comma-separated IDs or 'all'")
    parser.add_argument("--allow-all", action="store_true")
    parser.add_argument("--planned-runs", type=int, default=3)
    parser.add_argument("--max-output-tokens", type=int, default=5000)
    parser.add_argument("--temperature", type=float)
    parser.add_argument("--reasoning-effort", choices=["none", "minimal", "low", "medium", "high", "xhigh"])
    parser.add_argument("--timeout-seconds", type=int, default=300)
    parser.add_argument("--output-root", type=Path, default=EVAL_DIR / "runs")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.max_output_tokens < 1:
        parser.error("--max-output-tokens must be positive")
    if args.timeout_seconds < 1:
        parser.error("--timeout-seconds must be positive")
    return args


def main() -> int:
    try:
        destination = run_capture(parse_args())
    except CaptureError as exc:
        print(f"CAPTURE FAILED: {exc}", file=sys.stderr)
        return 2
    print(f"Capture artifacts: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
