---
description: Convert a verified business case and evidence ledger into a gated investment committee decision with staged commitment and explicit blockers
argument-hint: "<business case and evidence ledger>"
---

# /business-case-decision

Make an investment decision for `$ARGUMENTS` using evidence, not narrative quality.

## Required local skills

Apply:

1. **business-case-orchestrator** skill
2. **evidence-ledger** skill
3. **investment-red-team** skill
4. **economics-commercial-proof** skill

## Preconditions

Prefer an existing `evidence-ledger.json` and business case.

If no ledger exists, build the minimum P0 ledger before deciding.

Do not use model memory to fill missing decision-critical evidence.

## Step 1: Validate evidence

When execution is available run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

If the ledger fails, do not issue BUILD, BUY, or PARTNER.

## Step 2: Identify decision drivers

List no more than the decision-critical drivers:

- customer problem
- why now
- alternatives
- right-to-win
- feasibility
- economics
- WTP/commercial proof
- GTM path
- reuse/platform proof where relevant

Map every driver to claim IDs.

## Step 3: Check gates G0-G6

For each gate return PASS, FAIL, or NOT READY.

Do not average gates into a score that can hide a P0 failure.

A single unresolved P0 blocker can prevent an irreversible investment decision.

## Step 4: Re-run strongest rejection case

Before deciding, state the best case for rejecting the proposal now and the evidence that would reverse that rejection.

## Step 5: Compare strategic options

Evaluate:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

Ensure DO NOTHING/current-state economics are represented inside the comparison even though it is not a final status label.

Do not favor BUILD because engineering work has already started.

## Step 6: Choose staged commitment

When uncertainty remains but evidence generation is valuable, prefer EXPERIMENT with explicit:

- hypothesis
- investment ceiling
- evidence to collect
- metric
- decision threshold
- kill criterion
- next decision point

Do not approve a full platform roadmap when only a PoC is justified.

## Step 7: Final decision

Allowed final decisions only:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

For BUILD, BUY, or PARTNER:

- all P0 blockers must be resolved;
- evidence validator should pass where executable;
- strongest rejection case must be rebutted by evidence;
- economics must be reconstructable;
- alternatives must be explicitly compared.

## Output

### Investment committee decision

- Decision
- Readiness
- Capital/effort requested
- Why this option wins
- P0 claim IDs supporting decision
- P0 blockers
- Strongest rejection case
- What would change the decision
- Kill criteria
- Next irreversible decision

### Gate table

G0-G6 with status and claim IDs.

### Option table

BUILD, BUY, PARTNER, current state/do nothing, and other relevant alternatives with evidence-backed trade-offs.

### Staged commitment

What is approved now versus explicitly not approved yet.

## Fail-closed rule

If evidence is insufficient, `NOT READY` is a valid and preferred outcome over false precision.
