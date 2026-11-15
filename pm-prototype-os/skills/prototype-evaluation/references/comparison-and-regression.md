# Controlled comparisons and regression

Declare the product question, expected mechanism, metrics, critical gates, minimum useful difference, uncertainty plan and stopping rule before examining outcomes. Baseline can be the current model, keyword search, rules or human-assisted workflow. Public model rankings are screening signals, not product results.

Freeze case/group IDs, policy/corpus, tools and permissions, prompt hashes, model IDs/settings, retriever/index/reranker, judge/rubric, environment and trial budgets. Preserve raw first responses, tool errors and final-state evidence. Compare matched tasks. Change one factor when isolating its effect; if several changed, use a declared factorial/ablation plan or report confounding. A newly chosen evaluator can change the score without changing the product.

Keep development and held-out test separate. Reusing final results for prompt or threshold selection creates development information. Add a new untouched assessment after changes. Evaluate both capability and regression cases; an average improvement may hide a critical slice or permission regression.

Report trial and task denominators, all planned slots, missing/failed runs, paired changes, class/slice results, uncertainty, observed cost and end-to-end latency. Resample or model the independent task/group rather than correlated trials when estimating uncertainty. A single toy run is exploratory, not evidence of a low production failure rate. Avoid invented confidence intervals when raw data or assumptions are missing.

For model comparisons, disclose unequal tools, quotas, context budgets and source snapshots. For before/after skills, freeze prompts and expose only the procedure under test. Keep expected answers and grader hints out of execution context. Blind evaluators to version/model labels where practical; disclose residual author involvement and evaluator limits.

Regression artifacts: immutable inputs and source snapshots, expected observable behavior, grader version, run record/hash, critical failures and missing evidence. Keep app regression separate from the repository's own PM-skill benchmark. See [OpenAI evaluation workflow](https://developers.openai.com/api/docs/guides/evaluation-best-practices) and [Inspect scoring policy](https://inspect.aisi.org.uk/scoring.html) for implementation leads.
