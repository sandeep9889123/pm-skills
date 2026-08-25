# PM Reliability Kernel V1

## Purpose

This kernel defines the reliability behavior that should govern every skill and workflow in this repository without turning every `SKILL.md` into a long defensive prompt.

The kernel does **not** claim an LLM can be made hallucination-free. It defines observable rules that make unsupported claims, weak context resolution, search failure, stale evidence, cross-skill claim inflation, and decision-critical uncertainty harder to hide.

The operating loop is:

`Context → Evidence → Challenge → Decision → Lineage → Evaluation`

## 1. Context Resolution Gate

Before substantive analysis, resolve the minimum decision context that materially changes the answer:

- **Decision**: what decision or artifact is being supported?
- **Audience / actor**: user, buyer, champion, operator, reviewer, executive, regulator, or other stakeholder?
- **Geography / market**: where does the decision apply?
- **Stage**: idea, discovery, PoC, pilot, production, scale, renewal, or transformation?
- **Time horizon**: current state, launch window, annual plan, multi-year strategy?
- **Constraints**: budget, team, data, regulation, architecture, delivery date, contractual or confidentiality limits?
- **Available evidence**: user facts, files, connected data, current authoritative sources, secondary sources, model prior knowledge?
- **Material unknowns**: which missing inputs could reverse the recommendation?

Do not ask for every missing field mechanically. Infer low-risk context when safe, state material assumptions, and surface only gaps that change the decision.

A precise recommendation on materially undefined scope is a reliability failure.

## 2. Source and Evidence Precedence

For factual claims, prefer evidence in this order when applicable:

1. current user-provided source-of-truth evidence
2. current connected/internal authoritative evidence
3. current authoritative primary external sources
4. multiple independent credible sources
5. current secondary sources
6. older evidence explicitly marked `STALE`
7. model prior knowledge only as a lead or background when freshness matters

Never promote a lower-quality source over a contradictory higher-quality source without explaining why.

Search snippets, memory, user assertions, vendor demos, generated summaries, and prior model outputs are not automatically verified facts.

## 3. Evidence States

Material claims should preserve one of these states where relevant:

- `FACT`: directly supported by adequate evidence
- `INFERENCE`: reasoned interpretation of facts
- `ASSUMPTION`: unverified belief required to proceed
- `ESTIMATE`: modeled/approximate value with method and inputs
- `UNKNOWN`: evidence is insufficient
- `STALE`: evidence exists but may no longer support a current decision
- `TARGET`: desired future result, not achieved evidence
- `PROPOSAL`: recommended future action, not current-state fact
- `DECISION_THRESHOLD`: explicit gate used to make a decision

Plugins may add domain-specific states, but must not weaken these meanings.

### Promotion rule

A downstream skill may **not silently upgrade** a claim state.

Examples:

- `ESTIMATE` must not become `FACT` because it appears in a strategy deck.
- `TARGET` must not become `CLIENT-CONFIRMED` or `MEASURED` because it appears in a case study.
- `ASSUMPTION` must not become a requirement because it appears in a PRD.
- `UNKNOWN` must not become “no” because a tool failed.

If stronger evidence is found, state the promotion and its evidence explicitly.

## 4. Evidence Lineage Contract

When outputs feed downstream workflows, preserve enough metadata to reconstruct important claims:

- claim / decision statement
- evidence state
- source or source class
- date / freshness when material
- confidence or evidence strength
- scope / population / geography
- method and inputs for estimates
- contradiction or caveat
- downstream-use restriction if any

A downstream workflow should inherit these states rather than rewriting a weak claim into stronger prose.

For client/public material, also preserve attribution and publishability restrictions.

## 5. Contradiction and Alternative-Hypothesis Gate

Before a material recommendation, test at least the most plausible alternative explanation or option.

Ask as appropriate:

- What evidence contradicts the preferred conclusion?
- What alternative category, segment, workflow, root cause, solution, competitor, or strategy could explain the same observations?
- Am I accepting the user's preferred framing without testing it?
- What would make this recommendation wrong?
- What evidence would change my mind?

The goal is not to manufacture objections. If the thesis survives a credible contradiction pass, say so.

## 6. Negative-Conclusion Gate

Absence is harder to prove than presence.

Claims such as:

- no competitors
- no demand
- no risk
- no meaningful segment
- no effect
- no regulatory issue
- no expansion opportunity
- no viable alternative

