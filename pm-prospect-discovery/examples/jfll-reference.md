# JFLL Reference Pattern

## Why this example matters

This reference captures the reusable pattern from a pre-RFP discovery artifact created for Jet Freight Logistics Ltd. The specific freight questions are not the reusable IP. The reusable IP is the structure used to test a proposed use-case path before a formal proposal.

## Initial hypothesis

A Phase 1 `Quote-to-Booking` wedge was proposed for internal sales/operations users before a later customer self-service experience.

The workshop explicitly positioned the wedge as a working direction to shape together rather than a final requirement.

## Journey pattern

The proposed flow was decomposed into sequential waypoints:

1. Systems and API landscape
2. Shipment intake
3. Commercial logic and rate engine
4. Routing, carrier, and consolidation options
5. Quotation and comparison
6. Booking and operational handoff
7. Tracking and milestones
8. Customer self-service portal, deliberately deferred

## Three-direction pattern

For major stages, the workshop offered three ways to build:

- Industry-Standard
- Vision-Aligned
- Out-of-the-Box / differentiated

This helped the prospect react to concrete options while keeping them as hypotheses.

## Question pattern

Each waypoint paired the proposed direction with current-state discovery questions.

Examples of the question intent included:

- what systems and APIs exist
- what fields and rules are required
- where rates live and how they change
- how routing and consolidation work
- which quotes require approval
- what data operations needs at booking
- which tracking milestones exist today

The reusable principle is to ask for current operational behavior after presenting the hypothesis.

## Capability ownership pattern

The workshop explicitly captured who provides each capability:

- existing vendor API
- existing vendor with new API
- project scope

This is a strong mechanism for preventing scope ambiguity.

## Assumption pattern

Planning assumptions were numbered and could be:

- Confirmed
- Denied
- Partially Correct

The generalized plugin extends this to:

`UNTESTED | CONFIRMED | DENIED | PARTIAL | UNKNOWN`

## Deferred scope pattern

Customer self-service was shown for context but deliberately marked as Phase 2+ rather than allowing strategic ambition to inflate Phase 1.

## Post-session pattern

The artifact included:

- open questions
- progress capture
- session summary
- export
- follow-up actions

## Reuse rule

Do not copy the freight questionnaire into another prospect.

Reuse this pattern:

`hypothesis -> stages -> options -> current-state questions -> ownership -> assumptions -> deferred scope -> synthesis -> readiness`
