# PM Go To Market

GTM workflows for translating product proof, customer segments, positioning, launch strategy, battlecards, and growth motions into practical market execution.

## When to use

Use this plugin when you need to define ICPs, choose a beachhead segment, map GTM motions, create launch plans, build battlecards, translate proof into sales narrative, define growth loops, or align product, sales, and marketing.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-go-to-market@pm-skills
```

```text
/pm-go-to-market:plan-launch [product context]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-go-to-market@pm-skills
```

```text
Use pm-go-to-market to define ICP, anti-ICP, buying trigger, beachhead segment, proof points, objections, GTM motion, production path, and launch metrics.
```

### ChatGPT

Upload a skill such as `skills/gtm-strategy/` or `skills/competitive-battlecard/` when Skills is available.

With the GitHub app:

```text
Read pm-go-to-market/skills/gtm-strategy/SKILL.md from sandeep9889123/pm-skills and follow it for this product.
```

### Other LLMs

Copy or attach the relevant skill folders. Use natural-language workflow prompts where slash commands are unavailable.

## Skills (6)

- `beachhead-segment`
- `competitive-battlecard`
- `growth-loops`
- `gtm-motions`
- `gtm-strategy`
- `ideal-customer-profile`

## Commands (3)

- `/pm-go-to-market:battlecard`
- `/pm-go-to-market:growth-strategy`
- `/pm-go-to-market:plan-launch`

## Example prompts

```text
Use ideal-customer-profile to define user, buyer, economic buyer, buying trigger, current alternatives, anti-ICP, and evidence gaps for this enterprise solution.
```

```text
Use competitive-battlecard to build a sales-ready view of this competitor. Separate verified strengths/weaknesses from inference and include where they win, where we win, objections, and evidence freshness.
```

## Operating rules

1. Start with buyer, user, and buying trigger.
2. Do not create GTM content without proof points.
3. Separate ICP from broader TAM.
4. Identify objections and switching costs.
5. Match GTM motion to deal size, urgency, complexity, and buying committee.
6. Convert features into business outcomes and sales-ready evidence.

## Output standard

A strong output includes ICP, beachhead, positioning, proof points, GTM motion, launch plan, battlecard inputs, risks/objections, and success metrics.

## Attribution

Based on the original `phuryn/pm-skills` GTM workflows, enhanced with proof-to-sales and enterprise GTM discipline.
