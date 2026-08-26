---
name: create-prd
description: "Create a decision-first Product Requirements Document that preserves upstream discovery/research evidence states, claim IDs, scope, blockers, acceptance criteria, and release gates. Use when writing a PRD, feature spec, or reviewing an existing PRD."
---

# Create a Product Requirements Document

## Purpose

Create a PRD that records the product decision and the evidence behind it, not merely a polished specification.

## Context

A strong PRD aligns product, design, engineering, data, delivery, GTM, and leadership on the problem, scope, behavior, quality bar, risks, and what remains unproven.

## Cross-Skill Lineage Consumer Contract

When upstream discovery, research, analytics, business-case, or client evidence includes claim IDs or a `Reliability Handoff`:

- read the handoff before converting evidence into requirements;
- preserve stable claim IDs for restated claims;
- preserve `FACT | INFERENCE | ASSUMPTION | ESTIMATE | UNKNOWN | STALE | TARGET | PROPOSAL`;
- preserve source, scope, freshness, contradictions, confidentiality, and downstream restrictions;
- never convert a prospect statement, feature request, proposed use case, possible integration, or target into a validated requirement without new evidence/decision authority;
- create a new claim ID with parent claim IDs for product conclusions derived from upstream evidence;
- inherited unresolved P0 blockers remain visible in PRD readiness;
- a downstream PRD cannot silently broaden account-specific evidence into a market-wide or universal product requirement;
- a newer PRD date does not refresh stale upstream evidence.

A requirement may trace to an upstream claim while still being a **product decision** rather than a fact. Preserve that distinction.

## Instructions

1. **Gather Information**: If the user provides files, read them carefully. If they mention research, URLs, customer data, discovery synthesis, or existing systems, gather relevant context before writing. If a lineage handoff exists, ingest it first.

2. **Decision-first framing**: Before solution detail, state:
   - What decision are we making?
   - What user/business problem is supported by evidence?
   - Why now?
   - What alternatives exist, including doing nothing?
   - What assumptions remain unproven?
   - Which upstream claim IDs are load-bearing?

3. **Apply the PRD Template**:

### 1. Executive Summary
What, for whom, why now, intended outcome, current confidence, and inherited evidence coverage.

### 2. Contacts / Ownership
Decision owner, product owner, design, engineering, data/AI, delivery/QA, GTM/support, and approvers as applicable. Unknown ownership remains `UNKNOWN`.

### 3. Background & Evidence
- observed problem and evidence
- current workflow/alternative
- frequency/severity
- prior attempts
- relevant research/market/context
- inherited claim IDs
- evidence gaps / contradictions

Label load-bearing claims `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`, `TARGET`, or `PROPOSAL`.

Use an evidence table when material:

| Claim ID | Claim | State | Scope | Source | Freshness | PRD Use | Restriction |

### 4. Objective & Success Contract
- customer outcome
- business outcome
- product/operational metrics
- baseline if known
- target/range
- guardrails
- measurement method and owner

Do not invent baselines or targets. An upstream `TARGET` remains a target. If unknown, define how the baseline/threshold will be established.

### 5. Target Users / Segments / JTBD
- primary user/buyer
- job/context
- eligibility and exclusions
- user versus buyer differences
- accessibility/localization or enterprise constraints where relevant

Do not broaden evidence from one prospect/account/segment without a new derived claim and explicit caveat.

### 6. Scope and Requirements
Separate:
- `P0 Must Have`
- `P1 Should Have`
- `P2 Later/Optional`
- `Non-goals`

For every P0 requirement include:
- requirement ID
- source claim ID(s) or hard constraint
- product decision/rationale
- acceptance criteria
- failure/edge cases
- unresolved dependency

A requirement with no evidence/constraint trace must be labelled `PRODUCT ASSUMPTION / DECISION`, not presented as customer fact.

### 7. Solution & Decision Log
- proposed experience/workflow
- key product decisions and rationale
- alternatives rejected and why
- dependencies/integrations/data
- permissions/privacy/security
- AI behavior/evaluation/HITL when applicable
- analytics/instrumentation
- operational/support requirements

For decisions derived from upstream evidence, record parent claim IDs.

### 8. Release / Validation Plan
- smallest releasable/testable version
- rollout cohort
- pre-launch gates
- experiment/evaluation plan
- rollback or disable path
- unresolved questions
- revisit triggers
- inherited P0 blockers that prevent readiness

## Reliability and Scope Gate

Before finalizing:

- Do not convert a solution request into a validated problem.
- Do not convert discovery enthusiasm into demand/WTP proof.
- Do not convert `PROPOSAL` into committed scope without authorized decision evidence.
- Do not convert `TARGET` into baseline/achieved outcome.
- Do not convert `UNKNOWN` integration/system behavior into architecture fact.
- If evidence for the problem is weak, label the PRD `DISCOVERY / HYPOTHESIS`, not implementation-ready.
- Every P0 item must trace to a user/business outcome, evidence claim, hard constraint, or risk. Remove or explicitly label orphan requirements.
- Include unhappy paths, permissions, empty states, recovery, interruption, data failure, integration failure, and abuse/misuse scenarios when relevant.
- Separate desired behavior from implementation suggestion unless the technology choice is itself a product constraint.
- State what is deliberately not built and why.
- For AI features, define dataset/evaluation, hard gates, confidence/uncertainty behavior, human review, cost/latency, safety/privacy, and rollback. Model accuracy alone is not acceptance.
- For enterprise products, include buyer/admin/user roles, implementation, security/procurement dependencies, auditability, and sales-to-delivery assumptions when relevant.
- Avoid date certainty when dependencies/evidence do not support it.

## Final Decision Block

```text
Status: DISCOVERY | READY FOR DESIGN | READY FOR BUILD | BLOCKED
Decision:
Strongest evidence (claim IDs):
Top assumptions (claim IDs):
Inherited P0 hard gates:
Key trade-offs:
What would change scope/decision:
Owner:
```

## Reliability Handoff

For P0 downstream execution, emit:

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Claims
| Claim ID | Claim | State | Scope | Evidence | Freshness | Downstream Restrictions |

### Derived Product Claims / Decisions
| Claim ID | Parent IDs | Derivation / Decision | State | Caveats |

### Requirement Traceability
| Requirement ID | Source Claim IDs | Decision Status | Acceptance Evidence Needed |

### Unresolved P0
[Claim IDs + blocker + evidence/decision needed]

### Prohibited Interpretations
[what engineering/delivery/GTM must not infer]
```

Use accessible language. Save substantial output as `PRD-[product-name].md`.

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
