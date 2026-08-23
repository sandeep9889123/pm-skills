# PM Skills Upgrade Backlog V1

## Prioritization logic

Priority is based on:

**Hiring signal × user value × defect severity × differentiation ÷ implementation cost**

The fork should fix correctness first, then add differentiated Enterprise AI capability.

---

# P0, ship first

| ID | Work item | Why now | Effort | Differentiation | Upstream candidate |
|---|---|---|---:|---:|---|
| Q-01 | Add PM Skill Quality Standard | Establishes the fork's quality contract | S | High | Maybe |
| Q-02 | Add semantic golden-test harness | Converts quality from prose into executable checks | M | Very high | Maybe |
| R-01 | Add interview quote verification | Prevents fabricated research evidence | S | Medium | Yes |
| D-01 | Correct A/B power / sample-size logic | Fixes a decision-critical quantitative defect | S-M | Medium | Yes |
| E-01 | Add reusable evidence contract | Standardizes fact / inference / estimate / unknown handling | S | High | Maybe |
| AI-01 | Create `pm-enterprise-ai` plugin skeleton | Establishes differentiated fork direction | M | Very high | No, initially |
| AI-02 | Build `ai-evaluation-contract` | Core AI PM capability, reusable across all AI systems | M | Very high | No, initially |
| AI-03 | Build `golden-dataset-design` | Converts business risk into representative eval data | M | Very high | No, initially |
| AI-04 | Build `rag-evaluation` | High-demand AI PM competence | M | Very high | No, initially |
| AI-05 | Build `agent-evaluation` | High-demand agentic PM competence | M | Very high | No, initially |

---

# P1, differentiated operating system

| ID | Work item | Primary signal | Effort |
|---|---|---|---:|
| AI-06 | `ai-use-case-prioritization` | AI product strategy | M |
| AI-07 | `ai-build-buy-partner` | Executive AI judgment | M |
| AI-08 | `model-provider-selection` | Technical-commercial trade-offs | M |
| AI-09 | `human-review-policy` | HITL / risk design | M |
| AI-10 | `cost-latency-quality` | AI unit economics | M |
| AI-11 | `ai-rollout-rollback` | Production readiness | M |
| AI-12 | `ai-observability` | Post-launch ownership | M |
| AI-13 | `ai-ux-trust` | AI product design | M |
| AI-14 | `data-feedback-loop` | Defensibility / learning loop | M |
| ENT-01 | Create `pm-enterprise-product` plugin | Enterprise PM differentiation | M |
| ENT-02 | `buyer-user-admin-map` | Multi-stakeholder product thinking | S-M |
| ENT-03 | `rfp-rfi-analysis` | Enterprise sales/product bridge | M |
| ENT-04 | `integration-strategy` | Platform / ecosystem fluency | M |
| ENT-05 | `implementation-readiness` | Product-to-delivery bridge | M |
| ENT-06 | `enterprise-adoption` | Post-sale product outcomes | M |
| STR-01 | Add executive decision layer to strategy | Principal / Director PM signal | M |
| RES-01 | Add evidence ledger to competitor analysis | Research reliability | S-M |
| RES-02 | Add sensitivity table to market sizing | Investment-quality research | S-M |

---

# P2, executive layer

| ID | Work item | Signal | Effort |
|---|---|---|---:|
| EXE-01 | Create `pm-executive-decision` plugin | Seniority / leadership | M |
| EXE-02 | `decision-memo` | Crisp executive judgment | M |
| EXE-03 | `business-case` | Commercial thinking | M |
| EXE-04 | `investment-case` | Capital allocation | M |
| EXE-05 | `scenario-planning` | Strategic uncertainty | M |
| EXE-06 | `portfolio-prioritization` | Resource allocation | M |
| EXE-07 | `executive-red-team` | Leadership-level challenge | M |
| ENT-07 | `api-product-requirements` | Technical PM | M |
| ENT-08 | `rbac-permissions` | Enterprise security product sense | M |
| ENT-09 | `sla-slo-design` | Reliability / platform fluency | M |
| ENT-10 | `migration-cutover` | Enterprise transition planning | M |

---

# P3, only after evidence of demand

- additional marketing / growth skills
- more generic strategy frameworks
- expanded legal toolkit
- broad prompt collections
- low-signal templates already available elsewhere

---

# Implementation waves

## Wave 1: correctness and quality infrastructure

**Objective:** make the fork demonstrably more trustworthy before making it bigger.

Deliverables:

1. semantic test harness
2. evidence contract
3. quote-verification fix
4. A/B testing correctness fix
5. golden test cases for both defects

**Exit gate:** CI can fail for at least one semantic PM-quality regression, not only file-structure regression.

---

## Wave 2: AI PM evaluation spine

**Objective:** create the smallest coherent Enterprise AI PM plugin.

Deliverables:

1. `ai-evaluation-contract`
2. `golden-dataset-design`
3. `rag-evaluation`
4. `agent-evaluation`
5. `/evaluate-ai-capability` workflow
6. synthetic examples
7. golden regression scenarios

**Exit gate:** a reviewer can run one workflow from business objective to launch / hold recommendation and inspect the evidence and thresholds.

---

## Wave 3: enterprise product spine

**Objective:** model the part of enterprise PM work generic frameworks miss.

Deliverables:

1. buyer / user / admin map
2. RFP / RFI analysis
3. integration strategy
4. implementation readiness
5. enterprise adoption
6. `/enterprise-opportunity` workflow

**Exit gate:** workflow connects pre-sales evidence to reusable product decision, delivery readiness and adoption measurement.

---

## Wave 4: executive decision layer

**Objective:** make outputs useful at Principal PM / Director / CEO review level.

Deliverables:

1. decision memo
2. business case
3. scenario plan
4. executive red-team
5. `/decision-review` workflow

**Exit gate:** output is concise enough for executive review while preserving an auditable evidence appendix.

---

# Upstream contribution queue

## Candidate 1: interview quote verification

**Why upstream:** narrow reliability improvement; does not change marketplace positioning.

Proposed behavior:

- verify each direct quote against transcript
- label unmatched quote `UNVERIFIED`
- never silently repair a quote
- report verified / total quote count

## Candidate 2: A/B test power correctness

**Why upstream:** correctness bug in a quantitative decision skill.

Proposed behavior:

- use a power-aware sample-size method
- state assumptions and metric type
- calculate or report achieved power when possible
- avoid promising 80% power from a formula that omits beta

## Candidate 3: evidence-contract guidance for research skills

**Why upstream:** improves reliability without changing core frameworks.

Potential scope:

- market sizing
- competitor analysis
- user research synthesis

Recommend submitting only after the first two focused fixes.

---

# Portfolio / hiring signal

The strongest public story is not:

> "I forked a popular PM repository and added prompts."

It is:

> "I audited a 68-skill PM marketplace, found reliability gaps that structural CI could not detect, added semantic quality gates, fixed decision-critical defects, then extended it with an Enterprise AI PM evaluation system."

That narrative requires executable proof. The backlog is ordered to create that proof early.
