# Method provenance and maintenance

Reviewed 2026-11-15. This is source-informed original procedure design. Author reputation, a published example or a source link does not validate this skill. No third-party code, full transcripts or paid course content is copied. External SDKs, services and datasets are optional.

| Primary source | Inspected material and use | Limit |
| --- | --- | --- |
| [Husain and Shankar, evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | Public text on discovery, human labels and evaluator alignment | Practitioner methodology; sample counts are not universal requirements |
| [Shankar et al., EvalGen](https://arxiv.org/abs/2404.12272) | Abstract on human validation and evolving criteria | Abstract inspected; no claim to reproduce the study |
| [Anthropic agent evals](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Task/trial/outcome distinctions and grading approaches | Product-specific adaptation required |
| [OpenAI evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Application-specific evaluation workflow and case coverage | Example thresholds and platform APIs are not imported as defaults |
| [Chip Huyen, public chapter summaries](https://github.com/chiphuyen/aie-book/blob/main/chapter-summaries.md) | Evaluation, retrieval, inference and feedback scope | Public companion summaries, not full-book extraction |
| [Inspect tutorial](https://inspect.aisi.org.uk/tutorial.html) and [datasets](https://inspect.aisi.org.uk/datasets.html) | Dataset/solver/scorer and log patterns | External examples not executed here |
| [Hugging Face agent monitoring notebook](https://huggingface.co/learn/agents-course/en/bonus-unit2/monitoring-and-evaluating-agents-notebook) | Tracing, cost, latency and feedback examples | Notebook inspected, not executed; installs and services remain optional |
| [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/) | Trace/span hierarchy and correlation concepts | Provider-specific setup must be verified separately |
| [Microsoft Research human-AI interaction](https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/overview/) | Interaction, errors and adaptation framing | Research guidance does not replace product user evidence |
| [NIST proportion intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) | Proportion-interval assumptions for optional local arithmetic | Independence and representative data still matter |
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | Public course index for UX/operations context | 2023 material; no claim to watch all recordings or execute demos |
| [Karpathy's course entry points](https://karpathy.ai/llm-course/) | Technical learning lead for the mentor skill | No full video/transcript extraction and no eval procedure attributed solely to reputation |
| [Aman Khan, PM eval framing](https://amankhan1.substack.com/p/beyond-vibe-checks-a-pms-complete) | Public product/component evaluation framing | Practitioner perspective and affiliations, not independent validation |

Community discussions can propose failure hypotheses, but require reproduction or authoritative evidence before becoming factual claims or remedies. No Reddit remedy is treated as proven here.

## Refresh protocol

Keep source URL, exact section, inspection date, available revision, capability claim, scope and execution status. At a model/tool/rubric/corpus change, investigate affected assumptions and tests. At a source change, preserve the old citation/version and review the diff; do not silently rewrite past evidence. If retrieval fails, mark STALE or UNKNOWN and retain the gap. Avoid asserting that a live link proves unchanged content.

Update skill version, regression cases and known limitations when behavior changes; run structural checks and a fresh task comparison. Maintain policy/price sources separately from conceptual references. Keep a source-and-workflow revalidation queue with owner and trigger; do not create scheduled automation without a user request.
