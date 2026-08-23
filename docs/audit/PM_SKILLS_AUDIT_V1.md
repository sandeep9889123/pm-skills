# PM Skills Audit V1

## Executive verdict

The upstream marketplace is already a strong broad PM framework library. The fork should **not** compete by adding more generic frameworks. Its defensible differentiation should be:

> **Evidence-first Enterprise + AI Product Management, with skill quality evaluated as rigorously as plugin structure.**

### Baseline assessment

| Dimension | Baseline | Target | Audit view |
|---|---:|---:|---|
| Breadth of PM coverage | 9.0/10 | 9.0/10 | Already strong. Do not expand breadth for its own sake. |
| Workflow usability | 8.5/10 | 9.5/10 | Good chaining and checkpoints. Needs stronger decision gates. |
| Product judgment | 7.5/10 | 9.5/10 | Frameworks are good, but many outputs optimize for artifact completion rather than decision quality. |
| Evidence integrity | 6.5/10 | 10/10 | Research skills mention sourcing, but evidence discipline is inconsistent and not enforced. |
| Hallucination resistance | 6.0/10 | 10/10 | No repo-wide UNKNOWN / verification contract. Some skills invite unverifiable outputs. |
| Data / statistical rigor | 6.5/10 | 9.5/10 | Useful analytics coverage, but at least one high-consequence statistical defect exists. |
| Enterprise PM depth | 5.5/10 | 9.5/10 | Buyer committees, procurement, implementation, integrations, RBAC, SLA/SLO and enterprise adoption are underrepresented. |
| AI Product Management depth | 5.0/10 | 10/10 | `pm-ai-shipping` is strong for AI-built software reviewability, but model/product evaluation and AI operating decisions are largely absent. |
| Executive decision support | 6.5/10 | 9.5/10 | Strategy and red-team skills are useful, but IC/CEO decision memos, capital allocation and scenario logic are incomplete. |
| Semantic quality assurance | 4.0/10 | 10/10 | CI validates structure and consistency, not whether a skill gives a correct, grounded or decision-useful answer. |
| Open-source maintainability | 9.0/10 | 9.5/10 | Strong manifests, version consistency, tests and contribution conventions. |

**Overall baseline:** ~7.2/10 as a broad PM skill marketplace.

**Potential of this fork:** 9.5+/10 if it becomes a differentiated Enterprise AI PM decision system rather than a larger clone.

---

## What is already excellent

### 1. Repository architecture

The plugin architecture is clear, modular and installable across multiple AI environments. Skills and commands are separated cleanly, manifests are versioned consistently and CI enforces repository integrity.

### 2. Workflow orchestration

Commands such as `/discover`, `/strategy`, and `/write-prd` provide usable end-to-end flows instead of isolated prompts. Checkpoints and follow-up actions make the system practical for daily PM work.

### 3. Strongest existing pattern: intended vs implemented

`pm-ai-shipping/skills/intended-vs-implemented` is the strongest quality pattern in the repository. It requires:

- documented intent as a claim to verify
- implementation evidence as cited code
- explicit separation between evidence and unanswered questions
- no fabricated intent
- concrete actor, victim and boundary for findings

This **claim → evidence → mismatch → consequence → fix** pattern should be generalized beyond code audits into research, strategy, market intelligence and AI evaluation.

### 4. Strategy red-team discipline

`strategy-red-team` is materially better than generic risk analysis because it steelmans before attacking, prioritizes load-bearing assumptions, requires falsifiable failure conditions and asks for cheap tests and kill criteria.

---

# Critical gaps

## P0. Semantic quality is not tested

Current automated checks validate:

- plugin manifests
- YAML/frontmatter
- naming
- word counts
- README consistency
- version consistency
- command references

They do **not** validate:

- factual correctness
- statistical correctness
- evidence quality
- hallucination resistance
- decision usefulness
- source freshness
- confidence calibration
- whether a high-severity failure is hidden by an average score

### Consequence

A skill can pass CI while giving a professionally dangerous answer.

### Recommendation

Create a **PM Skill Quality Harness** with golden scenarios, expected behaviors and hard failure gates.

