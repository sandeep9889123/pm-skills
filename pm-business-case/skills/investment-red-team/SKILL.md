---
name: investment-red-team
description: "Attack a business case as a skeptical investment committee and produce the strongest rejection case, kill criteria, evidence gaps, and staged decision. Use before leadership review, capital allocation, platform investment, or a build recommendation."
---
# Investment Red Team

## Objective

Try to reject the business case before leadership does.

The purpose is not to make the case sound balanced. The purpose is to find the smallest number of reasons that could make the investment wrong.

Follow `pm-business-case/references/EVIDENCE_CONTRACT.md`.

Do not manufacture risks merely to fill a template. Every factual criticism must itself be evidence-backed or clearly labeled INFERENCE, ASSUMPTION, or UNKNOWN.

## Step 1: Reconstruct the thesis

State the business case in five lines:

1. customer or internal user
2. problem or job
3. proposed investment
4. mechanism of value creation
5. expected business outcome

Then state the critical assumptions that connect each line.

If the thesis cannot be reconstructed cleanly, mark `NOT READY` before deeper review.

## Step 2: Evidence attack

For every P0 claim ask:

- What source establishes this?
- Is the source primary or independent?
- Is it current enough?
- Does it actually support the exact claim?
- Is the claim broader than the evidence?
- Is there contradictory evidence?
- Is a model estimate being presented as an observed fact?
- Is a user assertion being treated as verification?

Any unsupported P0 claim becomes a blocker.

## Step 3: CEO attack

Ask:

- Why now?
- Why this problem?
- What happens if we do nothing?
- What strategic objective does this advance?
- What is the opportunity cost of funding this instead of the best alternative?
- What would make this a distraction?
- Is this a project, capability, accelerator, or product, and what evidence supports that level of ambition?

## Step 4: CTO and architecture attack

Ask:

- Is custom build actually required?
- Could an incumbent, hyperscaler, vendor, open-source tool, or integration solve enough of the problem?
- What is technically unique versus commodity?
- What data, security, observability, evaluation, and operating burden is hidden?
- What happens when models, APIs, dependencies, or schemas change?
- Does the proposed platform architecture precede proof of reuse?

Do not reject on technical complexity alone. Tie complexity to cost, risk, time, or strategic value.

## Step 5: CFO attack

Ask:

- Which benefits are measured versus modeled?
- Which inputs dominate ROI?
- What happens in the bear case?
- Are recurring costs included?
- Are support, human review, integration, presales, and implementation costs included?
- Does the business case confuse TAM with revenue?
- Is payback sensitive to arbitrary adoption or WTP assumptions?
- Is downside bounded?

Recompute key economics where possible.

## Step 6: Sales and GTM attack

Ask:

- Who is the economic buyer?
- What budget does this compete for?
- What trigger creates urgency?
- What proof will sales use?
- Is there a production path after the pilot?
- Is the sales cycle compatible with the model?
- Is the offering a standalone product, feature, bundled capability, or services accelerator?
- What existing account or channel advantage is actually verified?

If the case relies on "we can sell this to existing clients", demand evidence of fit, buyer access, and demand.

## Step 7: Delivery and operations attack

Ask:

- What customer-specific work remains?
- What cannot be standardized?
- Does reuse reduce marginal delivery effort?
- Who owns implementation, support, monitoring, and change management?
- What breaks at scale?
- What happens on exceptions and edge cases?
- Does the operating model require scarce experts?

A reusable code asset is not automatically a scalable delivery model.

## Step 8: Customer attack

Steelman the customer saying no:

- current process is good enough;
- budget is elsewhere;
- switching risk is too high;
- integration effort exceeds benefit;
- another vendor is already approved;
- problem is infrequent;
- value accrues to another team;
- security or governance blocks adoption;
- services are preferred over a platform;
- no appetite exists for another tool.

Identify evidence required to rebut each serious objection.

## Step 9: Competitor attack

Assume competitors respond.

Ask:

- Can an incumbent bundle this?
- Can a hyperscaler commoditize it?
- Can a services competitor replicate it?
- Can the buyer build internally?
- Is the supposed moat merely implementation know-how?
- Does proprietary data really exist and remain exclusive?
- Are switching costs real or imagined?

Moat by assertion is a defect.

## Step 10: Build vs buy vs partner vs do nothing

Re-score all strategic alternatives after the attacks.

A BUILD case must survive the strongest credible BUY, PARTNER, and DO NOTHING alternatives.

If another option wins, recommend it.

Do not protect sunk effort.

## Step 11: PoC falsification review

A valid PoC must contain:

- falsifiable hypothesis
- credible baseline
- representative dataset or sample
- primary metric
- guardrails
- decision threshold
- kill criterion
- failure cases
- explicit statement of what the PoC cannot prove

Reject demos presented as validation.

Reject technical success presented as commercial validation.

## Step 12: Platform and accelerator challenge

For any platform or reusable accelerator claim ask:

- How many distinct use cases have actually reused the common core?
- What percentage of delivery effort is reusable?
- Has marginal implementation effort declined?
- Is there repeatable customer value?
- Is there commercial pull?
- Who owns the platform operating model?
- Would a narrower shared service create most of the value with less cost?

If reuse is not evidenced, downgrade the recommendation to a narrower capability or experiment.

## Step 13: Kill criteria

Define observable conditions that should stop or materially redesign the initiative.

Examples, only when relevant:

- no measurable improvement over baseline;
- no credible buyer or budget;
- implementation effort exceeds threshold;
- recurring cost destroys margin;
- false-positive or error rate exceeds threshold;
- reuse fails to reduce delivery effort;
- incumbent alternative closes the differentiation gap;
- WTP remains below viable economics;
- governance or security constraints make deployment impractical.

Never create arbitrary thresholds. Thresholds must be DECISION_THRESHOLD claims with rationale.

## Step 14: Strongest rejection case

Produce the best concise case for saying no now.

Structure:

### Reject because
1. [highest-leverage reason]
2. [second reason]
3. [third reason]

### Evidence supporting rejection
Claim IDs only.

### What would reverse the rejection
Specific evidence or experiment results.

This section is mandatory even when the final recommendation is BUILD.

## Step 15: Final recommendation

Allowed decisions:

- BUILD
- BUY
- PARTNER
- EXPERIMENT
- DEFER
- KILL
- NOT READY

Use staged commitment where possible.

Prefer:

`approve the next evidence-generating investment`

over
`approve the full platform roadmap`

when uncertainty is still material.

## Hard stop conditions

Return NOT READY or a narrower EXPERIMENT when:

- P0 evidence is missing or stale;
- contradictions are unresolved;
- the business case depends on fabricated or unverified citations;
- customer demand is inferred only from market size;
- right-to-win is asserted rather than evidenced;
- the PoC cannot fail;
- ROI cannot be reconstructed;
- platform reuse is assumed from one project;
- the case has not compared build, buy, partner, and do nothing.
