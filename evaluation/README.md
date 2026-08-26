# PM Skills Behavioral Evaluation

## Why this exists

Structural validation proves that a skill is installable. Semantic regression tests prove that important reliability instructions still exist. Neither proves that a model will actually make a good PM decision on the first attempt.

The behavioral layer is:

> **Frozen adversarial case → fresh-session model output → deterministic hard gates → 100-point judgement → repeated-run aggregation → failure-rate report**

The objective is to make model failures observable and comparable without claiming that prompts can guarantee perfect judgment.

## Evaluation assets

### Legacy regression suite

`cases.json` preserves the earlier 14-case behavioral suite for observed failures in competitor research, enterprise transformation, automation, PoC readiness, and business-case formation.

### Wave 7 representative P0 suite

`wave7_cases.json` is the primary representative benchmark:

- 24 cases covering 12 decision-critical PM families, each with at least one BASE and one MUTATION challenge;
- 2 additional systemic cross-skill lineage stress cases;
- 26 primary cases total.

Representative families:

1. market research;
2. product discovery;
3. product strategy;
4. business case;
5. analytics;
6. execution / PRD / meeting truth;
7. GTM / pricing / launch;
8. client proof;
9. automation and governance;
10. AI shipping / production readiness;
11. roadmap and prioritization;
12. legal/privacy.

The two systemic cases test claim inflation across handoffs rather than one plugin in isolation.

`MUTATION` means an additional adversarial challenge in the same family. Wave 7 v1 does not claim that every BASE/MUTATION relationship is a controlled metamorphic pair, so the two strata are reported descriptively and not as a causal robustness delta.

## Benchmark governance

`benchmark_manifest.json` freezes the benchmark rules:

- primary and regression suites;
- required families;
- minimum repeated runs;
- completeness rules;
- reporting obligations;
- release gate.

Default Wave 7 gate:

- complete primary-suite coverage;
- at least 3 fresh-session runs per case;
- zero catastrophic hard-gate failures;
- at least 90% case pass rate;
- mean weighted score at least 90/100.
- 100% case pass rate inside every required family;
- zero unstable cases.

These are benchmark governance thresholds, not universal scientific constants. Do not change them after seeing results merely to force a pass.

## Two scoring layers

### Layer A: deterministic catastrophic gates

`score_output.py` checks deliberately narrow forbidden/required behaviors, such as:

- declaring no competitors after weak retrieval;
- converting a TARGET into achieved impact;
- manufacturing ROI from missing inputs;
- inventing build-ready API behavior;
- shipping after invalid A/B inference;
- publishing confidential client evidence;
- treating executive priority as customer evidence;
- treating zero static findings as security/scalability assurance;
- converting PoC results into production readiness.

A hard-gate failure fails the run regardless of weighted score.

Every primary case includes at least two known-PASS and two known-FAIL hard-gate fixtures. CI executes all 104 fixture observations, including contradictory outputs that contain a safe keyword while still making a prohibited conclusion. Regex gates remain narrow tripwires, not semantic truth judges.

### Layer B: 100-point decision-quality rubric

An independent human reviewer or evaluator model scores each dimension from 0 to 5 with rationale and output evidence:

- evidence integrity: 15;
- analysis sufficiency: 10;
- uncertainty calibration: 10;
- analytical correctness: 10;
- decision usefulness: 15;
- trade-offs and alternatives: 10;
- edge-case handling: 10;
- enterprise execution realism: 10;
- actionability: 5;
- executive clarity: 5.

Weights total 100. Default per-run threshold is 90.

A 100/100 score means full marks on that frozen case. It does not imply universal reliability.

## Validate the benchmark definition

```bash
python evaluation/validate_benchmark.py
```

This validates suite structure, rubric weights, unique case IDs, regexes, base/mutation coverage, required families, systemic case references, and fingerprints.

CI can run this safely because it validates the benchmark definition, not live model behavior.

## Capture a real run

### 1. Run the frozen case

Use the case prompt/context in a **fresh model session** with the intended skill/workflow and tool profile.

Do not expose expected behaviors, hard-gate regexes, rubric hints, prior failed outputs, or corrective feedback to the model.

### 2. Save the raw first response unchanged

Example:

```text
evaluation/runs/openai-gpt-x/W7_MR_ZERO_RESULT_BASE/run-1.md
```

### 3. Create a weighted judgement

Use the case's full rubric dimensions and include rationale plus at least one output evidence reference for every score. The judgement must include:

- the case ID and rubric revision;
- the raw-output SHA-256 it evaluated;
- evaluator ID, type, version, independence, and blinding state;
- all rubric dimensions with score, rationale, and evidence.

See `judgement.schema.json` for the machine-readable contract.

### 4. Record the run with hashes

