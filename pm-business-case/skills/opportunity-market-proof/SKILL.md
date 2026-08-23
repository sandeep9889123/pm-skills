---
name: opportunity-market-proof
description: "Validate why-now signals, market structure, competitors, substitutes, market size, strategic alternatives, and right-to-win for a business case. Use when proving whether an opportunity exists before recommending build or investment."
---
# Opportunity and Market Proof

## Objective

Prove that an opportunity exists and that the proposing organization has a credible reason to pursue it.

Do not treat market size, AI hype, analyst enthusiasm, or technology novelty as sufficient evidence.

Follow `pm-business-case/references/EVIDENCE_CONTRACT.md`.

## Step 1: Define the market from the problem

Start with the customer problem and workflow, not a vendor category label.

Capture:

- target job or workflow
- user and buyer language
- trigger event
- current process
- desired outcome
- industry or regulatory context
- geography
- adjacent workflows

Generate a search taxonomy before concluding anything about competition or demand.

## Step 2: Why now

Search for and classify evidence of:

- regulatory change
- technology cost or capability shift
- buyer behavior change
- labor or operating cost pressure
- platform/ecosystem change
- new data availability
- competitor movement
- procurement pattern changes
- internal strategic trigger

Separate:

- structural signal
- cyclical signal
- vendor hype
- one-off anecdote

If "why now" is mostly marketing language, label it weak evidence.

## Step 3: Competitive search exhaustion gate

Never conclude "no competitors" from a first pass.

Search all applicable framings:

1. direct category terms
2. problem language
3. JTBD language
4. workflow language
5. buyer language
6. technology language
7. substitutes
8. manual workflows
9. build-in-house alternatives
10. incumbent enterprise suites
11. open-source options
12. regional players
13. niche entrants
14. emerging startups
15. adjacent categories
16. acronyms, synonyms, spelling variants, and legacy terminology

For each candidate, verify that the company or product exists and that its relevant capability is supported by an accessible source.

User-supplied competitors are leads, not facts.

### Contradiction pass

After the first landscape is built, explicitly try to disprove it:

- "Who competes without using this category name?"
- "What would an enterprise already own that reduces the need to buy this?"
- "What would a services firm, hyperscaler, incumbent suite, or internal engineering team use instead?"
- "Which regional or niche players would a local buyer encounter?"
- "What new entrants appeared recently?"

Only then may you say:

`No verified direct competitor was found after the documented search set. Adjacent alternatives and substitutes still exist. Coverage limitations: ...`

If retrieval or search fails, say `coverage incomplete / UNKNOWN`.

Never say "there are no competitors" unless the claim itself can be proved, which is rarely possible.

## Step 4: Competitor and alternative matrix

Classify each verified alternative as:

- direct competitor
- adjacent competitor
- substitute
- incumbent suite capability
- open source
- internal build
- manual workflow
- partner option

Capture only verified attributes.

Do not populate blank cells with guessed pricing, capabilities, customer counts, funding, market share, integrations, or geography.

Use `UNKNOWN` for unverified fields.

## Step 5: Market sizing

Use multiple methods where decision importance justifies it.

### Top-down

Use reputable market sources, but inspect category definitions and methodology.

### Bottom-up

Prefer a transparent model such as:

`reachable accounts x relevant units per account x annual value per unit`

or another model appropriate to the business.

### SAM

Constrain by:

- geography
- segment
- product capability
- deployment model
- regulation
- sales coverage
- integration requirements
- buyer eligibility

### SOM

Derive from reachability, not an arbitrary percentage of TAM.

Consider:

- target account count
- seller capacity
- sales cycle
- win rate hypothesis
- implementation capacity
- pricing
- adoption ramp
- time horizon

Every number is FACT or ESTIMATE with explicit inputs.

## Step 6: Reconcile conflicting market evidence

Do not average incompatible reports.

Compare:

- definitions
- base years
- forecast years
- included segments
- geography
- methodology
- source lineage
- commercial incentives

If reconciliation remains impossible, present a range and explain why.

## Step 7: Right-to-win

Assess the proposing organization against the opportunity.

Evidence may include:

- existing customers
- domain expertise
- proprietary data
- reusable technical assets
- distribution
- implementation capability
- ecosystem relationships
- switching leverage
- regulatory credibility
- operational advantage

For each claimed advantage ask:

- Is it real today?
- Is it differentiated?
- Is it relevant to buyer choice?
- Can competitors copy it?
- Does it reduce time, cost, or risk?

Label aspirational capabilities as PROPOSAL, not FACT.

## Step 8: Strategic alternatives

Compare:

- BUILD
- BUY or consume
- PARTNER or integrate
- DO NOTHING or continue current state

Add open source and incumbent platform options when relevant.

Score only evidence-backed dimensions:

- time to value
- total cost
- strategic control
- differentiation
- switching cost
- vendor dependency
- maintenance
- security/data implications
- operating burden
- reversibility
- opportunity cost

Avoid fake precision. If a score is subjective, label it as a judgment and explain the basis.

## Step 9: Output

Produce:

### Opportunity thesis
A short evidence-backed statement of problem, buyer, why now, and opportunity.

### Market evidence ledger
Claim IDs for key market facts and estimates.

### Competitive landscape
Verified alternatives with UNKNOWN fields preserved.

### Market sizing
Top-down and bottom-up where possible, with formulae and sensitivity.

### Right-to-win
Current evidence versus capabilities that still need to be built.

### Strategic alternatives
Build vs buy vs partner vs do nothing.

### Blocking unknowns
What evidence would materially change the recommendation.

## Hard stop conditions

Do not recommend BUILD when:

- competition coverage is incomplete and material;
- market size depends on unsupported numbers;
- there is no clear customer problem;
- right-to-win is merely asserted;
- an existing alternative appears materially better and has not been rebutted;
- the proposed market exists only because the technology label was chosen first.
