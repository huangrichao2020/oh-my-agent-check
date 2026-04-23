# Quick Start — For Any Agent

If you (an AI agent) have just received this repository, follow these steps in order.

## Step 0: Understand What This Is

This is **not** a project to build features into. It is an **audit skill package** — a diagnostic instrument for inspecting other agent systems.

You use this skill to **audit another agent**, not to complete the user's domain task.

## Step 1: Read These Files in Order

Read these files to understand the skill contract before doing any work:

1. `SKILL.md` — The core skill definition. This is your primary instruction set.
2. `references/rubric.md` — The 7 evaluation dimensions.
3. `references/playbooks.md` — Standard audit modes (start here for common failures).
4. `references/example-report.json` — What a valid report looks like.
5. `references/report-schema.json` — The JSON schema every report must follow.

Do **not** read all 10 reference files before starting. Read the above 5, then pull others as needed during the audit.

## Step 2: When to Activate This Skill

Use this skill when the user says things like:

- "My agent is behaving weirdly"
- "The model is good but the wrapper makes it worse"
- "Tool use is flaky"
- "Memory keeps polluting"
- "Output keeps breaking"
- "Audit this agent architecture"

If the user sounds **frustrated** or **suspicious** of their agent system, this skill is almost certainly the right tool.

Do **not** use this skill for normal task completion (e.g., "write me a script", "fix this bug"). This is for **system-level diagnosis only**.

## Step 3: How to Run an Audit

### 3.1 Start with Scope

Before looking at any code, create `agent_check_scope.json` with:

```json
{
  "target_name": "<name of the agent being audited>",
  "entrypoints": ["<how users interact with it>"],
  "channels": ["<platforms/channels it runs on>"],
  "model_stack": ["<LLM models involved>"],
  "symptoms": ["<what the user reports is broken>"],
  "time_window": "<when did it start breaking>",
  "layers_to_audit": ["<which of the 12 layers to inspect>"]
}
```

If you do not know the answers, **ask the user** or inspect the codebase to infer them.

### 3.2 Gather Evidence

Use these tools to collect evidence:

- **`rg` (ripgrep)** — search codebase for patterns (tool routing, memory admission, hidden loops)
- **`file_read`** — read specific files at specific lines
- **`ls` / `find`** — locate config files, session logs, memory directories
- **`cat` log files** — inspect historical session traces

Evidence rules:
- Every claim must map to a **concrete file/line/log row**
- Prefer **historical evidence** over current code (current code may already be partially fixed)
- If the user says "it was worse yesterday", inspect **yesterday's logs/sessions**

### 3.3 Build the Failure Map

Create `failure_map.json` for each failure mode:

```json
{
  "symptom": "what the user sees",
  "user_impact": "what it costs the user",
  "mechanism": "how the wrapper causes it",
  "source_layer": "which of the 12 layers",
  "root_cause": "the deepest cause you can find",
  "confidence": 0.0,
  "evidence": ["file:line", "log:row"]
}
```

### 3.4 Produce the Report

Build `agent_check_report.json` following the schema in `references/report-schema.json`.

The report must include:
- `executive_verdict` — overall health + primary failure mode
- `findings[]` — severity-ranked list (critical → high → medium → low)
- `conflict_map[]` — inter-layer conflicts
- `ordered_fix_plan[]` — prioritized fix order

### 3.5 Render the Answer

Present findings to the user in this order:

1. **Severity-ranked findings** (most critical first)
2. **Architecture diagnosis** (which layer corrupted what, and why)
3. **Ordered fix plan** (code-first, not prompt-first)

Do **not** start with compliments or summaries. If the system is broken, say so directly.

## Step 4: Pick the Right Playbook

Match the user's symptom to a playbook:

| User says... | Use playbook |
|---|---|
| "Base model is fine but agent is worse" | `wrapper-regression` |
| "Old topics keep showing up in new conversations" | `memory-contamination` |
| "It should use tools but doesn't" | `tool-discipline` |
| "Internal answer is correct but output is broken" | `rendering-transport` |
| "There seem to be hidden repair/retry loops" | `hidden-agent-layers` |
| "Sounds confident but evidence is weak" | `false-confidence` (advanced) |
| "Keeps repeating old outputs as if they're fresh" | `stale-evidence-replay` (advanced) |

See `references/playbooks.md` and `references/advanced-playbooks.md` for details.

## Step 5: Validate Your Report

Before delivering the report, validate it:

```bash
python3 scripts/validate_schema.py
```

This checks that your `references/example-report.json` (or any report you produce following the schema) is structurally valid.

## Anti-Patterns to Avoid

- ❌ Saying "the model is weak" without first falsifying the wrapper
- ❌ Saying "memory is bad" without showing the contamination path
- ❌ Letting a clean current state erase a dirty historical incident
- ❌ Treating markdown prose as a trustworthy internal protocol
- ❌ Accepting "must use tool" in prompt text when code never enforces it
- ❌ Leading with compliments or softening the verdict for politeness

## Severity Labels

Use exactly these four labels:

| Label | When to use |
|---|---|
| `critical` | Agent can confidently produce wrong operational behavior |
| `high` | Agent frequently degrades correctness or stability |
| `medium` | Correctness usually survives, but output is fragile or noisy |
| `low` | Mostly cosmetic or maintainability issues |

## Time Estimate

- **Quick audit** (wrapper-regression, 1-2 symptoms): 5-10 minutes
- **Full audit** (all 12 layers, multiple symptoms): 15-30 minutes
- **Deep audit** (advanced playbooks, historical evidence): 30-60 minutes

## After the Audit

If the user wants to:
- **Evolve this skill** → read `references/framework-directions.md`
- **Turn audits into an internal standard** → read `references/governance-framework.md`
- **Package/distribute this skill** → read `references/clawhub-publish.md`
