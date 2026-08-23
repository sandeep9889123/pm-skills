---
name: ab-test-analysis
description: "Analyze A/B tests with setup validation, power/MDE checks, sample-ratio mismatch detection, confidence intervals, practical significance, guardrails, and calibrated ship/extend/stop recommendations. Use when evaluating experiment results, checking significance, interpreting split-test data, or deciding whether to ship a variant."
---

# A/B Test Analysis

Evaluate experiment results with statistical and product rigor.

> **A p-value is not a launch decision. A non-significant result is not proof of no effect.**

## Context

You are analyzing A/B test results for **$ARGUMENTS**.

If the user provides raw data or exports, calculate from those inputs where possible. If required fields are missing, state what cannot be validated rather than inventing assumptions silently.

## Step 1: Reconstruct the Experiment Contract

Before interpreting results, identify:

- hypothesis
- control and treatment
- randomization unit
- primary metric
- guardrail metrics
- expected baseline
- minimum detectable effect (MDE), if pre-specified
- target alpha
- target power
- planned sample size
- planned duration
- intended traffic split
- whether the test was stopped/extended based on interim results
- number of primary/secondary comparisons

If these were not defined before the experiment, label the analysis as partly **post hoc**.

## Step 2: Validate Experiment Integrity Before Outcome Significance

### A. Sample Ratio Mismatch (SRM)

Compare observed allocation against intended allocation.

If allocation is materially inconsistent with the planned split, investigate instrumentation/randomization before trusting treatment-effect estimates.

### B. Exposure and randomization

Check when possible:

- users were not exposed to both variants unintentionally
- assignment unit matches analysis unit
- bot/internal traffic is handled consistently
- logging differs neither by variant nor platform

### C. Duration and business cycles

Do not use a blanket “1-2 weeks” rule.

The test should cover relevant cycles for the product and avoid obvious event/holiday distortions unless those are part of normal usage.

### D. Peeking and optional stopping

If the team repeatedly checked a fixed-horizon p-value and stopped when it crossed 0.05, flag inflated false-positive risk.

Do not recommend simply “extend until significant.”

If sequential monitoring was planned, use the appropriate sequential method/boundaries rather than ordinary fixed-horizon interpretation.

### E. Novelty / learning effects

If behavior plausibly changes after users learn the variant, inspect performance over time rather than relying only on the aggregate.

## Step 3: Validate Power and Sample Size Correctly

### Important correction

A formula that uses only the alpha critical value cannot establish 80% power.

For a two-arm test of proportions with equal-sized groups, a common planning approximation is:

```text
n_per_arm ≈ [
  z_(1-alpha/2) * sqrt(2*p_bar*(1-p_bar))
  + z_(1-beta) * sqrt(p1*(1-p1) + p2*(1-p2))
]^2 / (p2 - p1)^2
```

where:

- `p1` = baseline conversion
- `p2` = baseline + target absolute effect
- `p_bar` = `(p1 + p2) / 2`
- `alpha` = false-positive rate
- `1-beta` = desired power
- `z_(1-beta)` is therefore required to claim a target power such as 80%

For means, ratios, clustered randomization, repeated measures, variance reduction, or non-standard metrics, use a method appropriate to the metric and design.

### Post-hoc “observed power”

Do not use post-hoc observed power as a substitute for confidence intervals or pre-test power planning. It is generally redundant with the observed p-value and can mislead interpretation.

Prefer:

- pre-test MDE/power planning
- confidence interval around the treatment effect
- whether the interval rules out effects that matter to the business

## Step 4: Calculate the Treatment Effect

For the primary metric, report as applicable:

- control value
- treatment value
- absolute difference
- relative lift
- confidence interval
- p-value / test statistic
- practical threshold or MDE

For proportions, a two-proportion z-test may be appropriate for large samples. Use exact or alternative methods when assumptions are not met.

Do not apply a statistical test merely because it is familiar.

## Step 5: Separate Statistical From Practical Significance

Ask two different questions:

### Statistical

Is the observed difference inconsistent with the null under the chosen design/test?

### Practical

Is the plausible effect large enough to matter to customers or the business?

A tiny effect can be statistically significant with a huge sample and still not justify launch complexity.

## Step 6: Inspect Guardrails and Segments

### Guardrails

Check material harms such as:

