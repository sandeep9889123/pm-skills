---
description: Diagnose and improve an enterprise sales motion using funnel evidence, qualification, solution selling, and measured conversion experiments
argument-hint: "<sales funnel, solution line, segment, CRM export, or transformation goal>"
---

# /transform-sales

Improve the sales system by finding and testing the constraint, not by adding activity everywhere.

## Workflow

### 1. Diagnose funnel
Apply **sales-funnel-diagnostic**:
- validate CRM/stage data quality
- analyze conversion and cycle time by meaningful cohort
- inspect loss reasons, buyer access, proof, commercial and implementation friction
- identify one primary constraint and at most two secondary constraints

If instrumentation is not trustworthy, recommend `INSTRUMENT FIRST`.

### 2. Audit the sellable motion
Apply **solution-to-sales-playbook** to verify:
- ICP/anti-ICP
- qualification exit criteria
- discovery quality
- proof ladder
- demo narrative
- objection handling
- scope/commercial boundaries
- sales-to-delivery handoff

### 3. Design experiments
Apply **pipeline-conversion-experiment** to each prioritized intervention:
- explicit hypothesis/mechanism
- target cohort
- baseline
- primary metric
- guardrails
- attribution risks
- scale/stop/rollback criteria

### 4. Operating cadence
Create a weekly transformation scorecard:
- primary constraint metric
- leading behavior metric
- guardrail
- experiment status
- learning
- owner
- next decision

Avoid turning the cadence into a dashboard of vanity activities.

### 5. Red-team
Check for:
- win-rate improvement caused by weaker opportunity creation or cherry-picking;
- stage conversion inflated by stage-definition changes;
- sales cycle reduced by smaller deals;
- discounting hidden behind conversion gains;
- successful pilot that cannot move to production;
- more collateral compensating for poor discovery;
- more leads compensating for low ICP quality;
- sales promises increasing delivery risk.

## Output

```text
Primary constraint:
Evidence/confidence:
Root cause:
Intervention:
Experiment:
Primary metric:
Guardrails:
Owner:
Scale/stop criteria:
```

### Decision
`RUN EXPERIMENT | REDESIGN MOTION | INSTRUMENT FIRST | FIX PRODUCT/DELIVERY PROOF | NO TRANSFORMATION REQUIRED`.
