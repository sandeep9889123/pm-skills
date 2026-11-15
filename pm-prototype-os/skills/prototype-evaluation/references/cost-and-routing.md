# AI economics, routing and fallback

## Accounting

Define currency, measurement window, price/as-of version, billing unit and what cost components are observed versus estimated. Include model input/output and cached-token prices when actually supplied, retrieval/embedding/reranking, external tools, retries, failed tasks, human review, infrastructure and allocated operating costs. Separate marginal execution cost from fully loaded business economics and incremental spending permission. Do not invent current prices or assume a free tier covers a workload.

Total observed task cost = supplied nonoverlapping component costs across all attempts and review. Cost per attempted task = total / attempted tasks. Cost per verified successful task = total / verified successes. If no task succeeds, the latter is undefined, not zero. Disclose missing components; do not silently fill them with zero. Keep currencies separate without a verified exchange basis. Avoid double-counting an invoice total and its spans.

Measure end-to-end wall-clock latency from task start to final result, including queues, retries and handoffs where in scope. Sum overlapping spans only for a deliberately defined work measure, not elapsed latency. Report sample size and percentile convention; small samples provide descriptive tails, not an SLO assurance.

Toy ledger: A costs USD9 across six tasks with three verified successes; B costs USD10 across six with five successes. Attempt costs are USD1.50 and approximately USD1.67; successful-task costs are USD3 and USD2. This does not establish production superiority or a rollout decision.

## Routing experiment

Specify the routing signal available before acting, eligible models, tenant/data constraints, budgets, quality gates and fallback triggers. Freeze versions and compare to a fixed-model and existing search/rules baseline. Include router errors and total pipeline cost, not only selected-model price. Test prompt sensitivity and shifts in task difficulty.

Key cache entries by permitted tenant/identity, source version, prompt/model and task-relevant state. Test invalidation and stale/permission changes. Define bounded retries, timeout, fallback to safe search/abstention/human handoff and compensation for partial actions. Never retry or escalate into an action the owner did not authorize. A cheaper model or automatic fallback is a hypothesis until matched-task evidence supports it.

For a local supplied-record calculator, use repository `evaluation/ai_pm/task_metrics.py` when available. Source context: [Chip Huyen, inference and feedback chapter summaries](https://github.com/chiphuyen/aie-book/blob/main/chapter-summaries.md) and [Hugging Face agent monitoring](https://huggingface.co/learn/agents-course/en/bonus-unit2/monitoring-and-evaluating-agents-notebook). The accounting formulas here are explicitly defined rather than attributed as measured vendor performance.
