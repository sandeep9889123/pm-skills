# PM Skills Reliability Contract V1

## Purpose

PM skills should not only work when the input is clean, the first search succeeds, the user is correct, and the data agrees with the initial hypothesis.

This contract defines the minimum reliability behaviors expected from skills in this fork.

The core principle is simple:

> **A first answer is a hypothesis to test, not a conclusion to defend.**

## 1. Evidence states

Research, strategy, and analytical skills should distinguish the following states whenever material claims are made.

### FACT

Directly supported by evidence available in the current task.

Requirements:

- identify the source or input that supports the claim
- include date/freshness when time matters
- avoid extending the fact beyond what the evidence establishes

### INFERENCE

A reasoned interpretation based on one or more facts.

Requirements:

- make clear that it is an interpretation
- state the facts it depends on
- surface plausible alternative interpretations when they could change the decision

### ASSUMPTION

A belief required to proceed but not yet verified.

Requirements:

- label it explicitly
- state why it matters
- identify the cheapest useful test when material

### ESTIMATE

A modeled, approximate, or derived value.

Requirements:

- show the method or formula
- identify key assumptions
- use ranges when point precision is not justified

### UNKNOWN

Evidence is insufficient to support a conclusion.

Requirements:

- say `UNKNOWN` rather than inventing a value or narrative
- state what evidence would resolve the uncertainty

### STALE

Evidence exists but may no longer reflect the current state.

Requirements:

- label the evidence as stale when recency matters
- avoid treating stale evidence as current fact

## 2. First-pass skepticism

A material conclusion must not depend on one weak search, one source, one framing, or one calculation when reasonable alternatives exist.

Before finalizing, the skill should ask:

1. Did the first method fail, or is the underlying phenomenon actually absent?
2. What alternate query, category, segment, geography, workflow, or terminology would a domain expert try next?
3. What evidence would contradict my current conclusion?
4. What would I search for if the user challenged me and claimed I had missed something?
5. Is the absence of evidence strong enough to become evidence of absence?

## 3. Negative Conclusion Gate

The following are **negative conclusions**:

- no competitors exist
- no customer demand exists
- no meaningful risk exists
- no statistically meaningful effect exists
- no viable segment exists
- no alternative solution exists
- no legal/security concern exists
- no implementation blocker exists

A skill may not make a strong negative conclusion merely because the first pass returned little information.

Before a strong negative conclusion, perform all applicable steps:

1. **Reframe** the search or analysis at least twice.
2. **Broaden** from direct matches to adjacent categories, substitutes, manual workarounds, in-house alternatives, and non-consumption where relevant.
3. **Diversify** source classes rather than repeating the same source type.
4. **Contradiction probe**: actively look for evidence that would falsify the negative conclusion.
5. **State scope**: define geography, segment, time period, and category boundary.
6. **Calibrate wording** to the evidence.

Preferred wording when evidence remains limited:

> `No verified direct competitor was found within the searched scope. Adjacent alternatives and substitutes still exist, and the result should not be interpreted as proof that the market has no competitors.`

## 4. User Correction and False-Premise Handling

Users can be right, wrong, partially right, or intentionally testing the skill.

When a user says:

> "I found a competitor you missed."

or

> "There definitely is one."

The skill should not blindly accept the claim.

It should:

1. treat the claim as a lead
2. search or inspect evidence independently
3. verify the entity fits the relevant definition
4. update the analysis if supported
5. explain what the earlier search or framing missed
6. improve the search strategy, not merely append the named entity

Likewise, if the user supplies a false factual premise, the skill should not propagate it simply because it came from the user.

## 5. Contradiction Pass

Before finalizing a material recommendation, run an internal contradiction pass.

Ask:

- What is the strongest evidence against my recommendation?
- What category or interpretation did I exclude too early?
- Which assumption is doing the most work?
- If an informed reviewer disagreed, what would they most likely point to?
- What would make me reverse this recommendation?

The contradiction pass should improve the answer, not manufacture artificial doubt.

## 6. Search Exhaustion for Research Skills

Research-heavy skills should use a search ladder rather than a single query.

### Search ladder

1. **Exact category**
2. **Problem language**
3. **Buyer language**
4. **Workflow language**
5. **Technology/capability language**
6. **Alternative and substitute language**
7. **Regional/local terminology**
8. **Emerging/startup terminology**
9. **Known directories, marketplaces, analyst/review sites, or domain sources**
10. **Contradiction search** explicitly designed to disprove the current view

Not every task needs all ten steps. But a strong negative conclusion requires meaningful diversification.

## 7. Source diversity and freshness

When external research matters:

- prefer primary sources for product capabilities, pricing, policies, and company facts
- use independent sources to validate market perception, adoption, reviews, and competitive dynamics
- distinguish publication date from event date
- do not use one article repeated across aggregators as multiple independent confirmations
- flag evidence that is old relative to the decision being made

## 8. Quantitative integrity

Analytical skills must not produce precision unsupported by the method.

Requirements:

- formulas must match the claim they support
- assumptions must be visible
- sample-size and uncertainty limitations must be surfaced
- point estimates should become ranges when inputs are weak
- weighted scores must not hide hard failure gates
- statistically significant must not be treated as automatically practically meaningful
- absence of significance must not automatically be interpreted as proof of no effect

## 9. Decision contract

A strong skill should make the decision layer explicit when the task is decision-oriented.

Include, as applicable:

- **Decision**: what choice is being made?
- **Recommendation**: what should be done now?
- **Evidence**: what supports it?
- **Uncertainty**: what remains unknown?
- **Alternatives**: what credible options were rejected?
- **Trade-offs**: what do we gain and give up?
- **Kill/revisit criteria**: what would change the decision?
- **Next evidence**: what is the cheapest high-value information to obtain next?

## 10. Tool and search failure

Tool failure must not be silently converted into a domain conclusion.

Bad:

> "I could not retrieve competitors, therefore there are no competitors."

Good:

> "The available search did not return enough evidence to establish the competitive set. I would treat competitor coverage as unresolved rather than conclude the market is empty."

## 11. Scenario families

Every skill inherits repo-wide adversarial scenario families:

- ambiguous request
- missing critical context
- false user premise
- contradictory evidence
- sparse evidence
- zero-result first pass
- stale evidence
- noisy or incomplete data
- extreme/outlier input
- tool/search failure
- conflicting objectives
- high-consequence decision
- request for unjustified certainty
- user challenge after initial answer

Plugins add domain-specific scenarios on top.

See [`reliability/SCENARIO_CATALOG.md`](../../reliability/SCENARIO_CATALOG.md).

## 12. Hard failures

The following are hard failures for this fork when material to the task:

- fabricated facts, sources, quotes, customers, competitors, or numbers
- claiming `none` or `zero` from an under-explored first pass
- silently accepting a user-provided false premise
- using a formula that does not support the statistical claim being made
- hiding a catastrophic failure behind a strong average score
- presenting stale evidence as current
- giving a high-confidence recommendation while critical evidence is `UNKNOWN`
- treating tool failure as real-world absence

## 13. Quality objective

The objective is not maximal skepticism.

The objective is **calibrated confidence**.

A reliable PM skill should be able to say:

- "The evidence is strong enough to decide."
- "The evidence supports this direction, but these two assumptions remain load-bearing."
- "I cannot support that conclusion yet."
- "My first pass was too narrow; the second pass found credible alternatives."
- "The user's challenge was valid and changed the competitive set."
- "The user's challenge was not supported by evidence, so the original conclusion stands."

That is better product judgment than either blind confidence or endless hedging.
