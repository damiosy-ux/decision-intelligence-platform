from __future__ import annotations

from .models import EntityMetrics, HarvestRecord


def _metrics(raw: dict) -> EntityMetrics:
    return EntityMetrics(
        entity=str(raw["entity"]),
        l3_gf=float(raw["l3_gf"]),
        l3_ga=float(raw["l3_ga"]),
        l10_gf=float(raw["l10_gf"]),
        l10_ga=float(raw["l10_ga"]),
    )


def normalize_records(raw_records: list[dict]) -> list[HarvestRecord]:
    """Convert provider-shaped sample rows into stable internal records."""
    records: list[HarvestRecord] = []

    for raw in raw_records:
        records.append(
            HarvestRecord(
                fixture=str(raw["fixture"]),
                competition=str(raw["competition"]),
                home=_metrics(raw["home"]),
                away=_metrics(raw["away"]),
            )
        )

    return records
