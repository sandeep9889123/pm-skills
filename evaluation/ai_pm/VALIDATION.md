# AI PM update validation, v2.3.0

## Result and scope

The update provides three new skills and expands the existing AI PM procedures. Local deterministic checks pass. The exploratory comparisons below found no measured advantage on their checked criteria: both old and revised procedures met all five criteria in each of four synthetic tasks. These were small, model-reviewed checks, not evidence of universal quality, production reliability or Claude-native activation.

## Executed deterministic checks

- Baseline remote commit a2d0591e698f4f4e1c00aa83547673a06aca3cc0: plugin validator passed and 171 tests passed.
- Revised source: plugin validator passed with 105 skills, 60 workflows and 13 plugins.
- Final local suite: 187 tests passed, including 16 new arithmetic, data-integrity and portability tests.
- Existing benchmark definition remains valid: 26 primary and 14 regression cases.
- One pre-existing nonblocking warning remains: missing author.email in pm-enterprise-transformation.
- The complete local baseline tree ff6e49d7dd2861b09d719fff70a6f005f15ceada matches the remote baseline. Local snapshot commit fab8975125c41489b840fcaf89cdce3ab3d6e8b9 has a different commit identity but identical file tree (348 files).

See [provenance](provenance.json), [source fingerprints](results/source-fingerprints.json) and the live [PR checks](https://github.com/sandeep9889123/pm-skills/pull/19/checks). Local tests exercise arithmetic and package contracts; they do not execute a production AI application.

## Exploratory before/after tasks

The four scenario definitions were frozen before procedure edits. Fresh execution contexts received a named procedure and task, without separate scoring criteria or prior outputs. The first two new specialized procedures are compared with the earlier generic prototype-evaluation procedure; the RAG and architecture comparisons use the earlier corresponding procedure. One completed output per condition was reviewed in a separate context with version labels masked. Outputs can still reveal procedural detail, so blinding is limited.

| Synthetic task | Earlier procedure, criteria met | Revised procedure, criteria met |
| --- | --- | --- |
| judge | 5/5 | 5/5 |
| discovery | 5/5 | 5/5 |
| rag | 5/5 | 5/5 |
| architecture | 5/5 | 5/5 |

Counts describe five predeclared criteria per output, not a validated aggregate quality metric. No criteria failures or unsupported-readiness issues were reported by the reviewer on these tasks. There is a ceiling effect on this small case set; it cannot support a claim of improved accuracy, error rates, productivity or ROI. Revised outputs were longer in these runs; user review burden and time were not measured.

A separate annotation transfer task also met its five criteria. After the maintenance review corrected a task-versus-attempt wording ambiguity, a fresh architecture rerun met the same five criteria. The earlier architecture output is retained rather than replaced. Two initial candidate sessions were interrupted before complete saved outputs and were resumed in fresh contexts. No output was coached or edited to pass grading.

Raw outputs, both model-review records, the revealed sample mapping and artifact hashes are in [results](results/). The [criteria summary](results/criteria-summary.json) exposes all ten completed outputs. The author knew the synthetic task definitions; source examples were kept distinct from their exact numbers. The extra annotation task was authored after the procedure freeze. Exact provider/model identifiers and full provider/system traces were not exposed by the host. These are host-model task artifacts, not a complete Wave 7 benchmark or a human-reviewed product dataset.

## Maintenance review and corrections

A separate read-only model review inspected procedures, packaging, arithmetic, source/update references and tests. It found two low-priority documentation defects: an installed-plugin link escaped the package, and an example conflated attempts with distinct tasks. Both were corrected. A new test copies the plugin outside the repository and checks local links there. The original [review](results/release-review-original.md) is retained with its limitations.

## Preserved evidence boundaries

The original 51 Prototype OS scenario definitions and 15 RAG cases retain NOT_RUN status. The repository's full PM-skill qualification benchmark has not been run by these tests. No live RAG system, external tool actions, deployment, real judge alignment, human-label provenance, production telemetry or installed Claude account was validated. No separate paid model API calls or package installations were used.

## Approved task-to-deliverable map

| Task | Approved work | Delivered artifact or procedure |
| --- | --- | --- |
| 1 | Annotation guidance | eval-annotation-guidance skill and labeling worksheet |
| 2 | Trace failure discovery | eval-error-discovery skill and evidence register example |
| 3 | Judge calibration | llm-judge-calibration skill, worksheet and offline calculator |
| 4 | Application eval workflow | Expanded prototype-evaluation and command routing |
| 5 | Eval dataset curation | Data/dataset module with grouped splits and leakage checks |
| 6 | Data readiness | Ownership, rights, quality, authority and freshness audit |
| 7 | RAG evaluation | Retrieval, grounding, citations, abstention and access tests |
| 8 | Agent evaluation | Tool correctness, actual state, retries, loops, delegation and recovery |
| 9 | Architecture alternatives | Rules/search, prompts, RAG, fine-tuning and agents |
| 10 | Controlled comparisons | Matched configurations, confounds, repetitions and regression evidence |
| 11 | Routing/fallback | Router signals, cache scope/invalidation and bounded fallback |
| 12 | AI economics | All-attempt costs, verified success denominator and local arithmetic |
| 13 | Trace instrumentation | Task/trace/span correlation and verification requirements |
| 14 | Production monitoring | Quality samples, drift investigation, alerts and ownership |
| 15 | Feedback to regression | Deduplication, trace linkage, oracle and confirmed-failure cases |
| 16 | Incident analysis | Evidence/timeline, competing causes, authorized containment and verified recovery |
| 17 | AI UX research | Task scripts, trust calibration, correction and handoff evidence |
| 18 | Repair references | Resolvable specialist index, standalone update guidance and package link test |
| 19 | Source grounding | Primary-source ledger with inspected scope and limits |
| 20 | Regression validation | 16 new offline tests plus preserved existing suites and scenario contracts |
| 21 | Fresh task comparison | Four paired tasks and two additional outputs, with raw artifacts and limits |
| 22 | Documentation/packaging | 105 skills, 60 workflows, 13 plugins; provider manifests version 2.3.0 |
| 23 | Reviewable PR | PR #19, with validation, review findings and update instructions |

## Next use

Use current main after the PR is merged. Previously installed or manually uploaded copies can remain on an older snapshot. Follow [update instructions](../../docs/UPDATING.md), then verify plugin version 2.3.0 and the three new skill folders. This release does not change the user's account settings. Real task data and the owner's criteria are still required to evaluate usefulness in their domain.
