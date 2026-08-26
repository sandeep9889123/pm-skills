---
name: outcome-roadmap
description: "Create or transform an outcome-focused roadmap that preserves upstream claim lineage, evidence-backed problems, desired outcomes, bets, learning milestones, dependencies, and decision points without false delivery certainty."
---

# Outcome-Focused Roadmap

## Purpose

Communicate **what outcomes matter, why they matter, what bets are being made, what must be learned, and when decisions will be revisited**. Do not disguise an uncertain portfolio as a feature calendar.

## Cross-Skill Lineage Consumer Contract

When strategy, business case, discovery, analytics, or capability work provides claim IDs / a `Reliability Handoff`:

- preserve claim IDs and evidence states for restated inputs;
- preserve scope, freshness, estimate methods, contradictions, and restrictions;
- never convert `PROPOSAL` into `COMMITTED` because it appears in an approved business-case deck;
- never convert `TARGET` into baseline or achieved outcome;
- never convert an `ESTIMATE` into a fixed capacity/date/benefit without preserving estimate status and assumptions;
- inherited `UNKNOWN`, `STALE`, or unresolved P0 claims remain explicit dependencies/gates;
- create new parent-linked claim IDs for roadmap-specific portfolio inferences;
- scope expansion from one client/segment to a portfolio assumption requires a new derived claim;
- roadmap sequencing or leadership preference is not new customer/market evidence.

## Method

1. **Gather strategy, business-case handoff, and evidence**
   For each initiative capture target segment, observed problem, baseline/metric if known, strategic link, urgency, constraints, confidence, upstream claim IDs, and inherited blockers.

2. **Uncover intended outcome**
   For each output ask:
   - what customer behavior/state should change?
   - what business/operational outcome follows?
   - what evidence supports this mechanism?
   - which claim IDs support it?
   - could another solution achieve the same outcome more cheaply?

   New outcome-mechanism conclusions are derived claims, not automatic FACTs.

3. **Separate commitment types**
   Classify items:
   - `COMMITTED`: authorized delivery obligation with justified timing and no material unresolved blocker for that commitment
   - `BET`: chosen investment with uncertainty
   - `DISCOVERY`: learning needed before commitment
   - `OPTION`: plausible later opportunity
   - `MAINTENANCE/RISK`: reliability/compliance/debt obligation

   A business-case `PROPOSAL`, `EXPERIMENT`, or `NOT READY` state cannot silently become `COMMITTED`.

4. **Write outcome statements**
   Use precise but non-fabricated language. Preserve `TARGET` and `ESTIMATE` labels. If no baseline exists, define baseline-establishment work first.

5. **Map bets to outcomes**
   Show multiple possible bets where appropriate. Roadmap should preserve solution flexibility and parent evidence links.

6. **Add learning and decision milestones**
   Examples: customer evidence threshold, prototype result, technical spike, evaluation gate, pilot outcome, security readiness, GTM proof.

   Proposed thresholds remain `DECISION_THRESHOLD` / proposed until owner-approved.

7. **Dependencies and capacity**
   Show cross-team/platform/data/GTM dependencies, resource contention, what is displaced by each commitment, and inherited P0 claim IDs.

## Reliability / Roadmap Certainty Gate

- Never convert leadership aspiration into a customer outcome without evidence.
- Never imply exact delivery dates from strategy/business-case estimates when dependencies do not justify them.
- Flag items whose outcome has no measurable signal.
- Flag output lists rewritten as "outcomes" without changing the decision logic.
- Show uncertainty/confidence and decision dates explicitly.
- Include kill/pivot conditions for major bets.
- Surface portfolio concentration on the same unproven claim/platform/client/market.
- Include operational work required to sustain existing products.
- Do not drop inherited P0 blockers because the roadmap needs executive simplicity.
- Do not refresh stale evidence merely because the roadmap is new.

## Output

| Horizon | Outcome | Evidence Claim IDs | Evidence State | Bet / discovery | Metric | Confidence | Dependency | Decision gate |
|---|---|---|---|---|---|---|---|---|

Then include:
- explicit non-goals / not-now items
- capacity allocation by strategic theme
- assumptions shared across roadmap with claim IDs
- inherited and new P0 risks
- next 3 leadership decisions

### Reliability Handoff

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Reused Claims
| Claim ID | Claim | State | Scope | Roadmap Use |

### Derived Portfolio Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Commitment Traceability
| Roadmap Item | Commitment Type | Supporting Claim IDs | Authorization / Gate | Unresolved Blocker |

### Prohibited Interpretations
[e.g. roadmap placement != evidence promotion; target != achieved; estimate != commitment]
```

### Decision

For each bet: `COMMIT | DISCOVER | CONTINUE | PIVOT | STOP | DEFER`.

`COMMIT` is a roadmap decision, not promotion of the underlying market/customer/economic claims to FACT.

---

### Further Reading

- [Product Vision vs Strategy vs Objectives vs Roadmap: The Advanced Edition](https://www.productcompass.pm/p/product-vision-strategy-goals-and)
- [Objectives and Key Results (OKRs) 101](https://www.productcompass.pm/p/okrs-101-advanced-techniques)
- [Business Outcomes vs Product Outcomes vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
