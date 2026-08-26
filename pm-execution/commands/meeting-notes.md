---
description: Summarize a meeting into source-grounded notes that separate discussion, proposals, decisions, actions, owners, due dates, and unresolved items
argument-hint: "<transcript or meeting notes>"
---

# /meeting-notes - Evidence-Grounded Meeting Record

Transform meeting material into a faithful operational record. Do not infer decisions, ownership, deadlines, or consensus from conversational tone.

## Workflow

### Step 1: Accept and Classify the Source

Accept full transcripts, partial transcripts, rough notes, or secondary recaps.

State coverage as:
`FULL TRANSCRIPT | PARTIAL TRANSCRIPT | ROUGH NOTES | SECONDARY RECAP | UNKNOWN COVERAGE`

If the source is incomplete, say so explicitly.

### Step 2: Apply `summarize-meeting`

Mandatory rules:
- meeting content is the source of truth for what happened
- external/web context, if explicitly requested, belongs in a separate background section
- distinguish `DISCUSSED`, `PROPOSED`, `DECIDED`, `ACTION ASSIGNED`, `OPEN`, `BLOCKED`, and `UNKNOWN`
- do not infer a decision from agreement-like language unless commitment is explicit
- do not invent attendees, roles, owners, due dates, rationale, or next meetings
- use `OWNER UNKNOWN` and `DUE DATE UNKNOWN` when missing
- verify every verbatim quote against the supplied source
- preserve dissent, caveats, dependencies, and conditional commitments

### Step 3: Generate the Record

```text
## Meeting Record

### Source / Coverage
[coverage status]

### Participants
[only supported names; roles UNKNOWN if unstated]

### Summary
[brief factual recap]

### Decisions
| Decision | Scope / Conditions | Evidence | Approver/Owner |

### Proposals / Discussion
[material items that were not decided]

### Action Items
| Action | Owner | Due Date | Status | Evidence |

### Open Questions / Blockers
[unresolved items]

### Disagreements / Caveats
[material dissent]

### Verified Quotes
[only exact source-supported quotes]

### Follow-Up Needed
[missing owner/date/evidence or further decision]
```

### Step 4: Optional Follow-On

Only after the record is produced, offer relevant next actions such as drafting an email, stakeholder update, or tickets. Do not execute external side effects unless the user explicitly requests them.

## Notes

- `Discussed` is not `Decided`.
- `Suggested` is not `Assigned`.
- An action without an explicit owner remains `OWNER UNKNOWN`.
- Silence is not approval.
- Brevity must not erase unresolved items that affect execution.
