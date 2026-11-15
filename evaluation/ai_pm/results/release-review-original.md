# AI PM skill update, independent maintenance review

Reviewed 2026-11-15 against local HEAD `fab8975125c41489b840fcaf89cdce3ab3d6e8b9`, tree `ff6e49d7dd2861b09d719fff70a6f005f15ceada`. Read `AGENTS.md` and `CLAUDE.md` before inspection. No repository source files were changed by this review.

Two low-priority documentation defects found. No P0/P1/P2 functional defect found in the reviewed changes.

## Findings

1. **P3, new update link does not survive standalone plugin installation.** `pm-prototype-os/README.md:52` links to `../docs/UPDATING.md`. The marketplace distributes the `pm-prototype-os` git subdirectory (`.claude-plugin/marketplace.json:318-322`), so a separately installed or uploaded plugin does not contain that parent `docs` folder. Following the new update instructions from that installed README produces a missing local target. The new link-existence test passes only because it checks the complete repository (`tests/test_ai_pm_evaluation.py:134-139`). Use a repository HTTPS documentation link or include an update document inside the plugin. This affects documentation discoverability, not execution of the skills. The same escape pattern in the earlier onboarding links predates this update.

2. **P3, economics example conflates attempts with tasks.** `pm-prototype-os/skills/prototype-ai-architecture/references/architecture-worksheet.md:7` gives a total across “six attempts” and labels total/6 as cost “per attempted task.” Attempts can include retries within one task, so this denominator is not established. For example, six attempts across three tasks would give USD3 per attempted task for USD9 total, rather than USD1.50. The main architecture procedure and `cost-and-routing.md` correctly use distinct attempted tasks. Change both example occurrences to six tasks, explicitly say one attempt per task, or provide the separate task count.

## Verification and reviewed scope

- `python3 validate_plugins.py`: passed for 13 plugins, 105 skills, and 60 commands. The existing `pm-enterprise-transformation` missing `author.email` warning remains.
- `python3 -m unittest discover -s tests -v`: all 186 tests passed.
- `git diff --check HEAD`: passed.
- Inspected the complete tracked diff, all new skill procedures and their references, application-evaluation modules, both offline calculators, forward-task fixture, scenario additions, inventories, provider manifests, and update documentation.
- Verified that the new standalone skills keep their required worksheets inside their own folders and treat sibling skills/repository calculators as optional. The canonical primary skill now explicitly provides contained fallback procedures when sibling modules are absent.
- Checked the calculator formulas and their handling of missing classes, abstentions, unresolved labels, split/group leakage, provenance, repeated groups, failed-task costs, zero successes, partial costs, currencies, and end-to-end latency. Their descriptive scope and inability to verify operator attestations are explicit.
- Spot-checked the current official Claude update documentation, the EvalGen abstract, and NIST's proportion-interval page. The inspected source content supports the corresponding update, human-validation, and Wilson-interval descriptions. Sources: https://code.claude.com/docs/en/discover-plugins ; https://support.claude.com/en/articles/13837440-use-plugins-in-claude ; https://arxiv.org/abs/2404.12272 ; https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm . No external API or package installation was performed.

## Limitations

This is a static maintenance review plus offline tests, not an actual Claude, ChatGPT, or Codex plugin installation, activation, or behavioral benchmark. No production AI application, judge, RAG pipeline, agent, telemetry, incident recovery, or human-label provenance was validated. Not every external source was independently reread in full. The root agent's validation report was still being prepared and is outside this review. The fixture's freeze chronology cannot be independently established from its self-attested JSON field alone. Green structure/arithmetic checks do not establish application quality, runtime parity, or a universal skill-quality score.
