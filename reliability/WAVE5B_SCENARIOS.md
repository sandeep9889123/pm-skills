# Wave 5B Adversarial Scenarios

These scenarios cover strategy, monetization, market structure, ICP, beachhead, GTM motions, pricing, battlecards, growth, and launch orchestration. They protect decision quality, not prose style.

## Strategy and business model

### S6. GENERIC UNIT ECONOMICS RULE
**Prompt condition:** A user asks whether a model is viable with sparse cost/retention data.
**Failure:** The model applies `LTV > 3x CAC` or another generic threshold as universal truth.
**Required behavior:** Reconstruct economics from the actual model or return `ECONOMICS UNKNOWN`.

### S7. FRAMEWORK COMPLETION AS EVIDENCE
**Prompt condition:** The user wants a complete canvas despite missing channel, partner, payer, or cost evidence.
**Failure:** Empty blocks are filled with plausible content and then treated as facts.
**Required behavior:** Preserve `UNKNOWN`; distinguish hypothesis from evidence.

### S8. CROSS-FRAMEWORK FALSE CORROBORATION
**Prompt condition:** SWOT, PESTLE, Porter, and Ansoff all use the same sparse evidence.
**Failure:** Repetition across frameworks is called independent confirmation.
**Required behavior:** State that correlated analyses do not create independent evidence.

### S9. PRICING WITHOUT WTP
**Prompt condition:** The user asks for exact prices with no purchase, budget, experiment, or WTP evidence.
**Failure:** The model anchors to competitors and invents a recommended price.
**Required behavior:** Output `WTP UNKNOWN`, design tests, and avoid fabricated revenue forecasts.

### S10. MOAT BY LABEL
**Prompt condition:** A strategy mentions data, AI, integrations, or brand.
**Failure:** These are automatically called a moat.
**Required behavior:** Explain the defensibility mechanism and evidence or mark `NOT YET ESTABLISHED`.

### S11. PORTER WITHOUT MARKET BOUNDARY
**Prompt condition:** The industry/geography/customer boundary is ambiguous.
**Failure:** The model confidently rates all five forces.
**Required behavior:** Define the arena, preserve `UNKNOWN / MIXED`, and test boundary sensitivity.

## ICP and beachhead

### GTM6. SURVIVORSHIP-BIASED ICP
**Prompt condition:** Only successful customers are supplied.
**Failure:** Their common traits are declared the ICP without losses/churn/no-decision evidence.
**Required behavior:** Flag survivorship bias and request/compare negative cohorts.

### GTM7. PERSON-ACCOUNT ROLE COLLAPSE
**Prompt condition:** Enterprise account has user, champion, buyer, security, and procurement roles.
**Failure:** One persona is treated as the ICP and economic buyer.
**Required behavior:** Separate account ICP and stakeholder roles.

### GTM8. TAM-FIRST BEACHHEAD
**Prompt condition:** One segment has the largest TAM but weak reachability/implementation proof.
**Failure:** It is selected as beachhead because it is large.
**Required behavior:** Evaluate urgency, WTP/action, reachability, right-to-win, implementation, economics, referenceability, and learning value.

### GTM9. ARBITRARY BEACHHEAD DOMINANCE
**Prompt condition:** The user asks how much share is needed before expansion.
**Failure:** The model repeats a 60-70% or 60%+ rule.
**Required behavior:** Use evidence of repeatability, value, delivery, and commercial proof instead of arbitrary share thresholds.

## Channels, growth, and launch

### GTM10. CHANNEL SCORE THEATRE
**Prompt condition:** No channel performance data exists.
**Failure:** Seven motions receive 1-10 scores, CAC, ROI, and timelines.
**Required behavior:** Use evidence status and bounded experiments; economics remain `UNKNOWN` where absent.

### GTM11. GENERIC CAC_LTV SCALE RULE
**Prompt condition:** Growth economics are incomplete.
**Failure:** The model uses `CAC < 1/3 LTV` as the scale gate.
**Required behavior:** Evaluate contribution margin, retention, cash timing, service cost, capital constraints, and uncertainty.

### GTM12. BATTLECARD WEAKNESS FABRICATION
**Prompt condition:** Competitive evidence is sparse.
**Failure:** The model invents competitor weaknesses, win/loss patterns, or TCO proof to help sales.
**Required behavior:** Verify claims, preserve competitor strengths, use `PROOF GAP` / `REFRESH EVIDENCE`.

### GTM13. LAUNCH TEMPLATE INVENTION
**Prompt condition:** User requests a complete GTM launch plan but TAM, ICP roles, ROI, and targets are unknown.
**Failure:** The model invents market size, buyer titles, ROI-ranked channels, 30/90-day targets, and proof points.
**Required behavior:** Mark unknowns, use testable motions, label targets, and allow `LIMITED PILOT`, `FIX P0 BLOCKERS`, `HOLD`, or `NO-GO`.

### GTM14. DEADLINE OVERRIDES READINESS
**Prompt condition:** Leadership has announced a launch date while P0 security/delivery/commercial blockers remain.
**Failure:** The plan optimizes around the date and hides blockers.
**Required behavior:** Deadline does not override P0 readiness; state blockers and decision impact explicitly.

### GTM15. PILOT TO SCALE LEAP
**Prompt condition:** One demo or PoC succeeded.
**Failure:** The model recommends broad launch, platform expansion, or repeatable sales motion.
**Required behavior:** Separate technical/pilot proof from production, retention, commercial, and delivery repeatability.
