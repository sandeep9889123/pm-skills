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

## Skills (6)
- `ai-product-prototype-os` (orchestrator and standalone fallback)
- `prototype-ai-architecture`
- `prototype-engineering`
- `prototype-ux-quality`
- `prototype-evaluation`
- `prototype-technical-mentor`

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
