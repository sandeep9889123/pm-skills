# PM Market Research

Market research workflows for competitor discovery, segmentation, market sizing, user research, feedback analysis, and customer journey mapping.

This plugin is part of Sandeep Kumar M's enhanced `pm-skills` fork. It is hardened against a specific high-risk failure mode: stopping too early and claiming there are no competitors, no alternatives, or no market signal when the research path was incomplete.

## When to use

Use this plugin when you need to:

- identify direct, adjacent, and indirect competitors
- run competitor analysis
- synthesize user feedback
- research users and personas
- estimate market size
- segment markets or users
- map customer journeys
- analyze sentiment or qualitative signals
- prepare leadership-facing market evidence

## Skills included

- `competitor-analysis`
- `customer-journey-map`
- `market-segments`
- `market-sizing`
- `sentiment-analysis`
- `user-personas`
- `user-segmentation`

## Commands included

- `/analyze-feedback`
- `/competitive-analysis`
- `/research-users`

## Operating rules

1. Never conclude “no competitors” without searching direct competitors, adjacent players, substitutes, internal build alternatives, service firms, open-source options, and workflow workarounds.
2. Always list the search strategy and evidence gaps.
3. Separate competitors from alternatives and substitutes.
4. Do not invent market size numbers.
5. Use confidence labels for every major finding.
6. Include disconfirming evidence and false-negative risk.

## Example use

```text
Use pm-market-research to identify competitors for this enterprise AI validation solution. Include direct competitors, adjacent platforms, substitutes, open-source alternatives, service providers, evidence strength, and research gaps.
```

## Output standard

A strong output from this plugin should include:

- category definition
- user segments
- competitor map
- alternatives and substitutes
- evidence table
- market signals
- gaps and unknowns
- implications for product and GTM

## Attribution

Based on the original `phuryn/pm-skills` market research workflows. Enhanced in this fork with stronger anti-hallucination, competitor false-negative prevention, and evidence-led research discipline.
