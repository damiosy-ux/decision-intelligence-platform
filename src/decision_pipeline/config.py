from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_rules(path: str | Path) -> dict[str, Any]:
    """Load external rule thresholds from JSON."""
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)
