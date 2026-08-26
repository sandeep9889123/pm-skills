---
description: Create an evidence-led go-to-market launch plan with beachhead, ICP, buying journey, proof, channels, readiness gates, learning milestones, and inherited claim-lineage preservation
argument-hint: "<product or feature to launch>"
---

# /plan-launch - Evidence-Led Go-to-Market Plan

Build a GTM plan from the evidence available. Do not invent TAM/SAM/SOM, ICP attributes, buyer titles, pricing, channel ROI, launch targets, timelines, proof points, or demand merely to produce a complete launch artifact.

## Reliability Contract

- Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`, `TARGET`, and `PROPOSAL`.
- A launch deadline does not override unresolved product, customer, security, delivery, pricing, legal, or measurement blockers.
- Do not force a single beachhead if evidence cannot distinguish segments. `TEST TWO SEGMENTS` or `NO BEACHHEAD READY` are valid outcomes.
- ICP must distinguish account, buyer, champion, user, procurement, security, executive sponsor, and blocker where relevant. Unknown roles remain `UNKNOWN`.
- Do not invent market size. If TAM/SAM/SOM is not needed for the immediate launch decision or cannot be reconstructed, omit it or mark `MARKET SIZE UNKNOWN`.
- Do not rank channels by expected ROI without evidence. Use experiments when channel economics are unknown.
- Never invent 30-day or 90-day targets. Use measured baselines, explicit `TARGET` values supplied by stakeholders, or define what must be calibrated.
- A successful demo or pilot is not proof of production readiness, repeatable sales, retention, or scalable delivery.
- Expansion is gated by beachhead learning and delivery quality, not an arbitrary market-share threshold.
- Keep claims NDA-safe and evidence-backed.

## Cross-Skill Lineage Consumer Contract

When analytics, research, discovery, client proof, PRD, business case, or shipping-readiness artifacts provide claim IDs / a `Reliability Handoff`:

- preserve stable IDs for restated claims;
- preserve state, scope, freshness, evidence refs, estimate method, contradictions, caveats, publishability, and restrictions;
- do not turn a measured analytical pattern into causal launch proof unless the evidence supports causality;
- do not turn p-value/significance alone into launch readiness or practical value;
- do not turn a client-specific outcome into universal launch proof;
- do not turn a `TARGET` into a baseline or achieved result;
- do not turn a `PROPOSAL`/pilot result into production readiness;
- create new parent-linked claims for launch-specific inferences such as expected ICP fit, channel response, or commercial outcome;
- inherited unresolved P0 blockers stay blocking when material;
- inherited `PARTIAL`/`BLOCKED` coverage cannot become complete because the launch plan is polished.

A decision to `LAUNCH` is a fact about the decision. It does not promote every supporting claim to `FACT`.

## Workflow

### Step 1: Resolve Launch Context and Inherited Evidence

Capture:
- what is launching
- launch stage and decision deadline
- target geography / market boundary
- user, buyer, payer, and account
- current alternatives
- product readiness and known limitations
- pricing/packaging status
- delivery / implementation model
- security, privacy, regulatory, procurement constraints
- available customer and market evidence
- upstream claim IDs and evidence coverage
- material unknowns / inherited P0 blockers

### Step 2: Beachhead Decision

Apply **beachhead-segment**.

Evaluate plausible segments on evidence for:
- problem urgency / consequence
- observable buying trigger
- WTP / budget pathway
- reachability
- right-to-win / proof
- implementation fit
- referenceability / expansion logic
- strategic fit

Outcome:

`FOCUS | PILOT BEACHHEAD | TEST TWO SEGMENTS | HOLD | NO BEACHHEAD READY`

Do not select a segment solely because TAM is large. Any new segment-fit conclusion derived from broader evidence receives a new claim ID with parent IDs.

### Step 3: ICP and Buying Journey

Apply **ideal-customer-profile**.

Define only supported attributes:
- account characteristics
- triggering situation
- primary JTBD
- current alternative
- qualification signals
- disqualification / anti-ICP signals
- user / champion / buyer / approver / blocker roles
- proof required at each decision stage

If the buying process is unknown, state `BUYING JOURNEY UNKNOWN` and include discovery actions.

### Step 4: GTM Strategy

Apply **gtm-strategy** and **gtm-motions**.

For each plausible motion/channel evaluate:
- why the ICP can be reached there
- evidence of intent or prior response
- sales / marketing / product capacity required
- economics when reconstructable
- time-to-learning
- delivery consequences
- guardrails

Use `SUPPORTED | TEST | UNKNOWN | REJECT` rather than unsupported ROI rankings. Channel-response hypotheses are derived claims, not inherited FACTs.

### Step 5: Proof and Messaging

For each stakeholder:
- problem / outcome language
- relevant proof claim IDs
- objection / risk
- evidence gap
- publishability / allowed-use restriction

Do not claim ROI, accuracy, speed, customer outcomes, integrations, security posture, or competitive superiority without support. Restricted proof stays restricted.

### Step 6: Production Path and Launch Readiness

Check:
- product acceptance criteria
- support / onboarding / implementation
- observability and analytics
- security/privacy/compliance
- commercial terms
- sales-to-delivery handoff
- rollback / incident path
- ownership
- inherited PoC/readiness coverage and blockers

Classify blockers `P0 | P1 | P2`.

A launch is blocked when unresolved P0 issues can create unacceptable customer, legal, financial, security, or delivery risk.

A successful PoC claim keeps its PoC scope unless new production evidence exists.

### Step 7: Metrics and Learning Milestones

Define:
- activation / value metric
- qualification and conversion metrics
- delivery / implementation quality
- retention / repeat-use signal
- economics where observable
- guardrails

Targets must be labelled `TARGET`; baselines must be observed. If neither exists, specify calibration rather than inventing a number.

When using analytics claims:
- preserve the original metric/data contract;
- separate observed effect from causal interpretation;
- preserve validity caveats such as SRM, censoring, segment-mix, instrumentation, or post-hoc analysis.

Use learning milestones instead of arbitrary calendar promises where evidence is immature.

### Step 8: Decision

`LAUNCH | LIMITED PILOT | TEST GTM | FIX P0 BLOCKERS | HOLD | NO-GO`

For each decision state what would change it and which supporting claim IDs remain uncertain.

## Output

```text
## Go-to-Market Decision: [Product]

