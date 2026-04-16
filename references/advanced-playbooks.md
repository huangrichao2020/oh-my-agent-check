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
