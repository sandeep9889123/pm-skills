---
description: Research the competitive landscape with search exhaustion, contradiction checks, evidence confidence, and direct/adjacent/substitute competitor classification
argument-hint: "<your product, market, or competitive question>"
---

# /competitive-analysis -- Reliability-First Competitive Intelligence

Research the competitive landscape without treating a weak first search as proof that the market is empty.

## Invocation

```text
/competitive-analysis AI-powered project management tools
/competitive-analysis Our product vs Notion, Asana, and Monday.com
/competitive-analysis [upload a competitor list or market brief]
```

## Workflow

### Step 1: Define the Competitive Arena

Establish:

- product / problem being solved
- target user and economic buyer
- geography / vertical
- core JTBD or workflow
- what decision this research must inform

Define competitor broadly enough to include products, services, in-house solutions, and workflows that compete for the same outcome or budget.

### Step 2: Run the First Search Pass

Apply the **competitor-analysis** skill.

Build a candidate set across:

- direct competitors
- adjacent competitors
- substitutes
- manual/service alternatives
- in-house/build alternatives
- emerging/regional players

Do not force exactly five direct competitors. Use the number supported by evidence.

### Step 3: Search Exhaustion and Contradiction Pass

Before accepting a small or empty competitive set:

- reformulate the search using category, problem, workflow, buyer, and technology language
- search substitutes and alternatives
- check relevant geography/vertical variants
- check emerging/new entrants
- diversify source classes when tools allow
- explicitly ask: **“If the user told me I missed a competitor, what would I search next?”**

If the user supplies a competitor name, verify it independently before classification.

If coverage remains weak, report **coverage incomplete / UNKNOWN** rather than “no competitors.”

### Step 4: Verify and Classify

For every material competitor, capture:

- competitive type
- why it competes for the same job/budget
- target segment
- current positioning
- evidence source/freshness
- confidence

Separate:

- FACT
- INFERENCE
- ESTIMATE
- UNKNOWN
- STALE

Do not invent private pricing, market share, customer counts, funding, product capabilities, or traction.

### Step 5: Analyze the Highest-Priority Competitors

For each verified player:

- positioning
- target customer / buyer
- JTBD and workflow
- strengths
- verified weaknesses / customer pain
- pricing/business model when public
- GTM/distribution
- recent moves when current evidence exists
- threat level and why

### Step 6: Synthesize the Market

Do not stop at a feature matrix.

Answer:

- Where is the market converging?
- Which competitors are structurally different?
- Which alternatives are most likely to win the same customer budget?
- What appears table stakes?
- What differentiation is actually supported by evidence?
- Which competitor is most strategically dangerous?
- What remains unresolved?

### Step 7: Generate the Competitive Intelligence Brief

```markdown
## Competitive Intelligence: [Product / Market]

### Executive View
- Competitive arena:
- Verified direct competitors:
- Important adjacent/substitute alternatives:
- Highest-priority threat:
- Coverage confidence: High / Medium / Low
- Biggest unknown:

### Search Coverage
[Query framings, source classes, geography/vertical coverage, known gaps]

### Competitive Set
| Competitor | Type | Target | Core job | Why it competes | Confidence |
|---|---|---|---|---|---|

### Detailed Competitor Analysis
[Evidence-backed profiles for highest-priority players]

### Competitive Pattern
[Where the market is converging/diverging]

### Differentiation Opportunities
| Opportunity | Evidence | Why competitors appear weak | Confidence | Cheapest validation |
|---|---|---|---|---|

### Threats
[Threat, mechanism, evidence, recommended response]

### Contradiction / What Could Change This View
[Unresolved players, stale evidence, excluded scopes, assumptions]

### Recommendation
- Double down on:
- Close gap on:
- Avoid competing on:
- Next evidence to obtain:
```

### Step 8: Offer Next Steps

- create a battlecard for a verified competitor
- develop positioning against the highest-priority alternatives
- identify product gaps only after validating whether they matter to the target segment
- schedule a refresh when the market is changing quickly

## Hard Rules

- Never say “no competitors” because one search returned little.
- Never accept a user-supplied competitor as fact without verification.
- Never force a fixed number of competitors by inventing weak matches.
- Never confuse a different category label with a different customer job.
- Never hide unknown evidence behind polished prose.
- Never treat tool failure as market absence.
