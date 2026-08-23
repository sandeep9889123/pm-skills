---
name: economics-commercial-proof
description: "Build transparent business-case economics, pricing evidence, scenario analysis, GTM wedge, sales motion, implementation economics, and commercialization proof. Use when ROI, payback, revenue, pricing, cost, or GTM claims must be auditable rather than persuasive guesses."
---
# Economics and Commercial Proof

## Objective

Turn commercial and financial claims into reproducible models rather than attractive numbers.

Follow `pm-business-case/references/EVIDENCE_CONTRACT.md`.

Every material number must be a FACT or ESTIMATE with explicit provenance.

## Step 1: Define the economic question

Clarify what the business case is optimizing for:

- new revenue
- services pull-through
- recurring software revenue
- retention
- margin improvement
- delivery productivity
- cost avoidance
- risk reduction
- strategic option value
- internal efficiency

Do not combine different value pools into one headline without showing each component.

## Step 2: Cost model

Model applicable costs separately:

### Build
- product and engineering
- data and AI work
- design
- domain expertise
- security and compliance
- infrastructure
- tooling
- integration
- testing and evaluation

### Deploy
- implementation
- migration or configuration
- customer-specific customization
- onboarding
- training
- change management

### Operate
- cloud or model inference
- support
- monitoring
- human review
- incident response
- retraining or re-indexing
- maintenance
- licensing
- vendor fees

### Sell
- sales capacity
- presales
- PoC effort
- partner economics
- marketing
- procurement and contracting overhead

Do not hide recurring operating cost inside one-time build cost.

## Step 3: Benefit model

Separate observed benefits from modeled benefits.

Potential value pools:

- revenue uplift
- conversion improvement
- cycle-time reduction
- labor reduction
- avoided rework
- lower error cost
- lower compliance exposure
- faster delivery
- reduced implementation effort
- improved utilization
- reduced vendor spend

If a benefit is not directly measured, classify it ESTIMATE.

Do not monetize risk reduction using invented probabilities or loss values.

## Step 4: Reconstructable estimates

Every material ESTIMATE must expose:

- formula
- input value
- unit
- input source claim ID when sourced
- assumption when unsourced
- low/base/high range when material

Examples:

`annual labor benefit = users x hours saved per user per month x loaded hourly cost x 12`

`annual recurring revenue = reachable accounts x expected win rate x average annual contract value`

`payback months = initial investment / monthly net benefit`

The formula is illustrative. Use the model appropriate to the case.

## Step 5: Scenario analysis

At minimum use bear, base, and bull cases when uncertainty is material.

Vary the assumptions that actually drive the outcome, such as:

- adoption
- price
- win rate
- implementation capacity
- cycle time saved
- utilization
- infrastructure cost
- support burden
- sales cycle

Do not create scenarios by applying arbitrary percentage haircuts to the final answer.

Show which variables create the most sensitivity.

## Step 6: Pricing evidence

Pricing is not automatically a FACT because competitors publish a list price.

Classify evidence:

- observed transaction
- signed contract
- procurement history
- pricing test
- explicit willingness to pay (WTP) research
- comparable verified price
- public list price
- analyst estimate
- internal proposal

A confident pricing recommendation requires credible willingness to pay (WTP) or comparable commercial evidence.

Without it, use PROPOSAL or ESTIMATE and define a pricing experiment.

## Step 7: Unit economics

Where applicable calculate:

- gross margin
- contribution margin
- customer acquisition cost
- implementation cost
- support cost
- payback period
- lifetime value assumptions
- expansion potential

Do not calculate LTV from arbitrary retention assumptions.

For services-heavy offerings, show delivery capacity and utilization constraints, not only software-style margins.

## Step 8: GTM wedge

Define the smallest commercially credible entry point:

- target segment
- urgent use case
- economic buyer
- trigger event
- existing pain
- proof asset
- sales motion
- expected implementation path
- expansion path

Avoid generic GTM statements such as "enterprise sales plus partnerships" without mechanism.

## Step 9: Pilot economics

A pilot must have a production path.

Capture:

- pilot objective
- who pays
- implementation effort
- data dependency
- success threshold
- conversion condition
- production deployment requirement
- post-pilot owner
- commercial next step

A free PoC that cannot convert is a research expense, not GTM evidence.

## Step 10: Reuse economics

For accelerators or platforms, model whether reuse reduces marginal effort.

Track:

- common reusable components
- customer-specific work
- deployment hours
- maintenance burden
- integration burden
- incremental gross margin
- implementation cycle time

One reusable codebase is not evidence of scalable economics.

## Step 11: Commercial contradiction pass

Actively test:

- what if customers will not pay separately for this capability;
- what if value is captured as services rather than software;
- what if implementation cost erodes margin;
- what if support or human-review cost scales with usage;
- what if sales cycles are longer than the model assumes;
- what if the buyer already owns an acceptable substitute;
- what if the benefit accrues to users but the budget owner sees little value;
- what if reuse does not reduce delivery effort.

Preserve the downside case.

## Output

### Cost model
FACT versus ESTIMATE inputs.

### Benefit model
Observed versus modeled value.

### Bear / base / bull scenarios
With driver sensitivity.

### Pricing evidence
What is known versus proposed.

### Unit economics
Where applicable.

### GTM wedge
Segment, buyer, trigger, sales motion, proof asset, production path.

### Reuse economics
Only when relevant.

### Commercial blockers
P0 unknowns and experiments required.

## Hard stop conditions

Do not make a confident ROI, revenue, payback, margin, or pricing claim when:

- formulas are missing;
- inputs are not traceable;
- adoption or win rate is arbitrary;
- market size is used as revenue forecast;
- willingness to pay is assumed;
- one-time and recurring costs are mixed;
- pilot economics ignore production conversion;
- platform economics assume reuse that has not been demonstrated.
