# ClawHub Publish Notes

Use this file when preparing `oh-my-agent-check` for distribution outside the current repository.

## Goal

Prepare a package that is:

- self-contained
- easy to inspect
- safe to distribute

## Minimum Package

Keep:

- `SKILL.md`
- `agents/openai.yaml`
- `references/report-schema.json`
- `references/rubric.md`
- `references/playbooks.md`
- `references/advanced-playbooks.md`
- `references/trigger-prompts.md`
- `references/example-report.json`
- `references/framework-directions.md`
- `references/governance-framework.md`
- icon assets

## Release Checklist

Before packaging:

1. confirm frontmatter is accurate
2. confirm `openai.yaml` matches the current positioning
3. confirm all referenced files actually exist
4. confirm examples and prompts do not overclaim unimplemented features
5. confirm there are no repo-specific secrets or internal-only assumptions

## Packaging Advice

Recommended deliverables:

- clean git repo
- `.zip` package without `.git`
- one README with:
  - what the skill audits
  - how it works
  - example prompts

## Publishing Advice

When publishing to any distribution channel:

- lead with the pain:
  - "base model is fine, wrapper is broken"
- lead with the differentiator:
  - JSON-first, evidence-backed, no-mercy audit
- show one example report
- show one trigger prompt

## What Not To Say

Do not claim:

- that the skill automatically fixes everything
- that every framework direction is already implemented
- that the package includes product-grade automation when it is still a guided audit skill
