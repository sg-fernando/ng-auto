import json
from pathlib import Path

def get_secrets():
    p = Path("secrets.json")
    if not p.exists():
        raise SystemExit("secrets.json missing")

    with p.open() as f:
        data = json.load(f)

    return data
