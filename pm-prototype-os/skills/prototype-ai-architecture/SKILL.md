---
name: prototype-ai-architecture
description: "Compare rules/search, prompting, RAG, fine-tuning and agents for an approved AI product. Specify data readiness, behavior contracts, routing/fallback, permissions, evaluation, cost per successful task, observability and recovery."
---
# AI solution architecture

For new tasks apply the 5–10-question and approval gates; continue an already scoped phase without duplicate intake. Preserve the canonical ai-product-prototype-os contract when available. This skill also works independently with the gates and procedure here. Respect ₹0 incremental spending, evidence states and the owner's decisions. No installs, billable resources, deployment or side-effecting tools without applicable authorization.

## Frame the system

Identify user job, observable success, target slices, domain authority, data and tenant boundaries, workflow volume, latency/privacy constraints, current baseline and material unknowns. Preserve claim IDs, freshness and source restrictions. Distinguish prototype viability from production or commercial proof. Tool failure means coverage incomplete / UNKNOWN.

## Compare the mechanism, not model fame

| Option | Hypothesis to test | Evidence needed / failure to probe |
| --- | --- | --- |
| Existing rules, keyword search or process change | Current tools may solve the bounded job | Baseline task quality, maintenance, exceptions and user effort |
| Prompted model | Context and general capability cover the task | Real examples, structured-output checks, unsupported-answer and sensitivity tests |
| RAG | Authorized external evidence improves answers | Corpus readiness, retrieval relevance, freshness, citations, abstention and access filtering |
| Fine-tuning | Stable behavior/style/task patterns need learned adaptation | Licensed representative labels, held-out benefit over simpler baselines, update and serving costs |
| Tool-using agent | Task requires bounded actions or multi-step work | Tool contracts, authority, actual state verification, recovery, loop/delegation budgets and handoffs |

Compare credible alternatives against owner-defined quality, risk, total task cost, latency, operational effort and reversibility. Fine-tuning is not evidence freshness; RAG is not automatically correct; an agent loop is not justified by an impressive demo. Keep unknown APIs, current prices, data rights and capacity as UNKNOWN rather than inventing them.

## Specify the contract and experiment

1. Audit corpus/input ownership, permission, freshness, schemas, duplicates, representative slices and missingness. Define source precedence and the behavior on stale/conflicting or unavailable data.
2. Define accepted input/output schemas, supported/unsupported tasks, uncertainty and abstention behavior, human escalation, tool preconditions and observable final state. Enforce authorization outside model instructions. Treat retrieved documents and tool outputs as untrusted data.
3. Draw data/control flows with tenant boundaries, identity propagation, tools, stores and evidence lineage. Define idempotency, bounded retries, timeout, partial success, compensation and kill switch. For agents include checkpoints, long-session state and worker authority.
4. Specify router signals available before action, eligible models/data boundaries, quality/cost budgets and safe fallback to rules/search/abstention/human review. Cache keys and invalidation must include relevant tenant, permission, source and prompt/model versions. Fallback cannot silently expand authority.
5. Design matched-task trials against the existing baseline. Freeze corpus, prompts, model versions, tools, rubric and judge, and isolate changes or disclose confounding. Evaluate per slice, critical permissions, actual outcomes and the full pipeline's cost and latency.
6. Account for all attempts, failures, retries, retrieval/tool usage and human review. Cost per verified successful task = total nonoverlapping task costs / verified successes; zero successes makes it undefined. Keep currency, price date, missing components and marginal versus fully loaded cost explicit. Do not treat posted token price as task economics.
7. Specify trace/span correlation, safe metadata, final-state verification, quality sampling, drift/incident ownership and rollback evidence. A configured logger or a proposed evaluation is NOT_RUN until observed.

Deliver architecture diagram, mechanism comparison, behavior/data contracts, permission/recovery matrix, evaluation plan, economics worksheet, unknowns and phase handoff. Keep the decision with the owner; code only in an approved implementation phase. For detailed local material see [architecture worksheet](references/architecture-worksheet.md). When available, prototype-evaluation supplies further evaluation worksheets; its availability is optional.
