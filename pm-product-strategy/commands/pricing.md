---
description: Design an evidence-led pricing strategy with model choices, willingness-to-pay evidence, economics, migration risk, and falsifiable experiments
argument-hint: "<product or pricing question>"
---

# /pricing - Evidence-Led Pricing Strategy

Build a pricing decision from evidence. Do not manufacture willingness to pay, competitor prices, revenue forecasts, CAC, LTV, margins, or conversion assumptions to complete the template.

## Reliability Contract

- Treat current pricing, customer budgets, competitor prices, WTP, elasticity, CAC, LTV, margin, conversion, and retention as `FACT` only when supported by supplied or verified evidence.
- If willingness-to-pay evidence is absent, write `WTP UNKNOWN`. Competitive anchoring and value hypotheses may guide experiments, but they are not WTP proof.
- Never invent a price point because the user requested a recommendation.
- Never state that one pricing model is universally best. Flat-rate, seat, usage, tiered, outcome-linked, transaction, subscription, one-time, hybrid, and free/trial structures depend on the value metric, buyer, costs, risk, and buying process.
- Do not use generic claims such as "value-based pricing always wins" or a universal CAC/LTV ratio as a decision rule.
- Revenue projections require reconstructable inputs and formulas. Otherwise mark `ECONOMICS UNKNOWN` and provide the missing inputs.
- Published competitor pricing must be current and sourced. Hidden/negotiated pricing remains `UNKNOWN` unless evidence exists.
- A pricing page, survey answer, or stated preference is not equivalent to observed purchase behavior.
- For irreversible or broad pricing changes, define a migration, rollback, and customer-protection path.

## Workflow

### Step 1: Frame the Pricing Decision

Capture:
- product and value delivered
- target account, buyer, user, and payer
- stage: pre-launch, pilot, established, migration
- current model/package/price if known
- business objective and constraints
- delivery/service/infrastructure cost structure if material
- evidence already available and material unknowns

State the actual decision, for example:

`Choose a price metric for the next pilot` is different from `set final enterprise list price`.

### Step 2: Define the Value and Cost Mechanics

Apply **pricing-strategy** and **monetization-strategy**.

For each plausible model, evaluate:
- what unit of value the customer perceives
- who controls or predicts usage
- whether the metric creates customer anxiety or gaming
- expansion and contraction behavior
- gross-margin / delivery-cost implications
- procurement and contract fit
- implementation and billing complexity
- likely failure modes

Do not force every model into the comparison. Exclude models that are structurally incompatible and explain why.

### Step 3: Build the Evidence Ledger

Separate:
- `FACT`: observed purchase, renewal, current spend, verified competitor price, actual unit cost
- `INFERENCE`: interpretation supported by facts
- `ASSUMPTION`: unverified belief
- `ESTIMATE`: reconstructable quantitative approximation
- `UNKNOWN`: missing decision-critical evidence
- `TARGET`: desired outcome, not observed performance

For WTP, rank evidence roughly from stronger to weaker:
1. completed purchase / signed commercial commitment
2. negotiated pilot or paid design partner
3. observed current spend / switching cost
4. structured pricing experiment
5. conjoint / Van Westendorp / survey evidence
6. interview statement
7. internal opinion or competitor anchor

Do not silently promote weaker evidence.

### Step 4: Competitive Pricing

When current research is available:
- verify applicable competitor and alternative prices
- capture unit, package, geography, customer tier, contract assumptions, and date
- include DIY, internal build, services, and status quo where relevant

Do not require a fixed competitor count. If coverage is incomplete, say `COMPETITIVE PRICING COVERAGE INCOMPLETE`.

### Step 5: Economics

Only calculate scenarios when inputs exist. Show formulas and sensitivities for material inputs such as:
- accounts/users/usage
- conversion
- retention/churn
- expansion/contraction
- price realization / discounting
- infrastructure and service cost
- sales/support cost when relevant

If inputs do not support a forecast, do not print fabricated Year 1 or Year 2 ARR.

### Step 6: Experiments and Decision Gates

Prefer tests that can disconfirm the preferred pricing thesis:
- paid pilot / design-partner offer
- package or price quote test with real prospects
- controlled offer test where ethically and operationally appropriate
- conjoint / Van Westendorp when survey design fits the question
- usage/value-metric instrumentation
- sales loss-reason capture

For each experiment specify:
- hypothesis
- segment
- evidence to collect
- success and failure rule
- guardrails
- what remains unproven

Decision outcomes:

`LAUNCH | PILOT | TEST WTP | TEST VALUE METRIC | HOLD | ECONOMICS UNKNOWN`

## Output

```text
## Pricing Decision: [Product]

### Decision and Stage
[What must be decided now]

### Evidence Status
[FACT / INFERENCE / ASSUMPTION / ESTIMATE / UNKNOWN / TARGET]

### Plausible Models
| Model | Value Metric | Evidence | Economics | Customer Risk | Operational Risk | Status |

### WTP Evidence
[Observed evidence, gaps, and confidence]

### Competitive / Alternative Pricing
[Verified current evidence only]

### Economics
[Formulas, inputs, sensitivities, or ECONOMICS UNKNOWN]

### Recommended Next Decision
[Recommendation appropriate to evidence maturity]

### Experiments
[Tests, gates, guardrails, disconfirming criteria]

### Migration / Rollback
[When relevant]

### What Would Change the Recommendation
[Specific evidence]
```

## Notes

- Pricing is a product and business-model decision, not a template-completion exercise.
- Customer value matters, but value hypotheses do not establish WTP.
- Prefer a reversible test over false precision when evidence is weak.
- Never turn a `TARGET`, benchmark, or internal aspiration into observed performance.
