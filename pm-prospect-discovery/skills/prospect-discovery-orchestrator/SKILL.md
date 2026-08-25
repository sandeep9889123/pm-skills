---
name: prospect-discovery-orchestrator
description: "Run fail-closed enterprise pre-RFP discovery from sparse prospect context through evidence, hypotheses, adaptive questioning, synthesis, and readiness gates. Use when a prospect opportunity needs repeatable solution discovery before proposal or RFP."
---

# Prospect Discovery Orchestrator

Use this skill when the team has a prospect, partial context, and a proposed problem or use-case path that must be validated before deeper commitment.

## Core principle

Discovery is a decision system, not questionnaire production.

The workflow is:

`Context -> Evidence -> Problem -> Alternatives -> Use-case hypothesis -> Red-team -> Journey -> Assumptions -> Questions -> Session -> Synthesis -> Readiness`

## Fail-closed operating rules

1. Never invent prospect facts, systems, APIs, volumes, budgets, timelines, stakeholder authority, data quality, or buying intent.
2. Treat sales language and the user's preferred use case as `ASSUMPTION` until supported.
3. Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE`.
4. A tool/search failure means `coverage incomplete / UNKNOWN`.
5. Do not let a polished workshop artifact create false confidence.
6. `WRONG USE CASE`, `SECOND DISCOVERY REQUIRED`, and `NOT READY` are valid outcomes.
7. Do not recommend architecture, estimate, or proposal commitment while unresolved P0 inputs can materially change scope or effort.
8. Every high-yield question must map to a decision: scope, value, architecture, data, integration, ownership, risk, economics, or next step.
9. Include the strongest disconfirming evidence and at least one credible alternative path.
10. A discovery confidence score cannot override a hard readiness gate.

## Minimum workflow

### Gate A: What decision must discovery enable?

State the next irreversible or costly decision. If the decision is unclear, define the likely one and mark it `ASSUMPTION`.

### Gate B: What do we know?

Build an evidence ledger. Do not convert public marketing claims into operational facts.

### Gate C: Are we solving the right problem?

Write a problem hypothesis and at least two alternative root causes.

### Gate D: Is the proposed wedge credible?

Compare 1-3 use-case options. If the preferred wedge is not best supported, reframe.

### Gate E: What must be true?

Create prioritized assumptions with consequence if false.

### Gate F: What should we ask?

Generate a short mandatory question set plus conditional branches. Avoid discovery theatre and generic lists.

### Gate G: What changed after the session?

Preserve contradictions. Unanswered items remain `UNKNOWN`.

### Gate H: Can we proceed?

Return explicit readiness for solutioning, architecture, estimation, business case, and proposal.

## Required decision output

Return one:

- `PROCEED TO SOLUTIONING`
- `PROCEED WITH CONDITIONS`
- `SECOND DISCOVERY REQUIRED`
- `REFRAME USE CASE`
- `STOP / NO-GO`

Always state what would change the recommendation.
