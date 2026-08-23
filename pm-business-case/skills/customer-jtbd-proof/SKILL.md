---
name: customer-jtbd-proof
description: "Validate ICP, user, buyer, economic buyer, JTBD, workflow pain, urgency, alternatives, adoption friction, and willingness to change for a business case. Use when customer evidence must be separated from persona or demand speculation."
---
# Customer and JTBD Proof

## Objective

Establish whether a real customer or internal user has a sufficiently important problem to justify investment.

Do not fabricate personas, quotes, pain severity, workflow frequency, budgets, willingness to pay, procurement behavior, or adoption intent.

Follow `pm-business-case/references/EVIDENCE_CONTRACT.md`.

## Step 1: Separate actors

Do not collapse "customer" into one persona.

Identify only actors supported by evidence or clearly label hypotheses:

- end user
- workflow owner
- buyer
- economic buyer
- technical approver
- security or compliance approver
- procurement
- executive sponsor
- blocker
- beneficiary

For each actor record:

- job in the decision or workflow
- success outcome
- pain or risk
- incentive
- authority
- evidence state

If the business case assumes the user is also the buyer, verify it.

## Step 2: Define JTBD from evidence

Use the structure:

`When [situation], [actor] wants to [motivation/job], so they can [outcome], despite [constraint].`

A JTBD is not a feature request or product description.

Link each JTBD to evidence claim IDs.

If no customer evidence exists, label the JTBD `HYPOTHESIS` through the ASSUMPTION or PROPOSAL evidence states. Do not present it as validated insight.

## Step 3: Map current workflow

Document:

1. trigger
2. current steps
3. systems or tools
4. handoffs
5. decision points
6. exceptions
7. delays
8. rework
9. failure consequences
10. current workaround

Differentiate observed workflow from assumed workflow.

## Step 4: Quantify pain carefully

For each pain point capture only what evidence supports:

- frequency
- duration
- labor effort
- error rate
- delay
- revenue impact
- cost impact
- compliance risk
- customer impact
- opportunity cost

Do not convert qualitative frustration into invented dollar value.

If quantitative impact is modeled, classify it as ESTIMATE and expose formula, inputs, and sensitivity.

## Step 5: Current alternatives

Ask what the actor actually does today:

- manual process
- spreadsheet
- email
- internal application
- enterprise suite
- vendor tool
- consulting or services
- custom code
- doing nothing

Current alternatives are part of the customer problem, not only the competitor section.

## Step 6: Pain severity and urgency

Assess separately:

- severity if the problem occurs
- frequency of occurrence
- urgency to solve now
- budget availability
- organizational priority
- switching friction

Do not infer urgency from severity.

A painful problem with no budget or timing trigger can still be a weak near-term business case.

## Step 7: Evidence of willingness to change

Strong evidence may include:

- purchase or renewal behavior
- active procurement
- funded initiative
- contract or pilot
- explicit budget
- repeated workarounds with material cost
- user abandonment or escalation
- validated interview evidence
- pricing experiment

Weak evidence includes:

- general enthusiasm
- "this would be useful"
- vendor case studies from unrelated segments
- internal excitement
- survey intent without behavior

Preserve the difference.

## Step 8: Willingness to pay

Never fabricate willingness to pay.

Classify commercial evidence:

- observed transaction
- contract value
- comparable verified pricing
- procurement history
- explicit WTP research
- pricing test
- unsupported assumption

If no WTP evidence exists, pricing remains a PROPOSAL or ESTIMATE and the business case must say so.

## Step 9: Segmentation

Segment by differences that change product or buying behavior, such as:

- workflow
- problem severity
- compliance burden
- scale
- integration complexity
- maturity
- buying motion
- deployment constraints
- economics

Do not invent demographic or firmographic precision because a template expects it.

Do not force exactly three personas or segments.

## Step 10: Customer contradiction pass

Actively look for evidence that challenges the desired conclusion:

- users tolerate the current process because the pain is minor;
- the problem occurs too rarely;
- the buyer is different from the user;
- budget belongs to another function;
- switching costs dominate benefits;
- an incumbent workflow already solves enough of the problem;
- customers want services rather than a product;
- the problem is project-specific rather than reusable;
- the proposed AI or platform element is not required.

Preserve contradictory evidence.

## Minimum evidence gate

A confident customer-problem claim requires evidence for:

- actor
- workflow
- JTBD
- pain
- current alternative
- consequence

A confident commercial problem claim additionally requires credible evidence of willingness to change, pay, or allocate budget.

If evidence is missing, output the minimum validation plan rather than filling gaps.

## Output

### Actor map
User, buyer, economic buyer, approvers, blockers.

### JTBD ledger
JTBD statements with evidence claim IDs and validation status.

### Current workflow
Observed versus assumed steps.

### Pain evidence
Severity, frequency, consequence, and confidence.

### Current alternatives
What is used today and why.

### Switching and adoption friction
Technical, process, behavioral, procurement, and organizational constraints.

### WTP evidence
Observed evidence versus commercial hypotheses.

### Contradictions
Evidence that weakens the customer thesis.

### Validation backlog
Smallest set of interviews, workflow observations, transaction data, pilots, or pricing tests needed to close P0 unknowns.

## Hard stop conditions

Do not claim validated demand when:

- personas are inferred only from generic market knowledge;
- customer quotes cannot be verified;
- WTP is assumed from market size;
- user and economic buyer are not distinguished;
- pain is described but not evidenced;
- the current alternative is unknown;
- customer evidence comes only from vendors selling the proposed solution.