---

## P0. Evidence integrity is inconsistent

Research-heavy skills often instruct the model to research and cite sources, but there is no universal evidence contract.

### Missing controls

Every research / strategy skill should distinguish:

- **FACT**: externally verifiable claim
- **SOURCE**: source and date supporting that claim
- **INFERENCE**: conclusion derived from facts
- **ASSUMPTION**: belief not yet supported
- **ESTIMATE**: modeled value with explicit method
- **UNKNOWN**: insufficient evidence
- **STALE**: evidence may no longer be current

### Required upgrade

No evidence should be silently converted into false precision.

If a value cannot be verified, the correct answer is **UNKNOWN**, not a plausible number.

---

## P0. Interview quote verification gap

`summarize-interview` asks for "unexpected findings or notable quotes" but does not require quote verification against the source transcript.

### Risk

A paraphrase or hallucinated quote can become a durable research artifact and later appear as false customer evidence in strategy or roadmap discussions.

### Required behavior

- Every direct quote must be traceable to the transcript.
- Unmatched quotes must be labeled `UNVERIFIED`, not silently repaired.
- The output should state a verification count.
- Paraphrases must be labeled as paraphrases.

**Upstream candidate:** Yes. This is a narrow reliability fix with broad value.

---

## P0. A/B test sample-size logic cannot support its stated power claim

The `ab-test-analysis` skill displays a sample-size formula based on the alpha critical value and then asks the model to flag tests below 80% power.

The displayed formula does not include a beta / power term, so it cannot by itself establish 80% power.

### Additional analytics gaps

- sequential peeking / repeated significance checks
- multiple comparisons
- metric distribution choice
- variance reduction / CUPED
- heterogeneous treatment effects
- novelty effects beyond a generic duration rule
- practical effect vs confidence interval around MDE
- experimentation guardrails for revenue, latency and quality

### Required behavior

The skill should separate:

1. experimental validity
2. statistical inference
3. practical significance
4. guardrail health
5. product decision

**Upstream candidate:** Yes. Statistical correctness should be fixed at source.

---

## P1. Research outputs need an evidence ledger

Market sizing and competitor analysis include good instincts, such as triangulation, sources and assumptions, but the output contract does not force claim-level provenance.

### Upgrade pattern

Add a compact evidence ledger:

| Claim | Type | Source | Source date | Confidence | Notes |
|---|---|---|---|---|---|

For market sizing, separately expose:

- observed inputs
- modeled inputs
- formulas
- sensitivity range
- base / bull / bear estimates
- what evidence would narrow the interval

For competitor analysis, prohibit unsupported estimates of market share, customer count, funding or pricing.

---

## P1. Strategy artifacts need stronger decision economics

The strategy canvas is useful, but a senior executive decision requires more than a complete canvas.

### Missing decision layer

- decision to be made
- alternatives considered
- explicit recommendation
- evidence supporting each alternative
- opportunity cost
- resource requirement
- reversibility
- 1-year / 3-year consequences
- key uncertainty
- cheapest test
- what would change the recommendation

### Upgrade

Add an optional **Executive Decision Layer** to strategy workflows rather than making every output longer.

---

## P1. Enterprise PM operating reality is underrepresented

The current marketplace covers general PM craft very well, but enterprise software has distinct decision surfaces.

### Missing or thin capabilities

- economic buyer vs user vs admin vs security stakeholder
- buying committee mapping
- enterprise discovery
- RFP / RFI analysis
- procurement and security review
- implementation readiness
- migration / cutover
- API and integration strategy
- RBAC / permissions product requirements
- SLA / SLO design
- auditability
- change management
- enterprise adoption
- expansion / renewal signals
- customer-specific request vs reusable platform capability

### Recommendation

Create a differentiated fork-only plugin: `pm-enterprise-product`.

---

## P1. AI PM is not the same as AI code shipping

`pm-ai-shipping` is valuable but focuses on making AI-built applications reviewable and auditable.

AI Product Managers also need a decision system for the AI capability itself.

### Missing capabilities

