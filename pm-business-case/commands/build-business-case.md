---
description: Build a reliability-first business case with verified evidence, alternatives, falsifiable PoC, economics, GTM, red-team review, gated investment decision, and cross-skill claim-lineage preservation
argument-hint: "<initiative, capability, product, platform, or investment> [context/files]"
---

# /build-business-case

Build an investment-grade business case for `$ARGUMENTS`.

This command is fail-closed. Evidence comes before narrative. Missing proof becomes `UNKNOWN`, `ASSUMPTION`, `ESTIMATE`, `STALE`, `TARGET`, or `PROPOSAL`. Do not fill evidence gaps with plausible prose.

## Cross-Skill Lineage Consumer Contract

If upstream research, prospect discovery, client proof, analytics, PRD, or strategy includes claim IDs or a `Reliability Handoff`:

1. ingest inherited claims before creating the business-case evidence ledger;
2. preserve stable claim IDs for the same substantive claims;
3. preserve evidence state, source, scope, freshness, contradictions, caveats, attribution, publishability, and prohibited uses;
4. do not promote an inherited claim without explicit new evidence and promotion history;
5. do not broaden one account/segment/geography/time-period claim into market proof under the same claim ID;
6. derived business-case claims receive new claim IDs with parent claim IDs;
7. inherited P0 blockers remain blocking when material to BUILD/BUY/PARTNER;
8. repeated use of a claim across research, strategy, and business-case sections is not independent corroboration;
9. a `TARGET` remains a target and a `PROPOSAL` remains proposed until evidence supports a different factual claim;
10. restricted/client-confidential claims cannot become public GTM proof without clearance and a new appropriately scoped claim record.

If an inherited handoff is `PARTIAL` or `BLOCKED`, preserve that coverage status until missing evidence is actually obtained.

## Required Local Skills

Apply these skills in order:

1. **business-case-orchestrator** skill
2. **evidence-ledger** skill
3. **opportunity-market-proof** skill
4. **customer-jtbd-proof** skill
5. **economics-commercial-proof** skill
6. **investment-red-team** skill

Do not substitute looser external skills for these proof obligations.

## Step 0: Establish Decision Frame

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
- inherited coverage and P0 blockers

If information is incomplete, label assumptions and proceed only where safe. Do not invent missing organizational facts.

## Step 1: Create the Evidence Ledger First

Create `evidence-ledger.json` using `pm-business-case/references/EVIDENCE_LEDGER_TEMPLATE.json`.

Before drafting the business case:

- inventory supplied files and internal evidence;
- ingest upstream claim-lineage records when supplied;
- retrieve current external evidence where tools permit;
- verify sources by opening or inspecting them;
- preserve existing claim IDs for restatements;
- assign new claim IDs for new or derived P0 claims;
- record parent claim IDs for derived claims;
- mark source freshness;
- run contradiction checks;
- classify user assertions correctly;
- expose coverage gaps.

If external retrieval is unavailable, do not use model memory as factual evidence. Mark affected claims `UNKNOWN` or `STALE`.

## Step 2: Prove Opportunity, Competition, and Right-to-Win

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

Inherited competitive research remains at its original state/scope unless independently refreshed or corroborated.

## Step 3: Prove Customer and JTBD

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

Never fabricate personas or customer quotes. Discovery enthusiasm cannot be promoted to demand or WTP proof through business-case narration.

## Step 4: Define Solution Only After Proof

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

A solution claim derived from earlier problem/market/customer claims must link parent claim IDs.

## Step 5: Design Falsifiable PoC

Require:
- hypothesis
- baseline
- representative dataset/sample
- primary metric
- guardrails
- `DECISION_THRESHOLD`
- kill criterion
- failure modes
- what would invalidate the thesis
- what the PoC cannot prove

A demo is not validation. A PoC success does not automatically promote production-readiness, retention, WTP, repeatability, or platform claims.

## Step 6: Build Economics and Commercialization

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

Every material estimate needs formula and inputs. An inherited estimate retains its estimate method and state.

## Step 7: Platform/Reuse Gate

If the proposal includes "platform", "accelerator", "reusable IP", or equivalent, require evidence of reuse across multiple credible use cases or clients.

If unproven, downgrade to a narrower capability, experiment, or reusable project asset. A client-specific success claim cannot become reusable-platform proof by scope expansion.

## Step 8: Red-Team Before Recommendation

Produce the strongest evidence-backed rejection case from CEO, CTO, CFO, Sales/GTM, Delivery/Operations, Customer, and Competitor perspectives.

Then state what evidence would reverse the rejection.

Do not protect prior effort or the user's preferred outcome. Do not manufacture objections where evidence holds.

## Step 9: Validate Evidence and Handoff

When file execution is available, run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

When a machine-readable cross-skill handoff is produced, also run when available:

```bash
python reliability/kernel/validate_handoff.py handoff.json
```

If comparing against an upstream handoff:

```bash
python reliability/kernel/validate_handoff.py handoff.json --previous upstream-handoff.json
```

If validation fails:
- do not label the case investment-ready;
- fix the ledger/handoff where evidence exists;
- otherwise downgrade to `EXPERIMENT`, `DEFER`, `KILL`, or `NOT READY`.

Never weaken evidence or lineage rules to force a pass.

## Step 10: Produce Artifacts

When file writes are supported, create:

### `business-case.md`

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
Claim-level provenance and decision state, preserving inherited IDs where applicable.

### `assumption-register.md`
For every P0/P1 assumption include claim ID, owner, impact, validation method, decision threshold, and due condition/date if known.

### `decision-gates.md`
Record G0-G6 as PASS, FAIL, or NOT READY with evidence claim IDs.

### `handoff.json` or Reliability Handoff block

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Scope | Evidence | Freshness | Publishability | Downstream Restrictions |

### Derived Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Unresolved P0
[Claim IDs + blocker + evidence needed]

### Decision Status
[investment decision + blockers]

### Prohibited Interpretations
[e.g. PoC success != production readiness; market estimate != achieved revenue; client proof != platform proof]
```

## Allowed Final Decisions

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

No BUILD, BUY, or PARTNER decision is allowed while a material P0 claim is `UNKNOWN`, `STALE`, materially contradicted, unverified, or inherited as blocked.

## Final Response

Return:
- decision
- readiness
- 3 strongest reasons
- 3 strongest reasons the decision may be wrong
- blocking P0 claim IDs
- inherited claims that materially drive the decision
- new derived claim IDs
- next evidence-generating action
- artifact paths when created

Do not hide uncertainty in an appendix. Restating upstream evidence never strengthens it.
