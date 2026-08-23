---
name: north-star-metric
description: "Define and validate a North Star Metric and supporting input/guardrail metrics using customer value, causal plausibility, data quality, segment behavior, and business sustainability. Use when deciding what a product or business should optimize."
---
# North Star Metric

Choose a metric that represents delivered customer value and is useful for decisions. Do not choose a metric merely because it is easy to measure or sounds strategic.

## Step 1: Understand the value system

Capture:
- customer/job and successful outcome
- business model
- frequency/cadence of value delivery
- buyer vs user if different
- value creation versus value capture
- current measurement/data quality
- known failure/abuse modes

## Step 2: Generate multiple candidates

Do not jump to the first plausible metric. Generate 3–5 candidates and evaluate each.

Useful business-game framing may include attention, transaction, productivity, or other context-specific value mechanics, but do not force a company into one taxonomy if its model is hybrid.

## Step 3: Validate each candidate

A strong NSM should:
1. represent customer value actually realized, not activity alone;
2. be understandable and consistently defined;
3. be measurable with acceptable latency/data quality;
4. be influenced by teams without encouraging obvious gaming;
5. correlate plausibly with durable business health;
6. distinguish healthy from unhealthy usage where relevant;
7. remain meaningful across important segments or explicitly state segment limitations;
8. have input metrics teams can act on;
9. have guardrails that prevent local optimization damage.

## Reliability / Causal Gate

Before selecting:
- Do not claim a candidate is a leading indicator of revenue/retention without evidence. Label that relationship `HYPOTHESIS` until validated.
- Test for Goodhart's Law: how could the organization increase the metric while making the customer/business worse?
- Check denominator effects, seasonality, cohort mix, and segment reversal.
- Separate **value delivered** from **usage volume**. More usage can mean friction in productivity products.
- Avoid vanity metrics such as raw signups, page views, messages, or time spent unless they genuinely represent the value mechanism.
- Test whether enterprise buyer value differs from end-user value.
- Include quality/safety/reliability guardrails for AI or high-risk workflows.
- If no single metric responsibly represents the system, say so. Use a primary value metric plus a small health constellation rather than forcing a misleading NSM.

## Step 4: Inputs and guardrails

For the selected candidate define:
- exact numerator/denominator/window
- unit of analysis
- eligible population
- data source/owner
- lag/freshness
- input metrics with causal hypothesis
- guardrails
- segmentation cuts
- alert thresholds only when baselines support them

## Step 5: Validation plan

Test whether changes in the candidate are associated with retention, expansion, successful task completion, or another durable outcome using historical cohorts/experiments where possible.

## Output

| Candidate | Customer-value fidelity | Actionability | Data quality | Gaming risk | Business-health evidence | Decision |
|---|---|---|---|---|---|---|

Then provide metric contract, inputs, guardrails, failure modes, and validation plan.

### Decision
`ADOPT | PILOT | VALIDATE RELATIONSHIP | USE METRIC SET | REJECT`.

---

### Further Reading

- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [AARRR (Pirate) Metrics: The 5-Stage Framework for Growth](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework: Your Guide to Measuring User-Centric Success](https://www.productcompass.pm/p/the-google-heart-framework)
- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
