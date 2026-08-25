# CLAUDE.md

Guidance for AI agents, including Claude Code, Cowork, Codex, and other capable models working in this repository. This file is the single source of truth for how the fork is structured and maintained.

## Project Overview

**PM Skills: Reliability-First Enterprise AI Edition** (`sandeep9889123/pm-skills`) is a fork of `phuryn/pm-skills` with **12 independent plugins, 96 skills, and 55 commands/workflows**.

The upstream project supplies the core PM framework foundation. This fork adds reliability contracts, adversarial scenarios, semantic behavior guards, enterprise transformation, reliability-first business-case automation, model-agnostic prospect discovery, behavioral evaluation, and cross-LLM packaging for Claude, Codex, ChatGPT Skills, and Agent Skills compatible runtimes.

Upstream creator/maintainer: Paweł Huryn, https://github.com/phuryn/pm-skills

Fork maintainer: Sandeep Kumar M, https://github.com/sandeep9889123

Preserve upstream MIT attribution. Do not relabel upstream skills as fork-original work.

## Model-Agnostic Principle

Core skills should remain portable Markdown. Provider-specific packaging or command wrappers may improve ergonomics, but correct reasoning must not depend on one provider's proprietary tool names.

When a model cannot browse, read files, execute code, or use another expected tool:

- do not simulate the missing tool
- do not fabricate the missing evidence
- mark the affected area `coverage incomplete / UNKNOWN`
- continue with the strongest safe partial workflow

For portable workflows, prefer a provider-neutral master prompt or `SKILL.md` contract plus optional provider adapters.

The underlying `skills/` folders are the capability source. `.claude-plugin/`, `.agents/plugins/`, and `.codex-plugin/` are packaging/distribution layers and must not fork the substantive PM logic.

## Fork Reliability Principle

For decision-critical behavior use:

`Observed failure -> adversarial scenario -> runtime guard -> deterministic proof obligation -> semantic regression test -> behavioral benchmark`

High-consequence skills should distinguish `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE` where applicable, seek disconfirming evidence, avoid false precision, define decision gates, and state what would change the recommendation.

For business cases, `PROPOSAL` and `DECISION_THRESHOLD` are additional explicit states. Unsupported decision-critical content must not be promoted to verified evidence merely because an executive-ready artifact is requested.

## Repo Structure

```text
pm-skills/
├── .claude-plugin/marketplace.json   <- Claude marketplace
├── .agents/plugins/marketplace.json  <- Codex marketplace
├── .github/workflows/
├── CHANGELOG.md
├── CLAUDE.md
├── AGENTS.md
├── README.md
├── LICENSE
├── validate_plugins.py
├── reliability/                     <- scenario catalogs + behavior contracts
├── evaluation/                      <- golden cases + captured-output scorer
├── docs/                            <- LLM usage guidance + quality/reliability standards
├── tests/                           <- structural + semantic + eval-harness tests
└── pm-{name}/                       <- 12 plugin directories
    ├── .claude-plugin/plugin.json   <- Claude plugin metadata
    ├── .codex-plugin/plugin.json    <- Codex plugin metadata; exposes ./skills/
    ├── skills/{skill}/SKILL.md      <- portable capability source
    ├── commands/{command}.md        <- Claude-oriented workflow wrappers
    ├── README.md                    <- self-contained user onboarding
    └── optional prompts/references/templates/evaluation assets
```

User-facing installation guidance lives in `README.md` and `docs/USING_WITH_LLMS.md`. The complete inventory lives in `docs/PLUGIN_CATALOG.md`.

### The 12 plugins

| Plugin | Focus |
|---|---|
| `pm-product-discovery` | Ideation, experiments, assumptions, prioritization, interviews |
| `pm-prospect-discovery` | Model-agnostic enterprise pre-RFP discovery, hypothesis falsification, adaptive questions, synthesis, and readiness |
| `pm-product-strategy` | Vision, strategy, pricing, business models, competitive/macro frameworks |
| `pm-execution` | Decision-first PRDs, OKRs, roadmaps, sprints, risk, stakeholders, stories, red-teaming |
| `pm-market-research` | Reliability-first competitors, sizing, personas, segmentation, journeys, feedback |
| `pm-data-analytics` | SQL, cohorts, statistically sound experiment analysis |
| `pm-go-to-market` | Enterprise GTM, beachheads, ICPs, motions, growth loops, battlecards |
| `pm-marketing-growth` | Positioning, value props, North Star, naming, marketing ideas |
| `pm-toolkit` | Resume, NDA, privacy, proofreading utilities |
| `pm-ai-shipping` | AI-built app reviewability, intended-vs-implemented, tests, security/performance |
| `pm-enterprise-transformation` | Future capabilities, client proof to GTM, sales transformation, tooling/automation |
| `pm-business-case` | Evidence-led business cases, proof gates, economics, falsification, investment decisions |

