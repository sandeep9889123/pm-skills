---
name: evidence-ledger
description: "Create and audit a claim-level evidence ledger for a business case. Use when validating facts, assumptions, estimates, citations, contradictions, source freshness, confidence, and investment readiness before writing executive recommendations."
---

# Evidence Ledger

## Operating principle

Make it impossible for unsupported claims to disappear into polished prose.

The ledger must exist before the executive narrative. It is the source of truth for business-case claims, not an appendix produced after the story is written.

Use `pm-business-case/references/EVIDENCE_CONTRACT.md` as the governing contract when available.

## Non-negotiable rules

1. Every material claim must have a claim ID.
2. Every material claim must have exactly one evidence state.
3. Never fabricate sources, URLs, quotes, page numbers, companies, competitors, customers, prices, market sizes, benchmarks, dates, or metrics.
4. Never cite a search snippet as if the underlying source was verified.
5. Model memory can propose search leads, not decision-critical evidence.
6. User-provided claims must be classified, not automatically trusted.
7. Tool or retrieval failure means `UNVERIFIED` and `coverage incomplete`, not absence.
8. P0 claims with `UNKNOWN`, `STALE`, `UNVERIFIED`, `CONTRADICTED`, or `NOT_CHECKED` cannot support a confident investment recommendation.
9. A business case with hidden P0 uncertainty must be downgraded to NOT READY or EXPERIMENT.

## Evidence states

Use exactly one:

| State | Meaning |
|---|---|
| FACT | Directly supported by adequate evidence |
| INFERENCE | Reasoned interpretation from verified facts |
| ASSUMPTION | Required working belief not yet verified |
| ESTIMATE | Modelled or approximate value with method and inputs |
| UNKNOWN | Material fact not verified |
| STALE | Evidence may no longer be current |
| PROPOSAL | Future action or intended capability |
| DECISION_THRESHOLD | Explicit pass/fail threshold for a decision gate |

Do not create hybrid labels such as `likely fact` or `soft proof`.

## User-provided information classification

Classify user inputs as:

| Type | Use |
|---|---|
| USER_PROVIDED_PRIMARY | Source-of-truth artifact or explicitly authoritative internal fact |
| USER_PROVIDED_CLAIM | Assertion without source-of-truth evidence |
| USER_PROVIDED_LEAD | Item to investigate, such as suggested competitor, market, customer, or metric |
| USER_PROVIDED_CONTEXT | Useful background, not proof by itself |

User confidence does not change evidence state.

A user-supplied competitor is a lead. Verify independently and expand the search taxonomy if it exposes a missed category.

## Required claim record

For every decision-critical claim capture:

```json
{
  "claim_id": "C001",
  "claim_text": "Exact claim being used",
  "state": "FACT",
  "priority": "P0",
  "decision_critical": true,
  "decision_area": "Competition",
  "sources": [
    {
      "source_type": "PRIMARY_AUTHORITATIVE",
      "title": "Source title",
      "reference": "URL, file path, or source identifier",
      "source_date": "YYYY-MM-DD or unknown",
      "accessed_date": "YYYY-MM-DD or not applicable",
      "support": "Short supporting excerpt or precise location marker",
      "independence_group": "origin identifier"
    }
  ],
  "basis_claim_ids": [],
  "formula": "",
  "inputs": [],
  "verification_status": "VERIFIED",
  "freshness_status": "CURRENT",
  "contradiction_status": "NONE_FOUND",
  "confidence": "HIGH",
  "notes": ""
}
```

Use `pm-business-case/references/EVIDENCE_LEDGER_TEMPLATE.json` when available.

## Decision criticality

Use:

- P0: could change BUILD, BUY, PARTNER, EXPERIMENT, DEFER, KILL, or NOT READY
- P1: materially changes scope, sequencing, economics, GTM, or risk
- P2: useful context, not decision-determinative

Do not bury P0 unknowns among low-value research details.

## Source standards

Preferred support:

