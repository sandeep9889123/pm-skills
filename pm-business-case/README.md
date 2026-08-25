# PM Business Case

Evidence-first business-case workflows for evaluating investment bets, AI solution opportunities, migration agents, enterprise accelerators, and product capability proposals.

## When to use

Use this plugin when you need to build a leadership-ready business case, validate market/customer proof, model economics, create an evidence ledger, run an investment red-team, or decide whether to BUILD, BUY, PARTNER, EXPERIMENT, DEFER, KILL, or return NOT READY.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-business-case@pm-skills
```

```text
/pm-business-case:build-business-case [initiative]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-business-case@pm-skills
```

```text
Use pm-business-case to evaluate this initiative. Build the evidence ledger before the narrative, compare BUILD/BUY/PARTNER/DO NOTHING, require reconstructable economics, define a falsifiable PoC, and produce the strongest rejection case.
```

### ChatGPT

Upload a specific skill such as `skills/business-case-orchestrator/` or `skills/evidence-ledger/` if Skills is available.

With the GitHub app:

```text
Read pm-business-case/skills/business-case-orchestrator/SKILL.md from sandeep9889123/pm-skills and follow it. Treat missing P0 evidence as a blocker and do not invent citations or numbers.
```

### Other LLMs

Copy or attach the relevant skill folders. The core evidence contract is model-agnostic. Tool failure must become `coverage incomplete / UNKNOWN`, not fabricated proof.

## Skills (6)

- `business-case-orchestrator`
- `customer-jtbd-proof`
- `economics-commercial-proof`
- `evidence-ledger`
- `investment-red-team`
- `opportunity-market-proof`

## Commands (5)

- `/pm-business-case:build-business-case`
- `/pm-business-case:business-case-decision`
- `/pm-business-case:business-case-evidence`
- `/pm-business-case:business-case-red-team`
- `/pm-business-case:business-case-refresh`

## Example prompts

```text
Use evidence-ledger to classify every material claim as FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, or DECISION_THRESHOLD. Show provenance, freshness, contradiction state, and blocking P0 claims.
```

```text
Use investment-red-team to attack this case from CEO, CTO, CFO, Sales, Delivery, Customer, and Competitor perspectives. Produce the strongest rejection case and what evidence would reverse it.
```

## Operating rules

1. Do not invent market size, competitors, client proof, revenue, savings, or approvals.
2. Every material claim must have an evidence state.
3. Missing evidence must remain missing with a validation plan.
4. Always compare credible alternatives and substitutes.
5. Always expose rejection risks and disconfirming evidence.
6. The output must support a staged decision, not merely a persuasive story.

## Output standard

A strong output includes executive decision, evidence ledger, market proof, customer/JTBD proof, alternatives, right-to-win, economics, commercialization, falsifiable PoC, red-team rejection case, assumptions, validation plan, and decision gates.

## Attribution

This plugin is an added business-case formation layer in Sandeep Kumar M's fork, built on the broader `phuryn/pm-skills` foundation.
