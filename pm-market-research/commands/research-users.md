---
description: Evidence-first user research synthesis — personas/segments/journeys only when supported, with sampling limits and hypothesis labels
argument-hint: "<research data, survey results, feedback, analytics, or product context>"
---

# /research-users -- Evidence-First User Research Synthesis

Turn available research into decision-useful user understanding without converting thin or biased evidence into invented personas, segment prevalence, or lifecycle claims.

## Step 1: Resolve the Decision and Evidence Mode

Capture:

- product / problem / geography
- decision this research informs
- data sources and date range
- sample/recruitment/source mechanism
- unit: user, buyer, account, workflow, etc.
- known underrepresented groups

Choose a mode:

- `EVIDENCE MODE`: actual research/behavioral data is available
- `HYPOTHESIS MODE`: only product/market context is available

In hypothesis mode, never call outputs research-backed or attach invented prevalence.

## Step 2: Evidence Inventory and Limitations

Create:

| Source | Sample / population | What it supports | Bias / limitation | Freshness |
|---|---|---|---|---|

Tool/file failure means `coverage incomplete / UNKNOWN`, not absence.

## Step 3: Personas, Only if Decision-Useful

Apply **user-personas**.

- Do not force 3-4 personas.
- Use only the number supported by evidence.
- If evidence does not support distinct personas, return `DO NOT CREATE PERSONAS YET`.
- Verify verbatim quotes; otherwise paraphrase.
- Do not infer prevalence from a non-representative sample.

## Step 4: Segment Users/Accounts

Apply **user-segmentation** and **market-segments**.

- define the segmentation unit
- distinguish observed segments from hypotheses
- do not invent size, WTP, engagement, growth, or “highest value”
- compare segment priority only using evidence-backed criteria
- check whether apparent segments are actually channel, tenure, geography, plan, or sampling artifacts

Return `DO NOT SEGMENT YET` if the evidence does not support a decision-useful segmentation.

## Step 5: Journey, Only at the Right Scope

Apply **customer-journey-map** to the actual job/workflow.

Do not force a generic Awareness → Advocacy lifecycle when the research concerns a narrower operational journey.

For each stage distinguish:

- `OBSERVED`
- `INFERENCE`
- `UNKNOWN`

Do not invent emotions, drop-offs, or “aha moments” that are absent from the evidence.

## Step 6: Contradiction Pass

Before recommendations:

- preserve minority/negative evidence
- identify patterns that contradict the dominant narrative
- inspect sample/source concentration
- state which conclusions would change with a more representative sample

## Output

### Research Decision
[what this analysis should change]

### Evidence / Sample Profile
[sources, coverage, limitations]

### Personas
`SUPPORTED | HYPOTHESIS-ONLY | DO NOT CREATE YET`

### Segmentation
`SUPPORTED | HYPOTHESIS-ONLY | DO NOT SEGMENT YET`

### Journey Evidence
[scoped journey with observed/inferred/unknown states]

### Findings
| Finding | Evidence state | Support | Confidence | Decision implication |
|---|---|---|---|---|

### Contradictions / Minority Signals
[what challenges the main story]

### Unknowns / Next Research
[cheapest decision-changing evidence]

### Decision
`ACT ON EVIDENCE | VALIDATE HYPOTHESES | COLLECT MORE DATA | REFRAME RESEARCH`

Do not output unsupported percentages or universal user claims.
