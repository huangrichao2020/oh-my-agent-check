---
name: oh-my-agent-check
description: Use when auditing any agent wrapper, CLI agent, coding assistant, browser agent, or long-running AI runtime for hidden prompt conflicts, memory pollution, tool misuse, rendering bugs, fallback path drift, and architecture-level self-sabotage. Produces a JSON-first, evidence-backed, brutally strict agent diagnosis with severity-ranked findings, root-cause mapping, and prioritized fixes.
---

# Oh My Agent Check

Use this skill to audit an agent system itself, not to complete the user's domain task.

This skill is for cases like:

- "Why does this agent become worse after wrapping a model?"
- "Why is the tool use flaky?"
- "Why does the agent hallucinate system state?"
- "Why does memory pollution happen?"
- "Why is the output formatting broken?"
- "Why does the platform layer mutate good answers into bad ones?"
- "Audit this CLI agent / runtime / assistant architecture end-to-end"

If the user sounds frustrated, suspicious, or says the base model behaves better elsewhere, this skill is almost always the right tool.

## Core Rule

Do not trust the current output quality, current prompt text, or current "fixed" behavior by default.

This skill assumes:

- the target agent may already be lying about its own capabilities
- current behavior may hide historical regressions
- the "smart" layer may actually be a stack of self-sabotaging wrappers
- explanations without evidence are noise

The target of the audit is the full stack:

1. System prompt / persona
2. Session history injection
3. Long-term memory retrieval
4. Distillation pipeline
5. Active recall / recap layers
6. Tool routing / selection
7. Tool execution and observation handling
8. Tool-output interpretation
9. Final answer shaping
10. Platform rendering / transport
11. Hidden fallback or repair loops
12. Persistence / stale state / cached artifacts

## Required Working Style

Work JSON-first internally.

Before writing prose conclusions, build these internal artifacts in order:

1. `agent_check_scope.json`
2. `evidence_pack.json`
3. `failure_map.json`
4. `agent_check_report.json`

Do not skip directly to recommendations.

Be brutal about causality:

- do not say "the model is weak" unless the wrapper layers have been falsified
- do not say "memory is bad" unless you can show the contamination path
- do not say "tool use is flaky" unless you can show the exact skip or drift path
- do not let a clean current state erase a dirty historical incident

## Artifact Contracts

Read these references before auditing:

- `references/report-schema.json`
- `references/rubric.md`
- `references/playbooks.md`
- `references/advanced-playbooks.md`
- `references/code-patterns.md`
- `references/example-report.json`
- `references/trigger-prompts.md`
- `references/framework-directions.md`
- `references/governance-framework.md`
- `references/clawhub-publish.md`

### `agent_check_scope.json`

Define:

- target system
- runtime entrypoints
- channels/platforms
- model/provider
- known symptoms
- suspected layers
- time window of interest

### `evidence_pack.json`

Capture:

- exact files inspected
- relevant code locations
- exact logs or DB rows
- config paths
- platform payload shapes
- whether evidence is current-state or historical-state

Every claim must map to concrete evidence.

### `failure_map.json`

For each failure mode include:

- symptom
- user-visible effect
- internal mechanism
- source layer
- root cause
- confidence
- contradictory evidence if any

### `agent_check_report.json`

Final structured report must include:

- executive verdict
- severity-ranked findings
- coupling / conflict map across layers
- contamination paths
- hidden-agent behaviors
- prompt-overuse indicators
- code-vs-prompt control gaps
- recommended fix order

## Audit Workflow

### Phase 1: Scope

Create `agent_check_scope.json` first.

Minimum fields:

- `target_name`
- `entrypoints`
- `channels`
- `model_stack`
- `symptoms`
- `time_window`
- `layers_to_audit`

### Phase 2: Evidence

Use direct evidence only:

- source code
- logs
- database rows
- transport payloads
- test output
- screenshots

Prefer:

- `rg`
- file reads
- exact line references
- historical session traces when the current version may already be partially fixed

If the user mentions "it was worse yesterday", inspect yesterday's sessions/logs instead of overfitting to current code.

### Phase 3: Failure Mapping

