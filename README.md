# PM Skills: Reliability-First Enterprise AI Edition

[![Tests](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml/badge.svg)](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Upstream](https://img.shields.io/badge/upstream-phuryn%2Fpm--skills-blue?style=flat-square)](https://github.com/phuryn/pm-skills)

> **A fork of [phuryn/pm-skills](https://github.com/phuryn/pm-skills) focused on evidence integrity, adversarial reliability, Enterprise AI product management, and decision quality.**

The upstream project provides an excellent PM framework marketplace. This fork keeps that foundation and adds a different question:

> **Does the skill still make a good product decision when the first search is weak, the evidence is sparse, the user is wrong, the data is noisy, or the model is overconfident?**

The baseline currently contains **68 PM skills and 42 chained workflows across 9 plugins**.

## Why this fork exists

A PM skill can look excellent on the happy path and still fail in the exact situations where judgment matters most.

Example: a competitor-analysis skill runs one weak search, finds little, and concludes there are no competitors. The user then says, “I found a competitor,” and suddenly the model searches harder and discovers several real players.

That is not a research problem. It is a **reliability problem**.

This fork is designed to reduce that class of failure by adding:

- **Search exhaustion before negative conclusions**
- **Contradiction probes and second-pass challenge**
- **FACT / INFERENCE / ASSUMPTION / ESTIMATE / UNKNOWN discipline**
- **Source freshness and evidence quality checks**
- **Explicit edge-case and failure-mode scenarios**
- **Semantic quality tests in addition to structural CI**
- **Hard gates for decision-critical errors**
- **Enterprise AI PM workflows and evaluation patterns**

## Reliability Contract

Every skill should be able to survive more than the obvious happy path.

Before making a material recommendation, high-risk skills should ask:

1. **What evidence supports this?**
2. **What evidence would contradict it?**
3. **Did the first query fail, or does the market/data genuinely show absence?**
4. **What alternative framing, segment, category, workflow, or substitute did I miss?**
5. **What is fact, inference, estimate, assumption, stale evidence, or unknown?**
6. **What would change the recommendation?**
7. **What is the cost of being wrong?**

A negative conclusion such as “no competitors,” “no demand,” “no risk,” or “no statistically meaningful effect” must be earned, not inferred from a weak first pass.

See:

- [`docs/standards/PM_SKILL_QUALITY_STANDARD_V1.md`](docs/standards/PM_SKILL_QUALITY_STANDARD_V1.md)
- [`docs/standards/RELIABILITY_CONTRACT_V1.md`](docs/standards/RELIABILITY_CONTRACT_V1.md)
- [`reliability/SCENARIO_CATALOG.md`](reliability/SCENARIO_CATALOG.md)
- [`docs/audit/PM_SKILLS_AUDIT_V1.md`](docs/audit/PM_SKILLS_AUDIT_V1.md)

## What is new in this fork

### 1. Adversarial scenario coverage

Every skill family is tested against scenarios beyond the default request:

`ambiguous scope` · `missing context` · `sparse evidence` · `zero-result search` · `false user premise` · `contradictory evidence` · `stale data` · `noisy input` · `small sample` · `outliers` · `tool failure` · `conflicting objectives` · `high-consequence decision`

High-risk skills get explicit golden scenarios with required and forbidden behaviors.

### 2. Research that distrusts its first answer

Research-heavy skills use a **Search → Challenge → Expand → Verify → Conclude** loop.

For competitor intelligence this means searching not only company names, but also:

- direct category competitors
- adjacent categories
- substitutes and manual workflows
- build-in-house alternatives
- buyer/problem language
- technology and workflow language
- regional players
- newly launched or niche entrants

Only after query diversification and source triangulation may the skill conclude that no verified direct competitor was found.

### 3. Evidence-first decisions

Research and strategy outputs should distinguish:

- **FACT**: directly supported by evidence
- **INFERENCE**: reasoned interpretation of facts
- **ASSUMPTION**: unverified belief required for the plan
- **ESTIMATE**: modeled or approximate value
- **UNKNOWN**: evidence is insufficient
- **STALE**: evidence exists but may no longer be current

False precision is treated as a defect.

### 4. Semantic quality checks

The original repository already validates manifests, versions, naming, references, and repository consistency.

This fork adds tests for **behavioral safeguards**. Examples:

- competitor analysis cannot regress to a one-query negative conclusion
- interview summaries must verify verbatim quotes
- A/B analysis must not claim 80% power using a formula that omits the power term
- every plugin is mapped to adversarial scenario families

### 5. Enterprise AI PM direction

The next differentiated plugin layer focuses on the decisions PMs increasingly own in AI products:

- AI use-case prioritization
- evaluation contracts and golden datasets
- RAG evaluation
- agent evaluation
- human-in-the-loop policy
- cost × latency × quality trade-offs
- build vs buy vs partner
- rollout, rollback, observability, trust, and governance

## Start here

**Competitor research** → use `competitor-analysis` and inspect the new search-exhaustion and contradiction pass.

**Product discovery** → `/discover`

**Product strategy** → `/strategy`

**PRD** → `/write-prd`

**GTM** → `/plan-launch`

**Metrics** → `/north-star`

**AI-built product shipping** → `/ship-check`

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
```

Claude slash commands remain Claude-specific. In Codex, describe the workflow in plain language when a command is not directly exposed.

## Available plugins

<details>
<summary><strong>1. pm-product-discovery</strong> — discovery and validation (13 skills, 5 commands)</summary>

Ideation, assumptions, experiments, interviews, Opportunity Solution Trees, feature requests, and discovery metrics.
</details>

<details>
<summary><strong>2. pm-product-strategy</strong> — strategy and business model (12 skills, 5 commands)</summary>

Product strategy, vision, pricing, value propositions, canvases, SWOT, PESTLE, Porter's Five Forces, and Ansoff.
</details>

<details>
<summary><strong>3. pm-execution</strong> — delivery and decision artifacts (16 skills, 11 commands)</summary>

PRDs, OKRs, roadmaps, sprints, retrospectives, stories, test scenarios, stakeholder management, pre-mortems, and red-teaming.
</details>

<details>
<summary><strong>4. pm-market-research</strong> — research and competitive intelligence (7 skills, 3 commands)</summary>

Competitors, market sizing, personas, segmentation, customer journeys, and feedback analysis. This is the first plugin receiving the new reliability guards.
</details>

<details>
<summary><strong>5. pm-data-analytics</strong> — quantitative product analysis (3 skills, 3 commands)</summary>

SQL, cohort analysis, and A/B test analysis.
</details>

<details>
<summary><strong>6. pm-go-to-market</strong> — enterprise and product GTM (6 skills, 3 commands)</summary>

Beachheads, ICPs, GTM strategy, motions, growth loops, and battlecards.
</details>

<details>
<summary><strong>7. pm-marketing-growth</strong> — positioning and growth (5 skills, 2 commands)</summary>

Positioning, value propositions, product naming, marketing ideas, and North Star metrics.
</details>

<details>
<summary><strong>8. pm-toolkit</strong> — PM utilities (4 skills, 5 commands)</summary>

Resume review, proofreading, NDA drafting, and privacy-policy support.
</details>

<details>
<summary><strong>9. pm-ai-shipping</strong> — reviewability for AI-built products (2 skills, 5 commands)</summary>

System documentation, intended-vs-implemented auditing, test derivation, security review, performance review, and shipping readiness.
</details>

## Reliability roadmap

### V1

- [x] Baseline audit and quality standard
- [x] Reliability contract
- [x] Adversarial scenario catalog
- [x] Competitor-analysis search exhaustion and contradiction pass
- [x] Interview quote verification guard
- [x] A/B power-analysis correction
- [x] Semantic regression tests for P0 guards

### Next

- [ ] Expand behavioral golden scenarios across every high-risk skill
- [ ] Add evidence contracts to research-heavy skills
- [ ] Add Enterprise AI PM plugin
- [ ] Add enterprise-product workflows
- [ ] Add executive-decision workflows
- [ ] Track skill-quality score changes release by release

## Contribution philosophy

This fork distinguishes between two kinds of work:

**Upstream-worthy improvements**

Correctness fixes and generic reliability improvements that benefit the original marketplace should be proposed back to [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) when appropriate.

**Fork differentiation**

Enterprise AI PM capabilities, semantic evaluation infrastructure, opinionated evidence contracts, and executive decision workflows may evolve faster here.

## Attribution

This repository is a fork of **[Paweł Huryn's PM Skills Marketplace](https://github.com/phuryn/pm-skills)** and preserves the original MIT license and attribution.

The goal of this fork is not to relabel upstream work. It is to test, harden, and extend it with reliability and Enterprise AI product-management capabilities.

## License

MIT. See [`LICENSE`](LICENSE).
