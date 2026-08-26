---
name: discovery-synthesis
description: "Turn enterprise prospect discovery notes or transcripts into evidence, validated assumptions, contradictions, scope implications, dependencies, next actions, and a lineage-preserving handoff for downstream PRD/proposal/business-case work."
---

# Discovery Synthesis

Treat the transcript or notes as evidence, not as a narrative prompt.

## Evidence Rules

- Do not invent answers for questions that were not answered.
- Preserve uncertainty and contradiction.
- Distinguish prospect statements from verified operational evidence.
- Preserve who said what when authority matters.
- Do not turn enthusiasm into willingness to pay.
- Do not turn "possible" into committed scope.
- Do not turn a target into an achieved metric.
- Do not turn a proposed use case into a validated requirement merely because the prospect discussed it.

## Claim-Lineage Producer Contract

For every decision-critical discovery claim:

- assign a stable `claim_id`;
- classify `FACT | INFERENCE | ASSUMPTION | ESTIMATE | UNKNOWN | STALE | TARGET | PROPOSAL`;
- preserve speaker/source and authority where material;
- preserve account/workflow/geography/time scope;
- preserve contradictions and caveats;
- mark confidentiality/publishability where known;
- mark prohibited downstream interpretations;
- list unresolved P0 claims separately.

Examples:
- "API may be available" stays `PROPOSAL`/`UNKNOWN`, not an integration requirement;
- "we would use this" remains weak intent evidence, not demand/WTP `FACT`;
- a target SLA remains `TARGET`, not current performance;
- one stakeholder's statement does not automatically represent economic-buyer approval.

Downstream PRDs, proposals, architecture estimates, and business cases must retain the same claim IDs when restating these claims.

## Synthesis Structure

### 1. Original Hypothesis

Restate the problem and use-case hypothesis going into the session. Preserve its original evidence state.

### 2. Evidence Changes

For each material claim show:

| Claim ID | Before State | New Evidence | After State | Scope | Contradiction/Caveat |

A state upgrade requires explicit new evidence. If evidence only weakens or complicates the claim, downgrade or preserve uncertainty.

### 3. Workflow and Actors

Capture validated actors, stages, systems, data, handoffs, exception paths, and authority boundaries.

Do not infer missing systems, APIs, volumes, owners, or approvals.

### 4. Scope Implications

Capture:
- Phase 1 candidates
- explicit out-of-scope
- deferred items
- dependencies
- prospect-owned inputs
- delivery-owned inputs

A Phase 1 candidate is not committed scope until an authorized decision supports it.

### 5. Assumption Register Update

Update status without erasing original assumptions or claim IDs.

### 6. Decision Gaps

List unresolved P0 items and why each blocks or conditions:
- solutioning
- architecture
- estimation
- business case
- proposal

### 7. Strongest Case Against Proceeding

State the strongest supported reason the opportunity or wedge could fail. Missing evidence alone is an evidence gap, not negative evidence.

### 8. Next Actions

Every follow-up should have:
- claim/question/evidence needed
- owner if explicitly assigned
- decision it unlocks
- target timing if supplied

### 9. Reliability Handoff

```text
## Reliability Handoff
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Scope | Source/Speaker | Authority | Freshness | Downstream Restrictions |

### Derived Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Unresolved P0
[Claim ID + blocker + evidence needed]

### Readiness by Decision
- Solutioning:
- Architecture:
- Estimation:
- Business case:
- Proposal:

### Prohibited Interpretations
[e.g. enthusiasm is not WTP; possible API is not verified integration; target is not achieved outcome]
```

## Output Principle

A shorter evidence-complete synthesis is better than an executive-looking summary that hides uncertainty. Restating discovery evidence downstream never strengthens it.
