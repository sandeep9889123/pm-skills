# pm-enterprise-transformation

## Overview

An enterprise PM operating system for four recurring leadership motions:

1. **Building Future Capabilities** — identify reusable solution opportunities, validate the right-to-win, build an investment case, and define a pilot-to-platform path.
2. **Client Proof → Sales GTM** — turn delivered client outcomes into evidence-safe case studies, sales narratives, expansion plays, and repeatable solution offers.
3. **Sales Transformation** — diagnose funnel leakage, improve solution-selling motions, and run measurable conversion experiments.
4. **Tooling & Automation** — identify PM/solution workflows worth automating, select tools using evidence, and govern automations safely.

The plugin is decision-first. It should not manufacture success metrics, case-study claims, market demand, or ROI. Unknown evidence remains `UNKNOWN` until verified.

## Install

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-enterprise-transformation@pm-skills
```

For Codex, install the plugin and invoke the skill/workflow in natural language if slash commands are unavailable.

## Skills (12)

### Building Future Capabilities
- `capability-opportunity-radar` — identify and rank reusable capability opportunities from client demand, delivery evidence, market signals, and strategic fit.
- `reusable-accelerator-thesis` — decide whether a recurring solution pattern should remain project-specific, become an accelerator, or become a platform capability.
- `solution-business-case` — produce an evidence-backed investment case with economics, scenarios, risks, pilot gates, and kill criteria.

### Client Proof → Sales GTM
- `client-proof-extractor` — extract reusable, NDA-safe proof from delivery artifacts without inventing outcomes or overstating ownership.
- `case-study-to-gtm` — convert verified proof into ICP, problem narrative, sales story, discovery questions, objections, and campaign assets.
- `account-expansion-play` — identify evidence-backed cross-sell/upsell/adjacent-use-case opportunities inside an existing account.

### Sales Transformation
- `sales-funnel-diagnostic` — identify the highest-value funnel constraint using stage conversion, cycle time, loss reasons, quality, and capacity evidence.
- `solution-to-sales-playbook` — convert a solution/capability into a repeatable consultative selling motion with qualification, discovery, proof, demo, and handoff.
- `pipeline-conversion-experiment` — design sales experiments with hypotheses, cohorts, guardrails, attribution limits, and stop/scale criteria.

### Tooling & Automation
- `pm-workflow-automation` — map a PM/solution workflow, identify automation candidates, design HITL controls, and estimate value versus failure cost.
- `tool-evaluation-selection` — compare tools using weighted requirements, workflow fit, integration/security constraints, TCO, switching cost, and evidence confidence.
- `automation-governance` — define permissions, review points, auditability, rollback, monitoring, ownership, and failure handling for automated workflows.

## Commands (4)

- `/build-future-capability` — evidence → opportunity → right-to-win → business case → pilot → scale/hold/kill decision.
- `/proof-to-gtm` — delivery proof → verified claims → reusable case study → ICP → sales narrative → GTM assets → measurement.
- `/transform-sales` — funnel evidence → constraint diagnosis → motion redesign → experiments → operating cadence.
- `/automate-pm-workflow` — workflow map → automation suitability → tool/design choice → controls → pilot → measured rollout.

## Reliability rules

Every workflow must:

- separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE`;
- verify user-provided claims rather than accepting them because they were supplied;
- search for disconfirming evidence before high-consequence recommendations;
- avoid forced rankings when evidence is insufficient;
- expose missing evidence and what would change the decision;
- distinguish measured client outcomes from marketing interpretation;
- protect confidential/client-identifying information unless explicitly cleared for public use;
- state decision criteria before recommending investment, GTM, sales-process change, or automation;
- include owner, next evidence action, and revisit trigger.

## Output standard

Substantial outputs should end with a compact decision block:

```text
Decision: GO | PILOT | HOLD | KILL | NEEDS EVIDENCE
Why: [3 strongest evidence points]
Critical unknowns: [what could reverse the decision]
Next test: [cheapest high-value validation]
Owner: [role]
Revisit when: [trigger/date/evidence]
```
