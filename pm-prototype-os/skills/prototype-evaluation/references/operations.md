# Tracing, production review, drift and incidents

## Instrumentation contract

Use task/run/trace IDs and parent/child span IDs for model, retrieval, tool, routing, review and final verification events. Record start/end time, status/error, attempt number, safe user/tenant identifiers, prompt/model/rubric/corpus versions, policy context, usage/price version, decision/action authorization and final-state evidence locator. Minimize payloads; redact secrets and sensitive content and define access/retention. Observability must not become a new data leak.

Before relying on telemetry, perform an authorized test trace and check propagation across services, asynchronous links, retry grouping, missing spans, clock assumptions and final outcome linkage. Do not assert instrumentation worked because a logging library was configured. Source pattern: [OpenTelemetry traces](https://opentelemetry.io/docs/concepts/signals/traces/) and [Hugging Face monitoring notebook](https://huggingface.co/learn/agents-course/en/bonus-unit2/monitoring-and-evaluating-agents-notebook); SDK-specific commands require a current compatibility check and authorization.

## Quality monitoring and drift

Combine a representative traffic sample with separately reported risk-targeted cases and user feedback. Define reviewer role, sampling inclusion, adjudication, service owner, intervals and alert basis. Track task success, false acceptance/rejection, abstention, critical actions, cost/latency, human overrides, queue burden and missing telemetry by slice. Unknown values remain UNKNOWN.

Compare source/input mix, language/task/customer slices, failure categories, label standards, versions and missingness against a declared baseline. Investigate whether a shift comes from data, model/prompt, corpus, tools or telemetry. A changed score alone does not identify the cause. Revalidate affected graders and refresh cases without overwriting the frozen regression suite. Set alert limits from owner-approved risk, history or SLOs; never invent red/green thresholds.

## Feedback to regression

Link feedback to an authorized trace and verified behavior. Deduplicate exports/incidents, inspect evidence, classify effect versus hypothesis and adjudicate the expected behavior. Redact and preserve source snapshots, add an oracle and failure family, then test the narrow fix and adjacent cases. Keep complaint frequency distinct from population prevalence and unsupported feedback distinct from confirmed defects.

## Incident worksheet

Record observed impact and affected scope; contain only within approved authority; preserve permitted evidence and versions; reconstruct the timeline and action/final-state mismatch; test competing causes; record unknowns and owners; propose a bounded fix with compensation, regression checks and recovery evidence. Do not close an incident from a better answer alone. Verify the intended state and remaining exposure. Escalation or rollback outside current authority needs the owner's action.
