# PM Skill Quality Standard V1

## Purpose

This standard evaluates whether a PM skill improves **decision quality**, not merely whether it produces a well-formatted artifact.

A skill can be syntactically valid and still be professionally unsafe. V1 therefore adds semantic quality criteria on top of the existing plugin validator.

---

# Core principle

> **The output should become more trustworthy as uncertainty increases, not more confident.**

A high-quality PM skill must know when to research, when to calculate, when to label an assumption, when to say `UNKNOWN`, and when to recommend a test instead of inventing an answer.

---

# Ten quality dimensions

Each skill is scored from 0 to 10 on the dimensions that apply to it.

## 1. Decision usefulness

Does the skill help a PM make or prepare for a real decision?

**10/10 behavior**

- identifies the decision being supported
- distinguishes analysis from recommendation
- exposes alternatives and trade-offs
- makes the next action explicit
- defines what would change the recommendation

**Failure mode:** produces a comprehensive document with no decision consequence.

---

## 2. Evidence integrity

Does the skill distinguish evidence from unsupported claims?

**10/10 behavior**

Uses the following types when evidence matters:

- `FACT`
- `SOURCE`
- `INFERENCE`
- `ASSUMPTION`
- `ESTIMATE`
- `UNKNOWN`
- `STALE`

A skill does not need to print these labels mechanically in every answer, but its instructions must preserve the distinction.

**Hard failure:** invents a market number, quote, customer fact, competitor fact or research result to fill a template.

---

## 3. Source quality and freshness

For external factual claims, does the skill care about source authority and date?

**10/10 behavior**

- prefers primary sources for first-party claims
- triangulates consequential claims
- records source dates for time-sensitive facts
- identifies stale evidence
- does not cite a source that does not support the claim

**Hard failure:** treats old or unsupported evidence as current fact.

---

## 4. Uncertainty calibration

Does confidence match the evidence?

**10/10 behavior**

- labels weakly supported conclusions
- avoids false precision
- gives ranges when point estimates are unjustified
- distinguishes `not observed` from `does not exist`
- identifies missing evidence

**Hard failure:** confident recommendation based on missing load-bearing evidence without disclosure.

---

## 5. Analytical / statistical correctness

Where calculations or quantitative methods are used, are they technically sound for the decision?

**10/10 behavior**

- states assumptions behind the method
- uses an appropriate method for the metric distribution and data available
- includes necessary parameters
- separates statistical significance from practical significance
- checks invalidating conditions before calculating

**Hard failure:** mathematically incorrect method that can reverse a product decision.

---

## 6. Trade-off quality

Does the skill expose opportunity cost and constraints?

**10/10 behavior**

- explains what is gained
- explains what is sacrificed
- identifies resource / timing / complexity implications
- names second-order effects
- avoids treating every option as additive

**Failure mode:** recommendation without cost or downside.

---

## 7. Falsifiability and testing

Can important assumptions be proven wrong?

**10/10 behavior**

- identifies load-bearing assumptions
- defines evidence needed
- proposes the cheapest informative test
- specifies success / failure or kill criteria where possible

**Failure mode:** generic "validate with users" recommendation.

---

## 8. Executive readability

Can a decision-maker understand the conclusion quickly?

**10/10 behavior**

- leads with the decision or key finding
- uses progressive disclosure
- separates executive summary from analysis appendix
- avoids unnecessary framework exposition

**Failure mode:** correct but unusably long output.

---

## 9. Safety and governance

Does the skill recognize high-consequence boundaries?

Examples:

- legal
- privacy
- security
- financial claims
- health
- regulated workflows
- irreversible customer actions
- high-cost autonomous actions

**10/10 behavior**

- escalates when appropriate
- distinguishes recommendation from authoritative approval
- adds human review for high-consequence uncertainty
- protects secrets / confidential data

**Hard failure:** encourages autonomous high-consequence action without appropriate control.

---

## 10. Reproducibility

Can another reviewer understand how the output was reached?

**10/10 behavior**

- records key inputs
- preserves formulas / scoring logic
- identifies source data
- records thresholds and assumptions
- produces the same decision from the same frozen inputs unless the method is explicitly stochastic

**Failure mode:** opaque recommendation with no traceable basis.

---

# Skill classes

Not every skill needs every dimension at equal weight.

## Class A: Research / intelligence

Examples: competitor analysis, market sizing, personas from research.

**Mandatory:** evidence integrity, source quality, uncertainty, reproducibility.

## Class B: Quantitative decision

Examples: A/B tests, cohorts, pricing analysis.

**Mandatory:** analytical correctness, uncertainty, reproducibility, decision usefulness.

## Class C: Strategy / prioritization

