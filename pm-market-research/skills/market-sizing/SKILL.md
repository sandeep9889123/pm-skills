---
name: market-sizing
description: "Estimate TAM, SAM, and SOM using triangulated top-down and bottom-up methods with explicit assumptions, source freshness, sensitivity ranges, and realistic go-to-market constraints. Use when sizing a market opportunity, preparing an investment case, or evaluating market entry."
---

# Market Sizing: TAM, SAM, SOM

## Purpose

Estimate market opportunity for **$ARGUMENTS** without manufacturing precision from weak inputs.

> **A market-size number is a model, not a fact, unless the underlying market definition and measurement support it.**

## Step 1: Define the Market Before Sizing It

Specify:

- customer / buyer
- job or problem
- product/category boundary
- geography
- industry/vertical
- time period
- unit of value: customers, seats, transactions, documents, spend, etc.
- revenue definition: software only, services included/excluded, gross vs net if relevant

If the market boundary is ambiguous, show how different definitions change the answer.

## Step 2: Build an Evidence Ledger

For each material input, record:

| Input | Value / Range | Type | Source / basis | Date | Confidence |
|---|---|---|---|---|---|

Type must be one of:

- **FACT**
- **ESTIMATE**
- **ASSUMPTION**
- **INFERENCE**
- **UNKNOWN**
- **STALE**

Do not silently promote assumptions into facts.

## Step 3: Top-Down Estimate

Start from the closest credible externally measured market and narrow it using explicit filters.

For each narrowing step show:

- parent market
- inclusion/exclusion rule
- percentage/value applied
- evidence or assumption behind the filter

Do not use a broad analyst market merely because its label sounds similar.

Check whether the source market includes categories or services outside the defined product arena.

## Step 4: Bottom-Up Estimate

Build from operating units.

Common forms:

```text
Customers × annual spend per customer
```

```text
Eligible accounts × adoption rate × average annual contract value
```

```text
Transactions × price / take rate
```

```text
Users × paid penetration × ARPU
```

For every variable:

- provide source or assumption
- use a range when precision is weak
- avoid double counting customer segments

## Step 5: Reconcile, Do Not Average Blindly

If top-down and bottom-up results disagree materially:

1. compare market definitions
2. compare years / currencies
3. compare included products/services
4. compare customer populations
5. inspect unit economics assumptions
6. inspect adoption/penetration assumptions
7. identify whether one source is stale

Do **not** simply average two incompatible estimates.

State which method is more decision-useful and why.

## Step 6: Define SAM From Actual Constraints

SAM is not an arbitrary percentage of TAM.

Constrain by factors such as:

- geography
- language
- regulatory eligibility
- product capability
- integrations
- customer size
- deployment model
- sales/channel reach
- implementation capacity
- pricing / willingness to pay

Show the bridge from TAM to SAM.

## Step 7: Estimate SOM From Reachability, Not Optimism

SOM should be tied to realistic capture capacity over a stated horizon.

Use inputs such as:

- addressable accounts
- sales capacity
- conversion rate
- sales cycle
- implementation/onboarding capacity
- retention
- competitive win rate
- partner/channel reach
- expansion revenue

If these inputs are unavailable, do not invent an “achievable 1-5% share.”

Instead provide scenario ranges and label SOM confidence low.

Example:

| Scenario | Accounts won | ACV | Annual SOM | Key assumption |
|---|---:|---:|---:|---|
| Bear | | | | |
| Base | | | | |
| Bull | | | | |

## Step 8: Sensitivity Analysis

Identify the 2-4 assumptions that drive most of the result.

Show how the estimate changes if they move.

Examples:

- eligible account count ±20%
- ACV range
- paid penetration
- conversion rate
- implementation capacity

A precise-looking TAM with a 5x sensitivity range should be presented as a range, not a point estimate.

## Step 9: Freshness and Contradiction Pass

Before finalizing, ask:

- Are market reports measuring the same thing?
- Is any key source old relative to current market change?
- Does bottom-up reality contradict the headline analyst number?
- Did I exclude a customer segment because data were missing rather than because it is truly out of scope?
- Is pricing evidence current?
- Does the SOM assume a GTM capacity the company does not have?

If credible evidence conflicts, surface the conflict rather than hiding it.

## Output

```markdown
## Market Sizing: [Market]

### Verdict
- TAM: [range]
- SAM: [range]
- SOM: [range / scenarios]
- Confidence: High / Medium / Low
- Most decision-sensitive assumption: [x]

### Market Definition
[Customer, job, geography, category boundary, year]

### Evidence Ledger
| Input | Value / Range | Type | Source / basis | Date | Confidence |
|---|---|---|---|---|---|

### TAM
**Top-down:** [method + range]
**Bottom-up:** [method + range]
**Reconciliation:** [why they differ / which is preferred]

### SAM Bridge
| Constraint | TAM population/value removed | Evidence / assumption |
|---|---:|---|

### SOM Scenarios
| Scenario | Reach / wins | ACV / value | SOM | Key assumptions |
|---|---:|---:|---:|---|

### Sensitivity
[Top 2-4 drivers and resulting range]

### What Is Known vs Unknown
- FACT:
- ESTIMATE:
- ASSUMPTION:
- UNKNOWN:
- STALE:

### What Would Change the Estimate
[Specific evidence or threshold]

### Next Research
[Cheapest high-value evidence to improve confidence]
```

## Hard Failures

Do not:

- present analyst market labels as automatically equivalent to the defined market
- invent market share, adoption, ACV, account counts, or SOM capture rates
- average incompatible top-down and bottom-up estimates
- use a generic “1-5% of SAM” as realistic SOM without a reachability model
- present a point estimate when inputs only justify a range
- hide source disagreement
- present stale market data as current
- treat missing evidence as zero demand or zero market

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Crossing the Chasm: The Ultimate Guide For PMs](https://www.productcompass.pm/p/crossing-the-chasm)
- [Product Innovation Masterclass](https://www.productcompass.pm/p/product-innovation-masterclass) (video course)
