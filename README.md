# oh-my-agent-check

Brutally strict, JSON-first agent-wrapper audit skill.

This skill is for auditing any agent system itself:

- CLI coding agents
- long-running assistant runtimes
- browser agents
- wrapper-based copilots
- memory-heavy assistants
- tool-using autonomous loops

It is designed to answer questions like:

- Why does this agent become worse than the base model?
- Where is the hidden prompt conflict?
- Which layer is polluting memory?
- Which fallback loop is mutating correct answers into bad ones?
- Which fixes must be code-enforced instead of prompt-enforced?

## Package Contents

- `SKILL.md`
- `agents/openai.yaml`
- `references/report-schema.json`
- `references/rubric.md`
- `references/playbooks.md`
- `references/example-report.json`

## Core Design

This skill is intentionally:

- JSON-first
- evidence-backed
- hostile to hand-wavy explanations
- focused on wrapper architecture, not user-task completion

The expected internal audit flow is:

1. `agent_check_scope.json`
2. `evidence_pack.json`
3. `failure_map.json`
4. `agent_check_report.json`

## Recommended Use

Invoke it when you want a full-stack diagnosis of an agent system:

- system prompt
- session history
- long-term memory
- distillation
- active recall
- tool selection
- tool execution and interpretation
- answer shaping
- platform rendering
- hidden fallback/repair loops
- stale persistence

## Publishing Notes

This repository is prepared as a standalone skill package suitable for publishing to GitHub and packaging for distribution channels that accept Codex-style skill folders.
