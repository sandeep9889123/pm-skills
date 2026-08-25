# PM Toolkit

Utility workflows for PM writing, resume review, proofreading, NDA drafting, privacy-policy starter drafts, and practical communication support.

## When to use

Use this plugin when you need to review or tailor a resume, proofread PM writing, draft basic NDA/privacy starter language, or clean up stakeholder-facing communication.

## Install and use

Full cross-LLM guide: [Using PM Skills with LLMs](../docs/USING_WITH_LLMS.md).

### Claude Code / Cowork

```bash
claude plugin marketplace add sandeep9889123/pm-skills
claude plugin install pm-toolkit@pm-skills
```

```text
/pm-toolkit:review-resume [resume + target role]
```

### Codex

```bash
codex plugin marketplace add sandeep9889123/pm-skills --ref main
codex plugin add pm-toolkit@pm-skills
```

```text
Use pm-toolkit to review this PM resume against the target role. Do not invent metrics or experience. Diagnose weak signals and rewrite only what the evidence supports.
```

### ChatGPT

Upload `skills/review-resume/`, `skills/grammar-check/`, or another specific skill if Skills is available.

With the GitHub app:

```text
Read pm-toolkit/skills/review-resume/SKILL.md from sandeep9889123/pm-skills and follow it for the attached resume.
```

### Other LLMs

Copy or attach the relevant skill folder. For legal-adjacent drafts, preserve the skill's review caveats.

## Skills (4)

- `draft-nda`
- `grammar-check`
- `privacy-policy`
- `review-resume`

## Commands (5)

- `/pm-toolkit:draft-nda`
- `/pm-toolkit:privacy-policy`
- `/pm-toolkit:proofread`
- `/pm-toolkit:review-resume`
- `/pm-toolkit:tailor-resume`

## Example prompts

```text
Use review-resume to assess this resume for a Principal Product Manager role. Separate missing evidence from writing problems and do not fabricate achievements.
```

```text
Use grammar-check to improve this email for clarity and brevity without changing intent, claims, or stakeholder commitments.
```

## Operating rules

1. Do not imply legal advice for NDA or privacy drafts.
2. Use clear caveats where expert legal review is required.
3. Resume feedback must be role-aligned and evidence-based.
4. Proofreading must preserve meaning.
5. Do not add fake achievements, metrics, employers, clients, or credentials.
6. Utility outputs should be concise and editable.

## Output standard

A strong output includes diagnosis, rewrite/draft, risk notes, assumptions, improvements, and a polished version where applicable.

## Attribution

Based on the original `phuryn/pm-skills` toolkit workflows, enhanced with stronger caveats and evidence discipline.
