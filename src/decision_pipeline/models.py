from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EntityMetrics:
    entity: str
    l3_gf: float
    l3_ga: float
    l10_gf: float
    l10_ga: float


@dataclass(frozen=True)
class HarvestRecord:
    fixture: str
    competition: str
    home: EntityMetrics
    away: EntityMetrics


@dataclass(frozen=True)
class EvaluationResult:
    fixture: str
    side: str
    entity: str
    score: int
    classification: str
    passed_rules: tuple[str, ...]
    failed_rules: tuple[str, ...]
    alignment_distance: float
