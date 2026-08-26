---
name: summarize-meeting
description: "Summarize a meeting transcript into evidence-grounded notes that separate discussion, proposals, decisions, unresolved items, and explicit action ownership. Use for meeting minutes, decision records, and follow-up summaries."
---

# Evidence-Grounded Meeting Summary

## Purpose

Turn a transcript, recording-derived text, or rough notes into a faithful operational record. Meeting summaries must not upgrade discussion into decisions, suggestions into commitments, or implied responsibility into assigned ownership.

## P0 Reliability Contract

1. Treat the supplied meeting content as the source of truth for what happened in the meeting.
2. Do not use external/web context to fill missing meeting facts unless the user explicitly asks for background enrichment. If external context is added, keep it in a separate `Background` section and never use it to manufacture meeting decisions.
3. Separate `DISCUSSED`, `PROPOSED`, `DECIDED`, `ACTION ASSIGNED`, `OPEN`, `BLOCKED`, and `UNKNOWN`.
4. A decision must be explicit enough that a reasonable attendee would understand commitment was reached. Consensus tone alone is not sufficient.
5. Do not invent attendees, roles, dates, deadlines, owners, rationale, status, next meetings, or approval.
6. If an action exists but no owner was assigned, write `OWNER UNKNOWN`. If no due date was stated, write `DUE DATE UNKNOWN`.
7. Verify every verbatim quote against the supplied text. Otherwise paraphrase and label it as such.
8. Preserve disagreement, uncertainty, conditional commitments, and dissent that could change execution.
9. Do not infer that silence equals agreement.
10. Sparse or partial notes must be labelled as incomplete coverage.

## Step 1: Establish Source Coverage

State:
- source type: full transcript / partial transcript / rough notes / recap
- known date/time
- participant labels actually present
- missing sections or inaudible/uncertain portions if known

Coverage states:
`FULL TRANSCRIPT | PARTIAL TRANSCRIPT | ROUGH NOTES | SECONDARY RECAP | UNKNOWN COVERAGE`

Do not imply complete meeting coverage from partial notes.

## Step 2: Extract Atomic Statements

Classify material statements as:
- `DISCUSSION`: information or viewpoint shared
- `PROPOSAL`: suggested future action/decision
- `DECISION`: explicit commitment/conclusion
- `ACTION`: explicit task commitment
- `QUESTION`: unresolved information need
- `BLOCKER/RISK`: execution constraint raised

For ambiguous statements, preserve ambiguity rather than upgrading status.

## Step 3: Decision Integrity

For each claimed decision capture:
- decision text
- evidence/paraphrase from transcript
- decision owner/approver if explicit
- scope/conditions
- dissent or unresolved caveat

If the meeting only explored an option, keep it under `Proposals / Discussion`, not `Decisions`.

## Step 4: Action Integrity

For each action item capture only what was explicit:

| Action | Owner | Due date | Status | Evidence |
|---|---|---|---|---|

Use:
- `OWNER UNKNOWN`
- `DUE DATE UNKNOWN`
- `STATUS UNKNOWN`

rather than guessing from role, hierarchy, or conversational context.

## Step 5: Contradictions and Open Items

Preserve:
- conflicting views
- unresolved dependencies
- conditional commitments
- decisions awaiting another stakeholder
- follow-up evidence required

Do not flatten disagreement into false consensus.

## Step 6: Quotes

Use a direct quote only when its exact wording exists in the source. Keep quoted text brief and relevant. If exact wording cannot be verified, paraphrase without quotation marks.

## Output

```text
## Meeting Record

### Source / Coverage
[coverage state, source type, known date]

### Participants
[only participants supported by source; roles UNKNOWN when not stated]

### Executive Summary
[brief factual summary]

### Decisions
| Decision | Scope / Conditions | Evidence | Approver/Owner |

### Proposals / Discussion
[important items that were not decided]

### Action Items
| Action | Owner | Due Date | Status | Evidence |

### Open Questions / Blockers
[unresolved items]

### Disagreements / Caveats
[material dissent or conditions]

### Verified Quotes
[only when exact wording is supported]

### Follow-Up Needed
[missing owner/date/evidence or second decision needed]
```

## Final Self-Check

- Did I turn any proposal into a decision?
- Did I invent any owner or date?
- Did I treat silence as agreement?
- Are all quotes verifiable?
- Did I preserve material disagreement?
- Did I state coverage limitations?
