---
name: business-case-orchestrator
description: "Orchestrate an evidence-led, gated business case from decision framing to investment recommendation. Use for product, AI, platform, accelerator, capability, migration, enterprise transformation, or solution business cases where hallucination control and decision readiness matter."
---

# Business Case Orchestrator

## Operating principle

Create investment-grade business cases that prefer `NOT READY` over unsupported confidence.

The correct sequence is:

`Decision -> Evidence ledger -> Market proof -> Customer/JTBD proof -> Alternatives -> Right-to-win -> Solution hypothesis -> Falsifiable PoC -> Economics -> GTM -> Reuse/platform gate -> Red-team -> Staged decision`

Do not start with a polished narrative, TAM slide, ROI claim, architecture diagram, platform roadmap, or AI buzzword and work backward to justification.

## Non-negotiable reliability contract

When file access is available, load and follow `pm-business-case/references/EVIDENCE_CONTRACT.md` before substantive work.

Rules:

1. Every material claim must be labeled as FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, or DECISION_THRESHOLD.
2. Never invent citations, quotes, competitors, market size, pricing, customer counts, benchmarks, product capabilities, dates, financial values, or sources.
3. Model memory is not decision-critical evidence.
4. User-provided competitors, market claims, metrics, and examples are leads unless they are explicitly provided as authoritative source-of-truth artifacts.
5. Search failure, retrieval failure, or tool unavailability means `coverage incomplete / UNKNOWN`, not absence.
6. Never conclude `no competitors`, `no demand`, `no risk`, or `clear ROI` from a first pass.
7. BUILD, BUY, or PARTNER recommendations are blocked while P0 evidence remains materially UNKNOWN, STALE, unverified, contradicted, or unresolved.
8. The answer must expose uncertainty in the executive layer, not bury it in appendices.

## Default behavior

Operate fail-closed. Move stage by stage. If a gate fails, output the failure, the blocking claims, and the cheapest next evidence action.

If the user asks for a quick executive narrative, still preserve evidence labels and readiness state. Do not use speed as permission to hallucinate.

## Stage 0: Decision frame

Define the decision before research.

Capture:

- decision to be made
- decision owner or audience
- organization context
- target customer or internal user
- geography and segment
- time horizon
- investment scale or capacity ask
- strategic objective
- constraints
- deadline
- out-of-scope decisions
- irreversible decisions being approached

### Gate G0: Scope readiness

Pass only when the decision can be stated in one sentence.

If not, output:

`NOT READY: decision scope ambiguous`

Then list the smallest missing inputs.

## Stage 1: Evidence intake and ledger

Apply `evidence-ledger` before writing the business case narrative.

Inventory:

- internal documents
- user-provided facts and claims
- external sources
- customer evidence
- competitor evidence
- commercial evidence
- technical evidence
- delivery evidence
- financial inputs
- prior work and reusable assets

Assign claim IDs to all decision-critical claims.

### Gate G1: Evidence readiness

Pass only when:

- decision-critical FACT claims have provenance
- source freshness is known
- contradictions were checked
- estimates have methods and inputs
- user claims are classified correctly
- unknowns and assumptions are visible

If not, continue in evidence-building mode.

## Stage 2: Opportunity and market proof

Apply `opportunity-market-proof`.

Test:

- why now
- market or workflow trigger
- direct competitors
- adjacent competitors
- substitutes
- manual workflows
- build-in-house alternatives
- incumbent-suite options
- open-source alternatives when relevant
- regional/niche/emerging players
- market size and reachable opportunity
- right-to-win

A weak first search triggers search expansion, not a negative conclusion.

## Stage 3: Customer and JTBD proof

Apply `customer-jtbd-proof`.

Separate:

- user
- buyer
- economic buyer
- approver
- blocker
- beneficiary
- operator

Validate:

- workflow
- pain severity
- frequency
- cost of current state
- current alternatives
- switching friction
- urgency
- willingness to change or pay
- adoption and governance constraints

If customer research is absent, label personas, JTBD, and pain as hypotheses.

### Gate G2: Problem and market readiness

Pass only when there is credible evidence of a problem worth solving for a segment worth testing.

Do not pass because the technology is fashionable or the market appears large.

Allowed outcomes:

- EXPERIMENT
- DEFER
- KILL
- NOT READY
- continue to alternatives analysis

## Stage 4: Strategic alternatives and right-to-win

Compare at minimum:

1. BUILD
2. BUY or consume
3. PARTNER or integrate
4. DO NOTHING or continue current workflow

Also evaluate open source, incumbent platforms, and services-led approaches where relevant.

For each option assess:

- customer outcome
- time to value
- total cost
- strategic control
- differentiation
- dependency risk
- maintenance burden
- data/security implications
- operating ownership
- reversibility
- opportunity cost

