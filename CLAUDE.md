# CLAUDE.md

Guidance for AI agents (Claude Code, Cowork, Codex, and others) working in this repository. This file is the single source of truth for how the fork is structured and maintained.

## Project Overview

**PM Skills: Reliability-First Enterprise AI Edition** (`sandeep9889123/pm-skills`) is a fork of `phuryn/pm-skills` with **10 independent plugins, 80 skills, and 46 commands/workflows**.

The upstream marketplace supplies the core PM framework foundation. This fork adds reliability contracts, adversarial scenarios, semantic behavior guards, hardened decision-critical skills, enterprise transformation, and model-agnostic behavioral evaluation.

Upstream creator/maintainer: Paweł Huryn — https://github.com/phuryn/pm-skills

Fork maintainer: Sandeep Kumar M — https://github.com/sandeep9889123

Preserve upstream MIT attribution. Do not relabel upstream skills as fork-original work.

## Fork Reliability Principle

For decision-critical behavior use:

`Observed failure → adversarial scenario → runtime guard → semantic regression test → behavioral benchmark`

High-consequence skills should distinguish `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE` where applicable, seek disconfirming evidence, avoid false precision, define decision gates, and state what would change the recommendation.

## Repo Structure

```
pm-skills/
├── .claude-plugin/marketplace.json
├── .github/workflows/
├── CHANGELOG.md
├── CLAUDE.md
├── README.md
├── LICENSE
├── validate_plugins.py
├── reliability/                     <- scenario catalogs + behavior contracts
├── evaluation/                      <- golden cases + captured-output scorer
│   ├── README.md
│   ├── cases.json
│   └── score_output.py
├── docs/standards/                  <- PM skill quality/reliability standards
├── docs/audit/                      <- audit and backlog
├── tests/                           <- structural + semantic + eval-harness tests
└── pm-{name}/                       <- 10 plugin directories
    ├── .claude-plugin/plugin.json
    ├── skills/{skill}/SKILL.md
    ├── commands/{command}.md
    └── README.md
```

### The 10 plugins

| Plugin | Focus |
|--------|-------|
| `pm-product-discovery` | Ideation, experiments, assumptions, prioritization, interviews |
| `pm-product-strategy` | Vision, strategy, pricing, business models, competitive/macro frameworks |
| `pm-execution` | Decision-first PRDs, OKRs, roadmaps, sprints, risk, stakeholders, stories, red-teaming |
| `pm-market-research` | Reliability-first competitors, sizing, personas, segmentation, journeys, feedback |
| `pm-data-analytics` | SQL, cohorts, statistically sound experiment analysis |
| `pm-go-to-market` | Enterprise GTM, beachheads, ICPs, motions, growth loops, battlecards |
| `pm-marketing-growth` | Positioning, value props, North Star, naming, marketing ideas |
| `pm-toolkit` | Resume, NDA, privacy, proofreading utilities |
| `pm-ai-shipping` | AI-built app reviewability, intended-vs-implemented, tests, security/performance |
| `pm-enterprise-transformation` | Future capabilities, client proof→GTM, sales transformation, tooling/automation |

## Key Design Rules

- **Skills = nouns/concepts.** Frameworks and analytical knowledge loaded when topic matches.
- **Commands = verbs.** User-triggered workflows chaining one or more skills.
- **No cross-plugin hard references in commands.** Plugins install independently. Suggest cross-plugin follow-ups in natural language only.
- Intra-plugin skill references are fine.
- Commands use a single `$ARGUMENTS` placeholder where needed; skills read context from the conversation.
- **Frontmatter required:** skills need `name` + `description`; commands need `description` + `argument-hint`.
- A skill's `name` must match its directory name.
- Keep frontmatter lean; put detailed behavior in the body.
- High-risk behavior guards referenced by `reliability/scenario_matrix.json` must not be removed without updating the scenario/test intentionally.
- Do not weaken a hard gate just to make an output more optimistic or concise.

## Versioning & Releases

