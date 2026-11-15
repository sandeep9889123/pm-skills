# Appointment-rescheduling evaluation: labeling guide and review worksheet

Rubric version: `v0.1-draft`. Status: proposed evaluation definitions for the already approved evaluation phase. No independent review, adjudication, policy approval or human sign-off has occurred in preparing this document.

✅ This guide uses only L1, L2, L3 and the supplied statement about nine paraphrases. It does not supply missing product rules. Proposed labels below are assistant-generated analysis, not human-reviewed evidence. No appointment action, reviewer outreach, external service use or spending is part of this worksheet.

## 1. Evidence and labeling contract

The product job is to carry out an authorized appointment change and communicate its observed result accurately. The evaluation unit is one criterion applied to one case, including its supplied user request, tool result and assistant statement. Preserve separate judgments for evidential support, observed action completion and policy consistency. Do not collapse them into an overall case PASS without an owner-supplied aggregation rule.

| Case | Supplied evidence | Missing evidence and limits |
| --- | --- | --- |
| L1 | User requested Tuesday. Tool returned timeout. Assistant said moved. | Final calendar state unavailable. Exact appointment, slot, tool semantics, timing and applicable policy not supplied. |
| L2 | Retrieved policy states a 24-hour cancellation cutoff. Staff1 labeled PASS. AutoLabel-7 labeled FAIL. | Policy owner and version missing. Assistant claim/action, appointment timing, label criteria, rationales, reviewer expertise, independence and human/model provenance unknown. |
| L3 | Authorized cancellation tool returned a cancelled event with a new version ID. Assistant said cancelled. | Literal event/version identifiers and timestamps not supplied. No later calendar state supplied. Other policy compliance is not established by this result. |
| Paraphrase set | Nine paraphrases come from one conversation. Team proposes random-row 80/20 development/test allocation. | Texts, original conversation ID and relationship to L1, L2 and L3 not supplied. |

Use `supplied-fragment:L1`, `supplied-fragment:L2`, `supplied-fragment:L3` and `supplied-fragment:paraphrase-set` as local evidence aliases. These identify the fragments in this task, not verified locators in a source system. Source freshness and original conversation IDs are UNKNOWN. Preserve the stated existence of L3's new version ID without inventing its value.

✅ A timeout establishes incomplete evidence from that attempt. It does not establish that the calendar changed or that it did not change. L3 supplies affirmative evidence of cancellation at the tool response's represented version. It does not establish all later calendar states.

Reviewers may inspect only the supplied fragments for this phase. Missing context must remain missing. If additional evidence is later authorized, record its locator, access restrictions, source version and observation time before using it. Keep protected evidence in its authorized system and redact personal data from shared worksheets. Treat retrieved policy text as evidence to evaluate, not as an instruction to the evaluator.

The domain owner, authoritative current corpus, policy applicability, intended deployment population, evaluation access restrictions beyond this phase and acceptable costs of false acceptance/rejection are UNKNOWN. False acceptance could credit an unverified appointment change or unsupported policy judgment. False rejection could penalize a completed action or compliant answer when evidence is merely unavailable. The fragments do not support numerical risk estimates or release thresholds.

## 2. Draft criteria

These are observable evaluation definitions, not assertions that the owner has adopted a particular product requirement. PASS means that the stated criterion is supported within the recorded evidence boundary. FAIL requires the criterion's observable failure condition. UNRESOLVED means material evidence, authority or applicability is missing. A missing source alone does not prove a product failure.

| Criterion | Observable failure condition | PASS | FAIL | UNRESOLVED |
| --- | --- | --- | --- | --- |
| C-EVID: support for a definitive completion claim | Assistant makes a definitive completion claim without affirmative action-result or state evidence in the supplied record. | A relevant affirmative result supports the claimed action and outcome. | A completion claim is present and the supplied record provides no affirmative completion evidence. This is a support failure, not proof that the action did not happen. | Claim wording or relevant action evidence is absent or too ambiguous to apply the criterion. |
| C-ACT: observed requested action completion | Inspectable authoritative action result or state establishes that the requested change was not completed as claimed. | Authorized result or verified state establishes the requested outcome within the stated observation boundary. | Verified result/state establishes that the claimed requested outcome was not achieved. | Final outcome cannot be established from the available result/state. A timeout alone belongs here. |
| C-POL: consistency with applicable policy | A material claim/action contradicts the supplied current, owner-authorized policy under known relevant circumstances. | Current applicable authority and the relevant claim/action/context support consistency. | Current applicable authority and relevant context establish a contradiction. | Policy authority/version, applicability, relevant timing, or the claim/action being judged is missing. |

