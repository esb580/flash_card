"""Load topic decks from JSON files. Used by the Flask app."""
import json
from pathlib import Path

from config import TOPICS_DIR


def load_topics():
    """Return list of topic dicts: {topic, title, cards} from topics/*.json."""
    topics = []
    if not TOPICS_DIR.exists():
        return topics
    for path in sorted(TOPICS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if "topic" in data and "title" in data and "cards" in data:
                topics.append(data)
        except (json.JSONDecodeError, OSError):
            continue
    return topics


def get_topic(topic_id: str):
    """Return one topic dict by topic id, or None."""
    path = TOPICS_DIR / f"{topic_id}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if "topic" in data and "title" in data and "cards" in data:
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return None
