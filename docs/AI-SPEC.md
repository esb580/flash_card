# AI spec — Flash Card learning aid

This file tells the AI (and you) what the project is and how to work on it. Keep it updated as the app grows.

---

## What this app is

A learning-aid app: flash cards. Python 3 backend; maybe a database later. For now we're defining structure and docs before adding a venv, git, or real code.

---

## Tech stack (current / planned)

- **Language:** Python 3
- **Data:** TBD (maybe SQLite or similar later)
- **Frontend:** TBD (basic HTML/CSS to start, or CLI)
- **AI use:** This repo is structured so Cursor (and other AI tools) can reason about layout, conventions, and where to put new code.

---

## Directory structure

```
flash_card/
  README.md           # Human-facing overview, how to run (once we have runnable app)
  docs/
    AI-SPEC.md        # This file — project context for AI
  .cursor/
    rules/            # Project rules (.mdc) — project-context.mdc, tone.mdc
  topics/             # Flash card decks per topic (e.g. ai-learning.json)
  # Later (we add when ready):
  # src/ or app/      # Python package
  # tests/
```

The AI should put new code and docs in the right place based on this. If we add a `src/` or `app/` later, we’ll say so here.

---

## Topics (flash card data)

Decks live in `topics/` as one JSON file per topic. Structure: `topic` (slug), `title` (display name), `cards` (array). Each card: `id` (kebab-case slug, unique in file), `question`, `answer`. Example file: `topics/ai-learning.json`. Add new topics with the same shape.

---

## Conventions

- **Python:** Prefer Python 3 style (type hints when helpful, clear names). We’ll add a venv and dependency list when we start coding.
- **Docs:** One main source of truth for “what the project is” → `docs/AI-SPEC.md`. README stays short (what it is, how to run).
- **Scope for now:** Structure and this spec only. No venv, git, or implementation until we’re happy with the layout.
- **Cursor vs app:** The `.cursor/` folder (rules, optional skills) is Cursor-only editor config. It does not run with the app. The app (code, `topics/`, future backend) is portable and runs anywhere; Cursor is not required at runtime.

---

## Working with Cursor

- **Rules** (`.cursor/rules/*.mdc`) ensure this spec is applied; they point the AI at AI-SPEC and set tone. They are Cursor-specific.
- **Skills** (if we add any) would go in `.cursor/skills/` for task workflows (e.g. how to generate commit messages); different from rules, which shape general behavior.
- **Modes:** Use Plan mode for multi-step or architectural work (plan first, then execute); use Agent for direct implementation or small edits.

---

## How to use this spec

- **You:** Edit this file when the app’s purpose, stack, or layout changes.
- **AI:** Read this file first when working in this repo; follow the structure and conventions above. Prefer small, clear steps.

We can add sections later (e.g. “Key user flows”, “API shape”, “Database schema”) as the app takes shape.
