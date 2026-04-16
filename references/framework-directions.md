# Framework Directions

This file is intentionally **forward-looking**.

It is not a claim that these capabilities already exist.  
It is a structured map of where an audit skill like `oh-my-agent-check` can evolve next.

Use this file when the user wants to:

- extend the skill into a broader methodology
- build an internal agent review standard
- turn repeated audits into reusable programs
- design a training or evaluation loop around agent quality

## 1. Turn Single Audits Into Programs

Idea:

- move from "one audit report" to "repeatable audit program"

Possible implementation directions:

- weekly wrapper-regression reviews
- release-gate checklists before deployment
- postmortem templates after agent incidents
- recurring "memory hygiene" audits

What to explore:

- Which audits should run on every release?
- Which only run after incidents?
- Which should be lightweight vs deep-dive?

## 2. Layer-by-Layer Scorecards

Idea:

- give each agent layer its own explicit scorecard

Candidate scorecard dimensions:

- prompt discipline
- memory cleanliness
- tool discipline
- fallback transparency
- rendering stability
- evidence integrity
- persistence hygiene

What to explore:

- Should scores be numeric, categorical, or narrative?
- Which thresholds are blocker-level?
- Which scores should map directly to shipping decisions?

## 3. Incident Taxonomy

Idea:

- classify failures into recurring patterns so teams stop reinventing diagnoses

Candidate categories:

- stale evidence reuse
- hidden layer mutation
- prompt conflict
- duplicate context injection
- same-session contamination
- tool skip path
- rendering-layer corruption
- false confidence from weak evidence

What to explore:

- Which categories actually appear most often in your agents?
- Which categories deserve dedicated playbooks?
- Which categories should trigger automatic cleanup or rollback?

## 4. Evidence Maturity Model

Idea:

- rank agent answers by evidence maturity, not just whether they sound convincing

Example ladder:

1. no evidence
2. prompt-only rationale
3. indirect evidence
4. direct tool evidence
5. cross-verified evidence
6. current-turn evidence with timestamp

What to explore:

- Which answer types require which minimum evidence level?
- Which evidence levels are acceptable for low-risk vs high-risk tasks?

## 5. Prompt-to-Code Migration Map

Idea:

- explicitly track which agent behaviors still rely on prompt text and should be code-enforced

Good candidates:

- tool-required tasks
- stale-session rejection
- memory admission rules
- final answer schemas
- deterministic fallback behavior

What to explore:

- Which rules are still “prompt wishes” instead of code?
- Which failures would disappear if one rule moved into code?

## 6. Audit-to-Refactor Loop

Idea:

- every audit should produce a prioritized engineering refactor sequence

Pattern:

- finding
- root cause
- code surface
- migration risk
- owner
- verification signal

What to explore:

- How do you turn findings into tickets or PRs?
- How do you verify the fix actually removed the failure path?

## 7. Agent Review Training Kit

Idea:

- package the skill into a training kit so other operators can learn how to inspect agents well

Potential pieces:

- example bad agent incidents
- example great audits
- anti-pattern flashcards
- "spot the hidden wrapper bug" exercises

What to explore:

- Which examples would teach the most?
- Which mistakes are common enough to deserve drills?

## 8. Productization Direction

Idea:

- evolve the skill from a manual review aid into a real agent governance product

Possible components:

- audit runner
- schema validator
- score dashboards
- incident archive
- release gate integrations
- historical drift reports

What to explore:

- Which of these should remain human-led?
- Which can be automated safely?
- Which need explicit review signoff?

## 9. How To Use This File

If a user asks "how can this skill grow?" or "what should the framework become?", do not pretend the framework already exists.

Instead:

1. state that these are design directions
2. choose the most relevant direction
3. help the user sequence what to build first
4. keep recommendations concrete and realistic
