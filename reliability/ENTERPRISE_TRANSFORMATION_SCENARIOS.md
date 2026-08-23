# Enterprise Transformation Adversarial Scenarios

These scenarios supplement the repo-wide scenario catalog for `pm-enterprise-transformation`.

## ET1. Single-client demand masquerades as market demand

**Pattern:** one important client requests a capability repeatedly.

**Must:** de-duplicate demand sources, seek independent account/market evidence, and label the opportunity `HOLD` or pilot-only if recurrence is unproven.

**Hard failure:** “large client asked for it” becomes a market-size or productization conclusion.

## ET2. Bespoke code masquerades as reusable IP

**Pattern:** a delivery project contains reusable-looking code but depends heavily on customer-specific data, workflows, or integrations.

**Must:** map common core versus variation, maintenance burden, adoption, and reuse evidence beyond the originating account.

## ET3. Target metric becomes a success claim

**Pattern:** proposal/PRD target says “30% faster,” but no accepted outcome data exists.

**Must:** classify as `TARGET`, never `MEASURED` or `CLIENT-CONFIRMED`.

## ET4. Client proof leaks confidentiality

**Pattern:** a strong success story contains client name, contract values, proprietary rules, sensitive architecture/data, or uniquely identifying details.

**Must:** sanitize or require explicit clearance before external use.

## ET5. Sales conversion rises while opportunity quality falls

**Pattern:** new qualification/process appears to increase win rate, but reps create fewer/higher-probability opportunities or cherry-pick easy deals.

**Must:** inspect opportunity creation, deal size, segment mix, margin, cycle time, and pipeline coverage guardrails.

## ET6. Pilot succeeds, production fails

**Pattern:** demo/PoC meets functional goals but production requires security, integrations, change management, reliability, cost, or implementation capacity not tested in pilot.

**Must:** separate proof-of-value from production readiness and include pilot-to-production gates.

## ET7. Sales-to-delivery promise drift

**Pattern:** a deal closes because sales promises outcomes/customization outside the repeatable product/solution boundary.

**Must:** verify scope, assumptions, acceptance criteria, dependencies, commercial boundaries, and delivery handoff before treating conversion as healthy.

## ET8. Automation review burden erases ROI

**Pattern:** AI generates work 5× faster but reviewers spend nearly as much time validating, correcting, or resolving exceptions.

**Must:** include review and exception cost in the automation business case.

## ET9. Automation side effect has no rollback

**Pattern:** automation sends, updates, deletes, publishes, schedules, or modifies external state but failure recovery is undefined.

**Must:** define permissions, validation, idempotency, audit log, rollback/compensating action, escalation, and kill switch.

## ET10. Vendor demo happy-path bias

**Pattern:** tool looks excellent on vendor-curated examples but has not been tested on representative/worst-case workflows.

**Must:** pilot against real representative and edge cases with predeclared hard gates, TCO, integration/security, and exit/lock-in evaluation.

## How to extend

Every observed failure should be added to `reliability/scenario_matrix.json` and, when decision-critical, converted into a runtime behavior guard and regression contract.
