---
name: evidence-ledger
description: "Create and audit a claim-level evidence ledger for a business case. Use when researching, validating, refreshing, or reviewing facts, assumptions, estimates, citations, contradictions, source freshness, and decision readiness."
---
# Evidence Ledger

## Objective

Make it impossible for unsupported business-case claims to disappear into polished prose.

Use `pm-business-case/references/EVIDENCE_CONTRACT.md` as the governing contract.

The ledger is created before the executive narrative and maintained throughout the workflow.

## Evidence states

Every material claim must be exactly one of:

- FACT
- INFERENCE
- ASSUMPTION
- ESTIMATE
- UNKNOWN
- STALE
- PROPOSAL
- DECISION_THRESHOLD

Do not create hybrid labels such as "likely fact". Pick the correct state and explain uncertainty in notes.

## Source handling rules

1. Retrieve and inspect external evidence before marking it VERIFIED.
2. Never cite a search snippet as if the underlying page was verified.
3. Never fabricate a URL, title, author, date, quote, page number, company, competitor, customer, price, market size, or benchmark.
4. If retrieval fails, mark `verification_status=UNVERIFIED` and state `coverage incomplete / UNKNOWN` where relevant.
5. Model memory can generate search hypotheses, never decision-critical FACT evidence.
6. Company-authored material verifies what the company claims, not necessarily whether the claim is objectively true.
7. Two sources copying the same announcement are one independence group, not two independent confirmations.

## User-provided information

Classify user input deliberately:

- `USER_PROVIDED_PRIMARY`: source-of-truth artifact or explicitly authoritative internal fact owned by the user.
- `USER_PROVIDED_CLAIM`: asserted information without source-of-truth evidence.
- `USER_PROVIDED_LEAD`: item to investigate, such as a suggested competitor.

User confidence does not change evidence state.

User-supplied competitors are leads, not facts. If the user says "I found a competitor" after a zero-result first pass, independently verify the named company and expand the search taxonomy. Do not merely add the company to the matrix.

## Required claim record

For every decision-critical claim capture:

```json
{
  "claim_id": "C001",
  "claim_text": "Example claim",
  "state": "FACT",
  "priority": "P0",
  "decision_critical": true,
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
  "notes": ""
}
```

Use `pm-business-case/references/EVIDENCE_LEDGER_TEMPLATE.json` as the starting structure.

## Decision criticality

Use:

- P0: could change BUILD, BUY, PARTNER, EXPERIMENT, DEFER, KILL, or NOT READY.
- P1: materially changes scope, sequencing, economics, or GTM.
- P2: useful context but not decision-determinative.

Do not bury P0 unknowns among low-value research details.

## Corroboration gate

A decision-critical FACT requires either:

- one primary authoritative source that directly establishes the claim, or
- two independent credible sources.

Exceptions are not granted because a claim is conventional wisdom.

For high-consequence claims, prefer independent corroboration even when a primary source exists if the primary source has a strong incentive to persuade.

## Contradiction pass

For each P0 claim, actively search for evidence that would make the claim false, narrower, older, geographically limited, or methodologically incompatible.

Record one of:

- NONE_FOUND
- RESOLVED
- UNRESOLVED
- NOT_CHECKED

A P0 FACT cannot be treated as investment-ready with UNRESOLVED or NOT_CHECKED contradiction status.

## Freshness

Do not use one universal freshness window.

Assess freshness based on the claim:

- pricing, product capabilities, competitors, regulations, funding, executive roles, and market activity can become stale quickly;
- audited historical financials may remain valid for the period they describe;
- structural research may remain useful longer, but its applicability must still be checked.

When current verification matters and cannot be completed, use STALE or UNKNOWN.

## Estimate discipline

Every ESTIMATE requires:

- formula or method
- inputs
- units
- source claim IDs for sourced inputs
- explicit assumptions
- sensitivity or range when material

Never hide an assumption inside a spreadsheet-style number.

Examples requiring ESTIMATE unless directly measured:

- TAM, SAM, SOM
- implementation savings
- engineering productivity
- revenue potential
- conversion lift
- adoption rate
- gross margin
- payback
- ROI
- time saved

## Market-size reconciliation

When external market estimates disagree:

1. compare category definition;
2. compare geography;
3. compare base year;
4. compare forecast horizon;
5. compare methodology;
6. compare included segments;
7. identify whether one source cites the other;
8. build a bottom-up estimate where possible.

Do not average conflicting numbers merely to produce a neat midpoint.

## Evidence coverage report

Before narrative generation, output:

| Area | P0 claims | Verified | Unknown/Stale | Contradicted | Readiness |
|---|---:|---:|---:|---:|---|
| Why now | | | | | |
| Customer/JTBD | | | | | |
| Competition | | | | | |
| Market size | | | | | |
| Right-to-win | | | | | |
| Technical feasibility | | | | | |
| Economics | | | | | |
| WTP/Pricing | | | | | |
| GTM | | | | | |
| Reuse/Platform | | | | | |

If any decision area is under-covered, state it before drafting recommendations.

## Validation

When execution is available, run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

Treat validator failure as a blocking defect. Fix evidence state, provenance, or the decision. Do not weaken the validator to make a case pass.
