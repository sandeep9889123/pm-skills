---
name: investment-red-team
description: "Attack a business case as a skeptical investment committee. Use before leadership review, capital allocation, platform investment, productization, or any BUILD/BUY/PARTNER recommendation that must survive CEO, CTO, CFO, Sales, Delivery, Customer, and competitor objections."
---

# Investment Red Team

## Operating principle

Try to reject the business case before leadership does.

The purpose is not to sound balanced. The purpose is to find the smallest number of reasons that could make the investment wrong, expensive, distracting, unscalable, unsellable, or premature.

Follow `pm-business-case/references/EVIDENCE_CONTRACT.md` when available.

Do not manufacture risks merely to fill a template. Every criticism must be evidence-backed or clearly labeled INFERENCE, ASSUMPTION, UNKNOWN, STALE, or CONTRADICTED.

## Non-negotiable rules

1. Reconstruct the thesis before attacking it.
2. Attack the strongest version of the case, not a strawman.
3. Separate evidence gaps from actual negative evidence.
4. Treat unsupported P0 claims as blockers.
5. Do not accept technical success as commercial proof.
6. Do not accept one project as reusable-platform proof.
7. Do not protect sunk effort.
8. Always compare BUILD, BUY, PARTNER, and DO NOTHING.
9. Always produce the strongest rejection case, even when final recommendation is positive.
10. Prefer staged evidence investment over full roadmap approval when uncertainty is material.

## Step 1: Reconstruct the thesis

State in five lines:

1. target customer or internal user
2. problem or job
3. proposed investment
4. mechanism of value creation
5. expected business outcome

Then list the critical assumptions that connect the lines.

If the thesis cannot be reconstructed cleanly, mark:

`NOT READY: thesis unclear`

## Step 2: Evidence attack

For each P0 claim ask:

- What source establishes this?
- Is the source primary, independent, internal, or user-asserted?
- Is it current enough?
- Does it support the exact claim or only a weaker claim?
- Is there contradictory evidence?
- Is an estimate being presented as an observed fact?
- Is a user assertion being treated as verification?
- Would this claim survive audit by the decision owner?

Any unsupported P0 claim becomes a blocker.

## Step 3: CEO attack

Ask:

- Why now?
- Why this problem?
- What happens if we do nothing?
- What strategic objective does this advance?
- What is the opportunity cost?
- What would make this a distraction?
- Is this a project, reusable asset, accelerator, productized solution, or platform?
- What evidence supports that ambition level?

## Step 4: CTO and architecture attack

Ask:

- Is custom build required?
- Could a vendor, hyperscaler, incumbent suite, open-source tool, integration, or workflow automation solve enough?
- What is technically unique versus commodity?
- What hidden operating burden exists?
- What data, security, observability, evaluation, and governance risks exist?
- What happens when models, APIs, dependencies, schemas, or client environments change?
- Does the architecture assume reuse before reuse is proven?

Tie technical complexity to cost, risk, time, scalability, or strategic value.

## Step 5: CFO attack

Ask:

- Which benefits are measured versus modelled?
- Which inputs dominate ROI?
- What happens in bear case?
- Are recurring costs included?
- Are presales, implementation, support, maintenance, integration, QA, governance, and human review included?
- Does the case confuse TAM with revenue?
- Is payback sensitive to arbitrary adoption, pricing, or WTP assumptions?
- Is downside exposure bounded?
- Is there a cheaper experiment?

Recompute or sanity-check economics when possible.

## Step 6: Sales and GTM attack

Ask:

- Who is the economic buyer?
- What budget does this compete for?
- What trigger creates urgency?
- What proof will sales use?
- What objections will buyers raise?
- Is there a production path after the pilot?
- Is the sales cycle compatible with the model?
- Is the offering a product, feature, bundle, accelerator, or services wrapper?
- What existing account, channel, or credibility advantage is verified?

If the case says `we can sell this to existing clients`, require evidence of fit, buyer access, problem urgency, and demand.

## Step 7: Delivery and operations attack

Ask:

