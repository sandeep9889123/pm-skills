# PM Prospect Discovery

## Overview

`pm-prospect-discovery` is a model-agnostic operating system for enterprise pre-RFP discovery. It is designed for the recurring situation where Sales or leadership has a prospect, a partial problem statement, and an early solution or use-case hypothesis, but the team needs a high-level discovery session before a formal RFP, proposal, estimate, or architecture commitment.

The plugin converts limited prospect context into a repeatable workflow:

`Account context -> evidence -> problem hypothesis -> use-case options -> red-team -> journey -> assumptions -> adaptive questions -> solution options -> session -> synthesis -> readiness gate -> proposal handoff`

It is intentionally different from generic customer interviews. Enterprise prospect discovery may begin with a proposed path, but the workflow must actively try to falsify that path rather than turn the session into solution-confirmation theatre.

### Core reliability rules

- Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE`.
- Never invent prospect systems, integrations, volumes, budgets, pain severity, buying intent, timelines, or stakeholder decisions.
- A user-supplied solution hypothesis is a hypothesis, not a validated requirement.
- Discovery must include disconfirming questions and at least one credible alternative to the proposed use case.
- Tool or search failure means `coverage incomplete / UNKNOWN`, never absence.
- Do not estimate delivery or commit architecture while P0 discovery inputs remain unresolved.
- `WRONG USE CASE`, `SECOND DISCOVERY REQUIRED`, and `NOT READY` are valid outcomes.
- Questions must be decision-linked. If an answer cannot change scope, architecture, economics, ownership, risk, or next action, deprioritize it.

## Install

### Any LLM

No plugin runtime is required. Give the model:

1. `prompts/prospect-discovery-master.md`
2. the prospect context
3. any source material such as call notes, emails, decks, websites, RFP fragments, or current solution hypothesis

For models that can read repository files, point them to this plugin directory and instruct them to follow the master prompt and local skills. The skills are plain Markdown using portable Agent Skills conventions and contain no provider-specific tool syntax.

See `references/model-agnostic-usage.md`.

### Claude Code / Cowork

Install from the repository marketplace and use one of the commands below.

## Skills (10)

1. `prospect-discovery-orchestrator` - controls the end-to-end discovery logic and fail-closed gates.
2. `prospect-research` - builds an evidence-led account and market context pack.
3. `problem-use-case-hypothesis` - converts weak inputs into falsifiable problem and wedge hypotheses.
4. `journey-decomposition` - decomposes the proposed business flow into decision-relevant capability stages.
5. `solution-option-framing` - generates baseline, vision-aligned, and differentiated solution directions without prematurely committing.
6. `discovery-question-engine` - generates adaptive questions from a stable enterprise discovery taxonomy.
7. `assumption-register` - creates and manages explicit assumptions with validation status and consequence.
8. `discovery-red-team` - attacks the proposed use case, root cause, buying logic, and delivery assumptions.
9. `discovery-synthesis` - converts session notes into evidence, decisions, changes, blockers, and follow-ups.
10. `proposal-readiness` - determines whether the opportunity is ready for solutioning, architecture, estimation, business case, and proposal.

## Commands (4)

### `/pm-prospect-discovery:prospect-discovery`

End-to-end workflow. Use when you have initial prospect context and want the complete pre-RFP discovery pack plus readiness logic.

### `/pm-prospect-discovery:discovery-prepare`

Pre-call workflow. Generates research, hypotheses, assumption register, journey, solution options, and the adaptive session guide.

### `/pm-prospect-discovery:discovery-synthesize`

Post-call workflow. Takes notes or a transcript and produces validated findings, contradictions, unresolved items, scope changes, and next actions.

### `/pm-prospect-discovery:discovery-readiness`

Decision gate. Determines whether evidence is sufficient to proceed to solutioning, estimation, business case, architecture, or proposal.

## What a strong discovery pack contains

- prospect/account context with evidence labels
- buyer, user, operator, approver, and technical stakeholder hypotheses
- explicit problem statement and alternative root causes
- 1-3 use-case wedges ranked by evidence, value, feasibility, and risk
- proposed journey or capability stages
- three solution directions per relevant stage where useful
- assumption register with consequence and validation method
- mandatory questions and conditional/deeper questions
- dependencies, ownership, integration, data, security, and operational constraints
- explicit out-of-scope items
- disconfirming evidence and strongest case against the proposed path
- post-session evidence ledger
- discovery confidence and readiness gates
- proposal handoff with knowns, unknowns, blockers, and estimation inputs

## Reference implementation

`examples/jfll-reference.md` documents the pattern extracted from a freight-logistics discovery session: a proposed Quote-to-Booking wedge, sequential capability waypoints, three solution directions, current-state questions, capability ownership, working assumptions, deferred scope, and structured follow-up.

The example is a pattern reference, not a reusable freight questionnaire. The engine must regenerate questions from each new prospect's context.

## Output principle

Do not optimize for the longest questionnaire. Optimize for the smallest set of questions that can change a material decision.

The goal is not to finish a checklist. The goal is to answer:

`Are we solving the right problem, for the right people, with a viable Phase 1, under understood constraints, with enough evidence to make the next commitment?`
