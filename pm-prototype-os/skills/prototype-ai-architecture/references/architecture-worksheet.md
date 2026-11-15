# Architecture worksheet

Record: job and decision owner; evidence/claim IDs; current baseline; approved requirements; data/permission boundaries; alternatives; quality and latency measures; all-in cost basis; failure/human recovery; what can falsify each option; unknown APIs/prices; implementation authorization; next evidence.

Use matched cases to isolate retrieval, model, prompt and router changes. If the corpus changes too, name the confound or design additional cells. Require final-state evidence for actions. Never infer live provider capability from an old example or a model's self-description.

Toy accounting: USD9 across six attempts with three verified successes gives USD1.50 per attempted task and USD3 per successful task. USD10 across six attempts with five successes gives approximately USD1.67 and USD2. Include review and retries consistently. Tiny synthetic samples do not establish production superiority. Report the percentile convention and uncertainty of latency comparisons.

Method leads: [Chip Huyen's public companion material](https://github.com/chiphuyen/aie-book), [Anthropic agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), [Hugging Face monitoring](https://huggingface.co/learn/agents-course/en/bonus-unit2/monitoring-and-evaluating-agents-notebook). No vendor service is a required dependency.
