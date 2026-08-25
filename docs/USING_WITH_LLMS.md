# Using PM Skills with Claude, ChatGPT, Codex, and other LLMs

This guide explains the exact installation and invocation model for this repository.

## The one rule to remember

The **skill folders are the portable product**.

```text
pm-<plugin>/skills/<skill-name>/SKILL.md
```

Claude commands are workflow wrappers. They are useful where slash commands are supported, but the underlying PM reasoning should remain usable without them.

## Choose your usage mode

| You use | Recommended path |
|---|---|
| Claude Cowork / Desktop | Add this repository as a personal marketplace |
| Claude Code | Add marketplace, then install plugin bundles |
| Codex | Add the Codex marketplace in this repo, then install plugin bundles |
| ChatGPT with Skills | Upload individual skill packages |
| ChatGPT with GitHub app | Let ChatGPT read the exact skill path from the repo |
| Gemini CLI / OpenCode / Cursor / Kiro | Copy skill folders into the tool's Agent Skills directory |
| Other LLM | Attach or paste `SKILL.md` and task context |

---

## Claude Cowork / Desktop

1. Open **Customize**.
2. Open **Browse plugins** -> **Personal** -> **+**.
3. Select **Add marketplace from GitHub**.
4. Enter `sandeep9889123/pm-skills`.
5. Enable the plugins you want if prompted.
6. Start a new chat after installation if your client does not immediately expose the new skills or commands.

### Verify

Ask:

```text
What PM Skills plugins are installed from pm-skills?
```

Then try a low-risk workflow:

```text
/discover A workflow that reduces repetitive PM status reporting
```

### Skill vs command

Claude can automatically load relevant skills. If you want a specific skill, name it explicitly in your prompt. Commands such as `/discover`, `/write-prd`, `/competitive-analysis`, or `/build-business-case` orchestrate multiple skills.

---

## Claude Code

### Add the marketplace

```bash
claude plugin marketplace add sandeep9889123/pm-skills
```

### Install one plugin

```bash
claude plugin install pm-market-research@pm-skills
```

### Install all plugins

```bash
claude plugin install pm-product-discovery@pm-skills
claude plugin install pm-prospect-discovery@pm-skills
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

### Invoke

Use a workflow command:

```text
/competitive-analysis enterprise document validation
```

Or force a skill by naming the exact skill:

```text
Use the competitor-analysis skill from pm-market-research. Research enterprise document validation competitors and apply the search-exhaustion gate before any negative conclusion.
```

---

## Codex

This repository includes:

```text
.agents/plugins/marketplace.json
pm-*/.codex-plugin/plugin.json
```

These files expose each plugin's `skills/` directory as a Codex plugin bundle without copying the underlying PM logic.

### Add the marketplace

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
```

### Install one plugin

```bash
codex plugin add pm-market-research@pm-skills
```

### List available plugins

```bash
codex plugin list --available
```

### Install all plugins

