# PM Product Discovery

Product discovery workflows for moving from vague product questions to structured evidence, risks, assumptions, opportunities, and testable next steps.

## When to use

Use this plugin when you need to:

- synthesize customer interviews
- write interview scripts
- triage feature requests
- identify risky assumptions
- generate discovery experiments
- build an opportunity-solution tree
- define early metrics for a problem area
- convert scattered qualitative inputs into PM-ready evidence

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

Add the marketplace once, then install this plugin:

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-product-discovery@pm-skills
```

Run a workflow:

```text
/pm-product-discovery:discover AI-assisted meeting notes for enterprise teams
```

Or name one skill directly:

```text
Use the prioritize-assumptions skill to rank these product assumptions by impact and evidence risk.
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-product-discovery@pm-skills
```

Then use plain language:

```text
Use pm-product-discovery to run ideation, assumption mapping, risk prioritization, and experiment design for this product idea. Pause at each decision gate.
```

### ChatGPT

If Skills upload is available, upload any folder under `skills/`, for example `skills/prioritize-assumptions/`.

If using the GitHub app, prompt:

```text
Read pm-product-discovery/skills/prioritize-assumptions/SKILL.md from sandeep9889123/pm-skills and follow it for the assumptions below.
```

Claude slash commands are not assumed in ChatGPT. Use the equivalent natural-language workflow prompt.

### Other LLMs

Copy the required `skills/*` folders into your tool's Agent Skills directory, or attach the relevant `SKILL.md` and tell the model to follow it as the governing workflow.

## Skills (13)

- `analyze-feature-requests`
- `brainstorm-experiments-existing`
- `brainstorm-experiments-new`
- `brainstorm-ideas-existing`
- `brainstorm-ideas-new`
- `identify-assumptions-existing`
- `identify-assumptions-new`
- `interview-script`
- `metrics-dashboard`
- `opportunity-solution-tree`
- `prioritize-assumptions`
- `prioritize-features`
- `summarize-interview`

## Commands (5)

- `/pm-product-discovery:brainstorm`
- `/pm-product-discovery:discover`
- `/pm-product-discovery:interview`
- `/pm-product-discovery:setup-metrics`
- `/pm-product-discovery:triage-requests`

## Example prompts

```text
Use pm-product-discovery to analyze these customer requests. Group them by user job, pain severity, evidence strength, and discovery risk. Then propose the cheapest validation experiments.
```

```text
Use the opportunity-solution-tree skill to map our target outcome, opportunities, candidate solutions, assumptions, and experiments. Do not force a solution where evidence is weak.
```

## Operating rules

1. Start with the user problem, not the solution.
2. Separate evidence from opinion.
3. Do not assume demand from stakeholder urgency alone.
4. Treat feature requests as signals, not requirements.
5. Expose risky assumptions before recommending experiments.
6. Make next steps measurable, small, and decision-oriented.

## Output standard

A strong output should include problem framing, user jobs, evidence summary, assumption map, opportunity areas, prioritization rationale, experiment plan, and open questions.

## Attribution

Based on the original `phuryn/pm-skills` product discovery work. Enhanced in this fork with evidence separation and decision-focused discovery outputs.
