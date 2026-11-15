# PM Prototype OS
Standalone, model-neutral approval-gated PM-to-prototype skill bundle for Claude, ChatGPT, Codex and other Agent Skills capable LLMs. Uses **₹0 incremental spend** and an explicitly approved phase protocol. The canonical name is `ai-product-prototype-os` (the marketplace plugin is `pm-prototype-os`).

## Install and use
### Claude Code / Cowork
Follow the [shared LLM guide](../docs/USING_WITH_LLMS.md). Add the existing `pm-skills` marketplace, then select `pm-prototype-os`. Use `/pm-prototype-os:start-prototype` or a plain-language request naming the primary skill. No installation has been conducted as part of this PR.

### Codex
Follow [docs/USING_WITH_LLMS.md](../docs/USING_WITH_LLMS.md). Use the `.agents/plugins/marketplace.json` plugin `pm-prototype-os` or a standalone skill folder. Commands can be invoked in plain language; native Claude slash commands are not assumed.

### ChatGPT
If native Skills upload is available, package `skills/ai-product-prototype-os/` as its own ZIP. Otherwise use `adapters/chatgpt/PROJECT_INSTRUCTIONS.md` plus the canonical skill and portable project capsule. No ChatGPT-specific tools are required for reasoning; implementation capabilities depend on account and host.

### Other LLMs
Use `adapters/portable-direct-chat/START_HERE.md` and attach the main skill folder with referenced files. If no native skill system exists, treat SKILL.md as instructions and carry the context capsule between sessions. Never claim capability parity without testing.

## Skills (9)
- `ai-product-prototype-os` (orchestrator and standalone fallback)
- `prototype-ai-architecture`
- `prototype-engineering`
- `prototype-ux-quality`
- `prototype-evaluation`
- `prototype-technical-mentor`
- `eval-annotation-guidance`
- `eval-error-discovery`
- `llm-judge-calibration`

## Commands (5)
- `/pm-prototype-os:start-prototype`
- `/pm-prototype-os:review-phase`
- `/pm-prototype-os:build-prototype`
- `/pm-prototype-os:evaluate-prototype`
- `/pm-prototype-os:handoff-prototype`

## Requirements
Every NEW task: ask 5–10 nonduplicative relevant questions and stop. Before each meaningful phase transition: decision-ready approval handoff. Actions inside an approved phase must stay within explicit scope. The user owns decisions. Provide concise or deep-dive explanations; no fabricated findings. No paid API, hosted resource or new subscription charge. All 8 archetypes are covered in the standalone main skill; the RAG pilot is a specification/evaluation suite, NOT a running application.

## Third-party design intelligence
Source-informed principles from UI UX Pro Max, Impeccable and Taste Skill are optional, independently authored references. No external tools were installed or bundled. See `provenance/THIRD_PARTY.md`.

## Validation
Structural and scenario definitions are in `evaluation/prototype_os/` and `tests/test_prototype_os_*.py`. No actual Claude or ChatGPT runtime benchmark is claimed. All execution outside the approved GitHub integration awaits a later gate.

## AI evaluation and operating workflows

Version 2.3.0 adds independent annotation guidance, trace error discovery and LLM judge calibration skills. prototype-evaluation now supplies a full application-eval procedure plus local reference modules for data/datasets, RAG, agents, comparisons, cost/routing, operations and AI UX. It distinguishes application quality evidence from the repository's own PM-skill benchmark.

Ask for the skill by name or use `/pm-prototype-os:evaluate-prototype`. Examples: “Design an eval suite for this RAG assistant,” “Discover failures from these traces,” or “Assess this judge against human-reviewed labels.” Missing data produces a plan or an explicit gap, never a fabricated test result.

No sibling plugin, hosted evaluator or Python dependency is required to use these skills. Optional arithmetic helpers live outside the plugin at repository evaluation/ai_pm. If uploading an individual skill, include its references folder; sibling skills are optional. The canonical primary skill remains independently usable, with contained fallback procedures when optional specialist folders are absent.

For an existing installation, follow [update instructions](../docs/UPDATING.md), then verify version 2.3.0 and nine skill folders. New repository text alone does not establish that a cached installed copy changed.
