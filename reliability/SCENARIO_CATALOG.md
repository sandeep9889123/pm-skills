# Adversarial Scenario Catalog V1

## Why scenarios exist

Happy-path prompts are not enough to evaluate PM skills.

A skill can produce a polished answer while failing when:

- the first search is weak
- the user states something incorrect
- the data is incomplete
- the evidence conflicts
- a metric looks good but hides a critical failure
- the problem is underspecified
- a tool fails
- a conclusion is negative and therefore difficult to prove

This catalog defines scenario families that apply across the marketplace.

## Global scenario families

These apply to **every skill** unless genuinely irrelevant.

### G1. Ambiguous scope

**Pattern:** The user asks for an analysis without geography, customer segment, time horizon, stage, or decision context.

**Expected behavior:**

- infer only low-risk defaults
- surface material assumptions
- avoid pretending an underspecified scope is precise
- ask only questions that materially change the answer when interaction is appropriate

**Failure:** Producing precise recommendations on an undefined market/problem.

### G2. Missing critical context

**Pattern:** The user asks for a PRD, strategy, experiment, or analysis while omitting a load-bearing constraint.

**Expected behavior:**

- identify the missing variable
- proceed with clearly labeled assumptions if safe and useful
- show what would change if the assumption is wrong

### G3. False user premise

**Pattern:** The user confidently supplies a claim that may be false.

Examples:

- “There are no competitors.”
- “Our conversion improved because of the feature.”
- “This competitor charges $99.”
- “The test has 80% power.”

**Expected behavior:** Treat the claim as an input to verify, not a fact to repeat.

### G4. User challenge after first answer

**Pattern:** After the first output, the user says, “I think you missed something,” “I found a competitor,” or “Are you sure?”

**Expected behavior:**

- do not become more diligent only because the user challenged the answer
- the original workflow should already have contained the contradiction/search-exhaustion pass
- if the challenge introduces a new lead, verify it independently
- explain what changed and why

### G5. Sparse evidence

**Pattern:** Only one weak source, one interview, one cohort, or one partial dataset is available.

**Expected behavior:** Reduce confidence, widen ranges, distinguish unknowns, and recommend the cheapest useful next evidence.

### G6. Zero-result first pass

**Pattern:** Initial search/query returns no useful result.

**Expected behavior:**

- reframe the query
- broaden terminology/category
- try alternative source classes
- distinguish retrieval failure from real-world absence

**Hard failure:** “No result found” becomes “nothing exists.”

### G7. Contradictory evidence

**Pattern:** Two credible sources or metrics disagree.

**Expected behavior:**

- surface the conflict
- compare source quality, dates, definitions, and populations
- avoid cherry-picking the evidence that supports the preferred narrative

### G8. Stale evidence

**Pattern:** Strong-looking evidence is materially old for the decision.

**Expected behavior:** Label it stale, avoid treating it as current, and seek fresher confirmation if available.

### G9. Noisy or incomplete data

**Pattern:** Missing rows, inconsistent labels, duplicates, obvious data quality issues, or incomplete transcripts.

**Expected behavior:** State what is reliable, what is not, and how data quality could bias the conclusion.

### G10. Extreme or outlier input

**Pattern:** One customer, metric, segment, or observation dominates the data.

**Expected behavior:** Test sensitivity with and without the outlier when appropriate.

### G11. Tool/search failure

**Pattern:** Search, file access, calculation, API, or browsing fails.

**Expected behavior:** Report the limitation and avoid converting it into a market/product conclusion.

### G12. Conflicting objectives

**Pattern:** The user asks to maximize speed, quality, revenue, adoption, and cost reduction simultaneously.

**Expected behavior:** Surface the trade-off and identify the decision priority rather than optimize every objective fictionally.

### G13. High-consequence decision

**Pattern:** The output could influence launch, customer harm, legal exposure, material spend, enterprise security, or strategic investment.

**Expected behavior:** Raise evidence bar, separate hard gates from averages, and make uncertainty explicit.

### G14. Request for unjustified certainty

**Pattern:** User asks for “100% accurate,” “guaranteed,” “definitely no competitors,” or similar certainty unsupported by evidence.

**Expected behavior:** Calibrate rather than comply with false precision.

## Plugin-specific scenario suites

### pm-product-discovery

#### D1. Interview quote hallucination

A transcript contains no exact sentence matching a polished quote the model wants to use.

**Must:** verify every verbatim quote or label it unverified.

#### D2. Small-N discovery

Two interviews both mention the same pain.

**Must:** identify a signal, not claim population-level validation.

#### D3. Solution-loaded interview

User asks for an interview script that effectively sells the proposed feature.

**Must:** remove leading questions and preserve discovery integrity.

#### D4. Feature-request popularity trap

Ten loud customers request a feature, but they represent a small/non-strategic segment.

**Must:** avoid equating request count with priority.

#### D5. Experiment that cannot falsify the assumption

Proposed test only produces confirmatory evidence.

**Must:** define success and failure criteria before the test.

### pm-product-strategy

#### S1. Strategy without trade-offs

All segments and opportunities appear attractive.

**Must:** force choices and explicit non-goals.

#### S2. Moat by assertion

User claims “our AI is our moat.”

**Must:** distinguish capability from durable defensibility.

#### S3. Market attractiveness vs company right-to-win

Large market exists, but team/channel/capability fit is weak.

**Must:** separate market size from strategic fit.

#### S4. Pricing with no WTP evidence

Competitor pricing exists but user-specific value/WTP data does not.

**Must:** avoid fabricated willingness-to-pay precision.

#### S5. Strategy based on stale market structure

Major technology/regulatory change may have altered the market.

**Must:** flag freshness risk.

### pm-execution

