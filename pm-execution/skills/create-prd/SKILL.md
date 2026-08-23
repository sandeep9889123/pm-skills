---
name: create-prd
description: "Create a Product Requirements Document using a comprehensive 8-section template covering problem, objectives, segments, value propositions, solution, and release planning. Use when writing a PRD, documenting product requirements, preparing a feature spec, or reviewing an existing PRD."
---

# Create a Product Requirements Document

## Purpose

Create a PRD that records the product decision and the evidence behind it, not merely a polished specification.

## Context

A strong PRD aligns product, design, engineering, data, delivery, GTM, and leadership on the problem, scope, behavior, quality bar, risks, and what remains unproven.

## Instructions

1. **Gather Information**: If the user provides files, read them carefully. If they mention research, URLs, customer data, or existing systems, gather relevant context before writing.

2. **Decision-first framing**: Before solution detail, state:
   - What decision are we making?
   - What user/business problem is supported by evidence?
   - Why now?
   - What alternatives exist, including doing nothing?
   - What assumptions remain unproven?

3. **Apply the PRD Template**:

### 1. Executive Summary
What, for whom, why now, intended outcome, and current confidence.

### 2. Contacts / Ownership
Decision owner, product owner, design, engineering, data/AI, delivery/QA, GTM/support, and approvers as applicable.

### 3. Background & Evidence
- observed problem and evidence
- current workflow/alternative
- frequency/severity
- prior attempts
- relevant research/market/context
- evidence gaps

Label load-bearing claims `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, or `STALE`.

### 4. Objective & Success Contract
- customer outcome
- business outcome
- product/operational metrics
- baseline if known
- target/range
- guardrails
- measurement method and owner

Do not invent baselines or targets. If unknown, define how they will be established.

### 5. Target Users / Segments / JTBD
- primary user/buyer
- job/context
- eligibility and exclusions
- user versus buyer differences
- accessibility/localization or enterprise constraints where relevant

### 6. Scope and Requirements
Separate:
- `P0 Must Have`
- `P1 Should Have`
- `P2 Later/Optional`
- `Non-goals`

For each P0 requirement include acceptance criteria plus failure/edge cases.

### 7. Solution & Decision Log
- proposed experience/workflow
- key product decisions and rationale
- alternatives rejected and why
- dependencies/integrations/data
- permissions/privacy/security
- AI behavior/evaluation/HITL when applicable
- analytics/instrumentation
- operational/support requirements

### 8. Release / Validation Plan
- smallest releasable/testable version
- rollout cohort
- pre-launch gates
- experiment/evaluation plan
- rollback or disable path
- unresolved questions
- revisit triggers

## Reliability and Scope Gate

Before finalizing:

- Do not convert a solution request into a validated problem.
- If evidence for the problem is weak, label the PRD `DISCOVERY / HYPOTHESIS`, not implementation-ready.
- Every P0 item must trace to a user/business outcome, hard constraint, or risk. Remove orphan requirements.
- Include unhappy paths, permissions, empty states, recovery, interruption, data failure, integration failure, and abuse/misuse scenarios when relevant.
- Separate **desired behavior** from **implementation suggestion** unless the technology choice is itself a product constraint.
- State what is deliberately not built and why.
- For AI features, define dataset/evaluation, hard gates, confidence/uncertainty behavior, human review, cost/latency, safety/privacy, and rollback. Model accuracy alone is not acceptance.
- For enterprise products, include buyer/admin/user roles, implementation, security/procurement dependencies, auditability, and sales-to-delivery assumptions when relevant.
- Avoid date certainty when dependencies/evidence do not support it.

## Final Decision Block

```text
Status: DISCOVERY | READY FOR DESIGN | READY FOR BUILD | BLOCKED
Decision:
Strongest evidence:
Top assumptions:
P0 hard gates:
Key trade-offs:
What would change scope/decision:
Owner:
```

Use accessible language. Save substantial output as `PRD-[product-name].md`.

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