Right-to-win must be evidenced. Market attractiveness is not proof that this organization should build.

### Gate G3: Alternative readiness

A BUILD recommendation cannot pass without credible alternatives analysis and a defensible right-to-win thesis.

## Stage 5: Solution hypothesis

Only now define what should be built or tested.

State:

- target customer
- job or workflow
- proposed capability
- expected measurable outcome
- mechanism of value creation
- assumptions required
- explicit non-goals
- minimum proof asset

Do not label something a platform, agent, accelerator, or product unless the evidence supports that maturity level.

## Stage 6: PoC and falsification

Define a falsifiable PoC or experiment before material investment.

Required:

- hypothesis
- baseline
- representative sample/dataset/accounts
- primary metric
- guardrail metrics
- DECISION_THRESHOLD
- kill criterion
- failure modes
- what evidence invalidates the thesis
- what the PoC cannot prove

A demo is not a PoC. Technical success is not commercial validation. A pilot without a production path is not investment proof.

### Gate G4: Validation readiness

Pass only when the hypothesis can fail. If success is subjective or inevitable, redesign the experiment.

## Stage 7: Economics and commercialization

Apply `economics-commercial-proof`.

Model:

- build cost
- implementation cost
- operating cost
- support and maintenance
- presales cost
- pricing hypothesis
- gross margin where applicable
- revenue potential
- savings or productivity benefit
- payback
- bear/base/upside scenarios
- GTM wedge
- sales motion
- implementation path
- expansion path

Every material estimate must be reconstructable.

### Gate G5: Commercial readiness

No confident ROI, revenue, payback, pricing, or margin claim without traceable inputs.

No pricing recommendation without willingness-to-pay, comparable pricing, or explicitly labeled hypothesis.

## Stage 8: Reuse and platform gate

If the case proposes a reusable accelerator, productized solution, or platform, require evidence of:

- multiple credible use cases or clients
- common reusable components
- lower marginal delivery effort
- repeatable value
- operating ownership
- sales or strategic pull
- maintenance model
- governance model

One successful project does not prove platform potential.

If reuse is unproven, recommend a narrower capability, method, reusable asset, or evidence-generating pilot.

## Stage 9: Investment red-team

Apply `investment-red-team` before final recommendation.

Attack from these perspectives:

- CEO
- CTO or chief architect
- CFO
- Sales/GTM leader
- delivery/operations leader
- customer economic buyer
- incumbent competitor
- internal skeptic

Produce the strongest rejection case even if the final recommendation is positive.

## Stage 10: Final decision

Allowed decisions:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

For BUILD, BUY, or PARTNER, list the claim IDs that justify the decision.

For EXPERIMENT, specify evidence to create, owner, method, timeline, and decision threshold.

For NOT READY, list blocking claim IDs and the next evidence action.

### Gate G6: Investment readiness

When file execution is available, run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

If validation fails, the business case is not investment-ready. Do not override validator failure with narrative confidence.

## Required output structure

### Executive decision

- Decision
- Readiness: READY / EXPERIMENT / NOT READY / KILL
- Why now
- What must be true
- Top blocking unknowns
- Capital/capacity requested
- Next irreversible decision
- Confidence and reason

### Business case body

1. Decision frame
2. Evidence quality summary
3. Market signal and why now
4. ICP, buyer, user, and JTBD
5. Current workflow and quantified pain
6. Alternatives and competitive landscape
7. Market size and reachable opportunity
8. Right-to-win
9. Build vs buy vs partner vs do nothing
10. Solution hypothesis
11. PoC and falsification plan
12. Economics and scenario analysis
13. Pricing and WTP evidence
14. GTM and commercialization
15. Reuse and platform gate
16. Risks, contradictions, and kill criteria
17. Red-team rejection case
18. Final recommendation and staged investment
19. Evidence gaps and next evidence plan

## Required companion artifacts

When file writes are available, create or update:

- `business-case.md`
- `evidence-ledger.json`
- `assumption-register.md`
- `decision-gates.md`
- `red-team.md`

## Hard failure conditions

Return `NOT READY`, `EXPERIMENT`, or `KILL` when:

- the decision frame is ambiguous
- P0 evidence is missing
- customer demand is inferred only from market size
- competitor coverage is incomplete and material
- right-to-win is asserted rather than evidenced
- build/buy/partner/do-nothing was not compared
- PoC cannot fail
- ROI cannot be reconstructed
- platform reuse is assumed from one project
- unresolved contradictions change the decision

## Final self-check

Before delivery, verify:

- claim labels are visible
- P0 unknowns are in the executive section
- no fabricated facts or citations appear
- alternatives were compared
- red-team rejection case is included
- decision is staged where uncertainty remains
- recommendation follows evidence, not user preference
