# PM Data Analytics

Product analytics workflows for SQL, cohort analysis, A/B test interpretation, and analytical reasoning for PM decisions.

## When to use

Use this plugin when you need to write SQL, define analysis logic, analyze cohorts, interpret experiments, define metrics, separate correlation from causation, or explain analytical caveats to stakeholders.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-data-analytics@pm-skills
```

```text
/pm-data-analytics:analyze-test [experiment results]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-data-analytics@pm-skills
```

```text
Use pm-data-analytics to evaluate this experiment. Check validity, sample-ratio mismatch, power assumptions, practical significance, guardrails, and the decision rule.
```

### ChatGPT

Upload `skills/ab-test-analysis/`, `skills/cohort-analysis/`, or `skills/sql-queries/` if Skills is available.

With the GitHub app:

```text
Read pm-data-analytics/skills/ab-test-analysis/SKILL.md from sandeep9889123/pm-skills and follow it for these results.
```

### Other LLMs

Copy or attach the relevant skill folder. If the model cannot query data, it should produce a query/measurement plan rather than invent observations.

## Skills (3)

- `ab-test-analysis`
- `cohort-analysis`
- `sql-queries`

## Commands (3)

- `/pm-data-analytics:analyze-cohorts`
- `/pm-data-analytics:analyze-test`
- `/pm-data-analytics:write-query`

## Example prompts

```text
Use cohort-analysis to define retention cohorts for this onboarding flow. Specify inclusion rules, denominator, time windows, segments, SQL logic, and decision implications.
```

```text
Use sql-queries to generate the query only after defining the product question, grain, metric definition, joins, exclusions, and validation checks.
```

## Operating rules

1. Define the decision before the metric.
2. Do not infer causality from descriptive metrics.
3. State denominator, segment, time window, and caveats.
4. Treat missing instrumentation as a product risk.
5. For experiments, call out validity, power, sample size, guardrails, and novelty effects.
6. If data is unavailable, produce a measurement plan instead of certainty.

## Output standard

A strong output includes decision question, metric definition, query/analysis logic, segmentation, interpretation, caveats, recommendation, and follow-up analysis.

## Attribution

Based on the original `phuryn/pm-skills` analytics workflows, enhanced with PM decision framing and analytical safeguards.
