# AI PM workflow map, v2.3.0

Use the current approved scope and existing question/phase/zero-incremental-spend contracts. These are reusable procedures and evidence templates; they do not create facts, authorize deployment or guarantee application quality.

| Task | Entry point |
| --- | --- |
| Product idea, requirements and prototype phases | pm-prototype-os/skills/ai-product-prototype-os/SKILL.md |
| Rules/search versus prompting, RAG, fine-tuning or agents; routing and economics | pm-prototype-os/skills/prototype-ai-architecture/SKILL.md |
| Application eval suite, datasets, RAG/agents, model comparison and production learning | pm-prototype-os/skills/prototype-evaluation/SKILL.md |
| Human annotation criteria and disagreement | pm-prototype-os/skills/eval-annotation-guidance/SKILL.md |
| Discover failures from traces | pm-prototype-os/skills/eval-error-discovery/SKILL.md |
| Align an automated judge with human-reviewed labels | pm-prototype-os/skills/llm-judge-calibration/SKILL.md |
| AI usability, trust, correction and recovery | pm-prototype-os/skills/prototype-ux-quality/SKILL.md |

Ask in plain language using the relevant skill name. Claude can also expose the existing `/pm-prototype-os:evaluate-prototype` workflow. The new skills are discovered from the same portable skills directory; no extra vendor, sibling plugin or hosted service is a core dependency. When uploading one skill, include its references folder. Optional repository calculators are outside the plugin and are not required for a standalone upload.

## Application evaluation outputs

Produce a product/evidence contract; representative versus stress dataset/split manifest; versioned rubric and label provenance; appropriate deterministic/human/model grading; judge error report; matched baseline/candidate runs; critical and slice failures; task cost/latency; uncertainty; monitoring/recovery plan and explicit unrun checks. Use the evaluation skill's linked modules for specific tasks.

The application eval workflow and the repository's PM-skill benchmark have different subjects. Keep their case data, measurements and claims distinct. The existing 51 Prototype OS scenarios and 15 RAG cases retain NOT_RUN status; new synthetic fixtures do not alter that history.

## Optional local calculators

Both use Python's standard library and supplied records only. They make no network/model calls and do not verify operator claims.

```bash
python3 evaluation/ai_pm/score_judge.py labels.csv --split test --provenance synthetic
python3 evaluation/ai_pm/task_metrics.py task-records.jsonl --provenance synthetic
```

For authentic reviewed labels use the appropriate provenance and held-out attestation only when true. Label CSV requires case_id, group_id, split, human_label and judge_label. Task JSONL requires task_id, success (boolean), cost, currency, cost_basis (complete/partial) and end-to-end duration_ms. Include all attempts/retries/review in nonoverlapping task totals. Retain the authoritative source and price/version outside the arithmetic report as part of the evidence manifest.

## Maintenance and evidence

Keep the [source ledger](../pm-prototype-os/skills/prototype-evaluation/references/source-ledger.md), source versions and known gaps attached to procedures. Revalidate when models, tools, corpora, rubrics or permission boundaries change. See [update instructions](UPDATING.md) for current-repository versus installed-copy behavior. Validation outcomes are recorded in evaluation/ai_pm/VALIDATION.md; read their scope before interpreting a score.
