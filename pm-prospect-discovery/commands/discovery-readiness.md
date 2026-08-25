---
description: "Assess whether enterprise prospect discovery evidence is sufficient for solutioning, architecture, estimation, business case, and proposal, with hard blockers and explicit next evidence."
argument-hint: "[discovery pack, session notes, synthesis, assumptions, dependencies]"
---

# Discovery Readiness

Assess:

$ARGUMENTS

Use proposal-readiness and discovery-red-team.

Return a gate matrix:

- READY FOR SOLUTIONING
- READY FOR ARCHITECTURE
- READY FOR ESTIMATION
- READY FOR BUSINESS CASE
- READY FOR PROPOSAL
- SECOND DISCOVERY REQUIRED

Each gate must be `YES | NO | CONDITIONAL`.

## Hard rule

No gate may be YES when an unresolved P0 item can materially change the decision being gated.

Do not estimate around missing P0 evidence by silently inserting assumptions.

Include:

- discovery confidence 0-100
- dimension scores
- blockers
- evidence required
- owner if known
- strongest rejection case
- what evidence would change the recommendation
