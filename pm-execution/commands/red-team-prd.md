---
description: Red-team a PRD, roadmap, or strategy by testing load-bearing assumptions, evidence, alternatives, and falsifiable decision gates without manufacturing objections
argument-hint: "<PRD, roadmap, strategy, or the current doc>"
---

# /red-team-prd - Evidence-Calibrated Red Team

Use this workflow to challenge a plan before commitment. The objective is decision quality, not a predetermined negative verdict.

## Workflow

### Step 1: Accept and Reconstruct the Plan

Take the PRD, roadmap, strategy memo, business case, one-line bet, or current document in context.

State the decision, target actor, problem, mechanism, outcome, stage, constraints, and dependencies. If these cannot be reconstructed, return `NOT READY` with the missing inputs.

### Step 2: Apply `strategy-red-team`

Mandatory behavior:
- extract load-bearing claims only
- preserve `FACT | INFERENCE | ASSUMPTION | ESTIMATE | UNKNOWN | STALE | TARGET | PROPOSAL`
- distinguish `NEGATIVE EVIDENCE` from `EVIDENCE GAP`
- steelman before attacking
- do not default to "the risk is real"
- do not manufacture weaknesses to fill a quota
- acknowledge `HOLDS UNDER CURRENT EVIDENCE` when appropriate
- compare credible alternatives including current state / do nothing when decision-relevant
- use proposed thresholds only when owner-approved thresholds do not exist

### Step 3: Return Decision-Focused Output

```text
## Red-Team: [decision / plan]

### Readiness
PASS | TEST FIRST | REDESIGN | NOT READY | KILL

### Load-Bearing Claims
| Claim | Evidence State | Evidence For | Evidence Against | Coverage Gap | Impact |

### Surviving Risks
For each material risk only:
- Claim
- Challenge type: NEGATIVE EVIDENCE | EVIDENCE GAP | ALTERNATIVE EXPLANATION
- Steelman
- Evidence-based challenge
- Fails if
- Cheapest credible test
- Proposed decision gate

### Credible Alternatives
[Only alternatives that could change the decision]

### What Holds Up
[Supported claims and mitigated risks]

### What Could Not Be Assessed
[Missing/stale/unavailable evidence]

### What Would Change the Recommendation
[Specific evidence]
```

Do not force 3-5 risks. Zero material objections is a valid result when evidence is strong.

### Step 4: Follow-On Action

Offer the next highest-value action only when useful, such as:
- convert one unresolved claim into a falsifiable experiment
- retrieve missing evidence
- revise the plan around a surviving blocker
- run a pre-mortem for operational failure-path exploration

## Notes

- Missing evidence is not proof that a claim is false.
- A red-team that always finds fatal flaws is as unreliable as one that never challenges anything.
- Preserve supported claims so strong decisions do not get endlessly reopened without new evidence.
