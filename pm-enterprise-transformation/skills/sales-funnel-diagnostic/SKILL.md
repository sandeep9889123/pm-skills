---
name: sales-funnel-diagnostic
description: "Diagnose the highest-value enterprise sales funnel constraint using stage conversion, cycle time, loss reasons, opportunity quality, capacity, and cohort evidence. Use when sales performance is weak, leadership wants sales transformation, or teams disagree on where pipeline is leaking."
---

# Sales Funnel Diagnostic

## Purpose

Identify the load-bearing constraint in the sales system before prescribing more leads, more collateral, more demos, or new tooling.

## Data hierarchy

Prefer opportunity-level CRM data, stage timestamps, win/loss reasons, segment/cohort data, rep capacity, activity quality, deal size, source, product/solution mix, and qualitative call evidence.

Do not diagnose solely from aggregate pipeline value or anecdotal complaints.

## Method

1. **Define funnel semantics**
   Verify stage definitions, exit criteria, reopen rules, stale-opportunity handling, and whether CRM fields are actually used consistently.

2. **Check data quality first**
   Identify missing timestamps, duplicate opportunities, stage skipping, inconsistent loss reasons, sandbagging, inflated probability, and source attribution gaps.

3. **Analyze by cohort, not only total**
   Segment by source, ICP fit, solution, geography, deal size, rep/team, new vs expansion, and period.

4. **Diagnose constraints**
   Examine:
   - lead/account quality
   - discovery-to-qualified conversion
   - buyer/champion access
   - problem/urgency validation
   - demo/proof effectiveness
   - proposal value clarity
   - security/procurement/legal drag
   - implementation confidence
   - pricing/commercial friction
   - competitive losses
   - follow-up/cadence discipline
   - rep/solution-consulting capacity

5. **Quantify leakage**
   For each suspected constraint estimate impact using conversion delta, cycle-time cost, lost ARR/value, capacity consumed, or opportunity cost. Use ranges if data is incomplete.

6. **Contradiction pass**
   Ask what evidence would show the apparent bottleneck is downstream of another problem. Example: poor proposal conversion may actually originate in weak qualification.

7. **Prioritize one primary and at most two secondary constraints**
   Avoid a transformation plan with 20 equal priorities.

## Output

### Funnel health
| Stage/cohort | Conversion | Cycle time | Quality signal | Evidence issue | Diagnosis confidence |
|---|---|---|---|---|---|

### Constraint tree
Root cause → mechanism → observable evidence → business consequence.

### Recommended intervention
For each top constraint: smallest intervention, owner, leading metric, lagging metric, guardrail, expected learning window.

### Decision
`INTERVENE | INSTRUMENT FIRST | NEEDS DATA CLEANUP | NO MATERIAL CONSTRAINT FOUND`

Never claim causality from correlation without an experiment or converging evidence.
