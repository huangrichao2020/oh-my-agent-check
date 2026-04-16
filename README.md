# oh-my-agent-check

Brutally strict, JSON-first agent-wrapper audit skill.

This package is for auditing any agent system itself:

- CLI coding agents
- long-running assistant runtimes
- browser agents
- wrapper-based copilots
- memory-heavy assistants
- tool-using autonomous loops

It exists to answer questions like:

- Why does this agent become worse than the base model?
- Which layer first corrupted the answer?
- Where is the hidden prompt conflict?
- Which memory path is polluting new turns?
- Which fallback loop is mutating correct answers into bad ones?
- Which fixes must be code-enforced instead of prompt-enforced?

## What It Produces

Internally, this skill expects the audit to be driven through four structured artifacts:

1. `agent_check_scope.json`
2. `evidence_pack.json`
3. `failure_map.json`
4. `agent_check_report.json`

The final user-facing answer should then be rendered from the report instead of improvised from memory.

## Audit Modes

Standard playbooks included in this package:

- `wrapper-regression`
- `memory-contamination`
- `tool-discipline`
- `rendering-transport`
- `hidden-agent-layers`

See:

- `references/playbooks.md`

## Why This Exists

Many agent systems degrade because they are not one model anymore. They become a stack:

- system prompt
- session history
- long-term memory
- distillation
- active recall
- tool selection
- tool execution
- tool interpretation
- answer shaping
- platform rendering
- hidden fallback agents
- stale persistence

This skill is designed to inspect that full stack without hand-wavy explanations.

## Package Contents

- `SKILL.md`
- `agents/openai.yaml`
- `references/report-schema.json`
- `references/rubric.md`
- `references/playbooks.md`
- `references/example-report.json`

## Example Prompt

Use `$oh-my-agent-check` to audit this agent runtime end-to-end. Focus on wrapper-regression and tool-discipline, inspect yesterday’s logs instead of only current behavior, and give me a severity-ranked diagnosis with code-enforced fixes first.

## Design Principles

This skill is intentionally:

- JSON-first
- evidence-backed
- hostile to hand-wavy explanations
- focused on wrapper architecture, not user-task completion
- biased toward code-control over prompt-control

## Publishing Notes

This repository is prepared as a standalone skill package suitable for publishing to GitHub and packaging for distribution channels that accept Codex-style skill folders.
