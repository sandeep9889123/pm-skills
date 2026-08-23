---
name: user-personas
description: "Create evidence-backed behavioral personas from research data, or clearly labeled hypothesis personas when evidence is insufficient. Avoids forced persona counts, invented demographics, and unverified quotes. Use when synthesizing interviews, surveys, usage data, or segment research into actionable user archetypes."
---

# Evidence-Backed User Personas

## Purpose

Create useful user archetypes for **$ARGUMENTS** without inventing “research-backed” personas when the research is missing, sparse, or contradictory.

> **A persona is a synthesis of evidence, not a creative-writing character.**

## Step 1: Classify the Evidence State

Before creating personas, determine which mode applies.

### RESEARCH-BACKED

Enough user evidence exists to support recurring behavioral/JTBD patterns.

### PROVISIONAL

Some evidence exists, but sample size, coverage, or consistency is too weak for strong segmentation.

### HYPOTHESIS-ONLY

Little or no user research exists.

In this mode, do **not** call the output research-backed personas. Call them **Hypothesis Personas** and list what must be validated.

## Step 2: Inspect the Data Before Choosing the Number of Personas

Do not force exactly three personas.

Use the smallest number of personas that captures meaningful differences in:

- job to be done
- trigger/context
- behavior/workflow
- pain severity
- desired outcome
- buying/adoption constraint
- current alternative

If the evidence supports two meaningful groups, create two.

If it supports four, create four.

If it supports no stable grouping, say that segmentation is not yet supported.

## Step 3: Prefer Behavioral Segmentation Over Decorative Demographics

Use demographics only when they materially explain behavior or buying needs.

Do not invent:

- age
- salary
- company size
- title
- geography
- family status
- technical skill

unless supported by the provided research or explicitly framed as a hypothesis.

Prefer:

- situation
- frequency
- workflow
- motivation
- JTBD
- constraints
- workaround
- decision criteria

## Step 4: Preserve Evidence Provenance

For each important persona attribute, distinguish:

- **OBSERVED**: directly supported by research
- **INFERENCE**: interpretation across observations
- **HYPOTHESIS**: plausible but unverified
- **UNKNOWN**: evidence unavailable

Do not convert one participant's behavior into a segment-wide property without support.

## Step 5: Verify Quotes

If using a verbatim quote:

- confirm the wording appears in the source transcript
- preserve meaning and context
- never polish a paraphrase into quotation marks

If exact verification is not possible, use a paraphrase without quotation marks or label `[UNVERIFIED QUOTE - do not cite]`.

## Step 6: Test Persona Distinctness

Before finalizing, ask:

- Do these personas have meaningfully different jobs, constraints, or product decisions?
- Would we build, position, onboard, price, or support differently because of this distinction?
- Are two personas actually the same user with cosmetic demographic differences?

Merge personas that do not change a product decision.

## Step 7: Contradiction Pass

Look for evidence that does not fit the proposed personas.

Ask:

- Which users are poorly represented?
- Is a dominant interviewee/outlier driving the segmentation?
- Do survey and interview signals disagree?
- Did we segment based on our product architecture rather than user behavior?
- Is there enough evidence to claim this pattern is recurring?

Surface meaningful exceptions rather than forcing every user into a persona.

## Output

```markdown
## Persona Synthesis: [Product / Problem]

**Evidence mode:** RESEARCH-BACKED / PROVISIONAL / HYPOTHESIS-ONLY
**Evidence coverage:** [interviews / surveys / usage / files]
**Segmentation confidence:** High / Medium / Low

### Segmentation Logic
[What behavioral/JTBD dimensions separate the groups and why they matter]

### Persona 1: [Descriptive behavioral name]

**Core situation / trigger**

**Primary JTBD**

**Current workflow / alternative**

**Key pains / constraints**

**Desired outcomes**

**Decision / adoption criteria**

**Evidence**
| Attribute | Evidence | Type | Confidence |
|---|---|---|---|

**Product implication**
[What decision changes because this persona exists]

**Unknowns / hypotheses**
[What still needs validation]

[Repeat only for personas supported by the evidence]

### Cross-Persona Differences
| Dimension | Persona A | Persona B | Why it matters |
|---|---|---|---|

### Users / Evidence That Do Not Fit Cleanly
[Exceptions, outliers, contradictions]

### Research Gaps
[What evidence would most improve segmentation confidence]
```

## Hard Failures

Do not:

- force exactly three personas because a template asks for three
- call a persona research-backed when no research was provided
- invent demographics or quotes
- create multiple personas that differ only cosmetically
- hide users who contradict the segmentation
- claim one interview establishes a recurring segment
- use `UNKNOWN` evidence as if it were observed behavior

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
