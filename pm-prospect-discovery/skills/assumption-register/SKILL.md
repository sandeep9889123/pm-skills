---
name: assumption-register
description: "Create and maintain a prioritized assumption register for pre-RFP prospect discovery. Use when solution, scope, data, integration, user, commercial, or ownership beliefs must be explicitly validated before commitment."
---

# Assumption Register

Make hidden beliefs visible before they become scope.

## Assumption classes

- problem
- user / buyer
- workflow
- volume
- value / economics
- data
- system / integration
- business rule
- security / compliance
- ownership
- delivery
- commercial
- phase / scope

## Record format

Each assumption needs:

- ID
- statement
- class
- evidence state
- consequence if false
- uncertainty
- decision affected
- validation method / question
- owner for follow-up
- status

Allowed status:

`UNTESTED | CONFIRMED | DENIED | PARTIAL | UNKNOWN`

## Prioritization

Prioritize by consequence x uncertainty.

A highly uncertain assumption with low consequence may wait.

A P0 assumption is one that can materially change:

- whether the use case is viable
- architecture
- implementation effort
- timeline
- security/compliance
- commercial viability
- ownership
- Phase 1 scope

## Guardrails

Do not mark an assumption `CONFIRMED` because a model finds it plausible.

Do not collapse `PARTIAL` into `CONFIRMED`.

If the person answering lacks authority or knowledge, preserve the status and capture a follow-up owner.

## Output

Lead with P0 assumptions, then P1/P2.