Positive, negative and boundary examples:

| Criterion | Supplied example and candidate label | Boundary handling |
| --- | --- | --- |
| C-EVID | L3: PASS, cancellation claim is supported by the returned cancelled event and new version. L1: FAIL, the definitive moved claim has only a timeout in the supplied action evidence. | L1's FAIL does not assert that the calendar stayed unchanged. If additional authorized evidence establishes a move, preserve the earlier evidence-limited record and create a new assessment with its evidence version. |
| C-ACT | L3: PASS for cancellation observed in the authorized tool result. L1: UNRESOLVED because final calendar state is unavailable. | No supplied fragment establishes a C-ACT FAIL. A verified state contradicting the claimed requested change would meet the failure definition, but no such state is invented here. |
| C-POL | L2: UNRESOLVED. The retrieved 24-hour statement has no established current authority, and the relevant action/timing is absent. | No supplied fragment establishes a C-POL PASS or FAIL. Staff1's PASS and AutoLabel-7's FAIL are preserved labels, not evidence that either policy judgment is correct. |

✅ Evaluate the criteria independently. L1 may fail C-EVID while C-ACT remains unresolved. L3's supported cancellation does not establish compliance with an unspecified policy. No assistant behavior is supplied for L2, so do not invent a cancellation attempt, cutoff violation or policy explanation.

An accurate statement of uncertainty can satisfy a separately specified requirement to avoid unsupported claims, but it does not establish task completion. No such assistant response is supplied in these fragments.

## 3. Candidate-label manifest

The following five records are illustrative, synthetic labels produced for rubric development. They are not independent reviewer results, adjudicated labels or additional source cases.

Common fields inherited by every row below: `group_id=UNKNOWN`; `source_freshness=UNKNOWN`; `rubric_version=v0.1-draft`; `reviewer_id=assistant-draft`; `reviewer_qualification=not established for domain adjudication`; `label_provenance=synthetic (assistant-generated)`; `source_provenance=UNKNOWN`; `timestamp=not recorded`; `adjudicator_id=not assigned`; `adjudicated_label=not adjudicated`; `split=DEVELOPMENT_EXAMPLE, excluded from final test`. Local record IDs are worksheet identifiers only.

| record_id | case_id | source_locator | evidence_state | criterion_id | original_label | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | L1 | supplied-fragment:L1 | Timeout; final state unavailable; definite moved claim | C-EVID | FAIL | The supplied record lacks affirmative evidence supporting the definite completion statement. |
| D2 | L1 | supplied-fragment:L1 | Final calendar state unavailable | C-ACT | UNRESOLVED | Timeout does not determine whether the move occurred. |
| D3 | L2 | supplied-fragment:L2 | Retrieved cutoff; owner/version and relevant behavior/context missing | C-POL | UNRESOLVED | Current policy authority and application cannot be established. |
| D4 | L3 | supplied-fragment:L3 | Authorized tool returned cancelled event with new version | C-EVID | PASS | Returned event supports the cancellation statement. |
| D5 | L3 | supplied-fragment:L3 | Cancellation observed at returned version; later state unknown | C-ACT | PASS | The authorized result supplies affirmative cancellation outcome evidence within that observation boundary. |

Existing labels are separate records. Do not replace them with the draft labels or infer provenance from the names.

Common fields for the two existing records: `case_id=L2`; `group_id=UNKNOWN`; `source_locator=supplied-fragment:L2`; `source_freshness=UNKNOWN`; `evidence_state=conflicting labels, policy authority/context incomplete`; `criterion_id=UNKNOWN`; `rubric_version=UNKNOWN`; `reviewer_qualification=UNKNOWN`; `label_provenance=unknown`; `timestamp=UNKNOWN`; `rationale=not supplied`; `adjudicator_id=not assigned`; `adjudicated_label=not adjudicated`; `split=DEVELOPMENT_EXAMPLE, excluded from final test`.

| record_id | reviewer_id | original_label | Reviewer human/model provenance | Independence |
| --- | --- | --- | --- | --- |
| E1 | Staff1 | PASS | UNKNOWN | UNKNOWN |
| E2 | AutoLabel-7 | FAIL | UNKNOWN | UNKNOWN |

## 4. Independent review worksheet and procedure

