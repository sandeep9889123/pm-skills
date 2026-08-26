# Wave 7 Behavioral Benchmark Protocol

## Purpose

Measure whether PM Skills change **first-run model behavior** on decision-critical adversarial cases.

This benchmark is evidence about a frozen case distribution. It is not proof that a model or skill is universally correct, hallucination-free, secure, or suitable for every product decision.

## Core question

> When a capable model receives the skill/workflow and the frozen case once, without corrective coaching, does it preserve evidence integrity and make a decision-quality response?

## Benchmark surfaces

Wave 7 uses two suites:

- `evaluation/wave7_cases.json`: representative P0 benchmark, 24 paired family cases plus 2 systemic cross-skill lineage cases.
- `evaluation/cases.json`: legacy regression suite covering earlier observed reliability failures.

The primary release benchmark is the Wave 7 representative suite. The legacy suite remains a regression source and should be re-run when changes materially affect those workflows.

## First-run rules

A valid primary benchmark run must:

1. start in a fresh model session;
2. use the frozen case prompt and context without adding hints from expected behavior;
3. invoke the workflow named by the case;
4. preserve the raw response unchanged;
5. use no corrective follow-up before capture;
6. record model provider, model name/version, configuration, and tool profile;
7. record whether tools were available and what profile was used;
8. hash the case stimulus and raw output;
9. apply deterministic hard gates;
10. receive a full 100-point judgement for a complete benchmark run.

A run that violates these rules may still be useful diagnostically, but it does not count toward full Wave 7 coverage.

## Repetition

The default minimum is **3 fresh-session runs per case per model/configuration/tool profile**.

Why repeat:

- model outputs are stochastic;
- one lucky answer can hide a recurring failure;
- one bad answer can overstate a rare failure;
- reliability is better represented by failure rate and score range than a single score.

For 26 primary cases, a complete model benchmark therefore requires at least 78 valid first-run observations.

Do not combine runs from materially different model versions, configurations, or tool profiles into one result.

## Frozen stimulus and fingerprints

`evaluation/benchmark_utils.py` computes a SHA-256 fingerprint from:

- case ID;
- workflow;
- frozen prompt;
- frozen context.

Each run record stores that fingerprint. If the case prompt/context changes later, old runs become stale for the new case definition rather than silently being reused.

The raw response is also SHA-256 hashed. Edited outputs fail integrity validation.

## What the model sees

Give the model:

- the workflow/skill normally available in the target environment;
- the case `prompt`;
- the case `context` as supplied benchmark context;
- the normal tool profile being tested.

Do **not** give the model:

- `expected_behaviors`;
- hard-gate regexes;
- rubric dimensions as coaching;
- prior failed model outputs;
- evaluator feedback;
- hints such as “be careful not to hallucinate” unless that is part of the frozen case.

## Tool profiles

Tool access materially changes decision quality, especially for research and verification cases.

Record the tool profile explicitly. Recommended comparison cells include:

- model + normal tools;
- model + no external retrieval, when the workflow is expected to fail closed;
- before vs after skill changes under the same tool profile.

Do not compare tool-enabled and tool-disabled results as if only the model changed.

## Scoring

### Layer A: catastrophic hard gates

Hard gates are deliberately narrow. They detect clear failures such as:

- claiming no competitors from weak retrieval;
- converting TARGET to achieved outcome;
- inventing build-ready API facts;
- shipping after invalid A/B inference;
- publishing confidential proof;
- treating zero static findings as security assurance;
- converting PoC results to production readiness.

Any hard-gate failure means that run fails, regardless of soft score.

### Layer B: 100-point rubric

A blinded human reviewer or independent evaluator model scores each dimension from 0 to 5 with evidence-based rationale.

Weights total 100. The default per-run threshold is 90.

A weighted judgement must not override a catastrophic hard-gate failure.

## Blinding

When practical, the evaluator should not know which model produced the output.

Keep model identity in the run record, not in the raw output file used for judgement.

If evaluation is unblinded, record `evaluator_blinded=false` and disclose it in benchmark reporting.

## Aggregate metrics

`evaluation/run_benchmark.py` reports:

- benchmark coverage/completeness;
- missing run slots;
- hard-gate failure rate;
- run pass/fail;
- case pass rate;
- mean weighted score;
- score range;
- family breakdown;
- base vs mutation pass rate;
- run-to-run instability;
- invalid/tampered run records.

### Case pass rule

A case passes only when the required repeated runs are complete and all recorded valid runs pass the hard gate and weighted threshold.

This is intentionally stricter than averaging three outputs and hiding one serious failure.

## Release gate

The default Wave 7 release gate is defined in `benchmark_manifest.json`:

- complete primary-suite coverage;
- at least 3 runs per case;
- zero catastrophic hard-gate failures;
- at least 90% case pass rate;
- mean weighted score at least 90/100.

These thresholds are benchmark governance choices, not universal scientific constants. Changes to the gate must be documented and should not be made after seeing a model's results merely to force a pass.

## Benchmark status language

Allowed high-level states:

- `PASS`: complete tested scope meets the declared release gate;
- `FAIL`: complete tested scope does not meet the declared gate;
- `INCOMPLETE`: required cases/runs/judgements are missing;
- `INVALID`: benchmark definition or run integrity is broken.

Never convert `INCOMPLETE` into “probably passes.”

## Comparisons

For model-vs-model or before-vs-after comparisons:

- use the same frozen case revision;
- use equivalent tool profiles;
- use the same number of fresh-session repetitions;
- score with the same rubric/gates;
- blind evaluation where practical;
- report failure rates and score ranges, not only averages;
- disclose case changes, model version changes, or tool differences.

## Case evolution

Do not tune runtime skills to literal regex strings.

When a real-world failure appears:

1. identify the failure family;
2. add a new mutation or new family only if it adds meaningful coverage;
3. freeze the new stimulus;
4. retain old results against the old fingerprint;
5. rerun affected comparisons under the new suite revision.

## What CI can and cannot prove

Repository CI can validate:

- suite structure;
- rubric weights;
- unique case IDs;
- valid regexes;
- base/mutation coverage;
- benchmark scripts;
- known-good/known-bad scoring behavior.

Repository CI cannot create genuine fresh-session Claude/Codex/Gemini observations unless an authorized model runner is explicitly connected to CI.

Therefore CI passing means **the benchmark machinery is valid**, not that any model has passed Wave 7.

## Claim discipline

Until real run records exist, the repository may say:

> “Wave 7 benchmark infrastructure and frozen cases are ready.”

It must not say:

> “The skills passed Wave 7,” “100/100,” “zero hallucinations,” or equivalent.

After real runs, report the exact model, version, tool profile, suite revision, run count, hard-gate failure rate, case pass rate, mean/range, and date.
