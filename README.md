# Decision Intelligence Platform

A modular data intelligence platform for multi-source ingestion, explainable pattern recognition, and feedback-driven evaluation.

## Overview

This repository demonstrates a small but practical decision-intelligence workflow:

1. Harvest public event data from an external provider.
2. Validate source quality before evaluation.
3. Normalize raw provider fields into a consistent internal schema.
4. Store harvested records before scoring.
5. Run an offline rule engine with explainable pass/fail diagnostics.

The current implementation uses public football match data as the working case study. The architecture is intentionally broader: it can be adapted to other noisy, multi-provider datasets where inputs must be filtered, normalized, evaluated, and explained.

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
tests/      Placeholder for validation tests
```

## Current Features

- Public data harvesting
- Source and competition filtering
- HTML table extraction
- Structured data normalization
- Two-phase harvest-then-evaluate workflow
- Explainable rule outcomes
- Compact result output
- Configurable evaluation rules
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

Private methodology, production source integrations, proprietary rules, and historical research datasets are intentionally excluded from the public repository.

## Core Capabilities Demonstrated

- Multi-source data ingestion
- Incremental synchronization workflows
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