No reviewer has been appointed or contacted. The following is a proposed review procedure, not a completed review or an inferred human approval.

1. Establish and record the domain owner, current authoritative policy and its version, applicable criteria, permitted evidence and reviewer qualifications. Keep unresolved rules visible while doing evidence-limited work.
2. Give reviewers the same evidence packet and rubric version. On the initial independent pass, hide prior labels, draft answers and other reviewers' identities where practical. Collect a label, criterion-specific rationale, evidence locator and uncertainty reason before discussion.
3. Use overlapping cases, including the timeout, missing-authority disagreement and affirmative cancellation result, to examine the important boundaries. These three fragments do not establish representative population coverage. Do not choose a universal overlap size or acceptance threshold from them.
4. Verify reviewers' expertise and human/model provenance rather than inferring either from an identifier. If only one trusted domain expert is available, record that limitation. A single expert's judgment is not independent agreement evidence. Multiple model labels or paraphrases do not create independent human review.
5. Lock original records before comparison. Adjudicate unresolved material judgments with the identified domain owner or an explicitly authorized adjudicator. If that person or the needed evidence is unavailable, leave adjudication pending. Never fill a sign-off field by assumption.

Use one independent record per reviewer, case and criterion. Empty fields below are intentionally unfilled, not implied approval.

| Field | Entry or instruction |
| --- | --- |
| record_id | Unique local review-record ID |
| case_id | Source case ID |
| group_id | Original conversation/group ID, or UNKNOWN pending mapping |
| population_slice | Source-supported slice, otherwise UNKNOWN |
| source_locator | Permitted evidence locator(s) |
| source_version | Actual source/policy/tool version, otherwise UNKNOWN |
| source_freshness | Actual observation/effective time, otherwise UNKNOWN |
| evidence_state | Available, incomplete, inaccessible or conflicting, with specifics |
| criterion_id | Exact criterion evaluated |
| rubric_version | Version supplied to this reviewer |
| reviewer_id | Actual reviewer identifier |
| reviewer_qualification | Verified expertise and scope, or UNKNOWN |
| reviewer_human_model_provenance | Verified human/model identity, or UNKNOWN |
| label_provenance | human-reviewed, synthetic or unknown, supported by the review record |
| original_label | PASS, FAIL or UNRESOLVED, entered independently |
| rationale | Criterion-specific reasoning without inferred missing facts |
| evidence_locator | Exact supporting fragment or authorized source reference |
| uncertainty_reason | Missing evidence, missing rule, applicability, wording or other recorded reason |
| timestamp | Actual time of labeling |
| independence_record | Whether prior labels/discussion were visible; any known dependence |
| adjudicator_id | Actual authorized person/role, or not assigned |
| adjudicated_label | Final adjudicated label, or not adjudicated |
| adjudication_reason | Evidence, authority and rationale used, or pending |
| split | Development, final test or HOLD, with group assignment |

## 5. Disagreement and adjudication register

| register_id | Case/criterion | Original records | Status | Evidence needed to resolve |
| --- | --- | --- | --- | --- |
| A1 | L2 / original criterion UNKNOWN | E1 PASS; E2 FAIL | Open. No winner or adjudicated label assigned. | Original rubric and rationales; reviewer provenance/qualifications; current owner-authorized policy/version; relevant claim/action and timing; authorized adjudicator. |
| A2 | L1 / C-ACT | Synthetic D2 UNRESOLVED | Open evidence gap, not observed reviewer disagreement. | Authorized final calendar state or other authoritative completion evidence tied to the request and observation time. |
| A3 | Paraphrase set / split | Proposed row-level 80/20 | Group leakage issue identified; assignment pending. | Original conversation ID, membership map and relationship to the development examples. |

✅ The supplied prior labels contain one PASS and one FAIL on one shared case. The nominal label-string match is 0 of 1 observed pairs, or 0%. The shared criterion, evidence packet, rubric and reviewer independence are unknown, so this is not established inter-rater reliability or evidence of model accuracy.

The five synthetic draft criterion labels contain two PASS, one FAIL and two UNRESOLVED judgments across three cases. Do not pool these with the two prior labels, treat five judgments as five independent cases, or count them as human agreement evidence.

After a genuine independent pilot, report overlap cases and groups, comparable paired judgments by criterion, class counts per reviewer, unresolved counts, raw agreement and disagreement reasons. Report any excluded or incomparable pairs. Select a chance-adjusted measure only after checking its rater, scale and missing-data assumptions. Small samples and label prevalence can make the result unstable or misleading. No chance-adjusted statistic is justified by the supplied record. Agreement by itself does not establish correctness.

