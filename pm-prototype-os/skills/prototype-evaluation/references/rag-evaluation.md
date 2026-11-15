# RAG retrieval, grounding and access evaluation

Freeze the query, authorized identity/tenant, corpus snapshot, as-of policy, retrieval/index settings and answer configuration. Resolve which source governs conflicts. A recent date alone does not establish authority. Check parsing, chunking, indexing and access filtering before attributing failure to generation.

## Retrieval component

Have qualified reviewers judge query-document relevance independently of the generated answer. Define document versus chunk identity and deduplicate before counting.

- precision@k = judged relevant returned items / returned items in the defined top-k evaluation. State how fewer than k results are handled.
- recall@k = relevant items retrieved / known relevant items in the declared eligible corpus. When the relevant inventory is incomplete, full recall is UNKNOWN; report a narrower judged-pool measure only with its limits.
- reciprocal rank = 1 / rank of the first relevant result, or zero if none within the searched range. State cutoff and ties.

Toy example: two relevant documents among five results, first found at rank 2, gives precision@5=2/5 and reciprocal rank=1/2. It does not establish recall without the known relevant set. Retrieval metrics do not establish answer correctness.

## Answer component

Split material answer claims and inspect support against authorized, current evidence. Separate citation existence, whether the cited passage supports the claim, completeness of required coverage, contradiction handling and task usefulness. Record unsupported claims even if other claims are correct. Abstention behavior needs answerable and unanswerable cases: rejecting everything cannot count as successful completion.

## Failure matrix

Include stale and contradictory documents, irrelevant/empty retrieval, partially answerable queries, inaccessible documents, tenant boundaries, prompt-injection text, parsing/index failures and unavailable dependencies. Keep retrieved instructions as data; enforce permissions outside model persuasion. Inspect source IDs and final outputs without exposing protected content in a public report.

Compare retriever/reranker/chunking changes on matched queries and snapshots, then inspect answer behavior. If corpus and model changed together, report a confounded comparison or add controlled cells. Preserve critical access failures separately from average answer scores. Freeze expected policy and test whether both retrieval and generation respect it.

Source leads: [Chip Huyen's public chapter summaries](https://github.com/chiphuyen/aie-book/blob/main/chapter-summaries.md), [Inspect datasets and scorers](https://inspect.aisi.org.uk/scoring.html), and [Anthropic agent evaluation](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). This worksheet defines its own transparent measurements rather than importing vendor scores.
