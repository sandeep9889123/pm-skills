---
name: proposal-readiness
description: "Gate enterprise prospect opportunities for solutioning, architecture, estimation, business case, and proposal based on discovery evidence. Use when deciding whether a pre-RFP opportunity is mature enough for the next commitment."
---

# Proposal Readiness

Readiness is not one binary state.

## Gates

Assess each independently:

- `READY FOR SOLUTIONING`
- `READY FOR ARCHITECTURE`
- `READY FOR ESTIMATION`
- `READY FOR BUSINESS CASE`
- `READY FOR PROPOSAL`
- `SECOND DISCOVERY REQUIRED`

Allowed result:

`YES | NO | CONDITIONAL`

## Hard blockers

A gate must not be `YES` when an unresolved P0 item can materially change:

- use-case viability
- Phase 1 scope
- architecture
- integration approach
- required data
- security/compliance
- delivery effort
- timeline
- ownership
- economics
- commercial commitment

Do not estimate around missing P0 inputs by quietly inserting assumptions.

## Discovery confidence

Score 0-10 for:

1. problem validation
2. user / buyer validation
3. workflow understanding
4. business value
5. systems / integration clarity
6. data clarity
7. scope clarity
8. dependency / ownership clarity
9. success metric clarity
10. stakeholder alignment

Convert to 0-100 only as a communication aid.

A high score cannot override a hard gate.

## Decision states

Return one:

- `PROCEED TO SOLUTIONING`
- `PROCEED WITH CONDITIONS`
- `SECOND DISCOVERY REQUIRED`
- `REFRAME USE CASE`
- `STOP / NO-GO`

## Required explanation

For every `NO` or `CONDITIONAL` gate state:

- blocker
- consequence
- evidence required
- owner if known
- what changes when resolved

Always state what evidence would change the overall recommendation.
