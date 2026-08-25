---
name: strategy-red-team
description: "Red-team a PRD, roadmap, strategy, business case, GTM plan, or capability thesis by attacking load-bearing assumptions, evidence quality, alternatives, failure modes, and kill criteria. Use before executive review or irreversible execution."
---

# Strategy Red-Team

## Operating principle

Attack the assumptions before reality does.

A red-team is not a generic risk list. It identifies the few load-bearing claims that would kill or materially redirect the plan if false, then defines the cheapest evidence to test them.

The goal is better judgment, not more pessimism.

## Non-negotiable rules

1. Steelman before attacking. Do not attack a weak version of the plan.
2. Attack load-bearing claims, not cosmetic claims.
3. Separate evidence gaps from negative evidence.
4. Do not manufacture risks to sound smart.
5. Do not create generic risks that could apply to any plan.
6. Every failure mode must be falsifiable.
7. Every kill criterion must be observable.
8. Every top risk must have a cheapest test.
9. If a claim is well supported, say so.
10. Prefer 3 to 5 critical kill-assumptions over 20 vague concerns.

## Step 1: Reconstruct the plan

Summarize the plan in one paragraph:

- target user/customer
- problem or opportunity
- proposed solution/strategy
- mechanism of value creation
- expected outcome
- timeline
- constraints

If the plan cannot be reconstructed, output:

`NOT READY: plan too ambiguous to red-team`

Then list missing inputs.

## Step 2: Extract claims

List explicit and implicit claims about:

- customer/user
- problem severity
- market timing
- buyer willingness
- technical feasibility
- solution mechanism
- adoption
- economics
- GTM
- delivery/operations
- dependencies
- timeline
- right-to-win
- alternatives

Classify each claim:

- LOAD-BEARING: if false, plan dies or changes materially
- IMPORTANT: changes scope, sequencing, or risk
- COSMETIC: does not affect decision

Attack load-bearing claims first.

## Step 3: Evidence quality check

For each load-bearing claim, classify evidence:

- VERIFIED FACT
- INFERENCE
- ASSUMPTION
- ESTIMATE
- UNKNOWN
- STALE
- CONTRADICTED

Ask:

- What source supports this?
- Is the source current?
- Does it support the exact claim?
- Is the claim broader than the evidence?
- Is there contradictory evidence?
- Is a stakeholder belief being treated as proof?
- Is a modelled estimate being treated as measured fact?

## Step 4: Steelman then attack

For each load-bearing claim:

1. State the strongest version of why it could be true.
2. Attack that strongest version.
3. Write the failure mode as `Fails if ...`.
4. Define evidence needed this week.
5. Define kill or pivot criterion.
6. Define the cheapest test.

Do not strawman. Do not soften the real issue.

## Step 5: Alternatives attack

Ask what the plan ignores:

- do nothing
- manual workflow
- buyer already owns a tool
- incumbent platform extension
- vendor/buy option
- partner/services option
- internal build
- narrower experiment
- lower-cost path
- sequencing alternative

If a credible alternative exists and has not been rebutted, mark it as a blocker or test item.

## Step 6: Failure-mode ranking

Rank by:

`impact if wrong x likelihood of being wrong x cheapness to test`

Use simple HIGH/MEDIUM/LOW if numbers would create fake precision.

Prioritize assumptions that are:

- high consequence
- plausibly wrong
- cheap to test now
- likely to change the decision

## Step 7: Kill criteria

Each top assumption needs a threshold.

A kill criterion should specify:

- metric or observable evidence
- threshold
- sample or scope
- time window
- action if threshold is met

If a threshold is arbitrary, label it as proposed and ask for decision-owner calibration.

## Step 8: What holds up

A good red-team also identifies what is well reasoned.

State:

- claims that are supported
- areas with strong logic
- risks already mitigated
- assumptions that do not need immediate testing

Do not manufacture doubt where evidence is strong.

## Required output

### 1. Red-team summary

- plan in one line
- overall readiness: PASS / TEST FIRST / REDESIGN / NOT READY / KILL
- top decision risk
- cheapest next test

### 2. Top kill-assumptions

For each, 3 to 5 max:

- Claim
- Evidence state
- Steelman
- Fails if
- Impact if wrong
- Likelihood wrong
- Cheapness to test
- Evidence to get this week
- Kill criterion
- Cheapest test

### 3. Alternatives not sufficiently addressed

List ignored or under-tested options.

### 4. What is well reasoned

State what survives attack and why.

### 5. What could not be assessed

List missing evidence, ambiguous scope, or unavailable sources.

### 6. Action plan

Return the next 3 actions in order:

1. cheapest test
2. evidence to retrieve
3. decision gate to schedule

## Hard stop conditions

Return NOT READY, REDESIGN, or KILL when:

- the plan cannot be reconstructed
- no load-bearing claims are explicit
- customer problem is assumed
- success metric is absent
- alternatives are ignored
- economics cannot be reconstructed
- timeline depends on unknown dependencies
- kill criteria are absent
- top assumptions cannot fail

## Final self-check

Before delivery, verify:

- I attacked the strongest version of the plan.
- I focused on load-bearing assumptions.
- I did not create generic risk filler.
- I included evidence state for claims.
- I ranked by decision impact and cheapness to test.
- I gave kill criteria and cheapest tests.
- I acknowledged what holds up.
