# PM Execution

Execution workflows for converting strategy and discovery into PRDs, stories, OKRs, roadmaps, sprint plans, stakeholder alignment, test scenarios, and delivery decisions.

## When to use

Use this plugin when you need to write or red-team a PRD, create stories or test scenarios, plan OKRs or sprints, summarize meetings, map stakeholders, run a pre-mortem, transform a roadmap, or generate dummy data.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-execution@pm-skills
```

```text
/pm-execution:write-prd Smart notification workflow that reduces alert fatigue
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-execution@pm-skills
```

```text
Use pm-execution to write a decision-first PRD with scope, non-goals, user journeys, failure cases, acceptance criteria, analytics, dependencies, rollout, and tests.
```

### ChatGPT

Upload a skill folder such as `skills/create-prd/` when Skills is available.

With the GitHub app:

```text
Read pm-execution/skills/create-prd/SKILL.md from sandeep9889123/pm-skills and follow it for the attached problem statement.
```

### Other LLMs

Copy the relevant skill folder into your tool's Agent Skills directory or attach `SKILL.md`. Use plain language for command workflows.

## Skills (16)

- `brainstorm-okrs`
- `create-prd`
- `dummy-dataset`
- `job-stories`
- `outcome-roadmap`
- `pre-mortem`
- `prioritization-frameworks`
- `release-notes`
- `retro`
- `sprint-plan`
- `stakeholder-map`
- `strategy-red-team`
- `summarize-meeting`
- `test-scenarios`
- `user-stories`
- `wwas`

## Commands (11)

- `/pm-execution:generate-data`
- `/pm-execution:meeting-notes`
- `/pm-execution:plan-okrs`
- `/pm-execution:pre-mortem`
- `/pm-execution:red-team-prd`
- `/pm-execution:sprint`
- `/pm-execution:stakeholder-map`
- `/pm-execution:test-scenarios`
- `/pm-execution:transform-roadmap`
- `/pm-execution:write-prd`
- `/pm-execution:write-stories`

## Example prompts

```text
Use the create-prd skill. Include decision framing, personas, scope, non-goals, journeys, edge/failure cases, acceptance criteria, analytics events, rollout, dependencies, and open evidence gaps.
```

```text
Use strategy-red-team on this roadmap. Steelman it first, then identify the load-bearing assumptions, what would make each fail, and the cheapest test before commitment.
```

## Operating rules

1. Execution artifacts must expose decisions, dependencies, and unknowns.
2. A PRD is incomplete without acceptance criteria and non-goals.
3. Stories must preserve the user job and business reason.
4. Tests must include failure paths and edge cases.
5. Roadmaps should connect work to outcomes.
6. Meeting notes should produce actions, owners, decisions, and risks.

## Output standard

A strong output includes crisp scope, decision log, requirements, acceptance criteria, owner map, dependencies, risks, validation plan, and next actions.

## Attribution

Based on the original `phuryn/pm-skills` execution workflows, enhanced with stronger red-team, testability, and delivery-readiness standards.