- revenue / margin
- retention
- latency/performance
- errors
- support burden
- cancellations
- trust/safety

A primary win does not automatically override a guardrail breach.

### Segments

Inspect segments when there is a pre-existing reason to expect heterogeneity, such as:

- platform
- geography
- new vs existing user
- enterprise vs self-serve
- traffic source

Do not data-mine dozens of segments and then present the most favorable one as causal proof.

If aggregate and important segment effects reverse, investigate possible Simpson's paradox / mix effects.

## Step 7: Handle Multiple Comparisons

If many primary-like metrics, variants, or repeated subgroup tests are being interpreted, surface inflated false-positive risk.

Use an appropriate correction or clearly distinguish:

- confirmatory metrics
- secondary/exploratory metrics

## Step 8: Calibrate the Decision

Do not use a simplistic rule that every p < 0.05 winner should ship.

Use this decision logic:

### SHIP / ROLL OUT

Only when:

- experiment integrity is acceptable
- primary result is supported by the planned analysis
- effect is practically meaningful or strategically justified
- guardrails are acceptable
- no hard-risk gate is breached

### LIMITED ROLLOUT / FOLLOW-UP

Use when:

- evidence is promising but important uncertainty remains
- effect varies by segment for plausible reasons
- operational risk warrants staged rollout

### CONTINUE / EXTEND ONLY WITH A VALID PLAN

Use when:

- the original plan allows more sample/time or a sequential method supports continuation
- additional data can meaningfully narrow the decision-relevant confidence interval

Do **not** extend only because the current result is not significant.

### STOP / NO EVIDENCE OF MEANINGFUL IMPROVEMENT

Use when the data are sufficiently informative to rule out effects worth pursuing or when economics/guardrails make continuation unattractive.

Do not translate `p >= alpha` into “the variants are the same.”

### INVALID / INVESTIGATE

Use when:

- SRM is unexplained
- randomization/exposure is broken
- instrumentation differs by variant
- stopping rule invalidates ordinary inference
- critical data quality issues exist

## Step 9: Contradiction Pass

Before finalizing, ask:

- Could a logging/randomization issue explain the result?
- Does the confidence interval include material harm or material upside?
- Am I calling “no effect” only because p >= 0.05?
- Am I calling “ship” only because p < 0.05?
- Did one important segment move in the opposite direction?
- Did a guardrail breach get hidden by the headline metric?
- Was the test stopped after peeking?
- Are multiple comparisons making the result look stronger than it is?

## Output

```markdown
## A/B Test Decision: [Test Name]

### Verdict
**Recommendation:** SHIP / LIMITED ROLLOUT / CONTINUE WITH VALID PLAN / STOP / INVALID-INVESTIGATE
**Confidence:** High / Medium / Low

### Experiment Contract
- Hypothesis:
- Randomization unit:
- Primary metric:
- Guardrails:
- Alpha:
- Target power:
- MDE:
- Planned sample / duration:
- Stopping rule:

### Integrity Checks
| Check | Status | Evidence / Concern |
|---|---|---|
| Sample ratio | Pass / Fail / Unknown | |
| Randomization | Pass / Fail / Unknown | |
| Exposure | Pass / Fail / Unknown | |
| Duration/cycles | Pass / Concern / Unknown | |
| Peeking/stopping | Pass / Concern / Unknown | |
| Data quality | Pass / Concern / Unknown | |

### Results
| Metric | Control | Treatment | Absolute diff | Relative lift | 95% CI | p-value | Practical threshold |
|---|---|---|---|---|---|---|---|

### Guardrails
[Material changes and hard gates]

### Segment / Sensitivity Checks
[Only decision-relevant checks]

### Interpretation
- What the data support
- What the data do not support
- Important unknowns

### What Would Change the Decision
[Specific additional evidence or threshold]

### Next Action
[Concrete action]
```

## Hard Failures

Do not:

- claim 80% power from a formula that omits `beta` / `z_(1-beta)`
- treat non-significance as proof of no difference
- recommend extending a fixed-horizon test simply to chase significance
- recommend shipping solely because p < 0.05
- ignore unexplained SRM
- hide guardrail harm behind a positive primary metric
- present exploratory subgroup wins as confirmatory without warning
- use post-hoc observed power as the primary interpretation tool

---

### Further Reading

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
