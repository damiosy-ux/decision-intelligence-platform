import pytest

from decision_pipeline.normalizer import RecordValidationError
from decision_pipeline.normalizer import normalize_records


def test_normalizer_converts_raw_rows_to_internal_records():
    records = normalize_records(
        [
            {
                "fixture": "Example Alpha vs Example Beta",
                "competition": "Example League",
                "home": {
                    "entity": "Example Alpha",
                    "l3_gf": "2.4",
                    "l3_ga": "1.1",
                    "l10_gf": "2.1",
                    "l10_ga": "1.2",
                },
                "away": {
                    "entity": "Example Beta",
                    "l3_gf": "1.0",
                    "l3_ga": "2.3",
                    "l10_gf": "1.2",
                    "l10_ga": "2.1",
                },
            }
        ]
    )

    assert records[0].home.entity == "Example Alpha"
    assert records[0].home.l3_gf == 2.4
    assert records[0].away.l10_ga == 2.1


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("l3_gf", None, "must be numeric"),
        ("l3_ga", "not-a-number", "must be numeric"),
        ("l10_gf", -0.1, "finite, non-negative"),
        ("l10_ga", float("nan"), "finite, non-negative"),
    ],
)
def test_normalizer_rejects_invalid_metrics(field, value, message):
    raw = {
        "fixture": "Example Alpha vs Example Beta",
        "competition": "Example League",
        "home": {
            "entity": "Example Alpha",
            "l3_gf": 2.0,
            "l3_ga": 1.0,
            "l10_gf": 2.0,
            "l10_ga": 1.0,
        },
        "away": {
            "entity": "Example Beta",
            "l3_gf": 1.0,
            "l3_ga": 2.0,
            "l10_gf": 1.0,
            "l10_ga": 2.0,
        },
    }
    raw["home"][field] = value

    with pytest.raises(RecordValidationError, match=message):
        normalize_records([raw])


def test_normalizer_rejects_incomplete_evidence():
    raw = {
        "fixture": "Example Alpha vs Example Beta",
        "competition": "Example League",
        "home": {
            "entity": "Example Alpha",
            "l3_gf": 2.0,
            "l3_ga": 1.0,
            "l10_gf": 2.0,
            "l10_ga": 1.0,
        },
    }

    with pytest.raises(RecordValidationError, match=r"record\[0\]\.away"):
        normalize_records([raw])
