from __future__ import annotations

import math

from .models import EntityMetrics, HarvestRecord


class RecordValidationError(ValueError):
    """Raised when a harvested record is incomplete or invalid."""


def _required_text(raw: dict, field: str, context: str) -> str:
    try:
        value = str(raw[field]).strip()
    except KeyError as exc:
        raise RecordValidationError(f"{context}.{field} is required") from exc

    if not value:
        raise RecordValidationError(f"{context}.{field} must not be blank")
    return value


def _required_metric(raw: dict, field: str, context: str) -> float:
    try:
        value = float(raw[field])
    except KeyError as exc:
        raise RecordValidationError(f"{context}.{field} is required") from exc
    except (TypeError, ValueError) as exc:
        raise RecordValidationError(f"{context}.{field} must be numeric") from exc

    if not math.isfinite(value) or value < 0:
        raise RecordValidationError(
            f"{context}.{field} must be a finite, non-negative number"
        )
    return value


def _metrics(raw: dict, context: str) -> EntityMetrics:
    if not isinstance(raw, dict):
        raise RecordValidationError(f"{context} must be an object")

    return EntityMetrics(
        entity=_required_text(raw, "entity", context),
        l3_gf=_required_metric(raw, "l3_gf", context),
        l3_ga=_required_metric(raw, "l3_ga", context),
        l10_gf=_required_metric(raw, "l10_gf", context),
        l10_ga=_required_metric(raw, "l10_ga", context),
    )


def normalize_records(raw_records: list[dict]) -> list[HarvestRecord]:
    """Convert provider-shaped sample rows into stable internal records."""
    records: list[HarvestRecord] = []

    for index, raw in enumerate(raw_records):
        context = f"record[{index}]"
        if not isinstance(raw, dict):
            raise RecordValidationError(f"{context} must be an object")

        records.append(
            HarvestRecord(
                fixture=_required_text(raw, "fixture", context),
                competition=_required_text(raw, "competition", context),
                home=_metrics(raw.get("home"), f"{context}.home"),
                away=_metrics(raw.get("away"), f"{context}.away"),
            )
        )

    return records