- `CHANGELOG.md` is the source of truth. The newest `## vX.Y.Z — YYYY-MM-DD` heading is the released version; `## Unreleased` may contain pending fork changes.
- Keep every released version in sync across `marketplace.json`, all **10** `plugin.json` files, and the latest released changelog heading.
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

Claims such as “no competitors,” “no demand,” “no risk,” “no effect,” or “automation is not viable” require evidence that the search/analysis scope was sufficient. Tool failure or first-pass zero results must not become real-world absence.

### Enterprise/client claims

Do not convert targets, inferred outcomes, team-wide results, or confidential client data into publishable success claims. Preserve evidence classification and attribution limits.

### Automation

Any workflow causing external side effects should define permissions, validation, HITL policy, auditability, retries/idempotency, rollback/compensating action, monitoring, ownership, and a kill switch proportional to risk.

## Behavioral Evaluation

`evaluation/cases.json` is the frozen adversarial benchmark suite. `evaluation/score_output.py` scores captured model outputs.

### Evaluation rules

- Keep case prompts/context frozen during a benchmark run.
- Evaluate **first-run** outputs. Do not coach the model with “you missed something” before scoring.
- Deterministic hard gates are deliberately narrow and catastrophic. Do not use regex to pretend to judge nuanced PM reasoning.
- Nuanced quality uses the 100-point rubric with a human or independent evaluator model, scoring every dimension 0–5 with rationale.
- Default pass is 90/100 **and zero hard-gate failures**.
- A 100/100 rubric score must never override a hard-gate failure.
- Blind evaluator identity to model name where practical.
- For stochastic comparisons, prefer multiple fresh runs and report mean, range, and hard-gate failure rate.
- Do not tune a skill only to literal benchmark wording. Add mutated cases to test the underlying failure family.
- Do not claim “100/100 PM skills” unless the exact benchmark scope, model/version, runs, scoring method, and results support that claim.

### Adding a golden case

A case should include:
- unique id
- workflow/skill
- failure family
- frozen prompt
- context the model should reason from
- expected behaviors
- narrow required/forbidden hard-gate patterns

Every new case must keep the shared rubric weights totaling 100 and should be covered by `tests/test_behavioral_eval_harness.py`.

## Operational Procedures

### After any skill/command change
1. Run `python3 validate_plugins.py` and `python3 -m unittest discover -s tests -v` where execution is available.
2. If skills/commands were added or removed, update root README headline/per-plugin counts and plugin README section counts.
3. If totals changed, update `marketplace.json` description.
4. Add/update plugin entry in marketplace when plugin set changes.
5. Update `reliability/scenario_matrix.json` for new plugins or new high-risk contracts.
6. Consider whether a behavioral golden case should be added/updated.
7. Add a `CHANGELOG.md` bullet under `## Unreleased`.
8. Check this `CLAUDE.md` for stale counts/structure.

## Validation

`validate_plugins.py` checks manifest/frontmatter/name/README/command structure.

`tests/test_consistency.py` checks marketplace-vs-disk plugin list, versions, README counts, changelog format, and plugin command references.

`tests/test_reliability_contracts.py` checks scenario coverage and protects decision-critical runtime guard phrases from silent regression.

`tests/test_behavioral_eval_harness.py` validates benchmark schema, 100-point weights, enterprise workflow coverage, known-bad hard-gate failures, and hard-gate precedence over a 100/100 soft score.

```bash
python3 validate_plugins.py
python3 -m unittest discover -s tests -v
```

The behavioral harness makes quality measurable on defined cases. It still does not prove universal correctness on unseen PM decisions.

## Upstream / Fork Boundary

- Generic correctness/reliability fixes that cleanly benefit upstream can be proposed to `phuryn/pm-skills`.
- Enterprise transformation, Enterprise AI PM, opinionated evidence contracts, and behavioral evaluation can evolve independently in this fork.
- Preserve neutral attribution and never imply upstream endorsement of fork-specific behavior.
