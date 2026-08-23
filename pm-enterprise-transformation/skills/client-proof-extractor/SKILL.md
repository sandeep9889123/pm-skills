---
name: client-proof-extractor
description: "Extract reusable, NDA-safe sales proof from completed client work while verifying outcomes, attribution, scope, and confidentiality. Use when turning delivery documents, retrospectives, metrics, demos, or client feedback into defensible success-story evidence."
---

# Client Proof Extractor

## Purpose

Convert delivery history into verified proof without turning correlation, targets, team outcomes, or confidential details into marketing claims.

## Input sources

Use available project artifacts such as contracts/scope, PRDs, acceptance reports, dashboards, before/after metrics, client emails, QBRs, release notes, retrospectives, architecture docs, and stakeholder feedback.

Treat all inputs as evidence to evaluate, not permission to publish.

## Claim taxonomy

Every proposed proof point must be classified:

- `MEASURED`: directly supported by before/after or accepted operational data
- `CLIENT-CONFIRMED`: client explicitly validated outcome/statement
- `DELIVERED`: capability/functionality demonstrably shipped
- `OBSERVED`: pattern seen but causal attribution is limited
- `TARGET`: intended outcome, not achieved result
- `INFERENCE`: plausible interpretation
- `UNKNOWN`: insufficient evidence

Never rewrite `TARGET`, `INFERENCE`, or `UNKNOWN` as achieved impact.

## Method

1. **Reconstruct the problem**: buyer/user, prior workflow, cost/risk, constraints.
2. **Reconstruct the intervention**: what was actually delivered, by whom, and what was outside scope.
3. **Build evidence ledger**:
   | Claim | Evidence source | Period | Attribution strength | Confidentiality | Status |
4. **Separate contribution from ownership**: distinguish team/company outcome from personal or product-specific contribution.
5. **Check causality**: identify concurrent changes that could explain the result.
6. **Check denominators and baselines**: reject percentage improvements with missing baseline/sample/period.
7. **Sanitize**: remove client name, proprietary rules, sensitive architecture/data, contract values, or unique identifiers unless publication is explicitly cleared.
8. **Identify reusable pattern**: what problem/solution mechanism generalizes across prospects?

## Contradiction pass

Ask:
- could the metric have improved without our intervention?
- is this a pilot result being presented as production impact?
- is a team result being attributed to one component?
- did the customer merely accept delivery rather than confirm business value?
- is the strongest claim publishable?

## Output

### Proof ledger
| Proof point | Classification | Evidence | Confidence | Publishability | Sales use |
|---|---|---|---|---|---|

### Safe success-story core
- customer archetype
- problem
- constraints
- intervention
- verified outcome
- why it mattered
- reusable mechanism

### Evidence gaps
List what must be confirmed before stronger claims are used.

### Decision
`PUBLIC-SAFE | INTERNAL-SALES-ONLY | NEEDS CLIENT CLEARANCE | NEEDS EVIDENCE | DO NOT USE`
