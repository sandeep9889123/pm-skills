---
name: interview-script
description: "Create decision-linked customer interview guides that minimize leading questions, confirmation bias, hypothetical demand, and overgeneralization. Uses past behavior, disconfirming probes, sampling context, and explicit evidence limits. Use for discovery interviews, JTBD research, or testing risky assumptions qualitatively."
---

# Customer Interview Script

## Purpose

Design an interview for `$ARGUMENTS` that can **change a product decision**, not merely collect supportive quotes or positive reactions.

Customer interviews produce qualitative evidence. They can reveal mechanisms, language, workflows, alternatives, and hypotheses. A small interview sample does not by itself prove market prevalence, willingness to pay, or causal impact.

## P0 Reliability Contract

### Hard rules

1. **Start from the decision and uncertainty, not the preferred solution.**
2. **Do not ask leading or confirmation-seeking questions.** Include at least one credible disconfirming probe for each load-bearing hypothesis.
3. Prefer **specific past behavior and real recent examples** over hypothetical future intent.
4. “Would you use/buy/pay for this?” is weak evidence. Prefer current spend, search behavior, procurement actions, switching attempts, commitments, and trade-offs.
5. **Do not turn one participant's statement into population evidence.** Capture sampling limits.
6. **Do not fabricate participant context, quotes, budgets, tools, workflows, or decision authority.**
7. If the research objective cannot be answered credibly by interviews alone, say so and recommend complementary evidence.
8. Respect recording/privacy/consent requirements and avoid collecting sensitive information that is not needed for the research decision.

## Step 1: Research Decision Frame

Define:

- decision this interview will inform
- target participant / recruitment criteria
- why this participant can provide relevant evidence
- stage: exploratory discovery vs concept/usability validation vs commercial discovery
- top 1-3 uncertainties
- what evidence would change the current belief
- time available

If the user provides a preferred feature/use case, rewrite it as a neutral hypothesis.

Example:

> Preferred framing: “Validate that AI recommendations would solve onboarding.”
>
> Neutral research question: “Understand where onboarding fails, how users currently recover, and whether recommendation quality is a material constraint relative to other causes.”

## Step 2: Hypothesis / Disconfirmation Map

For each material hypothesis:

| Hypothesis | Why it matters | Supporting evidence to seek | Disconfirming evidence to seek | Decision if false |
|---|---|---|---|---|

Do not ask the participant to validate the hypothesis directly.

## Step 3: Build the Interview Guide

### Opening

- explain learning purpose without pitching
- confirm role/context only as needed
- request recording permission where applicable
- state confidentiality/usage expectations where relevant

### Context and recent behavior

Use specific-event prompts:

- “Tell me about the last time you…”
- “What triggered that?”
- “Walk me through what happened next.”
- “Who else was involved?”
- “What tool/process did you use?”
- “What did it cost in time, money, risk, or delay?”

### Problem / friction

- “What was difficult about that?”
- “What did you try?”
- “What happened?”
- “How often has this happened recently?”
- “When does this *not* cause a problem?”

That last question is a useful contradiction probe.

### Alternatives and switching behavior

- current workaround/product/service/internal process
- why they chose it
- switching attempts
- what prevented change
- procurement/security/integration constraints for enterprise settings

### Priority / economic signal

Prefer observed commitment:

- current spend/cost if the participant knows it
- time/resources already allocated
- active search/evaluation behavior
- approved initiative/budget when directly known
- consequences of leaving the problem unsolved

Do not pressure participants to disclose confidential budget information they are not authorized to share.

### Disconfirming probes

Examples:

- “What is working well enough today that you would not change?”
- “When would solving this not be worth the effort?”
- “What problem would you solve before this one?”
- “What would make a new solution impossible to adopt?”
- “Who might disagree that this is important?”

### Concept discussion, only when appropriate

If the research stage requires showing a concept:

- separate pre-concept behavior evidence from post-concept reaction
- ask comprehension and trade-off questions
- avoid treating compliments as demand
- capture objections and reasons not to adopt

## Step 4: Fit the Timebox

Do not create a bloated questionnaire. Prioritize questions that can change a material decision.

Classify questions:

- `MUST ASK`: decision-changing
- `FOLLOW-UP`: triggered by an answer
- `OPTIONAL`: useful only if time permits

## Step 5: Sampling and Evidence Limits

Add a research note:

- participant/recruitment criteria
- known sampling bias
- current interview count if known
- underrepresented roles/segments
- what can be inferred from this interview
- what **cannot** be inferred

Repeated qualitative patterns are signals; prevalence requires appropriate quantitative/representative evidence.

## Output

### Research decision
[what this interview should change]

### Hypothesis / disconfirmation map
[table]

### Interview guide
[ordered MUST ASK questions + conditional probes]

### Questions to avoid
[leading/hypothetical/pitching questions relevant to this case]

### Note-taking template
- participant ID / role / context
- source type: transcript vs notes
- recent behavior / workflow
- alternatives
- pain / consequence
- observed commitment
- contradictions
- direct quotes with source/timestamp when available
- interpretations separately labeled
- follow-up evidence needed

### Evidence limit
State what a successful interview would and would not prove.

### Decision follow-up
`CONTINUE EXPLORATION | UPDATE HYPOTHESIS | QUANTIFY | TEST CONCEPT | COMMERCIAL VALIDATION | STOP/REFRAME`

---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
