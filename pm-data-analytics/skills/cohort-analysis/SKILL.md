---
name: cohort-analysis
description: "Perform defensible cohort and retention analysis with explicit definitions, eligible denominators, censoring/maturity checks, segment-mix controls, causal limits, and a lineage-preserving handoff for downstream product decisions."
---

# Cohort Analysis & Retention Explorer

## Purpose

Analyze longitudinal behavior for `$ARGUMENTS` without producing misleading retention curves from ambiguous event definitions, immature cohorts, denominator errors, or causal overreach.

## P0 Reliability Contract

1. **Define cohort membership and outcome event before calculating.** “Active,” “retained,” “adopted,” and “churned” are not self-defining.
2. **Use eligible denominators.** A cohort cannot be evaluated at period N if members have not had enough calendar time to reach period N.
3. **Do not compare immature and mature cohorts as if observation windows are equal.** Mark right-censored cells `NOT YET OBSERVABLE` rather than zero.
4. **Descriptive difference ≠ causal explanation.** Cohort analysis can show what changed; it usually cannot prove why without additional design/evidence.
5. **Do not invent industry benchmarks.** Use only current sourced benchmarks with matching metric definitions/populations, otherwise omit them or mark `UNKNOWN`.
6. **Do not infer user-level retention from aggregate data that cannot support it.** State the available unit of analysis.
7. **Tool/code/data failure means analysis incomplete, not “no effect.”**

## Claim-Lineage Producer Contract

For every decision-relevant analytical result:

- assign a stable `claim_id`;
- preserve the metric/data contract and population/time scope;
- classify calculated patterns as `FACT` only for the exact measured result when data integrity is acceptable;
- classify explanatory/causal interpretations separately as `INFERENCE`, `ASSUMPTION`, or `UNKNOWN`;
- preserve confidence, caveats, data-quality failures, censoring, and sensitivity;
- preserve source/query/file references where available;
- do not allow a downstream roadmap/launch artifact to interpret an observed cohort difference as causal proof;
- a new causal or strategic conclusion must be a parent-linked derived claim.

Example:
- `AN-014 FACT`: March cohort week-4 retention is 8pp lower than January under the stated metric contract.
- `AN-015 INFERENCE`, parents `[AN-014]`: acquisition-mix shift may contribute.
- Not allowed: reuse `AN-014` as “the onboarding redesign caused an 8pp retention drop.”

## Step 1: Decision and Data Contract

Resolve:
- decision the analysis supports
- entity: user, account, workspace, subscription, order, etc.
- cohort entry event and timestamp
- retention/adoption/churn event
- period granularity
- observation window
- timezone
- exclusion rules
- segment dimensions
- known product/marketing/pricing changes

Create a metric contract:

`Retention(N) = entities from cohort eligible for period N that perform qualifying event in period N / entities from cohort eligible for period N`

If using rolling/unbounded retention, survival, revenue retention, or another definition, state it explicitly instead.

## Step 2: Data Quality and Eligibility Gate

Check where possible:
- unique entity key integrity
- duplicate events
- missing cohort/event timestamps
- backfilled or late-arriving events
- timezone/calendar boundaries
- deleted/test/internal accounts
- multiple accounts per person where relevant
- acquisition/channel mix changes
- cohort size and extreme imbalance
- incomplete observation periods

Report what cannot be checked. Coverage failures must be inherited downstream.

## Step 3: Calculate With Observable Denominators

| Cohort | Original size | Eligible at period | Retained/adopted | Rate | Observable? |

Never populate future cells with 0 solely because time has not elapsed.

For feature adoption distinguish:
- eligible population
- exposed population
- attempted use
- successful use
- repeated/retained use

Do not call lack of adoption a preference signal when users may not have been exposed to the feature.

## Step 4: Compare Cohorts Carefully

Inspect:
- cohort size
- maturity / same-age comparison
- acquisition source
- plan / geography / customer type
- seasonality
- product version / launch date
- pricing or packaging changes
- instrumentation changes

Where sample size is small, show direction and uncertainty instead of declaring a stable trend.

## Step 5: Pattern vs Explanation

Label findings:
- `FACT / OBSERVED`: directly calculated pattern under a valid data contract
- `INFERENCE`: plausible explanation supported indirectly
- `ASSUMPTION`: unverified explanation
- `UNKNOWN`: insufficient evidence

Do not let the evidence state of the measured pattern transfer automatically to its explanation.

## Step 6: Contradiction / Sensitivity Pass

Before recommending action:
- compare same-age cohorts
- test major segment splits where justified
- inspect whether the conclusion reverses after controlling for acquisition/plan/geography
- test with/without outlier cohorts
- verify metric-definition or instrumentation changes
- distinguish calendar effect from product effect

If conclusions are highly sensitive, preserve that caveat in the lineage record.

## Step 7: Follow-Up Design

Choose the cheapest evidence that can test the leading explanation:
- event-level diagnostic
- segment drill-down
- funnel analysis
- qualitative interviews
- instrumentation audit
- controlled experiment
- quasi-experimental analysis when appropriate

Do not jump from a retention pattern directly to a feature roadmap.

## Output

### Analysis Contract
[entity, cohort event, outcome event, period, denominator, exclusions, observation window]

### Data-Quality Status
[known checks, failures, unknowns]

### Cohort Table / Curves
[with unobservable cells separated from zeros]

### Findings
| Claim ID | Finding | State | Metric/Population Scope | Evidence | Confidence | Decision Implication |

### Derived Explanations
| Claim ID | Parent IDs | Explanation | State | Evidence Needed |

### Alternative Explanations / Contradictions
[segment mix, seasonality, maturity, instrumentation, product changes]

### Decision
`ACT | INVESTIGATE | RUN EXPERIMENT | FIX DATA/INSTRUMENTATION | INCONCLUSIVE`

### Reliability Handoff

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Metric Contract / Scope | Evidence | Caveat | Downstream Restriction |

### Derived Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Unresolved P0
[data/instrumentation/causality gaps]

### Prohibited Interpretations
[observed != causal; immature != zero; correlation != product effect]
```

State what evidence would change the decision.

---

### Further Reading

- [Cohort Analysis 101: How to Reduce Churn and Make Better Product Decisions](https://www.productcompass.pm/p/cohort-analysis)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
