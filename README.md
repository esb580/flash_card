# Flash Card

A small learning-aid app: flash cards in the browser. Pick a topic, see a question, reveal the answer, next card. Python 3 + Flask; topic decks are JSON in `topics/`.

**Version:** 0.1.0  
**Author:** Phil

## Run locally

**First-time setup:**

```bash
cd /path/to/flash_card
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

**Start the app:**

```bash
cd /path/to/flash_card
.venv/bin/flask --app app run --host=127.0.0.1 --port=5001
```

Then open **http://127.0.0.1:5001**. (Port 5001 avoids conflict with macOS AirPlay on 5000.)

**Stop the app:** In the terminal where Flask is running, press **Ctrl+C**.

For structure, routes, and conventions, see [docs/AI-SPEC.md](docs/AI-SPEC.md).
