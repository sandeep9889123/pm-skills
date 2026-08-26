---
name: client-proof-extractor
description: "Extract reusable, NDA-safe sales proof from completed client work while verifying outcomes, attribution, scope, baselines, confidentiality, publishability, and claim lineage. Use when turning delivery evidence into case studies, GTM assets, or sales proof."
---

# Client Proof Extractor

## Operating Principle

Convert delivery history into verified proof without turning correlation, targets, acceptance, team effort, or confidential details into inflated marketing claims.

The goal is to create sales-usable evidence that can survive client, legal, delivery, and executive scrutiny **and preserve exactly what downstream GTM is allowed to claim**.

## Non-Negotiable Rules

1. Never rewrite a target as an achieved outcome.
2. Never imply client endorsement without explicit client confirmation.
3. Never attribute business impact to a solution if causality is weak or unproven.
4. Never publish client names, proprietary workflows, contract values, architecture details, data samples, rules, or identifiers without clearance.
5. Never use percentages without baseline, denominator, period, and sample.
6. Never turn team/company delivery into personal ownership without scope evidence.
7. Never present pilot results as production impact unless production evidence exists.
8. Never convert internal enthusiasm into buyer proof.
9. If evidence is insufficient, classify the claim as `NEEDS EVIDENCE` or `INTERNAL ONLY`.
10. Downstream case studies, GTM assets, and battlecards may not strengthen the claim merely by rewriting it.

## Claim-Lineage Producer Contract

Assign a stable `claim_id` to every material proof point.

For each claim preserve:
- claim text
- evidence state
- proof classification
- evidence/source refs
- baseline, denominator, period, and sample where applicable
- attribution strength
- account/segment/product/time scope
- contradictions/caveats
- publishability/confidentiality
- allowed downstream uses
- prohibited downstream uses

Map proof classifications to lineage state conservatively:
- `MEASURED`, `CLIENT_CONFIRMED`, `DELIVERED`, `ACCEPTED`, `OBSERVED` may support `FACT` only for the exact fact proven and scope observed;
- `TARGET` remains `TARGET`;
- `INFERENCE` remains `INFERENCE`;
- insufficient evidence remains `UNKNOWN`;
- sensitive evidence preserves restricted publishability even when factually strong.

Example: `ACCEPTED` can support the FACT "delivery was accepted". It does **not** support the FACT "business outcome was achieved."

## Input Sources

Use available artifacts such as contracts/scope documents, PRDs, delivery plans, acceptance reports, dashboards/logs, before/after metrics, client emails, QBRs, support tickets, release notes, retrospectives, architecture docs, QA reports, stakeholder feedback, sales notes, and case-study drafts.

Treat all inputs as evidence to evaluate, not permission to publish.

## Claim Taxonomy

| Classification | Meaning |
|---|---|
| MEASURED | Directly supported by before/after or accepted operational data |
| CLIENT_CONFIRMED | Client explicitly validated the outcome or statement |
| DELIVERED | Capability/functionality demonstrably shipped |
| ACCEPTED | Delivery accepted, business outcome not necessarily proven |
| OBSERVED | Pattern observed but causal attribution limited |
| TARGET | Intended outcome, not achieved result |
| INFERENCE | Plausible interpretation from evidence |
| UNKNOWN | Insufficient evidence |
| SENSITIVE | Cannot be used externally without sanitization/clearance |

Never rewrite `TARGET`, `INFERENCE`, `UNKNOWN`, or `ACCEPTED` as achieved impact.

## Method

### Step 1: Reconstruct Context

Capture:
- customer archetype
- industry/segment
- buyer/user
- prior workflow
- pain/cost/risk
- constraints
- scope boundary
- timeline
- stakeholders

### Step 2: Reconstruct Intervention

Capture:
- what was actually delivered
- by whom
- when
- systems/processes changed
- what was outside scope
- dependencies
- concurrent initiatives that may affect outcomes

### Step 3: Build Proof Ledger

| Claim ID | Proof point | Classification | Evidence source | Period | Baseline | Denominator | Attribution | Scope | Publishability | Status |