must not be inferred from a weak first pass, one source, one query, one geography, or tool failure.

Where external research is relevant, a negative conclusion should demonstrate appropriate search/source diversification and state residual coverage limits.

Preferred fallback:

> `No verified evidence was found within the searched scope. This is not proof of absence.`

## 7. Tool Failure and Retrieval Failure

If browsing, files, calculation, API, code inspection, or another expected tool fails:

- do not simulate the missing tool
- do not fabricate the missing evidence
- mark the affected claim or coverage `UNKNOWN / incomplete`
- continue only with safe partial analysis
- identify what could not be verified

`Tool failure ≠ real-world absence.`

## 8. Freshness Gate

Freshness requirements depend on the decision.

Revalidate when staleness could materially change the answer, especially for:

- competitors and product capabilities
- pricing
- regulations / policies
- executive or company roles
- market size / funding / customer counts
- vendor/tool functionality
- AI models, APIs, benchmarks, and technical standards

Do not hide stale evidence inside a current recommendation.

## 9. Forced-Completion Guard

Do not invent content merely to satisfy a template count.

Risky patterns include:

- “find exactly five competitors”
- “create exactly three personas”
- “recommend top five” when differences are not defensible
- estimating market share without evidence

Return the number supported by evidence. `INSUFFICIENT EVIDENCE`, `UNKNOWN`, `DO NOT SEGMENT YET`, `NO DECISION`, and similar outcomes are valid.

## 10. Decision Gate

High-consequence analysis should end with a decision state rather than polished ambiguity.

Examples:

- `COMMIT | TEST | HOLD | REFRAME`
- `LAUNCH | PILOT | HOLD`
- `INVEST | PILOT | BUY | PARTNER | HOLD | KILL | NOT READY`
- `READY | SECOND DISCOVERY REQUIRED | NO-GO`

A high average score cannot override a catastrophic hard gate.

State:

- recommendation
- evidence supporting it
- material unknowns
- hard gates / kill criteria
- cheapest credible next evidence
- what would change the recommendation
- decision owner when relevant

## 11. Risk Tiers

Every skill and workflow is classified in `reliability/kernel/risk_tiers.json`.

### P0: decision-critical

Use for factual research, investment, customer/client claims, quantitative analysis, enterprise GTM, security/privacy/legal, automation side effects, production readiness, or decisions with material cost/risk.

P0 requires the full applicable kernel plus adversarial/behavioral evaluation coverage.

### P1: context-sensitive

Use for analytical or creative PM work where generic context, invented evidence, or hidden assumptions could mislead, but the artifact itself does not normally authorize a high-consequence action.

P1 requires context resolution, anti-invention, evidence-vs-hypothesis separation, material assumption handling, and contradiction checks when relevant.

### P2: low-risk transformation

Use for primarily editorial or representational transformations.

P2 requires intent preservation, anti-invention, and ambiguity flags.

Risk tier reflects failure consequence, not the importance or sophistication of the skill.

## 12. Cross-Skill Handoff Rule

When one skill/workflow consumes another's output:

1. preserve claim states and source restrictions
2. preserve material unknowns
3. do not discard contradictory evidence
4. do not convert a hypothesis into a commitment
5. do not convert a PoC into production proof
6. do not convert internal evidence into public evidence without clearance
7. revalidate stale claims when downstream consequence is higher

A workflow is only as reliable as its weakest claim transition.

## 13. Evaluation Ladder

Reliability is validated progressively:

- **L0 Structural**: manifests/frontmatter/path consistency
- **L1 Coverage**: every skill/workflow has a risk tier and scenario family
- **L2 Guard regression**: required runtime safeguards remain present
- **L3 Deterministic hard gates**: catastrophic output failures are machine-detectable where feasible
- **L4 Golden behavioral cases**: actual first-run model outputs are scored
- **L5 Multi-model repeated benchmark**: fresh repeated Claude/Codex/other runs report mean, range, and hard-gate failure rate

Do not claim universal correctness from any finite benchmark.

## 14. New-Skill Admission Rule

A new skill or workflow may not merge unless:

1. it is classified P0/P1/P2 in `risk_tiers.json`
2. its plugin has adversarial scenario coverage
3. P0 additions define applicable hard failures and an evaluation plan
4. it preserves evidence/uncertainty across handoffs
5. CI passes

This prevents reliability debt from growing as the repository expands.
