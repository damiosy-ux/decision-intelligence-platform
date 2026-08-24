import json

import pytest

from decision_pipeline.config import RuleConfigError, load_rules, validate_rules


def valid_rules():
    return {
        "metrics": {
            "positive_signal": {"selected_gf_min": 2.0, "opponent_gf_max": 1.3},
            "suppression_signal": {"selected_ga_max": 1.3, "opponent_ga_min": 2.0},
        },
        "classification": {"2": "high", "1": "lean", "0": "skip"},
        "tie_breaking": {"minimum_alignment_gap": 1.0},
    }


def test_load_rules_validates_external_json(tmp_path):
    path = tmp_path / "rules.json"
    path.write_text(json.dumps(valid_rules()), encoding="utf-8")

    assert load_rules(path)["classification"]["2"] == "high"


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda rules: rules.pop("metrics"), "missing required rule section"),
        (
            lambda rules: rules["metrics"]["positive_signal"].update(
                {"selected_gf_min": "not-a-number"}
            ),
            "must be numeric",
        ),
        (
            lambda rules: rules["tie_breaking"].update(
                {"minimum_alignment_gap": float("nan")}
            ),
            "finite and non-negative",
        ),
        (lambda rules: rules["classification"].update({"1": ""}), "non-empty string"),
    ],
)
def test_validate_rules_rejects_malformed_configuration(mutate, message):
    rules = valid_rules()
    mutate(rules)

    with pytest.raises(RuleConfigError, match=message):
        validate_rules(rules)
