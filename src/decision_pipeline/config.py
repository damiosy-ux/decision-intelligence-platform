from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


class RuleConfigError(ValueError):
    """Raised when an external rule file is incomplete or malformed."""


def _finite_number(value: Any, path: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RuleConfigError(f"{path} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise RuleConfigError(f"{path} must be finite and non-negative")
    return number


def validate_rules(rules: Any) -> dict[str, Any]:
    """Validate the public rule schema before evaluation begins."""
    if not isinstance(rules, dict):
        raise RuleConfigError("rules must be an object")

    try:
        positive = rules["metrics"]["positive_signal"]
        suppression = rules["metrics"]["suppression_signal"]
        classification = rules["classification"]
        tie_breaking = rules["tie_breaking"]
    except (KeyError, TypeError) as exc:
        raise RuleConfigError(f"missing required rule section: {exc}") from exc

    required_numbers = {
        "metrics.positive_signal.selected_gf_min": positive.get("selected_gf_min"),
        "metrics.positive_signal.opponent_gf_max": positive.get("opponent_gf_max"),
        "metrics.suppression_signal.selected_ga_max": suppression.get("selected_ga_max"),
        "metrics.suppression_signal.opponent_ga_min": suppression.get("opponent_ga_min"),
        "tie_breaking.minimum_alignment_gap": tie_breaking.get("minimum_alignment_gap"),
    }
    for path, value in required_numbers.items():
        _finite_number(value, path)

    for score in ("0", "1", "2"):
        label = classification.get(score)
        if not isinstance(label, str) or not label.strip():
            raise RuleConfigError(f"classification.{score} must be a non-empty string")

    return rules


def load_rules(path: str | Path) -> dict[str, Any]:
    """Load and validate external rule thresholds from JSON."""
    with Path(path).open("r", encoding="utf-8") as handle:
        return validate_rules(json.load(handle))
