---
description: Design an evidence-led growth strategy using validated mechanisms, channel economics, experiments, and guardrails
argument-hint: "<product or growth challenge>"
---

# /growth-strategy - Evidence-Led Growth Strategy

Design growth mechanisms from observed behavior and economics. Do not force viral loops, PLG, CAC/LTV rules, ROI estimates, timelines, or channel priorities without evidence.

## Reliability Contract

- Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `TARGET`.
- Do not assume a growth loop exists because a framework lists one. A loop requires an observable reinforcing mechanism.
- Do not invent CAC, LTV, payback, ROI, conversion, referral rate, virality, retention, or time-to-result.
- Never use a universal rule such as `CAC < 1/3 of LTV` as a launch or scale gate. Economics depend on gross margin, retention, cash timing, service cost, capital constraints, and business model.
- PLG, outbound, paid, community, partners, ABM, inbound, referral, or other motions are hypotheses until reachability, conversion, economics, and operational capacity are demonstrated.
- A channel that generates volume but damages retention, deal quality, support load, margin, or trust is not a successful growth motion.
- Correlation between a channel and growth is not attribution.
- Scale only after evidence supports the mechanism and guardrails.

## Workflow

### Step 1: Frame the Growth Problem

Capture:
- product and stage
- user, buyer, payer, and account where relevant
- value moment and retention behavior
- current acquisition/activation/retention/expansion data
- revenue model and key cost structure
- current motions and known bottleneck
- constraints: budget, team, sales capacity, implementation, compliance

If no reliable baseline exists, output `INSTRUMENT FIRST` before prescribing scale.

### Step 2: Diagnose the Constraint

Determine whether the main constraint is actually:
- awareness / reach
- qualification
- activation / time-to-value
- retention
- expansion
- sales conversion
- implementation capacity
- pricing / packaging
- product value
- measurement quality

Do not treat every growth problem as an acquisition problem.

### Step 3: Evaluate Growth Mechanisms

Apply **growth-loops** and **gtm-motions**.

For each plausible mechanism, describe:
- trigger
- action
- value created
- how that output feeds the next cycle
- required conditions
- observable loop-health metric
- likely break point
- evidence status

If the feedback path is not real or measurable, call it a tactic or hypothesis, not a loop.

### Step 4: Evaluate GTM Motions

For each relevant motion evaluate:
- ICP reachability
- buyer fit
- evidence of demand/intent
- conversion evidence
- cost and capacity
- implementation / delivery implications
- payback mechanics when reconstructable
- quality guardrails
- reversibility

Do not score motions 1-10 without a defined evidence-based rubric. Use `SUPPORTED | PARTIAL | UNKNOWN | REJECT` where more appropriate.

### Step 5: Design Experiments

Each experiment must specify:
- hypothesis
- target segment
- intervention
- primary metric
- guardrails
- attribution method
- minimum decision window / maturity logic where relevant
- success, failure, and inconclusive rule
- scale / stop / iterate action

Prefer experiments that distinguish competing growth hypotheses.

### Step 6: Economics

When inputs are available, model:
- acquisition cost by motion
- contribution margin
- retention / churn
- expansion
- sales/service cost
- payback / cash timing
- sensitivity to major assumptions

Otherwise output `GROWTH ECONOMICS UNKNOWN` and identify the missing measurements.

### Step 7: Decision

`SCALE | PILOT | ITERATE | FIX INSTRUMENTATION | HOLD | STOP`

`SCALE` requires evidence of mechanism, acceptable economics or a justified strategic exception, and healthy guardrails.

## Output

```text
## Growth Strategy: [Product]

### Growth Decision
[what is being decided]

### Evidence / Baseline
[FACT / INFERENCE / ASSUMPTION / ESTIMATE / UNKNOWN / TARGET]

### Primary Constraint
[diagnosis + evidence]

### Candidate Mechanisms
| Mechanism | Loop/Tactic | ICP Fit | Evidence | Economics | Guardrails | Status |

### Recommended Experiment(s)
[hypothesis, design, decision rule]

### Economics
[reconstructable model or GROWTH ECONOMICS UNKNOWN]

### Risks and Counter-Metrics
[quality, retention, support, margin, trust, compliance]

### Decision
[SCALE | PILOT | ITERATE | FIX INSTRUMENTATION | HOLD | STOP]

### What Would Change the Recommendation
[specific evidence]
```

## Notes

- Growth is a system outcome, not a list of channels.
- Budget should follow demonstrated learning and economics, not framework popularity.
- A fast-growing low-quality cohort can destroy value while making top-line acquisition metrics look healthy.
