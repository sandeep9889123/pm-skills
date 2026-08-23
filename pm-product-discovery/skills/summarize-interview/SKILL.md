---
name: summarize-interview
description: "Summarize a customer interview transcript into JTBD, evidence-backed insights, satisfaction signals, verified quotes, and action items. Distinguishes observed evidence from inference and verifies verbatim quotes before use. Use when processing interview recordings or transcripts, synthesizing discovery interviews, or creating interview summaries."
---

# Summarize Customer Interview

Transform an interview transcript into a concise discovery artifact without inventing customer evidence.

## Core rule

> **The transcript is the source of truth. A polished paraphrase is not a verbatim quote.**

## Context

You are summarizing a customer interview for the product discovery of **$ARGUMENTS**.

The user may provide a pasted transcript or an attached transcript/file. Read the full available transcript before synthesizing it.

If the transcript is partial, corrupted, obviously truncated, or inaccessible, state that the evidence set is incomplete.

## Instructions

### 1. Read before interpreting

Read the full available transcript first.

Separate:

- **OBSERVED**: directly stated or clearly described by the participant
- **INFERENCE**: your interpretation of what the participant may mean
- **UNKNOWN**: not established by the transcript

Do not promote inference into observed customer evidence.

### 2. Extract jobs, pains, workarounds, outcomes, and signals

Look for:

- situation/context that triggers the job
- desired outcome
- current solution/workaround
- friction or dissatisfaction
- importance/urgency signals
- switching barriers
- buying/adoption constraints
- evidence of frequency
- evidence of workaround cost
- explicit requests
- contradictions or changes in the participant's own account

Do not infer population-level demand from one interview.

### 3. Verify every verbatim quote

If you include text inside quotation marks as a customer quote, verify that the wording appears in the transcript.

For each proposed quote:

1. search the transcript for a distinctive contiguous phrase from the quote
2. confirm the quote preserves the participant's actual wording and meaning
3. if exact wording cannot be verified, **do not silently repair or rewrite it as a quote**
4. either:
   - convert it into a clearly labeled paraphrase, or
   - mark it `[UNVERIFIED QUOTE - do not cite]`

At the end, report:

> **Quote verification:** X/X verbatim quotes verified

If no quotes are used, say:

> **Quote verification:** No verbatim quotes used

### 4. Preserve uncertainty and contradiction

If the participant gives inconsistent answers:

- surface the inconsistency
- do not choose the answer that best supports the product thesis

If the transcript does not establish importance, frequency, willingness to pay, or satisfaction, use `UNKNOWN` rather than inventing a qualitative rating.

### 5. Avoid research inflation

One interview can reveal:

- a pain
- a behavior
- a workaround
- a hypothesis
- a useful language pattern

One interview does **not** establish:

- market prevalence
- segment-wide demand
- statistical frequency
- product-market fit
- a validated persona
- representative willingness to pay

Label broader implications as hypotheses to test.

### 6. Action items must have provenance

Separate:

- **Participant commitments**: explicitly agreed by the participant
- **Researcher follow-ups**: sensible next actions inferred from the interview

Do not attribute a follow-up to the participant if they never agreed to it.

## Output Template

```markdown
## Interview Summary

**Date**: [date/time if available]
**Participants**: [names/roles if available]
**Research context**: [product / problem / decision]
**Transcript coverage**: [Complete / Partial / Unknown]

### Participant Context

[Role, workflow, relevant background. Use UNKNOWN where not established.]

### Current Solution / Workaround

[What they do today, with evidence.]

### Jobs and Desired Outcomes

| Job / situation | Desired outcome | Evidence | Confidence |
|---|---|---|---|

### Problems / Friction

| Problem | Evidence from transcript | Frequency / importance | Confidence |
|---|---|---|---|

### What Works Today

[What the participant values about the current solution.]

### Key Insights

For each insight:

- **Insight:** [synthesis]
- **Evidence:** [observed statement/behavior]
- **Type:** OBSERVED / INFERENCE
- **Confidence:** High / Medium / Low
- **Implication:** [what this may mean for product/research]

### Verified Quotes

> "[verbatim quote]"

**Quote verification:** [X/X verified / No verbatim quotes used]

### Contradictions / Ambiguities

[Anything the participant said that conflicts, changed during the interview, or remains unclear.]

### Hypotheses to Validate

- [Hypothesis created from this interview, not presented as a fact]

### Action Items

**Participant commitments**
- [Only explicit commitments]

**Researcher follow-ups**
- [Recommended next evidence or follow-up]
```

## Hard Failures

Do not:

- fabricate or polish a paraphrase into a customer quote
- attribute a statement to the participant that is not in the transcript
- claim one interview validates a segment-wide problem
- invent satisfaction, frequency, urgency, willingness to pay, or importance when absent
- hide contradictions because they weaken the product thesis
- silently complete missing transcript sections from context

## Final Self-Check

Before delivering:

- Are all quoted words verifiable in the transcript?
- Did I separate observation from inference?
- Did I avoid population claims from a single interview?
- Did I preserve contradictions and unknowns?
- Are action items correctly attributed?

If any answer is no, revise before delivery.

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
