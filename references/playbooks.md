# Playbooks

Use one of these as the primary audit mode.

## wrapper-regression

Use when:

- the base model seems strong, but the wrapped agent behaves much worse
- users say "this model is fine elsewhere, but your agent is stupid"
- the problem likely comes from context layering, wrappers, or orchestration

Focus:

- system prompt vs runtime role conflicts
- duplicated context injection
- model-generated text re-entering the loop
- hidden formatting or fallback layers

## memory-contamination

Use when:

- the agent drags old topics into new questions
- the same session seems to teach itself bad facts
- long-term memory and session history blur together

Focus:

- same-session artifact reentry
- stale session reuse
- weak memory admission criteria
- aggressive distillation cadence
- retrieval quality and ordering

## tool-discipline

Use when:

- the agent should have used a tool but did not
- the wrong tool was selected
- tool evidence was available but the conclusion drifted anyway

Focus:

- code-enforced vs prompt-enforced tool requirements
- preflight probes
- tool-call skip paths
- stale evidence reuse
- final answer bound to current-turn evidence or not

## rendering-transport

Use when:

- the answer is correct internally but broken in delivery
- raw markdown leaks into cards
- rich text, post, or platform payloads mutate meaning
- post/image payload parsing is flaky

Focus:

- transport payload shape assumptions
- rendering compatibility gaps
- deterministic fallback behavior
- platform-layer mutations

## hidden-agent-layers

Use when:

- there are repair, retry, summarize, or recap loops hidden in the stack
- unexpected second-pass LLM calls mutate outputs
- transport or maintenance layers behave like extra agents

Focus:

- hidden repair agents
- recap/recall loops
- maintenance-worker synthesis paths
- platform repair prompts

## Suggested Priority

If you are unsure which to start with:

1. `tool-discipline`
2. `memory-contamination`
3. `wrapper-regression`
4. `rendering-transport`
5. `hidden-agent-layers`