1. primary authoritative source that directly establishes the claim
2. internal source-of-truth artifact explicitly provided by the user
3. two independent credible sources
4. transparent estimate with sourced inputs
5. clearly labeled inference from verified facts

Company-authored material verifies what the company claims. It does not prove objective superiority, customer satisfaction, market leadership, or independent demand.

Two sources copying the same announcement are one independence group.

## Corroboration gate

A decision-critical FACT requires either:

- one primary authoritative source that directly establishes the claim, or
- two independent credible sources.

For high-consequence claims, prefer independent corroboration even when a primary source exists, especially if the source has incentive to persuade.

## Contradiction pass

For each P0 claim, actively search for evidence that would make it false, narrower, older, geographically limited, overstated, or methodologically incompatible.

Record:

- NONE_FOUND
- RESOLVED
- UNRESOLVED
- NOT_CHECKED

A P0 FACT is not investment-ready with UNRESOLVED or NOT_CHECKED contradiction status.

## Freshness discipline

Assess freshness by claim type:

- pricing, competitors, product capabilities, funding, regulations, executive roles, and market activity can stale quickly
- audited historical numbers may remain valid for their stated period
- structural research may remain useful longer, but applicability still needs checking
- internal delivery metrics need period, denominator, scope, and owner

When current verification matters and cannot be completed, use STALE or UNKNOWN.

## Estimate discipline

Every ESTIMATE requires:

- formula or method
- units
- inputs
- source claim IDs for sourced inputs
- explicit assumptions
- sensitivity or range when material

Never hide an assumption inside a single number.

Common estimates requiring method:

- TAM, SAM, SOM
- reachable accounts
- revenue potential
- implementation savings
- engineering productivity
- conversion lift
- adoption rate
- pricing/WTP
- gross margin
- payback
- ROI
- time saved

## Market-size reconciliation

When external market estimates disagree:

1. compare category definition
2. compare geography
3. compare base year
4. compare forecast horizon
5. compare included segments
6. compare methodology
7. compare source lineage
8. identify commercial incentives
9. build a bottom-up estimate when possible

Do not average incompatible numbers merely to produce a neat midpoint.

## Evidence coverage report

Before narrative generation, output:

| Area | P0 claims | Verified | Unknown/Stale | Contradicted | Readiness |
|---|---:|---:|---:|---:|---|
| Decision frame | | | | | |
| Why now | | | | | |
| Customer/JTBD | | | | | |
| Competition | | | | | |
| Market size | | | | | |
| Alternatives | | | | | |
| Right-to-win | | | | | |
| Technical feasibility | | | | | |
| Economics | | | | | |
| WTP/Pricing | | | | | |
| GTM | | | | | |
| Reuse/Platform | | | | | |
| Risk/Kill criteria | | | | | |

If any P0 decision area is under-covered, state it before drafting recommendations.

## Validation

When execution is available, run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

Treat validator failure as a blocking defect. Fix evidence state, provenance, or the decision. Do not weaken the validator to make a case pass.

## Required output

### 1. Evidence ledger summary

- number of P0/P1/P2 claims
- verified P0 count
- unknown/stale/unverified P0 count
- contradiction status
- readiness decision

### 2. Claim ledger

Use the required claim record format.

### 3. Blocking uncertainty

List P0 claims that block BUILD, BUY, PARTNER, or confident recommendation.

### 4. Contradictions

List resolved and unresolved contradictions.

### 5. Evidence plan

For each blocker:

- evidence needed
- source to retrieve
- owner if known
- cheapest verification action
- decision threshold

## Hard stop conditions

Return `NOT READY` when:

- P0 claims lack provenance
- source freshness is unknown and material
- contradictions are unresolved
- estimates lack method or inputs
- market size cannot be reconstructed
- competitor absence is inferred from weak search
- customer demand is asserted but not evidenced
- right-to-win is aspirational

## Final self-check

Before delivery, verify:

- every material claim has a state
- every P0 claim has readiness status
- no invented sources or numbers exist
- estimates are reconstructable
- contradictions were checked
- uncertainty is visible in the executive layer
