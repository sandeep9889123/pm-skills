---
description: Red-team an existing business case, attempt to reject it, expose unsupported claims, and define the evidence required to reverse rejection
argument-hint: "<business case, initiative, or attached document>"
---

# /business-case-red-team

Attempt to reject `$ARGUMENTS` before leadership, customers, or competitors do.

## Required local skills

Apply:

1. **evidence-ledger** skill
2. **investment-red-team** skill
3. **opportunity-market-proof** skill
4. **customer-jtbd-proof** skill
5. **economics-commercial-proof** skill

Do not optimize for balance or reassurance. Optimize for finding decision-changing weaknesses.

## Workflow

### 1. Reconstruct the thesis

State the proposed customer, problem, investment, value mechanism, and expected outcome.

List the P0 assumptions connecting them.

### 2. Audit evidence integrity

For every major claim identify:

- evidence state
- source
- verification status
- freshness
- contradiction status
- whether the wording is broader than the evidence

Fabricated, inaccessible, stale, or weak citations are blocking defects.

### 3. Attack from seven perspectives

Run CEO, CTO, CFO, Sales/GTM, Delivery/Operations, Customer, and Competitor attacks.

### 4. Re-run alternatives

Re-evaluate BUILD, BUY, PARTNER, DO NOTHING, plus incumbent and open-source alternatives where relevant.

Do not preserve the original recommendation if another option now wins.

### 5. Challenge market and competition coverage

If the business case says competition is weak or absent, verify that search exhaustion covered category, problem, workflow, buyer, technology, substitutes, internal build, incumbents, regional, niche, emerging, and adjacent options.

If not, mark competition coverage incomplete.

### 6. Challenge customer proof

Check whether user, buyer, and economic buyer are distinct where relevant.

Reject invented personas, unverifiable quotes, assumed pain severity, and WTP inferred from market size.

### 7. Challenge economics

Reconstruct major estimates.

If ROI, payback, pricing, adoption, margin, or revenue cannot be rebuilt from explicit inputs, downgrade the claim.

### 8. Challenge PoC and platform logic

Reject a demo presented as validation.

Reject a technical PoC presented as commercial proof.

Reject platform or accelerator investment when reuse has not been evidenced across multiple credible use cases or clients.

### 9. Create strongest rejection case

Output:

- top 3 reasons to reject now
- claim IDs supporting rejection
- what evidence would reverse each reason
- kill criteria
- whether the problem is thesis quality, evidence quality, economics, timing, or execution

### 10. Final red-team verdict

Allowed outcomes:

- SURVIVES RED TEAM
- SURVIVES WITH CONDITIONS
- EXPERIMENT FIRST
- DEFER
- KILL
- NOT READY

`SURVIVES RED TEAM` does not replace the formal BUILD/BUY/PARTNER decision gate.

## Output artifact

When file writes are available create `business-case-red-team.md` containing:

1. Thesis reconstruction
2. Evidence defects
3. CEO attack
4. CTO attack
5. CFO attack
6. Sales/GTM attack
7. Delivery attack
8. Customer attack
9. Competitor attack
10. Alternatives re-score
11. PoC challenge
12. Platform/reuse challenge
13. Strongest rejection case
14. Kill criteria
15. Evidence required to reverse rejection
16. Verdict

Do not invent risks just to populate sections. Every criticism must be evidence-backed or explicitly labeled as inference, assumption, or unknown.
