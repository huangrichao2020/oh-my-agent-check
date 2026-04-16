# Trigger Prompts

These are ready-to-paste prompts for using `$oh-my-agent-check`.

## 1. Wrapper Regression

Use `$oh-my-agent-check` to audit this agent end-to-end. The base model behaves much better outside this wrapper. I want a brutally honest diagnosis of where the wrapper is making it worse. Focus on wrapper-regression and tool-discipline. Inspect historical incidents, not just current code.

## 2. Memory Contamination

Use `$oh-my-agent-check` to audit this agent for memory pollution. Find how old topics leak into new turns, how same-session artifacts reenter the loop, and what should never be persisted. I want the contamination path, severity-ranked findings, and code-enforced fixes.

## 3. Tool Discipline

Use `$oh-my-agent-check` to audit this agent’s tool discipline. Show me exactly where the model can skip tools, where stale evidence is reused, and where conclusions drift away from real stdout/stderr. Prioritize code fixes over prompt advice.

## 4. Rendering / Transport

Use `$oh-my-agent-check` to audit this agent’s rendering and transport layers. The internal answer may be correct, but delivery is mutating it. Focus on rendering-transport and hidden-agent-layers. I want proof, not guesses.

## 5. Hidden Agents

Use `$oh-my-agent-check` to find hidden repair, retry, recap, or formatting agents inside this system. Show which layers act like another assistant without explicit contracts and how they silently mutate outputs.

## 6. No Mercy Full Audit

Use `$oh-my-agent-check` and assume this agent is lying about its own health. Audit every layer: prompt, history, memory, distillation, active recall, tool routing, tool execution, answer shaping, rendering, fallback loops, persistence. Give me the harshest evidence-backed diagnosis you can justify.
