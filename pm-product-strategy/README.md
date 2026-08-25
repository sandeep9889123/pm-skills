# PM Product Strategy

Product strategy workflows for turning market context, customer needs, competitive pressure, monetization options, and constraints into explicit choices and trade-offs.

## When to use

Use this plugin when you need to define product strategy, sharpen vision, evaluate business models, pressure-test pricing, write a value proposition, run a market scan, or prepare leadership-ready strategic choices.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-product-strategy@pm-skills
```

Example:

```text
/pm-product-strategy:strategy B2B AI workflow platform for operations teams
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-product-strategy@pm-skills
```

```text
Use pm-product-strategy to create three strategic options for this product, explicit trade-offs, a right-to-win hypothesis, what we should not do, and the evidence required before commitment.
```

### ChatGPT

Upload a specific skill folder if Skills is available, for example `skills/pricing-strategy/`.

With the GitHub app:

```text
Read pm-product-strategy/skills/product-strategy/SKILL.md from sandeep9889123/pm-skills and follow it for this product.
```

### Other LLMs

Copy the relevant `skills/*` folders into your Agent Skills directory or attach `SKILL.md`. For multi-stage strategy work, describe the desired sequence in plain language or also provide the relevant `commands/*.md` file.

## Skills (12)

- `ansoff-matrix`
- `business-model`
- `lean-canvas`
- `monetization-strategy`
- `pestle-analysis`
- `porters-five-forces`
- `pricing-strategy`
- `product-strategy`
- `product-vision`
- `startup-canvas`
- `swot-analysis`
- `value-proposition`

## Commands (5)

- `/pm-product-strategy:business-model`
- `/pm-product-strategy:market-scan`
- `/pm-product-strategy:pricing`
- `/pm-product-strategy:strategy`
- `/pm-product-strategy:value-proposition`

## Example prompts

```text
Use the pricing-strategy skill to compare three pricing models. Separate current evidence from willingness-to-pay hypotheses, include break-even logic, and state what experiment should run next.
```

```text
Use pm-product-strategy to assess this market using PESTLE, Five Forces, SWOT, and Ansoff only where each framework changes a real strategic decision. Do not fill frameworks for completeness.
```

## Operating rules

1. Strategy must force trade-offs.
2. Framework completion is not strategic insight.
3. Separate facts, assumptions, and judgment.
4. Define the segment and competitive context before recommending direction.
5. State what the company should not do.
6. Use frameworks as scaffolding, not the final answer.

## Output standard

A strong output includes strategic context, target users/segments, market dynamics, options considered, recommendation, trade-offs, risks, assumptions, and decision checkpoints.

## Attribution

Based on the original `phuryn/pm-skills` product strategy work, enhanced with stronger decision discipline and evidence separation.
