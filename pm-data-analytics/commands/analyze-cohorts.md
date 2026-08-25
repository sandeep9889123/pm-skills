---
description: Defensible cohort analysis — explicit event definitions, eligible denominators, maturity/censoring checks, segment-mix controls, and causal limits
argument-hint: "<data file or description of what to analyze>"
---

# /analyze-cohorts -- Defensible Cohort Analysis

Analyze retention, adoption, churn, or longitudinal engagement without letting immature cohorts, denominator errors, or descriptive patterns become false causal claims.

## Step 1: Define the Analysis Contract

Before calculating, define:

- decision being supported
- entity/grain: user, account, workspace, subscription, etc.
- cohort entry event
- retention/adoption/churn event
- granularity and observation window
- timezone
- exclusions
- segment cuts

If the user asks “why did cohort X underperform?”, treat `why` as a hypothesis question. Cohort analysis alone usually establishes **what differed**, not causality.

## Step 2: Data / Schema Gate

### With data

Validate:

- entity IDs and duplicates
- event/cohort timestamps
- cohort sizes
- missingness
- test/internal entities
- late-arriving/backfilled data
- maturity/right-censoring

### Without data

Create an analysis plan and, if useful, a SQL **template**. Do not invent real table/column names. Use the `sql-queries` reliability rules.

## Step 3: Analyze

Apply **cohort-analysis**.

Required behaviors:

- use eligible denominators
- mark future/unobservable cells `NOT YET OBSERVABLE`, not zero
- compare cohorts at the same age
- distinguish eligible vs exposed populations for feature adoption
- show sample/cohort size
- inspect acquisition/plan/geography/product-version mix when material

## Step 4: Interpretation Gate

Label findings:

- `OBSERVED`
- `INFERENCE`
- `ASSUMPTION`
- `UNKNOWN`

Do not write:

> “Cohort X is worse because of Y”

unless the available design/evidence supports that causal conclusion.

Prefer:

> “Cohort X has lower week-4 retention. Y is one plausible explanation; the following evidence would test it.”

## Step 5: Benchmark Guard

Do not add “industry benchmarks” unless a current source with a matching metric definition/population is actually available. Otherwise mark benchmark comparison `NOT AVAILABLE / NOT COMPARABLE`.

## Step 6: Sensitivity / Contradiction Pass

Check:

- same-age comparison
- segment-mix reversal
- seasonality
- product/instrumentation changes
- outlier cohorts
- alternate retention definitions when reasonable

## Output

### Analysis Contract
[entity, cohort, event, denominator, period, timezone]

### Data Quality / Observability
[checks, failures, unknowns]

### Cohort Results
[table/curves with observable status]

### Findings
| Finding | State | Evidence | Confidence | Implication |
|---|---|---|---|---|

### Alternative Explanations
[what else could explain the pattern]

### Follow-Up Evidence
[queries, interviews, funnel checks, instrumentation audit, experiment]

### Decision
`ACT | INVESTIGATE | RUN EXPERIMENT | FIX DATA/INSTRUMENTATION | INCONCLUSIVE`

If code is used, preserve the analysis script and assumptions so the result is reproducible.