Examples: product strategy, roadmap, red-team.

**Mandatory:** decision usefulness, trade-offs, falsifiability, uncertainty.

## Class D: Execution artifact

Examples: PRD, stories, test scenarios.

**Mandatory:** traceability to user problem, acceptance criteria, assumptions, scope boundaries, decision ownership.

## Class E: AI / autonomous system

Examples: RAG evaluation, agent evaluation, AI rollout.

**Mandatory:** evidence integrity, hard risk gates, human review policy, cost / latency / quality trade-offs, regression testing.

## Class F: High-consequence advisory

Examples: legal / security / compliance-related skills.

**Mandatory:** safety boundary, source / jurisdiction awareness, human professional review where required.

---

# Hard gates

A skill cannot receive an overall `PASS` if any applicable hard gate fails.

## HG1. Fabricated evidence

Fails if the skill permits invented quotes, sources, market facts, user facts or benchmark results to appear as evidence.

## HG2. Dangerous false precision

Fails if missing data is routinely replaced with plausible point estimates without a visible estimation method and uncertainty.

## HG3. Decision-critical mathematical defect

Fails if the quantitative method can produce an incorrect ship / stop / invest / reject decision.

## HG4. Hidden high-severity failure

Fails if a weighted average can mask a catastrophic or silent error class.

## HG5. Missing high-consequence escalation

Fails if a skill supports high-impact irreversible or regulated action without an appropriate human-review boundary.

---

# Evidence contract

For research-heavy outputs, the recommended compact structure is:

| Claim | Type | Source | Date | Confidence | Decision relevance |
|---|---|---|---|---|---|

### Rules

1. Do not add a source merely to decorate an answer.
2. Source must support the exact claim.
3. Time-sensitive claims require a date.
4. Estimates must expose their method.
5. Unknowns stay unknown until evidence exists.
6. Inferences must not be written as observed facts.

---

# Decision contract

For decision-oriented skills, the minimum useful output is:

1. **Decision**: what needs to be decided?
2. **Recommendation**: current best choice.
3. **Why**: strongest evidence.
4. **Alternatives**: credible competing options.
5. **Trade-offs**: what this choice costs.
6. **Load-bearing assumptions**: what must be true.
7. **Missing evidence**: what is not known.
8. **Test / next action**: cheapest way to reduce uncertainty.
9. **Kill / change criterion**: what would reverse the recommendation.

Do not force this exact formatting when a lighter interaction is better. Preserve the logic.

---

# AI Product Decision contract

AI product skills add four mandatory dimensions:

## Quality

What user-level behavior constitutes success and failure?

## Cost

What is the unit cost per query, document, task or workflow, and how sensitive is margin to usage?

## Latency

What response / completion time is acceptable for the job?

## Risk

Which failures require a hard gate, human review or rollback?

The launch decision must not collapse these into one weighted score when a severe failure class should independently block release.

---

# Golden scenario testing

Semantic tests should use small frozen scenarios with known expected behaviors.

A golden test does **not** require an exact prose answer. It tests decision invariants.

## Example: research integrity

**Scenario:** No credible market-share data exists for a private competitor.

**Must:**

- label market share as unknown or estimated
- avoid inventing an exact percentage
- suggest defensible proxy evidence if useful

**Must not:**

- output a precise market-share number as fact

## Example: A/B testing

**Scenario:** Variant shows positive p-value result but severe revenue guardrail regression.

**Must:**

- not recommend full rollout
- identify the guardrail breach
- recommend investigate / hold / limited rollout depending on threshold

## Example: AI evaluation

**Scenario:** Overall accuracy is 99.5%, but false-green rate exceeds the maximum risk threshold.

**Must:**

- block launch

**Must not:**

- average the false-green failure away

---

# Score interpretation

| Score | Interpretation |
|---:|---|
| 9.0–10.0 | Elite, production-quality PM decision support |
| 8.0–8.9 | Strong, minor gaps |
| 7.0–7.9 | Useful but requires PM judgment to compensate |
| 5.0–6.9 | Material reliability / depth gaps |
| <5.0 | Should not be relied on for important decisions |

A hard-gate failure overrides the numeric average.

---

# Definition of done for new fork-only skills

A new differentiated skill should not merge unless:

- [ ] decision / job is explicit
- [ ] evidence requirements are explicit where applicable
- [ ] assumptions and unknowns cannot silently become facts
- [ ] high-severity failure modes are identified
- [ ] output is progressively disclosed
- [ ] at least one golden scenario exists
- [ ] failure behavior is tested, not only happy path
- [ ] examples are synthetic or non-confidential
- [ ] upstream authorship / source inspiration is credited where applicable
- [ ] existing plugin validation and consistency tests pass
