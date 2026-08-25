# Model-Agnostic Usage

The core capability is plain Markdown and does not require Claude, ChatGPT, Codex, Gemini, or any other specific runtime.

## Universal mode

Give any capable LLM:

1. `prompts/prospect-discovery-master.md`
2. prospect context
3. source materials
4. desired meeting duration and next decision, if known

Optional instruction:

> Follow the local `pm-prospect-discovery` skills as modular reasoning contracts. Treat source files as evidence, use tools when available, and fail closed when decision-critical evidence is missing.

## Agent Skills mode

Models or agents that support the Agent Skills convention can load individual `skills/*/SKILL.md` files based on the task.

## Command mode

Claude-compatible plugin runtimes can use `commands/*.md`.

Other runtimes can treat each command file as an orchestration prompt. Replace `$ARGUMENTS` with the prospect context.

## No-browsing mode

If browsing is unavailable:

- use supplied evidence only
- tag unsupported account context as `UNKNOWN`
- do not fabricate public research
- generate a research gap list for a human or connected tool

## No-file mode

Paste the master prompt and the minimum prospect context directly into the model.

## Portability rule

Provider-specific tool names must not be required for correct reasoning. Skills may say "use available research or file tools", but the logic must remain valid when those tools are absent.
