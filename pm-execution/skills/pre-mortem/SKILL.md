---
name: pre-mortem
description: "Run an evidence-aware pre-mortem that identifies plausible failure modes, distinguishes risks from speculation, and defines mitigations, leading indicators, owners, and launch/investment kill gates. Use before launches, investments, GTM motions, or transformation programs."
---

# Pre-Mortem: Evidence-Aware Failure Analysis

## Purpose

Assume the initiative failed and identify the few failure modes that deserve action now. The output should improve a decision, not create a long anxiety list.

## Method

1. **Understand the initiative and success contract**
   Read the PRD/strategy/launch/business case. Capture intended outcome, users/buyers, scope, dependencies, metrics, timeline, and load-bearing assumptions.

2. **Generate failure modes across perspectives**
   Consider customer/value, usability/adoption, feasibility, AI/data quality, security/privacy, operations, delivery, GTM/sales, commercial/economics, legal/compliance, stakeholder/change, and dependencies.

3. **Write risks falsifiably**
   Use: `Fails if [specific condition]`, not generic labels like “execution risk.”

4. **Classify evidence**
   - `TIGER`: credible evidence/logical mechanism suggests material risk
   - `ELEPHANT`: important uncertainty with insufficient evidence
   - `PAPER TIGER`: concern investigated and reasonably refuted

   Do not call something a Paper Tiger merely because the team dislikes the implication.

5. **Rank by decision value**
   Evaluate impact, likelihood/confidence, detectability, time-to-harm, reversibility, and cheapness of testing/mitigation.

6. **Define action contract**
   For top risks provide:
   - leading indicator
   - evidence to obtain
   - mitigation/test
   - owner
   - due/revisit trigger
   - kill/block criterion
   - contingency/rollback

## Reliability Gate

- Do not manufacture risks to appear thorough.
- Separate known defect/dependency from probabilistic risk.
- Check correlated risks and shared root causes instead of double-counting them.
- Include risks created by the mitigation itself.
- High average success cannot override a catastrophic hard-gate risk.
- For AI: include silent errors, evaluation gaps, drift, cost/latency, prompt/input injection, tool misuse, HITL failure, privacy, and rollback where relevant.
- For enterprise GTM: include pilot-to-production, security/procurement, implementation readiness, sales promise drift, and adoption.
- For transformation/automation: include change adoption, measurement gaming, brittle integrations, and review burden.

## Output

### Top 5 decision-critical risks
| Failure condition | Evidence | Impact | Detectability | Leading signal | Test/mitigation | Kill/block gate | Owner |
|---|---|---|---|---|---|---|---|

### What holds up
Explicitly state important concerns that were investigated and reasonably refuted.

### Unknowns
What could not be assessed from available evidence.

### Decision
`PROCEED | PROCEED WITH GATES | HOLD | BLOCK` and the exact conditions for moving forward.

---

### Further Reading

- [How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
- [How to Manage Risks as a Product Manager](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)
