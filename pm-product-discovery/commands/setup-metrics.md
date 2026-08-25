---
description: Design a trustworthy product metrics system with precise definitions, instrumentation checks, baselines, guardrails, and evidence-based alert thresholds
argument-hint: "<product or feature area>"
---

# /setup-metrics -- Trustworthy Product Metrics Design

Design metrics that can support real decisions rather than filling a dashboard template with invented targets or ambiguous KPIs.

## Step 1: Resolve Decision and Stage

Capture:

- product/feature/workflow
- stage: pre-launch, pilot, production, scale
- decisions the metrics should trigger
- customer value/outcome
- business goal
- known risk/guardrail constraints
- current analytics/instrumentation if available

A pre-launch dashboard is a measurement design. It does not have current values or validated baselines unless evidence is provided.

## Step 2: Apply `metrics-dashboard`

For each metric require a reproducible contract:

- entity/grain
- formula
- numerator/denominator
- qualifying event/state
- time window/timezone
- exclusions
- segment cuts
- verified source or `UNKNOWN`
- owner/status

Do not treat metric names such as “active users” or “conversion” as definitions.

## Step 3: North Star / Inputs / Guardrails

- Do not force a North Star when value delivery is unclear. `NO VALID NSM YET` is valid.
- Input metrics are `HYPOTHESIZED DRIVERS` unless causal evidence exists.
- Add counter-metrics/guardrails that expose gaming, quality loss, margin harm, or key-segment regression.
- Prefer a smaller trustworthy metric set over dashboard sprawl.

## Step 4: Instrumentation Gate

For each material metric identify:

- event/table/system
- identity rules
- deduplication
- timezone
- missingness/late data/backfills
- test/internal traffic
- refresh latency

If measurement cannot be trusted, output `FIX DATA / INSTRUMENTATION FIRST` before target-setting.

## Step 5: Baselines, Targets, Alerts

Use explicit states:

- `OBSERVED`
- `TARGET`
- `PROPOSAL`
- `UNKNOWN`

Never invent current values or thresholds.

Each target/alert needs a basis:

- contractual/SLO
- historical baseline
- economic/customer harm threshold
- pilot/experiment criterion
- approved strategic objective
- comparable current external benchmark

For alerts define persistence/window, owner, action and recovery condition. Distinguish real product degradation from broken data pipelines.

## Step 6: Goodhart / Contradiction Pass

Ask:

- How can this metric improve while customer value worsens?
- Can an aggregate hide a harmed segment?
- Can teams game the numerator/denominator?
- What evidence would show the proposed driver is not causal?

## Output

### Decision Context
[stage, decision, value outcome]

### Metric Contracts
[precise definitions]

### Instrumentation Status
`VERIFIED | PARTIAL | GAP`

### Baselines / Targets / Alerts
| Metric | State | Value/threshold | Basis | Owner/action |
|---|---|---|---|---|

### Guardrails / Segment Cuts
[anti-Goodhart controls]

### Dashboard Layout
Do not display fabricated “current values.”

### Decision
`READY TO INSTRUMENT | READY TO MONITOR | CALIBRATE BASELINES | FIX DATA FIRST | REFRAME METRICS`

State what evidence would change the framework.
