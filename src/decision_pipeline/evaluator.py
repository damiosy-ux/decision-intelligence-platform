from __future__ import annotations

from .models import EntityMetrics, EvaluationResult, HarvestRecord


def _classification(score: int, rules: dict) -> str:
    labels = rules.get("classification", {})
    return labels.get(str(score), "skip")


def _alignment_distance(selected: EntityMetrics, opponent: EntityMetrics, rules: dict) -> float:
    positive = rules["metrics"]["positive_signal"]
    suppression = rules["metrics"]["suppression_signal"]

    return (
        abs(selected.l3_gf - positive["selected_gf_min"])
        + abs(selected.l10_gf - positive["selected_gf_min"])
        + abs(opponent.l3_gf - positive["opponent_gf_max"])
        + abs(opponent.l10_gf - positive["opponent_gf_max"])
        + abs(selected.l3_ga - suppression["selected_ga_max"])
        + abs(selected.l10_ga - suppression["selected_ga_max"])
        + abs(opponent.l3_ga - suppression["opponent_ga_min"])
        + abs(opponent.l10_ga - suppression["opponent_ga_min"])
    )


def evaluate_selection(
    record: HarvestRecord,
    side: str,
    selected: EntityMetrics,
    opponent: EntityMetrics,
    rules: dict,
) -> EvaluationResult | None:
    """Evaluate one side with intentionally simple, explainable rule groups."""
    positive = rules["metrics"]["positive_signal"]
    suppression = rules["metrics"]["suppression_signal"]

    positive_signal = (
        selected.l3_gf >= positive["selected_gf_min"]
        and selected.l10_gf >= positive["selected_gf_min"]
        and opponent.l3_gf <= positive["opponent_gf_max"]
        and opponent.l10_gf <= positive["opponent_gf_max"]
    )

    suppression_signal = (
        selected.l3_ga <= suppression["selected_ga_max"]
        and selected.l10_ga <= suppression["selected_ga_max"]
        and opponent.l3_ga >= suppression["opponent_ga_min"]
        and opponent.l10_ga >= suppression["opponent_ga_min"]
    )

    score = int(positive_signal) + int(suppression_signal)
    if score == 0:
        return None

    passed_rules: list[str] = []
    failed_rules: list[str] = []
    if positive_signal:
        passed_rules.append("positive_signal")
    else:
        failed_rules.append("positive_signal")
    if suppression_signal:
        passed_rules.append("suppression_signal")
    else:
        failed_rules.append("suppression_signal")

    return EvaluationResult(
        fixture=record.fixture,
        side=side,
        entity=selected.entity,
        score=score,
        classification=_classification(score, rules),
        passed_rules=tuple(passed_rules),
        failed_rules=tuple(failed_rules) or ("-",),
        alignment_distance=_alignment_distance(selected, opponent, rules),
    )


def choose_result(
    home: EvaluationResult | None,
    away: EvaluationResult | None,
    rules: dict,
) -> EvaluationResult | None:
    if home and not away:
        return home
    if away and not home:
        return away
    if not home or not away:
        return None

    if home.score > away.score:
        return home
    if away.score > home.score:
        return away

    minimum_gap = rules["tie_breaking"]["minimum_alignment_gap"]
    gap = abs(home.alignment_distance - away.alignment_distance)
    if gap < minimum_gap:
        return None

    return min((home, away), key=lambda result: result.alignment_distance)


def evaluate_records(records: list[HarvestRecord], rules: dict) -> list[EvaluationResult]:
    results: list[EvaluationResult] = []

    for record in records:
        home = evaluate_selection(record, "Home", record.home, record.away, rules)
        away = evaluate_selection(record, "Away", record.away, record.home, rules)
        chosen = choose_result(home, away, rules)
        if chosen:
            results.append(chosen)

    return sorted(results, key=lambda result: (-result.score, result.fixture))
