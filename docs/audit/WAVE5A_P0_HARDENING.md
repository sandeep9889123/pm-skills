# Wave 5A P0 Hardening

## Scope

Wave 5A hardens six decision-critical primitives and six workflow wrappers selected by the Reliability Risk Map.

### Skills

- `pm-market-research/market-segments`
- `pm-market-research/sentiment-analysis`
- `pm-data-analytics/cohort-analysis`
- `pm-data-analytics/sql-queries`
- `pm-product-discovery/interview-script`
- `pm-product-discovery/metrics-dashboard`

### Workflows

- `/research-users`
- `/analyze-feedback`
- `/analyze-cohorts`
- `/write-query`
- `/interview`
- `/setup-metrics`

## Failure modes removed

| Area | Before | Wave 5A behavior |
|---|---|---|
| Market segmentation | forced 3-5 segments and size/growth fields | evidence-supported count, hypothesis mode, no invented prevalence, `DO NOT SEGMENT YET` allowed |
| Sentiment | forced 3 segments, arbitrary -1..+1 score, NPS proxy | declared method, no text-derived NPS, sample-bias disclosure, observed vs inferred root cause |
| Cohorts | descriptive pattern could become “why”, immature cells ambiguous | eligible denominators, right-censoring, same-age comparison, causal limits |
| SQL | plausible schema could be inferred and query called production-ready | no schema invention, explicit template mode, metric contract, join-cardinality and validation checks |
| Interviews | solution hypothesis could shape questions; enthusiasm could look like demand | neutral decision framing, disconfirming probes, past behavior, sampling limits, stated enthusiasm not demand proof |
| Metrics | template encouraged invented targets/alerts and assumed causal input tree | metric contracts, instrumentation gate, observed/target/proposal states, evidence-based alerts, Goodhart checks |
| Workflow wrappers | command could override hardened skill | wrapper carries the same P0 guards and cannot reintroduce fixed-count/schema/benchmark assumptions |

## Reliability scenarios

`reliability/WAVE5A_SCENARIOS.md` adds 12 adversarial cases covering:

- forced segmentation
- sentiment false precision
- source-mix bias
- cohort right-censoring
- correlation-to-causation errors
- SQL schema hallucination
- join multiplication
- interview confirmation bias
- enthusiasm-as-demand
- invented dashboard thresholds
- North Star gaming
- workflow-overrides-skill regression

`tests/test_wave5a_hardening.py` protects the material runtime guards and selected forbidden legacy behaviors.

## What Wave 5A does not prove

These tests prove that required reliability instructions remain present. They do not prove that every LLM will follow them on every first run.

The behavioral evaluation layer should add frozen/mutated cases for these failure families in Wave 7 and score actual model outputs.

## Next P0 tranche

Wave 5B should harden enterprise strategy and GTM primitives:

- business model
- monetization strategy
- Porter's Five Forces
- ideal customer profile
- beachhead segment
- GTM motions
- high-consequence strategy/GTM command wrappers

Primary risks: unsupported economics, stale market structure, ICP invention, buyer/user confusion, TAM-biased beachhead selection, and GTM motion without realistic acquisition/implementation economics.
