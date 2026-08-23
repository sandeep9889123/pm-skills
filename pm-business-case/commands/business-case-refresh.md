---
description: Refresh stale or decision-critical evidence in an existing business case, preserve provenance, record changes, and recalculate decision readiness
argument-hint: "<existing business case and evidence ledger> [as-of date/context]"
---

# /business-case-refresh

Refresh `$ARGUMENTS` without rewriting history or inventing updates.

Use this command before leadership review, after a material market change, when evidence becomes stale, or when a previous business case is being reused for a new decision date.

## Required local skills

Apply:

1. **evidence-ledger** skill
2. **opportunity-market-proof** skill
3. **customer-jtbd-proof** skill
4. **economics-commercial-proof** skill
5. **investment-red-team** skill

## Step 1: Load prior state

Identify:

- prior decision
- prior as-of date
- P0/P1 claim IDs
- stale claims
- unknown claims
- unresolved contradictions
- assumptions with expired validation windows

Do not silently delete prior evidence. Preserve provenance and supersede claims explicitly.

## Step 2: Prioritize refresh effort

Refresh in this order:

1. decision-critical stale claims
2. previously blocking unknowns
3. competitor and substitute changes
4. pricing and product capability changes
5. regulatory or market changes
6. customer and WTP evidence
7. cost and economics inputs
8. GTM and implementation evidence
9. reuse/platform evidence
10. low-impact context

Do not spend equal effort on every citation.

## Step 3: Re-verify current external facts

Retrieve and inspect current evidence where tools permit.

Do not assume an old URL still supports the same claim.

If retrieval fails, mark `coverage incomplete / UNKNOWN` or STALE as appropriate.

## Step 4: Re-run negative conclusion gates

Any prior conclusion such as weak competition, no direct competitor found, no viable substitute, no regulatory blocker, or no commercial evidence must be re-tested if the claim could have changed.

Search direct, adjacent, substitute, manual, internal-build, incumbent, open-source, regional, niche, emerging, and alternative terminology where relevant.

## Step 5: Recompute estimates

Recompute market size, ROI, payback, revenue, margin, and pricing estimates when any material input changed.

Do not copy the old result if its inputs are stale.

Preserve formulas and changed input claim IDs.

## Step 6: Record evidence delta

Create a change log with:

- claim ID
- prior state
- new state
- prior source
- new source
- what changed
- decision impact

Separate source refresh from actual thesis change.

## Step 7: Re-run red team

Attack the updated case using the strongest new evidence, not the prior recommendation.

If a new competitor, lower-cost alternative, changed regulation, weaker WTP, or higher operating cost invalidates the old decision, change the recommendation.

## Step 8: Validate

When execution is available run:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

Do not restore an old BUILD/BUY/PARTNER decision if the refreshed ledger fails.

## Outputs

When file writes are available create or update:

- `evidence-ledger.json`
- `business-case-refresh.md`
- `evidence-change-log.md`
- `decision-gates.md`

## Final response

Return:

- prior decision
- refreshed decision/readiness
- material new evidence
- claims that changed state
- newly stale or unresolved P0 claims
- whether the original thesis strengthened, weakened, or materially changed
- next evidence action

Do not claim "no material change" unless the decision-critical evidence set was actually refreshed.
