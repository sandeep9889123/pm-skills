---
name: test-scenarios
description: "Create evidence-grounded test scenarios from user stories, requirements, or intended behavior without inventing product rules. Separates specified expectations from inferred risks, identifies specification gaps, and covers failure paths proportionally. Use for QA plans, acceptance tests, UAT, and feature validation."
---

# Evidence-Grounded Test Scenarios

## Purpose

Convert intended behavior into executable test scenarios while preserving the boundary between **what the product is specified to do** and **what the tester thinks it might reasonably do**.

A test suite must not create product requirements by accident.

## P0 Reliability Contract

1. Never invent expected behavior, thresholds, card counts, timeout limits, timestamps, status transitions, permissions, copy, data rules, or performance targets that are not in the supplied requirements or authoritative source.
2. Classify each expected behavior as `SPECIFIED`, `INFERRED TEST RISK`, `UNKNOWN / SPEC GAP`, or `NON-FUNCTIONAL REQUIREMENT PROVIDED`.
3. An `INFERRED TEST RISK` may justify a test exploration, but it must not be written as a pass/fail oracle until the product owner/requirement source confirms the expected behavior.
4. Missing acceptance criteria become `SPEC GAP`, not fabricated expected results.
5. Every pass/fail test must trace to a requirement, business rule, contract, documented system behavior, or explicitly approved test oracle.
6. Do not assume authentication, role permissions, tenancy, retry behavior, error copy, browser/device support, accessibility level, latency target, rate limit, or data retention unless supplied.
7. For high-risk flows, include failure, permission, recovery, concurrency/idempotency, data-integrity, and dependency-error paths where applicable.
8. Do not call coverage `comprehensive` when source requirements are incomplete or code/runtime paths were not inspected.
9. Tool/file access failure means `COVERAGE INCOMPLETE`.
10. Unknown behavior must be resolved before the corresponding scenario can be used as a release gate.

## Step 1: Build the Requirement Inventory

Capture:
- source artifact / user story / PRD / API contract
- requirement ID or traceable statement
- actor/role if specified
- preconditions
- expected behavior
- explicit non-functional requirements
- acceptance criteria
- known exclusions

Create a requirement state:
`SPECIFIED | AMBIGUOUS | MISSING | CONTRADICTED`

## Step 2: Identify Specification Gaps

Before generating tests, list gaps that would change the expected result, for example:
- undefined role/permission
- ambiguous status transition
- missing empty-state behavior
- unclear timeout/retry behavior
- undefined error response
- no data-retention rule
- no performance threshold

Do not choose a plausible answer. Mark `SPEC GAP` and identify the decision owner if known.

## Step 3: Derive Test Families

For each specified requirement consider relevant families:

### Functional happy path
Validate the explicitly intended flow.

### Boundary / validation
Only when input ranges or rules are known. If boundaries are not specified, create a discovery question rather than a pass/fail expectation.

### Failure / dependency
Network errors, downstream failure, timeout, partial failure, retries, cancellation, or degraded service when applicable.

### Authorization / tenancy
Role, object ownership, tenant isolation, escalation, or unauthorized access only when the system has such boundaries.

### Data integrity / state
Duplicate submission, stale state, concurrent updates, idempotency, partial write, rollback, resume/retry where relevant.

### Non-functional
Performance, accessibility, compatibility, reliability, security, observability only when requirement/standard or risk context exists. Do not invent numeric targets.

## Step 4: Define Test Oracle

Every executable scenario must state:
- requirement/source
- precondition
- action
- expected observable result
- postcondition
- evidence needed

If the expected result is unknown, set:

`BLOCKED BY SPEC GAP: [question]`

Do not silently convert a hypothesis into the expected result.

## Step 5: Traceability and Coverage

Create:

| Requirement | Requirement State | Scenarios | Failure Paths | Coverage Status |
|---|---|---|---|---|

Coverage states:
`COVERED | PARTIAL | BLOCKED BY SPEC GAP | NOT APPLICABLE | NOT ASSESSED`

A requirement is not `COVERED` merely because a scenario title exists. The oracle must be executable and grounded.

## Step 6: Prioritize by Risk

Prioritize scenarios by:
- customer/business consequence
- security/privacy/data integrity
- irreversible side effects
- frequency/core-flow importance
- likelihood of regression
- complexity/dependency exposure

Avoid arbitrary priority labels with no rationale.

## Output Template

```text
## Test Scenario: [name]

Requirement source: [ID / quote / section]
Requirement state: SPECIFIED | AMBIGUOUS | MISSING | CONTRADICTED
Test objective: [what is validated]
Preconditions: [known setup]
Actor: [specified role or UNKNOWN]

| Step | Action | Expected Result | Oracle Source |

Postconditions: [known expected state]
Priority: [with rationale]
Coverage status: COVERED | PARTIAL | BLOCKED BY SPEC GAP | NOT ASSESSED
```

Then provide:

### Specification Gaps
[questions that block executable tests]

### Coverage Matrix
[requirement to scenario traceability]

### Test Data Requirements
[only requirements grounded in scenarios]

### Failure-Path Coverage
[what was tested vs not assessed]

## Hard Failures

Do not call the suite release-ready when:
- material requirements are missing/contradicted
- critical expected outcomes are invented
- security/permission boundaries are unknown for a sensitive flow
- irreversible failure/recovery paths are untested
- source coverage is incomplete but output claims completeness

## Final Self-Check

- Did I invent any expected behavior?
- Does every pass/fail oracle trace to a source?
- Did I convert missing requirements into questions instead of guesses?
- Did I include failure paths proportional to risk?
- Did I distinguish `PARTIAL` from `COVERED`?