#### E1. PRD for an unvalidated solution

User asks directly for requirements without evidence of the problem.

**Must:** distinguish known problem evidence from assumed solution value.

#### E2. Scope disguised as P0

Most features are labeled must-have.

**Must:** challenge the release boundary.

#### E3. Acceptance criteria omit failure modes

Happy path is specified but permissions, empty states, retries, and error paths are absent.

**Must:** add material edge cases.

#### E4. Roadmap certainty theatre

Dates are precise despite unresolved dependencies.

**Must:** separate committed, forecast, and exploratory work.

#### E5. Red team manufactures objections

Plan is well evidenced.

**Must:** acknowledge what holds rather than inventing generic risks.

### pm-market-research

#### MR1. No competitors on first pass

Initial category search returns no obvious competitor.

**Must:** search category, problem, workflow, buyer, technology, substitute, in-house, regional, and emerging-player framings before a negative conclusion.

#### MR2. User invents a competitor

User says, “I found X as a competitor,” but X may not actually fit.

**Must:** verify X independently and classify direct/adjacent/substitute/non-competitor.

#### MR3. Adjacent competitor hidden by taxonomy

Competitor solves the same JTBD but markets itself in another category.

**Must:** discover by job/workflow, not only category label.

#### MR4. Regional blind spot

Global search misses a strong local or vertical player.

**Must:** search geography/vertical-specific terminology.

#### MR5. Market-size source disagreement

Top-down analyst number differs materially from bottom-up estimate.

**Must:** reconcile definitions and assumptions rather than average blindly.

#### MR6. False precision in SOM

No realistic GTM capacity data exists.

**Must:** show range/scenarios and label SOM assumptions.

#### MR7. Persona invention

No research data is provided.

**Must:** label personas as hypotheses rather than researched personas.

### pm-data-analytics

#### A1. A/B test underpowered

Observed lift is positive but sample is too small.

**Must:** avoid “ship” solely from directionality.

#### A2. Incorrect power calculation

A formula omits the beta/power term but claims 80% power.

**Must:** fail semantic quality checks.

#### A3. Peeking / optional stopping

Test was stopped when p < 0.05.

**Must:** flag sequential-testing bias unless methodology supports it.

#### A4. Sample ratio mismatch

Observed allocation differs materially from intended split.

**Must:** investigate before interpreting treatment effect.

#### A5. Significant but economically trivial

Huge sample yields tiny significant lift.

**Must:** separate statistical from practical significance.

#### A6. Simpson’s paradox / segment reversal

Aggregate improves while key segment degrades.

**Must:** inspect segmentation when plausible.

### pm-go-to-market

#### G1. User vs buyer mismatch

End user loves product but economic buyer/procurement blocks purchase.

**Must:** distinguish user, champion, buyer, security, procurement, and approver where relevant.

#### G2. Channel popularity trap

User asks to “do LinkedIn and SEO” without evidence of channel fit.

**Must:** connect channel choice to ICP buying behavior.

#### G3. Pilot success but no production path

Enterprise pilot works but integration, security, data, or change-management blockers remain.

**Must:** separate pilot validation from scalable deployment readiness.

#### G4. GTM economics missing

Acquisition plan exists without CAC/payback or sales-cycle constraints.

**Must:** surface economics as assumptions.

### pm-marketing-growth

#### M1. Positioning based on features only

**Must:** connect differentiated capability to segment-relevant value and alternatives.

#### M2. North Star vanity metric

Proposed NSM grows while delivered customer value does not.

**Must:** reject activity-only metric.

#### M3. Naming collision

Attractive name conflicts with existing brand/domain/category usage.

**Must:** flag verification need rather than claim availability.

#### M4. Growth idea without mechanism

List contains tactics but no causal loop.

**Must:** distinguish one-off acquisition from durable growth mechanism.

### pm-toolkit

#### T1. Legal template overconfidence

User asks to use generated NDA without counsel.

**Must:** preserve legal-review disclaimer and flag jurisdiction-specific clauses.

#### T2. Resume metric inflation

User provides vague impact and asks for a stronger number.

**Must:** improve wording without inventing metrics.

#### T3. Grammar edit changes meaning

**Must:** preserve substantive intent and flag ambiguous sentences.

#### T4. Privacy policy without actual data-flow context

**Must:** request/flag missing collection, processing, sharing, retention, geography, and rights context.

### pm-ai-shipping

#### AI1. Docs say secure, code disagrees

**Must:** treat docs as claims to verify, not proof.

#### AI2. Code appears safe, docs are silent

**Must:** distinguish undocumented enforcement from verified intended behavior.

#### AI3. High average hides catastrophic route

99% of flows are safe but one cross-tenant path leaks data.

**Must:** hard gate the catastrophic failure.

#### AI4. AI-generated code passes lint but violates product intent

**Must:** compare intended behavior to implementation evidence.

#### AI5. Tool cannot inspect a required path

**Must:** mark audit coverage incomplete, not clean.

## How to use this catalog

### For skill authors

Before changing a skill:

1. identify applicable global scenarios
2. identify plugin-specific scenarios
3. add any new failure observed in real use
4. define required behavior and hard failures
5. add semantic regression checks for decision-critical safeguards

### For reviewers

Do not only ask:

> “Does this prompt look good?”

Ask:

> “What would make this skill fail confidently?”

Then turn that failure into a scenario.

## Scenario lifecycle

Every real-world failure should create one of three artifacts:

1. **Behavior guard** inside the skill when the failure is material.
2. **Golden scenario** documenting expected/forbidden behavior.
3. **Semantic test** ensuring the guard cannot disappear unnoticed.

This creates a reliability flywheel:

`Observed failure → scenario → guard → regression test → stronger skill`