## Key Design Rules

- **Skills = nouns/concepts.** Frameworks and analytical knowledge loaded when topic matches.
- **Commands = verbs.** User-triggered workflows chaining one or more skills.
- **No cross-plugin hard references in commands.** Plugins install independently. Suggest cross-plugin follow-ups in natural language only.
- Intra-plugin skill references are fine.
- Commands use a single `$ARGUMENTS` placeholder where needed; skills read context from the conversation.
- **Frontmatter required:** skills need `name` + `description`; commands need `description` + `argument-hint`.
- A skill's `name` must match its directory name.
- Keep frontmatter lean; put detailed behavior in the body.
- Every plugin must preserve both provider manifests: `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`.
- Codex manifests must expose the existing `skills/` folder, not duplicate it elsewhere.
- Every plugin README must document Claude, Codex, ChatGPT, and generic/Agent Skills usage.
- Claude slash commands must not be described as universally available. Provide a plain-language equivalent for other runtimes.
- High-risk behavior guards referenced by `reliability/scenario_matrix.json` must not be removed without updating the scenario/test intentionally.
- Do not weaken a hard gate just to make an output more optimistic or concise.
- A deterministic validator is a proof-obligation check, not a truth oracle. Do not claim it verifies external reality.

## Prospect Discovery Reliability

`pm-prospect-discovery` is the generalized pre-RFP discovery engine for opportunities where a prospect signal and early solution/use-case hypothesis exist before formal requirements or RFP commitment.

The default sequence is:

`Signal -> Decision framing -> Prospect evidence -> Problem hypothesis -> Alternative root causes -> Use-case options -> Red-team -> Journey -> Solution anchors -> Assumptions -> Adaptive questions -> Session -> Synthesis -> Readiness -> Proposal handoff`

Mandatory rules:

- The user's or Sales team's preferred use case is a hypothesis, not a validated requirement.
- Never invent prospect systems, APIs, data quality, volumes, budgets, stakeholder authority, buying intent, or operational workflow details.
- Tool/search failure means `coverage incomplete / UNKNOWN`.
- Discovery must include disconfirming questions and credible alternative root causes or solution paths.
- A questionnaire is not successful merely because it is comprehensive. Mandatory questions should change a material decision.
- Use branching logic so unknown API, data, regulation, volume, or human-judgment conditions change the deeper questions.
- Preserve `UNKNOWN` when the relevant attendee does not know the answer. Capture owner/follow-up rather than guessing.
- Do not estimate delivery or commit architecture while unresolved P0 items can materially change scope, effort, security, economics, ownership, or timeline.
- Separate readiness for solutioning, architecture, estimation, business case, and proposal.
- A high discovery-confidence score cannot override a hard blocker.
- `WRONG USE CASE`, `REFRAME USE CASE`, `SECOND DISCOVERY REQUIRED`, and `STOP / NO-GO` are valid outcomes.

The model-agnostic entry point is:

```text
pm-prospect-discovery/prompts/prospect-discovery-master.md
```

## Business Case Reliability

`pm-business-case` is the generalized fail-closed business-case engine. `pm-enterprise-transformation/solution-business-case` remains the specialized future-capability business-case primitive inside the Enterprise Transformation operating system.

Business-case decisions must follow evidence before narrative. The default sequence is:

`Signal -> Customer -> JTBD -> Alternatives -> Right-to-win -> Build/Buy/Partner/Do Nothing -> Hypothesis -> PoC -> Evidence -> Economics -> GTM -> Investment Decision -> Reuse -> Platform`

Mandatory rules:

- Never fabricate citations, competitors, customer quotes, market sizes, pricing, benchmarks, financial inputs, dates, or source details.
- User-supplied competitors and external claims are leads until verified, unless an authoritative internal source-of-truth artifact is explicitly supplied.
- A zero-result first search must trigger search expansion and contradiction checking, never an empty-market conclusion.
- Tool/search failure means `coverage incomplete / UNKNOWN` for affected claims.
- Decision-critical FACT claims require one directly authoritative primary source or two independent credible sources.
- Material ESTIMATE claims require method/formula, explicit inputs, units, and source claim IDs where available.
- BUILD must be compared with BUY, PARTNER, and DO NOTHING/current-state alternatives.
- A PoC must be falsifiable and state what it cannot prove.
- Technical validation is not commercial validation.
- One client or one PoC is not sufficient evidence of platform/reusable-accelerator readiness.
- BUILD, BUY, or PARTNER is blocked while P0 evidence remains UNKNOWN, STALE, unverified, or materially contradicted.
- `NOT READY` and `EXPERIMENT` are valid outcomes and are preferable to manufactured certainty.

When a business-case run writes an evidence ledger, execute when available:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

Do not weaken the validator or relabel claims merely to force a pass.

## Versioning and Releases

