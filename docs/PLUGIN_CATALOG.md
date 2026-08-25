# PM Skills Plugin Catalog

This is the browseable inventory for the 12-plugin PM Skills repository.

For installation instructions, see [USING_WITH_LLMS.md](USING_WITH_LLMS.md).

## 1. pm-product-discovery

**Use for:** ideation, assumptions, discovery experiments, customer interviews, feature triage, opportunity mapping, and early metrics.

**Skills (13):**

- `analyze-feature-requests`
- `brainstorm-experiments-existing`
- `brainstorm-experiments-new`
- `brainstorm-ideas-existing`
- `brainstorm-ideas-new`
- `identify-assumptions-existing`
- `identify-assumptions-new`
- `interview-script`
- `metrics-dashboard`
- `opportunity-solution-tree`
- `prioritize-assumptions`
- `prioritize-features`
- `summarize-interview`

**Workflows (5):** `/brainstorm`, `/discover`, `/interview`, `/setup-metrics`, `/triage-requests`

**Starter prompt:**

```text
Use pm-product-discovery to turn this product idea into a problem framing, assumptions map, prioritized risks, and the cheapest experiments that could disconfirm the thesis.
```

## 2. pm-prospect-discovery

**Use for:** enterprise pre-RFP discovery, account research, problem/use-case falsification, adaptive questions, assumption registers, session synthesis, and proposal readiness.

**Skills (10):**

- `assumption-register`
- `discovery-question-engine`
- `discovery-red-team`
- `discovery-synthesis`
- `journey-decomposition`
- `problem-use-case-hypothesis`
- `proposal-readiness`
- `prospect-discovery-orchestrator`
- `prospect-research`
- `solution-option-framing`

**Workflows (4):** `/prospect-discovery`, `/discovery-prepare`, `/discovery-synthesize`, `/discovery-readiness`

**Starter prompt:**

```text
Use pm-prospect-discovery to prepare a 60-minute pre-RFP discovery session. Treat our proposed use case as a hypothesis, test alternative root causes, generate only decision-changing questions, and state all P0 readiness blockers.
```

## 3. pm-product-strategy

**Use for:** product strategy, vision, value proposition, business models, monetization, pricing, SWOT, PESTLE, Porter's Five Forces, and Ansoff analysis.

**Skills (12):**

- `ansoff-matrix`
- `business-model`
- `lean-canvas`
- `monetization-strategy`
- `pestle-analysis`
- `porters-five-forces`
- `pricing-strategy`
- `product-strategy`
- `product-vision`
- `startup-canvas`
- `swot-analysis`
- `value-proposition`

**Workflows (5):** `/business-model`, `/market-scan`, `/pricing`, `/strategy`, `/value-proposition`

**Starter prompt:**

```text
Use pm-product-strategy to create three strategic options, explicit trade-offs, a right-to-win hypothesis, what we should not do, and the evidence needed before commitment.
```

## 4. pm-execution

**Use for:** PRDs, OKRs, roadmaps, sprint planning, retros, release notes, pre-mortems, stakeholder mapping, stories, tests, dummy data, and strategy red-team.

**Skills (16):**

- `brainstorm-okrs`
- `create-prd`
- `dummy-dataset`
- `job-stories`
- `outcome-roadmap`
- `pre-mortem`
- `prioritization-frameworks`
- `release-notes`
- `retro`
- `sprint-plan`
- `stakeholder-map`
- `strategy-red-team`
- `summarize-meeting`
- `test-scenarios`
- `user-stories`
- `wwas`

**Workflows (11):** `/generate-data`, `/meeting-notes`, `/plan-okrs`, `/pre-mortem`, `/red-team-prd`, `/sprint`, `/stakeholder-map`, `/test-scenarios`, `/transform-roadmap`, `/write-prd`, `/write-stories`

**Starter prompt:**

```text
Use pm-execution to write a decision-first PRD with scope, non-goals, user journeys, failure cases, acceptance criteria, analytics, dependencies, rollout, and test scenarios.
```

## 5. pm-market-research

**Use for:** competitor intelligence, personas, segmentation, journeys, market sizing, sentiment, and evidence-led user/market research.

**Skills (7):**

- `competitor-analysis`
- `customer-journey-map`
- `market-segments`
- `market-sizing`
- `sentiment-analysis`
- `user-personas`
- `user-segmentation`

**Workflows (3):** `/analyze-feedback`, `/competitive-analysis`, `/research-users`

**Starter prompt:**

```text
Use pm-market-research to map direct competitors, adjacent alternatives, substitutes, manual workflows, internal builds, incumbents, regional players, and emerging entrants. Show search coverage and unresolved candidates.
```

