---
name: discovery-question-engine
description: "Generate adaptive, decision-linked enterprise discovery questions from a stable taxonomy. Use when preparing a prospect session and you need a concise must-ask set plus conditional deeper questions rather than a generic questionnaire dump."
---

# Discovery Question Engine

The objective is not maximum coverage. The objective is minimum sufficient evidence for the next decision.

## Enterprise taxonomy

Generate questions across relevant dimensions:

1. business trigger
2. user / buyer / operator
3. current workflow
4. pain and failure modes
5. volume / frequency / scale
6. economics / cost of current state
7. systems / architecture
8. data / quality / access
9. integrations / APIs / files / manual handoffs
10. business rules / exceptions
11. security / privacy / compliance
12. ownership / operating model
13. buying / decision process
14. success metrics / acceptance
15. constraints / budget / timeline / dependencies
16. future state / reuse

Not every session needs every category.

## Question quality rules

- Ask about current or past behavior before hypothetical preference.
- Do not embed the desired answer.
- Do not ask a question unless its answer can change a material decision.
- Prefer specific walk-through questions over "Do you have challenges with X?"
- Separate `MUST ASK` from `LEVEL 2`.
- Include explicit disconfirming questions.
- Map every MUST ASK question to one or more decisions.
- Avoid asking for details already present in authoritative supplied evidence.
- Do not ask the same information in multiple forms unless contradiction checking is intentional.

## Adaptive branching

Use conditional logic.

Examples:

- If API access is confirmed, explore authentication, limits, ownership, eventing, and write boundaries.
- If API access is absent, pivot to files, database views, middleware, manual handoffs, or vendor change.
- If volumes are low, challenge the automation ROI.
- If rules require frequent human judgment, explore HITL instead of assuming full automation.
- If data quality is poor, challenge downstream AI/automation feasibility.
- If buyer urgency is high but user pain is weak, separate buying trigger from product value.
- If security or regulation is material, expand access, residency, audit, and approval questions.
- If a critical answer is unknown to attendees, capture owner and follow-up evidence rather than guessing.

## Session sizing

For a 60-90 minute session, target roughly 15-25 MUST ASK questions, then conditional Level 2 questions.

This is guidance, not a quota.

## Hard guard

A beautifully written questionnaire fails if it only confirms the preferred solution.

Every pack must include at least:

- one root-cause challenge
- one existing-solution / substitute challenge
- one value / urgency challenge
- one dependency challenge
- one success-definition challenge

## Output

For each question include:

- question
- why it matters
- decision affected
- branch condition, if any
