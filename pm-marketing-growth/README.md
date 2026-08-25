# PM Marketing Growth

Marketing and growth workflows for North Star metrics, positioning, product naming, value propositions, and marketing idea generation.

## When to use

Use this plugin when you need to define a North Star metric, name a product, create positioning/value propositions, brainstorm channel-aware marketing ideas, or sharpen external-facing PM narratives.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-marketing-growth@pm-skills
```

```text
/pm-marketing-growth:market-product [product context]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-marketing-growth@pm-skills
```

```text
Use pm-marketing-growth to create positioning and value propositions for this target segment. Include pain, promise, proof, alternatives, objections, and channel implications.
```

### ChatGPT

Upload a skill such as `skills/positioning-ideas/` or `skills/north-star-metric/` when Skills is available.

With the GitHub app:

```text
Read pm-marketing-growth/skills/positioning-ideas/SKILL.md from sandeep9889123/pm-skills and follow it for this product.
```

### Other LLMs

Copy or attach the relevant skill folder. Use a plain-language workflow request where command syntax is unavailable.

## Skills (5)

- `marketing-ideas`
- `north-star-metric`
- `positioning-ideas`
- `product-name`
- `value-prop-statements`

## Commands (2)

- `/pm-marketing-growth:market-product`
- `/pm-marketing-growth:north-star`

## Example prompts

```text
Use north-star-metric to define one value-linked North Star and a small set of guardrails. Reject vanity metrics and explain the failure modes of the chosen metric.
```

```text
Use product-name to generate naming territories for this brand. Check distinctiveness, pronunciation, category fit, negative meanings, and validation steps before recommending a winner.
```

## Operating rules

1. Do not use vague AI-powered positioning unless the AI value is specific.
2. Name the target segment before messaging.
3. Link value propositions to real pain or measurable outcomes.
4. A North Star must reflect delivered value, not activity.
5. Positioning should say what the product is not for.
6. Marketing ideas should connect to distribution and proof.

## Output standard

A strong output includes target audience, problem insight, positioning options, value propositions, proof points, North Star, channel ideas, and messaging risks.

## Attribution

Based on the original `phuryn/pm-skills` marketing-growth workflows, enhanced with sharper positioning and proof-backed messaging expectations.
