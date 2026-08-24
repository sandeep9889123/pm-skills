# PM Skills, Evidence-First PM Operating System for Claude

A Claude plugin marketplace for product managers who want **repeatable, evidence-led PM execution** across discovery, strategy, execution, market research, GTM, analytics, AI shipping, enterprise transformation, and business-case formation.

This repository is a fork and extension of [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills). The original framework created a strong PM skills foundation. This fork adds a reliability-first operating layer for higher-stakes PM work, especially where weak research, hallucinated competitors, shallow business cases, and generic PM outputs are unacceptable.

## What changed in this fork

This fork is no longer positioned as a simple copy of the upstream PM skills library. It is organized as a **PM operating system for Claude Cowork and Claude Code**.

Key additions and hardening areas:

- **Evidence-first business-case system** for migration agents, AI accelerators, enterprise solution bets, and practice capability investments.
- **Enterprise transformation layer** for building future capabilities, converting client proof into GTM, sales transformation, tooling, and automation.
- **Market-research reliability guardrails** designed to avoid the common failure mode where the model says “no competitors found” too early.
- **Structured red-team and decision gates** for leadership-facing proposals.
- **Cowork-oriented marketplace manifest** with explicit GitHub-backed plugin sources.
- **Reliability contracts, scenario catalogs, and evaluation harnesses** to reduce hallucination and force evidence separation.
- **README and plugin documentation refresh** so each plugin is clearly positioned for practical PM workflows, not generic prompt use.

## Repository inventory

Current marketplace inventory:

| Asset type | Count |
|---|---:|
| Plugins | 11 |
| Skills | 86 |
| Commands | 51 |
| Total skill + command assets | 137 |

## Plugin suite

| Plugin | Purpose |
|---|---|
| `pm-product-discovery` | Research, interviews, feature triage, assumptions, opportunity mapping, and discovery synthesis. |
| `pm-product-strategy` | Product strategy, market scan, pricing, positioning, business models, and strategic frameworks. |
| `pm-execution` | PRDs, user stories, OKRs, roadmap transformation, sprint planning, stakeholder mapping, test scenarios, and red-team reviews. |
| `pm-market-research` | Competitor analysis, user research, segmentation, market sizing, sentiment analysis, and customer journey mapping. |
| `pm-data-analytics` | SQL, cohort analysis, A/B test analysis, and product analytics interpretation. |
| `pm-go-to-market` | ICP, GTM motions, beachhead segments, battlecards, launch planning, and growth strategy. |
| `pm-marketing-growth` | North-star metrics, product naming, positioning, value propositions, and marketing ideas. |
| `pm-toolkit` | Resume review, proofreading, NDA drafting, privacy policy drafting, and PM utility workflows. |
| `pm-ai-shipping` | AI product shipping checks, intended-vs-implemented review, documentation, security, performance, and test derivation. |
| `pm-enterprise-transformation` | Future capability building, sales transformation, proof-to-GTM, automation governance, reusable accelerators, and tool selection. |
| `pm-business-case` | Evidence-led business cases with market proof, JTBD proof, commercial proof, evidence ledgers, red-team risks, and decision gates. |

## Installation

### Claude Cowork / Claude Desktop

Use the marketplace URL:

```text
https://github.com/sandeep9889123/pm-skills
```

Recommended settings:

```text
Sync automatically = OFF
```

After installing, open Cowork and type `/` to search available skills and workflows.

### Claude Code CLI

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin marketplace list
```

Then install the plugin set you need, for example:

```bash
claude plugin install pm-business-case@pm-skills
claude plugin install pm-market-research@pm-skills
claude plugin install pm-enterprise-transformation@pm-skills
```

## Recommended PM workflows

### Build an enterprise business case

Use:

- `pm-business-case`
- `pm-market-research`
- `pm-enterprise-transformation`
- `pm-execution`

Expected output:

- evidence ledger
- assumptions register
- market proof
- JTBD proof
- commercial model
- competitive scan
- decision gates
- red-team rejection risks

### Convert client success stories into GTM assets

Use:

- `pm-enterprise-transformation`
- `pm-go-to-market`
- `pm-marketing-growth`

Expected output:

- proof inventory
- anonymized case-study skeleton
- target segment mapping
- battlecard inputs
- GTM narrative
- sales enablement checklist

### Harden market research

Use:

- `pm-market-research`
- `pm-product-strategy`
- `pm-business-case`

Expected output:

- named competitor set
- adjacent alternatives
- indirect substitutes
- search strategy log
- evidence strength labels
- gaps and false-negative risks

### Ship an AI PM prototype or AI-enabled workflow

Use:

- `pm-ai-shipping`
- `pm-execution`
- `pm-data-analytics`

Expected output:

- intended-vs-implemented review
- test scenarios
- analytics events
- security/performance caveats
- launch-readiness checklist

## Reliability principles

This fork is optimized for **low-hallucination PM work**.

Every high-stakes output should separate:

- verified facts
- source-backed evidence
- weak signals
- assumptions
- model judgment
- open questions
- disconfirming evidence
- decision risks

The model should not invent competitors, market sizes, customers, benchmarks, case studies, financials, or stakeholder decisions. Where evidence is missing, the expected behavior is to say so and produce a validation plan.

## Attribution

Original PM skills foundation: [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills).

This fork: maintained and extended by Sandeep Kumar M with added reliability-first business-case, enterprise-transformation, market-research, GTM, and automation layers.

## License

MIT, following the upstream project license.
