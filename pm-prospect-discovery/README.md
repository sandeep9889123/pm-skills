# PM Prospect Discovery

Model-agnostic enterprise pre-RFP discovery for turning sparse prospect context into evidence, falsifiable hypotheses, adaptive questions, solution options, and explicit readiness gates.

## When to use

Use this plugin when Sales or leadership has a prospect, partial problem statement, or early solution hypothesis and you need to prepare or synthesize discovery before estimation, architecture, business case, RFP, or proposal commitment.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-prospect-discovery@pm-skills
```

Prepare a session:

```text
/pm-prospect-discovery:discovery-prepare [prospect context]
```

Synthesize after the call:

```text
/pm-prospect-discovery:discovery-synthesize [notes or transcript]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-prospect-discovery@pm-skills
```

Then use:

```text
Use pm-prospect-discovery to prepare a pre-RFP discovery session. Treat our preferred solution as a hypothesis, test alternative root causes, generate only decision-changing questions, and state all P0 blockers.
```

### ChatGPT

If Skills upload is available, upload a specific skill such as `skills/prospect-discovery-orchestrator/` or `skills/discovery-question-engine/`.

With the GitHub app:

```text
Read pm-prospect-discovery/skills/prospect-discovery-orchestrator/SKILL.md from sandeep9889123/pm-skills and follow it using the prospect context below.
```

For the full portable workflow, you can also provide `prompts/prospect-discovery-master.md`.

### Other LLMs

Give the model `prompts/prospect-discovery-master.md`, the prospect context, and source material. If the model supports Agent Skills, load the local skill folders directly.

## Skills (10)

- `assumption-register`
- `discovery-question-engine`
- `discovery-red-team`
- `discovery-synthesis`
- `journey-decomposition`
- `problem-use-case-hypothesis`
- `proposal-readiness`
- `prospect-discovery-orchestrator`
- `prospect-research`
- `solution-option-framing`

## Commands (4)

- `/pm-prospect-discovery:prospect-discovery` - end-to-end workflow
- `/pm-prospect-discovery:discovery-prepare` - pre-call preparation
- `/pm-prospect-discovery:discovery-synthesize` - post-call synthesis
- `/pm-prospect-discovery:discovery-readiness` - readiness decision

## Example prompts

```text
Use pm-prospect-discovery to prepare a 60-minute discovery for this enterprise account. Build evidence-backed account context, alternative problem hypotheses, 1-3 plausible Phase 1 wedges, and the minimum sufficient MUST ASK questions.
```

```text
Use proposal-readiness on these discovery notes. Tell me separately whether we are ready for solutioning, architecture, estimation, business case, and proposal. A high score must not override an unresolved P0 blocker.
```

## Operating rules

- Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE`.
- Never invent systems, integrations, volumes, budgets, buying intent, timelines, or stakeholder decisions.
- A proposed use case is a hypothesis, not a validated requirement.
- Include disconfirming questions and credible alternatives.
- Tool or search failure means `coverage incomplete / UNKNOWN`, never absence.
- Do not estimate delivery or commit architecture while P0 discovery inputs remain unresolved.
- `WRONG USE CASE`, `SECOND DISCOVERY REQUIRED`, and `NOT READY` are valid outcomes.

## Output standard

A strong discovery pack includes account evidence, stakeholder hypotheses, alternative root causes, ranked wedges, journey stages, solution directions, assumptions, adaptive questions, dependencies, red-team evidence, post-session synthesis, and readiness gates.

## Reference pattern

`examples/jfll-reference.md` is a generalized pattern extracted from a freight-logistics discovery session. It is not a reusable freight questionnaire.
