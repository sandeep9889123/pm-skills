# Reliability Risk Map V1

## Executive summary

The repository currently contains **96 skills and 55 workflows across 12 plugins**.

Wave 4 classifies every artifact by the consequence of a confidently wrong output:

| Artifact | P0 decision-critical | P1 context-sensitive | P2 low-risk transformation | Total |
|---|---:|---:|---:|---:|
| Skills | 65 | 28 | 3 | 96 |
| Workflows | 45 | 9 | 1 | 55 |
| **Total** | **110** | **37** | **4** | **151** |

The machine-readable source of truth is [`reliability/kernel/risk_tiers.json`](../../reliability/kernel/risk_tiers.json).

This classification is intentionally conservative. A skill is P0 when an unsupported fact, hidden assumption, stale claim, bad quantitative conclusion, confidentiality leak, or unsafe external recommendation could materially alter a product, customer, commercial, legal/privacy, production, or investment decision.

## Why this exists

The repository had already hardened a meaningful set of high-risk primitives and introduced adversarial scenario coverage. The remaining risk was **coverage drift**:

- new skills could be added without an explicit reliability tier;
- a command could weaken a hardened skill;
- one workflow could silently promote an upstream `ESTIMATE` into a downstream `FACT`;
- a target could become an achieved client outcome;
- a stale source could become a current strategy input;
- a tool failure could become a negative market conclusion.

The Reliability Kernel converts these into repository-level invariants rather than relying on prompt-author memory.

## Plugin distribution

| Plugin | Skill P0/P1/P2 | Workflow P0/P1/P2 | Reliability implication |
|---|---:|---:|---|
| pm-product-discovery | 6 / 7 / 0 | 4 / 1 / 0 | experiments, interviews, prioritization and metrics need stronger proof discipline |
| pm-prospect-discovery | 10 / 0 / 0 | 4 / 0 / 0 | all outputs can change enterprise opportunity scope/readiness |
| pm-product-strategy | 5 / 7 / 0 | 4 / 1 / 0 | investment/economic strategy is P0; framing frameworks are mostly P1 |
| pm-execution | 7 / 7 / 2 | 7 / 4 / 0 | commitments, PRDs, risk and decision records are P0 |
| pm-market-research | 6 / 1 / 0 | 3 / 0 / 0 | factual market/user claims are predominantly P0 |
| pm-data-analytics | 3 / 0 / 0 | 3 / 0 / 0 | quantitative errors can directly reverse decisions |
| pm-go-to-market | 5 / 1 / 0 | 3 / 0 / 0 | ICP, beachhead, motion and competitive claims affect real pipeline spend |
| pm-marketing-growth | 1 / 4 / 0 | 1 / 1 / 0 | North Star is P0; most creative positioning work is P1 |
| pm-toolkit | 2 / 1 / 1 | 2 / 2 / 1 | legal/privacy work is P0; pure proofreading is P2 |
| pm-ai-shipping | 2 / 0 / 0 | 5 / 0 / 0 | shipping/security evidence is P0 |
| pm-enterprise-transformation | 12 / 0 / 0 | 4 / 0 / 0 | capability investment, client claims, sales and automation decisions are P0 |
| pm-business-case | 6 / 0 / 0 | 5 / 0 / 0 | investment decisions are P0 by definition |

## Tier definitions

### P0: decision-critical

Required behavior, where applicable:

- resolve decision context before precision;
- preserve evidence states and source precedence;
- check freshness;
- seek disconfirming evidence / alternative hypotheses;
- fail closed on tool/retrieval failure;
- earn negative conclusions;
- preserve claim lineage across downstream workflows;
- define hard gates and change-my-mind evidence;
- have a behavioral evaluation plan.

### P1: context-sensitive

Required behavior:

- resolve material context;
- do not invent supporting evidence;
- label hypotheses and assumptions;
- preserve user intent;
- challenge material framing when needed;
- avoid generic one-size-fits-all output.

### P2: low-risk transformation

Required behavior:

- preserve meaning;
- do not invent facts;
- flag ambiguity that would change the requested transformation.

## Current strength

