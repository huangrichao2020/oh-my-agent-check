# Governance Framework

Use this file when the user wants to turn repeated audits into an internal standard, review lane, or operating system for agent quality.

This is not a claim that the framework is already implemented.  
Treat it as a map for what to build next.

## 1. Release Gates

Possible gate families:

- tool-discipline gate
- memory-hygiene gate
- rendering-transport gate
- hidden-layer gate
- stale-evidence gate

Questions to force:

- What must never ship?
- What may ship behind a flag?
- What requires human signoff?

## 2. Layer Scorecards

Candidate scorecard dimensions:

- context cleanliness
- evidence integrity
- tool discipline
- stale-state resistance
- fallback transparency
- rendering stability
- prompt-to-code maturity

Possible scales:

- pass / warn / fail
- 1 to 5
- green / yellow / red

## 3. Incident Archive

Create a persistent archive of:

- incident title
- user-visible symptom
- root cause layer
- contamination path
- fix applied
- verification status

Goal:

- stop rediscovering the same failures

## 4. Evidence Ladder

Suggested maturity order:

1. prompt-only belief
2. weak indirect clue
3. single probe
4. direct tool evidence
5. multi-source confirmation
6. fresh current-turn evidence with timestamp

Use this to define minimum evidence requirements by task type.

## 5. Prompt-to-Code Migration Board

Maintain an explicit inventory:

- what is still prompt-enforced
- what is partially code-enforced
- what is fully code-enforced

Good candidates to migrate first:

- required tool use
- stale-state rejection
- memory admission
- distillation admission
- final answer schemas
- deterministic fallback

## 6. Audit Program

Move from one-off review to scheduled review:

- pre-release audits
- post-incident audits
- monthly contamination audits
- quarterly architecture reviews

## 7. Training Kit

Package the framework for humans:

- example bad incidents
- example strong audit reports
- anti-pattern flashcards
- "spot the hidden wrapper bug" exercises

## 8. What To Build First

If a team wants to adopt this framework, the recommended first build order is:

1. release gates
2. incident archive
3. prompt-to-code migration board
4. evidence ladder
5. scorecards
