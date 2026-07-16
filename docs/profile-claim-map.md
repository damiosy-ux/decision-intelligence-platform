# Profile Claim Map

This page maps the public repository to the engineering capabilities described in the profile. The public implementation is intentionally simplified and uses synthetic examples, but each profile claim has a visible artifact in the repo.

## Data Ingestion Architecture

Evidence:

- `src/public_event_harvest_eval.ps1`
- `docs/architecture.md`
- `README.md`

The prototype separates source feed parsing, source filtering, event-page extraction, harvest storage, and offline evaluation.

## Incremental Synchronization Workflows

Evidence:

- `docs/roadmap.md`
- `README.md`
- `docs/architecture.md`

The roadmap defines cache manifests, source timestamps, content hashes, partial-fetch recovery, and redundant-call reduction as planned synchronization components. The public code keeps this at architecture level to avoid exposing private operational playbooks.

## Dataset Normalization and Entity Resolution

Evidence:

- `src/decision_pipeline/normalizer.py`
- `src/decision_pipeline/models.py`
- `tests/test_normalizer.py`
- `docs/roadmap.md`

The Python layer converts provider-shaped sample rows into stable internal records. Entity resolution is represented in the roadmap as the next layer above normalization.

## External Rule Configuration

Evidence:

- `config/example-rules.json`
- `src/decision_pipeline/config.py`
- `scripts/run_evaluation.py`

The sample evaluator loads thresholds and classifications from a separate JSON rule file.

## Explainable Evaluation Pipelines

Evidence:

- `src/decision_pipeline/evaluator.py`
- `tests/test_evaluator.py`
- `examples/sample-output.md`

Evaluation output includes score, class, retained entity, and failed rule groups.

## Evidence Fusion and Pattern Recognition

Evidence:

- `docs/architecture.md`
- `docs/roadmap.md`
- `README.md`

The public repository documents the evidence-fusion layer and pattern-recognition role without exposing proprietary research logic or historical datasets.

## Incremental Learning and Continuous Improvement

Evidence:

- `docs/roadmap.md`
- `README.md`

The feedback-learning phase describes verified outcome ingestion, drift detection, weak-signal discovery, and recurring failure-mode analysis.

## Test Coverage and CI

Evidence:

- `tests/`
- `.github/workflows/tests.yml`
- `docs/testing.md`

The repository runs Python tests locally and through GitHub Actions on each push and pull request.