- `CHANGELOG.md` is the source of truth. The newest `## vX.Y.Z` dated heading is the released version; `## Unreleased` may contain pending changes.
- Keep every released version in sync across `.claude-plugin/marketplace.json`, every `.claude-plugin/plugin.json`, every `.codex-plugin/plugin.json`, and the latest released changelog heading.
- `.agents/plugins/marketplace.json` must list exactly the same plugin directories as the Claude marketplace and disk.
- Every user-facing change gets a changelog bullet under `## Unreleased`.
- Semver: breaking = major; new skills/commands or changed behavior = minor; fixes/docs = patch.

## Reliability and Scenario Maintenance

### When a real-world failure is reported

1. Reproduce/understand the failure mode.
2. Decide whether it is global, plugin-specific, or skill-specific.
3. Add/update an adversarial scenario.
4. Add a runtime behavior guard when material.
5. Add/update a semantic regression contract for decision-critical guards.
6. Add or mutate a behavioral golden case when the failure should be observable in model output.
7. Check adjacent skills for the same failure pattern.
8. Document the user-facing change in `CHANGELOG.md`.

### Negative conclusions

Claims such as "no competitors", "no demand", "no risk", "no effect", or "automation is not viable" require evidence that the search/analysis scope was sufficient. Tool failure or first-pass zero results must not become real-world absence.

### Enterprise/client claims

Do not convert targets, inferred outcomes, team-wide results, or confidential client data into publishable success claims. Preserve evidence classification and attribution limits.

### Automation

Any workflow causing external side effects should define permissions, validation, HITL policy, auditability, retries/idempotency, rollback/compensating action, monitoring, ownership, and a kill switch proportional to risk.

## Behavioral Evaluation

`evaluation/cases.json` is the frozen adversarial benchmark suite. `evaluation/score_output.py` scores captured model outputs.

### Evaluation rules

- Keep case prompts/context frozen during a benchmark run.
- Evaluate first-run outputs. Do not coach the model before scoring.
- Deterministic hard gates are deliberately narrow and catastrophic. Do not use regex to pretend to judge nuanced PM reasoning.
- Nuanced quality uses the 100-point rubric with a human or independent evaluator model, scoring every dimension 0-5 with rationale.
- Default pass is 90/100 and zero hard-gate failures.
- A 100/100 rubric score must never override a hard-gate failure.
- Blind evaluator identity to model name where practical.
- For stochastic comparisons, prefer multiple fresh runs and report mean, range, and hard-gate failure rate.
- Do not tune a skill only to literal benchmark wording. Add mutated cases to test the underlying failure family.
- Do not claim "100/100 PM skills" unless the exact benchmark scope, model/version, runs, scoring method, and results support that claim.

## Operational Procedures

### After any skill/command/packaging change

1. Run `python3 validate_plugins.py` and `python3 -m unittest discover -s tests -v` where execution is available.
2. If skills/commands were added or removed, update root README totals and relevant plugin README counts.
3. If totals changed, update `.claude-plugin/marketplace.json` description.
4. If the plugin set changes, update both `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`.
5. For every plugin addition or released version change, keep `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` aligned.
6. Update `reliability/scenario_matrix.json` for new plugins or high-risk contracts.
7. Add or update behavioral/adversarial cases when the new failure family is decision-critical.
8. Add a `CHANGELOG.md` bullet under `## Unreleased`.
9. Check all plugin READMEs and `docs/USING_WITH_LLMS.md` if installation or invocation changes.
10. Check this file for stale counts or structure.

## Validation

`validate_plugins.py` checks Claude manifest/frontmatter/name/README/command structure.

`tests/test_consistency.py` checks Claude/Codex marketplace parity, provider manifest versions, README totals, multi-LLM onboarding, changelog format, and command references.

`tests/test_reliability_contracts.py` checks scenario coverage and protects decision-critical guard phrases.

`tests/test_business_case_contracts.py` protects business-case proof obligations.

`tests/test_prospect_discovery_contracts.py` protects model-agnostic prospect-discovery portability, anti-confirmation behavior, question discipline, and readiness hard gates.

`tests/test_behavioral_eval_harness.py` validates benchmark schema, scoring rules, and hard-gate precedence.

```bash
python3 validate_plugins.py
python3 -m unittest discover -s tests -v
```

The behavioral harness makes quality measurable on defined cases. It does not prove universal correctness on unseen PM decisions.

## Upstream / Fork Boundary

- Generic correctness/reliability fixes that cleanly benefit upstream can be proposed to `phuryn/pm-skills`.
- Enterprise transformation, Enterprise AI PM, opinionated evidence contracts, business-case reliability, prospect-discovery reliability, behavioral evaluation, and cross-LLM packaging can evolve independently in this fork.
- Preserve neutral attribution and never imply upstream endorsement of fork-specific behavior.
