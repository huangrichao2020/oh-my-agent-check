# Audit Rubric

Use this rubric when producing `agent_check_report.json`.

## 1. Context Cleanliness

Check:

- Is the same information injected through multiple layers?
- Are model-generated summaries fed back as context?
- Is session history carrying stale facts forward?
- Are current-session artifacts re-entering the same turn?

Red flags:

- Prompt contains history + memory + distilled notes + recall notes that all restate the same thing
- Long answers become future pseudo-facts

## 2. Tool Discipline

Check:

- Are tools merely available, or actually required in code?
- Can the model skip tools and still answer?
- Does the system distinguish between "publicly readable" and "credential-backed" evidence?

Red flags:

- "Must use tool" exists only in prose instructions
- One failed probe becomes a strong conclusion

## 3. Failure Handling

Check:

- Does a send/render failure trigger another hidden agent?
- Is there a deterministic fallback path?
- Are failures visible and attributable?

Red flags:

- Platform layer uses another LLM to "repair" the answer
- Retry behavior mutates semantics

## 4. Memory Admission

Check:

- Can assistant self-talk become long-term memory?
- Are user corrections weighted more than assistant assertions?
- Is there a stable-window or evidence gate before distillation?

Red flags:

- Durable facts come from assistant-only text
- Distillation runs on every small session update

## 5. Answer Shaping

Check:

- Is the final response derived from structured evidence?
- Does formatting add noise or rewrap already-correct answers?
- Does platform rendering leak raw markdown or transform content unpredictably?

Red flags:

- Final answer gets wrapped multiple times
- Headings or labels duplicate
- Platform card renderer mutates meaning

## 6. Hidden Agent Layers

Check:

- Are there hidden repair, retry, summarize, or recap agents?
- Do these layers have explicit contracts and JSON schemas?

Red flags:

- A transport layer behaves like another assistant
- Recovery behavior is prompt-driven instead of code-driven

## 7. JSON vs Freeform Boundary

Preferred:

- Internal planning and state should be structured
- Final rendering may be prose

Red flags:

- Internal protocol is plain markdown
- Intermediate state is captured as narrative instead of typed data

## Severity Heuristics

### critical

- Can produce confident, operationally wrong behavior
- Wrong actions or wrong system state with high confidence

### high

- Frequently corrupts good evidence before final answer
- Memory or prompt layers repeatedly steer answers off target

### medium

- Correctness often survives, but output is noisy, fragile, or hard to trust

### low

- Mostly cosmetic or maintainability issues, not direct correctness risks
