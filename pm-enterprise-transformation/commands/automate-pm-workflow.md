---
description: Redesign and automate a PM, research, solution, or sales workflow with tool selection, HITL controls, governance, and measurable rollout gates
argument-hint: "<workflow, recurring task, process, or automation idea>"
---

# /automate-pm-workflow

Automate the right part of the workflow, with measurable value and bounded failure.

## Workflow

### 1. Map current state
Apply **pm-workflow-automation**:
- trigger/input
- actor and decision
- tools/data
- handoffs and exceptions
- time/rework/error baseline

Classify steps as deterministic, assistive, review-gated, autonomous candidate, or human-only.

### 2. Redesign before tooling
Remove unnecessary approvals, duplicated entry, low-value reports, and ambiguous ownership before automating them. Do not automate waste.

### 3. Decide build/buy/use-existing
Apply **tool-evaluation-selection** when tooling choice is material:
- hard gates vs weighted requirements
- broad candidate search including current stack, open-source and internal build
- workflow-based pilot
- TCO and switching cost
- evidence confidence

### 4. Design controls
Apply **automation-governance**:
- least privilege
- validation before side effects
- human approval/sampling policy
- audit logs
- retries/idempotency
- exceptions
- rollback/kill switch
- ownership and incident response

### 5. Pilot
Define:
- golden scenarios including edge/worst cases
- baseline and target
- quality/error gates
- human-review burden
- cost/latency
- time saved
- downstream business metric
- stop/rollback criteria

Start shadow/assistive when failure is hard to detect or costly.

### 6. Red-team
- What if the model is confidently wrong?
- What if source data is stale/missing?
- What if an integration partially fails?
- What if the wrong customer/project is selected?
- What if review effort erases time savings?
- What if process changes next month?
- What if automation creates output faster but no decision improves?

## Output

Produce current-state map, future-state architecture, tool decision, control matrix, pilot/evaluation contract, ROI range, rollout plan, and operating owner.

### Decision
`AUTOMATE | ASSIST | SHADOW PILOT | REDESIGN FIRST | KEEP HUMAN | HOLD`.
