# Data readiness and evaluation datasets

## Readiness audit

Inventory permitted sources, owner, license/consent, tenant/access boundary, language, domain, schema, missing fields, duplicates, quality defects, update mechanism and current authority. Sample raw documents and outputs with an expert. Record ingestion/parsing failures and evidence excluded by permissions. Distinguish an available dataset from one representative of the intended job. Missing ownership, authority or sensitive-data access remains a blocker for affected claims.

## Dataset contract

Use stable case_id and group_id; retain task/slice, real/synthetic origin, selection method, source locator/version, as-of time, rubric version, expected behavior/oracle, reference evidence, allowed tools, privacy restrictions and split. Keep production prevalence estimates separate from adversarial coverage. Never blend a stress suite into an overall user success rate without declared weighting and a defensible denominator.

For each failure criterion, include passing and failing examples, ambiguous cases and relevant strata. Synthetic examples can probe rare behavior, but cannot supply observed prevalence or authentic human judgment. Reviewer approval is a recorded action, not an assumption.

Split by leakage group, such as conversation, customer, document family or paraphrase source. Reserve separate development and final assessment sets before tuning. Freeze content hashes and policy/corpus snapshots. Trace relatives in different splits are contamination even if row IDs differ. Do not move a failed test case into development and keep calling its later result untouched test evidence. Preserve the old assessment and reserve a new held-out group.

## Annotation and coverage

Define exactly what a label means and who can judge it. Keep raw independent labels and adjudication; do not silently drop UNRESOLVED cases. Build a matrix from product requirements and observed failure families to cases and oracles. Report sample sizes by slice, missing classes, unknown relevant evidence and limits on generalization. Set sample requirements from error costs and uncertainty needs, not a universal number.

Deliver: readiness register, split manifest, rubric/version record, coverage matrix, leakage check, unresolved labels and permitted handling. [Inspect datasets](https://inspect.aisi.org.uk/datasets.html) supplies a concrete sample abstraction; [OpenAI evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices) illustrates application-specific case coverage. Fields here are a provider-neutral design.
