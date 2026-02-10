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

Or (uses port 5001 from config):

```bash
.venv/bin/python app.py
```

Then open **http://127.0.0.1:5001**. Port 5001 avoids conflict with macOS AirPlay on 5000.

**Stop the app:** In the terminal where Flask is running, press **Ctrl+C**.

## Run with Docker

**Build:**

```bash
docker build -t flash-card .
```

**Run:**

```bash
docker run -p 5001:5001 flash-card
```

Then open **http://127.0.0.1:5001**. For production, pass a secret: `docker run -p 5001:5001 -e SECRET_KEY=your-secret flash-card`.

For structure, routes, and conventions, see [docs/AI-SPEC.md](docs/AI-SPEC.md).
