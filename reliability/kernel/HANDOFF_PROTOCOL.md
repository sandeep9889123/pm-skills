# Cross-Skill Handoff Protocol V1

## Purpose

The largest reliability risk in a multi-skill PM workflow is not one isolated hallucination. It is **claim inflation across handoffs**.

Example failure:

```text
Market research: ESTIMATE, LOW confidence
  -> Strategy: "market is $500M"
  -> Business case: $500M FACT
  -> GTM: "proven $500M market"
```

This protocol makes that transformation illegal unless new evidence is explicit and traceable.

The portable unit of evidence remains [`claim_lineage.schema.json`](claim_lineage.schema.json). The handoff envelope packages those claims with decision context, coverage, unresolved blockers, source artifacts, and transformation lineage.

Core rule:

> **Restating a claim never strengthens it. Formatting, summarizing, executive polish, repetition across frameworks, model confidence, stakeholder enthusiasm, or downstream importance are not new evidence.**

## Producer Contract

A P0 workflow that hands decision-critical material downstream should emit or be able to emit a **Handoff Envelope**.

For every material claim:

1. assign a stable `claim_id`;
2. preserve its evidence `state`;
3. preserve source class and references;
4. preserve scope and freshness;
5. preserve contradictions/caveats;
6. preserve publishability/confidentiality;
7. specify allowed and prohibited downstream uses;
8. identify unresolved P0 evidence gaps separately from narrative conclusions.

Do not omit uncertainty because the receiving artifact is executive-facing.

## Consumer Contract

When a P0 skill receives a handoff envelope or a source artifact containing lineage records:

1. **Inherit before interpreting.** Read claim states, scope, sources, coverage, and blockers before producing recommendations.
2. **Preserve stable claim IDs** when merely restating a claim.
3. **No silent promotion.** A downstream skill may not strengthen a claim without explicit new evidence and promotion history.
4. **No silent scope expansion.** Evidence about one geography, segment, account, time period, or workflow cannot become a broader claim through paraphrase.
5. **Propagate contradictions.** Downstream synthesis may resolve a contradiction only with evidence; otherwise the contradiction remains visible.
6. **Propagate freshness.** A stale source does not become current because a new artifact cites it.
7. **Propagate confidentiality.** `CLIENT_CONFIDENTIAL`, `INTERNAL_ONLY`, and `REQUIRES_CLEARANCE` claims remain restricted downstream.
8. **Respect prohibited uses.** A claim marked unsuitable for public proof, ROI, market sizing, or sales collateral cannot be reused for that purpose without new evidence/clearance.
9. **Unresolved P0 survives polish.** A formatted deck, PRD, business case, roadmap, or launch plan cannot hide a P0 blocker inherited from upstream.
10. **Tool/retrieval failure stays visible.** Missing upstream artifacts or unavailable evidence becomes `COVERAGE INCOMPLETE`, not an implicit clean state.

## Transformation Types

Each claim in a handoff uses one transformation type:

- `ORIGINAL`: first appearance of the claim in the lineage system.
- `RESTATED`: same substantive claim, same state/scope/evidence.
- `DERIVED`: a new analytical claim based on one or more parent claim IDs.
- `PROMOTED`: evidence state strengthened because new evidence was added.
- `DOWNGRADED`: evidence state weakened because evidence became stale, contradicted, or less applicable.

### RESTATED

Must preserve:
- `claim_id`
- evidence state
- scope
- source references
- freshness
- publishability

A wording change is not a new claim if the meaning is materially the same.

### DERIVED

Must include:
- new `claim_id`
- one or more `parent_claim_ids`
- derivation explanation
- state no stronger than the evidence and reasoning justify
- explicit caveats where derivation depends on assumptions

A derived conclusion is usually `INFERENCE` or `ESTIMATE`, not `FACT`, unless it is a deterministic transformation of verified facts and the method is transparent.

### PROMOTED

Requires:
- stable `claim_id`
- explicit `promotion_history`
- `from` and `to` states
- at least one `new_evidence` reference
- reason for promotion
- freshness and scope re-check

