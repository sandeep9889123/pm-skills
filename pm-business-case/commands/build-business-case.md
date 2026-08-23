---
description: Build a reliability-first business case with verified evidence, alternatives, falsifiable PoC, economics, GTM, red-team review, and gated investment decision
argument-hint: "<initiative, capability, product, platform, or investment> [context/files]"
---

# /build-business-case

Build an investment-grade business case for `$ARGUMENTS`.

This command is fail-closed. Evidence comes before narrative. Missing proof becomes UNKNOWN, ASSUMPTION, ESTIMATE, STALE, or PROPOSAL. Do not fill evidence gaps with plausible prose.

## Required local skills

Apply these skills in order:

1. **business-case-orchestrator** skill
2. **evidence-ledger** skill
3. **opportunity-market-proof** skill
4. **customer-jtbd-proof** skill
5. **economics-commercial-proof** skill
6. **investment-red-team** skill

Do not substitute looser external skills for these proof obligations.

## Step 0: Establish decision frame

From the user request and supplied artifacts, infer the narrowest safe decision frame:

- decision
- owner
- objective
- scope
- geography
- time horizon
- investment horizon
- constraints
- known internal facts
- unknowns

If information is incomplete, label assumptions and proceed only where safe. Do not invent missing organizational facts.

## Step 1: Create the evidence ledger first

Create `evidence-ledger.json` using `pm-business-case/references/EVIDENCE_LEDGER_TEMPLATE.json`.

Before drafting the business case:

- inventory supplied files and internal evidence;
- retrieve current external evidence where tools permit;
- verify sources by opening or inspecting them;
- record claim IDs for every P0 claim;
- mark source freshness;
- run contradiction checks;
- classify user assertions correctly;
- expose coverage gaps.

If external retrieval is unavailable, do not use model memory as factual evidence. Mark affected claims UNKNOWN or STALE.

## Step 2: Prove opportunity, competition, and right-to-win

Run the full search exhaustion gate before negative conclusions.

Cover:

- why now
- direct competitors
- adjacent competitors
- substitutes
- manual workflows
- in-house build
- incumbent suites
- open-source alternatives
- regional players
- niche and emerging entrants
- market sizing
- reachable market
- right-to-win
- build vs buy vs partner vs do nothing

If the first pass finds no competitor, broaden and contradict the result. Never treat zero search results as proof of absence.

## Step 3: Prove customer and JTBD

Separate user, buyer, economic buyer, approver, and blocker.

Validate or label as hypotheses:

- workflow
- JTBD
- pain severity
- frequency
- current alternative
- consequence
- urgency
- switching friction
- willingness to change
- willingness to pay

Never fabricate personas or customer quotes.

## Step 4: Define solution only after proof

State the narrowest solution hypothesis that can test the opportunity.

Do not begin with a platform assumption.

Define:

- target actor
- job/workflow
- capability
- expected outcome
- mechanism
- non-goals
- assumptions

## Step 5: Design falsifiable PoC

Require:

- hypothesis
- baseline
- representative dataset/sample
- primary metric
- guardrails
- DECISION_THRESHOLD
- kill criterion
- failure modes
- what would invalidate the thesis
- what the PoC cannot prove

A demo is not validation.

## Step 6: Build economics and commercialization

Model transparently:

- build cost
- deploy cost
- recurring operating cost
- sales/presales cost
- benefit pools
- bear/base/bull scenarios
- pricing evidence
- unit economics where applicable
- payback
- GTM wedge
- pilot-to-production path
- expansion path
- reuse economics if relevant

Every material estimate needs formula and inputs.

## Step 7: Platform/reuse gate

If the proposal includes "platform", "accelerator", "reusable IP", or equivalent, require evidence of reuse across multiple credible use cases or clients.

If unproven, downgrade to a narrower capability, experiment, or reusable project asset.

## Step 8: Red-team before recommendation

Produce the strongest rejection case from CEO, CTO, CFO, Sales/GTM, Delivery/Operations, Customer, and Competitor perspectives.

Then state what evidence would reverse the rejection.

Do not protect prior effort or the user's preferred outcome.

## Step 9: Validate evidence

When file execution is available, run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

If validation fails:

- do not label the case investment-ready;
- fix the ledger where evidence exists;
- otherwise downgrade the recommendation to EXPERIMENT, DEFER, KILL, or NOT READY.

Never weaken the evidence rules to force a pass.

## Step 10: Produce artifacts

When file writes are supported, create:

### `business-case.md`

Structure:

1. Executive decision
2. Decision frame
3. Evidence quality and coverage
4. Why now
5. ICP, actors, and JTBD
6. Current workflow and quantified pain
7. Alternatives and competitive landscape
8. Market size and reachable opportunity
9. Right-to-win
10. Build vs buy vs partner vs do nothing
11. Solution hypothesis
12. PoC and falsification
13. Economics and scenario analysis
14. Pricing and WTP evidence
15. GTM and commercialization
16. Reuse/platform gate
17. Risks, contradictions, and kill criteria
18. Strongest rejection case
19. Final recommendation and staged investment
20. Evidence gaps and next evidence plan

### `evidence-ledger.json`
Claim-level provenance and decision state.

### `assumption-register.md`
For every P0/P1 assumption include owner, impact, validation method, decision threshold, and due condition/date if known.

### `decision-gates.md`
Record G0-G6 as PASS, FAIL, or NOT READY with evidence claim IDs.

## Allowed final decisions

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

No BUILD, BUY, or PARTNER decision is allowed while a P0 claim is UNKNOWN, STALE, materially contradicted, or unverified.

## Final response

Return:

- decision
- readiness
- 3 strongest reasons
- 3 strongest reasons the decision may be wrong
- blocking P0 claim IDs
- next evidence-generating action
- artifact paths when created

Do not hide uncertainty in an appendix.