- AI use-case selection
- deterministic vs probabilistic solution choice
- build / buy / partner
- model / provider selection
- evaluation contract
- golden dataset design
- RAG evaluation
- agent evaluation
- confidence calibration
- false-positive / false-negative economics
- human-review policy
- cost × latency × quality trade-offs
- AI UX / uncertainty communication
- model regression / drift
- rollout / rollback
- observability
- data flywheel / feedback loop
- safety and trust boundaries

### Recommendation

Create a differentiated fork-only plugin: `pm-enterprise-ai`.

---

## P1. North Star classification is too rigid for complex products

The current skill forces businesses into Attention, Transaction or Productivity games.

This is useful pedagogy but can oversimplify:

- multi-sided marketplaces
- enterprise platforms
- infrastructure products
- AI products with usage and outcome economics
- hybrid businesses with multiple value loops

### Upgrade

Treat business-game classification as a heuristic, not a mutually exclusive ontology. Require a value-delivery causal model and guardrails.

---

## P1. GTM needs an enterprise path

The generic GTM skill focuses heavily on marketing channels and launch activities.

For enterprise software, GTM must also model:

- ICP and trigger event
- buying committee
- sales cycle
- proof of value / pilot
- procurement
- security / legal review
- implementation capacity
- time-to-value
- adoption owner
- expansion and renewal
- partner / channel motion

This should be implemented in the enterprise plugin rather than bloating the generic GTM skill.

---

## P2. Pricing examples create decay risk

Hard-coded examples and specific price points can become stale even when the pricing logic remains valid.

### Upgrade

Use pricing examples illustratively and require current verification before treating competitor price points as facts.

For AI products, add:

- inference cost
- margin sensitivity
- usage volatility
- outcome-based pricing
- token / task / workflow economics
- cost controls and abuse risk

---

## P2. Toolkit scope is not strategically differentiating

Resume, grammar, NDA and privacy skills may be useful, but they are not where this fork should invest differentiation effort.

### Recommendation

Keep upstream compatibility. Do not spend roadmap capacity expanding the toolkit unless a clear PM workflow depends on it.

---

# Plugin scorecard

| Plugin | Current quality | Main strength | Main gap | Fork priority |
|---|---:|---|---|---|
| pm-product-discovery | 7.5 | Strong discovery flow and assumption mapping | Evidence verification and research provenance | P1 |
| pm-product-strategy | 7.5 | Good strategy/trade-off structure | Decision economics, evidence and scenario logic | P1 |
| pm-execution | 8.0 | PRD, red-team, execution breadth | Artifact-centric; acceptance / release gates uneven | P1 |
| pm-market-research | 6.5 | Broad research toolkit | Highest hallucination / stale-data exposure | P0 |
| pm-data-analytics | 6.5 | Useful PM-accessible analytics | Statistical rigor and semantic tests | P0 |
| pm-go-to-market | 7.0 | Practical generic launch planning | Enterprise buying / implementation motion | P1 |
| pm-marketing-growth | 7.0 | Accessible metrics and positioning | Heuristics can be oversimplified / static | P2 |
| pm-toolkit | 7.0 | Useful utilities, legal disclaimer present | Low differentiation for target fork | P3 |
| pm-ai-shipping | 8.5 | Best evidence discipline in repo | AI code shipping, not full AI product management | P0 foundation |

---

# Target architecture for the fork

Do **not** rewrite all 68 upstream skills immediately.

Build differentiation in layers.

## Layer 1: PM Skill Quality Standard

A repo-wide quality contract that defines evidence integrity, decision quality and hallucination resistance.

## Layer 2: Semantic evaluation harness

Golden scenarios + assertions that test expected behavior, not just file shape.

## Layer 3: `pm-enterprise-ai`

A new plugin for AI product decisions and evaluation.

## Layer 4: `pm-enterprise-product`

A new plugin for enterprise PM workflows.

## Layer 5: `pm-executive-decision`

A compact decision-support plugin for CEO / VP / Principal PM-level artifacts.

---

# Proposed fork-only plugins

## `pm-enterprise-ai`

