---
name: tool-evaluation-selection
description: "Evaluate and select enterprise PM, AI, sales, analytics, or automation tools using weighted requirements, workflow fit, integrations, security, TCO, switching cost, evidence quality, and pilot results. Use for build-vs-buy or vendor/tool selection decisions."
---

# Tool Evaluation and Selection

## Purpose

Choose a tool based on the target workflow and constraints, not feature-count marketing or first-page search results.

## Method

1. **Define decision and workflow**
   State what job the tool must improve, users, volume, critical integrations, data sensitivity, geography/compliance, budget, implementation capacity, and non-negotiables.

2. **Separate requirement types**
   - `HARD GATE`: failure eliminates vendor
   - `WEIGHTED`: contributes to fit score
   - `PREFERENCE`: tie-breaker
   - `UNKNOWN`: requires validation

3. **Build candidate set broadly**
   Search direct tools, adjacent categories, existing-stack capabilities, open-source, internal build, and do-nothing/process redesign. Run a search-exhaustion/contradiction pass before declaring no alternatives.

4. **Evidence hierarchy**
   - official docs/security pages for declared capabilities
   - hands-on pilot for workflow behavior
   - credible independent evidence for usability/reliability
   - community/reviews as signals, not facts
   - sales claims remain unverified until demonstrated

5. **Evaluate total fit**
   Score workflow fit, quality, integrations, APIs, admin/RBAC, security/privacy, auditability, reliability, support, implementation effort, change management, vendor viability, extensibility, exit/export, and TCO.

6. **Model economics**
   License/usage + implementation + integration + admin + review + training + migration + expected failure cost + switching/exit cost. Compare against baseline and build option.

7. **Pilot design**
   Use real representative workflows including worst-case/edge inputs. Define acceptance gates before pilot. Do not let a polished vendor demo substitute for testing.

## Anti-patterns

- scoring 100 features equally;
- awarding points for capabilities no one needs;
- vendor claims treated as verified;
- choosing lowest license price while ignoring implementation/TCO;
- ignoring lock-in/export;
- testing only clean happy-path data;
- using one analyst quadrant as the decision.

## Output

### Decision matrix
| Requirement | Type/weight | Candidate evidence | Confidence | Gap |
|---|---|---|---|---|

### TCO and risk view
Show ranges and load-bearing assumptions.

### Recommendation
`SELECT | PILOT | NEGOTIATE | BUILD | KEEP CURRENT | NO DECISION`.

Include runner-up, why it lost, and what new evidence would change the winner.
