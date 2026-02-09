# AI spec — Flash Card learning aid

This file tells the AI (and you) what the project is and how to work on it. Keep it updated as the app grows. Read this first when starting a new session or adding features.

---

## What this app is

A small learning-aid app: flash cards in the browser. User picks a topic (deck), sees one card at a time, reveals the answer, then goes to the next card. Python 3 + Flask backend; topic data is JSON files in `topics/`. No database, no auth, no spaced repetition yet—scope is deliberately small so it’s easy to maintain and extend.

---

## Tech stack

- **Backend:** Python 3, Flask. JSON only (stdlib); no DB yet.
- **Frontend:** Server-rendered HTML (Jinja2), one CSS file, minimal inline JS for reveal/hide. No build step, no SPA.
- **Data:** One JSON file per topic in `topics/` (see Topics below).
- **Run:** `.venv` + `requirements.txt`; dev server on port 5001 (5000 often used by macOS AirPlay).

---

## Frontend choices and how it works

- **Flask** serves all pages. Routes: `/` (topic list), `/study/<topic_id>` (one card), `/study/<topic_id>/next` (advance and redirect).
- **Session** holds `topic_id` and `card_index` so “Next card” moves through the deck; switching topic resets index.
- **UI:** Sky blue page background (`#87ceeb`). Card is 5"×3" landscape (480×288px), white with CSS-only ruled lines (repeating gradient). Buttons (Reveal answer / Next card) at bottom of card, centered. Reveal is client-side (JS toggles `.hidden` on the answer div).
- **Port:** Use 5001 so the app doesn’t conflict with macOS AirPlay on 5000.

---

## Directory and file layout (ASCII)

```
flash_card/
  app.py                 # Flask app: routes /, /study/<id>, /study/<id>/next
  config.py              # TOPICS_DIR, SECRET_KEY (env or defaults)
  load_topics.py         # load_topics(), get_topic(id) — reads topics/*.json
  requirements.txt       # flask (only dependency so far)
  .venv/                 # Virtual env (do not commit)
  .gitignore

  templates/             # Jinja2 HTML
    base.html            # Layout: <main>, block content, CSS link
    index.html           # Topic list (links to /study/<topic_id>)
    study.html           # One card: question, answer (hidden until reveal), buttons

  static/
    css/
      style.css          # Global + card: sky blue bg, 5×3 card, ruled lines, buttons

  topics/                # One JSON file per deck
    ai-learning.json     # topic, title, cards[{ id, question, answer }]

  docs/
    AI-SPEC.md           # This file
  .cursor/
    rules/               # Cursor project rules (project-context.mdc, tone.mdc)
  README.md
```

---

## Flask app: what you need to maintain it

**Entry point:** `app.py`. Run with:
`flask --app app run --host=127.0.0.1 --port=5001`
(or from repo root: `.venv/bin/flask --app app run --host=127.0.0.1 --port=5001`)

**Config:** `config.py` reads env: `FLASH_CARD_TOPICS` (default: repo `topics/`), `SECRET_KEY` (for session cookie). Override for different data dir or production.

**Data flow:** `load_topics()` returns all decks from `topics/*.json`. `get_topic(topic_id)` loads `topics/<topic_id>.json`. Each deck must have `topic`, `title`, `cards`; each card has `id`, `question`, `answer`.

**Routes:**
- `GET /` — Index: list topics, link each to `/study/<topic_id>`.
- `GET /study/<topic_id>` — Show one card. Session keeps `topic_id` and `card_index`; card is `cards[card_index]`. Template gets `topic_id`, `topic_title`, `card`, `card_num`, `total`.
- `GET /study/<topic_id>/next` — Increment `session["card_index"]`, redirect to `study(topic_id)`. Index wraps at end of deck.

**Templates:** `base.html` defines layout and `{% block content %}`. `index.html` and `study.html` extend it. Study page has a small inline script to toggle the answer visibility (no separate JS file).

**Adding a feature:** New route in `app.py`, new template in `templates/` if needed, link from existing page or add URL. New topic = new JSON in `topics/` with same shape.

---

## Topics (flash card data)

Decks live in `topics/` as one JSON file per topic. Structure: `topic` (slug, used in URL and filename), `title` (display name), `cards` (array). Each card: `id` (kebab-case slug, unique in file), `question`, `answer`. Example: `topics/ai-learning.json`. Add new topics by adding a new JSON file with the same shape; the app picks them up automatically.

---

## Conventions

- **Python:** Python 3 style, type hints where helpful. Use the repo `.venv` and `requirements.txt`.
- **Docs:** This file is the source of truth for structure and behavior. README stays short (what it is, how to run).
- **Cursor vs app:** `.cursor/` is editor/AI config only. The app runs without Cursor; code and `topics/` are portable.

---

## Working with Cursor

- **Assume:** The user is using Cursor for this project (so answers can refer to Cursor UI, terminal, Keep/Accept, etc.).
- **Rules** (`.cursor/rules/*.mdc`) point the AI at this spec and set tone.
- **Modes:** Plan for multi-step or architectural changes; Agent for small edits and features.
- **Bootstrap for a new session:** This app is a minimal flash card study UI. Backend is Flask + JSON in `topics/`. Frontend is server-rendered HTML + one CSS file + minimal JS. To add a feature: add a route in `app.py`, optional new template, optional new topic JSON. No DB or auth yet.

---

## How to use this spec

- **You:** Update this file when the app’s purpose, stack, layout, or key flows change.
- **AI:** Read this file first; follow the structure and conventions. Prefer small, clear steps. Use port 5001 for the dev server.
