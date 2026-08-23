---
name: pipeline-conversion-experiment
description: "Design measurable enterprise sales experiments to improve conversion, cycle time, deal quality, or expansion with cohorts, attribution limits, guardrails, and scale/stop criteria. Use when testing sales transformation interventions rather than rolling them out by opinion."
---

# Pipeline Conversion Experiment

## Purpose

Treat sales-process changes as experiments when uncertainty is material. The objective is to learn whether a specific intervention improves a defined constraint without degrading deal quality, customer trust, margin, or delivery readiness.

## Preconditions

State:
- diagnosed funnel constraint
- target cohort/segment
- baseline metric and measurement quality
- intervention mechanism
- primary decision metric
- guardrails
- contamination risks

If baseline data is unreliable, fix instrumentation before claiming uplift.

## Experiment design

1. **Hypothesis**
   `For [cohort], changing [specific behavior/process/asset] will improve [metric] from [baseline/range] to [target/range] because [mechanism].`

2. **Unit of analysis**
   Opportunity, account, rep, region, campaign, or time cohort. Avoid mixing levels.

3. **Comparison design**
   Prefer randomized/controlled assignment where practical. Otherwise use matched cohorts, stepped rollout, pre/post with seasonality controls, or qualitative triangulation. State causal limitations.

4. **Interventions**
   Examples: qualification gate, executive discovery, proof asset, demo format, pilot offer, pricing packaging, follow-up cadence, solution engineer involvement, account prioritization.

5. **Metrics**
   Primary: stage conversion, qualified pipeline, win rate, sales cycle, expansion, or another constraint metric.
   Guardrails: ASP, gross margin, churn risk, implementation failures, discounting, customer complaints, rep effort, pipeline quality.

6. **Stopping and scale rules**
   Define minimum evidence window, sample/case threshold, unacceptable downside, success condition, inconclusive outcome, and rollback.

7. **Attribution discipline**
   Track concurrent changes, rep effects, seasonality, segment mix, marketing source, product changes, and pricing changes.

## Edge cases

- apparent conversion gain caused by looser qualification;
- shorter cycle caused by smaller/easier deals;
- higher win rate caused by cherry-picking;
- pilot success with poor production conversion;
- rep adoption too low to evaluate intervention;
- multiple simultaneous changes make attribution impossible.

## Output

| Field | Definition |
|---|---|
| Constraint | |
| Hypothesis | |
| Cohort | |
| Intervention | |
| Baseline | |
| Primary metric | |
| Guardrails | |
| Attribution risks | |
| Scale criteria | |
| Stop criteria | |

### Decision after experiment
`SCALE | ITERATE | STOP | INCONCLUSIVE | FIX INSTRUMENTATION` with evidence and confidence.
