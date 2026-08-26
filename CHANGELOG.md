# Changelog

## Unreleased

### Operational Truth and Shipping Readiness Wave 5C

- Hardened `strategy-red-team` and `/red-team-prd` so evidence gaps are not treated as negative evidence, supported claims can survive the attack, `PASS` is legitimate, and red-teams cannot manufacture a fixed quota of objections.
- Hardened meeting summarization so discussion, proposals, decisions, actions, blockers, owners, dates, quotes, dissent, and source coverage remain distinct; missing owners/dates stay `UNKNOWN` rather than being inferred.
- Rebuilt test-scenario generation around requirement traceability and explicit test oracles. Missing behavior now becomes `SPEC GAP` / `BLOCKED BY SPEC GAP` instead of invented counts, thresholds, permissions, timeouts, or expected results.
- Hardened account expansion so relationship optimism, executive access, or one successful PoC cannot become buying proof; unresolved delivery/trust issues trigger `STABILIZE FIRST`, and concentration/capacity risk remains explicit.
- Added fail-closed coverage states to static security/performance audits and `/ship-check`. Partial or failed inspection cannot become a clean readiness claim; zero static findings are scoped to inspected code and never mean secure, scalable, or guaranteed safe.
- Added 16 Wave 5C adversarial scenarios plus semantic regression tests covering red-team theatre, decision/owner/date inflation, test-oracle invention, premature account expansion, partial-audit synthesis, zero-findings overclaiming, and proposed-tests-as-verified coverage.

### Reliability Kernel and P0 Hardening Waves 4-5B

- Added a repo-wide Reliability Kernel with decision-context resolution, evidence/source precedence, claim-state preservation, freshness, contradiction checks, negative-conclusion burden of proof, fail-closed tool/retrieval behavior, forced-completion guards, decision gates, cross-skill lineage, and P0/P1/P2 admission rules.
- Classified all 96 skills and 55 workflows by reliability risk and added CI coverage that fails when future artifacts are unclassified or core kernel/schema obligations regress.
- Added portable context-frame and claim-lineage schemas so downstream workflows can preserve `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`, `TARGET`, `PROPOSAL`, and `DECISION_THRESHOLD` states instead of silently promoting uncertainty.
- Wave 5A hardened segmentation, sentiment, cohorts, SQL, interviews, metrics, and six workflow wrappers against forced segmentation, invented NPS/sentiment, right-censoring errors, causal overclaiming, schema invention, demand/WTP inflation, and fabricated targets/alerts; added 12 adversarial scenarios and semantic regression tests.
- Wave 5B hardened business-model, monetization, Five Forces, ICP, beachhead, GTM-motion, pricing, strategy, battlecard, growth, launch, business-model orchestration, and market-scan behavior against generic unit-economics rules, forced framework completion, false cross-framework corroboration, invented WTP/market size/channel ROI, survivorship-biased ICPs, arbitrary beachhead-share rules, competitor weakness fabrication, and deadline-driven launch-readiness theatre.
- Added 16 Wave 5B adversarial scenarios and semantic regression tests covering all 13 hardened strategy/GTM runtime artifacts. `UNKNOWN`, `TEST`, `HOLD`, `REFRAME`, `FIX P0 BLOCKERS`, and `NO-GO` remain valid outcomes when evidence does not support a stronger decision.

### Cross-LLM onboarding and repository cleanup

- Reworked the root README into a user-first installation and usage guide for Claude Cowork/Desktop, Claude Code, Codex, ChatGPT, Agent Skills compatible tools, and generic LLMs.
- Added `docs/USING_WITH_LLMS.md` with exact install, invocation, update, fallback, and troubleshooting paths, including the distinction between portable skills and Claude-oriented slash-command workflows.
- Added `docs/PLUGIN_CATALOG.md` as the complete browseable catalog for all 12 plugins, 96 skills, 55 workflows, and starter prompts.
- Standardized all 12 plugin READMEs so a user landing directly on any plugin can install it, invoke a skill, run the equivalent workflow, and understand model-specific limitations without reading repository internals first.
- Added a Codex-native marketplace at `.agents/plugins/marketplace.json` plus `.codex-plugin/plugin.json` manifests for all 12 plugins, while keeping the existing Claude marketplace and the underlying `SKILL.md` files as the single capability source.
- Extended consistency tests to enforce Claude/Codex marketplace parity, Codex manifest/version correctness, multi-LLM onboarding sections, and valid namespaced command references.
- Removed five unreferenced legacy media assets under `.docs/images/` and two stale internal audit/backlog documents under `docs/audit/`; runtime skills, commands, standards, reliability assets, evaluation harnesses, and CI were preserved.

### Prospect Discovery Engine

