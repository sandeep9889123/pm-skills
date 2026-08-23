# PM Skills Behavioral Evaluation Harness

## Purpose

Structural validation proves that a skill is installable. Semantic guard tests prove that important instructions still exist. Neither proves that Claude, Codex, or another model will actually make a good PM decision when confronted with a difficult case.

This harness adds the next layer:

> **Golden scenario → model output → hard-gate check → 100-point decision-quality rubric → pass/fail → regression history**

The goal is not to claim that prompts can guarantee perfect PM judgment. The goal is to make failures observable, comparable, and harder to hide behind polished prose.

## Evaluation layers

### Layer A: deterministic hard gates

`score_output.py` checks explicit catastrophic behaviors that should fail regardless of the overall answer, for example:

- declaring “there are no competitors” after a weak/failed first search;
- converting a target metric into an achieved client result;
- claiming one client request proves market demand;
- calling originating-project code reusable IP without reuse evidence;
- manufacturing an ROI target when required economic inputs are missing;
- promoting one successful PoC directly into a platform investment;
- treating technical lift as proof of commercial demand;
- recommending autonomous automation with no rollback/approval boundary;
- calling a PoC production-ready while security/implementation blockers remain.

Hard gates are intentionally narrow. They should catch clear failures, not attempt to grade nuanced reasoning with regex alone.

### Layer B: 100-point behavioral rubric

Each case defines weighted decision-quality dimensions totaling 100 points. A human reviewer or independent evaluator model scores each dimension from 0–5 with rationale.

Typical dimensions:

- evidence integrity
- search/analysis sufficiency
- uncertainty calibration
- causal/analytical correctness
- decision usefulness
- trade-off quality
- edge-case handling
- enterprise execution realism
- actionability
- executive clarity

A case passes only when:

1. no hard gate fails; and
2. weighted score meets the case threshold, normally 90/100.

A score of 100/100 means the tested output earned full marks on that case. It does **not** mean the skill is infallible outside the tested distribution.

## Golden cases

`cases.json` includes 14 adversarial scenarios for:

1. competitor intelligence after a zero-result first pass;
2. one-client demand being mistaken for a future capability market;
3. bespoke delivery code being mistaken for reusable IP;
4. target metrics being turned into client success claims;
5. confidential delivery evidence being turned into public GTM collateral;
6. sales win-rate improvement caused by cherry-picking;
7. successful PoC with no production path;
8. automation whose human review burden erases ROI;
9. autonomous side effects with no rollback/permissions boundary;
10. vendor-demo happy-path bias in tool selection;
11. a business case treating weak competitor search as an uncontested market;
12. a business case manufacturing ROI with missing inputs;
13. a business case promoting one PoC directly into a platform investment;
14. a business case treating technical validation as commercial validation.

These cases directly exercise failure modes encoded in `reliability/scenario_matrix.json` and the dedicated business-case scenario catalog.

## Running an evaluation

Save a model response to a text/Markdown file, for example:

```bash
python evaluation/score_output.py \
  --case BC5_ROI_MISSING_INPUTS \
  --output evaluation/runs/claude/BC5.md
```

Without a judgement file, the command reports deterministic hard-gate status and leaves the nuanced score `UNSCORED`.

Create a judgement JSON using the case's dimension names:

```json
{
  "case_id": "BC5_ROI_MISSING_INPUTS",
  "evaluator": "independent-reviewer",
  "dimensions": {
    "evidence_integrity": {"score": 5, "rationale": "Refuses to invent missing ROI inputs."},
    "uncertainty_calibration": {"score": 5, "rationale": "Keeps ROI as unknown/estimate until inputs are established."}
  }
}
```

Then run:

```bash
python evaluation/score_output.py \
  --case BC5_ROI_MISSING_INPUTS \
  --output evaluation/runs/claude/BC5.md \
  --judgement evaluation/runs/claude/BC5.judgement.json
```

## Benchmark protocol

For a meaningful Claude vs Codex or before-vs-after comparison:

1. Freeze the case prompt/context.
2. Record model name/version/date and tool availability.
3. Start a fresh session so prior challenge/context does not help the model.
4. Run the skill/workflow once, without corrective follow-up.
5. Save the raw output unchanged.
6. Apply deterministic hard gates.
7. Blind the evaluator to model identity if possible.
8. Score all rubric dimensions with evidence/rationale.
9. Repeat stochastic cases at least 3 times when practical.
10. Report mean, range, hard-gate failure rate, and recurring failure modes.

The key metric for the original competitor problem and the business-case variants is **first-run success**, not whether the model can recover after the user tells it that it missed something.

## Quality policy

Do not tune a skill to literal test strings. Golden cases should represent failure families, and new real-world failures should create new or mutated cases.

A release should not be described as “100/100” unless the tested case suite actually scores 100 with zero hard-gate failures. Prefer reporting the exact benchmark scope and results.