```bash
python evaluation/record_run.py \
  --case W7_MR_ZERO_RESULT_BASE \
  --output evaluation/runs/openai-gpt-x/W7_MR_ZERO_RESULT_BASE/run-1.md \
  --judgement evaluation/runs/openai-gpt-x/W7_MR_ZERO_RESULT_BASE/run-1.judgement.json \
  --provider OpenAI \
  --model GPT-X \
  --version 2026-08-26 \
  --configuration default \
  --run-index 1 \
  --planned-runs 3 \
  --fresh-session \
  --tools-enabled true \
  --tool-profile normal-tools \
  --evaluator-blinded true
```

The record stores:

- frozen-case SHA-256 fingerprint;
- full-suite and exact workflow-subject fingerprints;
- repository commit SHA;
- raw-output SHA-256;
- optional judgement SHA-256;
- exact model/version/configuration;
- tool profile;
- fresh-session flag;
- whether corrective follow-up or extra context was used.

Edited outputs, changed scoring rules, changed cases, or changed workflow files fail integrity validation.

## Score one output directly

The original single-case scorer remains useful:

```bash
python evaluation/score_output.py \
  --case BC5_ROI_MISSING_INPUTS \
  --output evaluation/runs/example/BC5.md \
  --judgement evaluation/runs/example/BC5.judgement.json
```

Use `--cases evaluation/wave7_cases.json` for Wave 7 case IDs.

Without a judgement, `score_output.py` can still report hard-gate status, but that observation is not a complete Wave 7 benchmark run.

## Aggregate repeated runs

```bash
python evaluation/run_benchmark.py \
  --runs evaluation/runs \
  --json-out evaluation/reports/latest.json \
  --md-out evaluation/reports/latest.md
```

The aggregate report includes:

- complete/incomplete benchmark coverage;
- invalid/tampered run records;
- missing run slots;
- hard-gate failure rate;
- case pass rate;
- mean/min/max weighted score;
- family performance;
- descriptive BASE vs MUTATION challenge pass rate;
- unstable cases with mixed outcomes or wide score ranges;
- per-case and per-run status, scores, ranges, hard failures, and missing slots;
- evaluator provenance, suite fingerprint, and repository commit;
- release status per exact model/configuration/tool profile/repository commit.

## Repetition and case-pass rule

The primary suite requires a predeclared three-slot run plan per case per model/configuration/tool profile. Only exact slots `1..N` satisfy coverage. Later indexes cannot substitute for missing planned slots.

A case passes only when:

- the minimum repeated runs exist;
- every valid recorded run passes deterministic hard gates;
- every required run has a valid weighted judgement;
- every recorded valid run meets its weighted threshold.

A catastrophic or scored failure cannot be hidden by averaging it with stronger runs.

For 26 cases, the default complete model cell requires **78 first-run observations**. Three runs are a qualification smoke threshold, not statistical proof of a low production failure rate. Higher-risk claims require a separately predeclared larger run plan.

## Comparison discipline

For model-vs-model or before-vs-after comparisons:

1. use the same case fingerprint/revision;
2. use equivalent tool profiles;
3. use the same number of fresh-session repetitions;
4. preserve raw outputs unchanged;
5. use the same hard gates and rubric;
6. blind evaluators where practical;
7. report failure rate and score range, not only mean score;
8. disclose model/version/tool/case changes.

Do not mix materially different model versions or tool profiles into one model result.

## Protocol

See [`BENCHMARK_PROTOCOL.md`](./BENCHMARK_PROTOCOL.md) for the full first-run protocol, blinding guidance, tool-profile rules, release gate, case evolution rules, and allowed benchmark claim language.

## What CI proves

CI can prove that:

- benchmark JSON is valid;
- required families and mutations exist;
- hard-gate regexes compile;
- known-bad fixtures fail;
- known-good fixtures survive catastrophic gates;
- case/output hash tampering is detected;
- fresh-session/corrective-follow-up rules are enforced;
- aggregate PASS/FAIL/INCOMPLETE logic behaves as designed.

CI **cannot** create genuine fresh-session Claude, Codex, Gemini, or other model evidence unless an authorized model runner is explicitly connected.

Therefore a green repository test suite means:

> **Wave 7 benchmark machinery is valid.**

It does not mean:

> **The models or PM Skills passed Wave 7.**

## Claim policy

Before real complete runs exist, use wording such as:

> “Wave 7 benchmark infrastructure and frozen cases are ready for execution.”

Do not claim:

- “100/100”;
- “zero hallucinations”;
- “all models pass”;
- “production-proven reliability”;
- universal correctness.

After real runs, report exact model/version/configuration/tool profile, suite revision/fingerprint, number of runs, date, hard-gate failure rate, case pass rate, mean/range, and known failure families.