Attribution strength:
- `STRONG`: direct before/after with controlled or highly plausible causal link
- `MODERATE`: credible contribution but other factors exist
- `WEAK`: correlation or anecdote
- `UNKNOWN`: insufficient evidence

### Step 4: Validate Metrics

Reject or downgrade metrics when baseline, denominator, period, sample, metric owner, causal attribution, or production status does not support the intended wording.

A state upgrade requires explicit new evidence. A case-study rewrite is not new evidence.

### Step 5: Separate Ownership

Distinguish:
- company/team delivered
- product/capability enabled
- user personally contributed
- client achieved
- third-party system contributed

Do not over-attribute.

### Step 6: Check Publishability

Classify each proof point:
- `PUBLIC_SAFE`
- `ANONYMIZED_PUBLIC_SAFE`
- `INTERNAL_SALES_ONLY`
- `NEEDS_CLIENT_CLEARANCE`
- `NEEDS_LEGAL_REVIEW`
- `NEEDS_EVIDENCE`
- `DO_NOT_USE`

Preserve this restriction downstream. Sanitization does not automatically clear a claim for broader use.

### Step 7: Extract Reusable Sales Pattern

Identify:
- problem pattern
- buyer pain
- solution mechanism
- credible before/after evidence
- reusable capability
- relevant prospect segment
- objection it helps overcome
- evidence gap to close

Any generalized/transferability claim is **derived**, requires a new claim ID linked to client-proof parent IDs, and should normally be `INFERENCE` until tested outside the reference account.

## Contradiction Pass

Ask:
- could the metric have improved without our intervention?
- is this a target being presented as actual?
- is pilot evidence being presented as production?
- is acceptance being presented as business value?
- is a team result being attributed to one component?
- is the denominator missing?
- would the client agree with this wording?
- would legal approve external usage?
- can sales defend this claim live?
- has the claim's scope expanded beyond the reference account?

## Required Output

### 1. Proof Readiness Decision

`PUBLIC_SAFE | INTERNAL_SALES_ONLY | NEEDS_CLIENT_CLEARANCE | NEEDS_EVIDENCE | DO_NOT_USE`

### 2. Proof Ledger

| Claim ID | Proof point | State | Classification | Evidence | Attribution | Scope | Confidence | Publishability | Allowed Use |

### 3. Safe Success-Story Core

- customer archetype
- problem
- constraints
- intervention
- verified outcome
- why it mattered
- reusable mechanism
- prospect relevance

### 4. Claim-Safe Wording

- strongest externally safe claim
- stronger internal-only claim
- claims to avoid
- evidence needed for stronger claim

### 5. Evidence Gaps

List what must be confirmed before stronger claims are used.

### 6. Sales Asset Recommendation

Choose one:
- one-line proof point
- anonymized case study
- internal battlecard proof
- discovery-call story
- leadership slide
- do not use yet

### 7. Reliability Handoff

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED

### Material Proof Claims
| Claim ID | Claim | State | Scope | Evidence | Attribution | Publishability | Downstream Restrictions |

### Derived Transferability Claims
| Claim ID | Parent IDs | Derivation | State | Caveats |

### Unresolved P0
[Claim IDs + evidence/clearance needed]

### Prohibited Interpretations
[e.g. accepted != business impact; pilot != production; client proof != market demand]
```

## Hard Stop Conditions

Return `DO_NOT_USE` or `NEEDS_EVIDENCE` when baseline/denominator is missing for a numeric claim, causality is weak but wording implies causality, client endorsement is implied without confirmation, confidentiality risk is unresolved, acceptance is the only proof, outcome is a target, or personal contribution is over-claimed.

## Final Self-Check

- I did not inflate outcomes.
- I did not expose confidential details.
- I separated delivery, acceptance, outcome, and client confirmation.
- I preserved denominators and baselines.
- I preserved claim IDs, scope, attribution, and publishability.
- I provided safe wording and claims to avoid.
- I downgraded weak proof instead of dressing it up.
