---
name: competitive-battlecard
description: "Create evidence-backed sales-ready competitive battlecards while preserving upstream claim IDs, proof scope, freshness, attribution, confidentiality, and downstream restrictions. Use when preparing sales teams or responding to 'why not competitor X?'"
---

## Competitive Battlecard

Create a concise, current, evidence-backed battlecard for use against a specific competitor.

### Context

Research the competitor's current product, pricing, positioning, and recent changes. If the user provides feature lists, win/loss data, client proof, case studies, or internal notes, treat them as evidence to verify, not automatically as fact.

## Cross-Skill Lineage Consumer Contract

When upstream competitive research or client-proof/case-study assets provide claim IDs or a `Reliability Handoff`:

- preserve stable IDs for restated claims;
- preserve state, scope, source/freshness, attribution, publishability, caveats, and prohibited uses;
- do not convert a client-specific result into a universal competitive advantage;
- do not use `INTERNAL_ONLY`, `CLIENT_CONFIDENTIAL`, `REQUIRES_CLEARANCE`, or equivalent restricted proof in customer-facing talk tracks;
- a claim such as "we win for this ICP because..." is a new derived claim with parent IDs and should be no stronger than its evidence;
- competitor facts that have become stale stay `STALE` until refreshed;
- repeated claims across case studies, research, and sales notes do not count as independent corroboration;
- scope expansion requires a new derived claim, not reuse of the original claim ID.

## Evidence Rules

Classify important claims as:
- `VERIFIED / FACT`: current primary/credible evidence for the exact scoped fact
- `INTERNAL OBSERVATION`: supported by comparable win/loss or field evidence
- `INFERENCE`: reasoned but not directly verified
- `STALE`: evidence may no longer reflect current product
- `UNKNOWN`: insufficient evidence

Never invent competitor weaknesses, customer complaints, pricing, market share, or win/loss patterns to fill the template.

## Instructions

1. **Define competitive context**
   State target ICP, use case, buyer, geography, and deal context before declaring an advantage.

2. **Ingest inherited evidence**
   Read upstream handoff claims/restrictions before researching new evidence. Do not relabel inherited claims for convenience.

3. **Research current competitor evidence**
   - official product/docs/pricing
   - recent releases
   - target segment and messaging
   - integrations/security/implementation when material
   - independent reviews/community evidence as experience signals
   - internal verified win/loss evidence

   New evidence may support an explicit promotion only when scope/freshness are rechecked.

4. **Compare by decision criteria, not feature count**

   | Buyer criterion | Us | Them | Evidence claim IDs | Fit by segment |

   Avoid a generic `Winner` column when trade-offs depend on segment/context.

5. **Where we win**
   Every claim requires a mechanism, proof IDs, and target scope. If proof is missing, label it a positioning hypothesis.

6. **Where they win**
   State genuine strengths and preserve current evidence/freshness. Do not disguise competitor advantages as objection-handling opportunities.

7. **Qualification / disqualification**
   Define deals where we should pursue, where the competitor may be a better fit, and what evidence should be collected during discovery.

8. **Objections and responses**
   Responses must be truthful, specific, buyer-relevant, and use only claims allowed for the intended audience. Do not use unsupported TCO/ROI claims or restricted client proof.

9. **Competitive discovery questions**
   Ask neutral questions that surface decision criteria. Avoid manipulative landmines based on unverified deficiencies.

10. **Win/loss patterns**
    Only state patterns when enough comparable internal data exists. Include sample/time period/scope and confidence. A single client proof point is not a win/loss pattern.

## Contradiction Pass

Before delivery ask:
- Has the competitor shipped something that invalidates this card?
- Are we comparing list price to realized price?
- Are review complaints representative or anecdotes?
- Does our claimed advantage depend on services/custom work?
- Is the battlecard optimized to win bad-fit deals?
- Is a reference-client outcome being generalized beyond its scope?
- Is any proof restricted from external sales use?
- What would the competitor's best salesperson say is wrong with this card?

## Output

### One-Screen Rep Card
- ICP fit
- 3 decision criteria
- where we win with allowed proof claim IDs
- where they win
- discovery questions
- objections
- disqualifiers
- evidence freshness date

### Detailed Evidence Appendix

| Claim ID | Claim | State | Scope | Evidence | Freshness | Publishability | Allowed Use |

### Derived Competitive Claims

| Claim ID | Parent IDs | Derivation | Target Scope | State | Caveats |

### Reliability Handoff

```text
Coverage: COMPLETE FOR DECLARED SCOPE | PARTIAL | BLOCKED
Unresolved P0: [claim IDs]
Prohibited interpretations: [scope/confidentiality/causality limitations]
```

### Decision

`USE | USE WITH CAVEATS | REFRESH EVIDENCE | DO NOT USE`

Save as markdown and make it scannable during calls. Restating proof never strengthens it.

---

### Further Reading

- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