```bash
codex plugin add pm-product-discovery@pm-skills
codex plugin add pm-prospect-discovery@pm-skills
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

### Invoke

Codex should discover the installed skills by their names and descriptions. Do not assume Claude slash commands are available.

Use plain language:

```text
Use pm-business-case to evaluate whether we should invest in this migration-agent capability. Start from the evidence ledger. Compare build, buy, partner, and do nothing. Do not make an investment recommendation while P0 evidence is unresolved.
```

### Update a marketplace snapshot

When you want Codex to pick up newer repository changes:

```bash
codex plugin marketplace upgrade pm-skills
```

Then start a new task/thread if your Codex surface has cached the old skill bundle.

OpenAI reference: [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex)

---

## ChatGPT

### Method 1: Upload an individual Skill

Use this when your ChatGPT account or workspace exposes **Plugins -> Skills**.

1. On GitHub, select **Code -> Download ZIP** for this repository.
2. Extract the repository locally.
3. Choose one skill folder, for example:

```text
pm-market-research/skills/competitor-analysis/
```

4. Keep the complete skill folder together. It must include `SKILL.md` and any local references/assets the skill uses.
5. If the ChatGPT upload flow expects one file, zip that skill folder.
6. In ChatGPT, open **Plugins -> Skills -> Create -> Upload from your computer**.
7. Upload the skill.
8. Start a task normally, for example:

```text
Research competitors for an AI-assisted freight quote-to-booking workflow. Apply the installed competitor-analysis skill and show search coverage, evidence state, substitutes, and unresolved candidates.
```

OpenAI states that Skills follow the Agent Skills open standard. Personal Skills availability and upload permissions depend on plan and workspace settings.

Reference: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Method 2: Use the GitHub app

Use this when you want ChatGPT to read the current repository instead of installing a local skill copy.

1. Open **Settings -> Apps -> GitHub**.
2. Connect GitHub.
3. Allow access to the repository if required.
4. Ask ChatGPT to read an exact path before performing the task.

Example:

```text
Use the GitHub repository sandeep9889123/pm-skills. Read pm-execution/skills/create-prd/SKILL.md first and treat it as the governing workflow. Then write a PRD for the attached problem statement.
```

Reference: [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

### Method 3: Attach the skill manually

If neither Skills nor GitHub access is available:

1. Download/open the required `SKILL.md` from GitHub.
2. Attach it to the conversation or paste it.
3. Add your source material.
4. Use:

```text
Follow the attached SKILL.md as the governing workflow. Do not replace its rules with generic advice. If required evidence is unavailable, preserve it as UNKNOWN and tell me what would validate it.
```

### What about commands?

Files under `commands/` are Claude-oriented workflow wrappers. In ChatGPT, use the equivalent natural-language prompt from the plugin README or tell ChatGPT to read the command file and execute its sequence.

Example:

```text
Read pm-prospect-discovery/commands/discovery-prepare.md and execute that workflow using the attached prospect context. Preserve all hard readiness gates.
```

---

## Gemini CLI, OpenCode, Cursor, and Kiro

The skill folders are plain Agent Skills style content. Copy only the skills you want, or copy an entire plugin's `skills/` contents.

### Common project paths

| Tool | Common path |
|---|---|
| Gemini CLI | `.gemini/skills/` |
| OpenCode | `.opencode/skills/` |
| Cursor | `.cursor/skills/` |
| Kiro | `.kiro/skills/` |

Check the current documentation for your tool because directory conventions can change.

### macOS/Linux example

```bash
mkdir -p .gemini/skills
cp -R pm-product-strategy/skills/* .gemini/skills/
```

### PowerShell example

```powershell
New-Item -ItemType Directory -Force .gemini\skills | Out-Null
Copy-Item -Recurse pm-product-strategy\skills\* .gemini\skills\
```

### Verify

Ask the assistant to name or use one installed skill explicitly:

```text
Use the pricing-strategy skill to evaluate three pricing models for this product. Show willingness-to-pay evidence gaps and break-even logic.
```

---

## Generic LLMs and APIs

The minimum portable usage contract is:

```text
SYSTEM / CONTEXT:
Follow the supplied SKILL.md as the governing workflow.
Preserve its evidence labels, hard gates, and output requirements.
Do not silently invent missing facts.

TASK:
[Your task]

SOURCE MATERIAL:
[Your files, notes, URLs, data, or context]
```

For a workflow that chains several skills, also provide the relevant `commands/<workflow>.md` file or describe the workflow sequence in plain language.

---

## How to choose between a skill and a workflow

Use a **skill** when you have one clear PM job:

- competitor analysis
- market sizing
- create PRD
- pricing strategy
- cohort analysis
- stakeholder map
- evidence ledger

Use a **workflow/command** when the decision requires several stages:

- `/discover`
- `/strategy`
- `/write-prd`
- `/competitive-analysis`
- `/build-future-capability`
- `/build-business-case`
- `/pm-prospect-discovery:discovery-prepare`

If your LLM does not support slash commands, state the same objective in plain language and name the plugin.

---

## Troubleshooting

### The model ignores the skill

Use a stronger instruction:

```text
Read and follow [exact SKILL.md path] before answering. Its hard gates take precedence over generic model knowledge. Do not skip required evidence checks.
```

### The model invents facts

Use:

```text
Re-run using the repository reliability contract. Separate FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, and STALE. Any unsupported decision-critical claim must remain UNKNOWN.
```

### A command is unavailable outside Claude

This is expected. Use the plugin README's plain-language workflow example or provide the command `.md` file as an orchestration prompt.

### A plugin is installed but updated skills are not visible

Refresh or upgrade the marketplace for the relevant runtime, reinstall if required, and start a new thread/task so cached skill context is not reused.

### I only need one skill

Install or upload only that skill if your runtime supports standalone Skills. Otherwise installing the whole plugin is safer because related workflows may depend on multiple skills.
