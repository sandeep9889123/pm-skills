---
description: Evidence-first feedback analysis — sentiment and themes with explicit method, sample bias, quote verification, and observed-vs-inferred separation
argument-hint: "<feedback data as CSV, text, or file>"
---

# /analyze-feedback -- Evidence-First Feedback Analysis

Analyze reviews, surveys, tickets, NPS comments, or other feedback without turning a biased corpus into false population precision.

## Step 1: Define Corpus and Decision

Capture:

- decision this analysis informs
- feedback source/channel
- period and product/version scope
- unit of analysis
- record/respondent/account count if known
- metadata available
- selection mechanism and likely bias

If files/sources are inaccessible, mark coverage `UNKNOWN / incomplete`.

## Step 2: Apply Sentiment Analysis Reliability Rules

Use **sentiment-analysis**.

- Define the classification/scoring method before scoring.
- Do not generate an arbitrary average sentiment score.
- Do not derive an NPS proxy from free text. Use actual NPS rating data only when present.
- Do not force segments/themes.
- Verify direct quotes against source text.
- Keep `OBSERVED` feedback separate from `INFERENCE` about root cause or business impact.

## Step 3: Data Quality and Bias Checks

Check where possible:

- duplicates / repeat reporters
- source/channel concentration
- missingness
- language/translation uncertainty
- one large account/user dominating volume
- sample size per segment
- collection-method changes over time

Do not infer prevalence in the full customer base unless the sample supports it.

## Step 4: Themes and Segment Differences

For each theme report:

| Theme | Evidence | Record/account count | Sentiment mix | Severity | Segment/source | Confidence |
|---|---|---:|---|---|---|---|

For segment/time comparisons show denominators and flag small-N results.

## Step 5: Contradiction and Root-Cause Pass

- preserve minority signals
- find feedback contradicting the dominant theme
- distinguish requested features from underlying needs
- treat root cause as hypothesis unless independently supported
- check whether a trend is really a change in channel/customer mix

## Output

### Corpus / Method
[source, period, sample, bias, sentiment method]

### Sentiment Distribution
[counts/rates only where denominator supports them]

### Themes
[evidence-backed table]

### Segment / Time Differences
[with sample sizes and caveats]

### Verified Quotes
[verbatim only when source-verifiable]

### Root-Cause Hypotheses
| Hypothesis | Evidence for | Evidence against | Validation |
|---|---|---|---|

### Action Priority
Prioritize by severity, frequency, strategic/customer impact, confidence, and reversibility.

### Decision
`ACT NOW | INVESTIGATE | MONITOR | INSUFFICIENT EVIDENCE`

If structured input is enriched with labels, preserve the original raw text and state the classification method so results are auditable.
