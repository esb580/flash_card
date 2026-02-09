"""App configuration. Load from env or defaults."""
import os
from pathlib import Path

# Path to topics directory (JSON decks)
TOPICS_DIR = Path(os.environ.get("FLASH_CARD_TOPICS", Path(__file__).parent / "topics"))
# Secret key for Flask session (change in production)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")
