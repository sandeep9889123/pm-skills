# PM Market Research

Reliability-first market research for competitor discovery, segmentation, market sizing, user research, qualitative analysis, and customer journeys.

## When to use

Use this plugin when you need to identify competitors, synthesize user feedback, research personas or segments, estimate market size, map journeys, analyze sentiment, or prepare leadership-facing market evidence.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-market-research@pm-skills
```

```text
/pm-market-research:competitive-analysis enterprise AI document validation
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-market-research@pm-skills
```

```text
Use pm-market-research competitor-analysis for this market. Search direct, adjacent, substitute, incumbent, services, manual, open-source, internal-build, regional, and emerging alternatives before concluding.
```

### ChatGPT

Upload `skills/competitor-analysis/`, `skills/market-sizing/`, or another specific skill if Skills is available.

With the GitHub app:

```text
Read pm-market-research/skills/competitor-analysis/SKILL.md from sandeep9889123/pm-skills and follow it. Show search coverage and unresolved candidates.
```

### Other LLMs

Copy the required `skills/*` folders into your Agent Skills directory or attach the relevant `SKILL.md`. The reliability guards remain applicable even if the model has no search tools. Tool failure means incomplete coverage, not market absence.

## Skills (7)

- `competitor-analysis`
- `customer-journey-map`
- `market-segments`
- `market-sizing`
- `sentiment-analysis`
- `user-personas`
- `user-segmentation`

## Commands (3)

- `/pm-market-research:analyze-feedback`
- `/pm-market-research:competitive-analysis`
- `/pm-market-research:research-users`

## Example prompts

```text
Use competitor-analysis to identify direct competitors, adjacent players, substitutes, internal builds, services, open source, incumbents, regional players, and emerging entrants. Verify user-supplied names independently.
```

```text
Use market-sizing to build transparent top-down and bottom-up ranges. Do not average incompatible reports or derive SOM from an arbitrary TAM percentage.
```

## Operating rules

1. Never conclude no competitors from a weak first pass.
2. Show search strategy and evidence gaps.
3. Separate competitors, alternatives, and substitutes.
4. Do not invent market-size numbers.
5. Use evidence states and confidence for material findings.
6. Include disconfirming evidence and false-negative risk.

## Output standard

A strong output includes category definition, segments, competitor/alternative map, evidence table, market signals, gaps/unknowns, and implications for product and GTM.

## Attribution

Based on the original `phuryn/pm-skills` market research workflows, enhanced with anti-hallucination and false-negative prevention.