Initial skills:

1. `ai-use-case-prioritization`
2. `ai-solution-fit`
3. `ai-build-buy-partner`
4. `model-provider-selection`
5. `ai-evaluation-contract`
6. `golden-dataset-design`
7. `rag-evaluation`
8. `agent-evaluation`
9. `human-review-policy`
10. `ai-risk-register`
11. `cost-latency-quality`
12. `ai-rollout-rollback`
13. `ai-observability`
14. `ai-ux-trust`
15. `data-feedback-loop`

## `pm-enterprise-product`

Initial skills:

1. `enterprise-icp`
2. `buyer-user-admin-map`
3. `enterprise-discovery`
4. `rfp-rfi-analysis`
5. `integration-strategy`
6. `api-product-requirements`
7. `rbac-permissions`
8. `security-readiness`
9. `implementation-readiness`
10. `migration-cutover`
11. `enterprise-adoption`
12. `sla-slo-design`
13. `renewal-expansion-signals`
14. `custom-request-vs-platform`

## `pm-executive-decision`

Initial skills:

1. `decision-memo`
2. `business-case`
3. `investment-case`
4. `executive-brief`
5. `scenario-planning`
6. `portfolio-prioritization`
7. `resource-allocation`
8. `operating-review`
9. `executive-red-team`
10. `decision-log`

---

# Upstream contribution strategy

A fork becomes more credible when improvements are not merely private divergence.

## Good upstream candidates

- interview quote verification
- A/B test power / statistical correctness
- generic evidence integrity rules that do not change the marketplace's positioning
- validator improvements that detect malformed quality metadata
- narrow bug fixes

## Keep fork-only initially

- Enterprise AI plugin
- Enterprise Product plugin
- Executive Decision plugin
- semantic skill-quality scoring system if it introduces opinionated behavior incompatible with upstream philosophy
- portfolio-specific README positioning

---

# Do not do

- Do not add 50 generic skills to inflate counts.
- Do not rewrite upstream authorship or remove MIT attribution.
- Do not claim upstream work as original work.
- Do not make every skill longer.
- Do not force web research when the task does not need it.
- Do not turn every output into a consultant-style report.
- Do not use one weighted score to hide hard risk gates.
- Do not let an LLM invent market data because a template expects a number.
- Do not diverge so aggressively that upstream syncing becomes impossible.

---

# Recommended execution order

### Phase A, quality foundation

1. Add PM Skill Quality Standard.
2. Add evidence contract.
3. Add semantic golden-test harness.
4. Fix interview quote verification.
5. Fix A/B testing correctness.

### Phase B, differentiated AI PM plugin

6. Build `pm-enterprise-ai` MVP with 5 highest-value skills:
   - ai-use-case-prioritization
   - ai-evaluation-contract
   - golden-dataset-design
   - rag-evaluation
   - agent-evaluation
7. Add launch-decision workflow that composes these skills.
8. Add synthetic golden examples and regression tests.

### Phase C, enterprise PM

9. Build the enterprise buying / delivery spine:
   - buyer-user-admin-map
   - rfp-rfi-analysis
   - integration-strategy
   - implementation-readiness
   - enterprise-adoption

### Phase D, executive layer

10. Add decision memo, business case and executive red-team.
11. Benchmark against realistic CEO / VP Product scenarios.

---

# Success criteria for the fork

The fork is successful when a reviewer can answer **yes** to all of these:

1. Does it preserve upstream PM breadth?
2. Does it add clearly original Enterprise AI PM capability?
3. Can its highest-value skills be tested against golden scenarios?
4. Does it distinguish facts, assumptions, estimates and unknowns?
5. Does it expose evidence and source freshness where relevant?
6. Does it define hard decision gates for high-risk outputs?
7. Does it produce concise executive recommendations, not just templates?
8. Does it include falsification / kill criteria where decisions are uncertain?
9. Can improvements be contributed upstream without misrepresenting authorship?
10. Would a strong PM or engineering leader learn something from the implementation itself?

If these are true, the fork becomes a real public product artifact rather than a customized prompt pack.
