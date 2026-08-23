---
name: brainstorm-experiments-existing
description: "Design falsifiable experiments for existing products using real baselines, causal mechanisms, decision thresholds, guardrails, and rollout/rollback criteria. Use when validating assumptions or product changes before full implementation."
---

## Design Experiments for an Existing Product

## Purpose

Resolve a specific product uncertainty while protecting current users and business outcomes. Do not recommend an A/B test merely because production traffic exists.

## Step 1: Define decision and mechanism

State:
- proposed change
- user/business problem evidence
- assumption/mechanism
- decision the result will inform
- current baseline and data quality
- affected segments
- downside risk

## Step 2: Choose the smallest credible method

Consider:
- existing-data analysis
- usability/prototype test
- fake door / feature stub
- concierge/Wizard of Oz
- technical spike
- phased rollout
- shadow mode
- randomized A/B test
- switchback/time-based test when appropriate

Choose based on causal question, traffic/sample reality, user risk, implementation cost, and reversibility.

## Step 3: Experiment contract

For each experiment include:
- hypothesis
- unit of randomization/analysis if applicable
- cohort/eligibility
- primary metric
- guardrails
- baseline and MDE/practical threshold where relevant
- sample/evidence logic
- duration/business cycles
- contamination risks
- success/failure/inconclusive rules
- rollback/stop condition

## Reliability / Edge Cases

- Do not test a solution when the underlying problem is unvalidated.
- Do not recommend an A/B test when traffic cannot support meaningful inference.
- Check sample-ratio mismatch, novelty, seasonality, repeated peeking/optional stopping, multiple metrics, and segment reversal when statistical tests are used.
- Distinguish statistical significance from practical/business significance.
- Do not ignore users harmed by a “winning” average.
- For high-risk AI behavior, use frozen evaluation sets, shadow mode, human review, and hard safety/quality gates before broad experiments.
- For enterprise workflows, account-level contamination and long sales/implementation cycles may make standard user-level A/B testing inappropriate.
- If deployment cost exceeds the value of learning, use a cheaper prototype/data test first.
- If multiple product changes ship simultaneously, state attribution limitations.

## Output

| Assumption | Method | Why this method | Metric | Guardrail | Success/Failure | Risk | Next decision |
|---|---|---|---|---|---|---|---|

Recommend the **single best next experiment** based on information value / effort / risk.

### Decision outcomes
`SHIP | EXPAND | ITERATE | STOP | ROLLBACK | INCONCLUSIVE`.

---

### Further Reading

- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
