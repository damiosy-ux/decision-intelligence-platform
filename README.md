# Decision Intelligence Platform

A modular data intelligence platform for multi-source ingestion, explainable pattern recognition, and feedback-driven evaluation.

## Overview

This repository demonstrates a small but practical decision-intelligence workflow:

1. Ingest event data through an abstract source boundary.
2. Validate source quality before evaluation.
3. Normalize raw provider fields into a consistent internal schema.
4. Store harvested records before scoring.
5. Run an offline rule engine with explainable pass/fail diagnostics.

The public implementation uses synthetic event records. Its architecture can be adapted to noisy, multi-source datasets where inputs must be filtered, normalized, evaluated, and explained.

## Why This Matters

Many analytical systems fail because they mix data collection, cleaning, scoring, and decision output into one opaque process. This project separates those stages so each decision can be traced back to the harvested evidence.

## Architecture

```text
Public Data Sources
    -> Ingestion Layer
    -> Competition / Source Filter
    -> Normalization + Validation
    -> Harvested Dataset
    -> Offline Evaluation Engine
    -> Explainable Output
    -> Outcome Feedback Loop
```

## Architecture Summary

```text
Data Providers
      |
      v
Incremental Harvest
      |
      v
Normalization & Entity Resolution
      |
      v
Unified Knowledge Base
      |
      +-- Pattern Recognition
      +-- Evidence Fusion
      +-- Explainable Evaluation
      +-- Post-Event Learning
             |
             v
Continuous Knowledge Improvement
```

## Repository Structure

```text
src/        Core ingestion and evaluation scripts
scripts/    Command-line entry points
docs/       Architecture and workflow notes
examples/   Example output formats
config/     Example rule and threshold configuration
data/       Local runtime data folder, ignored by git
tests/      Validation, configuration, and evaluation tests
```

## Current Features

- Source-agnostic ingestion contracts
- Structured data normalization
- Two-phase harvest-then-evaluate workflow
- Explainable rule outcomes
- Explicit passed-rule and failed-rule diagnostics
- Compact result output
- Configurable evaluation rules
- Fail-fast external rule configuration validation
- Synthetic sample harvest records
- Python evaluation package with tests

## Current Status

Early-stage research prototype with a public reference implementation.

The repository currently includes:

- a synthetic Python evaluation package
- externalized example rules
- unit tests
- GitHub Actions CI
- architecture notes
- roadmap documentation
- public-scope safeguards
- a claim map linking profile language to visible artifacts
- dated status snapshots that document current public-safe progress

Private methodology, production source integrations, proprietary rules, and historical research datasets are intentionally excluded from the public repository.

Recent research direction: domain-specific decision workflows are being developed privately as case studies in evidence harvesting, slice-based comparison, explainable diagnostics, and post-event learning. The public repository documents the reusable architecture while keeping proprietary thresholds, provider-specific mechanics, and private datasets out of scope.

Current public update as of 2026-07-29: the repository now makes the public/private boundary more explicit for the draw-intelligence research direction. Public materials demonstrate architecture, normalization, configurable examples, explainable diagnostics, tests, and CI while excluding production provider logic, private data, scoring thresholds, and operational methods.

Current engine correction update as of 2026-08-24: the public reference engine now validates external configuration before evaluation, rejects ambiguous tied candidates deterministically, reports both passed and failed rule groups, and treats rule scores as eligibility signals rather than calibrated probabilities. Private formulas, provider mechanics, operational automation, and proprietary thresholds remain excluded.

Current public-safety update as of 2026-08-31: production harvesting integrations have been removed from the public tree, classification labels now describe evidence strength rather than implied probability, and public examples remain entirely synthetic. No private datasets, credentials, machine paths, provider endpoints, or operational scoring logic are included.

Current documentation update as of 2026-09-04: public claims, roadmap items, and progress records now match the source-agnostic implementation. Rule-group scores remain evidence labels; percentage confidence requires separate outcome calibration and is not inferred from thresholds.

## Core Capabilities Demonstrated

- Source-agnostic ingestion design
- Incremental synchronization workflows
- Harvest-before-evaluate workflow design
- Evidence completeness validation
- Dataset normalization and entity resolution
- Configurable evaluation rules
- Explainable evaluation pipelines
- Pattern recognition and evidence fusion
- Synthetic sample datasets
- Automated Python testing
- GitHub Actions continuous integration

See:

- `docs/architecture.md`
- `docs/roadmap.md`
- `docs/usage.md`
- `docs/testing.md`
- `docs/public-scope.md`
- `docs/profile-claim-map.md`
- `docs/progress.md`
- `docs/status-2026-07-18.md`
- `docs/status-2026-07-26.md`
- `docs/status-2026-07-28.md`
- `docs/status-2026-07-29.md`
- `docs/status-2026-08-09.md`
- `docs/status-2026-08-14.md`
- `docs/status-2026-08-24.md`
- `docs/status-2026-08-31.md`
- `docs/status-2026-09-04.md`
- `config/example-rules.json`
- `examples/sample-harvest.json`

## Python Quick Start

Run the synthetic example evaluator:

```powershell
$env:PYTHONPATH = "src"
python .\scripts\run_evaluation.py
```

Run tests:

```powershell
$env:PYTHONPATH = "src"
python -m pytest
```

The Python implementation intentionally uses synthetic input records. This keeps the public repository focused on architecture, normalization, and explainable evaluation without exposing private source-specific workflows.

## Public Scope

This repository is a simplified reference implementation. It uses synthetic examples and generic rules to demonstrate architecture while keeping private datasets, provider-specific playbooks, and deeper research methodology out of the public codebase.

## Goal

To build a reusable decision-intelligence framework that supports pattern recognition, explainable evaluation, and continuous learning across noisy real-world datasets.
