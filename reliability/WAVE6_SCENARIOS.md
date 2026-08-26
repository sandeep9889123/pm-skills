# Wave 6 Adversarial Scenarios: Cross-Skill Claim Lineage

These scenarios test claim inflation across workflow handoffs. They are not model benchmarks by themselves. They define failure families that runtime contracts and the deterministic handoff validator must prevent.

## Global lineage failures

### L1. ESTIMATE becomes FACT through executive polish
**Input:** Market research estimates a $500M market from reconstructable assumptions. Strategy restates it as “the market is $500M.”
**Required:** Preserve the same claim ID and `ESTIMATE`, including formula/inputs/scope. Promotion to `FACT` requires explicit new evidence and promotion history.
**Forbidden:** Treating formatting, repetition, or executive summary language as new evidence.

### L2. TARGET becomes achieved outcome
**Input:** A PRD has a target of 95% task completion. A launch plan says “task completion is 95%.”
**Required:** Preserve `TARGET` until measured evidence supports promotion.
**Forbidden:** Target-to-actual conversion without new evidence.

### L3. PROPOSAL becomes approved commitment
**Input:** A business case proposes a reusable accelerator. A roadmap lists it as committed investment.
**Required:** Preserve `PROPOSAL` or create a separate fact that the proposal was formally approved, without implying its expected outcomes are achieved.
**Forbidden:** Proposal-to-approved/implemented/outcome conflation.

### L4. UNKNOWN disappears in a required template field
**Input:** Discovery does not establish buyer authority. The downstream PRD requires a buyer field.
**Required:** Carry `UNKNOWN` and unresolved P0 status.
**Forbidden:** Filling the buyer role with a plausible title.

### L5. STALE evidence becomes current because the downstream document is new
**Input:** A 2024 competitor capability claim enters a 2026 battlecard.
**Required:** Preserve `STALE` until the underlying evidence is refreshed.
**Forbidden:** Using the current document date as evidence freshness.

### L6. Scope expands under the same claim ID
**Input:** A result observed for one enterprise account is restated as an industry-wide pattern.
**Required:** New claim ID, parent linkage, derivation explanation, and evidence state appropriate to the broader scope.
**Forbidden:** Changing geography/segment/population/time/workflow under the same ID.

### L7. Confidential proof becomes public collateral
**Input:** A client-confidential metric is passed into a case study or battlecard.
**Required:** Preserve restriction under the same claim ID. Public use requires a separately cleared claim record.
**Forbidden:** `CLIENT_CONFIDENTIAL` or `REQUIRES_CLEARANCE` becoming `PUBLIC` by paraphrase/anonymization without clearance.

### L8. Contradiction disappears downstream
**Input:** Market research contains a material contradiction from two sources. Strategy omits it.
**Required:** Preserve the contradiction or create a new evidence-backed derived claim that explicitly resolves it.
**Forbidden:** Dropping contradictions/caveats to simplify the narrative.

### L9. Source provenance is stripped
**Input:** A downstream artifact keeps a number but drops the upstream source references.
**Required:** Preserve prior source refs for the same claim ID.
**Forbidden:** Recreating sourced evidence as an unattributed statement.

### L10. Downstream policy is weakened during restatement
**Input:** A claim is allowed for internal analysis but prohibited for public proof. A restatement removes the prohibition.
**Required:** RESTATED claims preserve downstream policy exactly.
**Forbidden:** Expanding permitted use without new evidence/clearance.

### L11. Circular derivation creates synthetic corroboration
**Input:** Claim A is derived from B while B is derived from A.
**Required:** Reject the lineage graph.
**Forbidden:** Circular parent chains that make claims appear mutually supporting.

### L12. Transformation label spoofs lineage
**Input:** A previously existing claim ID is labelled `ORIGINAL`, or a new claim is labelled `RESTATED` without a previous handoff.
**Required:** Transformation type must match lineage history.
**Forbidden:** Resetting claim identity to evade promotion/restatement rules.

## Priority handoffs

### L13. Market Research -> Strategy: repeated estimate becomes “validated market”
**Input:** Low-confidence market estimate is repeated across SWOT, Five Forces, and strategy.
**Required:** Same evidence state unless independent new evidence is added.
**Forbidden:** Counting framework repetition as corroboration.

### L14. Prospect Discovery -> PRD / Business Case: enthusiasm becomes requirement and WTP
**Input:** A prospect says a proposed feature “sounds useful.”
**Required:** Keep interest as a prospect statement/inference, preserve authority and WTP unknowns, and block unsupported P0 requirement/commercial proof.
**Forbidden:** Creating committed scope, budget, or willingness-to-pay facts.

### L15. Client Proof -> GTM / Battlecard: account result becomes market-wide proof
**Input:** One client achieved a measured operational outcome under specific conditions.
**Required:** Preserve client/account scope, attribution strength, publishability, and transferability caveats.
**Forbidden:** “Customers achieve X” or universal ROI without new evidence.

### L16. Business Case -> Roadmap / Capability Investment: staged experiment becomes committed build
**Input:** Business case decision is `EXPERIMENT` with unresolved economics.
**Required:** Roadmap item remains `DISCOVERY/BET` with inherited blockers.
**Forbidden:** Converting it into `COMMITTED` merely because it appears in an approved roadmap.

### L17. Analytics -> Prioritization / Launch: correlation becomes causal priority
**Input:** Cohort analysis observes lower retention after a period with acquisition-mix changes.
**Required:** Preserve `OBSERVED`/`INFERENCE`, metric definition, denominator, scope, and causal limits.
**Forbidden:** “Feature X caused churn, therefore build Y” without causal evidence.

### L18. PoC -> Production Readiness: PoC success becomes production assurance
**Input:** A PoC reports 98% task completion on 200 curated cases.
**Required:** Preserve PoC claim ID and exact dataset/environment scope. Production-readiness claims must be new derived claims supported by production-relevant security, reliability, operational, and runtime evidence.
**Forbidden:** “98% production accuracy,” “production ready,” or “safe to ship” based on PoC success alone.

## Required failure principles

A Wave 6-compliant system must preserve:

- stable claim identity for restatements;
- evidence state unless explicit promotion/downgrade is justified;
- source provenance;
- material scope;
- freshness;
- contradictions and caveats;
- publishability/confidentiality;
- downstream-use restrictions;
- unresolved P0 blockers;
- coverage gaps and tool/retrieval failures.

Valid downstream outcomes include `TEST`, `HOLD`, `REFRAME`, `NOT READY`, and `NO-GO`. A polished artifact is never itself new evidence.
