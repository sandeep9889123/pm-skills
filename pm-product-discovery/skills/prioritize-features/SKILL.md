---
name: prioritize-features
description: "Prioritize product opportunities or features using outcome impact, evidence confidence, effort, risk, strategic fit, opportunity cost, and inherited claim lineage. Use when making scope, portfolio, or backlog investment decisions."
---

## Prioritize Product Opportunities / Features

Prioritize only as precisely as the evidence allows. The goal is to allocate scarce capacity to the highest expected value learning or outcome, not to manufacture a ranked list.

## Cross-Skill Lineage Consumer Contract

When analytics, research, discovery, strategy, or business-case artifacts provide claim IDs / a `Reliability Handoff`:

- preserve stable claim IDs for restated evidence;
- preserve evidence state, population/segment/time scope, metric definition, confidence, caveats, contradictions, and freshness;
- do not convert `FACT` about a measured pattern into `FACT` about its cause;
- do not convert statistical significance into practical/business significance automatically;
- do not convert `INFERENCE`/`ASSUMPTION` into impact scores as though measured;
- preserve `ESTIMATE` ranges and methods rather than collapsing to point values;
- create new parent-linked claims for prioritization-specific expected-impact or causal hypotheses;
- inherited data-quality/SRM/censoring/instrumentation blockers remain visible;
- repeated evidence in multiple candidate briefs does not become independent corroboration.

## Step 1: Define the Decision

State:
- product/business outcome
- time horizon
- capacity/budget constraint
- target segment
- hard commitments/dependencies
- risk tolerance
- upstream claim coverage and material blockers

Without a decision constraint, prioritization is usually just scoring theatre.

## Step 2: Separate Problem From Solution

Where possible, assess **opportunities/problems first**, then solutions. A popular feature request may be one proposed solution to a deeper job/pain.

Do not let an analytics correlation silently turn a candidate solution into a validated causal remedy.

## Step 3: Build Evidence Ledger

For each candidate capture:
- supporting claim IDs
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

Use:

| Candidate | Evidence Claim IDs | Evidence States | Scope | Expected Mechanism | Impact Range | Effort Range | Key Unknown |

## Step 4: Choose Framework to Fit Uncertainty

Use Opportunity Score, ICE, RICE, cost of delay, expected value, or qualitative portfolio judgment only where input quality supports it. Do not convert low-confidence guesses into precise composite scores.

Any expected-impact score calculated from upstream estimates remains a derived `ESTIMATE`, with parent claim IDs and sensitivity.

## Step 5: Rank by Decision Quality

Prefer tiers when evidence does not justify exact order:
- `COMMIT`
- `VALIDATE NEXT`
- `DEFER`
- `DROP`

Only provide exact top-N rankings when meaningful differences survive uncertainty/sensitivity checks.

A `COMMIT` decision does not promote its supporting analytical claims to `FACT`.

## Step 6: Opportunity-Cost and Dependency Pass

For each `COMMIT`, state:
- what gets delayed or not funded;
- which supporting claim IDs are load-bearing;
- what prerequisite must be true;
- whether another smaller experiment could resolve uncertainty first;
- whether the initiative is reversible.

## Edge Cases / Anti-Patterns

- Do not force "top 5" when only two candidates are supported.
- Do not reward large reach if evidence of value is weak.
- Do not let executive/customer seniority substitute for problem evidence.
- Do not treat committed delivery obligations and speculative bets as identical backlog items.
- Do not double-count reach and impact across overlapping scoring dimensions.
- Do not ignore maintenance, support, compliance, or operational load.
- Do not rank a 10x uncertain estimate above a well-supported smaller bet without showing sensitivity.
- Do not turn cohort correlation or exploratory segment results into causal impact assumptions without an explicit derived claim.

## Output

| Candidate | Outcome | Claim IDs | Evidence States | Confidence | Impact Range | Effort Range | Risk | Learning Value | Decision |

Then show:
- capacity allocation
- deprioritized items and why
- top uncertainty to test
- sensitivity: what input change would reorder priorities

### Derived Prioritization Claims

| Claim ID | Parent IDs | Derivation | State | Sensitivity / Caveat |

### Reliability Handoff

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED
Unresolved P0: [claim IDs + evidence needed]
Prohibited interpretations: [priority != proof; commit != evidence promotion; correlation != causal impact]
```

### Decision

`COMMIT | VALIDATE | DEFER | DROP` per candidate, with no false precision.

---

### Further Reading

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
