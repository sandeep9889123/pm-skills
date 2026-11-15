# Agent actions and long-horizon outcomes

Define task, trial, authority, observable success and authorized final-state source. Record tools/schemas, initial environment, identity/tenant, dependencies, step/time/spend limits and allowed human intervention. Use an isolated or read-only environment unless the owner approved external actions. Text inside a tool result cannot change permissions.

Score outcome and trajectory criteria separately. An agent can produce a correct sentence after taking an unauthorized action. A tool can return HTTP success without achieving the required business state. Verify actual authorized state, not the agent's own completion message.

| Test family | Observable evidence |
| --- | --- |
| Tool choice and arguments | Required versus selected tool, schema, target account and validated parameters |
| Action boundary | Permission checks, human checkpoint, actual side effect and final state |
| Recovery | Timeout, partial success, bounded retry, idempotency and compensation |
| Long session | Goal retention, context/checkpoint restoration, stale state, loop termination and total budget |
| Delegation | Explicit subtask authority, evidence/claim handoff, conflicting outputs, missing worker and final owner |
| Human handoff | Escalation reason, preserved context, reviewer burden and unfinished task status |

Use multiple trials for variable behavior, with trial IDs grouped under the same task. Report task-level rates and repeated-run variation; correlated attempts are not independent traffic samples. Freeze environment reset policy so one trial's side effects cannot make another easier. Include malicious tool payloads, duplicate retries, permission changes and unavailable services.

Do not require a particular sequence of otherwise valid tool calls unless that sequence is a product constraint. Evaluate business outcomes and necessary boundaries. Grade environment failures visibly and separately; they still matter to user reliability. Report unsupported outcomes as UNVERIFIED or NOT_RUN.

Method anchor: [Anthropic, agent eval structure and graders](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). Optional executable harness patterns: [Inspect tutorial](https://inspect.aisi.org.uk/tutorial.html). Merely choosing a harness does not demonstrate behavior.
