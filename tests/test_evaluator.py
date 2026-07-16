from decision_pipeline.evaluator import evaluate_records
from decision_pipeline.normalizer import normalize_records


def test_evaluator_retains_explainable_result():
    rules = {
        "metrics": {
            "positive_signal": {"selected_gf_min": 2.0, "opponent_gf_max": 1.3},
            "suppression_signal": {"selected_ga_max": 1.3, "opponent_ga_min": 2.0},
        },
        "classification": {"2": "high_confidence", "1": "lean", "0": "skip"},
        "tie_breaking": {"minimum_alignment_gap": 1.0},
    }
    records = normalize_records(
        [
            {
                "fixture": "Example Alpha vs Example Beta",
                "competition": "Example League",
                "home": {
                    "entity": "Example Alpha",
                    "l3_gf": 2.2,
                    "l3_ga": 1.1,
                    "l10_gf": 2.1,
                    "l10_ga": 1.2,
                },
                "away": {
                    "entity": "Example Beta",
                    "l3_gf": 1.0,
                    "l3_ga": 2.3,
                    "l10_gf": 1.2,
                    "l10_ga": 2.1,
                },
            }
        ]
    )

    results = evaluate_records(records, rules)

    assert len(results) == 1
    assert results[0].entity == "Example Alpha"
    assert results[0].score == 2
    assert results[0].classification == "high_confidence"
    assert results[0].failed_rules == ("-",)
