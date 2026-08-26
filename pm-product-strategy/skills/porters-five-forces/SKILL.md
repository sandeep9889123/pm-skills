---
name: porters-five-forces
description: "Perform evidence-backed Porter's Five Forces analysis with explicit market boundaries, current source/freshness checks, substitute and entrant search, uncertainty, and strategic implications. Avoids fabricated force ratings and generic industry-attractiveness claims."
---

# Evidence-Backed Porter's Five Forces

## Purpose

Use Porter's framework for `$ARGUMENTS` to understand structural pressure on value capture within a **defined market boundary**.

The framework is a lens, not evidence. Do not populate forces with generic industry stereotypes.

## P0 Reliability Contract

1. Define the industry/market, geography, customer, value chain, and time horizon before rating forces.
2. **Do not invent competitors, suppliers, buyer concentration, switching costs, margins, regulation, entry barriers, market growth, or substitutes.**
3. Rate a force only when evidence is sufficient. `UNKNOWN / MIXED` is valid.
4. Preserve source freshness. Fast-changing markets, AI/software categories, regulation, and platform ecosystems require current evidence.
5. A weak search or unfamiliar category does not mean substitutes/entrants are absent.
6. Separate structural market facts from company-specific right-to-win. A structurally difficult industry may still be attractive to a particular position, and vice versa.
7. Tool/search failure means coverage incomplete.

## Step 1: Define the Arena

State:

- customer/buyer
- job/outcome
- geography
- product/service boundary
- upstream suppliers/dependencies
- downstream buyers/channels
- time horizon

Test at least one plausible narrower/broader boundary. Force ratings can change materially with market definition.

## Step 2: Evidence Ledger

For each force collect material current evidence:

| Claim | Force | Evidence state | Source/date | Confidence | Contradiction |
|---|---|---|---|---|---|

Use `FACT`, `INFERENCE`, `ASSUMPTION`, `ESTIMATE`, `UNKNOWN`, `STALE`.

## Step 3: Competitive Rivalry

Assess evidence for:

- number/concentration of credible rivals
- differentiation and switching
- growth vs capacity pressure
- fixed-cost/price dynamics where relevant
- consolidation/exit behavior
- strategic intensity

Do not infer rivalry from competitor count alone.

## Step 4: Supplier Power

Define the actual scarce inputs/dependencies, for example:

- critical data
- cloud/model/API providers
- distribution platforms
- labor/expertise
- hardware/components
- licensed content/IP

Assess concentration, switching cost, substitutability, forward integration, contract terms, and dependency criticality only when supported.

## Step 5: Buyer Power

Distinguish user from buyer/payer.

Assess:

- buyer concentration
- procurement leverage
- price sensitivity / budget pressure
- switching and multi-homing
- availability of credible alternatives
- information/transparency
- backward integration / internal build

## Step 6: Threat of Substitutes

Search by **customer job**, not category label.

Include:

- adjacent software/products
- services/consulting
- manual workflows
- internal build
- open-source/commodity alternatives
- non-consumption

Before calling substitute threat low, perform a reasonable alternative search and state coverage limits.

## Step 7: Threat of New Entrants

Assess current evidence for:

- capital/technical/data/regulatory barriers
- distribution access
- trust/brand/reference requirements
- economies of scale/scope
- network/data effects
- switching costs
- incumbent response
- platform/API changes that lower entry barriers

Do not call “AI,” “IP,” or “brand” a barrier without explaining mechanism and durability.

## Step 8: Rate With Confidence

For each force:

`LOW | MEDIUM | HIGH | MIXED | UNKNOWN`

and:

- evidence
- trend
- confidence
- what would change the rating

Avoid pseudo-precision such as 7.4/10 unless a defined scoring method is genuinely useful.

## Step 9: Contradiction and Strategic Implications

Ask:

- Which evidence contradicts the dominant rating?
- Is a company-specific advantage being mistaken for a structural force?
- Does a different segment/geography reverse the result?
- What structural change could alter the next 12-36 months?

Translate only the strongest forces into choices about positioning, build/buy/partner, vertical integration, channel, pricing, or segment focus.

## Output

### Market boundary
### Evidence ledger
### Five Forces
| Force | Rating | Trend | Evidence | Confidence | Strategic implication |
|---|---|---|---|---|---|

### Boundary sensitivity
[how result changes under plausible alternate market definition]

### Contradictions / unknowns
### Strategic response options
### Decision
`ACT ON STRUCTURE | VALIDATE CRITICAL FORCE | REFINE MARKET BOUNDARY | INSUFFICIENT EVIDENCE`

Do not label an industry universally “attractive/unattractive” without tying the conclusion to the defined position and evidence.

---

### Further Reading

- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
