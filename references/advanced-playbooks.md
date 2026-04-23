# Advanced Playbooks

Use these when the target system is not merely flaky, but structurally rotten.

## false-confidence

Use when:

- the agent sounds decisive while evidence is weak or missing
- the wrapper adds confidence without adding truth

Focus:

- confidence without evidence
- definitive language after failed probes
- "clean" prose masking bad epistemics

## stale-evidence-replay

Use when:

- old outputs are repeated as if they were current
- the agent reuses a prior PID, IP, or status after the system changed

Focus:

- current-turn evidence binding
- stale session carryover
- historical artifact residue

## fake-agentic-depth

Use when:

- the system looks more agentic but gets less reliable
- extra planning, recap, or orchestration layers degrade truthfulness

Focus:

- multiple smart-sounding layers with no control benefit
- complexity without enforcement
- "agent theater" vs genuine capability

## hidden-repair-brain

Use when:

- platform or fallback code silently spins up a second LLM pass
- good answers become worse during repair or downgrade

Focus:

- hidden repair loops
- transport-layer intelligence
- semantic mutation during fallback

## memory-poisoning

Use when:

- assistant self-talk becomes durable knowledge
- same-session facts teach the agent the wrong thing

Focus:

- admission criteria
- distillation cadence
- persistence hygiene

## protocol-decay

Use when:

- internal state is carried as prose instead of typed data
- markdown becomes the protocol
- intermediate layers keep paraphrasing each other

Focus:

- JSON vs narrative boundary
- envelope integrity
- loss of structure across layers

## runaway-agent-loop

Use when:

- agents call agents call agents, without iteration guards
- circular dependencies between agent components
- cost spikes with no visible output

Focus:

- max-iteration enforcement at every agent boundary
- cycle detection in agent dependency graphs
- cost guardrails and circuit breakers

## prompt-injection-surface

Use when:

- user input reaches agent prompts without sanitization
- the agent processes untrusted text as instructions
- tool outputs can influence system behavior

Focus:

- input/output sanitization boundaries
- instruction vs data separation
- tool output trust model

## multi-agent-orchestration-failure

Use when:

- multiple agents coordinate but produce worse results than a single agent
- supervisor/worker patterns fail to converge
- agents contradict each other or duplicate work

Focus:

- supervisor authority and conflict resolution
- worker isolation and responsibility boundaries
- shared state consistency
