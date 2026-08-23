# Changelog

## Unreleased

### Enterprise Transformation Wave 2

- Added **`pm-enterprise-transformation`** with 12 skills and 4 workflows for four recurring leadership motions: Building Future Capabilities, Client Success → Sales GTM, Sales Transformation, and Tooling & Automation.
- Added `/build-future-capability`: recurring-demand evidence → right-to-win → reuse classification → business case → pilot/kill decision.
- Added `/proof-to-gtm`: verified delivery proof → NDA-safe claims → transferable case study → ICP/discovery/proof → GTM asset and measurement plan.
- Added `/transform-sales`: funnel/cohort diagnosis → solution-selling playbook → controlled conversion experiments with quality/economic guardrails.
- Added `/automate-pm-workflow`: current-state workflow → automation suitability → build/buy/tool selection → HITL/governance → shadow/pilot rollout.
- Added decision skills for capability opportunity radar, reusable accelerator thesis, investment business cases, client-proof extraction, case-study-to-GTM, account expansion, sales funnel diagnosis, solution-to-sales playbooks, pipeline experiments, PM workflow automation, tool selection, and automation governance.
- Hardened 13 high-value existing primitives: `product-strategy`, `pricing-strategy`, `create-prd`, `gtm-strategy`, `competitive-battlecard`, `prioritize-features`, `north-star-metric`, `outcome-roadmap`, `stakeholder-map`, `pre-mortem`, both experiment-design skills, and `user-segmentation`.
- Expanded semantic behavior contracts and adversarial scenarios to cover one-client-demand bias, fake reusable IP, unsupported client success claims, sales-quality degradation, pilot-to-production failure, sales-to-delivery promise drift, automation ROI/review burden, uncontrolled side effects, and vendor-demo happy-path bias.
- Refreshed the root README and marketplace to the new 80-skill / 46-workflow / 10-plugin enterprise decision system.

### Reliability-first fork

- Reframed the fork around **evidence integrity, adversarial reliability, Enterprise AI PM, and semantic decision quality** while preserving explicit attribution to the upstream `phuryn/pm-skills` project.
- Added a repo-wide **Reliability Contract V1** covering evidence states, first-pass skepticism, negative-conclusion gates, user false-premise handling, contradiction passes, search exhaustion, quantitative integrity, tool failure, and hard-failure conditions.
- Added an **Adversarial Scenario Catalog** plus machine-readable scenario matrix. Every skill inherits global scenarios; every plugin adds domain-specific failure cases.
- Added semantic regression tests so critical PM behavior guards cannot disappear silently during future edits or upstream syncs.
- Hardened `competitor-analysis` and `/competitive-analysis` against the observed failure where a weak first search produces “no competitors” until the user challenges the answer. The workflow now searches category/problem/workflow/buyer/technology/substitute/regional/emerging framings, verifies user-supplied competitors independently, and runs a contradiction pass before negative conclusions.
- Hardened `market-sizing` against false precision, incompatible top-down/bottom-up estimates, arbitrary SOM percentages, stale evidence, and hidden assumptions.
- Hardened `user-personas` against forced persona counts, invented demographics, unsupported “research-backed” claims, and unverified quotes.
- Hardened `summarize-interview` with verbatim-quote verification, observation-vs-inference separation, contradiction preservation, and small-N research safeguards.
- Corrected `ab-test-analysis` power guidance so a target such as 80% power requires the beta / `z_(1-beta)` term; added SRM, optional-stopping, multiple-comparison, practical-significance, guardrail, and invalid-test decision logic.

## v2.1.0 — 2026-07-03

### pm-ai-shipping

- `/security-audit-static` findings now carry a mandatory **Evidence** line (`file:line` + verbatim snippet), and every citation is re-verified against the file before the final report ships.
- Subagent fan-out has a concrete trigger (scope over ~30 files / ~5,000 lines) and a structured candidate-record contract, so parallel audit slices merge cleanly into one self-refute pass.
- `/performance-audit-static` now hunts **N+1 queries and request waterfalls** — the most common perf failure in AI-generated code — alongside over-fetching, indexes, and caching, and gained a refute-before-reporting pass (dynamic field access, existing indexes, hot-path evidence).
- Both audit commands pre-approve a read-only toolset (`allowed-tools`): read, search, fan out, and write under `reports/` — never edit the code under audit.
- The audited repo is treated as untrusted input across the kit: instructions embedded in code, comments, or docs are data to analyze — a steering attempt is itself a finding — never directives to follow.
- `/ship-check` runs the security and performance audits as parallel subagents once the docs exist.
- Security reports gained severity anchors (what Critical/High/Medium/Low mean) and a consolidation rule (more than ~12 findings → lead with the worst, group the tail by root cause).
- Docs and reports now use repo-relative paths (`documentation/`, `reports/`) — the old absolute forms (`/documentation`) could resolve to the filesystem root — and reports are always written, with the path announced, instead of "optionally".

### Repo

- Added this `CHANGELOG.md` as the release source of truth with auto-tag-and-release on merge (adapted from [claude-usage](https://github.com/phuryn/claude-usage)): pushing a new `## vX.Y.Z` heading to `main` tags that version and publishes a GitHub Release with the section as notes — gated on the test suite and a version-sync check.
- Added a test suite (`tests/`) and a Tests workflow (every PR and push to `main`): plugin-spec validation plus docs consistency — README skill/command counts vs. disk, marketplace plugin list vs. directories, version sync across all manifests, CHANGELOG format.
- CONTRIBUTING now documents the changelog convention (every user-facing change gets a bullet; contributors credited inline) and the release procedure.
- Docs since v2.0.0: native Codex CLI install path; companion badges (burnstop, claude-usage).

## v2.0.0 — 2026-06-05

- Added the **pm-ai-shipping** plugin (AI Shipping Kit): `/ship-check`, `/document-app`, `/derive-tests`, `/security-audit-static`, `/performance-audit-static`, plus the `shipping-artifacts` and `intended-vs-implemented` skills.
- Added the `strategy-red-team` skill and `/red-team-prd` command to pm-execution.
- Refreshed the root README; added `CLAUDE.md` / `AGENTS.md` agent guidance.
