# PM Skills: Reliability-First Enterprise AI Edition

A model-agnostic PM operating system for **repeatable, evidence-led product and enterprise solution work** across discovery, prospect discovery, strategy, execution, market research, GTM, analytics, AI shipping, enterprise transformation, and business-case formation.

This repository is a fork and extension of [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills). The upstream project created the core PM skills foundation. This fork adds reliability contracts, adversarial decision gates, enterprise workflows, and portable prompt/skill patterns for higher-stakes PM work where hallucinated evidence, shallow research, and premature commitments are unacceptable.

The reliability loop is:

`Search → Challenge → Expand → Verify → Conclude`

The repository can be used with Claude plugin surfaces, Agent-Skills-compatible runtimes, Codex-style agents, or any capable LLM that can read the Markdown skill and prompt files.

## Current inventory

**96 PM skills and 55 chained workflows across 12 plugins.**

| Asset type | Count |
|---|---:|
| Plugins | 12 |
| Skills | 96 |
| Commands / workflows | 55 |
| Total skill + command assets | 151 |

## What this fork adds

- **Evidence-first business-case system** for migration agents, AI accelerators, enterprise solution bets, and practice capability investments.
- **Enterprise transformation layer** for future capabilities, client-proof-to-GTM, sales transformation, tooling, and automation.
- **Prospect Discovery Engine** for repeatable pre-RFP solution discovery, hypothesis falsification, adaptive questioning, assumption tracking, and proposal readiness.
- **Market-research reliability guardrails** against false negative competitor searches and unsupported market conclusions.
- **Structured red-team and decision gates** for leadership-facing proposals and investment choices.
- **Behavioral evaluation and scenario contracts** that protect high-consequence reasoning rules from silent regression.
- **Model-agnostic usage paths** so core capability does not depend on one LLM provider.

## Plugin suite

| Plugin | Purpose |
|---|---|
| `pm-product-discovery` | Research, interviews, feature triage, assumptions, opportunity mapping, and discovery synthesis. |
| `pm-prospect-discovery` | Enterprise pre-RFP discovery, prospect research, hypothesis validation, adaptive questions, assumption registers, session synthesis, and proposal-readiness gates. |
| `pm-product-strategy` | Product strategy, market scan, pricing, positioning, business models, and strategic frameworks. |
| `pm-execution` | PRDs, user stories, OKRs, roadmaps, sprint planning, stakeholder mapping, test scenarios, and red-team reviews. |
| `pm-market-research` | Competitor analysis, user research, segmentation, market sizing, sentiment analysis, and customer journey mapping. |
| `pm-data-analytics` | SQL, cohort analysis, A/B test analysis, and product analytics interpretation. |
| `pm-go-to-market` | ICP, GTM motions, beachhead segments, battlecards, launch planning, and growth strategy. |
| `pm-marketing-growth` | North-star metrics, product naming, positioning, value propositions, and marketing ideas. |
| `pm-toolkit` | Resume review, proofreading, NDA drafting, privacy policy drafting, and PM utility workflows. |
| `pm-ai-shipping` | AI product shipping checks, intended-vs-implemented review, documentation, security, performance, and test derivation. |
| `pm-enterprise-transformation` | Future capability building, sales transformation, proof-to-GTM, automation governance, reusable accelerators, and tool selection. |
| `pm-business-case` | Evidence-led business cases with market proof, JTBD proof, commercial proof, evidence ledgers, red-team risks, and decision gates. |

## Use with any LLM

Core skills live in `pm-*/skills/*/SKILL.md` as plain Markdown. Provider-specific command wrappers are optional.

For the new prospect-discovery capability, the most portable entry point is:

```text
pm-prospect-discovery/prompts/prospect-discovery-master.md
```

Give that file plus the prospect context and source material to the LLM. If tools are unavailable, the workflow must preserve missing evidence as `UNKNOWN` rather than fabricate it.

### Agent Skills compatible runtimes

Load the relevant `SKILL.md` files directly. Skill frontmatter follows the repository's portable Agent Skills convention.

### Other LLMs without skill loading

Paste the relevant skill or the plugin master prompt into the model and provide the task context. Command files can be treated as orchestration prompts by replacing `$ARGUMENTS` with the user input.

## Claude installation

### Claude Cowork / Claude Desktop

Use the marketplace URL:

```text
https://github.com/sandeep9889123/pm-skills
```

### Claude Code CLI

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin marketplace list
```

Install the plugin set you need, for example:

```bash
claude plugin install pm-prospect-discovery@pm-skills
claude plugin install pm-business-case@pm-skills
claude plugin install pm-market-research@pm-skills
```

## Recommended PM workflows

### Standardize pre-RFP prospect discovery

Use:

- `pm-prospect-discovery`

Expected output:

- evidence-classified account context
- problem and alternative-root-cause hypotheses
- ranked use-case wedges
- red-team rejection case
- 5-8 stage journey
- baseline / vision-aligned / differentiated solution anchors
- prioritized assumption register
- adaptive MUST ASK and Level 2 questions
- post-session synthesis
- readiness for solutioning, architecture, estimation, business case, and proposal

### Build an enterprise business case

Use:

- `pm-business-case`
- `pm-market-research`
- `pm-enterprise-transformation`
- `pm-execution`

Expected output includes evidence ledger, customer/JTBD proof, alternatives, reconstructable economics, GTM logic, rejection case, and gated investment decision.

### Convert client success into GTM

Use:

- `pm-enterprise-transformation`
- `pm-go-to-market`
- `pm-marketing-growth`

Expected output includes proof inventory, NDA-safe case-study skeleton, segment mapping, battlecard inputs, GTM narrative, and sales-enablement actions.

### Harden market and competitive research

Use:

- `pm-market-research`
- `pm-product-strategy`
- `pm-business-case`

Expected output includes direct and adjacent alternatives, search-strategy coverage, evidence states, contradiction checks, and false-negative risk.

### Ship an AI PM prototype or AI-enabled workflow

Use:

- `pm-ai-shipping`
- `pm-execution`
- `pm-data-analytics`

Expected output includes intended-vs-implemented review, tests, analytics events, security/performance caveats, and launch-readiness checks.

## Reliability principles

Every high-stakes output should distinguish, where applicable:

- `FACT`
- source-backed evidence
- `INFERENCE`
- `ASSUMPTION`
- `ESTIMATE`
- `UNKNOWN`
- `STALE`
- disconfirming evidence
- decision risks

The model must not invent competitors, market sizes, customers, prospect systems, APIs, benchmarks, case studies, financial inputs, quotes, or stakeholder decisions. Missing evidence should produce an explicit gap and validation path.

A strong-looking deliverable is not a substitute for decision readiness. `NOT READY`, `SECOND DISCOVERY REQUIRED`, `EXPERIMENT`, `HOLD`, and `KILL` are valid outcomes when evidence warrants them.

## Repository guidance for AI agents

`CLAUDE.md` is the repository-wide source of truth for contributors and AI agents. `AGENTS.md` points non-Claude agents to the same guidance.

## Attribution

Original PM skills foundation: [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills).

This fork is maintained and extended by Sandeep Kumar M. Upstream attribution is preserved for upstream-derived skills; fork-specific enterprise, reliability, business-case, prospect-discovery, and evaluation layers evolve independently.

## License

MIT, following the upstream project license.
