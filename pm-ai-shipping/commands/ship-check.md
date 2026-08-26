---
description: Compile a reviewer-ready shipping-readiness packet from documentation, tests, PoC evidence, security review, performance review, explicit coverage gaps, and inherited claim lineage
argument-hint: "<repo path or area; defaults to the whole repository>"
---

# /ship-check - Shipping Readiness Review

This workflow answers a narrower and more defensible question than "is this safe?":

> **What evidence do we have for shipping readiness, what remains unverified, and what should block release?**

It coordinates documentation, PoC/validation evidence, static audits, and test evidence into a packet for human decision. It does not certify security, scalability, commercial success, or production safety.

## P0 Reliability Contract

1. Preserve coverage status from every component audit. Never summarize `PARTIAL`, `BLOCKED`, tool failure, or uninspected scope as a clean pass.
2. Overall coverage states are `COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED`.
3. A security result of `NO SURVIVING FINDINGS IN INSPECTED SCOPE` is not equivalent to secure.
4. A performance result of `NO MATERIAL STATIC FINDINGS IN INSPECTED SCOPE` is not equivalent to scalable or performant.
5. Static review cannot prove runtime behavior, deployed configuration, production data behavior, external service behavior, or load characteristics that were not dynamically verified.
6. Missing/stale critical documentation, unverified trust-boundary rules, unresolved Critical/High security findings, or unavailable required audit/test coverage block a clean readiness state.
7. Tool/subagent/read failures are shipping evidence gaps and must appear in Launch Blockers / Coverage Gaps.
8. Do not generalize a scoped audit to the whole repository/system.
9. Proposed tests are not existing test coverage. Manual checks are not automated regression protection.
10. Final decision remains human-owned.

## Cross-Skill Lineage Consumer Contract

If upstream business case, PRD, experiment, PoC, analytics, client proof, or rollout work provides claim IDs / a `Reliability Handoff`:

- preserve stable claim IDs for restated evidence;
- preserve state, scope, freshness, source/evidence refs, metric/test contract, contradictions, caveats, and restrictions;
- a PoC `FACT` is a fact about the PoC's scoped result, not a FACT about production scale, reliability, security, retention, adoption, WTP, or commercialization;
- `TARGET` thresholds remain targets unless measured;
- `PROPOSAL` architecture/controls remain proposed until implemented/verified;
- create new parent-linked claims for production-readiness conclusions derived from PoC + tests + audits;
- never reuse the PoC claim ID while silently broadening its scope to production;
- inherited P0 blockers remain visible until verified resolution;
- `PARTIAL`/`BLOCKED` upstream coverage remains inherited unless missing evidence is actually obtained;
- decision approval does not promote underlying evidence states.

Example:
- `POC-07 FACT`: 98% task completion on 200 representative test cases under PoC conditions.
- `SHIP-12 INFERENCE`, parents `[POC-07, TEST-04]`: production task quality may be acceptable for limited rollout, conditional on live guardrails.
- Not allowed: restate `POC-07` as "98% production accuracy."

## Invocation

```text
/ship-check
/ship-check the payments service
/ship-check supabase/functions
```

## Step 1: Declare Shipping Scope and Inherited Evidence

State exactly what is being evaluated:
- repository / service / module / feature
- intended environment/release if known
- included and excluded areas
- evidence sources available
- upstream PoC/experiment/business-case claim IDs
- inherited P0 blockers and coverage gaps

If the user requests the whole repo but material areas cannot be inspected, the final coverage cannot be `COMPLETE FOR DECLARED SCOPE`.

## Step 2: Document the System

Ensure system documentation is present/current, using `/document-app` when available.

Apply `shipping-artifacts` for architecture, flows, permissions, variables, and relevant conditional artifacts.

Classify each critical document:
`CURRENT | STALE | MISSING | NOT APPLICABLE | NOT ASSESSED`

Missing/stale critical intent limits intended-vs-implemented assurance. An upstream proposed architecture remains `PROPOSAL` until code/config evidence verifies implementation.

## Step 3: Reconcile PoC/Experiment Claims With Implemented Scope

For every material PoC/experiment claim:

| Claim ID | Upstream State | PoC Scope | Production-Relevant? | Implementation Match | New Evidence | Resulting State/Claim |

Check:
- representative population/data differences
- traffic/volume/concurrency differences
- production integrations/dependencies
- security/privacy boundaries
- human-review assumptions
- cost/latency differences
- failure/recovery paths
- monitoring/rollback
- operating ownership

Do not promote PoC scope to production scope. Create a new derived readiness claim when evidence supports one.

## Step 4: Agent Context

Create/refresh `CLAUDE.md` and thin `AGENTS.md` only from verified/current system intent.

Do not turn undocumented assumptions into authoritative agent instructions. Unknown boundaries remain explicit.

## Step 5: Security and Performance Review

Run the specialist audits independently when tooling permits.

