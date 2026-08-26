---
name: strategy-red-team
description: "Red-team a PRD, roadmap, strategy, business case, GTM plan, or capability thesis by testing load-bearing assumptions, evidence quality, alternatives, failure modes, and decision gates without manufacturing objections. Use before executive review or irreversible execution."
---

# Strategy Red-Team

## Operating principle

Attack the assumptions before reality does, but do not confuse skepticism with quality.

A red-team is not a generic risk list and not a pessimism generator. It identifies the few load-bearing claims that could materially change the decision if false, evaluates the evidence for and against them, and defines the cheapest credible test where uncertainty remains.

## P0 Reliability Contract

1. Steelman before attacking. Do not attack a weak version of the plan.
2. Separate `NEGATIVE EVIDENCE` from `EVIDENCE GAP`. Missing evidence is not evidence the claim is false.
3. Do not manufacture objections, failure modes, or alternatives merely to make the red-team look rigorous.
4. If a load-bearing claim is strongly supported, say `HOLDS UNDER CURRENT EVIDENCE` and move on.
5. Preserve `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`, `TARGET`, and `PROPOSAL` where relevant.
6. Every surviving failure mode must be tied to a load-bearing mechanism and be falsifiable.
7. Every kill/pivot criterion must be observable and labelled `PROPOSED` if not owner-approved.
8. Do not force 3-5 risks. Return the number of material risks the evidence supports, including zero when appropriate.
9. Compare credible alternatives including `DO NOTHING/current state` when they could change the decision.
10. `PASS` is a legitimate outcome. A strong plan should not be downgraded to justify the exercise.

## Step 1: Reconstruct the Decision

State:
- decision being made
- target user/customer/buyer
- problem/opportunity
- proposed strategy/solution
- mechanism of value creation
- expected outcome
- timing/stage
- constraints and dependencies

If the decision cannot be reconstructed, return:

`NOT READY: decision or plan too ambiguous to red-team`

List the missing inputs rather than inventing them.

## Step 2: Extract Load-Bearing Claims

Capture explicit and implicit claims about:
- customer/problem
- market/timing
- buyer willingness
- technical feasibility
- mechanism of value
- adoption
- economics
- GTM
- operations/delivery
- dependencies
- right-to-win
- alternatives

Classify:
- `LOAD-BEARING`: false changes or kills the decision
- `IMPORTANT`: changes scope/sequencing/risk
- `COSMETIC`: does not change the decision

Do not attack cosmetic claims for volume.

## Step 3: Evidence Integrity

For each load-bearing claim capture:

| Claim | State | Evidence for | Evidence against | Coverage gap | Freshness |
|---|---|---|---|---|---|

Ask:
- Does the source support the exact claim?
- Is the claim broader than the sample/scope?
- Is evidence current?
- Is a stakeholder belief or target being treated as fact?
- Is an estimate being treated as measured performance?
- Is contradictory evidence being ignored?

## Step 4: Steelman and Test

For each material unresolved claim:
1. State the strongest case that it is true.
2. State the strongest evidence-based challenge.
3. Classify the challenge as `NEGATIVE EVIDENCE`, `EVIDENCE GAP`, or `ALTERNATIVE EXPLANATION`.
4. Write `Fails if ...` only when the mechanism is specific enough to falsify.
5. Define the cheapest credible evidence to obtain next.
6. Define a proposed decision threshold when one is needed.

Do not start from "the risk is real." Start from the evidence state.

## Step 5: Alternatives Attack

Consider only credible alternatives that could change the decision:
- current state / do nothing
- manual workflow
- existing owned tool or configuration
- incumbent extension
- buy/vendor
- partner/services
- internal build
- narrower experiment
- different sequence

For each alternative state why it is or is not credible. Do not invent a substitute to populate the section.

## Step 6: Rank Decision Risks

Rank by decision impact, uncertainty, and value of information.

Use qualitative levels if numeric scoring would create false precision.

Prioritize risks that are:
- high consequence if wrong
- materially uncertain or contradicted
- testable before commitment
- likely to change the recommendation

## Step 7: Decision Gates

For each top unresolved risk specify:
- observable signal/metric
- proposed threshold if needed
- scope/sample/time window where relevant
- action if threshold is crossed
- decision owner if known

Unapproved thresholds remain `PROPOSED DECISION THRESHOLD`.

## Step 8: What Holds Up

Explicitly identify:
- claims supported by strong evidence
- mitigated risks
- assumptions that no longer deserve priority
- areas that should not be reopened without new evidence

This prevents red-team theatre and endless re-litigation.

## Required Output

### Decision summary
- decision in one line
- readiness: `PASS | TEST FIRST | REDESIGN | NOT READY | KILL`
- highest material uncertainty, if any
- best next evidence action

### Load-bearing claim table
[claim, evidence state, evidence for/against, decision impact]

### Surviving risks
For each material risk:
- claim
- challenge type
- steelman
- evidence-based challenge
- `Fails if`
- cheapest credible test
- proposed threshold / gate

### Credible alternatives
[only those that could change the decision]

### What holds up
[state what survives and why]

### What could not be assessed
[missing/stale/unavailable evidence]

### Decision and change-my-mind evidence
[state what evidence would upgrade/downgrade the recommendation]

## Hard Stops

Return `NOT READY`, `REDESIGN`, or `KILL` when the evidence supports those outcomes, for example:
- decision cannot be reconstructed
- core customer/problem is unsupported and commitment is irreversible
- critical economics/dependency is unknowable before commitment
- a credible alternative dominates and is not addressed
- contradicted evidence invalidates the mechanism

Do not hard-stop merely because a template field is blank.

## Final Self-Check

- Did I distinguish evidence gap from evidence against?
- Did I attack the strongest version?
- Did I avoid generic risk filler?
- Did I preserve claim states?
- Did I acknowledge what holds up?
- Would every surviving objection change a material decision?
- Could `PASS` have been returned if the plan genuinely held up?
