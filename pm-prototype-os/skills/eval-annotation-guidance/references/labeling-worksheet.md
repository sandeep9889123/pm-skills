# Labeling worksheet

Example only: a fictional support assistant must use the current authorized policy. The product owner must supply that policy; do not infer it from an old retrieved snippet.

| Criterion | PASS | FAIL | UNRESOLVED |
| --- | --- | --- | --- |
| Policy support | Material policy claims supported by the current authorized source | A material claim contradicts the supplied current authority | Current authority or relevant context missing |
| Action completion | Requested action verified in the authorized system | Reply claims completion but verified state shows otherwise | Final state cannot be inspected |

Record each criterion independently. One good citation cannot cancel another unsupported material claim. Abstention can pass a requirement to avoid unsupported answers; evaluate task completion separately so refusal does not count as success on answerable tasks.

Worksheet fields: case_id, conversation/group_id, population slice, source/version, criterion, reviewer, original label, rationale/evidence locator, timestamp, rubric version, adjudicator, adjudicated label, disagreement reason and intended split. Preserve the original record after adjudication.

Before labeling a batch: show reviewers the permitted evidence and counterexamples; hide model identity where practical. After a pilot: inspect disagreement by criterion and slice. A missing evidence source is not automatically a model failure. A repeated complaint may be one exported conversation, not several independent incidents.
