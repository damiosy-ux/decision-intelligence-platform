# Architecture

This project separates source collection from evaluation so that every output can be inspected and explained.

## Pipeline

```text
Provider feed
  -> competition/source filter
  -> event page fetch
  -> table extraction
  -> normalized harvest record
  -> offline evaluation
  -> explainable result
```

## Design Principles

- Harvest first, evaluate second.
- Reject unverifiable or low-quality source contexts before scoring.
- Keep provider-specific parsing isolated from evaluation logic.
- Return failed rules with every retained result.
- Prefer small, transparent rules over opaque scoring.

## Case Study

The current implementation uses public football event pages because they provide noisy, semi-structured data, changing schedules, and inconsistent competition metadata. These are useful stress tests for a broader decision-intelligence pipeline.
