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

## Repository Structure

```text
src/        Core ingestion and evaluation scripts
docs/       Architecture and workflow notes
examples/   Example output formats
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

## Current Status

Early-stage research prototype.

## Goal

To build a reusable decision-intelligence framework that supports pattern recognition, explainable evaluation, and continuous learning across noisy real-world datasets.
