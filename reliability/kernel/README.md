# Reliability Kernel

The Reliability Kernel is the shared control plane for the PM Skills repository.

It exists so reliability does not depend on every individual `SKILL.md` repeating the same long instructions.

## Assets

- [`RELIABILITY_KERNEL.md`](RELIABILITY_KERNEL.md): normative context, evidence, contradiction, lineage, decision, and admission rules.
- [`risk_tiers.json`](risk_tiers.json): complete P0/P1/P2 classification of all 96 skills and 55 workflows.
- [`context_frame.schema.json`](context_frame.schema.json): portable decision-context contract.
- [`claim_lineage.schema.json`](claim_lineage.schema.json): portable evidence/claim handoff contract.
- [`../../docs/audit/RELIABILITY_RISK_MAP_V1.md`](../../docs/audit/RELIABILITY_RISK_MAP_V1.md): audit summary and Wave 5-7 hardening priorities.
- [`../../tests/test_reliability_kernel.py`](../../tests/test_reliability_kernel.py): CI invariants preventing classification and kernel drift.

## Core rule

`Context → Evidence → Challenge → Decision → Lineage → Evaluation`

The kernel does not guarantee that an LLM will never hallucinate. It makes common reliability failures explicit and testable:

- unsupported facts;
- weak first-pass negative conclusions;
- stale evidence presented as current;
- tool failure presented as real-world absence;
- generic advice that ignores market/stage/audience context;
- forced template completion;
- targets or estimates promoted into achievements/facts;
- PoC evidence promoted into production readiness;
- internal/confidential proof promoted into public sales claims;
- downstream workflows dropping uncertainty from upstream work.

## Risk tiers

### P0

Decision-critical. Full applicable kernel, runtime hardening, and behavioral evaluation plan required.

### P1

Context-sensitive. Context resolution, anti-invention, evidence-vs-hypothesis separation, material assumptions, and relevant contradiction checks required.

### P2

Low-risk transformation. Preserve intent, do not invent, flag substantive ambiguity.

## Adding or changing a skill

1. Classify it in `risk_tiers.json`.
2. Identify applicable plugin scenarios in `../scenario_matrix.json`.
3. Apply the tier controls.
4. For P0, define hard failures and behavioral evaluation coverage.
5. Preserve claim states at workflow handoffs.
6. Run repository CI.

A new artifact that is not classified should fail `tests/test_reliability_kernel.py`.
