---
description: "Evaluate an approved prototype or AI application using evidence-linked cases, graders, matched comparisons and explicit runtime limits"
argument-hint: "[prototype, AI system, traces or evaluation question]"
---
# /evaluate-prototype

Evaluate **$ARGUMENTS** within the current approved phase. For a new task apply the canonical 5–10-question gate and wait; an approval reply for an already scoped phase continues that phase. Keep zero incremental spending and the user's action boundaries.

Use `prototype-evaluation`. When the task requires them, use the same plugin's `eval-error-discovery`, `eval-annotation-guidance` and `llm-judge-calibration`. No other plugin is required. Define current authority, rubric, dataset/splits, versions, permitted tools and owner-defined gates. Compare matched tasks; report RAG retrieval and generation, agent final-state correctness, cost, latency, slices and uncertainty as relevant. Preserve claim IDs, evidence restrictions and missing data.

Deliver PASS/FAIL/BLOCKED/NOT_RUN results with evidence, environment, actual execution status, critical failures and next approval scope. Do not convert synthetic cases, a static scan or a convincing judge rationale into runtime or production proof.
