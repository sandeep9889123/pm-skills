# PM AI Shipping

AI product shipping workflows for intended-vs-implemented review, launch readiness, documentation, test derivation, static security checks, and static performance checks.

## When to use

Use this plugin when you need to review whether an app matches intended behavior, derive tests, document an AI-built product, run static security/performance checks, identify launch risks, or create reviewer-ready shipping evidence.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-ai-shipping@pm-skills
```

```text
/pm-ai-shipping:ship-check [repository or implementation context]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-ai-shipping@pm-skills
```

```text
Use pm-ai-shipping to compare intended and implemented behavior, derive tests, identify launch blockers, and separate verified code evidence from unknowns.
```

### ChatGPT

Upload `skills/intended-vs-implemented/` or `skills/shipping-artifacts/` if Skills is available.

With the GitHub app:

```text
Read pm-ai-shipping/skills/intended-vs-implemented/SKILL.md from sandeep9889123/pm-skills and use it to review the connected application repository.
```

ChatGPT's GitHub app may be read-only on some surfaces, so use Codex or another write-capable environment when code changes are required.

### Other LLMs

Copy or attach the relevant skill folder. Static audit workflows require actual repository/code access for evidence-backed findings.

## Skills (2)

- `intended-vs-implemented`
- `shipping-artifacts`

## Commands (5)

- `/pm-ai-shipping:derive-tests`
- `/pm-ai-shipping:document-app`
- `/pm-ai-shipping:performance-audit-static`
- `/pm-ai-shipping:security-audit-static`
- `/pm-ai-shipping:ship-check`

## Example prompts

```text
Use intended-vs-implemented to compare the product requirements with the actual code. Cite implementation evidence, preserve unanswered intent as unknown, and rank gaps by user/business consequence.
```

```text
Use pm-ai-shipping to produce a ship/no-ship packet with test coverage, security/performance caveats, unresolved blockers, monitoring, and rollback needs.
```

## Operating rules

1. Distinguish demo quality from production readiness.
2. Test intended, failure, and edge behavior.
3. Do not declare security or performance safety from superficial inspection.
4. Flag unverified implementation details.
5. Connect findings to launch risk and user impact.
6. Produce concrete fixes, not generic warnings.

## Output standard

A strong output includes intended behavior, implementation evidence, gap analysis, tests, launch blockers, security/performance caveats, monitoring recommendations, and a ship/no-ship view.

## Attribution

Based on the original `phuryn/pm-skills` AI shipping workflows, enhanced with stronger AI PM launch-readiness and evidence discipline.
