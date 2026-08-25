---
name: monetization-strategy
description: "Design and test monetization options using payer/value-metric fit, willingness-to-pay evidence, delivery economics, competitive context, and falsifiable experiments. Avoids forced option counts and invented CAC/LTV/margins. Use when choosing revenue models, packaging, or monetization direction."
---

# Evidence-First Monetization Strategy

## Purpose

Identify monetization options for `$ARGUMENTS` that fit the value delivered, buyer/payer behavior, cost structure, and company strategy.

Do not generate a fixed number of revenue models merely to fill a template.

## P0 Reliability Contract

1. **Do not force 3-5 monetization strategies.** Return only materially plausible alternatives.
2. **Do not invent WTP, budget, CAC, LTV, gross margin, conversion, churn, deal size, or payback.**
3. Competitor pricing is evidence of market behavior, not proof of this customer's willingness to pay.
4. Interviews that ask “would you pay?” are weak evidence. Prefer current spend, approved budget, paid pilots, price tests, procurement actions, or observed trade-offs.
5. Do not quote generic conversion ranges as if they apply to the user's product.
6. Preserve `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `TARGET`, and `PROPOSAL` states.
7. Tool/search failure means evidence coverage is incomplete.

## Step 1: Monetization Context

Resolve:

- user, buyer and payer
- core job/outcome and value mechanism
- current alternative and spend where known
- product/delivery cost driver
- business stage
- enterprise procurement or self-serve path
- strategic objective: adoption, revenue, margin, expansion, ecosystem, etc.

## Step 2: Evidence Inventory

| Evidence | What it supports | State | Limitation |
|---|---|---|---|

Useful evidence:

- actual contracts/prices/discounts
- WTP research
- lost/won deal reasons
- usage and cost-to-serve
- competitive pricing with source/date
- current workaround spend
- expansion/churn behavior

## Step 3: Generate Plausible Models

Consider only relevant mechanisms:

- subscription
- per-seat / per-account
- usage / consumption
- transaction / take rate
- project / service
- outcome/value-based
- license
- freemium/trial
- platform/marketplace
- partner/channel revenue
- hybrid

For each option define:

| Model | Who pays | Value metric | Why fit | Evidence | Key risk |
|---|---|---|---|---|---|

Do not recommend a value metric simply because it is easy to meter. It should correlate with value while remaining predictable and hard to game.

## Step 4: Economics

Where evidence exists, model the actual economics:

- price / usage assumptions
- variable delivery/inference/cloud/support cost
- implementation/onboarding burden
- sales/acquisition cost when known
- gross/contribution margin
- payback / cash timing
- expansion/contraction behavior

For `ESTIMATE`, show formula, inputs, units, range and sensitivity.

If inputs are unavailable, output `ECONOMICS UNKNOWN` and specify required evidence rather than fabricating CAC/LTV.

## Step 5: Buyer and Adoption Reality

For B2B/enterprise, assess:

- budget owner
- procurement preference
- predictability requirements
- security/legal/finance friction
- PO/contract thresholds
- chargeback/accounting needs
- implementation and renewal path

A technically elegant usage model can fail because buyers require predictable budgets.

## Step 6: Contradiction / Cannibalization Pass

Ask:

- Could pricing suppress the behavior that creates value?
- Could the value metric create cost anxiety or gaming?
- Does freemium attract non-ICP users and raise cost-to-serve?
- Could enterprise discounts erase economics?
- Could a new model cannibalize existing revenue?
- Does a competitor model work because their cost/channel structure differs?
- What is the strongest case for keeping the current model?

## Step 7: Falsifiable Monetization Tests

Use the cheapest credible evidence:

- paid pilot / offer test
- founder/sales price conversations tied to actual buying process
- packaging/price experiment where ethical and statistically appropriate
- quote/proposal conversion
- willingness-to-switch behavior
- usage/cost simulation
- procurement feedback

Define success, failure and inconclusive states before the test.

## Output

### Monetization decision context
### Evidence ledger
### Plausible options
### Economics / sensitivity
### Buyer/procurement fit
### Cannibalization / downside
### Validation plan
### Decision
`TEST | PILOT | KEEP CURRENT | CHANGE MODEL | HOLD | NOT READY`

State what evidence would reverse the recommendation.

---

### Further Reading

- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