### Security
Use `/security-audit-static` and preserve:
- declared scope
- coverage status
- findings
- uninspected areas
- runtime/configuration items not verifiable statically
- tool/subagent failures

### Performance
Use `/performance-audit-static` and preserve:
- declared scope
- coverage status
- static risks
- schema/index coverage
- runtime telemetry/profiling gaps
- tool/subagent failures

Do not downgrade coverage gaps while compiling the packet.

## Step 6: Derive Test-Coverage Map

Run `/derive-tests` or inspect available test evidence.

For each critical rule classify:
- `PINNED BY EXECUTED TEST`
- `EXISTING TEST - NOT EXECUTED/VERIFIED`
- `MANUAL / GUARDED LIVE`
- `PROPOSED TEST`
- `NO VERIFICATION`
- `BLOCKED BY SPEC GAP`

A test file existing is not proof it passes unless execution evidence is available.

Prioritize trust boundaries, irreversible side effects, data integrity, auth/tenancy, recovery, and critical business rules.

Link verification evidence to upstream or derived claim IDs when it changes readiness state.

## Step 7: Compile Coverage Before Readiness

Create one consolidated matrix:

| Area | Claim IDs | Coverage | Evidence | Unverified | Blocks readiness? |

Overall coverage:
- `COMPLETE FOR DECLARED SCOPE`: all material declared areas were inspectable and required evidence stages completed
- `PARTIAL`: some material areas/evidence remain uninspected or unverified
- `BLOCKED`: required evidence stage could not be performed or critical intent is unavailable

Coverage and finding severity are separate dimensions. A partial audit with zero findings is still partial.

## Step 8: Readiness Gate

Possible outcomes:

`READY FOR HUMAN REVIEW | CONDITIONAL | BLOCKED | NOT READY | COVERAGE INCOMPLETE`

### READY FOR HUMAN REVIEW
Requires all of:
- coverage complete for the declared scope
- critical intent documentation sufficiently current
- no unresolved Critical/High security findings
- no critical trust-boundary rule left both unaudited and unverified
- critical tests/verification evidence acceptable for the release consequence
- no material audit/tool failure hidden by synthesis
- no inherited PoC claim silently generalized beyond its tested scope
- production-readiness conclusions represented as explicit derived claims

This does **not** mean guaranteed safe. It means the evidence packet is sufficiently complete for a human release decision.

### CONDITIONAL
Evidence is substantial but named non-catastrophic gaps require explicit human acceptance or follow-up.

### BLOCKED / NOT READY
Use when critical findings, spec gaps, missing intent, failed required audits, inherited P0 blockers, or unverified high-consequence paths should stop release.

### COVERAGE INCOMPLETE
Use when the system may or may not be ready, but the evidence is insufficient to make the readiness call safely.

## Required Output

```text
## Shipping Readiness Packet: [declared scope]

### Overall Coverage
COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Inherited Claims
| Claim ID | Claim | State | Original Scope | Evidence | Restriction | Shipping Use |

### PoC -> Production Reconciliation
| Upstream Claim ID | PoC Scope | Production Difference | New Evidence | Derived Readiness Claim ID | State |

### Documentation Inventory
| Doc | Status | Notes / Gap |

### Test / Verification Coverage
| Critical Rule | Claim IDs | Verification State | Evidence | Gap |

### Security Review
Coverage: [...]
Audit status: [...]
Critical/High findings: [...]
Not verified statically: [...]

### Performance Review
Coverage: [...]
Audit status: [...]
Static risks: [...]
Runtime validation needed: [...]

### Derived Production-Readiness Claims
| Claim ID | Parent IDs | Derivation | State | Production Scope | Caveats |

### Coverage Gaps
[uninspected areas, tool failures, stale/missing docs, runtime unknowns]

### Launch Blockers
[evidence-backed blockers + claim IDs]

### Readiness Decision
READY FOR HUMAN REVIEW | CONDITIONAL | BLOCKED | NOT READY | COVERAGE INCOMPLETE

### Human Decision Required
[what the release owner must accept/decide]

### Recommended Next Actions
[highest-value evidence/actions in order]

## Reliability Handoff
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED
Unresolved P0: [claim IDs + evidence needed]
Prohibited interpretations: [PoC != production; ready-for-review != guaranteed safe; decision != evidence promotion]
```

## Final Self-Check

- Did any partial specialist result become a pass during synthesis?
- Did I call zero security findings "secure"?
- Did I call zero static performance findings "scalable"?
- Did I treat proposed tests as executed coverage?
- Did I preserve every tool/subagent failure?
- Is the readiness label scoped to exactly what was inspected?
- Did any PoC result become a production claim under the same claim ID?
- Did any `TARGET`/`PROPOSAL` become actual through implementation narrative?

The packet is evidence for human sign-off, not a substitute for it. Restating upstream evidence never strengthens it.
