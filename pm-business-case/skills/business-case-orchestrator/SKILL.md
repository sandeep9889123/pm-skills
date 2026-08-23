---
name: business-case-orchestrator
description: "Build an evidence-led, gated business case from decision framing through investment recommendation. Use when creating, rebuilding, automating, or reviewing a business case for a product, capability, platform, AI initiative, accelerator, or major investment."
---
# Business Case Orchestrator

## Purpose

Create investment-grade business cases that prefer `NOT READY` over unsupported certainty.

The correct sequence is:

`Signal -> Customer -> JTBD -> Alternatives -> Right-to-win -> Build/Buy/Partner/Do Nothing -> Hypothesis -> PoC -> Evidence -> Economics -> GTM -> Investment Decision -> Reuse -> Platform`

Do not start with a polished narrative, architecture, TAM slide, ROI claim, or platform roadmap and work backward to justification.

## Mandatory evidence contract

Before substantive work, load and follow `pm-business-case/references/EVIDENCE_CONTRACT.md` when file access is available.

Non-negotiable rules:

- Every material claim is one of FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, or DECISION_THRESHOLD.
- Never invent a citation, quote, competitor, customer, market size, benchmark, price, capability, financial value, date, or source.
- Model memory is not decision-critical evidence.
- User-supplied competitors and market claims are leads unless verified or explicitly supplied as authoritative internal source-of-truth evidence.
- Tool/search failure means `coverage incomplete / UNKNOWN`, not absence.
- Never conclude "no competitors", "no demand", "no risk", or equivalent from a first pass.
- A BUILD, BUY, or PARTNER recommendation is prohibited while P0 evidence remains materially UNKNOWN, STALE, unverified, or unresolved.

## Default operating mode

Use a fail-closed workflow. Work stage by stage. Do not skip a failed gate because the user asks for an executive-ready output quickly.

If evidence is missing, continue only where the work can be explicitly labeled hypothesis, estimate, proposal, or unknown. Do not fill gaps with plausible prose.

## Stage 0: Decision frame

Define the decision before research.

Capture:

- decision to be made
- decision owner
- organization or product context
- time horizon
- geography
- target customer or internal user if known
- investment scale if known
- strategic objective
- constraints
- deadline
- what decisions are out of scope

If the request is ambiguous, make the minimum safe assumptions and label them. Do not silently broaden the scope.

### Gate G0: Scope readiness

Pass only when the decision can be stated in one sentence.

If not, output `NOT READY: decision scope ambiguous` and list the smallest missing inputs.

## Stage 1: Evidence intake and ledger

Apply the **evidence-ledger** skill.

Create `evidence-ledger.json` before writing the business case narrative.

Inventory:

- supplied internal documents
- user-provided facts and claims
- external sources
- existing research
- prior business cases
- customer evidence
- commercial evidence
- technical evidence
- financial inputs

Assign claim IDs to all decision-critical claims.

### Gate G1: Evidence readiness

Before promoting evidence into the narrative, verify:

- decision-critical FACT claims have adequate provenance;
- source freshness is known;
- contradictions were checked;
- external claims were retrieved rather than recalled;
- estimates have methods and sourced inputs;
- unknowns and assumptions are visible.

If not, continue in evidence-building mode. Do not draft a confident executive recommendation.

## Stage 2: Opportunity and market proof

Apply the **opportunity-market-proof** skill.

Test:

- what changed and why now;
- market or workflow trigger;
- direct competitors;
- adjacent competitors;
- substitutes and manual workflows;
- build-in-house alternatives;
- incumbent suites;
- open-source alternatives when relevant;
- regional players;
- niche and emerging entrants;
- market size and reachable opportunity;
- right-to-win.

A weak first search triggers expansion, not a negative conclusion.

## Stage 3: Customer and JTBD proof

Apply the **customer-jtbd-proof** skill.

Separate:

- user
- buyer
- economic buyer
- approver
- blocker
- beneficiary

Validate:

- workflow and context
- JTBD
- pain severity
- frequency
- cost of current state
- current alternatives
- switching friction
- urgency
- evidence of willingness to change or pay

If customer research is absent, label personas and JTBD as hypotheses.

### Gate G2: Problem and market readiness

Pass only when there is credible evidence of a problem worth solving and a target segment worth testing.

Do not pass because the technology is fashionable or the market appears large.

