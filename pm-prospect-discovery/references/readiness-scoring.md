# Discovery Readiness Scoring

## Purpose

Communicate evidence maturity without hiding hard blockers.

## Confidence dimensions

Score each 0-10:

- problem validation
- user/buyer validation
- workflow understanding
- business value
- systems/integration clarity
- data clarity
- scope clarity
- dependency/ownership clarity
- success metric clarity
- stakeholder alignment

The total can be shown as 0-100.

## Interpretation

- 80-100: high evidence maturity, subject to hard gates
- 60-79: usable but conditional
- 40-59: material gaps, targeted second discovery likely
- below 40: weak foundation, reframe or broaden discovery

These ranges are guidance, not statistical confidence intervals.

## Hard-gate precedence

Regardless of total score, block the relevant next step if unresolved P0 items can materially change scope, architecture, effort, security, economics, or commercial commitment.

A score of 90/100 with unknown integration access can still be `NOT READY FOR ESTIMATION`.

## Readiness matrix

Assess independently:

| Gate | Typical minimum evidence |
|---|---|
| Solutioning | validated problem, users, workflow, major constraints |
| Architecture | systems, integration, data, security boundaries |
| Estimation | stable Phase 1 scope, dependencies, ownership, acceptance |
| Business case | value drivers, alternatives, cost/benefit inputs, buyer context |
| Proposal | solution path, scope, exclusions, dependencies, commercial inputs |

Always explain blockers and evidence needed.
