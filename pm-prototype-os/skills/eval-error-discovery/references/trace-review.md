# Worked trace review

Fictional examples, not observed production incidents:

| Trace | Evidence | Observation | Hypothesis / next evidence |
| --- | --- | --- | --- |
| C101 | Tool returned error; verified record unchanged; reply said complete | Claimed completion disagrees with observed state | Inspect response handling; do not assume the model is the sole cause |
| C102 | Old document retrieved; current authority unavailable | Freshness risk; correctness unresolved | Obtain the permitted current policy |
| C103 | Retrieved text requested secret disclosure; output exposed it | Instruction/data boundary failure in this example | Inspect context assembly and enforced output/action controls |
| C104 | Duplicate export of C101 | Same incident, additional copy | Link to C101; do not count as independent failure |

Keep unique tasks, attempts and exports as separate counts. An enriched set of bad examples is useful for discovery, but it does not establish the fraction of all users affected. Evidence missing from a trace can be an instrumentation gap and a limit on causal diagnosis.

Candidate regression record: case_id; parent trace/group; current source snapshot; scenario; expected final state or response; oracle; permitted tools; privacy restrictions; failure family; validation status. Keep hypothetical fixes outside the observed-evidence column.
