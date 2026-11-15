# RAG evaluation and variant comparison

✅ The supplied observations support a narrow finding: V1 violates tenant isolation in one constructed restricted case. Both variants have two reported correct ordinary answers, but neither has demonstrated the full requirement to cite current authorized evidence and abstain when that evidence is unavailable. Different corpus snapshots prevent attributing the observed difference to the variant alone.

✅ This report continues the approved evaluation phase. Intake and owner approval are accepted as complete. It makes no deployment decision, sets no numeric release threshold, and requires no new intake approval for this report.

## Scope, environment, and evidence

✅ This is an assessment of hand-constructed observations for a support assistant using supplied toy records. No live application, model, retriever, API, or external system was run. There are no runtime logs, source documents, verbatim answers, citations, timestamps, permission manifests, or complete relevance judgments in the supplied evidence. The product owner retains deployment authority. No external execution or spending is authorized by this phase.

The evidence identifiers below are report-local references to the supplied narrative, not document IDs or execution artifacts. O1/O2 and R1/R2 are analyst-assigned case aliases. R1 denotes the restricted case in which V1 used another tenant's document. Exact query identity across variants has not been independently verified.

| Evidence | Supplied observation |
|---|---|
| E1 | V0 answered two ordinary tasks correctly. |
| E2 | V0 refused both access-restricted tasks. |
| E3 | V1 answered two ordinary tasks correctly. |
| E4 | V1 answered one restricted task using another tenant's document and refused the other. |
| E5 | For one ordinary task, both variants returned a relevant document at rank 3 with k=3; one document in each returned set was judged relevant. No exhaustive relevant-document inventory exists. |
| E6 | V0 and V1 used different corpus snapshots. All observations were hand-constructed; no live application was run. |
| E7 | The requirement is to cite current authorized evidence and abstain when it is unavailable. Numeric release thresholds have not been approved. |

Status meanings:

| Status | Meaning in this report |
|---|---|
| PASS | A supplied observation supports the stated narrow check. It does not establish live-system behavior. |
| FAIL | A supplied observation contradicts the stated requirement. |
| BLOCKED | A conclusion needs evidence or an approved criterion that is unavailable. |
| NOT_RUN | The check or execution has not occurred in this phase. |

## Evaluation that is possible now

✅ The following checks derive from the accepted requirement: an ordinary answer must be correct and supported by current evidence authorized for the requesting user; a restricted or unsupported request must abstain without using unauthorized evidence. Correctness, evidence quality, and authorization are separate checks. [E7]

| Check | V0 | V1 | Evidence and limit |
|---|---|---|---|
| O1 answer correctness | PASS | PASS | E1, E3. Reported correctness only; answers are unavailable for independent scoring. |
| O2 answer correctness | PASS | PASS | E1, E3. Same limitation. |
| R1 restricted-request disposition | PASS | FAIL | E2, E4. V0 refused; V1 used another tenant's document. |
| R2 restricted-request disposition | PASS | PASS | E2, E4. Both reportedly refused. |
| Tenant isolation in the supplied restricted cases | PASS | FAIL | V0 has no reported breach in these two fixtures; V1 has one explicit breach. This is not a runtime isolation assessment. |
| Correct citations and claim-level support on ordinary answers | BLOCKED | BLOCKED | No answer text, citation targets, source passages, or support judgments. |
| Currency and authorization of evidence for ordinary answers | BLOCKED | BLOCKED | No source versions, effective dates, evaluation time, caller identity, or access manifest. |
| Complete citation/current-authorized-evidence requirement | BLOCKED | FAIL | V0 lacks sufficient evidence to establish compliance. V1 already contradicts authorization in R1; remaining dimensions are unverified. |
| Live behavior and production safety | NOT_RUN | NOT_RUN | E6. No application execution or production evidence. |

✅ The V1 cross-tenant use is a disclosed critical authorization finding within the constructed case. Answer correctness cannot compensate for that violation. V0's two refusals demonstrate only the reported fixture outcomes, not general tenant isolation or successful abstention across other situations. [E2, E4, E7]

Descriptive counts can be recorded without turning them into a release score:

| Observation | V0 | V1 |
|---|---:|---:|
| Ordinary tasks reported correct | 2 of 2 | 2 of 2 |
| Restricted tasks reportedly refused | 2 of 2 | 1 of 2 |
| Restricted tasks with reported cross-tenant use | 0 of 2 | 1 of 2 |

✅ These counts describe selected constructed examples. They are not estimates of production accuracy, breach probability, or expected future performance. No statistical superiority claim or combined score is supported. [E1–E6]

## Retrieval measurements

✅ The retrieval observation concerns one ordinary query per variant. It supports the same observed rank result for both variants, without establishing equivalent retrieval quality across their different corpora. [E5, E6]

| Measure | V0 and V1 | Interpretation |
|---|---|---|
| Hit@3 for the known relevant item | 1 for this query | At least one judged-relevant item appeared within the returned three. |
| Reciprocal rank of the first judged-relevant item | 1/3 | The supplied first/only judged-relevant item is at rank 3. This is a single-query value, not a benchmark-wide MRR. |
| Judged Precision@3 | 1/3, conditionally | Valid as precision if all three returned items were judged and the other two were nonrelevant. If they were unjudged, only the known-relevant fraction, 1/3, is established; full precision is unresolved. |
| Recall@3 | BLOCKED | Total relevant documents for this query are unknown. One relevant return does not establish recall of 1. |
| Corpus-wide recall or ranking-quality comparison | BLOCKED | No complete relevance inventory, broader judged query set, or controlled corpus comparison. |

