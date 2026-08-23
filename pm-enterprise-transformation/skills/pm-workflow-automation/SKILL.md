---
name: pm-workflow-automation
description: "Assess and design automation for PM, research, solution, sales, and operating workflows using workflow decomposition, automation suitability, HITL controls, value, failure cost, and measurable pilot gates. Use when deciding what PM work to automate with AI, agents, scripts, or integrations."
---

# PM Workflow Automation

## Purpose

Identify where automation creates net value without hiding ambiguity, amplifying bad inputs, or removing human judgment from high-consequence decisions.

## Step 1: Map the current workflow

For each step capture:
- trigger/input
- actor
- action/decision
- tools/data
- output
- handoff
- exception paths
- cycle time/effort
- error/rework rate if known

Do not automate a process that has not been understood.

## Step 2: Classify each step

- `DETERMINISTIC`: explicit rules, stable inputs
- `ASSISTIVE`: AI can draft/summarize/rank but human owns decision
- `REVIEW-GATED`: automation may act only after approval
- `AUTONOMOUS-CANDIDATE`: bounded action with observable success and cheap rollback
- `HUMAN-ONLY`: negotiation, sensitive judgment, irreversible/high-consequence decision, ambiguous accountability

## Step 3: Score automation suitability

Assess volume, repetitiveness, input quality, rule stability, tool/API availability, observability, exception rate, reversibility, failure cost, privacy/security, latency need, and human review burden.

High frequency does not justify automation when failure is expensive or invisible.

## Step 4: Design future state

Specify:
`trigger → context retrieval → reasoning/rules → tool action → validation → human gate → output → audit log → failure/rollback`.

Define idempotency, permissions, retry policy, escalation, timeout, and data retention where relevant.

## Step 5: Economics

Estimate baseline human effort/cost, automation build/maintenance, review effort, tool/model/API cost, expected error cost, and recovered capacity. Use ranges and sensitivity analysis.

## Step 6: Pilot

Start with shadow mode or assistive mode when uncertainty is high. Define golden examples, acceptance metrics, false-positive/false-negative costs, review sample, stop conditions, and owner.

## Edge cases

- automation speeds up creation but increases review burden;
- workflow changes frequently, making automation brittle;
- model confidence is high on incorrect output;
- tool/API partial failure leaves inconsistent state;
- permissions allow cross-account/client leakage;
- human reviewers rubber-stamp because automation appears authoritative;
- success metric measures tasks completed instead of business outcome.

## Output

### Automation map
| Step | Current pain | Classification | Suitability | Failure cost | Control | Expected value |
|---|---|---|---|---|---|---|

### Future-state design
Include HITL, monitoring, auditability, rollback, ownership.

### Decision
`AUTOMATE | ASSIST | PILOT IN SHADOW MODE | REDESIGN PROCESS FIRST | DO NOT AUTOMATE`.
