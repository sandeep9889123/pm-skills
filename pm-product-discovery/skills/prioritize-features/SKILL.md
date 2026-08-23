---
name: prioritize-features
description: "Prioritize product opportunities or features using outcome impact, evidence confidence, effort, risk, strategic fit, and opportunity cost. Use when making scope, portfolio, or backlog investment decisions."
---

## Prioritize Product Opportunities / Features

Prioritize only as precisely as the evidence allows. The goal is to allocate scarce capacity to the highest expected value learning or outcome, not to manufacture a ranked list.

### Context

If the user provides spreadsheets, backlogs, customer evidence, strategy, or opportunity assessments, read them directly.

## Step 1: Define the decision

State:
- product/business outcome
- time horizon
- capacity/budget constraint
- target segment
- hard commitments/dependencies
- risk tolerance

Without a decision constraint, prioritization is usually just scoring theatre.

## Step 2: Separate problem from solution

Where possible, assess **opportunities/problems first**, then solutions. A popular feature request may be one proposed solution to a deeper job/pain.

## Step 3: Build evidence ledger

For each candidate capture:
- user/problem evidence
- reach/frequency
- severity/economic consequence
- strategic linkage
- expected mechanism
- confidence
- effort range
- dependencies
- downside/failure risk
- reversibility
- learning value

Mark unsupported inputs `UNKNOWN` instead of assigning convenient scores.

## Step 4: Choose framework to fit uncertainty

Use Opportunity Score, ICE, RICE, cost of delay, expected value, or qualitative portfolio judgment only where input quality supports it. Do not convert low-confidence guesses into precise composite scores.

## Step 5: Rank by decision quality

Prefer tiers when evidence does not justify exact order:
- `COMMIT`
- `VALIDATE NEXT`
- `DEFER`
- `DROP`

Only provide exact top-N rankings when meaningful differences survive uncertainty/sensitivity checks.

## Step 6: Opportunity-cost and dependency pass

For each `COMMIT`, state:
- what gets delayed or not funded;
- what prerequisite must be true;
- whether another smaller experiment could resolve uncertainty first;
- whether the initiative is reversible.

## Edge cases / anti-patterns

- Do not force “top 5” when only two candidates are supported.
- Do not reward large reach if evidence of value is weak.
- Do not let executive/customer seniority substitute for problem evidence.
- Do not treat committed delivery obligations and speculative bets as identical backlog items.
- Do not double-count reach and impact across overlapping scoring dimensions.
- Do not ignore maintenance, support, compliance, or operational load.
- Do not rank a 10× uncertain estimate above a well-supported smaller bet without showing sensitivity.

## Output

| Candidate | Outcome | Evidence | Confidence | Impact range | Effort range | Risk | Learning value | Decision |
|---|---|---|---|---|---|---|---|---|

Then show:
- capacity allocation
- deprioritized items and why
- top uncertainty to test
- sensitivity: what input change would reorder priorities

### Decision
`COMMIT | VALIDATE | DEFER | DROP` per candidate, with no false precision.

---

### Further Reading

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
