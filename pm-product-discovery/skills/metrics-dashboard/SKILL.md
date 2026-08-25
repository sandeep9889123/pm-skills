---
name: metrics-dashboard
description: "Design a decision-linked product metrics dashboard with precise metric contracts, source/instrumentation checks, baselines, guardrails, and evidence-based alerts. Avoids invented targets, vanity metrics, and unsupported causal trees. Use when defining KPIs, dashboards, instrumentation, or monitoring."
---

# Product Metrics Dashboard

## Purpose

Design a metrics system for `$ARGUMENTS` that can support real product decisions. A polished dashboard with ambiguous definitions or invented thresholds is worse than a smaller dashboard with trustworthy metrics.

## P0 Reliability Contract

### Hard rules

1. **Do not invent current values, baselines, targets, alert thresholds, industry benchmarks, or data sources.** Mark unsupported values `UNKNOWN` or `PROPOSAL`.
2. **Metric names are not definitions.** “Active user,” “conversion,” “retention,” “revenue,” and “quality” require numerator/denominator, entity, event, window, exclusions, and grain.
3. **Do not claim an input metric causes the North Star** without causal evidence. Use `hypothesized driver` until validated.
4. **Do not select a North Star merely because the template expects one.** `NO VALID NSM YET` is acceptable when value delivery is unclear or instrumentation is immature.
5. **Alert thresholds must come from an explicit basis** such as SLO/business impact, historical baseline, control limits, contractual threshold, or validated operating tolerance. Arbitrary green/yellow/red numbers are not allowed.
6. **Instrumentation failure or unknown data lineage means metric status is not trusted.**
7. **A target is not an outcome.** Preserve `TARGET` vs observed values.
8. Check for Goodhart/gaming effects and segment-level harm hidden by aggregates.

## Step 1: Decision and Stage

Resolve:

- product / feature / workflow
- stage: pre-launch, pilot, production, scale
- decisions the dashboard should trigger
- key customer outcome
- business model / value exchange
- known guardrails / risk constraints
- current analytics stack and evidence, if provided

A pre-launch dashboard is a **measurement design**, not evidence of current performance.

## Step 2: Metric Contract

For every metric define:

| Field | Required definition |
|---|---|
| Name | human-readable name |
| Decision | what action could this metric change? |
| Entity / grain | user, account, session, order, document, etc. |
| Formula | numerator / denominator or exact aggregation |
| Event / state | qualifying behavior |
| Window | daily, weekly, rolling 28-day, cohort week N, etc. |
| Exclusions | tests, staff, refunds, ineligible entities, etc. |
| Segment cuts | dimensions needed to detect hidden harm |
| Source | verified table/event/system or `UNKNOWN` |
| Owner | metric definition/data owner if known |
| Status | `VERIFIED | PROPOSED | INSTRUMENTATION GAP` |

Do not recommend a dashboard metric whose definition cannot be reproduced.

## Step 3: Metric Architecture

Use only layers needed by the product:

### Value / North Star candidate
A customer-value measure with a plausible connection to sustainable business value.

### Input / leading indicators
Shorter-cycle metrics teams can influence. Label causal relationships `HYPOTHESIZED` unless established.

### Guardrails / counter-metrics
Metrics that detect optimization damage: quality, safety, margin, complaints, error rate, abandonment, review burden, segment harm, etc.

### Operational health
Latency, availability, error/failure rate, queue/backlog, data freshness, processing completeness where relevant.

### Business/economic outcomes
Revenue, gross margin, cost-to-serve, expansion, churn, payback, or equivalent when applicable.

Avoid dashboard sprawl. Every metric should have a reason to exist.

## Step 4: Data and Instrumentation Gate

For each metric verify or identify:

- source system/table/event
- event semantics
- identity resolution
- deduplication
- timezone
- late-arriving data
- backfills
- bot/test/internal traffic
- missingness
- ownership
- freshness / refresh latency

If the system cannot measure the metric reliably, prioritize instrumentation before target-setting.

## Step 5: Baselines and Targets

Classify values:

- `OBSERVED`: measured from trusted data
- `TARGET`: explicit desired future value
- `PROPOSAL`: suggested threshold requiring approval/validation
- `UNKNOWN`: no reliable value

A target should state its basis:

- contractual/SLO
- economic model
- historical performance
- experiment/pilot threshold
- strategic objective
- externally sourced benchmark with matching definition

Do not copy generic benchmarks when definitions/populations differ.

## Step 6: Alerts

For each alert define:

| Metric | Trigger | Basis | Persistence | Segment scope | Owner | Expected action |
|---|---|---|---|---|---|---|

Avoid alert fatigue:

- separate informative dashboard movement from operational paging
- require persistence/window where appropriate
- distinguish data-pipeline failure from real product degradation
- include recovery/closure condition

## Step 7: Goodhart and Contradiction Pass

Ask:

- How could this metric improve while customer value worsens?
- Could aggregate improvement hide a key segment regression?
- Could teams game the numerator/denominator?
- Is the metric a proxy that may decouple from the intended outcome?
- What counter-metric would expose the failure?
- What evidence would show the proposed driver is not causal?

## Output

### Decision context
[stage, value outcome, decisions supported]

### Metric contracts
[precise reproducible definitions]

### Dashboard layout
Only include current values when observed; otherwise display `UNKNOWN / NOT YET INSTRUMENTED`.

### Instrumentation gaps
[what must exist before the metric is trustworthy]

### Baseline / target / alert register
[each value state + basis]

### Guardrails and segment cuts
[how gaming/hidden harm will be detected]

### Review cadence and ownership
[who reviews what and what action follows]

### Decision
`READY TO INSTRUMENT | READY TO MONITOR | CALIBRATE BASELINES | FIX DATA FIRST | REFRAME METRICS`

State what evidence would change the metric architecture.

---

### Further Reading

- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [AARRR (Pirate) Metrics: The 5-Stage Framework for Growth](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework: Your Guide to Measuring User-Centric Success](https://www.productcompass.pm/p/the-google-heart-framework)
- [Funnel Analysis 101: How to Track and Optimize Your User Journey](https://www.productcompass.pm/p/funnel-analysis)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