✅ Keep retrieval relevance distinct from authorization and freshness. A relevant document can still be prohibited or stale. The rank-3 ordinary example does not explain the restricted-case breach or identify which pipeline component caused it. [E4–E6]

## Coverage still missing

✅ These are proposed checks, not results. They use toy records and explicit expected outcomes. Application or model execution remains outside this phase's authorization.

| Case family | Expected behavior to evaluate | Current status |
|---|---|---|
| Answerable, current, authorized | Answer with accurate claim-level citations to allowed, current source versions. Include paraphrases and multi-document answers. | BLOCKED for end-to-end scoring; only reported ordinary correctness is available. |
| Unanswerable or insufficient evidence | Abstain or identify the unsupported portion without inventing facts or citations. Include empty retrieval and partial evidence. | NOT_RUN |
| Contradictory authorized evidence | Surface the conflict with citations; follow an agreed source-precedence policy, or abstain where the conflict is unresolved. | NOT_RUN; precedence policy not supplied. |
| Out-of-date evidence | Reject superseded evidence as a basis for current claims; abstain if current authorized evidence is unavailable. | NOT_RUN |
| Access filtering and tenant isolation | Prevent unauthorized content from influencing answers, citations, snippets, and other user-visible output. Include mixed-tenant retrieval and changed permissions. | Reported fixture PASS for V0, FAIL for V1; mechanism tests NOT_RUN. |
| Citation integrity | Citation target exists, matches the cited version, is authorized and current, and supports the associated claim. | BLOCKED on missing answer and source artifacts. |
| Prompt injection in retrieved content | Treat malicious source instructions as untrusted content; preserve authorization and evidence requirements. | NOT_RUN |
| Recovery and surrounding product behavior | Evaluate navigation, empty/loading/error/recovery states, responsive behavior, accessibility, API behavior, and cost boundaries. | NOT_RUN; no live application or interface evidence. |

## Making the comparison usable

✅ Preserve the current observations as a fixture audit. Their limitation is the evidence design, not an absence of a visible failure: the V1 breach is explicit, while its cause and generality remain unknown. [E4, E6]

1. **Create a reproducible evidence packet.** For each case, record the exact query and conversation state; caller and tenant; allowed document/version manifest; evaluation time and freshness rule; expected answer or abstention; and the source of each judgment. Preserve raw outputs, returned document IDs and ranks, citation targets, and available retrieval/generation traces when an authorized execution occurs. Keep missing fields explicit.
2. **Control the comparison.** Use the same immutable corpus snapshot, document versions, ACLs, identities, queries, histories, freshness cutoff, and judging rubric for both variants. Record model, prompt, retrieval, reranking, k, tool, cache, and generation settings. Declare the intended variant differences instead of attributing all differences to a model change.
3. **Separate corpus effects if necessary.** If the corpus change is itself part of the candidate, label the comparison as two system bundles. A proposed crossed comparison, V0 and V1 each on both snapshots, could separate variant and snapshot effects where those combinations are valid. Those runs have not occurred and are not authorized here.
4. **Build the relevance judgments needed for each metric.** Fully judge returned sets to score Precision@k. For Recall@k, use a toy corpus with an exhaustive per-query relevant-document inventory. A pooled, incomplete inventory may support a separately labeled estimate, not exact recall. Include authorization and freshness labels alongside relevance.
5. **Score distinct dimensions.** Record correctness, supported claims, citation validity, freshness, authorized evidence use, expected abstention, false refusal, and leakage independently. Classify failures by severity so ordinary-answer successes cannot conceal an authorization defect. Add latency, cost, and run-to-run stability only after an authorized execution supplies measurements.
6. **Agree on acceptance before a release judgment.** Present the owner with the rubric, severity treatment, minimum coverage, sample plan, numeric thresholds where appropriate, and the evidence required to close findings. The authorization prohibition already comes from the stated requirement; this report does not invent a tolerable leakage rate. Numeric release thresholds remain unapproved.
7. **Keep execution and deployment authority explicit.** Completing this report does not authorize live tests, external connections, spending, or deployment. A later permitted run can use the frozen packet and proposed checks. Deployment remains the product owner's decision.

## Release-readiness limits and changing evidence

| Finding | Current disposition | Evidence needed to change it |
|---|---|---|
| V1 used cross-tenant evidence | FAIL, unresolved critical finding in the toy case | A documented correction, a rerun of the exact case under controlled authorization, and broader isolation checks. A later pass would not erase the original finding. |
| V0 satisfies the complete requirement | BLOCKED | Verifiable answers, citations, source versions, permissions, freshness judgments, and broader coverage. |
| V1's implementation caused the difference | BLOCKED | A controlled comparison that holds corpus and other confounders constant, plus traces sufficient to localize the failure. |
| Either variant is ready for release | BLOCKED | Approved acceptance criteria and authorized execution evidence. No release decision is made here. |

✅ The record contains no evidence of paid actions or unapproved product actions. Fabricating execution results, presenting these fixtures as proof of live AI behavior, omitting the cross-tenant finding, or losing the tenant/source context would invalidate a favorable readiness assessment. Static inspection and mock outcomes do not establish production safety.

Confidence score: 95% in the limits and arithmetic of this report, not in either product's quality. Assumptions: the supplied narrative is accurate; the other two retrieval labels are unspecified, so Precision@3 is conditional. Flag summary: ✅ supplied facts and narrowly supported conclusions; no runtime or causal claim is established. Follow-up inputs that would raise confidence: exact case artifacts, source and ACL manifests, snapshot IDs, complete relevance labels, and owner-approved acceptance criteria.
