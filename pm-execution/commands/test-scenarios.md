---
description: Generate traceable test scenarios from requirements without inventing product behavior, thresholds, permissions, or pass/fail expectations
argument-hint: "<user stories, feature spec, or description>"
---

# /test-scenarios - Evidence-Grounded Test Scenario Generator

Turn requirements into QA/UAT scenarios while keeping unknown product behavior explicit. A test scenario must not become an accidental requirements document.

## Workflow

### Step 1: Accept and Inventory Requirements

Accept user stories, acceptance criteria, PRD sections, feature specs, API contracts, or documented intended behavior.

For each material requirement classify:
`SPECIFIED | AMBIGUOUS | MISSING | CONTRADICTED`

If only a one-line feature description is supplied, do not pretend the full expected behavior is known.

### Step 2: Apply `test-scenarios`

Mandatory rules:
- never invent expected behavior, numeric thresholds, counts, timestamps, error copy, permissions, retry rules, browser support, performance targets, or state transitions
- every pass/fail oracle must trace to a supplied/authoritative requirement
- inferred risks may produce exploratory tests but not invented pass/fail expectations
- unresolved behavior becomes `SPEC GAP`
- include failure, permission, recovery, concurrency/idempotency, data-integrity, and dependency paths when applicable to the risk
- source/tool access failure means `COVERAGE INCOMPLETE`
- do not call coverage comprehensive when requirements or implementation paths were not fully assessed

### Step 3: Generate Scenarios

```text
## Test Scenarios: [Feature]

### Source Coverage
[requirements inspected and limitations]

### Specification Gaps
| Gap | Why It Changes Expected Behavior | Owner/Source Needed | Status |

### Scenario: [Title]
Requirement source: [ID / section / exact supplied behavior]
Requirement state: SPECIFIED | AMBIGUOUS | MISSING | CONTRADICTED
Objective: [what is validated]
Preconditions: [specified or UNKNOWN]
Actor: [specified or UNKNOWN]

| Step | Action | Expected Result | Oracle Source |

Postconditions: [specified or UNKNOWN]
Coverage status: COVERED | PARTIAL | BLOCKED BY SPEC GAP | NOT ASSESSED
Priority: [risk rationale]

### Coverage Matrix
| Requirement | State | Happy Path | Failure/Edge | Security/Permission | Recovery/Data Integrity | Coverage |

### Test Data Requirements
[grounded in executable scenarios]

### Not Assessed
[paths or environments outside current evidence]
```

If expected behavior is unknown, write:

`BLOCKED BY SPEC GAP: [specific decision/question]`

rather than choosing a plausible expected result.

### Step 4: Release-Readiness Gate

Do not describe the suite as release-ready when material requirements are missing/contradicted, critical oracles are invented, or high-consequence failure paths remain `NOT ASSESSED`.

Valid outcomes:
`READY FOR EXECUTION | PARTIAL COVERAGE | BLOCKED BY SPEC GAPS | COVERAGE INCOMPLETE`

## Notes

- Happy paths do not have automatic priority over catastrophic failure paths.
- An edge case without a defined expected outcome is a specification question, not an executable test.
- Traceability matters more than scenario count.
