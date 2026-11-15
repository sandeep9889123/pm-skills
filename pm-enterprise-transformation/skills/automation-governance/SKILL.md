---
name: automation-governance
description: "Design governance for AI agents and workflow automations: permissions, human review, audit logs, monitoring, rollback, ownership, incident handling, data boundaries, and release gates. Use before moving business-critical automation from prototype to production."
---

# Automation Governance

## Purpose

Make automation accountable. A workflow is not production-ready because it works in a demo; it is ready when actions are bounded, observable, recoverable, owned, and tested against harmful failure modes.

## Governance model

1. **Action inventory**
   List every read, write, send, approve, delete, publish, purchase, schedule, modify, or external side effect the automation can perform.

2. **Risk classification**
   For each action assess data sensitivity, monetary impact, customer impact, reversibility, blast radius, legal/compliance consequence, and detectability of failure.

3. **Permission design**
   Apply least privilege. Separate read from write. Scope by tenant/account/project. Avoid shared broad credentials. Define credential rotation and secret handling.

4. **Human-in-the-loop policy**
   Decide whether each action is `AUTO`, `REVIEW-SAMPLED`, `APPROVAL-REQUIRED`, or `HUMAN-ONLY` based on consequence, uncertainty, and reversibility.

5. **Validation before action**
   Define schema checks, business rules, confidence/quality gates, duplicate detection, target verification, and precondition checks.

6. **Observability**
   Log trigger, inputs/references, decision, tool call, result, validation, approver, exception, and final state. Monitor success, silent failure, retries, cost, latency, human overrides, and drift.

7. **Failure handling**
   Define timeout, retry limits, idempotency, dead-letter/manual queue, rollback/compensating action, escalation, kill switch, and incident owner.

8. **Release gates**
   Use offline tests → sandbox → shadow mode → limited cohort → broader rollout. High average success cannot override a catastrophic hard-gate failure.

## Red-team scenarios

- wrong customer/account selected;
- prompt/input injection tries to alter operating rules;
- duplicate retry creates repeated external action;
- partial tool failure creates inconsistent state;
- user permission changes after context was cached;
- automation sends confidential content externally;
- model fabricates completion despite tool failure;
- human review becomes rubber-stamping;
- cost/latency degrades enough to erase ROI.

## Output

### Control matrix
| Action | Risk | Permission | Validation | HITL | Monitoring | Rollback | Owner |
|---|---|---|---|---|---|---|---|

### Release decision
`PRODUCTION READY | LIMITED PILOT | SHADOW ONLY | BLOCKED`.

List blocking controls, evidence required, incident owner, and kill-switch procedure.

## AI quality evidence and operational learning

Correlate task/run/trace and parent/child span IDs across model, retrieval, tool, router, review and final verification. Record safe metadata, versions, authorization, retry/idempotency, measured latency and known costs; minimize sensitive payloads and define retention/access. Verify propagation with an authorized trace before relying on logs.

Use representative review sampling plus separately reported targeted-risk cases. Define human-label authority, grader calibration, unjudgeable cases, drift investigation, feedback-to-regression, incident timeline and verified recovery. Preserve raw evidence and versions; distinguish model/prompt/corpus/tool defects from telemetry gaps. Do not infer population failure rates from complaints. A stronger average score cannot erase an unauthorized action, cross-tenant leak or false completion. Stop or escalate only within approved authority, with an accountable owner for unresolved controls.
