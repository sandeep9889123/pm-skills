# PM Data Analytics

Product analytics workflows for SQL, cohort analysis, A/B test interpretation, and analytical reasoning for PM decisions.

This plugin is part of Sandeep Kumar M's enhanced `pm-skills` fork. It is designed to help PMs reason from data without overstating causality or hiding uncertainty.

## When to use

Use this plugin when you need to:

- write SQL for product analysis
- define analysis logic before querying
- interpret A/B test results
- analyze cohorts
- structure metrics for a product question
- separate correlation from causation
- explain data caveats to stakeholders

## Skills included

- `ab-test-analysis`
- `cohort-analysis`
- `sql-queries`

## Commands included

- `/analyze-cohorts`
- `/analyze-test`
- `/write-query`

## Operating rules

1. Define the decision before defining the metric.
2. Do not infer causality from descriptive metrics.
3. Always state denominator, segment, time window, and caveats.
4. Treat missing instrumentation as a product risk.
5. For experiments, call out power, sample size, guardrails, and novelty effects.
6. If data is not available, produce a measurement plan instead of pretending certainty.

## Example use

```text
Use pm-data-analytics to design a cohort analysis for this onboarding flow. Define the SQL logic, metrics, segments, caveats, and decision implications.
```

## Output standard

A strong output from this plugin should include:

- decision question
- metric definition
- query logic
- segmentation
- interpretation
- caveats
- recommendation
- follow-up analysis

## Attribution

Based on the original `phuryn/pm-skills` analytics workflows. Enhanced in this fork with stronger PM decision framing and analytical caveat discipline.
