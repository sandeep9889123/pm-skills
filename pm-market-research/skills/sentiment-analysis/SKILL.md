---
name: sentiment-analysis
description: "Analyze feedback with evidence-backed sentiment, themes, segment differences, and uncertainty. Requires a declared scoring method, representative-sample caveats, quote verification, and separation of observed feedback from inferred root causes. Use for reviews, surveys, support tickets, NPS comments, or qualitative feedback analysis."
---

# Feedback Sentiment & Theme Analysis

## Purpose

Analyze feedback for `$ARGUMENTS` without converting qualitative text into unsupported precision or population-level claims.

The output should answer:

1. What was actually observed in the provided feedback?
2. How representative is the dataset?
3. Which themes/sentiment patterns are robust enough to act on?
4. What remains hypothesis or `UNKNOWN`?

## P0 Reliability Contract

### Hard rules

1. **Do not invent a numeric sentiment score.** A -1..+1 or 0..10 score is allowed only if a scoring/classification method is explicitly defined and applied consistently.
2. **Do not create an NPS proxy from text sentiment.** NPS is based on the 0-10 recommendation question; text sentiment is not a substitute.
3. **Do not force a minimum number of segments or themes.** Return what the data supports.
4. **Do not infer population prevalence from a convenience sample.** App reviews, support tickets, escalations, and opt-in survey responses are selection-biased unless proven otherwise.
5. **Verify verbatim quotes against source text.** Otherwise paraphrase and label it as a paraphrase.
6. **Observed complaint ≠ root cause.** Label causal explanations `INFERENCE` until corroborated by behavior, diagnostics, interviews, or other evidence.
7. **Frequency ≠ importance.** High-severity low-frequency problems and high-value-account issues may matter more than common minor complaints.
8. **Tool/file/translation failure means coverage incomplete / UNKNOWN.** Do not silently drop inaccessible feedback.

## Step 1: Define the Decision and Corpus

Resolve:

- What decision will this analysis inform?
- Feedback source(s)
- Date range
- Product/version/geography/language scope
- Unit of analysis: message, respondent, ticket, review, account, conversation?
- Available metadata: rating, plan, segment, date, revenue/account value, channel?

Create a source inventory:

| Source | Records | Period | Population | Selection mechanism | Known bias / missingness |
|---|---:|---|---|---|---|

If these are unknown, state them as `UNKNOWN`.

## Step 2: Data Quality Gate

Check where possible:

- duplicates / repeated conversations
- bot/spam/templated responses
- missing text or metadata
- language coverage / translation uncertainty
- one user/account contributing many records
- channel mix changes over time
- ratings not aligned with text
- very small segment samples

Do not compare segments or periods when definitions/data collection changed materially without flagging the break.

## Step 3: Define Sentiment Method Before Scoring

Choose one method and document it.

### Preferred interpretable method

Classify each record:

`POSITIVE | MIXED | NEUTRAL/UNCLEAR | NEGATIVE`

Optionally add **intensity** separately:

`LOW | MEDIUM | HIGH`

### Numeric score

Use only if needed and define the mapping explicitly, for example:

`negative=-1, neutral/unclear=0, positive=+1`

If `MIXED` exists, define how it is handled. Report counts/distributions alongside any mean; never imply the numeric mapping is a validated psychological scale.

## Step 4: Theme Extraction

For each theme capture:

| Theme | Evidence | Record/account count | Sentiment mix | Severity | Segments | Confidence |
|---|---|---:|---|---|---|---|

Keep separate:

- observed need/problem
- requested feature/solution
- inferred root cause
- business/product consequence

Do not turn a requested solution into the underlying need without analysis.

## Step 5: Segment Analysis

Use existing metadata when available. If segments are inferred from the text, label them as `HYPOTHESIS` and avoid invented prevalence.

For comparisons show:

- denominator / sample size
- source/channel mix
- absolute counts and rates when appropriate
- uncertainty for small samples

Look for Simpson's-paradox-style reversals: overall sentiment may worsen because the mix of segments/channels changed even when each segment was stable.

## Step 6: Contradiction and Minority Pass

Before concluding:

- identify evidence contradicting the dominant theme
- inspect minority/high-severity feedback
- check whether one account/user is dominating mentions
- compare positive and negative evidence for the same feature/workflow
- distinguish new issue vs longstanding issue when dates exist

Do not erase disagreement to create a cleaner narrative.

## Step 7: Root Cause Discipline

Use states:

- `OBSERVED`: directly present in feedback/data
- `INFERENCE`: plausible interpretation
- `ASSUMPTION`: unverified explanation used to proceed
- `UNKNOWN`: insufficient evidence

A root-cause claim needs more than sentiment text unless the respondent directly explains the cause and the claim is scoped to that respondent.

## Output

### Analysis context
- decision
- corpus and period
- sample/selection limitations
- sentiment method

### Sentiment distribution
Use counts/percentages only when denominators are known and meaningful.

### Evidence-backed themes
| Theme | Observed evidence | Volume | Sentiment | Severity | Confidence | Implication |
|---|---|---:|---|---|---|---|

### Segment / time differences
[with denominators and caveats]

### Verified quotes
Only source-verifiable verbatim quotes. Otherwise use paraphrases.

### Contradictions / minority signals
[what does not fit the dominant story]

### Root-cause hypotheses
| Hypothesis | Supporting evidence | Contradicting evidence | Next validation |
|---|---|---|---|

### Decision
`ACT NOW | INVESTIGATE | MONITOR | INSUFFICIENT EVIDENCE`

Prioritize actions by severity, frequency, strategic/customer impact, confidence, and reversibility. State what evidence would change the recommendation.

---

### Further Reading

- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