The repo already has deep contracts around several high-risk families, including competitor analysis, market sizing, personas, interview evidence, A/B analysis, product strategy, pricing, PRDs, enterprise GTM, battlecards, prioritization, North Star metrics, roadmaps, stakeholders, pre-mortems, experiments, segmentation, enterprise transformation, business cases, and prospect discovery.

This is **partial P0 deep coverage**, not universal P0 coverage.

Wave 4 therefore adds a repository admission gate: every current and future skill/workflow must be classified. Wave 5 expands runtime hardening and golden behavioral cases across the remaining P0 surface.

## Wave 5 priority order

Priority is based on expected frequency × consequence × current reliability gap × downstream propagation.

### Wave 5A: evidence and quantitative decision primitives

1. `pm-market-research/market-segments`
2. `pm-market-research/sentiment-analysis`
3. `pm-data-analytics/cohort-analysis`
4. `pm-data-analytics/sql-queries`
5. `pm-product-discovery/interview-script`
6. `pm-product-discovery/metrics-dashboard`
7. their high-consequence command/workflow wrappers

Focus:

- sample/source representativeness;
- selection bias;
- taxonomy/segment stability;
- denominator and event-definition correctness;
- SQL schema/table/column invention;
- causal vs descriptive interpretation;
- leading/loaded interview questions;
- metric definitions and Goodhart/vanity risk.

### Wave 5B: enterprise strategy and GTM

1. `pm-product-strategy/business-model`
2. `pm-product-strategy/monetization-strategy`
3. `pm-product-strategy/porters-five-forces`
4. `pm-go-to-market/ideal-customer-profile`
5. `pm-go-to-market/beachhead-segment`
6. `pm-go-to-market/gtm-motions`
7. their command/workflow wrappers

Focus:

- evidence-backed revenue/cost assumptions;
- WTP and value-capture uncertainty;
- current market-structure freshness;
- buyer/user/champion distinction;
- anti-ICP and disqualifiers;
- beachhead concentration vs TAM attractiveness;
- motion economics and implementation/production path.

### Wave 5C: operational truth and red-team integrity

1. `pm-execution/strategy-red-team`
2. `pm-execution/summarize-meeting`
3. `pm-execution/test-scenarios`
4. `pm-enterprise-transformation/account-expansion-play`
5. selected AI-shipping workflows that can convert incomplete inspection into a clean readiness claim

Focus:

- do not manufacture objections when evidence holds;
- decisions vs discussion vs proposals vs unresolved items;
- quote/owner/date integrity;
- failure-path coverage;
- account expansion proof vs relationship optimism;
- audit coverage incomplete must not become safe/ready.

## Wave 6: cross-skill lineage

The largest systemic risk is not a single hallucination. It is **claim inflation across a workflow**.

Example:

`Market research: ESTIMATE, low confidence`

→ `Strategy: market is $500M`

→ `Business case: $500M FACT`

→ `GTM: target the proven $500M market`

Wave 6 will make lineage portable across major handoffs using [`claim_lineage.schema.json`](../../reliability/kernel/claim_lineage.schema.json) and require downstream workflows to preserve uncertainty until stronger evidence explicitly promotes the claim.

Priority handoffs:

1. Market Research → Product Strategy
2. Prospect Discovery → PRD / Proposal / Business Case
3. Client Proof → Case Study → GTM / Battlecard
4. Business Case → Roadmap / Capability Investment
5. Analytics → Prioritization / Launch Decision
6. PoC → Production Readiness

## Wave 7: behavioral coverage

The benchmark should evolve from a small set of exemplar cases into representative P0 decision families.

For each major P0 family:

- frozen first-run case;
- at least one mutated edge case;
- deterministic catastrophic hard gates where feasible;
- 100-point rubric for nuanced reasoning;
- repeated fresh-session runs for model comparisons when practical;
- failure-rate reporting, not only average score.

The benchmark is evidence about tested behavior. It is not a guarantee of hallucination-free behavior outside the test distribution.

## Admission rule

From Wave 4 onward, a new skill/workflow is incomplete unless it:

1. appears in `risk_tiers.json`;
2. inherits plugin adversarial scenarios;
3. defines P0 hard failures/evaluation plan when applicable;
4. preserves evidence states across handoffs;
5. passes repository CI.

This is the key architectural change: reliability becomes a property of the repository, not a one-time prompt-writing exercise.
