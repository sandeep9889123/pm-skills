---
description: Build an evidence-led product strategy with explicit choices, uncertainties, alternatives, right-to-win, and falsification gates
argument-hint: "<product or company>"
---

# /strategy - Evidence-Led Product Strategy

Create a strategy that makes choices under uncertainty. Do not fill every strategy section with invented specificity merely because the requested artifact is executive-ready.

## Reliability Contract

- Separate `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, and `TARGET`.
- A strategy is not a list of initiatives. It must contain choices, trade-offs, opportunity cost, and a theory of why this path can win.
- Do not invent segment size, pain severity, market attractiveness, moat, growth engine, investment level, timeline, or economics.
- Do not force a North Star metric when the value-delivery mechanism is not yet validated.
- Do not label an asset, data set, model, integration, relationship, brand, or feature as defensibility without explaining the mechanism and evidence that competitors cannot or will not replicate it economically.
- Build/Buy/Partner choices remain hypotheses until requirements, economics, control, time, switching, and strategic leverage are evaluated.
- Include at least one credible alternative strategy and `DO NOTHING / continue current state` where relevant.
- Explicitly state the strongest evidence against the preferred strategy.
- If decision-critical evidence is missing, choose `TEST`, `HOLD`, or `REFRAME` rather than fabricating a complete strategy.

## Workflow

### Step 1: Resolve the Decision Context

Capture:
- strategic decision to be made
- product/company stage
- target actor and geography
- current state and alternatives
- business objective
- constraints and non-negotiables
- evidence available
- material unknowns

A strategy for an idea should not be written with the certainty of a scaled product strategy.

### Step 2: Diagnose the Problem Before the Solution

Apply **product-strategy** and **product-vision**.

Establish:
- who has the problem
- when/how often it occurs
- current alternatives and switching barriers
- consequence of the problem
- why now
- what evidence contradicts the problem framing

If this is not sufficiently supported, label the framing `HYPOTHESIS`.

### Step 3: Generate Strategic Options

Create only materially distinct options supported by the context. For each:
- target segment / wedge
- value proposition
- what we deliberately do not serve or build
- growth / distribution mechanism
- capabilities required
- right-to-win hypothesis
- economics or resource implications where known
- biggest invalidating assumption

Include a credible alternative and current-state / do-nothing comparison when relevant.

### Step 4: Evaluate Choices

Compare options on evidence-backed criteria such as:
- customer value / urgency
- strategic fit
- right to win
- time to evidence
- capital / capacity requirement
- reversibility
- operational complexity
- regulatory / enterprise constraints
- GTM feasibility
- economic viability

Do not use arbitrary numeric scores unless the scale, inputs, and sensitivity are defined. Qualitative `SUPPORTED / PARTIAL / UNKNOWN` is preferable to false precision.

### Step 5: Define the Strategy

Cover these sections only to the level evidence supports:

1. **Vision / desired future**
2. **Target and anti-target segments**
3. **Problem / JTBD and value thesis**
4. **Value proposition and current alternatives**
5. **Strategic choices and trade-offs**
6. **Metrics and guardrails**
7. **Growth / distribution hypothesis**
8. **Capabilities and Build/Buy/Partner questions**
9. **Right-to-win / defensibility hypothesis**

Unknown fields remain `UNKNOWN`, not polished guesses.

### Step 6: Falsification and Decision Gate

For the recommended option state:
- strongest rejection case
- disconfirming evidence already known
- riskiest assumptions
- cheapest evidence needed next
- trigger to stop, pivot, or reframe

Decision outcome:

`COMMIT | TEST | HOLD | REFRAME | NO STRATEGY DECISION YET`

`COMMIT` requires enough evidence for the consequence and reversibility of the decision. It does not mean all uncertainty is gone.

## Output

```text
## Product Strategy: [Product]

### Decision Context
[decision, stage, constraints, evidence maturity]

### Evidence Ledger
[FACT / INFERENCE / ASSUMPTION / ESTIMATE / UNKNOWN / TARGET]

### Strategic Diagnosis
[problem, alternatives, why now, contradiction]

### Options
| Option | Target | Value Thesis | Trade-offs | Right-to-Win | Key Unknown | Reversibility |

### Recommended Strategy
[choices, not feature list]

### Explicit Non-Goals
[what we will not do and why]

### Metrics and Guardrails
[only validated or clearly labelled candidate metrics]

### Capability Choices
[Build / Buy / Partner / Unknown with rationale]

### Right-to-Win / Defensibility
[mechanism + evidence, or NOT YET ESTABLISHED]

### Strongest Rejection Case
[best argument against this strategy]

### Falsification Plan
[tests and pivot/kill triggers]

### Decision
[COMMIT | TEST | HOLD | REFRAME | NO STRATEGY DECISION YET]

### What Would Change the Recommendation
[specific evidence]
```

## Notes

- Executive brevity must not erase uncertainty.
- Trade-offs are mandatory for strategy; fabricated precision is not.
- Early-stage strategies should often look like falsifiable theses rather than final answers.
- A moat is an outcome of a defensibility mechanism, not a label.
