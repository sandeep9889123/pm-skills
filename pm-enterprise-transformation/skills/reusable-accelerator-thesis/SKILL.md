---
name: reusable-accelerator-thesis
description: "Decide whether repeated delivery work should remain bespoke, become a reusable accelerator, become a productized solution, or evolve into a platform capability. Use when evaluating reusable IP, internal accelerators, solution factories, or platformization opportunities."
---

# Reusable Accelerator Thesis

## Purpose

Turn repeated delivery work into a falsifiable reuse thesis. The goal is not to label existing code as IP. The goal is to prove that reuse lowers delivery time, cost, risk, or improves sales conversion across multiple contexts.

## Required evidence

Inventory:
- repeated use cases and their variation
- common versus client-specific components
- delivery effort by stage
- recurring defects/rework
- integration/data dependencies
- security/compliance variation
- existing code/assets and maintainability
- buyer value and willingness-to-pay signals
- alternative products/platforms

Mark evidence as `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, or `STALE`.

## Decision tests

Evaluate:

1. **Repeatability**: does the same job recur across independent customers?
2. **Common-core ratio**: how much of the solution is genuinely reusable?
3. **Configuration boundary**: can differences be configuration/rules rather than forks?
4. **Economics**: does reuse improve margin, cycle time, quality, or pre-sales effort enough to justify maintenance?
5. **Adoption**: will delivery/sales teams actually use the accelerator?
6. **Differentiation**: does it create a meaningful advantage or merely recreate commodity functionality?
7. **Lifecycle cost**: versioning, support, security, documentation, testing, compatibility, ownership.
8. **Platform trap**: are we prematurely building abstractions before three or more validated reuse patterns exist?

## Contradiction pass

Actively look for evidence that:
- client-specific variation dominates;
- open-source/vendor options are cheaper or safer;
- reuse shifts cost from delivery to maintenance without net value;
- buyers do not value the reusable layer;
- the asset depends on one client’s data/process;
- internal teams will bypass it.

## Output

### Reuse map
| Component/workflow | Common | Variable | Reuse evidence | Maintenance cost | Recommended boundary |
|---|---|---|---|---|---|

### Options
Compare `BESPOKE`, `METHOD`, `ACCELERATOR`, `PRODUCTIZED SOLUTION`, `PLATFORM`, `BUY/PARTNER`.

### Thesis
Write one falsifiable statement:

> If we standardize [common core] and configure [variation], then across [target contexts] we expect [measurable improvement] without exceeding [maintenance/customization limit].

### Pilot gates
Define baseline, target, test accounts/use cases, owner, duration, and stop conditions.

### Decision
`INVEST | PILOT | KEEP BESPOKE | BUY/PARTNER | HOLD`

Never claim reusable IP until reuse has been demonstrated beyond the originating project.
