---
name: user-segmentation
description: "Segment users or accounts from behavioral, JTBD, needs, usage, and economic evidence without forcing arbitrary cluster counts. Use when building actionable segmentation for product, GTM, pricing, or customer-success decisions."
---

# User / Account Segmentation

## Purpose

Find segments that are **real enough to change a product, GTM, pricing, or service decision**. Do not force three segments from sparse feedback or create polished archetypes that the data cannot support.

## Step 1: Define the decision

State what segmentation will inform: product experience, prioritization, pricing, GTM, support, account expansion, research sampling, etc.

## Step 2: Assess data suitability

Inventory:
- source types and time period
- number of users/accounts
- representation / sampling bias
- behavioral/usage data
- qualitative evidence
- revenue/economic data if relevant
- missing groups

If there is no user/account-level evidence, create **segmentation hypotheses**, not research-backed segments.

## Step 3: Identify candidate dimensions

Prioritize dimensions that plausibly explain different needs/outcomes:
- JTBD / workflow
- behavior/frequency/depth
- sophistication/maturity
- pain severity
- desired outcome
- constraints/integrations
- buying/implementation complexity
- value/economic profile
- lifecycle stage

Use demographics/firmographics only when they explain meaningful differences.

## Step 4: Form and validate clusters

Do not require a minimum number of segments. Use the fewest segments that are distinct, stable enough, and actionable.

For each candidate segment test:
- within-segment coherence
- between-segment separation
- size/representation confidence
- outcome/behavior differences
- actionability
- stability over time
- overlap / multi-job users

Where quantitative clustering is used, explain features, scaling, method, sensitivity, and validation rather than presenting algorithmic clusters as truth.

## Reliability / Edge Cases

- Never invent percentages or segment size without denominators.
- Verify verbatim quotes or omit them.
- Flag underrepresented groups.
- Do not infer causality from segment association.
- Check Simpson's paradox / cohort mix when aggregate behavior differs.
- Avoid persona-like fictional enrichment not present in evidence.
- For enterprise: distinguish account segment, buyer persona, user role, and use-case segment. They are not interchangeable.
- Test whether segment differences justify different actions. If not, the segmentation is decorative.

## Output

### Evidence quality
`ROBUST | DIRECTIONAL | HYPOTHESIS-ONLY` with reasons.

### Segment table
| Segment | Defining evidence | JTBD/behavior | Size/range | Distinct need | Product/GTM implication | Confidence |
|---|---|---|---|---|---|---|

### Overlaps and excluded/unknown groups
State what the model does not explain.

### Validation plan
What additional usage/research data would confirm or reject each segment.

### Decision
`USE | USE DIRECTIONALLY | VALIDATE | DO NOT SEGMENT YET`.

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