Fail options:

- EXPERIMENT to gather customer or market proof
- DEFER if timing is weak
- KILL if evidence contradicts the opportunity
- NOT READY if coverage is inadequate

## Stage 4: Strategic alternatives and right-to-win

Compare at minimum:

1. BUILD
2. BUY or consume
3. PARTNER or integrate
4. DO NOTHING or continue the current workflow

Also evaluate open source or incumbent platform capabilities where relevant.

For each option assess:

- customer outcome
- time to value
- total cost
- strategic control
- differentiation
- dependency risk
- maintenance burden
- data and security implications
- talent and operating requirements
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
- mechanism by which the outcome is created
- assumptions required
- explicit non-goals

Do not prematurely label the solution a "platform" or "agentic" product if a narrower capability can test the thesis.

## Stage 6: PoC and falsification

Define a falsifiable PoC or experiment before material investment.

Required:

- hypothesis
- credible baseline
- evaluation dataset or sample
- primary metric
- guardrail metrics
- DECISION_THRESHOLD
- kill criterion
- failure modes
- what evidence would invalidate the thesis
- what the PoC cannot prove

A demo is not a PoC. A technical PoC is not commercial validation.

### Gate G4: Validation readiness

Pass only when the hypothesis can fail.

If the experiment is constructed so success is inevitable or subjective, redesign it.

## Stage 7: Economics and commercialization

Apply the **economics-commercial-proof** skill.

Model:

- build cost
- implementation cost
- operating cost
- support and maintenance
- pricing hypothesis
- gross margin where applicable
- revenue potential
- cost savings or productivity benefit
- payback
- scenario ranges
- GTM wedge
- sales motion
- implementation path
- expansion path

Every material estimate must be reconstructable. Do not hide assumptions inside formulas.

### Gate G5: Commercial readiness

No confident ROI, pricing, revenue, or payback claim without traceable inputs.

No confident pricing recommendation without WTP or comparable commercial evidence.

## Stage 8: Reuse and platform gate

If the case proposes a reusable accelerator or platform, require evidence of:

- multiple credible use cases or clients;
- common reusable components;
- reduced marginal delivery effort;
- repeatable value;
- operating ownership;
- commercial or strategic pull.

One project does not establish platform potential.

If reuse is unproven, recommend a narrower capability or reusable project asset first.

## Stage 9: Investment red team

Apply the **investment-red-team** skill.

Attack the business case from the perspective of:

- CEO
- CTO or chief architect
- CFO
- Sales or GTM leader
- delivery or operations leader
- customer economic buyer
- incumbent competitor

Produce the strongest rejection case before the recommendation.

## Stage 10: Final decision

Allowed decisions:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

For BUILD, BUY, or PARTNER, identify the claim IDs that justify the decision.

For EXPERIMENT, specify exactly what evidence must be created next and the decision threshold.

For NOT READY, list blocking claim IDs.

### Gate G6: Investment readiness

Before finalizing:

1. Run the evidence validator when file execution is available:
   `python pm-business-case/scripts/validate_evidence.py evidence-ledger.json`
2. If validation fails, the business case is not investment-ready.
3. Do not override validator failure with narrative confidence.

## Required output structure

### Executive decision
- Decision
- Decision readiness
- Why now
- What must be true
- Top blocking unknowns
- Capital or effort requested
- Next irreversible decision

### 1. Decision frame
### 2. Evidence quality summary
### 3. Market signal and why now
### 4. ICP, buyer, user, and JTBD
### 5. Current workflow and quantified pain
### 6. Alternatives and competitive landscape
### 7. Market size and reachable opportunity
### 8. Right-to-win
### 9. Build vs buy vs partner vs do nothing
### 10. Solution hypothesis
### 11. PoC and falsification plan
### 12. Economics and scenario analysis
### 13. Pricing and willingness-to-pay evidence
### 14. GTM and commercialization
### 15. Reuse and platform gate
### 16. Risks, contradictions, and kill criteria
### 17. Red-team rejection case
### 18. Final recommendation and staged investment
### 19. Evidence gaps and next evidence plan

## Required companion artifacts

When file writes are available, create:

- `business-case.md`
- `evidence-ledger.json`
- `assumption-register.md`
- `decision-gates.md`

Never hide unresolved evidence in appendices. Decision-critical uncertainty belongs in the executive layer.
