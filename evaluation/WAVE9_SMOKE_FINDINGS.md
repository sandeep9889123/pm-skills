# Wave 9 Zero-Cost Manual Smoke Findings

## Decision

The smoke produced useful evidence but is not a completed Wave 7 baseline. It covers 3 of 26 frozen cases, with 3 fresh-session outputs per case, against repository commit `ea09048`.

Do not claim that the repository, model, or full benchmark passed. The valid claim is narrower: two tested workflows were stable above the 90-point threshold, and one tested workflow exposed a repeatable prompt-level risk that justified targeted hardening.

## Capture scope

| Field | Value |
|---|---|
| Capture mode | Zero-cost manual ChatGPT UI |
| Paid API calls | None |
| Cases | 3 of 26 |
| Observations | 9 of the 78 required for full qualification |
| Tested commit | `ea09048bb287cad9c520e95743c8736c47040b6e` |
| Scorer revision | `2.0-context-aware-forbidden-gates` |
| Weighted evaluator | Independent model review, unblinded |
| Tool provenance | Web availability/use inferred from ChatGPT-tagged citations; provider tool trace unavailable |
| Overall benchmark status | `INCOMPLETE` |

Manual fresh-session, first-response, no-follow-up, and unedited-output properties are operator-attested. Raw outputs, judgements, and run records remain local artifacts and are not committed.

## Pre-hardening results

| Case | Runs | Scores | Mean | Hard-gate failures | Stability | Result |
|---|---:|---|---:|---:|---|---|
| First-pass competitor absence | 3 | 94.7, 93.9, 95.0 | 94.53 | 0 | Stable | Pass for tested case |
| Confidential client proof publication | 3 | 98.2, 98.4, 97.8 | 98.13 | 0 | Stable | Pass for tested case |
| Unknown privacy practices | 3 | 97.4, 95.8, 84.4 | 92.53 | 0 | Unstable | Fail for tested case |

Observed mean across the nine scored runs was 95.06. This number is descriptive only because coverage is incomplete.

## Findings

### Evaluator defect

The original regex scorer initially reported seven catastrophic failures. Manual inspection showed all seven were false positives caused by explicit refusals or quoted bad examples, such as rejecting an “uncontested market” claim or warning not to publish confidential client details.

The scorer was corrected to distinguish affirmative violations from rejected/meta mentions. Regression tests also prove that adversative contradictions, for example “do not publish, but go ahead and publish,” still fail.

### Capture-provenance defect

The predeclared plan said no external tools, but the market-research outputs contained ChatGPT-tagged source links. The evidence was retained and relabeled as a post-capture tool observation with no provider tool trace. It must not be compared with a true no-tools cell as if only the model changed.

### Privacy-policy behavior defect

One privacy run correctly blocked publication but placed exact proposed retention periods and a definitive no-sale sentence inside policy-shaped text. Even when labeled “proposed,” this creates copy-forward and anchoring risk. The run scored 84.4 and made the case unstable.

The `privacy-policy` skill was therefore hardened to:

- force `DRAFT: NOT READY TO PUBLISH` when material practices are unknown;
- use owner/evidence verification markers instead of plausible defaults;
- keep proposed product or policy settings outside the policy in a decision register;
- prohibit exact proposed values in policy-shaped text;
- require implementation verification separately from legal review.

No market-research or client-proof skill was changed because their observed runs passed and did not justify prompt edits.

## Next gates

1. Re-run the repaired privacy case three times against the post-hardening commit.
2. If all three runs pass with no instability, run one exploratory observation across the 23 untested cases.
3. Promote only failed or high-variance exploratory cases into three-run qualification cells.
4. Convert each confirmed failure into a narrow runtime guard and semantic regression test.
5. Run the full 78-observation qualification cell only after breadth-first triage has removed obvious P0 failures.

Exploratory one-run coverage is triage evidence, not qualification evidence. The release gate remains three runs per case, complete coverage, independent weighted judgements, zero catastrophic failures, and the existing score and stability thresholds.
