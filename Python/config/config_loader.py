import json
import os

CONFIG_DIR = os.path.dirname(__file__)

def load_config(filename: str) -> dict:
    """Lädt eine JSON-Konfigurationsdatei aus dem config-Ordner."""
    path = os.path.join(CONFIG_DIR, f"{filename}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