### Decision Context
[stage, market, deadline, consequence]

### Inherited Evidence Ledger
| Claim ID | Claim | State | Scope | Evidence | Freshness | Restriction | Launch Use |

### Beachhead
[decision + evidence claim IDs + alternatives]

### ICP / Anti-ICP
[account, JTBD, qualification, disqualification]

### Buying Journey
[roles and proof requirements, or BUYING JOURNEY UNKNOWN]

### Positioning and Proof
[stakeholder message + allowed proof IDs + gap]

### GTM Motions
| Motion | Supporting Claim IDs | ICP Reachability | Evidence State | Economics | Capacity | Guardrails | Status |

### Production Readiness
[P0/P1/P2 blockers + source claim IDs]

### Metrics and Learning Milestones
[baselines, TARGETS, metric contracts, calibration needs]

### Derived Launch Claims
| Claim ID | Parent IDs | Derivation | State | Scope | Caveats |

### Risks / Failure Modes
[customer, delivery, commercial, security, compliance]

### Decision
[LAUNCH | LIMITED PILOT | TEST GTM | FIX P0 BLOCKERS | HOLD | NO-GO]

### What Would Change the Recommendation
[specific evidence / claim-state changes]

## Reliability Handoff
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED
Unresolved P0: [claim IDs + evidence needed]
Prohibited interpretations: [launch approval != evidence promotion; significance != practical value; pilot != production]
```

## Notes

- A polished launch calendar is not evidence of launch readiness.
- Tight targeting improves learning only when the chosen segment is evidence-backed.
- Post-launch expansion follows repeatable value, delivery, and economics, not arbitrary elapsed time.
- Restating upstream evidence never strengthens it.