## 6. pm-data-analytics

**Use for:** SQL, cohort analysis, A/B test interpretation, metric logic, and PM analytics reasoning.

**Skills (3):**

- `ab-test-analysis`
- `cohort-analysis`
- `sql-queries`

**Workflows (3):** `/analyze-cohorts`, `/analyze-test`, `/write-query`

**Starter prompt:**

```text
Use pm-data-analytics to define the decision question first, then design the analysis, metrics, segments, SQL logic, caveats, and decision rule.
```

## 7. pm-go-to-market

**Use for:** ICP, beachhead segment, GTM strategy, motions, growth loops, competitive battlecards, and launch planning.

**Skills (6):**

- `beachhead-segment`
- `competitive-battlecard`
- `growth-loops`
- `gtm-motions`
- `gtm-strategy`
- `ideal-customer-profile`

**Workflows (3):** `/battlecard`, `/growth-strategy`, `/plan-launch`

**Starter prompt:**

```text
Use pm-go-to-market to define the ICP, buying trigger, anti-ICP, beachhead, proof points, objections, GTM motion, production path, and launch metrics.
```

## 8. pm-marketing-growth

**Use for:** North Star metrics, positioning, product naming, value-proposition statements, and marketing ideas.

**Skills (5):**

- `marketing-ideas`
- `north-star-metric`
- `positioning-ideas`
- `product-name`
- `value-prop-statements`

**Workflows (2):** `/market-product`, `/north-star`

**Starter prompt:**

```text
Use pm-marketing-growth to define positioning for this target segment, with pain, promise, proof, alternatives, objection handling, and a North Star metric tied to delivered value.
```

## 9. pm-toolkit

**Use for:** resume review, tailoring, proofreading, NDA drafting, privacy-policy starter drafts, and PM utility writing.

**Skills (4):**

- `draft-nda`
- `grammar-check`
- `privacy-policy`
- `review-resume`

**Workflows (5):** `/draft-nda`, `/privacy-policy`, `/proofread`, `/review-resume`, `/tailor-resume`

**Starter prompt:**

```text
Use pm-toolkit to review this PM resume. Do not invent metrics or experience. Diagnose weak signals, map them to the target role, and rewrite only what the evidence supports.
```

## 10. pm-ai-shipping

**Use for:** intended-vs-implemented review, shipping evidence, test derivation, app documentation, static security review, and static performance review.

**Skills (2):**

- `intended-vs-implemented`
- `shipping-artifacts`

**Workflows (5):** `/derive-tests`, `/document-app`, `/performance-audit-static`, `/security-audit-static`, `/ship-check`

**Starter prompt:**

```text
Use pm-ai-shipping to compare intended and implemented behavior, derive tests, identify launch blockers, and separate verified code evidence from unknowns.
```

## 11. pm-enterprise-transformation

**Use for:** future capability building, reusable accelerators, client proof to GTM, account expansion, sales transformation, tool selection, and PM workflow automation.

**Skills (12):**

- `account-expansion-play`
- `automation-governance`
- `capability-opportunity-radar`
- `case-study-to-gtm`
- `client-proof-extractor`
- `pipeline-conversion-experiment`
- `pm-workflow-automation`
- `reusable-accelerator-thesis`
- `sales-funnel-diagnostic`
- `solution-business-case`
- `solution-to-sales-playbook`
- `tool-evaluation-selection`

**Workflows (4):** `/automate-pm-workflow`, `/build-future-capability`, `/proof-to-gtm`, `/transform-sales`

**Starter prompt:**

```text
Use pm-enterprise-transformation to evaluate this future capability. Separate real client proof from aspiration, test reuse economics and right-to-win, define GTM path, and recommend PILOT, HOLD, BUY/PARTNER, or investment only when evidence supports it.
```

## 12. pm-business-case

**Use for:** evidence ledgers, market proof, customer/JTBD proof, economics, commercialization, alternatives, investment red-team, and gated business-case decisions.

**Skills (6):**

- `business-case-orchestrator`
- `customer-jtbd-proof`
- `economics-commercial-proof`
- `evidence-ledger`
- `investment-red-team`
- `opportunity-market-proof`

**Workflows (5):** `/build-business-case`, `/business-case-decision`, `/business-case-evidence`, `/business-case-red-team`, `/business-case-refresh`

**Starter prompt:**

```text
Use pm-business-case to evaluate this initiative. Build the evidence ledger before the narrative, test market/customer/right-to-win proof, compare alternatives, model reconstructable economics, define a falsifiable PoC, and include the strongest rejection case.
```
