---
name: ab-test-analysis
description: "Analyze A/B tests with setup validation, power/MDE checks, sample-ratio mismatch detection, confidence intervals, practical significance, guardrails, calibrated decisions, and claim-lineage preservation for downstream prioritization/launch."
---

# A/B Test Analysis

Evaluate experiment results with statistical and product rigor.

> **A p-value is not a launch decision. A non-significant result is not proof of no effect.**

## Context

You are analyzing A/B test results for **$ARGUMENTS**.

If the user provides raw data or exports, calculate from those inputs where possible. If required fields are missing, state what cannot be validated rather than inventing assumptions silently.

## Claim-Lineage Producer Contract

For every decision-relevant experiment claim:

- assign a stable `claim_id`;
- preserve experiment population, period, randomization unit, metric definition, variant, and analysis method;
- distinguish the measured treatment-effect result from the product/causal interpretation;
- preserve validity caveats: SRM, exposure/randomization, peeking/stopping, multiple comparisons, data quality, maturity, and guardrail status;
- preserve confidence intervals and practical-significance context where material;
- an experiment decision such as `SHIP` is a decision, not promotion of every analytical claim to universal `FACT`;
- downstream prioritization/launch may restate measured claims only at the tested scope;
- new cross-segment, long-term, production, or causal conclusions require new claim IDs linked to the experiment claims.

Example:
- `AB-021 FACT`: treatment increased conversion by 1.2pp in the tested population/period, CI [...], assuming experiment integrity checks pass.
- `AB-022 INFERENCE`, parent `[AB-021]`: the change may improve paid conversion in a broader rollout.
- Not allowed: reuse `AB-021` as “the feature improves conversion by 1.2pp for all users.”

## Step 1: Reconstruct the Experiment Contract

Identify:
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
- stopping/extension behavior
- number of primary/secondary comparisons

If these were not defined before the experiment, label the analysis partly **post hoc** and preserve that limitation downstream.

## Step 2: Validate Experiment Integrity Before Outcome Significance

### A. Sample Ratio Mismatch

Check **Sample Ratio Mismatch (SRM)** against intended allocation. If unexplained SRM is material, investigate instrumentation/randomization before trusting the treatment effect.

### B. Exposure and Randomization

Check when possible:
- users were not exposed to both variants unintentionally
- assignment unit matches analysis unit
- bot/internal traffic is handled consistently
- logging differs neither by variant nor platform

### C. Duration and Business Cycles

Do not use a blanket “1-2 weeks” rule. Cover relevant product cycles and note event/holiday distortion.

### D. Peeking and Optional Stopping

If a fixed-horizon p-value was repeatedly checked and the test stopped when it crossed 0.05, flag inflated false-positive risk.

**Do not recommend simply** “extend until significant.” If sequential monitoring was planned, use the appropriate method/boundaries.

### E. Novelty / Learning Effects

If behavior plausibly changes after users learn the variant, inspect performance over time rather than aggregate only.

## Step 3: Validate Power and Sample Size Correctly

A formula that uses only the alpha critical value cannot establish 80% power.

For a two-arm proportions test with equal groups, a common planning approximation is:

```text
n_per_arm ≈ [
  z_(1-alpha/2) * sqrt(2*p_bar*(1-p_bar))
  + z_(1-beta) * sqrt(p1*(1-p1) + p2*(1-p2))
]^2 / (p2 - p1)^2
```

`z_(1-beta)` is required to claim a target power such as 80%.

For means, ratios, clustered randomization, repeated measures, variance reduction, or non-standard metrics, use a method appropriate to the design.

### Post-hoc observed power

Do not use **post-hoc observed power** as a substitute for confidence intervals or pre-test power planning. Prefer the pre-test MDE/power contract and the treatment-effect confidence interval.

## Step 4: Calculate the Treatment Effect

For the primary metric report as applicable:
- control value
- treatment value
- absolute difference
- relative lift
- confidence interval
- p-value/test statistic
- practical threshold/MDE

Do not apply a statistical test merely because it is familiar.

## Step 5: Separate Statistical From Practical Significance

Ask separately:
- Statistical: is the result inconsistent with the null under the chosen analysis?
- Practical: is the plausible effect large enough to matter?

A tiny statistically significant effect may not justify complexity. **Non-significance** is not proof of equality or no effect.

## Step 6: Inspect Guardrails and Segments

Check material harms such as revenue/margin, retention, latency, errors, support burden, cancellations, and trust/safety.

A primary win does not override a hard guardrail breach.

Inspect segments only with a pre-existing reason or clearly label exploratory analysis. Do not mine many segments and publish the most favorable result as causal proof. Investigate aggregate/segment reversal and Simpson's paradox where relevant.

## Step 7: Handle Multiple Comparisons

If many metrics, variants, or subgroup tests are interpreted, surface inflated false-positive risk and distinguish confirmatory from secondary/exploratory metrics.

## Step 8: Calibrate the Decision

Do not use a simplistic p < 0.05 ship rule.

### SHIP / ROLL OUT
Only when integrity is acceptable, planned primary analysis supports the result, effect is practically meaningful/strategically justified, guardrails are acceptable, and no hard-risk gate is breached.

### LIMITED ROLLOUT / FOLLOW-UP
Use when evidence is promising but uncertainty or operational risk remains.

### CONTINUE / EXTEND ONLY WITH A VALID PLAN
Use only when the analysis plan/sequential method supports continuation and more data can narrow the decision-relevant interval. Do not extend only to chase significance.

### STOP / NO EVIDENCE OF MEANINGFUL IMPROVEMENT
Use when data rule out effects worth pursuing or economics/guardrails make continuation unattractive. Do not translate `p >= alpha` into “the variants are the same.”

### INVALID / INVESTIGATE
Use for unexplained SRM, broken randomization/exposure, inconsistent instrumentation, invalid stopping, or critical data-quality issues.

## Step 9: Contradiction Pass

Ask:
- Could logging/randomization explain the result?
- Does the CI include material harm/upside?
- Am I calling no effect only because p >= 0.05?
- Am I calling ship only because p < 0.05?
- Did an important segment reverse direction?
- Did guardrail harm get hidden?
- Was the test stopped after peeking?
- Are multiple comparisons making evidence look stronger?

## Output

```text
## A/B Test Decision: [Test Name]

### Verdict
Recommendation: SHIP | LIMITED ROLLOUT | CONTINUE WITH VALID PLAN | STOP | INVALID-INVESTIGATE
Confidence: High | Medium | Low

### Experiment Contract
[hypothesis, randomization unit, metrics, alpha, power, MDE, sample/duration, stopping]

### Integrity Checks
| Check | Status | Evidence / Concern |

### Results
| Claim ID | Metric | Population/Period | Control | Treatment | Absolute diff | Relative lift | CI | p-value | Practical threshold | State |

### Guardrails
[claims + states + hard gates]

### Derived Product Claims
| Claim ID | Parent IDs | Interpretation | State | Scope | Caveats |

### Interpretation
- What the data support
- What the data do not support
- Important unknowns

### What Would Change the Decision
[specific evidence]

### Next Action
[concrete action]

## Reliability Handoff
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Experiment Scope | Evidence | Validity Caveat | Downstream Restriction |

### Unresolved P0
[SRM/data/guardrail/maturity/analysis blockers]

### Prohibited Interpretations
[p-value != launch proof; measured scope != universal effect; exploratory subgroup != confirmatory result]
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
- allow a downstream artifact to broaden the tested scope under the same claim ID

---

### Further Reading

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
