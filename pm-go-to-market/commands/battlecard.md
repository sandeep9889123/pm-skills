---
description: Create an evidence-led competitive battlecard with verified claims, buyer context, proof gaps, and objection handling
argument-hint: "<your product> vs <competitor>"
---

# /battlecard - Evidence-Led Competitive Battlecard

Create a concise sales battlecard without inventing competitor weaknesses, pricing, win/loss patterns, customer stories, proof points, or deal outcomes.

## Reliability Contract

- Treat every competitor claim as time-sensitive. Verify current capabilities, packaging, positioning, and published pricing where possible.
- Reviews, forums, analyst commentary, and sales anecdotes are evidence inputs, not universal truths about the competitor.
- Do not state `we win when`, `we lose when`, or `we typically win/lose because` without actual win/loss or deal evidence. Use `HYPOTHESIS` when evidence is absent.
- Never invent a competitor weakness to create a "landmine".
- Never fabricate customer stories, TCO proof, implementation results, benchmarks, or pricing.
- Separate public competitor facts from internal claims about our own product. If internal product capability is not verified, mark it `UNVERIFIED INTERNAL CLAIM`.
- Distinguish user, champion, buyer, procurement, security, and executive concerns when the purchase is multi-stakeholder.
- If evidence is stale or incomplete, output `REFRESH EVIDENCE` rather than a confident sales assertion.

## Workflow

### Step 1: Define the Competitive Situation

Capture:
- our product / offer
- competitor or alternative
- target account/segment
- buyer and other stakeholders
- deal context: new evaluation, displacement, renewal, expansion
- known evaluation criteria
- internal win/loss evidence if available

### Step 2: Build an Evidence Table

Apply **competitive-battlecard** and current research where available.

For each material claim capture:
- claim
- evidence/source
- date/freshness
- scope (plan, geography, segment, product version)
- state: `VERIFIED | PARTIAL | UNKNOWN | STALE`

Research:
- official product capabilities and documentation
- current positioning
- published pricing/package terms
- implementation / ecosystem constraints
- credible review themes
- recent strategic changes when relevant

Do not require a fixed number of proof points.

### Step 3: Compare on Buyer-Relevant Jobs

Build comparison dimensions from the prospect's decision criteria and JTBD, not from a feature checklist designed to make us look better.

For each dimension state:
- why it matters to this buyer
- our evidence
- competitor evidence
- trade-off
- unresolved question

A competitor can legitimately be stronger on a dimension. Preserve that result.

### Step 4: Objections and Discovery Questions

For each likely objection:
- acknowledge factual competitor strengths when supported
- respond using verified differentiation
- attach proof point or mark `PROOF GAP`
- avoid FUD, unverifiable security/performance claims, or disparagement

Replace manipulative "landmines" with **decision-revealing questions** that surface buyer requirements, for example:
- "How important is [requirement], and how will you validate it?"
- "What evidence would you require before switching?"

Do not imply the competitor will fail the question unless evidence supports that conclusion.

### Step 5: Win/Loss Patterns

If sufficient internal data exists, summarize:
- sample and period
- segment/deal context
- observed reasons
- contradictory cases
- limitations

Otherwise state:

`WIN/LOSS PATTERN UNKNOWN - collect structured deal evidence.`

### Step 6: Sales Readiness Decision

Outcome:

`READY | READY WITH PROOF GAPS | REFRESH EVIDENCE | NOT READY`

A battlecard with unresolved decision-critical claims should not be represented as fully sales-ready.

## Output

```text
## Competitive Battlecard: [Us] vs [Alternative]

### Use Context
[segment, buyer, deal stage]

### Evidence Freshness
[what is verified, stale, unknown]

### Buyer-Relevant Comparison
| Decision Criterion | Why It Matters | Us | Them | Trade-off | Evidence Status |

### Where We May Have Advantage
[verified or explicitly HYPOTHESIS]

### Where They May Have Advantage
[verified or explicitly HYPOTHESIS]

### Objections
| Objection | Response | Proof | Gap |

### Decision-Revealing Questions
[neutral questions that expose requirements]

### Win/Loss Evidence
[observed patterns or WIN/LOSS PATTERN UNKNOWN]

### Proof Gaps / Refresh List
[claims requiring validation]

### Readiness
[READY | READY WITH PROOF GAPS | REFRESH EVIDENCE | NOT READY]
```

## Notes

- Truthful competitive selling is more durable than adversarial theatre.
- One-page brevity should compress evidence, not delete caveats.
- Win/loss data is valuable only when sample, segment, and decision context are understood.