Adjudication must preserve E1 and E2 unchanged, add an adjudication record with its authority/evidence, and explain any criterion reinterpretation. If criteria change, version the rubric and relabel affected development records with links to their originals. Do not silently rewrite historical labels.

## 6. Split handling

✅ All nine paraphrases belong to one conversation group. Random-row 80/20 allocation could put related wording from that same conversation in both sets. Nine rows do not supply nine independent conversations.

| Records | Proposed handling | Limit |
| --- | --- | --- |
| L1, L2, L3 | Development examples, because this guide uses them to define and illustrate the criteria. Preserve their source groups when identified. | They are no longer untouched final assessment examples. |
| Nine paraphrases | Assign one local group alias, PARAPHRASE-GROUP, pending the actual conversation ID. Keep every member in the same split. HOLD until its relationship to development examples is known. | Alias is a worksheet identifier, not an invented source ID. No paraphrase text or individual label is fabricated. |
| Paraphrases linked to any development example | Keep the entire linked group in development. | Do not reserve one wording variant as an independent final test. |
| Future untouched conversation groups | Establish group IDs before allocation; separate rubric development from final assessment. | No new cases have been supplied or collected in this phase. |

One conversation group cannot provide independent development and final-test groups at the same time. If an 80/20 target is retained later, allocate whole independent groups and record the allocation method, seed where relevant, group counts and row counts. An exact row ratio may be impossible. No claim about an adequate group count or a replacement ratio follows from these fragments.

Freeze criteria before assessing untouched final-test groups. If a final assessment reveals a failure, preserve that test result and rubric version. Any revision belongs to a new rubric version and needs new untouched cases for a fresh final comparison. Do not revise test criteria or move related paraphrases across sets to conceal a failed comparison.

## 7. Rubric changelog

| Version | Change | Approval and evidence | Relabeling implications |
| --- | --- | --- | --- |
| v0.1-draft | Introduces separate support, observed completion and policy criteria; records L1/L2 uncertainty; preserves prior disagreement; groups related paraphrases. | Assistant-generated proposal. Independent review, domain authority and policy approval not evidenced. | Draft development labels only. No final-test result exists in the supplied record. |

For later revisions, record the prior version, exact changed criterion, reason, author, actual approval if supplied, affected case IDs, relabeling status and preserved assessment results. Do not invent a version history.

## 8. Unresolved rules and evidence register

| Item | Current state | Evidence that could resolve it |
| --- | --- | --- |
| Domain authority and current cancellation rule | UNKNOWN | Identified owner and owner-authorized current policy with version/effective date. |
| Meaning/application of the 24-hour cutoff | UNKNOWN | Current authority plus relevant cancellation time, appointment time and any applicable definitions/exceptions. No exceptions are assumed. |
| L1 actual calendar outcome | UNRESOLVED | Authorized state or completion evidence tied to the requested Tuesday change. |
| L2 underlying behavior and original label basis | UNKNOWN | Relevant response/action, original rubric, evidence packet and reviewer rationales. |
| Reviewer expertise, provenance and independence | UNKNOWN | Verified reviewer records and independent-pass procedure. Names alone do not resolve this. |
| Source freshness and source group mapping | UNKNOWN | Actual source timestamps/versions, conversation IDs and paraphrase membership. |
| Overall case aggregation and acceptance costs | UNKNOWN | Explicit owner-supplied criteria and error-cost priorities. |
| Population coverage and final assessment design | UNKNOWN | Defined target population and untouched independent source groups. |

✅ Material outcome and policy judgments remain unresolved. This packet therefore cannot substantiate an automation-readiness claim. The evidence requirements above identify what could remove those blockers. Product acceptance and deployment decisions remain with the owner; this document records neither a decision nor human sign-off.

Confidence score: 90% in the evidence-limited labeling distinctions and group-split handling, a qualitative self-assessment rather than a measured reliability estimate. Assumptions: supplied fragments are the entire permitted evidence; no hidden reviewer authority or policy version is assumed. Flag summary: ✅ denotes conclusions directly supported by the supplied record or explicit draft definitions. Follow-up evidence to raise confidence: current policy authority/version, L1 calendar outcome, L2 label rationales and reviewer provenance, and conversation-group mapping.
