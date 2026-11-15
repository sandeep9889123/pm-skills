# Calibration worksheet

Required: criterion/rubric version; label origin and reviewer role; case/group IDs; source snapshots; train/dev/test allocation; freeze time; exact judge configuration; owner-defined acceptance gates; unresolved cases.

Toy example: a supplied worksheet has TP=2, FN=1, TN=4 and FP=1 under the failure-positive convention. Agreement is 6/8, failure recall is 2/3, specificity is 4/5 and precision is 2/3. Report all denominators and the origin of the labels. A dev worksheet does not establish held-out alignment; unknown authorship remains unknown even when arithmetic is correct.

Optional repository command, from repository root:

```bash
python3 evaluation/ai_pm/score_judge.py labels.csv --split test --provenance human-reviewed --heldout-attested
```

CSV columns: case_id, group_id, split, human_label, judge_label. Allowed human labels: PASS, FAIL, UNRESOLVED. Allowed judge labels: PASS, FAIL, ABSTAIN. A group cannot cross data splits. The helper exposes unresolved/abstained cases and returns undefined rates where a class has no observations. It cannot verify the operator's provenance or held-out attestation. Synthetic examples must use `--provenance synthetic`; their result is FIXTURE_ONLY.

An interval or many repeated judge calls does not compensate for unrepresentative data, correlated cases, criteria drift, or absent human authority. Record the selection and blind spot alongside every numeric result.
