---
description: Build or refresh the evidence pack for a business case without forcing a recommendation or polished narrative
argument-hint: "<initiative or business case> [sources/files/context]"
---

# /business-case-evidence

Build the evidence foundation for `$ARGUMENTS`.

Use this command when the topic is under-researched, current evidence may be stale, or leadership needs proof before a business case narrative.

## Required local skills

Apply:

1. **evidence-ledger** skill
2. **opportunity-market-proof** skill
3. **customer-jtbd-proof** skill
4. **economics-commercial-proof** skill

Do not generate a final investment recommendation unless the evidence itself supports one and the user explicitly asks for it.

## Workflow

### 1. Define the evidence questions

Convert the decision into P0 questions:

- Is the problem real and important?
- Why now?
- Who is the user, buyer, and economic buyer?
- What is the JTBD and current workflow?
- What alternatives exist?
- What competitors or substitutes could invalidate the thesis?
- What is the reachable market?
- What right-to-win exists?
- What economics are known versus modeled?
- What commercial evidence exists?
- What would make the initiative fail?

### 2. Create `evidence-ledger.json`

Classify every material claim using the evidence contract.

External factual claims must be retrieved and inspected before VERIFIED status.

User-supplied names, competitors, demand claims, and numbers are leads or user-provided claims unless supported by authoritative evidence.

### 3. Search broadly before absence claims

If a first pass is sparse or zero-result, expand across category, problem, JTBD, workflow, buyer, technology, substitutes, manual processes, internal build, incumbent suites, open source, regional, niche, emerging, and adjacent framings.

Run a contradiction pass before any negative conclusion.

Tool or search failure means `coverage incomplete / UNKNOWN`.

### 4. Reconcile evidence

When sources disagree, compare scope, date, geography, definitions, methodology, and source lineage.

Do not average incompatible estimates.

### 5. Quantitative proof

For every material ESTIMATE include:

- method/formula
- input values and units
- source claim IDs where available
- assumptions
- sensitivity or range

### 6. Customer proof

Do not fabricate personas, quotes, pain scores, urgency, budgets, or WTP.

Where direct evidence is missing, create a validation backlog instead.

### 7. Produce coverage report

Summarize readiness by area:

- why now
- customer/JTBD
- competition
- market size
- right-to-win
- technical feasibility
- economics
- WTP/pricing
- GTM
- reuse/platform

Each area must be PASS, PARTIAL, FAIL, or UNKNOWN with supporting claim IDs.

### 8. Validate

When execution is available:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

Do not change a claim state merely to satisfy the validator.

## Outputs

When file writes are available create:

- `evidence-ledger.json`
- `evidence-gap-register.md`
- `source-map.md`

The gap register should rank missing evidence by decision impact, not by ease of research.

## Final response

Return:

- overall evidence readiness
- P0 verified claims
- P0 unknown/stale/contradicted claims
- largest coverage risk
- next 3 highest-value evidence actions
- artifact paths when created

If coverage is weak, say so directly. Do not compensate with longer prose.
