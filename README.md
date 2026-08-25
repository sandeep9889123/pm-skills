# PM Skills: Reliability-First Enterprise AI Edition

> **96 PM skills and 55 chained workflows across 12 plugins.** Built for Claude, ChatGPT, Codex, Agent Skills compatible tools, and any capable LLM that can read Markdown.

A model-agnostic PM operating system for repeatable, evidence-led work across discovery, prospect discovery, strategy, execution, market research, analytics, GTM, growth, AI shipping, enterprise transformation, and business-case formation.

This repository is a fork and extension of [phuryn/pm-skills](https://github.com/phuryn/pm-skills). The upstream project created the core PM skills foundation. This fork adds reliability contracts, adversarial decision gates, enterprise workflows, business-case formation, prospect discovery, and portable packaging for higher-stakes PM work.

The reliability loop is:

`Search -> Challenge -> Expand -> Verify -> Conclude`

## Start here

| What you need | Start with |
|---|---|
| Explore a new product idea | `pm-product-discovery` |
| Prepare a prospect discovery session before an RFP | `pm-prospect-discovery` |
| Build product strategy or pricing | `pm-product-strategy` |
| Write or red-team a PRD | `pm-execution` |
| Research competitors, users, or market size | `pm-market-research` |
| Analyze SQL, cohorts, or experiments | `pm-data-analytics` |
| Build ICP, GTM, launch, or battlecards | `pm-go-to-market` |
| Position, name, or define a North Star metric | `pm-marketing-growth` |
| Review resumes, writing, NDA, or privacy drafts | `pm-toolkit` |
| Audit an AI-built product before shipping | `pm-ai-shipping` |
| Build reusable capabilities or sales transformation plays | `pm-enterprise-transformation` |
| Build an evidence-first investment/business case | `pm-business-case` |

## How the repository works

### Skills

Skills are the reusable reasoning building blocks. Every skill lives at:

```text
pm-<plugin>/skills/<skill-name>/SKILL.md
```

The skill files use the Agent Skills style: instructions, guardrails, workflow steps, and required outputs in plain Markdown. This is the most portable layer in the repository.

### Commands / workflows

Commands live at:

```text
pm-<plugin>/commands/<workflow-name>.md
```

Claude can expose these as slash commands. Other LLMs can run the same workflow from plain language by following the command file or the equivalent prompt shown in each plugin README.

### Plugins

Plugins group related skills and workflows. Installing a plugin is the safest default because workflows often depend on multiple skills.

## Installation

### Claude Cowork / Desktop

1. Open **Customize**.
2. Open **Browse plugins** -> **Personal** -> **+**.
3. Choose **Add marketplace from GitHub**.
4. Enter:

```text
sandeep9889123/pm-skills
```

5. Enable the plugins you want if your Claude surface asks you to select them.
6. Start with a command such as `/discover`, `/write-prd`, `/competitive-analysis`, or `/build-business-case`.

### Claude Code CLI

Add the marketplace once:

```bash
claude plugin marketplace add sandeep9889123/pm-skills
```

Install the plugins you want:

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

Claude can use skills automatically when relevant. To force a specific skill, reference the skill explicitly or use the namespaced skill form supported by your Claude surface. Workflows can be invoked with their slash command.

### Codex CLI / Codex app

This fork includes a Codex-native marketplace at `.agents/plugins/marketplace.json` and a `.codex-plugin/plugin.json` for every plugin.

Add the marketplace:

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
```

Install the plugins you want:

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

Codex installs the skill bundles natively. Claude-style slash commands are not assumed to exist in Codex. Use a plain-language workflow prompt instead, for example:

```text
Use the pm-market-research skills to run a competitive analysis for [market]. Search direct, adjacent, substitute, incumbent, regional, open-source, services, manual, and internal-build alternatives. Show evidence gaps and run a contradiction pass before concluding.
```

### ChatGPT

There are two supported usage patterns.

#### Option A: upload an individual Skill

If Skills upload is available for your ChatGPT plan or workspace:

1. Download this repository with **Code -> Download ZIP**, then extract it.
2. Choose one folder under `pm-<plugin>/skills/<skill-name>/`.
3. Keep `SKILL.md` and any files inside that skill folder together. If your upload flow expects one file, zip that skill folder.
4. In ChatGPT, open **Plugins -> Skills -> Create -> Upload from your computer**.
5. Upload the skill package.
6. Ask for the task normally. ChatGPT can use installed Skills automatically when relevant.

OpenAI documents Skills as following the Agent Skills open standard. Skill availability and upload permissions depend on plan and workspace settings.

Official reference: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

#### Option B: connect GitHub and use the repository directly

If the GitHub app is available in your ChatGPT experience:

1. Open **Settings -> Apps -> GitHub**.
2. Connect GitHub and allow access to `sandeep9889123/pm-skills` if required.
3. Ask ChatGPT to use the exact skill path as the governing workflow.

Example:

```text
Read pm-business-case/skills/business-case-orchestrator/SKILL.md from sandeep9889123/pm-skills and follow it for this business case. Treat missing evidence as UNKNOWN and do not invent sources or numbers.
```

If GitHub access or Skills upload is unavailable, attach or paste the relevant `SKILL.md` into the conversation and give the task context.

Official reference: [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

### Gemini CLI, OpenCode, Cursor, Kiro, and other Agent Skills compatible tools

Copy the skill folders you want into the tool's skills directory. The exact path can vary by product version. Common project-level conventions include:

| Tool | Common project path |
|---|---|
| Gemini CLI | `.gemini/skills/` |
| OpenCode | `.opencode/skills/` |
| Cursor | `.cursor/skills/` |
| Kiro | `.kiro/skills/` |

Example on macOS/Linux:

```bash
mkdir -p .cursor/skills
cp -R pm-market-research/skills/* .cursor/skills/
```

Example on PowerShell:

```powershell
New-Item -ItemType Directory -Force .cursor\skills | Out-Null
Copy-Item -Recurse pm-market-research\skills\* .cursor\skills\
```

### Any other LLM

No installation is required. Give the model:

1. the relevant `SKILL.md`,
2. your task context,
3. the source material it should use,
4. and, for a multi-skill workflow, the relevant `commands/*.md` file or a plain-language workflow request.

Use this instruction when you want strict adherence:

```text
Treat the attached SKILL.md as the governing workflow. Follow its evidence rules and hard gates. Do not fill missing facts from memory. Mark unsupported information UNKNOWN and list what evidence is required next.
```

See [Using PM Skills with Claude, ChatGPT, Codex, and other LLMs](docs/USING_WITH_LLMS.md) for detailed setup, update, troubleshooting, and invocation guidance.

## Compatibility matrix

| Surface | Install plugin bundle | Native skills | Claude slash commands | Best usage path |
|---|---:|---:|---:|---|
| Claude Cowork / Desktop | Yes | Yes | Yes | Add GitHub marketplace |
| Claude Code | Yes | Yes | Yes | `claude plugin ...` |
| Codex | Yes | Yes | No assumption | `.agents` marketplace + plain-language workflows |
| ChatGPT with Skills | Individual skills | Yes | No | Upload a skill package |
| ChatGPT with GitHub app | No local install required | Read from repo | No | Ask ChatGPT to follow an exact repo path |
| Agent Skills compatible tools | Copy skill folders | Yes | No | Copy `skills/*` into tool skills directory |
| Generic LLM | No | Manual | No | Attach/paste `SKILL.md` and task context |

## Plugin suite

| Plugin | Skills | Workflows | Purpose |
|---|---:|---:|---|
| [`pm-product-discovery`](pm-product-discovery/) | 13 | 5 | Ideation, assumptions, experiments, interviews, feature triage, OSTs, metrics |
| [`pm-prospect-discovery`](pm-prospect-discovery/) | 10 | 4 | Enterprise pre-RFP discovery, hypotheses, adaptive questions, readiness gates |
| [`pm-product-strategy`](pm-product-strategy/) | 12 | 5 | Vision, strategy, business models, value propositions, pricing, strategic frameworks |
| [`pm-execution`](pm-execution/) | 16 | 11 | PRDs, OKRs, roadmaps, sprints, stories, tests, stakeholder work, red-team |
| [`pm-market-research`](pm-market-research/) | 7 | 3 | Competitors, personas, segmentation, journeys, market sizing, sentiment |
| [`pm-data-analytics`](pm-data-analytics/) | 3 | 3 | SQL, cohorts, A/B test analysis |
| [`pm-go-to-market`](pm-go-to-market/) | 6 | 3 | ICP, beachhead, GTM motions, growth loops, battlecards, launch |
| [`pm-marketing-growth`](pm-marketing-growth/) | 5 | 2 | Positioning, value props, naming, marketing ideas, North Star metrics |
| [`pm-toolkit`](pm-toolkit/) | 4 | 5 | Resume, writing, NDA, privacy-policy utilities |
| [`pm-ai-shipping`](pm-ai-shipping/) | 2 | 5 | Intended-vs-implemented audits, tests, docs, security, performance, ship checks |
| [`pm-enterprise-transformation`](pm-enterprise-transformation/) | 12 | 4 | Future capabilities, proof-to-GTM, sales transformation, tooling and automation |
| [`pm-business-case`](pm-business-case/) | 6 | 5 | Evidence-led market/customer/economic proof and investment decisions |

For every skill and workflow name, plus starter prompts, see [Full plugin and skill catalog](docs/PLUGIN_CATALOG.md).

## Common workflow examples

### Product discovery

Claude:

```text
/discover AI-powered meeting summarizer for enterprise teams
```

Other LLMs:

```text
Use pm-product-discovery to take this idea through ideation, assumption mapping, risk prioritization, and experiment design. Pause at each decision gate.
```

### Prospect discovery

Claude:

```text
/pm-prospect-discovery:discovery-prepare [prospect context]
```

Other LLMs:

```text
Use pm-prospect-discovery to prepare a pre-RFP discovery session. Research the account, test alternative root causes, rank plausible Phase 1 wedges, build the minimum sufficient question set, and state readiness blockers.
```

### Competitive research

Claude:

```text
/competitive-analysis [market or product]
```

Other LLMs:

```text
Use pm-market-research competitor-analysis. Do not conclude market absence from a weak first search. Search direct, adjacent, substitute, incumbent, internal-build, services, manual, regional, and emerging alternatives.
```

### Business case

Claude:

```text
/build-business-case [initiative]
```

Other LLMs:

```text
Use pm-business-case to build an investment-grade case. Create an evidence ledger first, compare BUILD/BUY/PARTNER/DO NOTHING, require reconstructable economics, define a falsifiable PoC, and produce the strongest rejection case before the recommendation.
```

### PRD and execution

Claude:

```text
/write-prd [problem or feature]
```

Other LLMs:

```text
Use pm-execution to create a decision-first PRD with scope, non-goals, user journeys, failure cases, acceptance criteria, analytics, dependencies, and validation gates.
```

## Reliability principles

For high-stakes outputs, distinguish where applicable:

- `FACT`
- `INFERENCE`
- `ASSUMPTION`
- `ESTIMATE`
- `UNKNOWN`
- `STALE`
- disconfirming evidence
- decision risks

The model must not invent competitors, market sizes, customers, prospect systems, APIs, benchmarks, case studies, financial inputs, quotes, or stakeholder decisions. Missing evidence should produce an explicit gap and validation path.

A polished artifact is not a substitute for decision readiness. `NOT READY`, `SECOND DISCOVERY REQUIRED`, `EXPERIMENT`, `HOLD`, and `KILL` are valid outcomes when evidence warrants them.

## Validation and contribution

Repository CI validates plugin structure, inventory consistency, reliability guard contracts, behavioral test fixtures, and cross-platform packaging.

- Contributor guidance: [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md)
- Quality standards: [`docs/standards/`](docs/standards/)
- Behavioral evaluation harness: [`evaluation/`](evaluation/)
- Reliability scenarios: [`reliability/`](reliability/)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)

## Attribution

Original PM skills foundation: [phuryn/pm-skills](https://github.com/phuryn/pm-skills).

This fork is maintained and extended by Sandeep Kumar M. Upstream attribution is preserved for upstream-derived skills. Fork-specific enterprise, reliability, business-case, prospect-discovery, evaluation, and multi-LLM packaging layers evolve independently.

## License

MIT, following the upstream project license.
