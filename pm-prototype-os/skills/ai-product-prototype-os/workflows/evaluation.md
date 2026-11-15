# Phase 6 Evaluation

Map accepted requirements to evidence-backed PASS/FAIL/NOT_RUN/BLOCKED checks. Preserve user approval, declared environment, exact source versions and claim lineage. Test functionality, actual device/viewport, keyboard/contrast, errors/recovery, permission boundaries, APIs, costs and AI behavior as relevant. A prototype cannot certify production readiness.

In the complete plugin use [prototype-evaluation](../../prototype-evaluation/SKILL.md) and its directly linked modules. The relative link is from this workflow's containing directory; if sibling modules are absent, follow this fallback:

1. Define the job, current policy, success and critical failure criteria, dataset selection, human-label provenance and owner-defined gates.
2. Inspect representative and known-bad traces; link observations, deduplicate tasks and keep ambiguous cases. Separate causal hypotheses from evidence.
3. Build versioned cases and rubrics; separate development from untouched test groups. Grade exact state/schema checks deterministically and align judgment-based graders with human labels.
4. Compare frozen baseline/candidate settings with matched tools/corpus and explicit trial budgets. Verify actual outcomes and report critical/slice failures, uncertainty and missing observations.
5. For RAG separate retrieval relevance, claim support, current citations, abstention, stale/conflicting evidence and tenant filtering. For agents test authority, arguments, retries, final state, loop limits and human handoff.
6. Include all attempts, failures, tools and review in task cost; use verified successful tasks as the success denominator. Report measured elapsed latency and assumptions.
7. Deliver the comparison, failed examples, limits, monitoring/rollback requirements and approval gate. Design critique is supplementary. Report proposed checks separately from measured results.
