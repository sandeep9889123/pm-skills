# PM Enterprise Transformation

Enterprise transformation workflows for building future capabilities, converting client proof into GTM, improving sales execution, selecting tools, governing automation, and testing reusable accelerator theses.

## When to use

Use this plugin when you need to build a future capability thesis, turn client success into sales/GTM assets, diagnose funnel gaps, create account expansion plays, evaluate tooling/automation, test reusable IP, or prepare leadership-facing transformation decisions.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-enterprise-transformation@pm-skills
```

```text
/pm-enterprise-transformation:build-future-capability [opportunity]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-enterprise-transformation@pm-skills
```

```text
Use pm-enterprise-transformation to evaluate this future capability. Separate verified demand/proof from aspiration, test reuse economics and right-to-win, define the GTM path, and recommend the next evidence-generating commitment.
```

### ChatGPT

Upload a specific skill such as `skills/capability-opportunity-radar/`, `skills/client-proof-extractor/`, or `skills/tool-evaluation-selection/` when Skills is available.

With the GitHub app:

```text
Read pm-enterprise-transformation/skills/capability-opportunity-radar/SKILL.md from sandeep9889123/pm-skills and follow it for this capability proposal.
```

### Other LLMs

Copy or attach the required skill folders. For multi-stage transformations, provide the relevant workflow file or describe the sequence and decision gate explicitly.

## Skills (12)

- `account-expansion-play`
- `automation-governance`
- `capability-opportunity-radar`
- `case-study-to-gtm`
- `client-proof-extractor`
- `pipeline-conversion-experiment`
- `pm-workflow-automation`
- `reusable-accelerator-thesis`
- `sales-funnel-diagnostic`
- `solution-business-case`
- `solution-to-sales-playbook`
- `tool-evaluation-selection`

## Commands (4)

- `/pm-enterprise-transformation:automate-pm-workflow`
- `/pm-enterprise-transformation:build-future-capability`
- `/pm-enterprise-transformation:proof-to-gtm`
- `/pm-enterprise-transformation:transform-sales`

## Example prompts

```text
Use reusable-accelerator-thesis to test whether this client solution is genuinely reusable. Require common-core evidence, marginal delivery reduction, repeatable value, ownership, and a build/buy/partner alternative.
```

```text
Use client-proof-extractor on these delivery artifacts. Separate publishable verified outcomes from confidential, target, inferred, or unsupported claims before creating GTM content.
```

## Operating rules

1. Separate proof from aspiration.
2. Do not convert one delivery success into reusable IP without evidence.
3. Link capability bets to demand, sales motion, delivery feasibility, and commercial value.
4. Identify missing proof before investment.
5. Treat automation as a governance problem, not just tooling.
6. Make outputs useful for CEO, Sales, Delivery, Product, and Engineering.

## Output standard

A strong output includes capability thesis, evidence ledger, buyer/user jobs, proof inventory, GTM path, reuse logic, operating model, risks, disconfirming evidence, and decision gates.

## Attribution

This plugin is an added enterprise transformation layer in Sandeep Kumar M's fork, built on the broader `phuryn/pm-skills` foundation.
