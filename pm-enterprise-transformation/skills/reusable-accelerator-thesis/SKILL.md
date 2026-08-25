---
name: reusable-accelerator-thesis
description: "Decide whether repeated delivery work should remain bespoke, become a method, reusable accelerator, productized solution, or platform capability. Use when evaluating reusable IP, solution factories, internal accelerators, and platformization opportunities without over-claiming reuse."
---

# Reusable Accelerator Thesis

## Operating principle

Turn repeated delivery work into a falsifiable reuse thesis.

The goal is not to label existing code, prompts, templates, or delivery know-how as IP. The goal is to prove that reuse reduces time, cost, risk, defects, presales effort, implementation effort, or improves sales conversion across multiple contexts.

Never claim reusable IP until reuse has been demonstrated beyond the originating project.

## Non-negotiable rules

1. One project does not prove accelerator potential.
2. A reusable code asset is not automatically a reusable business capability.
3. Reuse must reduce marginal effort, risk, cycle time, or improve commercial conversion.
4. Client-specific variation must be measured, not hand-waved.
5. Maintenance cost must be included.
6. Internal adoption must be tested.
7. Buyer value must be separated from delivery convenience.
8. Open-source, vendor, incumbent, and services alternatives must be considered.
9. Platformization is blocked until repeatable reuse patterns are evidenced.
10. Use `UNKNOWN` rather than claiming commonality without proof.

## Required evidence inventory

Capture:

- repeated use cases
- independent customers/accounts/projects
- variation across customers
- common versus client-specific components
- delivery effort by stage
- presales effort by stage
- recurring defects and rework
- implementation dependencies
- data and integration dependencies
- security/compliance variation
- ownership and maintenance model
- documentation/test coverage
- existing code/assets/prompts/templates
- buyer value evidence
- sales proof evidence
- willingness-to-pay or packaging signal
- vendor/open-source/incumbent alternatives

Mark every claim as FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, or DECISION_THRESHOLD.

## Decision taxonomy

Classify the opportunity into one of:

| Level | Meaning | Evidence required |
|---|---|---|
| BESPOKE | Remains client/project-specific | variation dominates, reuse weak |
| METHOD | Repeatable delivery approach, not software/IP | playbook improves delivery quality |
| COMPONENT | Reusable module/template/script | common technical unit is reused |
| ACCELERATOR | Configurable package reduces delivery effort | repeatable use, measurable savings |
| PRODUCTIZED SOLUTION | Repeatable offer with sales/implementation motion | buyer value and GTM proof |
| PLATFORM | Shared foundation supporting multiple solution lines | multi-use-case reuse, governance, operating model |
| BUY/PARTNER | External option is cheaper, safer, or faster | alternatives outperform internal build |

Do not jump levels for storytelling convenience.

## Reuse tests

Evaluate:

1. **Repeatability**: does the same job recur across independent customers or internal contexts?
2. **Common-core ratio**: what percentage of workflow, code, logic, prompts, data model, integrations, tests, and operating process is reusable?
3. **Configuration boundary**: can variation be handled through configuration, rules, templates, connectors, or policy, rather than forks?
4. **Economic lift**: does reuse improve delivery time, cost, margin, quality, presales speed, or support load?
5. **Adoption**: will sales, delivery, engineering, and solution teams actually use it?
6. **Differentiation**: does it create advantage or recreate commodity capability?
7. **Lifecycle cost**: who owns versioning, testing, security, docs, compatibility, support, and roadmap?
8. **GTM value**: does it help sell, prove, price, or expand an offering?
9. **Platform trap**: are abstractions being built before 3 or more validated reuse patterns exist?

## Measurement model

Where possible, create before/after or baseline/target metrics:

- discovery time
- solution design time
- build effort
- integration effort
- QA/regression effort
- implementation cycle time
- defect/rework rate
- presales/demo effort
- delivery margin
- support effort
- win-rate or conversion signal
- time to first value

For each metric, capture baseline, sample, period, owner, and confidence.

## Contradiction pass

Actively look for evidence that:

- client-specific variation dominates
- integration differences destroy reuse
- compliance or security requirements fragment the core
- open-source/vendor options are cheaper or safer
- reuse shifts cost from delivery to maintenance without net value
- buyers do not value the reusable layer
- the asset depends on one client process or dataset
- internal teams will bypass it
- a narrower method captures most value with less cost
- the platform ambition is premature

## Required output

### 1. Reuse decision

Decision: BESPOKE / METHOD / COMPONENT / ACCELERATOR / PRODUCTIZED SOLUTION / PLATFORM / BUY-PARTNER / NOT READY

Include confidence and reason.

### 2. Reuse map

| Component/workflow | Common | Variable | Reuse evidence | Maintenance cost | Recommended boundary |
|---|---|---|---|---|---|

### 3. Evidence coverage

| Area | Evidence state | Blocking unknowns |
|---|---|---|
| Repeatability | | |
| Common core | | |
| Configuration boundary | | |
| Economic lift | | |
| Adoption | | |
| Differentiation | | |
| Lifecycle ownership | | |
| GTM value | | |

### 4. Options comparison

Compare BESPOKE, METHOD, ACCELERATOR, PRODUCTIZED SOLUTION, PLATFORM, BUY/PARTNER.

### 5. Falsifiable thesis

Use this form:

> If we standardize [common core] and configure [variation], then across [target contexts] we expect [measurable improvement] without exceeding [maintenance/customization limit].

### 6. Pilot gates

Define:

- baseline
- target
- sample projects/accounts/use cases
- owner
- duration
- success threshold
- kill threshold
- what cannot be proved yet

### 7. Red-team rejection

State the strongest reason not to invest in reuse now.

## Hard stop conditions

Return `NOT READY`, `KEEP BESPOKE`, or `METHOD ONLY` when:

- only one project proves the asset
- common-core ratio is unknown
- variation is not measured
- maintenance owner is absent
- adoption is assumed
- buyer value is unproven
- vendor/open-source alternatives were not assessed
- economics do not include lifecycle cost
- platform claim lacks multiple reuse patterns

## Final self-check

Before delivery, verify:

- I did not label delivery residue as IP.
- I measured reuse, not just described it.
- I separated method, component, accelerator, solution, and platform.
- I included maintenance and adoption costs.
- I compared alternatives.
- I stated what would kill the reuse thesis.
