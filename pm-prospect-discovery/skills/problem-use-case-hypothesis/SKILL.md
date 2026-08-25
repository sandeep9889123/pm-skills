---
name: problem-use-case-hypothesis
description: "Convert sparse prospect signals into falsifiable problem and use-case hypotheses, including alternative root causes and ranked wedges. Use when Sales or leadership proposes a solution path before formal RFP discovery."
---

# Problem and Use-Case Hypothesis

Do not begin with a solution label.

## Problem hypothesis

Use:

`We believe [user/operator/buyer] experiences [problem] during [job/workflow], causing [consequence], based on [evidence].`

Then list:

- supporting evidence
- missing evidence
- at least two alternative root causes
- what would falsify the problem hypothesis

Examples of alternative root causes include:

- process design
- policy
- incentives
- ownership
- data quality
- system configuration
- fragmented responsibilities
- low adoption of an existing capability

## Use-case wedges

Generate up to three plausible wedges and rank them on:

- evidence strength
- pain severity
- frequency / scale
- business value
- data availability
- integration feasibility
- time to proof
- strategic differentiation
- operational change burden
- delivery risk

Do not use false precision. A simple High / Medium / Low rating is acceptable when evidence is weak.

## Hard guard

The user's preferred wedge must not win by default.

If evidence is insufficient, return `HYPOTHESIS ONLY`.

If a lighter process or configuration intervention plausibly solves the problem, include it.

## Output

- problem hypothesis
- alternative root causes
- candidate wedges
- ranking rationale
- falsification evidence
- recommended discovery focus