- Added **`pm-prospect-discovery`** with 10 local skills and 4 workflows for repeatable enterprise pre-RFP discovery, from sparse prospect context through evidence, hypotheses, journey decomposition, adaptive questioning, synthesis, and proposal-readiness gates.
- Added a provider-neutral `prompts/prospect-discovery-master.md` so the capability can run in any capable LLM without requiring a Claude plugin runtime.
- Added fail-closed controls for unsupported prospect systems, APIs, data quality, volumes, budgets, stakeholder authority, buying intent, and operational facts. Tool/search failure now remains `coverage incomplete / UNKNOWN`.
- Added explicit anti-confirmation behavior so a Sales or user-proposed use case is treated as a hypothesis, red-teamed against alternative root causes, existing-system/configuration options, vendor substitutes, lighter interventions, and `DO NOTHING`.
- Added a reusable 16-dimension enterprise discovery taxonomy with decision-linked MUST ASK questions, conditional Level 2 branches, and guidance to prefer roughly 15-25 high-yield questions for a 60-90 minute session instead of questionnaire bloat.
- Added an assumption register with P0/P1/P2 prioritization and `UNTESTED | CONFIRMED | DENIED | PARTIAL | UNKNOWN` states.
- Added separate readiness gates for solutioning, architecture, estimation, business case, and proposal. Discovery-confidence scores cannot override unresolved P0 blockers.
- Added an enterprise prospect-discovery SOP, evidence standard, readiness scoring guide, model-agnostic usage guide, reusable brief/summary/proposal-handoff templates, and a portable HTML session shell.
- Added the JFLL Quote-to-Booking discovery artifact as a generalized reference pattern rather than a freight-specific questionnaire.
- Added eight prospect-discovery adversarial scenarios and `tests/test_prospect_discovery_contracts.py` covering preferred-solution confirmation bias, unknown API assumptions, enthusiasm-as-demand, questionnaire bloat, low-volume automation, user-buyer mismatch, missing data quality, and second-discovery requirements.
- Updated root README, marketplace registration, agent guidance, and consistency tests for 12 plugins, 96 skills, 55 workflows, model-agnostic usage, and the current `git-subdir` marketplace source shape.

### Business Case Reliability Wave 4

- Added **`pm-business-case`** with 6 local skills and 5 workflows for generalized evidence-first business-case formation, evidence refresh, investment red-teaming, and gated BUILD / BUY / PARTNER / EXPERIMENT / DEFER / KILL / NOT READY decisions.
- Added a mandatory business-case evidence contract with explicit `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`, `PROPOSAL`, and `DECISION_THRESHOLD` states, plus source freshness, contradiction, corroboration, and user-claim handling rules.
- Added a machine-readable evidence-ledger template and standard-library `validate_evidence.py` proof validator that rejects unsourced facts, unreconstructable estimates, unresolved P0 evidence, and irreversible investment decisions that fail proof obligations.
- Added competitor search-exhaustion and contradiction gates to the business-case flow so a weak or failed first search cannot become “no competitors”; user-supplied competitors remain leads until independently verified.
- Added customer/JTBD, build-vs-buy-vs-partner-vs-do-nothing, falsifiable PoC, willingness-to-pay, reconstructable economics, commercialization, and platform/reuse gates so technical feasibility cannot silently become market or investment proof.
- Added 20 business-case adversarial scenarios covering zero-result research, user-invented competitors, stale evidence, conflicting market sizes, missing ROI inputs, absent WTP proof, sunk-cost build bias, demo-as-PoC errors, premature platform claims, tool failure, unverifiable quotes/citations, AI-label bias, and technical-success/commercial-failure divergence.
- Expanded the behavioral evaluation harness with first-run business-case cases for zero-result competitor research, missing ROI inputs, premature platform investment, and technical success without commercial proof. A 100/100 soft score still cannot override a catastrophic hard-gate failure.
- Added `tests/test_business_case_contracts.py` and extended the behavioral-harness tests so future changes cannot silently remove evidence gates, reconstructable economics, first-pass competitor safeguards, platform proof requirements, or deterministic decision blocking.
- Preserved `pm-enterprise-transformation/solution-business-case` as the specialized future-capability investment primitive while positioning `pm-business-case` as the generalized business-case engine.

### Behavioral Evaluation Wave 3

- Added a model-agnostic **behavioral evaluation harness** in `evaluation/` so actual Claude, Codex, or other model outputs can be scored rather than inferring quality from prompt text alone.
- Added 10 frozen adversarial golden cases covering zero-result competitor research, single-client-demand bias, fake reusable IP, target-to-success claim inflation, confidentiality leakage, cherry-picked sales uplift, PoC-to-production confusion, automation review-cost erosion, uncontrolled external side effects, and vendor-demo happy-path bias.
- Added a shared **100-point decision-quality rubric**: evidence integrity, analysis sufficiency, uncertainty calibration, analytical correctness, decision usefulness, trade-offs, edge cases, enterprise execution realism, actionability, and executive clarity.
- Added deterministic catastrophic hard gates that take precedence over the soft score: a nominal 100/100 judgement still fails when a hard gate is breached.
- Added `evaluation/score_output.py` to score captured first-run outputs with optional human/independent-model judgement files.
- Added `tests/test_behavioral_eval_harness.py` to validate rubric weights, case coverage, known-bad failures, and hard-gate precedence.
- Updated README and agent guidance to distinguish guard-regression tests from actual output benchmarks and to prohibit unsupported “100/100” claims without scoped benchmark evidence.

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