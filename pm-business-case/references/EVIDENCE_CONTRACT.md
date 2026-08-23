# Business Case Evidence Contract

This contract is mandatory for every skill and command in `pm-business-case`.

## 1. Evidence states

Every material claim must be classified as exactly one of:

- `FACT`: directly supported by accessible evidence.
- `INFERENCE`: reasoned interpretation derived from one or more facts.
- `ASSUMPTION`: unverified condition required for analysis or planning.
- `ESTIMATE`: modeled value derived from explicit inputs and method.
- `UNKNOWN`: evidence is insufficient.
- `STALE`: evidence exists but is no longer sufficiently current for the decision.
- `PROPOSAL`: recommended action, design, commercial model, or future state.
- `DECISION_THRESHOLD`: explicit condition that determines whether a gate passes.

Never relabel an ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, or user assertion as FACT because it makes the business case cleaner.

## 2. Claim provenance

Every decision-critical factual claim must have a claim ID and provenance in `evidence-ledger.json`.

For each sourced claim capture:

- claim text
- evidence state
- decision criticality
- source title or identifier
- source type
- source reference or URL when available
- publication or source date when available
- access date when retrieved externally
- exact supporting excerpt or a precise location marker when permitted
- verification status
- freshness status
- contradiction status

Do not fabricate citations, URLs, page numbers, quotes, authors, publication dates, customer statements, company capabilities, competitor names, market sizes, pricing, benchmarks, or financial values.

If a source cannot be opened, inspected, or otherwise verified, do not cite it as verified evidence.

## 3. Source hierarchy

Prefer evidence in this order when applicable:

1. Primary authoritative evidence: official filings, audited reports, government or regulator data, official product documentation, contractual or internal source-of-truth data supplied by the user.
2. Independent high-quality evidence: reputable research, industry bodies, established analyst material, peer-reviewed work, trusted journalism.
3. Company-authored evidence: product pages, press releases, case studies, pricing pages.
4. Community or anecdotal evidence: forums, social posts, reviews, informal discussions.
5. Unsourced summaries or model memory: never sufficient for a decision-critical FACT.

Company-authored evidence can verify that a company makes a claim. It does not automatically verify that the claim is true.

## 4. User-provided information

Treat user-provided information as one of:

- `USER_PROVIDED_PRIMARY`: the user supplies a source-of-truth artifact or explicitly identifies an authoritative internal fact they own.
- `USER_PROVIDED_CLAIM`: the user states something without verifiable supporting evidence.
- `USER_PROVIDED_LEAD`: the user suggests a competitor, market fact, customer behavior, or other item to investigate.

A user challenge such as "I found a competitor" must trigger independent verification and broader search. It must never be accepted as proof merely because the user asserted it.

## 5. Negative conclusion gate

Never conclude "no competitors", "no demand", "no risk", "no alternatives", "no evidence", or an equivalent absence claim from a weak first pass.

Before a negative competitive or market conclusion, complete all applicable searches:

- direct category terms
- problem and JTBD language
- workflow language
- buyer language
- technology language
- substitutes and manual processes
- build-in-house alternatives
- incumbent suites
- regional players
- niche and emerging entrants
- adjacent categories
- alternative spellings, acronyms, and terminology

Then run a contradiction pass that actively tries to disprove the negative conclusion.

If search or retrieval fails, output `coverage incomplete / UNKNOWN`. Tool failure is not evidence of absence.

## 6. Independent corroboration

Decision-critical FACT claims require either:

- one primary authoritative source that directly establishes the claim, or
- at least two independent credible sources.

Two pages repeating the same press release are not independent corroboration.

When sources disagree, preserve the disagreement and reconcile scope, definitions, dates, geography, methodology, and incentives. Do not average incompatible estimates blindly.

## 7. Numerical integrity

Every material ESTIMATE must include:

- formula or method
- all material inputs
- units
- source claim IDs for sourced inputs
- sensitivity or range where uncertainty is material

Market sizing must not use an arbitrary SOM percentage. SOM should be derived from reachability, ICP, sales capacity, geography, pricing, adoption constraints, and time horizon.

ROI, payback, margin, productivity, implementation savings, and revenue projections must never be presented as factual outcomes when they are modeled assumptions.

## 8. Customer evidence

Never fabricate customer quotes, personas, pain intensity, frequency, willingness to pay, switching behavior, or purchase intent.

If customer research is missing, label the resulting ICP, JTBD, pain, and WTP claims as hypotheses and specify the minimum evidence needed to validate them.

No confident pricing recommendation is allowed without evidence from at least one of: observed transactions, contracts, pricing tests, procurement history, comparable verified pricing, or explicit WTP research. Otherwise pricing remains a PROPOSAL or ESTIMATE.

## 9. Build versus alternatives

Every BUILD recommendation must compare at minimum:

- build
- buy or consume
- partner or integrate
- do nothing or continue current workflow

When relevant, also evaluate open-source and incumbent-platform alternatives.

The business case must state why Fission or the proposing organization has a right-to-win. Market attractiveness alone is not a build rationale.

## 10. PoC and falsification

A PoC must test a falsifiable hypothesis against a credible baseline.

Each PoC must define:

- hypothesis
- baseline
- evaluation dataset or sample
- primary success metric
- guardrail metrics
- decision threshold
- kill criterion
- known failure modes
- what evidence would invalidate the thesis

A demo is not proof of product value. A successful technical PoC is not proof of willingness to pay, repeatability, or platform potential.

## 11. Platform and reusable accelerator gate

Do not recommend platform-level investment from one successful project or one architecture diagram.

A platform or reusable accelerator recommendation requires evidence of reuse across multiple credible use cases or clients, with common components, reduced marginal delivery effort, and commercial or strategic pull.

If reuse is unproven, recommend a narrower capability, PoC, or project-level asset first.

## 12. Decision readiness

Allowed final decisions:

- `BUILD`
- `BUY`
- `PARTNER`
- `EXPERIMENT`
- `DEFER`
- `KILL`
- `NOT READY`

A final BUILD, BUY, or PARTNER recommendation is prohibited when any P0 decision-critical claim remains UNKNOWN, STALE, unverified, or materially contradicted without resolution.

The correct output under insufficient evidence is `NOT READY` or a narrower `EXPERIMENT`, not a confident narrative.
