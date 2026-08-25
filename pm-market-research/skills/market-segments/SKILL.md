---
name: market-segments
description: "Identify evidence-supported customer or market segments using JTBD, behavior, firmographics, buying context, and product fit. Avoids forced segment counts, invented market sizes, and unsupported prioritization. Use when exploring target segments, evaluating markets, or deciding where to focus."
---

# Market Segments

## Purpose

Identify the **smallest defensible set of materially different customer groups** for `$ARGUMENTS` and show what evidence supports each segment.

Do not create segments merely because a template expects them.

## P0 Reliability Contract

Before segmenting, resolve the decision context where material:

- What decision will the segmentation support: discovery, product strategy, pricing, GTM, sales coverage, or expansion?
- B2B, B2C, B2B2C, marketplace, or mixed?
- Geography / industry / product scope?
- Current stage: hypothesis, discovery, pilot, production, scale?
- What evidence is actually available?

Use these evidence states where needed: `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`.

### Hard rules

1. **Do not force 3-5 segments.** Return the number supported by evidence. One, two, six, or `DO NOT SEGMENT YET` are valid.
2. **No invented segment sizes, growth rates, WTP, demographics, or market shares.** If unsupported, mark `UNKNOWN` or provide an explicitly modeled `ESTIMATE` with method/inputs.
3. **Do not treat a persona as a market segment.** A segment must be useful for a materially different product, buying, servicing, or GTM decision.
4. **Do not infer prevalence from source frequency when the sample is not representative.** Ten interview mentions do not equal 10% of the market.
5. **Do not force mutually exclusive groups if real buying/usage modes overlap.** State the segmentation unit and overlap rules.
6. **Tool/search failure is coverage incomplete, not evidence that a segment does not exist.**
7. **User-supplied segments are hypotheses to test, not facts to preserve.**

## Step 1: Define the Segmentation Unit

State what is being segmented:

- individual users
- buyer roles
- accounts/companies
- use cases / jobs
- transactions
- operating environments
- another explicit unit

Mixing units creates false segments. If both account and user segmentation matter, keep them as separate layers.

## Step 2: Inventory Evidence

For each source, note:

| Source | Population / scope | What it can support | Bias / limitation | Freshness |
|---|---|---|---|---|

Possible inputs:

- interviews / research notes
- product usage / transaction data
- CRM / sales data
- support tickets
- market research
- public market evidence
- product description only

If only a product description is available, produce **segment hypotheses**, not research-backed segments.

## Step 3: Generate Candidate Segmentation Dimensions

Consider only dimensions that could change a decision:

- JTBD / desired outcome
- workflow and frequency
- pain severity / consequence
- current alternative
- sophistication / readiness
- buying trigger
- buyer / champion / user relationship
- company size / industry where behavior actually differs
- regulatory / operational environment
- willingness-to-pay evidence, if available
- implementation/integration burden

Demographics/firmographics are descriptors, not automatically causal segment definitions.

## Step 4: Build Candidate Segments

For each candidate:

| Segment | Defining rule | Evidence | Distinct job/behavior | Different decision implied? | Confidence |
|---|---|---|---|---|---|

Reject segments that are merely labels with no different job, behavior, buying motion, economics, or product implication.

## Step 5: Validate Segment Quality

A useful segment should be sufficiently:

- **distinct**: materially different from other segments
- **observable/measurable**: membership can be identified
- **actionable**: changes a product/GTM decision
- **reachable**: a realistic channel or route exists when GTM is relevant
- **economically coherent**: value/cost-to-serve can eventually be assessed
- **stable enough**: not an artifact of one temporary event unless event-based segmentation is intended

### Contradiction pass

Before finalizing, ask:

- Could these differences be explained by geography, acquisition channel, customer tenure, plan, or another confounder?
- Does the segmentation disappear under another plausible grouping?
- Are minority/high-value groups being hidden by aggregate volume?
- What evidence would show these are not real decision-useful segments?

## Step 6: Characterize Only What Evidence Supports

For each retained segment provide:

### Segment definition
- membership rule
- unit of segmentation
- evidence status and confidence

### Job / context
- core JTBD or desired outcome
- workflow / trigger / stakes
- current alternative

### Needs and friction
- supported pain points
- desired gains
- constraints

### Product / buying implications
- product fit
- adoption or implementation barriers
- buyer/champion/user differences where relevant
- likely GTM implication as hypothesis if not validated

### Size / growth
Use only if evidence supports it:

- `FACT`: sourced population/size
- `ESTIMATE`: method + formula + assumptions + range
- `UNKNOWN`: insufficient evidence

Never manufacture precision to fill this section.

## Step 7: Prioritize for the Actual Decision

Do not declare a universal “best segment.” Score or compare only against criteria relevant to the user's decision, such as:

- problem intensity
- strategic fit / right-to-win
- reachability
- evidence of demand / WTP
- implementation burden
- competitive intensity
- unit economics / cost-to-serve
- learning value

Show sensitivity when uncertain assumptions could reorder the ranking.

## Output

### Decision context
[scope, unit, decision, evidence limits]

### Evidence-backed segments
[return only supported number]

### Segment comparison
| Segment | Evidence state | JTBD / trigger | Product fit | GTM/economic implication | Confidence |
|---|---|---|---|---|---|

### Rejected / unresolved candidates
[why not retained]

### Unknowns and next evidence
[cheapest evidence that could change segmentation]

### Decision
`USE SEGMENTATION | USE AS HYPOTHESES | COLLECT MORE DATA | DO NOT SEGMENT YET`

State what would change the decision.

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Crossing the Chasm: The Ultimate Guide For PMs](https://www.productcompass.pm/p/crossing-the-chasm)
- [How to Achieve Product-Market Fit? Part I: Market and Value Proposition](https://www.productcompass.pm/p/how-to-achieve-the-product-market)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