- What customer-specific work remains?
- What cannot be standardized?
- Does reuse reduce marginal delivery effort?
- Who owns implementation, support, monitoring, and change management?
- What breaks at scale?
- What happens on exceptions and edge cases?
- Does the operating model require scarce experts?
- Does the implementation burden destroy margin?

A reusable code asset is not automatically a scalable delivery model.

## Step 8: Customer attack

Steelman the customer saying no:

- current process is good enough
- budget is elsewhere
- switching risk is too high
- integration effort exceeds benefit
- an approved vendor already exists
- problem is infrequent
- value accrues to another team
- security/governance blocks adoption
- services are preferred over a tool
- buyer does not want another system

Identify evidence required to rebut each serious objection.

## Step 9: Competitor and substitute attack

Assume alternatives respond.

Ask:

- Can an incumbent bundle this?
- Can a hyperscaler commoditize it?
- Can a services competitor replicate it?
- Can the buyer build internally?
- Can open source be good enough?
- Is the moat merely implementation know-how?
- Does proprietary data really exist and remain exclusive?
- Are switching costs real or imagined?

Moat by assertion is a defect.

## Step 10: Strategic alternatives attack

Re-score:

- BUILD
- BUY
- PARTNER
- DO NOTHING
- SERVICES-led solution
- OPEN SOURCE or internal toolkit where relevant

A BUILD case must survive the strongest credible alternative. If another option wins, recommend it.

## Step 11: PoC falsification review

A valid PoC must contain:

- falsifiable hypothesis
- credible baseline
- representative sample
- primary metric
- guardrails
- decision threshold
- kill criterion
- failure cases
- what the PoC cannot prove

Reject demos presented as validation. Reject technical success presented as commercial proof.

## Step 12: Platform and accelerator challenge

For platform or reusable accelerator claims ask:

- How many distinct use cases reused the common core?
- What percentage of delivery effort is reusable?
- Has marginal implementation effort declined?
- Is there repeatable customer value?
- Is there sales or strategic pull?
- Who owns the operating model?
- What maintenance burden is created?
- Would a narrower method, shared component, or service create most value with less risk?

If reuse is not evidenced, downgrade to a narrower pilot, method, reusable asset, or experiment.

## Step 13: Kill criteria

Define observable stop or redesign conditions.

Examples when relevant:

- no measurable improvement over baseline
- no credible buyer or budget
- implementation effort exceeds threshold
- recurring cost destroys margin
- error rate exceeds threshold
- reuse fails to reduce delivery effort
- incumbent alternative closes gap
- willingness to pay remains below viable economics
- governance/security blocks deployment

Thresholds must be DECISION_THRESHOLD claims with rationale. Do not invent arbitrary thresholds.

## Required output

### 1. Thesis reconstruction

Five-line thesis and critical assumptions.

### 2. Evidence attack summary

| Claim | Evidence state | Attack | Blocking? | Evidence needed |
|---|---|---|---|---|

### 3. Stakeholder attacks

CEO, CTO, CFO, Sales/GTM, Delivery/Ops, Customer, Competitor.

### 4. Strongest rejection case

#### Reject because

1. highest-leverage reason
2. second reason
3. third reason

#### Evidence supporting rejection

Use claim IDs or clearly labeled UNKNOWNs.

#### What would reverse the rejection

Specific evidence or experiment results.

### 5. Alternatives after red-team

Re-score build, buy, partner, do nothing, and other relevant alternatives.

### 6. Kill criteria

Observable thresholds and triggers.

### 7. Final recommendation

Allowed decisions:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

Use staged commitment when uncertainty remains.

## Hard stop conditions

Return NOT READY or EXPERIMENT when:

- P0 evidence is missing or stale
- contradictions are unresolved
- customer demand is inferred only from market size
- right-to-win is asserted rather than evidenced
- PoC cannot fail
- ROI cannot be reconstructed
- platform reuse is assumed from one project
- build/buy/partner/do-nothing was not compared

## Final self-check

Before delivery, verify:

- I created the strongest rejection case.
- I did not manufacture generic risk.
- I attacked evidence, economics, GTM, delivery, customer, and alternatives.
- I exposed blockers rather than smoothing them.
- I recommended the next evidence-generating decision where full investment is premature.
