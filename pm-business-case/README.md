# pm-business-case

Reliability-first business case formation for product managers, founders, strategy teams, and investment committees.

This plugin is designed for decisions where a polished narrative is not enough. It forces evidence before recommendation, separates facts from assumptions, challenges negative conclusions, exposes missing proof, and can stop with `NOT READY` instead of inventing certainty.

## Overview

The core sequence is:

`Signal -> Customer -> JTBD -> Alternatives -> Right-to-win -> Build/Buy/Partner/Do Nothing -> Hypothesis -> PoC -> Evidence -> Economics -> GTM -> Investment Decision -> Reuse -> Platform`

The plugin follows a fail-closed reliability contract:

- Unsupported factual claims are not facts.
- User assertions are inputs or leads until independently verified when verification is possible.
- Negative conclusions require search exhaustion and a contradiction pass.
- Decision-critical numbers require sourced inputs and reproducible formulas.
- Conflicting sources are reconciled, not averaged blindly.
- Missing willingness-to-pay evidence blocks confident pricing claims.
- A platform recommendation requires demonstrated reuse, not architecture enthusiasm.
- Tool or search failure must be reported as coverage incomplete, never converted into evidence of absence.
- If critical evidence is unresolved, the correct decision can be `NOT READY`, `EXPERIMENT`, or `DEFER`.

## Install

### Claude Code

```bash
claude plugin install pm-business-case@pm-skills
```

### Codex CLI

```bash
codex plugin add pm-business-case@pm-skills
```

Claude slash commands are Claude-specific. In Codex, request the equivalent workflow in natural language when command routing is not exposed.

## Skills (6)

### 1. `business-case-orchestrator`
Runs the complete gated business case workflow from decision framing through investment recommendation. It owns stage ordering, stop conditions, evidence readiness, PoC falsification, and final decision logic.

### 2. `evidence-ledger`
Creates and audits claim-level provenance using FACT, INFERENCE, ASSUMPTION, ESTIMATE, UNKNOWN, STALE, PROPOSAL, and DECISION_THRESHOLD states. It prevents unsupported claims and false precision from leaking into executive outputs.

### 3. `opportunity-market-proof`
Tests why-now signals, market structure, competitors, substitutes, internal-build alternatives, regional and emerging players, market sizing, and right-to-win. It includes a search exhaustion gate before any negative competitive conclusion.

### 4. `customer-jtbd-proof`
Validates ICPs, users, buyers, economic buyers, JTBD, workflow pain, severity, frequency, current alternatives, and adoption friction. It does not fabricate personas, quotes, or customer demand.

### 5. `economics-commercial-proof`
Builds transparent investment economics, pricing evidence, unit economics, scenario analysis, GTM wedge, sales motion, implementation economics, and commercialization proof. Every material estimate must be reconstructable.

### 6. `investment-red-team`
Acts as a skeptical CEO, CTO, CFO, Sales leader, operator, and customer. It attacks the thesis, tests build-vs-buy-vs-partner-vs-do-nothing, verifies kill criteria, challenges premature platform claims, and produces the strongest rejection case before any recommendation.

## Commands (5)

### `/pm-business-case:build-business-case`
End-to-end workflow. Produces an evidence-led business case, evidence ledger, assumption register, decision gates, and investment recommendation.

### `/pm-business-case:business-case-evidence`
Research and evidence mode. Builds or refreshes the evidence ledger without forcing a business case narrative.

### `/pm-business-case:business-case-red-team`
Adversarial review mode. Attempts to reject an existing business case and identifies what evidence would reverse the rejection.

### `/pm-business-case:business-case-decision`
Investment committee mode. Converts verified evidence into BUILD, BUY, PARTNER, EXPERIMENT, DEFER, KILL, or NOT READY.

### `/pm-business-case:business-case-refresh`
Refresh mode. Re-checks stale or decision-critical claims, records changed evidence, and updates decision readiness without rewriting verified history.

## Required outputs

A complete run should produce four artifacts when the environment supports file writes:

1. `business-case.md`
2. `evidence-ledger.json`
3. `assumption-register.md`
4. `decision-gates.md`

The evidence ledger can be validated with:

```bash
python pm-business-case/scripts/validate_evidence.py evidence-ledger.json
```

The validator is intentionally conservative. It checks structural proof obligations, not whether the model sounds convincing.

## Decision gates

| Gate | Question | Fail-closed outcome |
|---|---|---|
| G0 | Is the decision and scope explicit? | Clarify scope or mark NOT READY |
| G1 | Are decision-critical claims traceable and verified? | Stop narrative promotion |
| G2 | Is there credible market and customer pain evidence? | EXPERIMENT, DEFER, or KILL |
| G3 | Are alternatives and right-to-win understood? | No BUILD recommendation |
| G4 | Is the solution hypothesis falsifiable against a baseline? | Define PoC before investment |
| G5 | Are economics and commercial assumptions reconstructable? | No confident ROI or pricing claim |
| G6 | Did the thesis survive adversarial review? | NOT READY, DEFER, or KILL |

## Anti-hallucination behavior

This plugin does not promise that an LLM can never generate an incorrect token. Instead, it is designed so unsupported decision-critical content cannot legitimately pass as verified evidence.

The workflow must:

- say `UNKNOWN` when evidence is missing;
- say `coverage incomplete` when retrieval fails;
- distinguish user-provided claims from independently verified facts;
- preserve contradictions;
- record source dates and freshness;
- refuse fabricated citations, customer quotes, competitor names, market sizes, pricing, or ROI inputs;
- require evidence before a final investment recommendation.

## Recommended usage

Use `build-business-case` for new capabilities such as AI agents, knowledge graph platforms, enterprise accelerators, new SaaS products, internal platforms, GTM investments, or major feature bets.

Use `business-case-evidence` first when the topic is poorly understood or research coverage is uncertain.

Use `business-case-red-team` before leadership review, capital allocation, sales commitment, or platform-level investment.
