from __future__ import annotations

import argparse
import json
from pathlib import Path

from decision_pipeline import evaluate_records, normalize_records
from decision_pipeline.config import load_rules


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the sample decision-intelligence evaluator.")
    parser.add_argument("--rules", default="config/example-rules.json")
    parser.add_argument("--input", default="examples/sample-harvest.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rules = load_rules(args.rules)

    with Path(args.input).open("r", encoding="utf-8") as handle:
        raw_records = json.load(handle)

    records = normalize_records(raw_records)
    results = evaluate_records(records, rules)

    print(f"records={len(records)} results={len(results)}")
    for result in results:
        failed = ",".join(result.failed_rules)
        print(
            f"{result.fixture} | {result.side} | {result.entity} | "
            f"{result.score} | {result.classification} | {failed}"
        )


if __name__ == "__main__":
    main()