Examples:
- `ASSUMPTION -> FACT` after direct authoritative evidence
- `UNKNOWN -> ESTIMATE` after collecting reconstructable inputs
- `ESTIMATE -> FACT` after measurement
- `PROPOSAL -> FACT` only when the fact being asserted is that the proposal was formally approved/implemented, not that its target outcome was achieved

### DOWNGRADED

Use when:
- evidence becomes stale;
- contradictory evidence appears;
- the claim is discovered to exceed source scope;
- a previously trusted source is invalidated.

Do not preserve a stronger state merely to avoid rewriting downstream artifacts.

## State-Specific Rules

### FACT

A downstream FACT remains scoped to the exact evidence. `FACT` does not mean universally true.

### INFERENCE

May support a decision when uncertainty is acceptable, but must not become FACT through repetition.

### ASSUMPTION

Must stay visibly testable. It cannot be converted to a roadmap commitment or launch proof without evidence appropriate to the consequence.

### ESTIMATE

Must preserve formula, inputs, units, and sensitivity/range where material. Rounding or visual simplification does not remove the estimate status.

### UNKNOWN

Must not disappear merely because a downstream template has a required field.

### STALE

Must not become current via a newer document date. Refresh the underlying evidence.

### TARGET

A desired result is not an achieved result. Downstream artifacts must retain `TARGET` until measurement proves outcome.

### PROPOSAL

A proposed action is not an approved decision, completed implementation, or achieved result.

### DECISION_THRESHOLD

A threshold should preserve whether it is owner-approved, evidence-derived, or merely proposed.

## Scope Rules

Material scope dimensions include:
- geography
- segment / account type
- population
- time period
- product/workflow

For the same `claim_id`, a consumer must not silently change material scope.

If a broader/narrower claim is analytically needed:
- create a new claim ID;
- link the parent claim(s);
- explain the transformation;
- set evidence state appropriate to the new scope.

## Coverage Rules

Handoff coverage states:

- `COMPLETE FOR DECLARED SCOPE`
- `PARTIAL`
- `BLOCKED`

`PARTIAL` or `BLOCKED` coverage cannot be summarized downstream as complete merely because all available material was processed.

## Decision Gate

A downstream irreversible decision is blocked when inherited unresolved P0 claims are material to that decision and remain `UNKNOWN`, `STALE`, materially contradicted, or prohibited for the intended use.

Valid downstream outcomes include:

`PROCEED | PROCEED WITH CONDITIONS | TEST | HOLD | REFRAME | NOT READY | NO-GO`

The exact vocabulary may differ by skill, but uncertainty cannot be hidden by the label.

## Priority Handoffs

Wave 6 applies this protocol first to:

1. Market Research -> Product Strategy
2. Prospect Discovery -> PRD / Proposal / Business Case
3. Client Proof -> Case Study -> GTM / Battlecard
4. Business Case -> Roadmap / Capability Investment
5. Analytics -> Prioritization / Launch Decision
6. PoC -> Production Readiness

## Minimum Handoff Block for Markdown Workflows

When JSON output is not appropriate, a P0 workflow can emit this compact block:

```text
## Reliability Handoff

Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Scope | Source/Evidence | Freshness | Publishability | Downstream Restrictions |

### Derived Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Unresolved P0
[claim IDs + evidence needed]

### Decision Status
[decision + inherited blockers]

### Prohibited Interpretations
[what the downstream reader must not infer]
```

## Non-Negotiable Self-Check

Before consuming a handoff, ask:

- Did any `ESTIMATE` become an unlabeled number?
- Did any `TARGET` become an achieved outcome?
- Did any `PROPOSAL` become an approved decision?
- Did any `UNKNOWN` disappear because the template wanted completeness?
- Did any stale claim become current because this artifact is new?
- Did scope broaden without a new claim and derivation?
- Did client-confidential evidence become public proof?
- Did a repeated claim become "corroborated" without an independent source?

If yes, the handoff fails.
