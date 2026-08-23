# PM Skills: Reliability-First Enterprise AI Edition

[![Tests](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml/badge.svg)](https://github.com/sandeep9889123/pm-skills/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Upstream](https://img.shields.io/badge/upstream-phuryn%2Fpm--skills-blue?style=flat-square)](https://github.com/phuryn/pm-skills)

> **An evidence-first fork of [phuryn/pm-skills](https://github.com/phuryn/pm-skills) for PM decisions that must survive weak searches, sparse evidence, false premises, noisy data, enterprise constraints, and AI failure modes.**

**86 PM skills and 51 chained workflows across 11 plugins.**

This fork adds four layers to the upstream PM framework foundation:

1. **Reliability**: adversarial scenarios, contradiction passes, uncertainty labels, hard gates, and semantic regression checks.
2. **Enterprise decision quality**: hardened strategy, PRD, pricing, GTM, prioritization, roadmap, stakeholders, risk, research, analytics, and experimentation.
3. **Enterprise transformation**: repeatable workflows for **Building Future Capabilities**, **Client Success → Sales GTM**, **Sales Transformation**, and **Tooling & Automation**.
4. **Business-case reliability**: claim-level evidence, deterministic proof obligations, falsifiable PoCs, reconstructable economics, investment red-teaming, and staged BUILD / BUY / PARTNER / EXPERIMENT / DEFER / KILL / NOT READY decisions.

The target is **100/100 decision usefulness on defined benchmark cases**, not a self-awarded “perfect prompt” claim. The repository includes a behavioral evaluation harness so actual Claude/Codex outputs can be scored against hard failure gates and a 100-point rubric.

## Why this fork exists

A PM skill can produce polished output and still fail where judgment matters.

A real trigger for this fork: competitor analysis ran a weak first search and concluded there were no competitors. Only after the user challenged the answer did the model research harder and find credible players.

The same failure pattern appears elsewhere:

- one client request becomes “market demand”;
- bespoke project code becomes “reusable IP”;
- a target metric becomes a client success claim;
- a successful PoC is mistaken for production readiness;
- technical feasibility is mistaken for commercial validation;
- missing ROI inputs are silently replaced with plausible assumptions;
- one PoC becomes a platform investment thesis;
- a sales win-rate increase hides worse opportunity quality;
- an automation saves generation time but creates more review work;
- a vendor demo substitutes for a representative enterprise pilot;
- a strategy canvas is complete but no strategic choice was actually made.

The reliability flywheel is:

> **Observed failure → adversarial scenario → runtime guard → deterministic proof obligation → semantic regression test → behavioral benchmark**

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
- [`reliability/ENTERPRISE_TRANSFORMATION_SCENARIOS.md`](reliability/ENTERPRISE_TRANSFORMATION_SCENARIOS.md)
- [`reliability/business_case_golden_scenarios.json`](reliability/business_case_golden_scenarios.json)
- [`reliability/scenario_matrix.json`](reliability/scenario_matrix.json)

## Behavioral Evaluation Harness

Structural CI proves a skill is installable. Guard-regression tests prove important instructions still exist. The [`evaluation/`](evaluation/) layer tests captured **model behavior**.

The evaluation flow is:

`frozen adversarial case → first-run model output → deterministic hard gates → 100-point rubric → pass/fail → regression history`

### Current golden cases

The suite contains 14 adversarial cases covering:

- competitor zero-result first pass;
- single-client demand masquerading as market demand;
- bespoke delivery code masquerading as reusable IP;
- target metrics becoming client success claims;
- confidential proof leaking into public GTM;
- win-rate improvement caused by cherry-picking;
- PoC success without a production path;
- automation review burden erasing ROI;
- autonomous side effects without rollback/permissions;
- vendor-demo happy-path bias;
- business-case competitor absence after a weak first pass;
- ROI demanded with missing economic inputs;
- platform investment inferred from one PoC;
- technical validation mistaken for commercial validation.

### 100-point scoring

Each output is graded across:

- evidence integrity: 15
- analysis sufficiency: 10
- uncertainty calibration: 10
- analytical correctness: 10
- decision usefulness: 15
- trade-offs and alternatives: 10
- edge-case handling: 10
- enterprise execution realism: 10
- actionability: 5
- executive clarity: 5

Default pass threshold: **90/100 plus zero hard-gate failures**.

A 100/100 soft score cannot override a catastrophic hard-gate breach.

Run a captured output:

```bash
python evaluation/score_output.py \
  --case BC5_ROI_MISSING_INPUTS \
  --output evaluation/runs/claude/BC5.md
```

Add a human/independent-model judgement file to calculate the weighted 100-point score. See [`evaluation/README.md`](evaluation/README.md).

The critical metric is **first-run success**. Recovery after a user says “you missed something” does not count as a clean pass.

## Reliability-First Business Case Engine

Use `/build-business-case` for a generalized, investment-grade business case.

The core sequence is:

`Signal → Customer → JTBD → Alternatives → Right-to-win → Build/Buy/Partner/Do Nothing → Hypothesis → PoC → Evidence → Economics → GTM → Investment Decision → Reuse → Platform`

`pm-business-case` is deliberately fail-closed:

- unsupported decision-critical claims become `UNKNOWN`, `ASSUMPTION`, `ESTIMATE`, `STALE`, or `PROPOSAL`, not polished facts;
- external facts must be retrieved and inspected before they become verified evidence;
- user-supplied competitors are leads until independently verified;
- negative conclusions require search exhaustion and contradiction checking;
- tool/search failure becomes `coverage incomplete / UNKNOWN`, never evidence of absence;
- material estimates require formulas, inputs, units, and provenance;
- customer, buyer, economic buyer, JTBD, WTP, and current alternatives are separated;
- BUILD is compared with BUY, PARTNER, and current-state/do-nothing;
- PoCs require a credible baseline, falsifiable hypothesis, thresholds, guardrails, and kill criteria;
- technical success is not commercial validation;
- one successful project or PoC is not proof of platform/reusable-IP readiness;
- irreversible investment decisions are blocked while P0 evidence remains unresolved.

The generated claim ledger can be structurally checked with:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

The validator protects proof obligations. It does not claim to be an external truth oracle, and the project does not claim that any LLM can guarantee zero hallucinations on unseen tasks.

### Business-case commands

- `/build-business-case`: end-to-end evidence-led business case
- `/business-case-evidence`: evidence and research mode without forcing a recommendation
- `/business-case-red-team`: strongest rejection case before leadership review
- `/business-case-decision`: investment committee decision gate
- `/business-case-refresh`: refresh stale P0 evidence and re-evaluate readiness

## Enterprise Transformation Operating System

### 1. Building Future Capabilities

Use `/build-future-capability`:

`capability-opportunity-radar → reusable-accelerator-thesis → solution-business-case`

It requires independent demand signals, right-to-win, common-core/reuse evidence, alternatives, reachable economics, sensitivity, pilot gates, and kill criteria. A single client request is not market validation.

The Enterprise Transformation `solution-business-case` skill remains the specialized capability-investment primitive. Use `pm-business-case` when you need the generalized business-case engine and its full evidence ledger, refresh, red-team, and investment-decision workflow.

### 2. Existing Client Success → Sales GTM

Use `/proof-to-gtm`:

`client-proof-extractor → case-study-to-gtm → account-expansion-play`

It separates `MEASURED`, `CLIENT-CONFIRMED`, `DELIVERED`, `OBSERVED`, `TARGET`, `INFERENCE`, and `UNKNOWN` before claims enter sales collateral, while enforcing NDA/publication boundaries and transferability tests.

### 3. Sales Transformation

Use `/transform-sales`:

`sales-funnel-diagnostic → solution-to-sales-playbook → pipeline-conversion-experiment`

It diagnoses before prescribing and tests for fake improvements such as win-rate gains from cherry-picking, faster cycles from smaller deals, poor qualification disguised as proposal failure, and PoC wins that never reach production.

### 4. Tooling & Automation

Use `/automate-pm-workflow`:

`pm-workflow-automation → tool-evaluation-selection → automation-governance`

It covers process redesign, automation suitability, build/buy/tool selection, HITL, permissions, validation, auditability, retries/idempotency, rollback, kill switches, TCO, review burden, and shadow-mode rollout.

## Other hardened decision areas

### Market intelligence

Competitor research uses **Search → Challenge → Expand → Verify → Conclude** and checks category, problem/JTBD, workflow, buyer language, adjacent categories, substitutes, manual/in-house alternatives, geography, and emerging players before negative conclusions.

### Product / strategy / execution

Decision and evidence gates cover product strategy, pricing, PRDs, prioritization, outcome roadmaps, stakeholder decision rights, pre-mortems, new/existing product experiments, and segmentation.

### GTM / measurement / analytics

Enterprise GTM models buyer/champion, technical/security review, procurement, implementation, adoption, expansion, and renewal. Battlecards require evidence and acknowledge where competitors are stronger. North Star selection tests Goodhart/gaming and causal assumptions. A/B analysis includes correct power logic, SRM, optional stopping, multiple comparisons, practical significance, and guardrails.

## Start here

| Goal | Start with |
|---|---|
| Build an investment-grade business case | `/build-business-case` |
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
claude plugin install pm-business-case@pm-skills
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
codex plugin add pm-business-case@pm-skills
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

<details>
<summary><strong>11. pm-business-case</strong> — reliability-first investment cases (6 skills, 5 commands)</summary>

Business-case orchestration, evidence ledgers, market and customer proof, economics, commercialization, falsification, investment red-teaming, evidence refresh, and staged capital decisions.
</details>

## Reliability architecture

Every skill inherits global + plugin-specific adversarial scenario families. Decision-critical files have explicit behavior contracts protected by `tests/test_reliability_contracts.py`. Business-case proof obligations additionally have `tests/test_business_case_contracts.py` and a deterministic evidence-ledger validator. The behavioral suite in `evaluation/` separately scores actual captured model responses.

These tests improve observability and regression control. They do not prove that an LLM will be correct on every unseen PM decision.

## Roadmap

### Shipped
- [x] Baseline audit and PM Skill Quality Standard
- [x] Reliability Contract and adversarial scenario matrix
- [x] Search-exhaustion competitor intelligence
- [x] Quote-verification and A/B correctness guards
- [x] High-value hardening across strategy, PRD, pricing, GTM, prioritization, metrics, roadmap, stakeholders, risk, experiments, and segmentation
- [x] Enterprise Transformation plugin for the four enterprise motions
- [x] Executable golden-case behavioral evaluation harness
- [x] 100-point model-agnostic scoring rubric with hard-gate precedence
- [x] Reliability-first Business Case engine with evidence ledger, deterministic proof validator, 20 adversarial scenarios, and first-run behavioral cases

### Next
- [ ] Capture repeatable Claude/Codex first-run benchmark outputs for all golden cases
- [ ] Report hard-gate failure rate, mean/range score, and recurring failures by model/version
- [ ] Add mutated cases to reduce overfitting to literal benchmark prompts
- [ ] Add Enterprise AI product-decision plugin: use-case selection, eval contracts, RAG, agents, HITL, model/provider selection, cost/latency/quality, rollout, observability
- [ ] Track reliability scores release by release

## Contribution philosophy

**Upstream-worthy:** generic correctness/reliability improvements that benefit the original marketplace should be proposed back to [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) when appropriate.

**Fork differentiation:** enterprise transformation, Enterprise AI PM, semantic/behavioral evaluation, evidence contracts, business-case reliability, and executive decision workflows can evolve independently here.

## Attribution

This repository is a fork of **[Paweł Huryn's PM Skills Marketplace](https://github.com/phuryn/pm-skills)** and preserves the original MIT license and attribution.

The fork-specific work is the reliability/evaluation layer, hardened decision behaviors, enterprise transformation extensions, business-case reliability engine, and behavioral benchmark infrastructure. Upstream work is not relabeled as original work.

## License

MIT. See [`LICENSE`](LICENSE).