Look specifically for these anti-patterns:

- same information injected multiple times through different layers
- model-generated text fed back into model as pseudo-truth
- tools being exposed without being required
- current-session distilled artifacts re-entering the same session
- stale session state being reused as live evidence
- platform formatting destroying valid answers
- hidden recovery agents or repair prompts mutating outputs
- "must use tool" expressed only in prompt, not in code
- freeform markdown being used as an internal protocol
- transport-layer code acting like another agent

Also look for the "fake depth" pattern:

- the wrapper adds more steps, but fewer reliable controls
- the model sounds more sophisticated while becoming less grounded
- the stack appears more agentic, but evidence quality gets worse

### Phase 4: Fix Strategy

Prefer code control over prompt control.

Recommended fix order by default:

1. Hard-gate tool requirements in code
2. Remove or narrow hidden fallback/repair agents
3. Reduce context duplication across prompt/history/memory/distillation/recall
4. Tighten memory admission criteria
5. Tighten distillation trigger policy
6. Reduce rendering-layer mutation
7. Convert internal flow to typed JSON envelopes

## Severity Model

Use these severity labels:

- `critical`
- `high`
- `medium`
- `low`

`critical` means the agent can confidently produce wrong operational behavior.

`high` means the agent frequently degrades correctness or stability.

## Output Rules

The final user-facing response should present:

1. Severity-ranked findings first
2. Then the architecture diagnosis
3. Then the ordered fix plan

Do not lead with compliments or summaries.

If the user explicitly asks for the structured JSON, provide the JSON report.

If the user asks for a readable summary, render from `agent_check_report.json` instead of improvising a new theory.

Do not soften the verdict for politeness.

If the system is broken, say it is broken.

If the main problem is wrapper design, say so directly.

## Standard Audit Modes

Use the closest playbook from `references/playbooks.md`:

Core playbooks:

- `wrapper-regression`
- `memory-contamination`
- `tool-discipline`
- `rendering-transport`
- `hidden-agent-layers`

Production-discovered playbooks (from Langflow, GenericAgent, OpenCode, superpowers integrations):

- `code-execution-safety`
- `memory-growth-hazard`
- `observability-gap`
- `state-mutator-safety`

If multiple apply, combine them, but still keep one primary playbook name in `agent_check_scope.json`.

For fast starts, pull an exact prompt from `references/trigger-prompts.md`.

For code-level evidence, search patterns in `references/code-patterns.md`.

If the target system is deeply broken, escalate into the harsher modes from:

- `references/advanced-playbooks.md`

New advanced modes:

- `runaway-agent-loop`
- `prompt-injection-surface`
- `multi-agent-orchestration-failure`

## Framework Expansion

This skill package also includes `references/framework-directions.md`.

Use it when the user wants to evolve this audit skill into a broader methodology, framework, workshop, internal standard, or productized review system.

Important:

- treat those directions as design prompts, not as already-built capabilities
- guide the user to explore and implement them deliberately
- do not overclaim that the framework already exists in code unless it truly does

If the user wants to turn audits into an internal standard or governance system, continue with:

- `references/governance-framework.md`

If the user wants to package or distribute this skill, continue with:

- `references/clawhub-publish.md`

## What Good Looks Like

A good audit from this skill should be able to answer:

- Which layer first corrupted the answer?
- Which layer amplified the corruption?
- Which layer failed to stop it?
- Which fixes must be code-enforced?
- Which prompts should be deleted entirely?
- Which state should never be persisted?
- Which layer is pretending to help while actually making the system worse?
- Which "agentic" behaviors are fake sophistication?

## Minimal Publishing Shape

This skill package is intended to be portable.

Keep the package self-contained:

- `SKILL.md`
- `agents/openai.yaml`
- `references/report-schema.json`
- `references/rubric.md`
- `references/playbooks.md`
- `references/advanced-playbooks.md`
- `references/code-patterns.md`
- `references/example-report.json`
- `references/trigger-prompts.md`
- `references/framework-directions.md`
- `references/governance-framework.md`
- `references/clawhub-publish.md`

Do not depend on repo-specific assumptions unless the user asks for a repo-specific extension.
