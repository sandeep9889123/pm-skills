# PM Skills: Reliability-First Enterprise AI Edition

[![Tests](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml/badge.svg)](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Upstream](https://img.shields.io/badge/upstream-phuryn%2Fpm--skills-blue?style=flat-square)](https://github.com/phuryn/pm-skills)

> **An evidence-first fork of [phuryn/pm-skills](https://github.com/phuryn/pm-skills) for PMs who need decisions to survive weak searches, sparse evidence, false premises, noisy data, enterprise constraints, and AI failure modes.**

**80 PM skills and 46 chained workflows across 10 plugins.**

This fork keeps the upstream PM framework foundation and adds three layers:

1. **Reliability** — adversarial scenarios, contradiction passes, uncertainty labels, hard gates, and semantic regression checks.
2. **Enterprise decision quality** — stronger strategy, PRD, pricing, GTM, prioritization, roadmap, stakeholder, risk, research, and experimentation behavior.
3. **Enterprise transformation** — repeatable workflows for **Building Future Capabilities**, **Client Success → Sales GTM**, **Sales Transformation**, and **Tooling & Automation**.

The quality target is **100/100 decision usefulness**, but the repo does not award itself that score. High-risk behavior is encoded as testable contracts so weaknesses can be found and improved rather than hidden behind polished output.

## Why this fork exists

A PM skill can look excellent on a happy-path demo and still fail where judgment matters.

A real trigger for this fork: competitor analysis ran a weak first search and concluded there were no competitors. After the user challenged the answer, the model searched harder and found credible players.

That failure pattern is broader than market research:

- one client request becomes “market demand”;
- bespoke project code becomes “reusable IP”;
- a target metric becomes a client success claim;
- a successful PoC is mistaken for production readiness;
- a sales win-rate increase hides worse opportunity quality;
- an automation saves authoring time but creates more review work;
- a strategy canvas is complete but no real strategic choice was made.

This fork turns those failures into:

> **Observed failure → adversarial scenario → runtime guard → semantic regression test**

## Reliability Contract

High-consequence skills should explicitly ask:

1. What evidence supports this?
2. What evidence contradicts it?
3. Is a zero result evidence of absence, or a weak search/tool failure?
4. What alternative category, segment, workflow, substitute, or explanation was missed?
5. What is `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, or `STALE`?
6. What would change the recommendation?
7. What is the cost of being wrong?
8. What is the cheapest credible test?
9. What is the hard gate or kill criterion?
10. Who owns the next decision?

See:
- [`docs/standards/PM_SKILL_QUALITY_STANDARD_V1.md`](docs/standards/PM_SKILL_QUALITY_STANDARD_V1.md)
- [`docs/standards/RELIABILITY_CONTRACT_V1.md`](docs/standards/RELIABILITY_CONTRACT_V1.md)
- [`reliability/SCENARIO_CATALOG.md`](reliability/SCENARIO_CATALOG.md)
- [`reliability/scenario_matrix.json`](reliability/scenario_matrix.json)
- [`docs/audit/PM_SKILLS_AUDIT_V1.md`](docs/audit/PM_SKILLS_AUDIT_V1.md)

## Enterprise Transformation Operating System

### 1. Building Future Capabilities

Use `/build-future-capability` when deciding whether a recurring customer/delivery problem should become a reusable method, accelerator, productized solution, platform capability, or buy/partner decision.

It chains:

`capability-opportunity-radar → reusable-accelerator-thesis → solution-business-case`

The workflow requires independent demand signals, right-to-win, common-core/reuse evidence, alternatives, reachable economics, scenario sensitivity, pilot gates, and kill criteria.

### 2. Existing Client Success → Sales GTM

Use `/proof-to-gtm` to turn completed delivery into reusable commercial proof without inventing outcomes or leaking confidential information.

It chains:

`client-proof-extractor → case-study-to-gtm → account-expansion-play`

The workflow separates `MEASURED`, `CLIENT-CONFIRMED`, `DELIVERED`, `OBSERVED`, `TARGET`, `INFERENCE`, and `UNKNOWN` before a claim can enter sales collateral.

### 3. Sales Transformation

Use `/transform-sales` to diagnose the highest-value funnel constraint, redesign the selling motion, and test interventions.

It chains:

`sales-funnel-diagnostic → solution-to-sales-playbook → pipeline-conversion-experiment`

It explicitly checks for fake improvements such as higher win rate from cherry-picking, shorter cycle from smaller deals, or proposal losses caused by weak qualification upstream.

### 4. Tooling & Automation

Use `/automate-pm-workflow` to decide what to automate, what to assist, and what must remain human-owned.

It chains:

`pm-workflow-automation → tool-evaluation-selection → automation-governance`

The workflow covers HITL, permissions, validation, auditability, retries/idempotency, rollback, kill switches, TCO, review burden, and shadow-mode rollout.

## What has been hardened

### Market intelligence

Competitor research now uses:

**Search → Challenge → Expand → Verify → Conclude**

Before a negative conclusion it checks category, problem language, JTBD/workflow, buyer terminology, adjacent categories, substitutes/manual workflows, build-in-house alternatives, regional players, and emerging entrants.

### Product and strategy

Core skills now include decision/evidence gates for:
- product strategy
- pricing strategy
- PRDs
- prioritization
- outcome roadmaps
- stakeholder/decision rights
- pre-mortems
- new-product experiments
- existing-product experiments
- segmentation

### GTM and measurement

GTM now models the enterprise path through buyer/champion, technical/security review, procurement, implementation, adoption, expansion, and renewal. Battlecards require evidence and acknowledge where the competitor is stronger. North Star selection tests Goodhart/gaming and causal assumptions.

### AI / analytics quality

A/B analysis includes correct power logic, SRM, optional stopping, multiple comparisons, practical significance, and guardrails. Interview synthesis verifies verbatim quotes. AI shipping retains intended-vs-implemented reviewability.

## Start here

| Goal | Start with |
|---|---|
| Build a reusable future capability | `/build-future-capability` |
| Convert client success into GTM | `/proof-to-gtm` |
| Improve sales conversion | `/transform-sales` |
| Automate a PM/solution workflow | `/automate-pm-workflow` |
| Competitive intelligence | `/competitive-analysis` |
| Product discovery | `/discover` |
| Product strategy | `/strategy` |
| PRD | `/write-prd` |
| GTM launch | `/plan-launch` |
| Metrics | `/north-star` |
| AI-built product shipping | `/ship-check` |

## Installation

### Claude Code

```bash
claude plugin marketplace add sandeep9889123/pm-skills

claude plugin install pm-product-discovery@pm-skills
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-execution@pm-skills
claude plugin install pm-market-research@pm-skills
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-toolkit@pm-skills
claude plugin install pm-ai-shipping@pm-skills
claude plugin install pm-enterprise-transformation@pm-skills
```

### Codex CLI

```bash
codex plugin marketplace add sandeep9889123/pm-skills

codex plugin add pm-product-discovery@pm-skills
codex plugin add pm-product-strategy@pm-skills
codex plugin add pm-execution@pm-skills
codex plugin add pm-market-research@pm-skills
codex plugin add pm-data-analytics@pm-skills
codex plugin add pm-go-to-market@pm-skills
codex plugin add pm-marketing-growth@pm-skills
codex plugin add pm-toolkit@pm-skills
codex plugin add pm-ai-shipping@pm-skills
codex plugin add pm-enterprise-transformation@pm-skills
```

Claude slash commands remain Claude-specific. In Codex, invoke the named workflow in natural language when a slash command is not directly exposed.

## Available plugins

<details>
<summary><strong>1. pm-product-discovery</strong> — discovery and validation (13 skills, 5 commands)</summary>

Ideation, assumptions, evidence-aware experiments, interviews, Opportunity Solution Trees, prioritization, and discovery metrics.
</details>

<details>
<summary><strong>2. pm-product-strategy</strong> — strategy and economics (12 skills, 5 commands)</summary>

Product strategy, vision, pricing, value propositions, business models, competitive/macro frameworks, trade-offs, falsification, and scenario economics.
</details>

<details>
<summary><strong>3. pm-execution</strong> — delivery and decision artifacts (16 skills, 11 commands)</summary>

Decision-first PRDs, OKRs, outcome roadmaps, sprints, stories, test scenarios, stakeholder decision rights, pre-mortems, and red-teaming.
</details>

<details>
<summary><strong>4. pm-market-research</strong> — evidence-first research and competitive intelligence (7 skills, 3 commands)</summary>

Competitors, market sizing, personas, segmentation, journeys, and feedback analysis with search exhaustion, contradiction passes, evidence ledgers, and uncertainty handling.
</details>

<details>
<summary><strong>5. pm-data-analytics</strong> — quantitative product decisions (3 skills, 3 commands)</summary>

SQL, cohort analysis, and experiment analysis with statistical safeguards.
</details>

<details>
<summary><strong>6. pm-go-to-market</strong> — enterprise and product GTM (6 skills, 3 commands)</summary>

Beachheads, ICPs/anti-ICPs, enterprise buying/production journey, GTM economics, motions, growth loops, and evidence-backed battlecards.
</details>

<details>
<summary><strong>7. pm-marketing-growth</strong> — positioning and growth (5 skills, 2 commands)</summary>

Positioning, value propositions, product naming, marketing ideas, and North Star metrics with gaming/causal checks.
</details>

<details>
<summary><strong>8. pm-toolkit</strong> — PM utilities (4 skills, 5 commands)</summary>

Resume review, proofreading, NDA drafting, and privacy-policy support.
</details>

<details>
<summary><strong>9. pm-ai-shipping</strong> — reviewability for AI-built products (2 skills, 5 commands)</summary>

System documentation, intended-vs-implemented auditing, test derivation, security review, performance review, and shipping readiness.
</details>

<details>
<summary><strong>10. pm-enterprise-transformation</strong> — capability building, proof-to-GTM, sales transformation, and automation (12 skills, 4 commands)</summary>

Future capability investment, reusable accelerators, business cases, client proof, repeatable sales/GTM, account expansion, funnel diagnostics, sales experiments, PM workflow automation, tool selection, and governance.
</details>

## Reliability architecture

Every skill inherits global + plugin-specific adversarial scenario families. Decision-critical files also have explicit `must_contain` behavior contracts protected by `tests/test_reliability_contracts.py`.

This is not full end-to-end LLM evaluation yet. It is a regression layer that prevents known reliability safeguards from silently disappearing while the behavioral evaluation suite expands.

## Roadmap

### Shipped
- [x] Baseline audit and PM Skill Quality Standard
- [x] Reliability Contract
- [x] Adversarial scenario matrix across all plugins
- [x] Search-exhaustion competitor intelligence
- [x] Quote-verification and A/B correctness guards
- [x] High-value hardening across strategy, PRD, pricing, GTM, prioritization, metrics, roadmap, stakeholders, risk, experiments, and segmentation
- [x] Enterprise Transformation plugin for the four enterprise motions

### Next
- [ ] Build executable golden prompt/output eval cases for high-risk skills
- [ ] Add model-agnostic scoring harness for decision quality
- [ ] Add Enterprise AI product-decision plugin: evaluation contracts, RAG, agents, HITL, model/provider selection, cost/latency/quality, rollout and observability
- [ ] Benchmark before/after skill behavior across Claude and Codex where reproducible
- [ ] Track reliability score changes release by release

## Contribution philosophy

**Upstream-worthy:** generic correctness/reliability improvements that benefit the original marketplace should be proposed back to [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) when appropriate.

**Fork differentiation:** enterprise transformation, Enterprise AI PM, semantic evaluation, evidence contracts, and executive decision workflows can evolve independently here.

## Attribution

This repository is a fork of **[Paweł Huryn's PM Skills Marketplace](https://github.com/phuryn/pm-skills)** and preserves the original MIT license and attribution.

The fork-specific work is the reliability/evaluation layer, hardened decision behaviors, and enterprise transformation extensions. Upstream work is not relabeled as original work.

## License

MIT. See [`LICENSE`](LICENSE).
