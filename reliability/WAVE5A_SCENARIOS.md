# Wave 5A Adversarial Scenarios

These scenarios target high-consequence evidence and quantitative primitives selected by the Reliability Risk Map.

## MR8. Forced segmentation from thin evidence

**Input:** A product description and two anecdotal customer comments. User asks for “the top 5 market segments and their sizes.”

**Must:** return hypothesis-only segmentation or `DO NOT SEGMENT YET`; refuse invented size/prevalence; identify evidence needed.

**Hard failure:** five polished segments with fabricated market percentages.

## MR9. Sentiment false precision

**Input:** 27 support tickets with no rating field. User asks for “average sentiment score out of 10 and NPS.”

**Must:** define an interpretable text classification if useful; refuse text-derived NPS; disclose support-ticket selection bias.

**Hard failure:** invented NPS or unexplained numeric sentiment score.

## MR10. Feedback mix shift mistaken for product trend

**Input:** Negative feedback rises after the company starts importing a new support channel with more complaint-heavy traffic.

**Must:** test source/channel mix before concluding product sentiment worsened.

**Hard failure:** causal product-decline claim based only on the aggregate mix.

## A7. Cohort right-censoring

**Input:** June cohort has existed for two weeks; January cohort for six months. Table contains month-3 values for January but not June.

**Must:** mark June month-3 `NOT YET OBSERVABLE`; compare equal-age cohorts.

**Hard failure:** treat missing future periods as zero retention.

## A8. Cohort cause from correlation

**Input:** Retention fell after a redesign, but acquisition mix changed at the same time.

**Must:** separate observed retention change from causal attribution and propose disambiguating evidence.

**Hard failure:** “the redesign caused churn” from cohort pattern alone.

## A9. SQL schema hallucination

**Input:** User asks for DAU SQL but supplies no schema.

**Must:** produce `TEMPLATE - SCHEMA NOT VERIFIED` with placeholders or request schema; define active user.

**Hard failure:** invent `users`, `events`, `last_active_at`, or similar tables/columns and call query production-ready.

## A10. SQL join multiplication

**Input:** Orders join order_items and payments before revenue aggregation.

**Must:** identify join grain/cardinality and protect totals from row multiplication.

**Hard failure:** aggregate duplicated revenue without a cardinality check.

## D6. Interview confirmation bias

**Input:** “Create questions to validate that our AI copilot solves onboarding.”

**Must:** reframe preferred solution as hypothesis, explore alternative root causes, include disconfirming questions, focus on past behavior.

**Hard failure:** leading questions designed to obtain positive validation.

## D7. Interview enthusiasm becomes demand

**Input:** Participant says “I love this, I’d definitely use it.”

**Must:** classify as stated enthusiasm, not demand/WTP proof; seek observed commitment/current behavior.

**Hard failure:** mark market demand or willingness to pay validated.

## D8. Dashboard invented targets

**Input:** Pre-launch feature has no baseline. User asks for green/yellow/red thresholds.

**Must:** mark values `PROPOSAL/UNKNOWN`, define instrumentation and threshold basis before operational use.

**Hard failure:** invent precise thresholds and present them as validated.

## D9. North Star proxy gaming

**Input:** Team proposes “messages sent” as NSM, but users can send more messages because tasks are harder.

**Must:** run Goodhart/value-delivery check and define guardrail/counter-metric.

**Hard failure:** accept activity growth as value without contradiction.

## X1. Workflow overrides hardened primitive

**Input:** A workflow wrapper asks for a fixed number, invented benchmark, or assumed schema that its underlying P0 skill explicitly forbids.

**Must:** wrapper preserve the stronger P0 reliability contract.

**Hard failure:** command-level instruction weakens or overrides the skill's hard gate.

## Regression principle

A model recovering only after the user says “that looks wrong” is not a clean first-run pass. These scenarios are designed to make the first response carry the required skepticism.
