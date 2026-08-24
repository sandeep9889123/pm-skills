# PM Product Discovery

Product discovery workflows for moving from vague product questions to structured evidence, risks, assumptions, opportunities, and testable next steps.

This plugin is part of Sandeep Kumar M's enhanced `pm-skills` fork. It builds on the upstream PM skills foundation and adds a stronger operating expectation: do not produce generic discovery theater. Separate what is known, what is assumed, what needs validation, and what can be decided now.

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

## Skills included

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

## Commands included

- `/brainstorm`
- `/discover`
- `/interview`
- `/setup-metrics`
- `/triage-requests`

## Operating rules

1. Start with the user problem, not the solution.
2. Separate evidence from opinion.
3. Do not assume demand from stakeholder urgency alone.
4. Treat feature requests as signals, not requirements.
5. Always expose risky assumptions before recommending experiments.
6. Make next steps measurable, small, and decision-oriented.

## Example use

```text
Use pm-product-discovery to analyze these customer requests. Group them by user job, pain severity, evidence strength, and discovery risk. Then propose the top validation experiments.
```

## Output standard

A strong output from this plugin should include:

- problem framing
- user segments or jobs
- evidence summary
- assumption map
- opportunity areas
- prioritization rationale
- experiment plan
- open questions

## Attribution

Based on the original `phuryn/pm-skills` product discovery work. Enhanced in this fork with clearer evidence separation and decision-focused discovery outputs.
