---
description: Compile a reviewer-ready shipping-readiness packet from documentation, test coverage, security review, performance review, and explicit coverage gaps
argument-hint: "<repo path or area; defaults to the whole repository>"
---

# /ship-check - Shipping Readiness Review

This workflow answers a narrower and more defensible question than "is this safe?":

> **What evidence do we have for shipping readiness, what remains unverified, and what should block release?**

It coordinates documentation, static audits, and test evidence into a packet for human decision. It does not certify security, scalability, or production safety.

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

## Invocation

```text
/ship-check
/ship-check the payments service
/ship-check supabase/functions
```

## Step 1: Declare the Shipping Scope

State exactly what is being evaluated:
- repository / service / module / feature
- intended environment/release if known
- included and excluded areas
- evidence sources available

If the user requests the whole repo but material areas cannot be inspected, the final coverage cannot be `COMPLETE FOR DECLARED SCOPE`.

## Step 2: Document the System

Ensure system documentation is present/current, using `/document-app` when available.

Apply `shipping-artifacts` for architecture, flows, permissions, variables, and relevant conditional artifacts.

Classify each critical document:
`CURRENT | STALE | MISSING | NOT APPLICABLE | NOT ASSESSED`

Missing/stale critical intent limits intended-vs-implemented assurance.

## Step 3: Agent Context

Create/refresh `CLAUDE.md` and thin `AGENTS.md` only from verified/current system intent.

Do not turn undocumented assumptions into authoritative agent instructions. Unknown boundaries remain explicit.

## Step 4: Security and Performance Review

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

## Step 5: Derive Test-Coverage Map

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

## Step 6: Compile Coverage Before Readiness

Create one consolidated matrix:

| Area | Coverage | Evidence | Unverified | Blocks readiness? |
|---|---|---|---|---|

Overall coverage:
- `COMPLETE FOR DECLARED SCOPE`: all material declared areas were inspectable and required evidence stages completed
- `PARTIAL`: some material areas/evidence remain uninspected or unverified
- `BLOCKED`: required evidence stage could not be performed or critical intent is unavailable

Coverage and finding severity are separate dimensions. A partial audit with zero findings is still partial.

## Step 7: Readiness Gate

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

This does **not** mean guaranteed safe. It means the evidence packet is sufficiently complete for a human release decision.

### CONDITIONAL
Evidence is substantial but named non-catastrophic gaps require explicit human acceptance or follow-up.

### BLOCKED / NOT READY
Use when critical findings, spec gaps, missing intent, failed required audits, or unverified high-consequence paths should stop release.

### COVERAGE INCOMPLETE
Use when the system may or may not be ready, but the evidence is insufficient to make the readiness call safely.

## Required Output

```text
## Shipping Readiness Packet: [declared scope]

### Overall Coverage
COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Documentation Inventory
| Doc | Status | Notes / Gap |

### Agent Context
[created/updated/current + any unknown boundaries]

### Test / Verification Coverage
| Critical Rule | Verification State | Evidence | Gap |

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

### Coverage Gaps
[uninspected areas, tool failures, stale/missing docs, runtime unknowns]

### Launch Blockers
[only evidence-backed blockers]

### Readiness Decision
READY FOR HUMAN REVIEW | CONDITIONAL | BLOCKED | NOT READY | COVERAGE INCOMPLETE

### Human Decision Required
[what the release owner must accept/decide]

### Recommended Next Actions
[highest-value evidence/actions in order]
```

## Final Self-Check

- Did any partial specialist result become a pass during synthesis?
- Did I call zero security findings "secure"?
- Did I call zero static performance findings "scalable"?
- Did I treat proposed tests as executed coverage?
- Did I preserve every tool/subagent failure?
- Is the readiness label scoped to exactly what was inspected?

The packet is evidence for human sign-off, not a substitute for it.
