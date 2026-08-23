# CLAUDE.md

Guidance for AI agents (Claude Code, Cowork, Codex, and others) working in this repository. This file is the single source of truth for how the fork is structured and maintained.

## Project Overview

**PM Skills: Reliability-First Enterprise AI Edition** (`sandeep9889123/pm-skills`) is a fork of `phuryn/pm-skills` with **10 independent plugins, 80 skills, and 46 commands/workflows**.

The upstream marketplace supplies the core PM framework foundation. This fork adds reliability contracts, adversarial scenarios, semantic behavior guards, hardened decision-critical skills, and enterprise transformation / Enterprise AI PM extensions.

Upstream creator/maintainer: Paweł Huryn — https://github.com/phuryn/pm-skills

Fork maintainer: Sandeep Kumar M — https://github.com/sandeep9889123

Preserve upstream MIT attribution. Do not relabel upstream skills as fork-original work.

## Fork Reliability Principle

For decision-critical behavior use:

`Observed failure → adversarial scenario → runtime guard → semantic regression test`

High-consequence skills should distinguish `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `STALE` where applicable, seek disconfirming evidence, avoid false precision, define decision gates, and state what would change the recommendation.

See `docs/standards/`, `reliability/scenario_matrix.json`, and `tests/test_reliability_contracts.py`.

## Repo Structure

```
pm-skills/                           <- repo root
├── .claude-plugin/marketplace.json  <- root marketplace manifest (lists all 10 plugins)
├── .docs/images/                    <- images used by README
├── .github/workflows/               <- CI: tests.yml, tag-on-merge.yml
├── CHANGELOG.md                     <- release source of truth
├── CLAUDE.md                        <- this file
├── AGENTS.md                        <- pointer to CLAUDE.md
├── CONTRIBUTING.md
├── README.md
├── LICENSE
├── validate_plugins.py
├── reliability/                     <- scenario catalogs + machine-readable contracts
├── docs/standards/                  <- PM skill quality and reliability standards
├── docs/audit/                      <- baseline audit and backlog
├── tests/                           <- structural + semantic-regression tests
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

## What's Visible Where

| Location | Visible in | Notes |
|----------|-----------|-------|
| `marketplace.json` → `description` | marketplace browser / CLI | One-line marketplace positioning |
| `plugin.json` → `description` | plugin list / CLI | Per-plugin summary |
| `SKILL.md` frontmatter → `description` | skill auto-loading | Include clear trigger phrases |
| command frontmatter | command discovery | Short/actionable |
| root `README.md` | GitHub | Public documentation |
| `CLAUDE.md` | repo agents | Maintenance source of truth |

## Versioning & Releases

- `CHANGELOG.md` is the source of truth. The newest `## vX.Y.Z — YYYY-MM-DD` heading is the released version; `## Unreleased` may contain pending fork changes.
- Keep every released version in sync across `marketplace.json`, all **10** `plugin.json` files, and the latest released changelog heading. There is no independent per-plugin versioning in the current repo tests.
- Every user-facing change gets a changelog bullet under `## Unreleased`.
- Semver: breaking = major; new skills/commands or changed behavior = minor; fixes/docs = patch.

## Reliability and Scenario Maintenance

### When a real-world failure is reported

1. Reproduce/understand the failure mode.
2. Decide whether it is global, plugin-specific, or skill-specific.
3. Add/update an adversarial scenario.
4. Add a runtime behavior guard in the affected skill/workflow when material.
5. Add/update a semantic regression contract for decision-critical guards.
6. Check adjacent skills for the same failure pattern.
7. Document the user-facing change in `CHANGELOG.md`.

### Negative conclusions

Claims such as “no competitors,” “no demand,” “no risk,” “no effect,” or “automation is not viable” require evidence that the search/analysis scope was sufficient. Tool failure or first-pass zero results must not become real-world absence.

### Enterprise/client claims

Do not convert targets, inferred outcomes, team-wide results, or confidential client data into publishable success claims. Preserve evidence classification and attribution limits.

### Automation

Any workflow causing external side effects should define permissions, validation, HITL policy, auditability, retries/idempotency, rollback/compensating action, monitoring, ownership, and a kill switch proportional to risk.

## Article Links in Upstream Skills

- Existing mapped upstream skills may include `### Further Reading` links.
- Preserve neutral tone and original attribution.
- Do not add promotional claims or imply endorsement by upstream authors of fork-specific work.

## Operational Procedures

### After any skill/command change
1. Run `python3 validate_plugins.py` and `python3 -m unittest discover -s tests -v` where execution is available.
2. If skills/commands were added or removed, update root README headline/per-plugin counts and plugin README section counts.
3. If totals changed, update `marketplace.json` description.
4. Add/update plugin entry in marketplace when plugin set changes.
5. Update `reliability/scenario_matrix.json` for new plugins or new high-risk contracts.
6. Add a `CHANGELOG.md` bullet under `## Unreleased`.
7. Check this `CLAUDE.md` for stale counts/structure.

### After a description change
- Check public README/marketplace copy if the change affects positioning.
- Keep skill descriptions concise enough for auto-loading.

## Validation

`validate_plugins.py` checks manifest/frontmatter/name/README/command structure.

`tests/test_consistency.py` checks marketplace-vs-disk plugin list, versions, README counts, changelog format, and plugin command references.

`tests/test_reliability_contracts.py` checks global/plugin scenario coverage and protects decision-critical runtime guard phrases from silent regression.

```bash
python3 validate_plugins.py
python3 -m unittest discover -s tests -v
```

These semantic tests are guard-regression tests, not yet a complete end-to-end LLM quality benchmark. Do not claim they prove 100% output accuracy.

## What to Suggest After Completing Work

Prioritize evidence and validation over repo churn:
- after a behavioral change, identify the failure scenario it prevents;
- after adding a high-risk skill, add semantic contracts;
- after adding a plugin, update marketplace/counts/scenarios/agent guidance;
- before release, run structural + semantic tests and inspect the diff;
- propose upstream PRs only for generic fixes that cleanly benefit `phuryn/pm-skills`.
