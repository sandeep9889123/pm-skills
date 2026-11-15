# Portable measurement records

Use Markdown, CSV or JSON; these are logical fields rather than a mandatory vendor schema.

| Artifact | Minimum record |
| --- | --- |
| Contract | product job, owner, authority, scope, metrics, gates, allowed actions and evidence gaps |
| Case | case_id, group_id, slice, origin, selection, source snapshot, requirement, expected behavior, oracle and split |
| Label | criterion/rubric version, reviewer/provenance, original label, rationale, adjudication and uncertainty |
| Run | run_id, case/group, trial, timestamps, prompt/model/tool/corpus hashes or versions, raw output locator, status and final state |
| Grade | run/criterion, grader version, evidence, PASS/FAIL/BLOCKED/NOT_RUN, unresolved cases and score denominator |
| Cost | attempted task, verified success, nonoverlapping cost total, currency, price version, missing components and observed wall-clock latency |
| Decision packet | matched comparison, critical and slice failures, uncertainty, controls, evidence links and owner decision pending |

Example: a tool timeout with unchanged order state and a completion reply is a proposed FAIL for an approved completion requirement, even if language quality is high. If final state cannot be inspected, record UNVERIFIED rather than manufacturing a success or silently deleting the task.

Keep hashes, source locators, permissions and freshness attached through handoffs. A template, static check or synthetic fixture does not create a runtime observation. Store sensitive raw content in its authorized location and expose only permitted identifiers in shared reports.
